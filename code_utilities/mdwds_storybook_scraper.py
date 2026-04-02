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
MAX_DOCS_IFRAME_CHARS  = 8_000   # cap on docs iframe HTML (prose + code examples)
MAX_STORY_IFRAME_CHARS = 5_000   # cap on rendered story HTML (real component markup)
MAX_TEXT_CHARS         = 2_000   # cap on visible text content

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
    Also stores the first story variant path so the scraper can access rendered
    component HTML even for docs-only components.
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
        if not chosen:
            continue
        first_story = comp["stories"][0] if comp["stories"] else None
        selected.append({
            **chosen,
            # For docs pages this gives us the story variant to render for real HTML
            "first_story_path": first_story["path"] if first_story else None,
        })

    n_docs = sum(1 for c in components.values() if c["docs"])
    n_fallback = sum(1 for c in components.values() if not c["docs"] and c["stories"])
    print(f"  Selected {len(selected)} pages ({n_docs} docs, {n_fallback} story fallbacks).")
    return selected


# ── Phase 2: Scrape pages ─────────────────────────────────────────────────────

def _story_id(path: str) -> str:
    """Extract the Storybook story ID from a ?path= value."""
    return re.sub(r"^/(docs|story)/", "", path)


def _iframe_url(story_id: str, view_mode: str) -> str:
    """Build the direct Storybook iframe URL.
    This bypasses the Storybook shell — navigating here gives us the raw rendered
    content (docs text + code blocks, or the component HTML) without chrome noise.
    """
    return f"{STORYBOOK_URL.rstrip('/')}/iframe.html?id={story_id}&viewMode={view_mode}"


async def _navigate(page, url: str, is_iframe: bool = False) -> bool:
    """
    Navigate to a URL and wait for it to be usable.
    For iframe.html pages we use domcontentloaded + a fixed settle time rather than
    networkidle — Storybook iframes keep a WebSocket open for hot-reload, which means
    networkidle never fires and the script hangs indefinitely.
    """
    wait_until = "domcontentloaded" if is_iframe else "networkidle"
    try:
        await page.goto(url, wait_until=wait_until, timeout=PAGE_TIMEOUT)
        if is_iframe:
            await page.wait_for_timeout(PAGE_SETTLE_MS)
        return True
    except PlaywrightTimeout:
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
            await page.wait_for_timeout(PAGE_SETTLE_MS)
            return True
        except Exception:
            return False


async def scrape_page_content(page, story: dict) -> dict:
    """
    Scrape a Storybook component by navigating directly to its iframe.html URL.

    The main Storybook shell (/?path=...) renders all content inside nested iframes,
    so inner_text() on the shell returns nothing useful. Navigating to iframe.html
    directly gives us the real content without any of the Storybook chrome.

    For docs pages we fetch two iframes:
      1. viewMode=docs  — the MDX documentation page: prose, usage notes, code blocks
      2. viewMode=story — the first story variant: actual rendered component HTML

    For story-only pages we fetch just viewMode=story.
    """
    parts = []
    sid = _story_id(story["path"])

    # ── Pass 1: docs iframe (prose + embedded code examples) ─────────────────
    if story["is_docs"]:
        url = _iframe_url(sid, "docs")
        if await _navigate(page, url, is_iframe=True):
            # Storybook renders docs asynchronously — wait for the loading skeleton
            # to detach before reading content, or bail after 15s
            try:
                await page.wait_for_selector(
                    ".sb-preparing-docs, .sb-preparing-story",
                    state="detached",
                    timeout=15_000,
                )
            except Exception:
                pass  # either already gone or never appeared
            await page.wait_for_timeout(500)
            try:
                html = await page.evaluate("() => document.body.innerHTML")
                if html and len(html.strip()) > 100:
                    parts.append(
                        f"[DOCS PAGE HTML — prose, usage notes, code examples]\n"
                        f"{html[:MAX_DOCS_IFRAME_CHARS]}"
                    )
            except Exception:
                pass
            try:
                text = await page.locator("body").inner_text(timeout=5_000)
                if text and len(text.strip()) > 30:
                    parts.append(f"[DOCS VISIBLE TEXT]\n{text[:MAX_TEXT_CHARS]}")
            except Exception:
                pass

    # ── Pass 2: story iframe (rendered component — real class names) ──────────
    # For docs pages, use the stored first story variant.
    # For story pages, use the page itself.
    story_path = story.get("first_story_path") or (
        story["path"] if not story["is_docs"] else None
    )
    if story_path:
        story_sid = _story_id(story_path)
        url = _iframe_url(story_sid, "story")
        if await _navigate(page, url, is_iframe=True):
            await page.wait_for_timeout(PAGE_SETTLE_MS)
            try:
                html = await page.evaluate("() => document.body.innerHTML")
                if html and len(html.strip()) > 100:
                    parts.append(
                        f"[RENDERED STORY HTML — exact component markup with real class names]\n"
                        f"{html[:MAX_STORY_IFRAME_CHARS]}"
                    )
            except Exception:
                pass

    content = "\n\n".join(parts)
    return {
        **story,
        "content": content.strip(),
        "error": None if parts else "no content retrieved",
    }


