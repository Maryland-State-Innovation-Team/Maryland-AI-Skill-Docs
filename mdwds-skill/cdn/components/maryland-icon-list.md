# maryland-icon-list

Maryland Design System icon list presents a 1-, 2-, or 3-column grid of items where each item leads with a circular Material Symbols icon, then a heading, description, and optional clickable arrow. Used as a feature grid on agency homepages and topic pages.

> **Use `maryland-icon-list` for a feature grid where each tile leads with a visual icon prefix.** For service tiles with photos and CTA buttons, use `maryland-card`. For two-column featured-link groups with arrow rows, use `maryland-highlight`. For a flat list of related links, use `maryland-link-collection`.

## What it looks like

The icon list is a `<section>` with an optional header (title + description + "more" link in a CSS-grid layout that places title above on mobile, title + side-by-side description/link at tablet+) and a 1–3 column grid of items.

Each item is a flex-column tile:

- **Circular icon** — 80px square with `border-radius: 50%`, `base-lightest` (cream) background, 1px white inset outline, and a 48px Material Symbols glyph in `secondary` (Maryland gold). Falls back to a CSS-mask via `--icon-url` custom property if no inline SVG is provided.
- **Item title** (`<h3>`) — applies the MDWDS `h4` mixin (Source Sans semibold, ~16–18px). 48px bottom margin.
- **Description** — body-7 (20px). 16px bottom margin.
- **Item footer** (only when `linkItems: true`) — bottom-aligned via `margin-top: auto`. Holds a small forward-arrow icon flush right, with a 1px `gray-40` underline that thickens to 2px Maryland blue on hover/focus. Arrow translates right 12px and recolors to Maryland blue on hover.

Layout breakpoints:

- 1 column on mobile.
- 2 columns at tablet (640px+).
- 3 columns at desktop (1024px+) when the container is wide enough (>8/12 of the row).

When `linkItems: true`, each `<li>` wraps its content in an `<a>`, making the entire tile a clickable target.

## When to use

- 6–9 service categories on an agency homepage ("Permits", "Licenses", "Inspections", ...).
- Topic exploration grid where icons help visual scanning.
- Comparing feature tiles where each tile leads to a deeper page.

Avoid icon lists for single-CTA promotional blocks (use `maryland-promo`), long flat lists (use `maryland-link-collection`), or items with prominent photos (use `maryland-card`).

## Default markup

```html
<section class="maryland-icon-list" aria-labelledby="il-1">
  <div class="maryland-icon-list__header">
    <h2 id="il-1" class="maryland-icon-list__title">Services for Maryland businesses</h2>
    <div class="maryland-icon-list__description">
      Find the resources your business needs — from registering an LLC to bidding on state contracts.
    </div>
    <a class="maryland-link" href="/business">See all business services</a>
  </div>
  <ul class="maryland-icon-list__list">
    <li class="maryland-icon-list__item maryland-icon-list__item--linked">
      <a href="/business/register" class="maryland-icon-list__link">
        <span class="maryland-icon-list__icon" aria-hidden="true">
          <!-- inline Material Symbols SVG, e.g. "domain" -->
          <svg viewBox="0 -960 960 960"><path d="..." /></svg>
        </span>
        <h3 class="maryland-icon-list__item-title">Register a business</h3>
        <p class="maryland-icon-list__item-description">Form an LLC, corporation, or sole proprietorship through SDAT.</p>
        <div class="maryland-icon-list__item-footer">
          <span class="maryland-icon-list__arrow" aria-hidden="true"></span>
        </div>
      </a>
    </li>
    <li class="maryland-icon-list__item maryland-icon-list__item--linked">
      <a href="/business/taxes" class="maryland-icon-list__link">
        <span class="maryland-icon-list__icon" aria-hidden="true">
          <svg viewBox="0 -960 960 960"><path d="..." /></svg>
        </span>
        <h3 class="maryland-icon-list__item-title">File business taxes</h3>
        <p class="maryland-icon-list__item-description">E-file annual returns through the Comptroller of Maryland.</p>
        <div class="maryland-icon-list__item-footer">
          <span class="maryland-icon-list__arrow" aria-hidden="true"></span>
        </div>
      </a>
    </li>
    <li class="maryland-icon-list__item maryland-icon-list__item--linked">
      <a href="/business/permits" class="maryland-icon-list__link">
        <span class="maryland-icon-list__icon" aria-hidden="true">
          <svg viewBox="0 -960 960 960"><path d="..." /></svg>
        </span>
        <h3 class="maryland-icon-list__item-title">Apply for permits</h3>
        <p class="maryland-icon-list__item-description">Building, environmental, and professional licensing through OneStop.</p>
        <div class="maryland-icon-list__item-footer">
          <span class="maryland-icon-list__arrow" aria-hidden="true"></span>
        </div>
      </a>
    </li>
  </ul>
</section>
```

## Markup — non-linked items

When items aren't clickable, the wrapping element becomes a `<span>` instead of `<a>`, and the footer is omitted. Drop the `--linked` modifier:

