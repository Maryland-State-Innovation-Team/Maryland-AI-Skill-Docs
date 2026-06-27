# usa-accordion

A USWDS Accordion is a stack of collapsible panels: each panel has a header button that toggles the visibility of a content region below it. Useful for FAQs, technical reference, terms of service — anywhere a single page must hold a lot of optional-to-read content. MDWDS uses the upstream USWDS component as-is.

> **Prefer `maryland-accordion` on Maryland.gov pages.** The Maryland-themed accordion uses Maryland visual styling (Merriweather headings, Maryland blue accents) and is the recommended choice for any branded page. Reach for `usa-accordion` only inside USWDS-style internal tools where MDWDS theming would clash. See `cdn/components/maryland-accordion.md` and the disambiguation table in `cdn/component-index.md`.

## What it looks like

A vertical stack of full-width panels. Each panel has two parts:

- A **header** — a wide rectangular button stretching the full container width. Header text sits on a near-white background (`base-lightest`) with a small chevron icon (downward when collapsed, upward when expanded) pinned to the right side. The button label is Source Sans Pro semibold, ~16px, in `base-darkest`. On hover the header background shifts a shade darker. On focus the button receives a 2px primary-blue outline.
- A **content panel** — a white-background region below the header that holds paragraphs, lists, or any other inline content. Collapsed panels are not just hidden visually; they are removed from the layout via the `hidden` HTML attribute, so the page doesn't reserve their space when closed.

Panels touch each other vertically with no gap. There is no outer border by default — the visual separation between panels comes from the alternating header (slightly tinted) and content (white) backgrounds.

The **bordered** variant adds a 1px gray border around each panel, giving a more boxed look that suits dense FAQ pages.

## Variants

| Variant | Class / attribute | Visual |
|---|---|---|
| Default | `usa-accordion` | Stacked panels with no outer border; alternating tint between header and content distinguishes panels. |
| Bordered | `usa-accordion--bordered` (on the wrapper) | Same layout, but each panel has a 1px gray border surrounding it. The borders give a more enclosed, table-like appearance. |
| Multiselectable | `data-allow-multiple` (attribute on the wrapper, not a class) | Multiple panels can be open simultaneously. By default, opening one panel closes any others in the same accordion. |

## When to use which variant

- **Default** → Standard FAQ or "Learn more" sections inside narrative pages where a softer visual fits the surrounding text.
- **`usa-accordion--bordered`** → Dense reference content (regulations, eligibility criteria, definitions) where users will likely scan multiple panels and need clear visual separation.
- **`data-allow-multiple`** → FAQ pages where the user is likely to want to compare two panels' content side-by-side. Without it, opening panel B closes panel A — which is fine for most cases but frustrating for cross-referencing.

## Default markup

A DNR fishing license FAQ section. Three questions, the first one open by default:

```html
<div class="usa-accordion" aria-label="Fishing license FAQs">
  <h3 class="usa-accordion__heading">
    <button
      type="button"
      class="usa-accordion__button"
      aria-expanded="true"
      aria-controls="fishing-faq-1"
      id="fishing-faq-1-button"
    >
      Who needs a Maryland fishing license?
    </button>
  </h3>
  <div id="fishing-faq-1" class="usa-accordion__content" aria-labelledby="fishing-faq-1-button">
    <p>Anyone age 16 or older who fishes in Maryland's freshwater, tidal, or Chesapeake Bay waters needs a license, unless covered by a specific exemption (active military on leave, individuals with disabilities, residents fishing on a Free Fishing Day).</p>
  </div>

  <h3 class="usa-accordion__heading">
    <button
      type="button"
      class="usa-accordion__button"
      aria-expanded="false"
      aria-controls="fishing-faq-2"
      id="fishing-faq-2-button"
    >
      How much does a recreational license cost?
    </button>
  </h3>
  <div id="fishing-faq-2" class="usa-accordion__content" aria-labelledby="fishing-faq-2-button" hidden>
    <p>Resident annual licenses are $20.50; non-resident annual licenses are $30.50. Short-term and senior options are also available at DNR Service Centers and online.</p>
  </div>

  <h3 class="usa-accordion__heading">
    <button
      type="button"
      class="usa-accordion__button"
      aria-expanded="false"
      aria-controls="fishing-faq-3"
      id="fishing-faq-3-button"
    >
      Where can I buy a license?
    </button>
  </h3>
  <div id="fishing-faq-3" class="usa-accordion__content" aria-labelledby="fishing-faq-3-button" hidden>
    <p>Online through COMPASS, at any DNR Service Center, or at authorized retail license agents (most tackle shops, Walmart, and sporting-goods retailers across the state).</p>
  </div>
</div>
```

