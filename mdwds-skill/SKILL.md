---
name: mdwds
description: Use when building Maryland state government web pages, sites, or HTML using the Maryland Web Design System (MDWDS). Covers CDN setup, all maryland-* and usa-* components, the required statewide banner, page shell composition, and full page templates (agency homepage, landing, listing, basic, news, location, action, search). Use whenever the user asks to build, scaffold, or modify a Maryland.gov-style page or web app, references MDWDS or designsystem.maryland.gov, or asks about maryland-header / maryland-footer / maryland-hero / maryland-card / maryland-statewide-banner / maryland-statewide-footer.
---

# Maryland Web Design System (MDWDS) Skill

This skill helps you build Maryland state government web pages using the Maryland Web Design System (MDWDS). MDWDS is built on top of the U.S. Web Design System (USWDS), so you will mix `maryland-*` classes (MDWDS-specific) with `usa-*` classes (inherited from USWDS).

**Pinned MDWDS version in this skill:** `0.47.4`
**Recommended CDN version string for adopters:** `latest` resolves to the newest build; pin to a specific version (e.g. `0.47.4-beta.{hash}`) in production. Always confirm the current stable version on [designsystem.maryland.gov](https://designsystem.maryland.gov/?path=/docs/getting-started-for-engineers--docs) before shipping.

---

## How to use this skill

Do not read every file. Start with `cdn/setup.md` + `cdn/page-shell.md` + `cdn/component-index.md`, then load the specific component / recipe files you need.

---

## Reading order

1. **`cdn/setup.md`** — CDN tags, init script, FOUC prevention. Read first.
2. **`cdn/page-shell.md`** — The required top-to-bottom page structure (skipnav → banner → header → main → footer). Read whenever building a full page.
3. **`cdn/component-index.md`** — The lookup table. Use this to decide which component file to read next. Includes the maryland-card vs usa-card disambiguation and similar.
4. **`cdn/composition.md`** — Heading hierarchy, spacing (`margin-y-*`, `block-spacing`), `usa-prose`, grid utilities. Read whenever placing components on a page (not just inserting one in isolation).
5. **`cdn/foundation.md`** — Colors, typography, design tokens. Read only when the user asks about color, fonts, tokens, or accessibility contrast.
6. **`cdn/components/{name}.md`** — One file per component. Read on demand.
7. **`cdn/recipes/{template}.md`** — Full assembled page templates. Read when building an agency homepage, listing page, etc.

---

## The six rules — get these right

**1. Always load the CDN. Never write custom CSS to reproduce component styles.**
Every visual property of every MDWDS component comes from the CDN stylesheet. Your job is correct HTML structure with correct class names. Writing your own button color, card shadow, or alert background is always wrong — there's a class for it.

**A common failure mode:** agents reach for inline `<style>` blocks or `style="..."` attributes because they can't picture what a class will do. **Don't.** If you don't know what a class does visually, read the component's reference file — every one has a "What it looks like" section and a "What each class does" table that describes the visual effect of every class. Read first, then write markup. Inline CSS to "make it look right" almost always means you skipped the reference.

**2. The Statewide Banner is required on every Maryland state page.**
The `usa-banner` element with `aria-label="Official website of the State of Maryland"` (or the `<maryland-statewide-banner>` web-component equivalent) must appear at the top of every page before any other content. This is a non-negotiable state requirement.

**3. Two class namespaces. Do not mix them up.**
- `maryland-*` → MDWDS components and CSS (e.g. `maryland-header`, `maryland-card`, `maryland-hero`)
- `usa-*` → USWDS-inherited components and CSS (e.g. `usa-button`, `usa-banner`, `usa-form`, `usa-prose`, `grid-container`, `grid-col-*`)

Use the exact names from the per-component reference files. Don't invent plausible-sounding alternatives — they'll produce unstyled HTML.

**4. Web components (`<maryland-statewide-banner>`, `<maryland-statewide-footer>`) require the JS bundle.**
Without `mdwds-core.js` loaded, those elements render empty. Include a `<noscript>` fallback inside the banner (see `cdn/components/maryland-statewide-banner.md`).

**5. Follow a template — don't improvise the shell.**
For full pages, start from a file in `cdn/recipes/` and modify the body. Do not assemble your own skipnav/banner/header/footer combination from scratch.

**6. Trust the design system's spacing, color, and typography. Don't override them.**
MDWDS controls vertical rhythm with `block-spacing` and `margin-y-*` utilities; you don't need `margin-top: 24px` style attributes. Colors come from `bg-primary`, `text-base-darkest`, etc. — not from hex values you type. Fonts (Source Sans Pro Web for body, Merriweather for h1–h3) are loaded automatically. See `cdn/composition.md` and `cdn/foundation.md`.

**7. Copy markup verbatim from the component reference. Do not simplify it.**
This is the most common cause of broken pages. The BEM modifier classes (`--level-one`, `--mobile-panel`, `--container`, `__toggle`, etc.) and the wrapper `<div>`s in component markup are **not decoration** — both the CDN stylesheet and the MDWDS JS bundle target them. Examples of real bugs this rule prevents:
- Writing `<ul class="maryland-nav__list">` instead of `<ul class="maryland-nav__items maryland-nav__items--level-one">` → the JS init fails with `Cannot read properties of null (reading 'setAttribute')` because it expects the wrapping `__toggle` button + `__mobile-panel` div.
- Writing `<ul class="maryland-link-collection">` with inline `<span>` children instead of the `<section>` → `__container` → `__list` → `<li class="__item">` → `<a class="__link">` structure → no styling applies, items render as default underlined links.
- Skipping `<div class="maryland-card__container">` inside a card → flex layout breaks, header/body/footer collapse together.
- Omitting `data-mdwds` from the CDN stylesheet link → `<maryland-statewide-banner>` and `<maryland-statewide-footer>` register and render but invisibly (Shadow-DOM components look this attribute up to adopt the global stylesheet).
- Loading only `mdwds-core.js` and skipping `mdwds-elements.js` → `<maryland-statewide-banner>` / `<maryland-statewide-footer>` / `<maryland-translate>` produce empty unknown HTML elements. `mdwds-core.js` ships USWDS behaviors and the nav JS, but the Lit custom elements are registered by `mdwds-elements.js`. See `cdn/setup.md`.

If a component file's default markup looks "verbose," it isn't — every class and nested element is load-bearing. **Read the component file before writing markup, then copy its structure exactly.** When in doubt, prefer the component file's markup over what's in a recipe — recipes can drift.

---

## Decision tree

```
User wants to build...
├── A full Maryland.gov-style page? → cdn/recipes/{type}.md
│     • Generic agency site → agency-homepage.md
│     • State-level home → maryland-homepage.md
│     • News landing → news-page.md or listing-page.md
│     • Form / interaction → action-page.md
│     • Office / location info → location-page.md
│     • Search results → search-page.md
│     • Anything else with a hero → landing-page.md or basic-page.md
│
├── A single component? → cdn/components/{name}.md
│     • Use cdn/component-index.md to disambiguate (e.g. maryland-card vs usa-card)
│
├── Just the header/footer/banner? → cdn/page-shell.md
│
└── Custom styling / spacing? → cdn/composition.md + cdn/foundation.md
                                 (and review the question — usually a built-in class
                                  already covers it)
```

---

## What's in each file

| File | When to read |
|---|---|
| `cdn/setup.md` | First, for every task. CDN tags + init script. |
| `cdn/page-shell.md` | Building or modifying a full page. |
| `cdn/component-index.md` | Looking up a component, or unsure which to use. |
| `cdn/composition.md` | Heading hierarchy, spacing, grid, prose. |
| `cdn/foundation.md` | Colors, typography, tokens. |
| `cdn/components/*.md` | Reference for a specific component. |
| `cdn/recipes/*.md` | Full page templates with assembled HTML. |