async def detect_cdn_version(page) -> str:
    """
    Detect the current MDWDS CDN version by checking:
    1. The deployed ai.maryland.gov site CSS link (most authoritative)
    2. Any cdn.maryland.gov reference in the Storybook Getting Started iframe
    Falls back to the last known stable version.
    """
    # Check the deployed Maryland site — its CSS link contains the live CDN version
    try:
        await page.goto("https://ai.maryland.gov/", wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
        links = await page.evaluate(
            "() => Array.from(document.querySelectorAll('link[rel=\"stylesheet\"]')).map(l => l.href)"
        )
        for href in links:
            m = re.search(r"cdn\.maryland\.gov/mdwds/([^/]+)/", href)
            if m:
                return m.group(1)
    except Exception:
        pass

    # Fallback: scan Getting Started Storybook iframe for any CDN reference in text
    try:
        url = _iframe_url("getting-started-for-engineers--docs", "docs")
        await page.goto(url, wait_until="domcontentloaded", timeout=PAGE_TIMEOUT)
        await page.wait_for_timeout(PAGE_SETTLE_MS)
        text = await page.locator("body").inner_text(timeout=5_000)
        m = re.search(r"cdn\.maryland\.gov/mdwds/([0-9]+\.[0-9]+\.[0-9]+)/", text)
        if m:
            return m.group(1)
    except Exception:
        pass

    return "0.44.0"  # last known stable version


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
You are extracting documentation from a single Maryland Web Design System (MDWDS) \
Storybook page. The content below includes real rendered HTML from the Storybook \
component iframes — these contain the ACTUAL class names used by MDWDS.

Page title: {title}
Page URL: {url}
MDWDS CDN version: {version}

Page content:
{content}

Extract the following fields:

- component_name: Clean display name (e.g. "Header", "Accordion", "Statewide Banner")
- category: One of: Getting Started, Foundation, Components, Templates, Utilities, Other
- summary: 2-3 sentences — what it is, what problem it solves, when to use it
- key_information: Markdown covering all variants, CSS class modifier patterns, required
  HTML attributes, and important facts. List the actual class names you see in the HTML.
- implementation: Markdown with fenced HTML code blocks showing the EXACT structure from
  the rendered HTML above — real class names, required ARIA attributes, correct nesting.
  For complex components show the full structure. Include ALL variants you see.
- context: 1-2 sentences on how this fits into the MDWDS system or composes with others.

CRITICAL RULES:
1. Use ONLY class names that appear verbatim in the HTML provided above.
   DO NOT invent, guess, or generalize class names. If you see "maryland-header" in the
   HTML, write "maryland-header". Do not write "header" or "md-header" or anything else.
2. If the HTML is empty or minimal, say so in the summary and leave implementation empty
   rather than fabricating markup.
3. For the CDN URLs in Getting Started content, use version {version} (no "v" prefix).\
"""


async def extract_page(
    scraped: dict,
    client: anthropic.AsyncAnthropicBedrock,
    sem: asyncio.Semaphore,
    cdn_version: str = "unknown",
) -> PageExtraction | None:
    content = (scraped.get("content") or "").strip()
    if not content:
        return None

    prompt = _extraction_prompt_template.format(
        title=scraped.get("text") or scraped.get("path", ""),
        url=scraped.get("href", ""),
        version=cdn_version,
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
    scraped_pages: list[dict],
    client: anthropic.AsyncAnthropicBedrock,
    cdn_version: str = "unknown",
) -> list[PageExtraction]:
    """Extract structured info from every scraped page, in parallel."""
    sem = asyncio.Semaphore(EXTRACTION_CONCURRENCY)
    tasks = [
        extract_page(p, client, sem, cdn_version)
        for p in scraped_pages
        if p.get("content")
    ]

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

def _build_synthesis_prompt(
    extractions: list[PageExtraction], cdn_version: str
) -> str:
    # Pass only compact summaries and context — not full implementation details.
    lines = []
    for e in extractions:
        lines.append(
            f"**{e.component_name}** ({e.category})\n"
            f"Summary: {e.summary}\n"
            f"Context: {e.context}\n"
            f"Key info (brief): {e.key_information[:400]}..."
        )
    compact_view = "\n\n---\n\n".join(lines)

    return f"""You are writing the introduction and overview section of an LLM skill document for the Maryland Web Design System (MDWDS). The current MDWDS CDN version is {cdn_version}.

The full document will consist of this introduction followed by detailed per-component reference entries. Your job is to write the intro — the section that gives another LLM the mental model it needs to use MDWDS correctly.

Below is a compact summary of every component and page in the system.

## All Components (Compact View)

{compact_view}

---

## What to Write

Write 600–900 words of Markdown covering:

1. **What MDWDS is** — its relationship to USWDS, what it's for, the Maryland state government context.

2. **CDN setup** — the exact HTML to include in `<head>`. The CDN version is {cdn_version} — do NOT add a "v" prefix (write `{cdn_version}`, not `v{cdn_version}`). Show the correct link and script tags. Emphasize that ALL component styling comes from the CDN — the LLM must never write custom CSS to replicate MDWDS styles. Mention FOUC prevention with `usa-js-loading`.

3. **The class naming system** — `maryland-*` web components and CSS custom properties, `usa-*` USWDS-inherited classes with BEM modifiers (`usa-button--secondary`), and plain BEM for layout. Explain that `maryland-header`, `maryland-nav`, `maryland-search-form` etc. are the real header classes — not generic `header` or `header__container`.

4. **How components compose** — page shell order: `usa-banner` (statewide banner) → `maryland-header` → `maryland-nav` → main content → statewide footer. Templates show the authoritative nesting.

5. **Key things to get right** — at minimum: (a) always load the CDN, never write custom CSS; (b) the Statewide Banner is required on every Maryland state page; (c) use real MDWDS class names from the component reference, not invented ones; (d) `<maryland-*>` web components need the JS bundle to function.

Be direct and concrete. Generated: {datetime.now().strftime('%Y-%m-%d')}
"""


async def synthesize_intro(
    extractions: list[PageExtraction],
    client: anthropic.AsyncAnthropicBedrock,
    cdn_version: str = "unknown",
) -> str:
    print("\nPhase 4: Writing synthesis intro with Claude on Bedrock...")
    prompt = _build_synthesis_prompt(extractions, cdn_version)
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
        # Detect version even when using cache (fast, single page load)
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=True)
            context = await browser.new_context(viewport={"width": 1280, "height": 900})
            await context.route("**/*", _route_handler)
            page = await context.new_page()
            cdn_version = await detect_cdn_version(page)
            await browser.close()
        print(f"  CDN version detected: {cdn_version}")
    else:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=True)
            context = await browser.new_context(viewport={"width": 1280, "height": 900})
            await context.route("**/*", _route_handler)
            page = await context.new_page()
            stories = await discover_story_urls(page)
            cdn_version = await detect_cdn_version(page)
            await browser.close()

        print(f"  CDN version detected: {cdn_version}")
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
        extractions = await run_extraction(successful, client, cdn_version)

        with open(EXTRACTION_CACHE, "w", encoding="utf-8") as f:
            json.dump([e.model_dump() for e in extractions], f, indent=2, ensure_ascii=False)
        print(f"  Cached to {EXTRACTION_CACHE}")

    print(f"  {len(extractions)} extractions ready.")

    # ── Synthesis ────────────────────────────────────────────────────────────
    intro = await synthesize_intro(extractions, client, cdn_version)

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