Important notes about the markup:

- Each panel is **two adjacent siblings** inside the wrapper: the heading (containing the button) and the content `<div>`. They are *not* nested inside a per-panel container — the wrapper holds all heading/content pairs as flat siblings.
- The `<button>` is **inside** a heading element (`<h2>`, `<h3>`, `<h4>` etc.) so screen readers announce it as both a heading and a button.
- The default heading level in the documented variants is `<h4>` (the `headingLevel` arg defaults to `"h4"`). **Adjust the heading level to match your page outline** — see `cdn/composition.md`.
- Each button has `aria-controls` pointing to its content `<div>`'s `id`, and each content `<div>` has `aria-labelledby` pointing back to the button's `id`.
- Initial state is set by two paired attributes: `aria-expanded="true|false"` on the button and the `hidden` attribute (present or absent) on the content `<div>`. Closed panels carry `hidden`; open panels omit it.

## Markup — bordered variant

Add `usa-accordion--bordered` to the wrapper:

```html
<div class="usa-accordion usa-accordion--bordered" aria-label="Eligibility requirements">
  <h3 class="usa-accordion__heading">
    <button type="button" class="usa-accordion__button" aria-expanded="false" aria-controls="elig-1">
      Residency requirements
    </button>
  </h3>
  <div id="elig-1" class="usa-accordion__content" hidden>
    <p>Maryland residents must show proof of in-state residency dated within the last 60 days.</p>
  </div>
  <!-- ...repeat for additional panels... -->
</div>
```

## Markup — multiselectable

Add `data-allow-multiple` as an attribute on the wrapper:

```html
<div class="usa-accordion" data-allow-multiple aria-label="Compare park amenities">
  <h3 class="usa-accordion__heading">
    <button type="button" class="usa-accordion__button" aria-expanded="false" aria-controls="park-1">
      Patapsco Valley State Park
    </button>
  </h3>
  <div id="park-1" class="usa-accordion__content" hidden>
    <p>Camping, trails, fishing, swimming. 16,000 acres.</p>
  </div>

  <h3 class="usa-accordion__heading">
    <button type="button" class="usa-accordion__button" aria-expanded="false" aria-controls="park-2">
      Assateague State Park
    </button>
  </h3>
  <div id="park-2" class="usa-accordion__content" hidden>
    <p>Oceanfront camping, swimming, wildlife viewing. Wild horses on site.</p>
  </div>
</div>
```

With `data-allow-multiple`, opening panel 2 leaves panel 1 open. Without it, opening panel 2 closes panel 1.

## What each class does

| Class / attribute | Effect |
|---|---|
| `usa-accordion` | Base wrapper. Establishes the stacking context for the panels and tells the USWDS JS to treat this element's children as a single accordion group. By default, only one panel at a time can be open within this wrapper. |
| `usa-accordion--bordered` | Adds a 1px gray border around each panel inside the wrapper. Gives panels a boxed look. |
| `usa-accordion__heading` | Class applied to the heading element (`<h2>`–`<h6>`) that wraps the button. Removes default heading margins and resets typography so the wrapping heading doesn't break the panel's visual rhythm. |
| `usa-accordion__button` | The clickable header button. Full-width, light-gray (`base-lightest`) background, semibold body text, chevron icon pinned right. Darker on hover; primary-blue focus ring. Background switches to light primary tint when the panel is expanded. |
| `usa-accordion__content` | The content panel `<div>`. White background, padding-y ~16px and padding-x ~16px. Hidden when its sibling button is `aria-expanded="false"` (via the `hidden` HTML attribute). |
| `data-allow-multiple` | HTML attribute (not a class) on the wrapper. Tells the USWDS JS to allow multiple panels open at once. Omit this attribute and the JS will auto-collapse other panels when one is opened. |
| `aria-expanded="true|false"` | Set on the button. The USWDS JS toggles this value on click; CSS uses it to flip the chevron icon and adjust the button's background tint. |
| `aria-controls="{id}"` | Set on the button. Points to the `id` of the panel it controls — required so screen readers can navigate from the button to the content region. |
| `aria-labelledby="{id}"` | Set on the content `<div>`. Points back to the controlling button's `id`. |
| `hidden` | HTML attribute on the content `<div>`. Hides the content from layout when the panel is collapsed. Toggled by the USWDS JS in sync with `aria-expanded`. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `default` \| `bordered` | `default` | When `bordered`, applies `usa-accordion--bordered` to the wrapper. |
| `items` | `Array<{title, content, open}>` | 3-item sample (constitutional amendments) | List of panels. `open: true` sets that panel's initial state to expanded. |
| `headingLevel` | `h1`–`h6` | `h4` | Heading element wrapping each panel's button. Adjust to match the page outline. |
| `ariaLabel` | string | `""` | Optional `aria-label` for the wrapper. Useful when there are multiple accordions on a page. |
| `role` | `none` \| `group` \| `region` | `none` | Optional ARIA role on the wrapper. Use `region` when the accordion is a major page landmark; otherwise omit. |

