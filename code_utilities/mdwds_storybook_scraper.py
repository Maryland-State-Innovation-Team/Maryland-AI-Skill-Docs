"""
mdwds_storybook_scraper.py — Playwright crawler + Bedrock Claude pipeline

Phase 1: Discover all story/docs URLs from the Storybook sidebar (deterministic).
Phase 2: Scrape each page with Playwright — text, headings, and code blocks.
Phase 3: Per-page extraction — Claude (Haiku) reads each page and extracts:
           key information, detailed implementation, and summarized context.
Phase 4: Synthesis — Claude (Sonnet) reads all per-page summaries and writes
           an introduction and cross-cutting pattern analysis.
Phase 5: Assembly — programmatically build the final document:
           [synthesis intro] + [each page extraction, sorted by category]

The split between per-page extraction and holistic synthesis means:
  - Each extraction call is focused (no noise from other components).
  - The synthesis has a compact, structured view of the whole system.
  - The final document is predictable and easy to re-generate or diff.
  - Caches at both the scrape and extraction layers — iterate fast.

Requirements: pip install playwright anthropic python-dotenv pydantic
              playwright install chromium
"""

import asyncio
import json
import os
import re
import sys
from datetime import datetime
from urllib.parse import urlparse, parse_qs

import anthropic
from dotenv import load_dotenv
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
from pydantic import BaseModel, Field

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

# --- Configuration ---
STORYBOOK_URL = "https://designsystem.maryland.gov/"
OUTPUT_FILE = "mdwds_skill_document.md"
SCRAPE_CACHE = "code_utilities/mdwds_scraped_pages.json"
EXTRACTION_CACHE = "code_utilities/mdwds_extracted_pages.json"

# Haiku for per-page extraction (fast, cheap, focused task)
EXTRACTION_MODEL = "us.anthropic.claude-haiku-4-5-20251001-v1:0"
# Sonnet for holistic synthesis. Note: "[1m]" in settings.json is Claude Code's
# internal notation — not a valid Bedrock model ID. Use the plain cross-region ID.
SYNTHESIS_MODEL = "us.anthropic.claude-sonnet-4-6"

EXTRACTION_CONCURRENCY = 5   # parallel Bedrock calls during extraction
PAGE_TIMEOUT = 25_000        # ms — navigation timeout
PAGE_SETTLE_MS = 1_500       # ms — extra settle time after navigation
CRAWL_DELAY_S = 0.5          # seconds — polite delay between pages
MAX_CHARS_PER_PAGE = 6_000   # cap raw scraped content per page

# Category display order in the final document
CATEGORY_ORDER = [
    "Getting Started",
    "Foundation",
    "Components",
    "Templates",
    "Utilities",
    "Other",
]


# ── Data model for per-page extraction ───────────────────────────────────────

class PageExtraction(BaseModel):
    component_name: str = Field(
        ..., description="Display name of the component or section (e.g. 'Accordion', 'Colors')"
    )
    category: str = Field(
        ...,
        description=(
            "One of: Getting Started, Foundation, Components, Templates, Utilities, Other"
        ),
    )
    summary: str = Field(
        ...,
        description="2-3 sentences: what this is, what problem it solves, when to use it.",
    )
    key_information: str = Field(
        ...,
        description=(
            "Markdown text covering: variants, modifiers, options, CSS class names, "
            "required attributes, and any important facts an LLM needs to know."
        ),
    )
    implementation: str = Field(
        ...,
        description=(
            "Markdown with fenced HTML code blocks. Show the correct structure, "
            "all required class names, ARIA roles/attributes, and any JS initialization. "
            "Include multiple variants if they differ structurally."
        ),
    )
    context: str = Field(
        ...,
        description=(
            "1-2 sentences: how this fits into the broader MDWDS system, "
            "how it composes with other components, or patterns it shares."
        ),
    )


# ── Routing helper ────────────────────────────────────────────────────────────

async def _route_handler(route):
    if route.request.resource_type in ("image", "font", "media"):
        await route.abort()
    else:
        await route.continue_()


# ── Phase 1: Discover URLs ────────────────────────────────────────────────────

