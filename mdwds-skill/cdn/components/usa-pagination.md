# usa-pagination

USWDS pagination control — previous-arrow, page numbers, optional ellipses, next-arrow. Used at the bottom of listing pages, search results, and any paginated collection.

> MDWDS doesn't have a Maryland-specific pagination variant. Pagination styles come from upstream USWDS — the colors and typography are USWDS defaults, themed to match Maryland's primary-blue token. Use this component as-is.

## What it looks like

A horizontal flex row centered on the page. Each "page" is an inline element — a number, an ellipsis, or a prev/next arrow.

- **Page number links** — small square-ish buttons with 1px transparent border, 16px font. Hover/focus: text Maryland blue (`primary`), background `base-lightest`. Plain number, no `#` prefix.
- **Current page** (`usa-current`) — Maryland blue background pill with white text, semibold. Marked with `aria-current="page"`.
- **Previous / Next arrows** — text labels ("Previous" / "Next") with a leading/trailing chevron icon. On mobile, the labels may collapse to icon-only depending on viewport.
- **Ellipsis** — three centered dots representing skipped page ranges. Rendered as `<span>…</span>` inside a `<li class="usa-pagination__item usa-pagination__overflow">` with `aria-label="ellipsis indicating non-visible pages"`.

The pagination is wrapped in a `<nav>` with `aria-label` (default "Pagination") so screen readers can identify the landmark.

## Variants

| Variant | Visual |
|---|---|
| `default` | Bounded: shows first page, ellipsis, surrounding pages, ellipsis, last page (e.g., `1 … 8 9 [10] 11 … 24`). Indicates a known total. |
| `unbounded` | Trailing ellipsis only (e.g., `1 [2] 3 4 5 …`). Used when total page count is unknown or computed lazily. |

Both variants use the same markup; only the page-list contents differ.

## Default markup

```html
<nav class="usa-pagination" aria-label="Pagination">
  <ul class="usa-pagination__list">

    <!-- Previous arrow -->
    <li class="usa-pagination__item usa-pagination__arrow">
      <a href="?page=9" class="usa-pagination__link usa-pagination__previous-page" aria-label="Previous page">
        <span class="usa-pagination__link-text">Previous</span>
      </a>
    </li>

    <!-- First page -->
    <li class="usa-pagination__item usa-pagination__page-no">
      <a href="?page=1" class="usa-pagination__button" aria-label="Page 1">1</a>
    </li>

    <!-- Leading ellipsis -->
    <li class="usa-pagination__item usa-pagination__overflow" aria-label="ellipsis indicating non-visible pages">
      <span>…</span>
    </li>

    <!-- Surrounding pages -->
    <li class="usa-pagination__item usa-pagination__page-no">
      <a href="?page=8" class="usa-pagination__button" aria-label="Page 8">8</a>
    </li>
    <li class="usa-pagination__item usa-pagination__page-no">
      <a href="?page=9" class="usa-pagination__button" aria-label="Page 9">9</a>
    </li>

    <!-- Current page -->
    <li class="usa-pagination__item usa-pagination__page-no">
      <a href="?page=10" class="usa-pagination__button usa-current" aria-label="Page 10" aria-current="page">10</a>
    </li>

    <li class="usa-pagination__item usa-pagination__page-no">
      <a href="?page=11" class="usa-pagination__button" aria-label="Page 11">11</a>
    </li>

    <!-- Trailing ellipsis -->
    <li class="usa-pagination__item usa-pagination__overflow" aria-label="ellipsis indicating non-visible pages">
      <span>…</span>
    </li>

    <!-- Last page -->
    <li class="usa-pagination__item usa-pagination__page-no">
      <a href="?page=24" class="usa-pagination__button" aria-label="Page 24">24</a>
    </li>

    <!-- Next arrow -->
    <li class="usa-pagination__item usa-pagination__arrow">
      <a href="?page=11" class="usa-pagination__link usa-pagination__next-page" aria-label="Next page">
        <span class="usa-pagination__link-text">Next</span>
      </a>
    </li>
  </ul>
</nav>
```

## Markup — unbounded variant

