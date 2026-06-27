# maryland-breadcrumb

Maryland-styled breadcrumb trail showing the user's location in the site hierarchy. Comes in **two color variants** because breadcrumbs commonly nest inside a hero with a dark blue background.

> **Use this, not `usa-breadcrumb`, on Maryland-branded pages.** It uses dual classes (`usa-breadcrumb` + `maryland-breadcrumb`) on the same element to extend USWDS styles with Maryland-specific overrides. See `cdn/components/usa-breadcrumb.md` for the plain USWDS version.

## What it looks like

A horizontal trail of links separated by a 24×24px Material `chevron_right` icon. Items wrap to multiple lines on narrow viewports (unlike USWDS, MDWDS shows **all** breadcrumb items even on mobile — USWDS hides everything except the parent on mobile and shows a "back" arrow). Each link is 16px (`body-xs`) normal weight, 1.3 line-height. The current page (last item) is **not** a link — it renders as a `<span>` with `aria-current="page"`, no underline, and truncates with an ellipsis when too long.

### Light variant (default)

- Wrapper: **white** background, full-width.
- Links: color `blue-60v` (Maryland blue), with an underline on the inner `<span>` by default; underline disappears on hover.
- Current page: color `gray-90` (near-black).
- Chevron separator: filled with color `base-darkest`.

### Dark variant

Used **inside the hero** (where the background is `blue-60v` Maryland blue).

- Wrapper: **`blue-60v`** background, full-width. The breadcrumb itself sits on top with transparent background.
- Links: **white**, with underline on the `<span>` by default. Hover removes underline.
- Current page: white, no underline.
- Chevron separator: filled with white.
- Focus rings: switch to the `focus--dark` mixin so they remain visible on the blue background.

In both variants, the wrapper takes 100% width so the colored band stretches edge-to-edge — only the breadcrumb content stays within the page container.

## When to use which variant

- **Light** → Top of a page section outside the hero (e.g., above a long article).
- **Dark** → Inside a `maryland-hero` (the common pattern). The hero's blue background continues seamlessly under the breadcrumb wrapper.

## Default markup — light variant

```html
<div class="maryland-breadcrumb__wrapper maryland-breadcrumb__wrapper--light">
  <nav class="usa-breadcrumb maryland-breadcrumb maryland-breadcrumb--light" aria-label="Breadcrumbs">
    <ol class="usa-breadcrumb__list maryland-breadcrumb__list">
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <a href="/" class="usa-breadcrumb__link maryland-breadcrumb__link">
          <span>Home</span>
        </a>
      </li>
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <a href="/recreation" class="usa-breadcrumb__link maryland-breadcrumb__link">
          <span>Recreation</span>
        </a>
      </li>
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <a href="/recreation/fishing" class="usa-breadcrumb__link maryland-breadcrumb__link">
          <span>Fishing</span>
        </a>
      </li>
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item usa-current" aria-current="page">
        <span class="usa-breadcrumb__link maryland-breadcrumb__link">
          <span>Buy a license</span>
        </span>
      </li>
    </ol>
  </nav>
</div>
```

## Markup — dark variant (inside hero)

```html
<div class="maryland-breadcrumb__wrapper maryland-breadcrumb__wrapper--dark">
  <nav class="usa-breadcrumb maryland-breadcrumb maryland-breadcrumb--dark" aria-label="Breadcrumbs">
    <ol class="usa-breadcrumb__list maryland-breadcrumb__list">
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <a href="/" class="usa-breadcrumb__link maryland-breadcrumb__link">
          <span>Home</span>
        </a>
      </li>
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <a href="/services" class="usa-breadcrumb__link maryland-breadcrumb__link">
          <span>Services</span>
        </a>
      </li>
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item usa-current" aria-current="page">
        <span class="usa-breadcrumb__link maryland-breadcrumb__link">
          <span>Driver's license</span>
        </span>
      </li>
    </ol>
  </nav>
</div>
```

## Markup — with RDFa schema metadata (SEO)

```html
<div class="maryland-breadcrumb__wrapper maryland-breadcrumb__wrapper--light">
  <nav class="usa-breadcrumb maryland-breadcrumb maryland-breadcrumb--light" aria-label="Breadcrumbs">
    <ol class="usa-breadcrumb__list maryland-breadcrumb__list" vocab="http://schema.org/" typeof="BreadcrumbList">
      <li property="itemListElement" typeof="ListItem" class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <a property="item" typeof="WebPage" href="/" class="usa-breadcrumb__link maryland-breadcrumb__link">
          <span property="name">Home</span>
        </a>
        <meta property="position" content="1" />
      </li>
      <li property="itemListElement" typeof="ListItem" class="usa-breadcrumb__list-item maryland-breadcrumb__list-item usa-current" aria-current="page">
        <span property="item" typeof="WebPage" class="usa-breadcrumb__link maryland-breadcrumb__link">
          <span property="name">Annual report</span>
        </span>
        <meta property="position" content="2" />
      </li>
    </ol>
  </nav>
</div>
```