async def discover_story_urls(page) -> list[dict]:
    """
    Extract all ?path= links from the Storybook sidebar.
    Storybook lazily renders sidebar items — we must click every expand button
    to reveal nested story/docs links before collecting hrefs.
    """
    print("Phase 1: Discovering story URLs from sidebar...")
    await page.goto(STORYBOOK_URL, wait_until="networkidle", timeout=PAGE_TIMEOUT)
    await page.wait_for_timeout(2_000)

    # Expand all collapsed sidebar groups by clicking their toggle buttons.
    # Repeat up to 5 passes in case newly revealed items have their own children.
    for pass_num in range(5):
        toggles = await page.query_selector_all(
            'button[aria-expanded="false"], '
            '[data-nodetype="group"] button, '
            '[data-nodetype="component"] button'
        )
        if not toggles:
            break
        clicked = 0
        for btn in toggles:
            try:
                is_expanded = await btn.get_attribute("aria-expanded")
                if is_expanded == "false":
                    await btn.click(timeout=1_000)
                    clicked += 1
            except Exception:
                pass
        if clicked == 0:
            break
        await page.wait_for_timeout(500)

    await page.wait_for_timeout(1_000)

    raw_links = await page.evaluate("""() => {
        const links = Array.from(document.querySelectorAll('a[href*="path="]'));
        return links.map(a => ({
            href: a.href,
            text: (a.textContent || a.innerText || '').trim(),
        }));
    }""")

    seen_paths = set()
    stories = []
    for link in raw_links:
        href = link["href"]
        parsed = urlparse(href)
        qs = parse_qs(parsed.query)
        path = qs.get("path", [""])[0]
        if not path or path in seen_paths:
            continue
        seen_paths.add(path)
        is_docs = "/docs/" in path
        is_story = "/story/" in path
        if is_docs or is_story:
            stories.append({
                "href": href,
                "text": link["text"],
                "path": path,
                "is_docs": is_docs,
            })

    print(f"  Found {len(stories)} unique story/docs paths.")
    return stories


def select_pages_to_scrape(stories: list[dict]) -> list[dict]:
    """
    Group stories by component ID and select the best page per component.
    Priority: docs page > first story page.
    """
    components: dict[str, dict] = {}
    for s in stories:
        path = s["path"]
        clean = re.sub(r"^/(docs|story)/", "", path)
        component_id = clean.split("--")[0]
        if component_id not in components:
            components[component_id] = {"docs": None, "stories": []}
        if s["is_docs"]:
            components[component_id]["docs"] = s
        else:
            components[component_id]["stories"].append(s)

    selected = []
    for comp in components.values():
        chosen = comp["docs"] or (comp["stories"][0] if comp["stories"] else None)
        if chosen:
            selected.append(chosen)

    n_docs = sum(1 for c in components.values() if c["docs"])
    n_fallback = sum(1 for c in components.values() if not c["docs"] and c["stories"])
    print(f"  Selected {len(selected)} pages ({n_docs} docs, {n_fallback} story fallbacks).")
    return selected


# ── Phase 2: Scrape pages ─────────────────────────────────────────────────────