There is no documented prop for `data-allow-multiple`; add it directly to the wrapper markup when needed.

## Accessibility

- Each panel button must carry `aria-expanded="true"` (open) or `aria-expanded="false"` (closed). The USWDS JS keeps this attribute in sync with the visible state — do not toggle it manually elsewhere.
- Each button has `aria-controls` pointing to the `id` of its content panel; each content panel has `aria-labelledby` pointing back to the button's `id`. Both directions are required.
- The button must be wrapped in a heading element (`<h2>`–`<h6>`) so screen readers announce "Heading level N, button, {title}, expanded/collapsed". The default in the MDWDS Storybook is `<h4>`. **Adjust the heading level so it fits the surrounding page outline** — `<h2>` if the accordion is the section heading itself, `<h3>` under an `<h2>` section, `<h4>` under an `<h3>`, etc. See `cdn/composition.md` for the page-wide hierarchy rule.
- The accordion's collapse mechanism uses the HTML `hidden` attribute on the content `<div>`, which removes it from the accessibility tree as well as from layout. Don't use `display: none` via inline styles instead — `hidden` is the supported pattern.
- When there are multiple accordion groups on one page, give each wrapper a distinct `aria-label` so screen-reader users can tell them apart in landmark navigation.

## JS requirements

`usa-accordion` **requires `mdwds-core.js` to function.** Without it:

- Clicking a panel header does nothing — the button has no toggle behavior, so the `aria-expanded` attribute never changes and the `hidden` attribute is never removed from the content `<div>`.
- Panels stay in whatever state the markup specifies on page load. A panel that starts collapsed (`hidden` present, `aria-expanded="false"`) stays collapsed forever; a panel that starts expanded stays expanded.
- The chevron icon does not animate or flip because its rotation is driven by the `aria-expanded` attribute.
- `data-allow-multiple` has no effect — there is no JS to enforce either the single-open default or the multi-open variant.

`mdwds-core.js` is loaded from the CDN in the `<head>` of every page; see `cdn/setup.md`. If you must support a no-JS audience, render any critical content outside the accordion or pre-open the panel containing it via `aria-expanded="true"` and an unset `hidden` attribute.

## Common mistakes

1. **Forgetting to load `mdwds-core.js`** — the accordion is markup-correct but inert; nothing expands or collapses on click.
2. **Setting `aria-expanded="false"` but omitting `hidden`** (or vice versa) on initial state — the two attributes must agree, or the panel renders inconsistently before the JS hydrates.
3. **Wrapping the button in a `<div>` instead of a heading element** — breaks screen-reader navigation (no heading-level announcement) and violates the USWDS pattern. Always use `<h2>`–`<h6>` for the button wrapper.
4. **Copying `<h4>` from the story example without checking the page outline** — produces a skipped heading level (e.g., `<h2>` section followed directly by an `<h4>` accordion). Use `<h3>` instead in that case.
5. **Using the same `id` on multiple panels** — `aria-controls` and `aria-labelledby` rely on unique IDs. Duplicate IDs break the relationship and cause USWDS JS to toggle the wrong panel.
6. **Nesting panels inside per-panel `<div>` wrappers** — the heading and the content `<div>` must be flat siblings inside the `usa-accordion` wrapper. Adding an extra wrapper between them breaks the USWDS JS's panel-pairing logic.
7. **Mixing `usa-accordion` and `maryland-accordion` markup** — they have different DOM and class names. Pick one component and use its full structure; do not splice classes between them.