## What each class does

| Class | Effect |
|---|---|
| `maryland-breadcrumb__wrapper` | Outer `<div>` that fills 100% of the container width — this is what makes the colored band stretch edge-to-edge. The MDWDS breadcrumb requires this wrapper; the USWDS version doesn't have it. |
| `maryland-breadcrumb__wrapper--light` | Adds white background to the wrapper. |
| `maryland-breadcrumb__wrapper--dark` | Adds `blue-60v` (Maryland blue) background to the wrapper. |
| `usa-breadcrumb` | USWDS base class on the `<nav>`. Sets list-reset, baseline padding, sr-only fallback for mobile (which MDWDS overrides). |
| `maryland-breadcrumb` | Maryland override — transparent background, MDWDS chevron icon, **shows all items on mobile** (overrides USWDS `sr-only` behavior), uses Material `chevron_right` instead of USWDS's CSS triangle. |
| `maryland-breadcrumb--light` | Light variant. Links `blue-60v`, current page `gray-90`, separator `base-darkest`. |
| `maryland-breadcrumb--dark` | Dark variant. Links + current + separator all white. Adds the `focus--dark` outline mixin so focus is visible on the blue background. |
| `usa-breadcrumb__list` + `maryland-breadcrumb__list` | The `<ol>`. Flex row with 8px row gap / 4px column gap, wrapping enabled, 100% width. Slight 0.025rem left offset to align with body content. |
| `usa-breadcrumb__list-item` + `maryland-breadcrumb__list-item` | Each `<li>`. Inline-flex with center alignment. Generates the chevron separator via a `::after` pseudo (24×24px CSS mask, currentColor-or-override). Removes USWDS's mobile "back arrow" treatment. |
| `usa-breadcrumb__link` + `maryland-breadcrumb__link` | The link or current-page `<span>`. 16px (`body-xs`) normal weight, 1.3 line-height. The inner `<span>` carries the underline; hover removes it. Visited links inherit the link color (don't shift to purple). |
| `usa-current` | Marker class on the current-page `<li>`. Disables underline, truncates the page name with `text-overflow: ellipsis` when too long, prevents the chevron `::after` from rendering after this item. |
| `usa-breadcrumb--wrap` | USWDS-provided modifier. Toggles a wrapping behavior at narrow widths. MDWDS already wraps by default, so this is rarely needed. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `pages` | array of `string` or `{label, href}` | sample 6-item trail | The breadcrumb items in order. The **last item is automatically the current page** and renders as a non-link span. String items become `<a href="#">{string}</a>`. |
| `variant` | `light` \| `dark` | `light` | Color variant. |
| `wrapping` | bool | `false` | Adds `usa-breadcrumb--wrap` for forced wrapping behavior. Usually unnecessary. |
| `rdfa` | bool | `false` | Adds `vocab="http://schema.org/"`, `typeof="BreadcrumbList"`, and per-item `property`/`typeof`/`<meta>` attributes for Google rich-result eligibility. |

## Heading level adjustment

The breadcrumb contains no semantic heading. The `<nav aria-label="Breadcrumbs">` is the landmark; do not add an `<h2>` titled "You are here" or similar.

## Common mistakes

1. **Omitting the `maryland-breadcrumb__wrapper`** — without it, the colored band can't stretch edge-to-edge, and the dark variant won't have a blue background under the breadcrumb when nested in a hero.
2. **Linking the current page** — the last item must be a `<span>` with `aria-current="page"`, not an `<a>`. The `usa-current` class on the `<li>` is what hides the trailing chevron.
3. **Using the light variant inside a hero** — the hero is Maryland blue; light breadcrumbs become invisible. Use the dark variant inside `maryland-hero`.
4. **Missing the dual classes** (`usa-breadcrumb maryland-breadcrumb`) — both are required. The `maryland-*` class extends/overrides USWDS; without the USWDS base class, the list-reset and separator positioning fall back to browser defaults.
5. **Wrapping individual item text directly in the link without `<span>`** — the underline-on-hover logic targets `.maryland-breadcrumb__link span`. Plain text inside the `<a>` won't underline.
6. **Building a "Home > Page" trail that's only two items** — short trails work, but a breadcrumb with only the current page (one item) provides no value. Skip the breadcrumb on top-level pages.
7. **Putting the breadcrumb above the hero rather than inside it** — the canonical Maryland pattern is the breadcrumb nested **inside** `maryland-hero` so it shares the blue background. See `cdn/components/maryland-hero.md`.