async def scrape_page_content(page, story: dict) -> dict:
    """Navigate to a Storybook page and extract structured text and code blocks."""
    url = story["href"]
    try:
        await page.goto(url, wait_until="networkidle", timeout=PAGE_TIMEOUT)
    except PlaywrightTimeout:
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
        except Exception as e:
            return {**story, "content": "", "error": str(e)}

    await page.wait_for_timeout(PAGE_SETTLE_MS)

    # Reveal any hidden code blocks
    try:
        btns = await page.query_selector_all(
            'button[title*="ode" i], button[aria-label*="code" i], '
            'button:has-text("Show code"), button:has-text("show code")'
        )
        for btn in btns:
            try:
                await btn.click(timeout=2_000)
                await page.wait_for_timeout(400)
            except Exception:
                pass
    except Exception:
        pass

    # Use Playwright's locator API (no JS eval string) to extract content.
    # Try the docs wrapper first, then the generic root, then the whole body.
    main_locator = (
        page.locator(".sbdocs-wrapper").first
        if await page.locator(".sbdocs-wrapper").count() > 0
        else page.locator("#storybook-root").first
        if await page.locator("#storybook-root").count() > 0
        else page.locator("main").first
        if await page.locator("main").count() > 0
        else page.locator("body").first
    )

    # Grab all pre/code blocks first so we can reinsert them with fences
    code_parts = []
    for pre in await page.locator("pre").all():
        try:
            code_text = (await pre.inner_text(timeout=3_000)).strip()
            if code_text:
                code_parts.append("```\n" + code_text + "\n```")
        except Exception:
            pass

    # Get the full visible text of the main content area
    try:
        raw_text = await main_locator.inner_text(timeout=5_000)
    except Exception:
        raw_text = ""

    # Combine: prose text + code blocks appended at the end.
    # (Code blocks from <pre> are already embedded in inner_text, but separating
    # them here lets the LLM see clean fenced blocks regardless of rendering quirks.)
    content_parts = [raw_text.strip()]
    if code_parts:
        content_parts.append("\n\n--- Code Examples ---\n")
        content_parts.extend(code_parts)
    content = "\n\n".join(content_parts)

    return {
        **story,
        "content": (content or "").strip()[:MAX_CHARS_PER_PAGE],
        "error": None,
    }


async def scrape_all_pages(selected: list[dict]) -> list[dict]:
    results = []
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1280, "height": 900})
        await context.route("**/*", _route_handler)
        page = await context.new_page()

        for i, story in enumerate(selected):
            label = story.get("text") or story["path"]
            print(f"  [{i+1}/{len(selected)}] {label}")
            result = await scrape_page_content(page, story)
            results.append(result)
            if result.get("error"):
                print(f"    ! Error: {result['error']}")
            await asyncio.sleep(CRAWL_DELAY_S)

        await browser.close()
    return results


# ── Phase 3: Per-page extraction ──────────────────────────────────────────────

_extraction_tool = {
    "name": "submit_page_extraction",
    "description": "Submit the structured extraction for this Storybook page.",
    "input_schema": PageExtraction.model_json_schema(),
}

_extraction_prompt_template = """\
You are reading a single page from the Maryland Web Design System (MDWDS) Storybook.
Extract structured documentation that an LLM can use to build Maryland state web pages.

Page title: {title}
Page URL: {url}

Raw page content:
{content}

Extract:
- component_name: The clean display name (e.g. "Accordion", "Color Palette")
- category: One of: Getting Started, Foundation, Components, Templates, Utilities, Other
- summary: 2-3 sentences — what it is, what problem it solves, when to use it
- key_information: Markdown covering variants, CSS class names, modifier patterns, options,
  required attributes, and important facts. Be specific and complete.
- implementation: Markdown with fenced HTML code blocks. Correct structure, all required
  class names, ARIA attributes, and JS initialization if any. Cover structural variants.
- context: 1-2 sentences on how this fits into MDWDS, how it composes with other parts.

If the page has little content or is a redirect/index, still do your best with what's there.\
"""


async def extract_page(
    scraped: dict, client: anthropic.AsyncAnthropicBedrock, sem: asyncio.Semaphore
) -> PageExtraction | None:
    content = (scraped.get("content") or "").strip()
    if not content:
        return None

    prompt = _extraction_prompt_template.format(
        title=scraped.get("text") or scraped.get("path", ""),
        url=scraped.get("href", ""),
        content=content,
    )

    async with sem:
        for attempt in range(3):
            try:
                response = await client.messages.create(
                    model=EXTRACTION_MODEL,
                    max_tokens=4_096,
                    tools=[_extraction_tool],
                    tool_choice={"type": "tool", "name": "submit_page_extraction"},
                    messages=[{"role": "user", "content": prompt}],
                )
                block = next((b for b in response.content if b.type == "tool_use"), None)
                if block:
                    return PageExtraction.model_validate(block.input)
                return None
            except anthropic.RateLimitError:
                wait = 2 ** (attempt + 1)
                print(f"    Rate limited, retrying in {wait}s...")
                await asyncio.sleep(wait)
            except Exception as e:
                print(f"    Extraction error for '{scraped.get('text')}': {e}")
                return None
    return None