```html
<nav class="usa-pagination" aria-label="Pagination">
  <ul class="usa-pagination__list">
    <li class="usa-pagination__item usa-pagination__arrow">
      <a href="?page=1" class="usa-pagination__link usa-pagination__previous-page" aria-label="Previous page">
        <span class="usa-pagination__link-text">Previous</span>
      </a>
    </li>
    <li class="usa-pagination__item usa-pagination__page-no">
      <a href="?page=1" class="usa-pagination__button" aria-label="Page 1">1</a>
    </li>
    <li class="usa-pagination__item usa-pagination__page-no">
      <a href="?page=2" class="usa-pagination__button usa-current" aria-label="Page 2" aria-current="page">2</a>
    </li>
    <li class="usa-pagination__item usa-pagination__page-no">
      <a href="?page=3" class="usa-pagination__button" aria-label="Page 3">3</a>
    </li>
    <li class="usa-pagination__item usa-pagination__page-no">
      <a href="?page=4" class="usa-pagination__button" aria-label="Page 4">4</a>
    </li>
    <li class="usa-pagination__item usa-pagination__overflow" aria-label="ellipsis indicating non-visible pages">
      <span>…</span>
    </li>
    <li class="usa-pagination__item usa-pagination__arrow">
      <a href="?page=3" class="usa-pagination__link usa-pagination__next-page" aria-label="Next page">
        <span class="usa-pagination__link-text">Next</span>
      </a>
    </li>
  </ul>
</nav>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-pagination` | The outer `<nav>`. Flex container, horizontally centered, sets baseline typography. |
| `usa-pagination__list` | The `<ul>`. Unstyled list (no bullets, no margins). Flex row centered. |
| `usa-pagination__item` | Each `<li>`. Inline-flex with center alignment. Margin between items. |
| `usa-pagination__arrow` | Modifier for the `<li>` containing Previous or Next. Slightly more left/right margin to separate from numbers. |
| `usa-pagination__page-no` | Modifier for the `<li>` containing a numbered page link. |
| `usa-pagination__overflow` | Modifier for the `<li>` containing the ellipsis. Uses an `aria-label` so screen readers announce it as "ellipsis indicating non-visible pages." |
| `usa-pagination__link` | Generic class on the prev/next anchor — sets the underline-on-hover behavior. |
| `usa-pagination__link-text` | Wrapper around "Previous" / "Next" text. Allows hiding the text at narrow viewports while keeping the icon visible. |
| `usa-pagination__previous-page` | Adds a leading chevron-left icon to the prev anchor. |
| `usa-pagination__next-page` | Adds a trailing chevron-right icon to the next anchor. |
| `usa-pagination__button` | The numbered-page anchor. 1px transparent border by default. Hover: `base-lightest` background, `primary` text. |
| `usa-current` | Marker on the current page's anchor. Inverts visuals: Maryland blue background, white text, semibold. Must pair with `aria-current="page"`. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `default` \| `unbounded` | `default` | Default shows bounded list with leading + trailing ellipsis; unbounded shows trailing ellipsis only and omits known last page. |
| `currentPage` | number | `10` | Active page number. |
| `totalPages` | number | `24` | Total page count. In `unbounded` mode this is treated as a soft limit. |
| `showEllipses` | bool | `true` | Whether to collapse distant page numbers into ellipses. If `false`, all pages render. |
| `ariaLabelPagination` | string | `"Pagination"` | Override the nav landmark label. |

## Heading level adjustment

Pagination contains no heading. It's a navigation landmark via `<nav aria-label="...">` and doesn't need an `<h2>` titled "Pages" or similar.

## Common mistakes

1. **Forgetting `aria-current="page"` on the current page link** — without it, screen-reader users can't tell which page they're on. The `usa-current` class alone is visual; `aria-current` is semantic.
2. **Linking the current page back to itself** — common but harmless. Better practice: make the current page a non-link (`<span class="usa-pagination__button usa-current" aria-current="page">10</span>`), but rendering it as a link with `aria-current` is also acceptable per USWDS.
3. **Omitting per-link `aria-label`** — each `<a>` should have `aria-label="Page N"` so screen readers announce the page number, not just "page". The `<a>10</a>` alone announces as "10 link," not "page 10."
4. **Showing every page when there are 30+ pages** — use `showEllipses: true` to trim. Otherwise the nav overflows and breaks layout.
5. **Rendering pagination inside a `<div>`** — must be `<nav>`. Otherwise no landmark for AT.
6. **Hardcoding `href="#"` on prev/next** — the prev/next links should point to the actual previous/next page query string (`?page=9`). `#` jumps to the top of the page and breaks history.
7. **Forgetting to disable prev on page 1 / next on last page** — either omit the arrow `<li>` entirely on the boundary, or render it without an `href` (a non-link). Don't render an active prev arrow on page 1.
