# maryland-visual-link-collection

Maryland Design System visual link collection renders a grid of `maryland-card--linked` cards (image, heading, description, footer arrow), each entirely clickable. It's the "card grid" version of `maryland-link-collection` — same flat-list intent, but with photo-led tiles.

> **Use `maryland-visual-link-collection` for a service-directory or topic-hub grid where each tile leads with an image.** The component is essentially a styled `maryland-card-group` of `linked` cards plus a header. For per-tile separate text-only links, use `maryland-link-collection`. For richer cards with subheadings and buttons, build a `maryland-card-group` directly. For a non-linked icon grid, use `maryland-icon-list`.

## What it looks like

A `<section>` containing an optional header (title + description + "more" link) and a `<ul class="maryland-card-group">` of linked cards. The card group layout is provided by `maryland-card`'s own grid:

- 1 column at mobile.
- 2 columns at tablet (640px+).
- 3 columns at desktop (1024px+) when the container is wide; 2 when nested in a ≤8/12 column.

Each card uses the `linked` variant: the entire card is one `<a>` with an arrow icon in the footer. Hover slides the icon right ~12px and turns the footer's bottom border Maryland blue. Cards have an image at the top (16:9 by default — see `maryland-card.md` for variants), a 22px Source Sans semibold heading, a 16px body description, and a footer with a forward-arrow icon (or `open_in_new` for external URLs).

The component re-uses `maryland-card-group__header` markup (also used by `maryland-card-group` directly), so the header treatment matches other card collections on the page.

## When to use

- "Featured services" with photos on an agency homepage.
- Topic-hub navigation where each tile represents a destination page.
- "Latest updates" tile grids with banner photography.

Don't use it for non-clickable text content (use `usa-prose`) or for collections where each item has multiple sub-links (use `maryland-card--full`).

## Default markup

```html
<section class="maryland-visual-link-collection" aria-labelledby="vlc-1">
  <div class="maryland-card-group__header">
    <div class="maryland-card-group__header-content">
      <h2 id="vlc-1" class="maryland-card-group__title">Latest updates</h2>
      <p class="maryland-card-group__description">
        Maryland's newest programs, grants, and resources — refreshed weekly.
      </p>
    </div>
    <div class="maryland-card-group__more-link">
      <a class="maryland-link" href="/updates">See all updates</a>
    </div>
  </div>

  <ul class="maryland-card-group">
    <li class="maryland-card maryland-card--linked">
      <a href="/news/farm-drought" class="maryland-card__link" aria-label="Federal Financial Assistance for Farmers Affected by Drought">
        <div class="maryland-card__container">
          <div class="maryland-card__media">
            <div class="maryland-card__img">
              <img src="/img/farmland.jpg" alt="Maryland farmland" />
            </div>
          </div>
          <div class="maryland-card__header">
            <h3 class="maryland-card__heading">Federal Financial Assistance for Farmers Affected by Drought</h3>
          </div>
          <div class="maryland-card__body">
            <p>USDA and Maryland Department of Agriculture announce supplemental aid for affected counties.</p>
          </div>
          <div class="maryland-card__footer maryland-card__footer--right">
            <span class="maryland-card__icon maryland-card__icon--arrow" aria-hidden="true"></span>
          </div>
        </div>
      </a>
    </li>

    <li class="maryland-card maryland-card--linked">
      <a href="https://example.com/climate" class="maryland-card__link" aria-label="Environmental Resilience in the Face of Climate Change (external link)">
        <div class="maryland-card__container">
          <div class="maryland-card__media">
            <div class="maryland-card__img">
              <img src="/img/wetlands.jpg" alt="Maryland wetlands at sunrise" />
            </div>
          </div>
          <div class="maryland-card__header">
            <h3 class="maryland-card__heading">Environmental Resilience in the Face of Climate Change</h3>
          </div>
          <div class="maryland-card__body">
            <p>Maryland's Department of the Environment publishes its 2026 resilience report.</p>
          </div>
          <div class="maryland-card__footer maryland-card__footer--right">
            <span class="maryland-card__icon maryland-card__icon--external-link" aria-hidden="true"></span>
          </div>
        </div>
      </a>
    </li>

    <li class="maryland-card maryland-card--linked">
      <a href="/bay/protection" class="maryland-card__link" aria-label="Support for Chesapeake Bay Legacy Act to Protect the Bay">
        <div class="maryland-card__container">
          <div class="maryland-card__media">
            <div class="maryland-card__img">
              <img src="/img/bay.jpg" alt="Chesapeake Bay shoreline" />
            </div>
          </div>
          <div class="maryland-card__header">
            <h3 class="maryland-card__heading">Support for Chesapeake Bay Legacy Act to Protect the Bay</h3>
          </div>
          <div class="maryland-card__body">
            <p>Governor signs the Bay Legacy Act funding 25 new protection programs across the watershed.</p>
          </div>
          <div class="maryland-card__footer maryland-card__footer--right">
            <span class="maryland-card__icon maryland-card__icon--arrow" aria-hidden="true"></span>
          </div>
        </div>
      </a>
    </li>
  </ul>
</section>
```