async def run_extraction(
    scraped_pages: list[dict], client: anthropic.AsyncAnthropicBedrock
) -> list[PageExtraction]:
    """Extract structured info from every scraped page, in parallel."""
    sem = asyncio.Semaphore(EXTRACTION_CONCURRENCY)
    tasks = [extract_page(p, client, sem) for p in scraped_pages if p.get("content")]

    extractions = []
    results = await asyncio.gather(*tasks)
    for scraped, result in zip(
        [p for p in scraped_pages if p.get("content")], results
    ):
        label = scraped.get("text") or scraped.get("path", "")
        if result:
            print(f"  + Extracted: {result.component_name} [{result.category}]")
            extractions.append(result)
        else:
            print(f"  - Skipped (no output): {label}")
    return extractions


# ── Phase 4: Holistic synthesis ───────────────────────────────────────────────

def _build_synthesis_prompt(extractions: list[PageExtraction]) -> str:
    # Pass only compact summaries and context to the synthesis call —
    # not the full implementation details. The synthesis is about the big picture.
    lines = []
    for e in extractions:
        lines.append(
            f"**{e.component_name}** ({e.category})\n"
            f"Summary: {e.summary}\n"
            f"Context: {e.context}\n"
            f"Key info (brief): {e.key_information[:400]}..."
        )
    compact_view = "\n\n---\n\n".join(lines)

    return f"""You are writing the introduction and overview section of an LLM skill document for the Maryland Web Design System (MDWDS).

The full document will consist of this introduction followed by detailed per-component reference entries. Your job is to write the intro — the section that gives another LLM the mental model it needs to use MDWDS correctly.

Below is a compact summary of every component and page in the system.

## All Components (Compact View)

{compact_view}

---

## What to Write

Write 600–900 words of Markdown covering:

1. **What MDWDS is** — its relationship to USWDS, what it's for, the Maryland state government context.

2. **CDN setup** — the exact HTML to include in `<head>`. Critical: version numbers in CDN URLs do NOT use a `v` prefix (write `0.36.0` not `v0.36.0`). Show the correct link and script tags. Mention FOUC prevention.

3. **The class naming system** — explain the patterns (`.usa-` prefix inheritance, modifier classes, BEM-like structure) so the LLM can reason about unfamiliar class names rather than just looking them up.

4. **How components compose** — how pages are built from blocks, the role of layout wrappers, and how foundation tokens underpin components.

5. **Key things to get right** — 3-5 common pitfalls or non-obvious requirements that an LLM should know before generating any MDWDS HTML.

Be direct, concrete, and instructional. This intro is read before the component reference entries, so don't repeat what's in them — focus on the system-level understanding. Generated: {datetime.now().strftime('%Y-%m-%d')}
"""