```html
<li class="maryland-icon-list__item">
  <span class="maryland-icon-list__link">
    <span class="maryland-icon-list__icon" aria-hidden="true">
      <svg viewBox="0 -960 960 960"><path d="..." /></svg>
    </span>
    <h3 class="maryland-icon-list__item-title">24/7 hotline</h3>
    <p class="maryland-icon-list__item-description">Call 211 anytime for help connecting to state services.</p>
  </span>
</li>
```

## Markup — using --icon-url instead of inline SVG

If you can't ship inline SVG, point `--icon-url` at a published icon URL. The icon `<span>` will use that URL as a CSS mask:

```html
<span
  class="maryland-icon-list__icon"
  aria-hidden="true"
  style="--icon-url: url('https://cdn.maryland.gov/mdwds-icons/latest/svg/outlined/400/star.svg');"
></span>
```

Without `--icon-url`, the fallback is `broken_image.svg`.

## What each class does

| Class | Effect |
|---|---|
| `maryland-icon-list` | Base `<section>`. Applies `block-spacing` and `grid-container`. |
| `maryland-icon-list__header` | Header CSS grid. On mobile: stacked rows (title/description/link). On tablet+: title on top spanning both columns, description in left column (3fr), link in right column (1fr). 64px bottom margin. |
| `maryland-icon-list__title` | The `<h2>`. Uses the `h2` mixin (Merriweather light, 32–48px responsive). 32px bottom margin. At widescreen, scales up to heading-14 (40px); falls back to heading-12 (32px) when nested in a sidebar. |
| `maryland-icon-list__description` | Description block. body-7 (20px) / body-9 (22px at tablet+). |
| `maryland-icon-list__header > a` | The header "more" link. body-6 (20px). On tablet+: right-aligned and end-justified inside the header grid. |
| `maryland-icon-list__list` | The items `<ul>`. CSS grid: 1 col → 2 col (tablet) → 3 col (desktop, when container is wide). 64px gap. |
| `maryland-icon-list__item` | Each `<li>`. Display flex stretch. |
| `maryland-icon-list__item--linked` | Marker class indicating the item wraps an `<a>`. Used as a structural marker; no direct style. |
| `maryland-icon-list__link` | The clickable (or non-clickable span) wrapper. Display flex column. 100% width. `text-decoration: none` and `base-darkest` color. On hover, the footer underline thickens to Maryland blue and the arrow translates right 12px and recolors. Focus ring 2px primary, 2px offset. |
| `maryland-icon-list__icon` | Circular icon container. 80×80px, `border-radius: 50%`, `base-lightest` background, 1px white inset outline. Inner SVG is 48×48px filled with `secondary` color (Maryland gold). Fallback: mask-image via `--icon-url` CSS var. |
| `maryland-icon-list__item-title` | Item heading (`<h3>`). Applies the MDWDS `h4` mixin (Source Sans semibold, ~18px). 48px bottom margin. `text-trim` to remove inherited line-height baggage. |
| `maryland-icon-list__item-description` | Item body. body-7 (20px). 16px bottom margin. Removes nested first/last child margins. |
| `maryland-icon-list__item-footer` | Bottom footer (linked only). `margin-top: auto` to push to the bottom of the tile. 20px vertical padding. Has a 2px `gray-40` `::after` underline (scaled to 0.5 by default) that animates to full size + Maryland blue on hover. |
| `maryland-icon-list__arrow` | The arrow icon. 24×24px. `base-darkest` color via `arrow_forward` mask (rounded variant). 0.2s ease transform transition. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `title` | string | sample | Section heading. |
| `hideTitle` | bool | false | Visually hide the title (adds `usa-sr-only`). |
| `description` | string | sample | Description text. |
| `moreLinkText` | string | — | "More" link label. |
| `moreLinkUrl` | string | — | "More" link URL. Both required for the link to render. |
| `items` | number (2–12) | 6 | Number of items rendered in the documented variants. In hand-written markup, render as many `<li>` as needed. |
| `linkItems` | bool | true | Make each item a link. |

In hand-written markup, supply your own per-item content (heading, description, and icon) for each item.

## Heading level adjustment

- `maryland-icon-list__title` defaults to `<h2>`.
- `maryland-icon-list__item-title` defaults to `<h3>`.

Demote both by one level if the icon list is nested inside another `<h2>`-headed section. Keep classes — they control styling, not outline.

## Common mistakes

1. **Forgetting `aria-hidden="true"` on `.maryland-icon-list__icon`** — the icon is decorative; without `aria-hidden`, screen readers may announce the SVG content as `image`.
2. **Linked items with internal links** — if `linkItems: true`, the entire tile is an `<a>`. Don't add a nested `<a>` inside — it's an accessibility violation. For a tile with multiple links, use `maryland-card--full`.
3. **Mixing icon sources** — pick inline SVG OR `--icon-url` per item, not both. The published CSS branches on `:has(svg)`.
4. **Item title rendered as `<h2>` or `<h4>`** — for the typical 1-`<h1>` + `<h2>` section layout, `<h3>` is correct. Demote only when nested deeper.
5. **More than ~9 items** — gets unwieldy. Either paginate or split into themed groups.
6. **Removing the footer when `linkItems: true`** — the visual hover affordance (the arrow + underline) depends on the footer. Don't strip it.