The icon glyph is picked automatically by the component: external URLs (`http*`) get the `--external-link` icon; internal URLs default to `--arrow`. Override per-item by setting `icon` on the props.

## What each class does

| Class | Effect |
|---|---|
| `maryland-visual-link-collection` | Base `<section>`. Applies `block-spacing` and `grid-container`. |
| `maryland-card-group__header` | Header block shared with `maryland-card-group`. At tablet-lg+, places title/description on the left and more-link on the right. |
| `maryland-card-group__header-content` | Wraps title + description. |
| `maryland-card-group__title` | The `<h2>`. Uses the `h2` mixin (Merriweather, 32–48px). |
| `maryland-card-group__description` | Description paragraph. 16–22px responsive. |
| `maryland-card-group__more-link` | More-link wrapper. Right-aligned at tablet-lg+. |
| `maryland-card-group` | The `<ul>` grid. Provides the 1/2/3-column responsive layout, list reset, and `max-width: none` override against `usa-prose`. |
| `maryland-card maryland-card--linked` | The `linked` variant of `maryland-card`. See `cdn/components/maryland-card.md` for the full anatomy. The whole card is one `<a>`; an arrow icon sits in the footer. |
| `maryland-card__link` | The wrapping `<a>` inside `--linked`. Removes underline, inherits color, applies 4px focus outline, hover effects on footer + icon. |
| `maryland-card__container` | White-background flex column inside the card. |
| `maryland-card__media` / `__img` | Image wrapper. Square-cornered (no border-radius). |
| `maryland-card__header` / `__heading` | Heading area. Body font, 22px semibold inside `--linked`. |
| `maryland-card__body` | Body paragraph. ~16px. |
| `maryland-card__footer maryland-card__footer--right` | Right-aligned footer holding the icon. |
| `maryland-card__icon maryland-card__icon--arrow` / `--external-link` / `--download` | Icon glyph. Slides ~12px right on hover; recolors to Maryland blue. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `title` | string | — | Section heading. |
| `description` | string | — | Section description. |
| `moreLinkText` | string | `"More Link"` | More-link label. |
| `moreLinkUrl` | string | — | More-link URL. |
| `items` | `Array<{title, description?, url, imageUrl?, imageAlt?, icon?: "arrow" \| "external-link"}>` | — | Card data. Defaults `icon` to `external-link` when `url` starts with `http`, else `arrow`. |
| `enableAnalytics` | bool | false | Add `data-ga-*` attributes to the link. |
| `gaCategory` | string | — | GA category. |

## Heading level adjustment

`maryland-card-group__title` defaults to `<h2>`; `maryland-card__heading` defaults to `<h3>`. Demote both by one level when nested under an existing `<h2>`-led section.

## Common mistakes

1. **Forgetting the `aria-label` on `maryland-card__link`** — for a fully-clickable card, the accessible name should combine title + description (+ "external link" when applicable). Without it, the link text alone may not be descriptive enough.
2. **Internal links inside a linked card** — the `<a>` already wraps the whole card; nested anchors are an accessibility violation.
3. **Using `maryland-card-group__header` from this component but `maryland-card-group` items styled with a different variant** — keep all cards in the group on the same variant. Mixing `--linked` with `--simple` or `--media` confuses hover and layout expectations.
4. **Custom shadow or border via inline `<style>`** — MDWDS cards intentionally have no border or shadow; the hover state communicates clickability. Adding a custom border breaks the design.
5. **Reaching for this when you only need text links** — use `maryland-link-collection` for text-only grids; visual cards are heavier and slower to scan.