async def synthesize_intro(
    extractions: list[PageExtraction], client: anthropic.AsyncAnthropicBedrock
) -> str:
    print("\nPhase 4: Writing synthesis intro with Claude on Bedrock...")
    prompt = _build_synthesis_prompt(extractions)
    print(f"  Prompt size: {len(prompt):,} characters")

    response = await client.messages.create(
        model=SYNTHESIS_MODEL,
        max_tokens=4_096,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


# ── Phase 5: Assemble document ────────────────────────────────────────────────

def _render_extraction(e: PageExtraction) -> str:
    """Render a single PageExtraction as a Markdown section."""
    lines = [
        f"## {e.component_name}",
        "",
        f"*{e.category}*",
        "",
        e.summary,
        "",
        "### Key Information",
        "",
        e.key_information,
        "",
        "### Implementation",
        "",
        e.implementation,
        "",
        "### Context",
        "",
        e.context,
        "",
        "---",
        "",
    ]
    return "\n".join(lines)


def assemble_document(intro: str, extractions: list[PageExtraction]) -> str:
    # Sort extractions by canonical category order, then alphabetically within
    cat_index = {cat: i for i, cat in enumerate(CATEGORY_ORDER)}
    sorted_extractions = sorted(
        extractions,
        key=lambda e: (cat_index.get(e.category, 99), e.component_name.lower()),
    )

    parts = [
        "# Maryland Web Design System (MDWDS) — LLM Skill Document",
        "",
        f"*Generated {datetime.now().strftime('%Y-%m-%d')} · "
        f"{len(extractions)} components documented*",
        "",
        "---",
        "",
        intro.strip(),
        "",
        "---",
        "",
        "# Component Reference",
        "",
    ]

    current_category = None
    for e in sorted_extractions:
        if e.category != current_category:
            current_category = e.category
            parts.append(f"# {current_category}")
            parts.append("")

        parts.append(_render_extraction(e))

    return "\n".join(parts)


# ── Main ──────────────────────────────────────────────────────────────────────

async def run():
    print("=" * 60)
    print("MDWDS Documentation Scraper")
    print("Playwright + Bedrock Claude (per-page extract + synthesis)")
    print("=" * 60)

    client = anthropic.AsyncAnthropicBedrock()

    # ── Scrape (cached) ──────────────────────────────────────────────────────
    if os.path.exists(SCRAPE_CACHE):
        print(f"\nLoading scrape cache from {SCRAPE_CACHE} (delete to re-crawl)...")
        with open(SCRAPE_CACHE, "r", encoding="utf-8") as f:
            scraped_pages = json.load(f)
        print(f"  Loaded {len(scraped_pages)} cached pages.")
    else:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=True)
            context = await browser.new_context(viewport={"width": 1280, "height": 900})
            await context.route("**/*", _route_handler)
            page = await context.new_page()
            stories = await discover_story_urls(page)
            await browser.close()

        selected = select_pages_to_scrape(stories)
        print(f"\nPhase 2: Scraping {len(selected)} pages...")
        scraped_pages = await scrape_all_pages(selected)

        os.makedirs(os.path.dirname(SCRAPE_CACHE), exist_ok=True)
        with open(SCRAPE_CACHE, "w", encoding="utf-8") as f:
            json.dump(scraped_pages, f, indent=2, ensure_ascii=False)
        print(f"  Cached to {SCRAPE_CACHE}")

    successful = [p for p in scraped_pages if p.get("content")]
    print(f"  {len(successful)}/{len(scraped_pages)} pages have content.")

    # ── Per-page extraction (cached) ─────────────────────────────────────────
    if os.path.exists(EXTRACTION_CACHE):
        print(f"\nLoading extraction cache from {EXTRACTION_CACHE} (delete to re-extract)...")
        with open(EXTRACTION_CACHE, "r", encoding="utf-8") as f:
            raw = json.load(f)
        extractions = [PageExtraction.model_validate(e) for e in raw]
        print(f"  Loaded {len(extractions)} cached extractions.")
    else:
        print(f"\nPhase 3: Extracting {len(successful)} pages with {EXTRACTION_MODEL}...")
        extractions = await run_extraction(successful, client)

        with open(EXTRACTION_CACHE, "w", encoding="utf-8") as f:
            json.dump([e.model_dump() for e in extractions], f, indent=2, ensure_ascii=False)
        print(f"  Cached to {EXTRACTION_CACHE}")

    print(f"  {len(extractions)} extractions ready.")

    # ── Synthesis ────────────────────────────────────────────────────────────
    intro = await synthesize_intro(extractions, client)

    # ── Assemble ─────────────────────────────────────────────────────────────
    print("\nPhase 5: Assembling final document...")
    markdown = assemble_document(intro, extractions)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"\nSkill document saved to: {OUTPUT_FILE}")
    print(f"Document size: {len(markdown):,} characters")
    print(
        f"Breakdown: {sum(1 for e in extractions if e.category == 'Components')} components, "
        f"{sum(1 for e in extractions if e.category == 'Foundation')} foundation, "
        f"{sum(1 for e in extractions if e.category == 'Templates')} templates, "
        f"{sum(1 for e in extractions if e.category == 'Utilities')} utilities"
    )


if __name__ == "__main__":
    asyncio.run(run())
