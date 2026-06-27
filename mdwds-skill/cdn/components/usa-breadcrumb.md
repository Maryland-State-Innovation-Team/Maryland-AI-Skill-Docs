# usa-breadcrumb

The plain USWDS breadcrumb — a horizontal trail of links separated by a CSS-rendered triangle/arrow, with each item showing the path back to the homepage.

> **Prefer `maryland-breadcrumb` on Maryland-branded pages.** The MDWDS variant adds Maryland-specific styling, both light + dark color modes (for use inside the hero), and shows all items on mobile instead of collapsing to a "back" link. Use `usa-breadcrumb` only when you specifically want plain USWDS styling. See `cdn/components/maryland-breadcrumb.md`.

## What it looks like

A horizontal flex row of small links separated by a USWDS CSS-rendered triangular separator (a chevron-like arrow generated via `::before` pseudo-element). Each link is 14-16px Source Sans, color `primary` (Maryland blue from the MDWDS CDN's primary token).

- **Default desktop layout:** All items visible, each followed by a small triangle separator.
- **Default mobile layout (under 480px):** USWDS hides all items except the second-to-last (the parent), prefixed with a left-pointing back arrow icon, so users see "← Federal Contracting" pointing back to the parent. The current page and earlier ancestors are hidden via `usa-sr-only`.
- **With `usa-breadcrumb--wrap`:** Forces multi-line wrapping at narrow widths instead of the back-arrow collapse.
- **Current page** (`usa-current` on the `<li>`): not a link. The `<a>` inside renders as plain text with no underline; the trailing separator is hidden.

The styles come from upstream USWDS — colors, separator shape, and mobile collapse logic are all USWDS defaults.

## Variants

| Variant | Visual |
|---|---|
| Default | Standard horizontal trail with mobile-collapse to back-arrow + parent only. |
| `usa-breadcrumb--wrap` | Wraps to multiple lines on narrow viewports instead of collapsing. |
| With RDFa | Adds schema.org `BreadcrumbList` metadata for Google rich results. |

## Default markup

```html
<nav class="usa-breadcrumb" aria-label="Breadcrumbs">
  <ol class="usa-breadcrumb__list">
    <li class="usa-breadcrumb__list-item">
      <a href="/" class="usa-breadcrumb__link">Home</a>
    </li>
    <li class="usa-breadcrumb__list-item">
      <a href="/business" class="usa-breadcrumb__link">Business</a>
    </li>
    <li class="usa-breadcrumb__list-item">
      <a href="/business/licenses" class="usa-breadcrumb__link">Licenses</a>
    </li>
    <li class="usa-breadcrumb__list-item usa-current" aria-current="page">
      <a href="/business/licenses/professional" class="usa-breadcrumb__link">Professional license</a>
    </li>
  </ol>
</nav>
```

## Markup — wrapping variant

```html
<nav class="usa-breadcrumb usa-breadcrumb--wrap" aria-label="Breadcrumbs">
  <ol class="usa-breadcrumb__list">
    <!-- ...same items as default... -->
  </ol>
</nav>
```

## Markup — with RDFa SEO metadata

```html
<nav class="usa-breadcrumb" aria-label="Breadcrumbs">
  <ol class="usa-breadcrumb__list" vocab="http://schema.org/" typeof="BreadcrumbList">
    <li property="itemListElement" typeof="ListItem" class="usa-breadcrumb__list-item">
      <a property="item" typeof="WebPage" href="/" class="usa-breadcrumb__link">
        <span property="name">Home</span>
      </a>
      <meta property="position" content="1" />
    </li>
    <li property="itemListElement" typeof="ListItem" class="usa-breadcrumb__list-item usa-current" aria-current="page">
      <a property="item" typeof="WebPage" href="/agencies" class="usa-breadcrumb__link">
        <span property="name">Maryland agencies</span>
      </a>
      <meta property="position" content="2" />
    </li>
  </ol>
</nav>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-breadcrumb` | The outer `<nav>`. USWDS layout: flex row with `body-3` (~16px) typography, base spacing. Themed link color comes from `primary` (Maryland blue). |
| `usa-breadcrumb--wrap` | Modifier that disables mobile-collapse behavior. All items wrap to multiple lines instead of hiding behind a back-arrow. |
| `usa-breadcrumb__list` | The `<ol>`. No list bullets, no margins. Flex container. |
| `usa-breadcrumb__list-item` | Each `<li>`. Inline-flex. Adds a CSS triangle separator after each item via `::before` (which is positioned absolutely on the *next* item). On mobile (<480px), all items except the parent are visually hidden via `usa-sr-only` — only the second-to-last item shows as "← {parent}". |
| `usa-breadcrumb__link` | The `<a>` inside each `<li>`. Color `primary`, underline by default, no underline on hover. |
| `usa-current` | Marker on the current page's `<li>`. Suppresses the trailing separator, removes underline from the link, makes the text non-actionable visually. **Pair with `aria-current="page"` on the `<li>`.** |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `pages` | array of `string` | sample 4-item trail | Items in order. Last item is treated as current page. |
| `wrapping` | bool | `false` | Adds `usa-breadcrumb--wrap` modifier. |
| `rdfa` | bool | `false` | Adds schema.org RDFa attributes for SEO. |

## Heading level adjustment

Breadcrumbs contain no heading. The `<nav aria-label="Breadcrumbs">` is the landmark. Don't add an `<h2>` titled "Breadcrumb."

## Common mistakes

1. **Using `usa-breadcrumb` inside a Maryland-themed page when you wanted `maryland-breadcrumb`** — the two look subtly different (separator shape, mobile behavior, color modes). On Maryland.gov agency pages, prefer `maryland-breadcrumb`.
2. **Forgetting `aria-current="page"` on the last `<li>`** — without it, the `usa-current` class is only visual; screen-reader users won't know which item is the current page.
3. **Linking the current page back to itself** — the current item's anchor should be the current page (or omit the `href` entirely). USWDS still styles the `<a>` as non-link inside a `usa-current` parent.
4. **Putting separators in the markup** — the chevron/triangle is a CSS `::before` pseudo-element. Don't hard-code "›" or "/" between items.
5. **Using `<ul>` instead of `<ol>`** — breadcrumbs are ordered (the path from root to current page). USWDS expects an `<ol>` element.
6. **Mixing `usa-breadcrumb` and `maryland-breadcrumb` classes on the same nav** — that's actually how `maryland-breadcrumb` is structured. But applying just `maryland-breadcrumb` without the `usa-breadcrumb` base means none of the USWDS layout applies. See `cdn/components/maryland-breadcrumb.md` for the dual-class pattern.
7. **Skipping the `<nav>` wrapper** — without it, no landmark, no `aria-label`, no breadcrumb semantics. Just a bare list.
