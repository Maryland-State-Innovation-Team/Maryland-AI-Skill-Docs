# &lt;maryland-statewide-footer&gt;

The Lit-based web component containing the **statewide service-directory footer** ("Explore Maryland.gov" with links to Top services, Government, Policies, Connect, Alerts). **Required at the very bottom of every Maryland.gov agency page**, below the agency-specific `maryland-footer`.

> Zero configuration. Drop in the tag and it renders the full statewide footer with the canonical state services links. **Do not edit the link list** — it's the same across every Maryland.gov site by design, and updating it is the design system team's responsibility.

## What it looks like

Visually **identical** to the "statewide" half of `maryland-footer` (the component reuses `maryland-footer` SCSS classes internally). Specifically:

- Dark `ink` (near-black) full-width background.
- Content constrained to a `widescreen` (1400px) `grid-container` with site margins.
- A large `<h2>` "Explore Maryland.gov" at the top (22px / `body-11`, semibold, white).
- A grid of five `<nav>` link-groups: **Top services**, **Government**, **Policies**, **Connect**, **Alerts**. Each group is a heading (`<h3>`, 16px semibold white) over an unstyled bulleted list of 4–8 links (14px / `body-4`, color `base-lighter`).
- Layout: 1 column on mobile, 2 columns at tablet (≥640px), 4 columns at desktop (≥1024px). Groups flow into the column layout via CSS `column-count`.
- A 1px `base-darker` horizontal divider with ~`units(7)` vertical margin at desktop.
- Bottom branding row: horizontal Maryland wordmark (inverted/white, 176×36px) on the left, copyright "© {current year} State of Maryland. All rights reserved." on the right (stacked on mobile, flex-space-between at desktop).

The footer content is fixed — there's no way to customize the link list, headings, or wordmark without a feature request to the MDWDS team.

## Default markup

```html
<!-- 1. Load the bundle that REGISTERS Lit custom elements (mdwds-core.js alone is NOT enough) -->
<script type="module" src="https://cdn.maryland.gov/mdwds/latest/js/mdwds-elements.js"></script>

<!-- 2. Place the element at the very bottom of the page -->
<maryland-statewide-footer></maryland-statewide-footer>
```

That's it. No attributes. No slot content. No props.

> **Critical:** `mdwds-core.js` does NOT register `<maryland-statewide-footer>`. The element is defined by `mdwds-elements.js` (or the per-component standalone script at `components/maryland-statewide-footer.js`). If you only load `mdwds-core.js`, this tag renders as an empty unknown HTML element. See `cdn/setup.md`.

## Placement in the page shell

Per `cdn/page-shell.md`:

```html
<body>
  <a class="usa-skipnav" href="#main-content">Skip to main content</a>
  <section class="usa-banner" aria-label="Official website of the State of Maryland">...</section>
  <header class="maryland-header">...</header>
  <main id="main-content" tabindex="-1">...</main>
  <footer class="maryland-footer">...</footer>          <!-- Agency footer -->
  <maryland-statewide-footer></maryland-statewide-footer>  <!-- Statewide footer (last) -->
</body>
```

## What you get (the rendered DOM)

The component renders the same structure that the HTML `maryland-footer` produces when `displaySitewide: true`. The full markup includes:

- `<footer class="maryland-footer">` wrapper
- `<div class="maryland-footer__container">` (grid container)
- `<section class="maryland-footer__section" aria-labelledby="global-footer">`
- `<h2 class="maryland-footer__title" id="global-footer">Explore Maryland.gov</h2>`
- `<div class="maryland-footer__content">` containing 5 `<nav class="maryland-footer__link-group">` blocks
- `<hr aria-hidden="true" class="maryland-footer__divider">`
- `<div class="maryland-footer__branding">` with the horizontal inverted Maryland wordmark and copyright

See `cdn/components/maryland-footer.md` for the class table — every rendered class is the same.

## What each class does

All visual styling comes from the published CSS. The component pulls in the MDWDS stylesheet during its connected lifecycle. Refer to `cdn/components/maryland-footer.md` for the full class table — the statewide variant uses these classes from there:

- `maryland-footer`, `maryland-footer__container`, `maryland-footer__section`
- `maryland-footer__title`, `maryland-footer__content`
- `maryland-footer__link-group`, `maryland-footer__link-group-heading`, `maryland-footer__link-group-list`
- `maryland-footer__divider`
- `maryland-footer__branding`, `maryland-footer__logo`, `maryland-footer__copyright`

## Prop schema

None. The component is zero-config. The documented variants describe this as "zero configuration required — plug-and-play with built-in styles."

## Heading level adjustment

The component's headings are fixed at `<h2>` (the "Explore Maryland.gov" title) and `<h3>` (each link-group title). These are the canonical levels and **cannot** be changed via attribute. Since the footer is a top-level section of the page (alongside `<main>`), `<h2>` is the correct level for its title.

## Common mistakes

1. **Loading only `mdwds-core.js` and not `mdwds-elements.js`** — the most common silent-failure mode. `mdwds-core.js` registers behaviors (banner toggle, accordion, nav JS) but does NOT register the Lit custom elements. `<maryland-statewide-footer>` will sit in the DOM as an empty unknown element with no visible output. You need a `<script type="module">` tag for either `mdwds-elements.js` (covers all `<maryland-*>` web components) or the per-component file at `components/maryland-statewide-footer.js`. See `cdn/setup.md`.
2. **Forgetting the `data-mdwds` attribute on the stylesheet `<link>`** — second most common silent failure. The component renders into Shadow DOM and looks up the CDN stylesheet via `link[rel="stylesheet"][data-mdwds]` to adopt it into the shadow root. Without `data-mdwds`, the footer registers and renders its markup but appears as invisible/unstyled text — no fonts, no colors, no layout.
3. **Putting it above the agency footer** — order is fixed: `maryland-footer` (agency) first, then `<maryland-statewide-footer>` last. See `cdn/page-shell.md`.
4. **Trying to pass attributes (`<maryland-statewide-footer agency="...">`)** — there are no attributes. The element ignores any you add.
5. **Rendering it AND `maryland-footer` with `displaySitewide: true`** — that produces two statewide blocks. Use one approach: either `maryland-footer` (agency only) + `<maryland-statewide-footer>` separately, or `maryland-footer` with both `displayAgency` and `displaySitewide` set (and skip the web component).
6. **Customizing the links via JS** — the link list is intentionally fixed. If a link is wrong, file a request with the design system team rather than DOM-patching the shadow root.
7. **Wrapping the element in a `<footer>`** — the component already renders a `<footer>` internally. An outer `<footer>` creates a redundant landmark.
8. **Skipping the statewide footer entirely** — even agencies that have rich agency-specific footers must include `<maryland-statewide-footer>` per state branding policy. It's the same requirement as the statewide banner.
