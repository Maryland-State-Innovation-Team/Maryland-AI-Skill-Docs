# &lt;maryland-statewide-banner&gt;

The Lit-based web-component version of the "Official website of the State of Maryland" banner. Designed for **embedding the banner in non-MDWDS sites** (e.g., a third-party application that wants to identify as an official Maryland service) — the component is fully self-contained, loads its own styles, and injects Google Analytics + Microsoft Clarity tags on mount.

> **For full MDWDS pages, use the `usa-banner` HTML version instead.** When the rest of the page already loads the MDWDS CDN stylesheet, the HTML banner is lighter and consistent with the rest of the page chrome. The web component is for sites that **don't** otherwise use MDWDS. See `cdn/components/usa-banner.md`.

## What it looks like

The rendered output is **identical** to the HTML `usa-banner` (the web component renders the same banner DOM with the flag, Maryland.gov link, and Translate link enabled). It produces:

- Thin gray strip with white-ish text at the top of the page.
- Left: Maryland state flag (18×13px), then "An official website of the State of Maryland." in 14px (`ui-4`) Source Sans.
- Center: "Here's how you know" expandable button with a chevron icon (12px, rotates -90° when collapsed, 90° when expanded).
- Right (desktop only): "Maryland.gov" link and "Translate" link (with globe icon), separated by a 1px `base-light` vertical divider.
- Expanded content (when the button is toggled): a two-column block at tablet+ with the .gov icon + explainer on the left and the HTTPS lock icon + explainer on the right. Below tablet, the columns stack.

**Important differences from the plain `usa-banner` HTML:**

1. The component **auto-injects Google Analytics** (`GTM-TZXNZMFJ`) and **Microsoft Clarity** scripts the first time it connects to the DOM, unless those scripts are already present. This is the canonical way the state tracks adoption of the banner across sites.
2. The component requires the MDWDS JS bundle to be loaded — without it, the element renders empty.
3. State management for the expand/collapse is internal to the component; no `usa-accordion` JS needed.

## Default markup

```html
<!-- 1. Load the web component bundle from the CDN -->
<script
  type="module"
  src="https://cdn.maryland.gov/mdwds/latest/components/maryland-statewide-banner.js"
></script>

<!-- 2. Drop the element at the top of the page, before any other content -->
<maryland-statewide-banner>
  <!-- 3. Optional but recommended noscript fallback -->
  <noscript>
    <link
      rel="stylesheet"
      href="https://cdn.maryland.gov/mdwds/latest/css/mdwds.min.css"
    />
    <div class="maryland-alert maryland-alert--warning">
      <div class="maryland-alert__body">
        <h4 class="maryland-alert__heading">JavaScript Required</h4>
        <p class="maryland-alert__text">
          JavaScript is required to use content on this page. Please enable
          JavaScript in your browser.
        </p>
      </div>
    </div>
  </noscript>
</maryland-statewide-banner>
```

## When to use this vs. `usa-banner`

| Situation | Choice |
|---|---|
| Building an MDWDS-styled Maryland.gov page from scratch | `usa-banner` (HTML) — see `cdn/components/usa-banner.md` |
| Embedding the banner on a third-party app or vendor portal that doesn't otherwise use MDWDS | `<maryland-statewide-banner>` — drops in as a single element, brings its own CSS |
| Need to avoid the auto-injected analytics scripts | `usa-banner` (HTML) — the web component always injects GTM + Clarity |
| Building inside a Single-Page Application (React/Vue/Angular) where the banner needs to remount cleanly | `<maryland-statewide-banner>` — it's a real custom element |

## What you cannot configure

Unlike the HTML `usa-banner`, the web component **does not expose props**. It always renders with:

- Maryland flag always shown
- Maryland.gov link always shown at desktop
- Translate link always shown
- `aria-label="Official website of the State of Maryland"` (fixed)

This is intentional — the statewide banner is meant to be a consistent state-branded element across **all** Maryland services, regardless of which agency or vendor renders it. If you need a different banner configuration, use the HTML `usa-banner` instead.

## What each class does (rendered output)

The component renders the same DOM as `usa-banner`. See `cdn/components/usa-banner.md` for the class table — it applies equally here.

## Prop schema

None. The component is zero-config.

## Heading level adjustment

The banner contains no headings. The page `<h1>` should still be the hero title, not the banner text.

## Common mistakes

1. **Loading only `mdwds-core.js` and not `mdwds-elements.js`** — the most common silent-failure mode. `mdwds-core.js` registers behaviors (banner toggle, accordion, nav) but does NOT register the Lit custom elements. `<maryland-statewide-banner>` will sit in the DOM as an empty unknown element with no visible output. You need a `<script type="module">` tag for either `mdwds-elements.js` (covers all `<maryland-*>` web components) or the per-component file at `components/maryland-statewide-banner.js`. See `cdn/setup.md`.
2. **Forgetting the `data-mdwds` attribute on the stylesheet `<link>`** — second most common silent failure. The component renders into Shadow DOM and looks up the CDN stylesheet via `link[rel="stylesheet"][data-mdwds]` to adopt it into the shadow root. Without `data-mdwds`, the banner registers and renders its markup but appears as invisible/unstyled text — no fonts, no colors, no layout.
2. **Omitting the `<noscript>` fallback** — users with JS disabled get nothing. The recommended fallback is an `maryland-alert--warning` directing them to enable JS, including its own stylesheet link in case MDWDS isn't loaded.
3. **Loading the web component **and** also rendering `usa-banner` HTML** — you'll get two banners stacked. Pick one.
4. **Using this banner on a non-government site** — the banner explicitly says "official website of the State of Maryland." Per USWDS guidance, **do not use on `.com` / `.org` sites**.
5. **Wrapping the element in a `<header>`** — the banner is its own landmark via the internal `<section aria-label>`. An outer `<header>` creates a redundant landmark.
6. **Trying to override the styles via shadow DOM** — the component uses Lit's default shadow-root and pulls in the MDWDS stylesheet. External CSS won't penetrate the shadow boundary. To customize, switch to the HTML `usa-banner`.
7. **Expecting the analytics injection to no-op locally** — the component injects GTM and Clarity tags on every fresh mount (it checks for existing script tags first, but in dev iframes/Storybook it may re-inject). If you don't want this, use the HTML banner instead.
