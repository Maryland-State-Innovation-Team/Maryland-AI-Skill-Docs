# maryland-listing-page

Maryland Design System listing page is a **page-level pattern**, not a single component. It composes a filter form, a result summary, a vertical list of `maryland-listing-item` rows, and a USWDS pagination block — the standard shape of a news/events/locations/contacts/documents listing page on Maryland.gov.

> **This file documents the listing-page primitives (`maryland-listing__body`, `__form`, `__list`, `maryland-listing-item`) for direct use.** For the fully-assembled page with header, hero, sidebar, and footer, use `cdn/recipes/listing-page.md` — that recipe shows where this pattern sits in the page shell. If you only need a card-grid-style list (no filters, no pagination), use `maryland-automatic-list` or `maryland-card-group` instead.

## What it looks like

The listing page sits inside `<main>` and consists of (top to bottom):

1. **`maryland-listing__body`** — Optional intro paragraph wrapper. Renders a `usa-prose`-styled HTML block above the filter form. 48px bottom margin.
2. **`maryland-listing__form`** — A flex-row of filter controls (USWDS `usa-input`, `usa-select`, and `usa-button`). Wraps onto multiple rows at narrow widths; aligns end of inputs at the same line. 56/64px bottom margin.
3. **`maryland-listing__list-summary`** — A `role="status" aria-live="polite"` paragraph showing the result count ("Showing 151-175 of 315 results"). body-4 (16px) italic.
4. **`maryland-listing__list`** — The list `<ul>` of items. 32px top margin, 16/32px bottom margin, with a 1px `base-light` bottom border separating the list from pagination.
5. **`usa-pagination`** (USWDS) — Pagination controls below the list.

Each `maryland-listing-item` is a 12-col row with:

- **Optional image** on the left at mobile-lg+ (small: 180×240px; default: 591×333px). On mobile, image stacks above content.
- **Content column** on the right: optional uppercase eyebrow (category/type label), title (`<h2>` per item, linked, with a primary-color hover underline), optional subtitle (body-6 semibold), optional date row, and a description (HTML allowed via `usa-prose`).
- For document items, the title contains the document-title typography spans (title + " — " + "PDF 2.1MB"), and a download icon SVG appears next to the title.

Items are separated by a 1px `base-light` top border (except when the preceding item has a full-size image; in that case the border is transparent).

The listing-item content is responsive: the image and content columns flex-wrap, gap 16/32px row and 24/32/64px column at mobile/mobile-lg/tablet.

## Variants — by content type

The documented variants surface five content types via the `contentType` prop (`location`, `contact`, `event`, `news`, `document`). Each chooses sample data, but the underlying markup is the same — the variation is in which fields are filled (eyebrow vs. date, etc.).

Use the right combination of fields per content type:

| Content type | Eyebrow | Date | Subtitle | Description |
|---|---|---|---|---|
| `news` | Yes (e.g., "Press Release") | Yes | No | Yes |
| `event` | Yes (e.g., "Webinar") | Yes (e.g., "Thursday, October 23, 2026") | No | Yes |
| `document` | Yes (e.g., "Annual Report") | No | No | Yes (with download icon) |
| `location` | No | No | No | Yes (`<address>`) |
| `contact` | No | No | Yes (role) | Yes (`<dl>` of contact links) |

## When to use

- The body of a news, events, locations, contacts, or documents listing page.
- Search-results-like pages with filters and pagination (when not using site search / `maryland-search-results`).

Avoid the listing page pattern for short lists (< 10 items, no pagination needed) — use `maryland-link-collection`, `maryland-card-group`, or `maryland-automatic-list` instead.

## Default markup — listing page contents

```html
<div class="maryland-listing__body usa-prose">
  <p>Browse the latest press releases and news from Maryland state government.</p>
</div>

<form class="maryland-listing__form">
  <div class="maryland-listing__filter maryland-listing__filter--input">
    <label class="usa-label" for="news-search">Search news</label>
    <input class="usa-input" id="news-search" name="q" size="35" type="text" />
  </div>
  <div class="maryland-listing__filter maryland-listing__filter--select">
    <label class="usa-label" for="news-category">Filter by category</label>
    <select class="usa-select" name="category" id="news-category">
      <option value="all">All categories</option>
      <option value="press-release">Press release</option>
      <option value="public-notice">Public notice</option>
      <option value="media-advisory">Media advisory</option>
    </select>
  </div>
  <button class="usa-button" type="submit">Filter</button>
</form>

<div class="maryland-listing__list-summary" role="status" aria-live="polite" aria-atomic="true">
  <p>Showing 151-175 of 315 results</p>
</div>

<ul class="maryland-listing__list">
  <li class="maryland-listing-item">
    <article class="maryland-listing-item__container" id="item-1" aria-labelledby="item-1-title">
      <div class="maryland-listing-item__image maryland-listing-item__image--small">
        <figure>
          <img src="/img/quantum.jpg" alt="Quantum research facility opening" />
        </figure>
      </div>
      <div class="maryland-listing-item__content">
        <div class="maryland-listing-item__eyebrow">Press Release</div>
        <a class="maryland-listing-item__title" href="/news/microsoft-quantum">
          <h2 id="item-1-title">Governor Moore announces Microsoft Quantum Research Center</h2>
        </a>
        <div class="maryland-listing-item__date">October 25, 2026</div>
        <div class="maryland-listing-item__description">
          <p>The University of Maryland Discovery District will host the new center, which is expected to bring 200 high-tech jobs over the next three years.</p>
        </div>
      </div>
    </article>
  </li>
  <!-- Additional <li class="maryland-listing-item"> entries -->
</ul>

<nav aria-label="Pagination for results" class="usa-pagination">
  <!-- See cdn/components/usa-pagination.md -->
</nav>
```

## Markup — location item (with `<address>`)

```html
<li class="maryland-listing-item">
  <article class="maryland-listing-item__container" id="loc-1" aria-labelledby="loc-1-title">
    <div class="maryland-listing-item__image maryland-listing-item__image--small">
      <figure>
        <img src="/img/state-house.jpg" alt="Maryland State House" />
      </figure>
    </div>
    <div class="maryland-listing-item__content">
      <a class="maryland-listing-item__title" href="/locations/state-house">
        <h2 id="loc-1-title">Maryland State House</h2>
      </a>
      <div class="maryland-listing-item__description">
        <address>
          100 State Circle<br>
          Annapolis, MD 21401
        </address>
      </div>
    </div>
  </article>
</li>
```

## Markup — document item (with download icon)

```html
<li class="maryland-listing-item">
  <article class="maryland-listing-item__container" id="doc-1" aria-labelledby="doc-1-title">
    <div class="maryland-listing-item__content">
      <div class="maryland-listing-item__eyebrow">Annual Report</div>
      <a class="maryland-listing-item__title" href="/documents/fy2026-report.pdf" download>
        <h2 id="doc-1-title">
          <span class="maryland-link__document-title">FY2026 Annual Report</span>
          <span class="maryland-link__document-divider"> - </span>
          <span class="maryland-link__document-format-size">PDF 64.56KB</span>
        </h2>
        <span aria-hidden="true">
          <!-- inline download SVG -->
        </span>
      </a>
      <div class="maryland-listing-item__description">
        <p>An annual summary of department activities, fiscal performance, and strategic priorities for FY2026.</p>
      </div>
    </div>
  </article>
</li>
```

## Markup — contact item (with `<dl>` of links)

```html
<li class="maryland-listing-item">
  <article class="maryland-listing-item__container" id="contact-1" aria-labelledby="contact-1-title">
    <div class="maryland-listing-item__image maryland-listing-item__image--small">
      <figure>
        <img src="/img/elizabeth.jpg" alt="Photo of Dr. Elizabeth Hughs" />
      </figure>
    </div>
    <div class="maryland-listing-item__content">
      <a class="maryland-listing-item__title" href="/staff/elizabeth-hughs">
        <h2 id="contact-1-title">Dr. Elizabeth Mary Hughs, PhD</h2>
      </a>
      <span class="maryland-listing-item__subtitle">Director, State Historic Preservation Officer</span>
      <div class="maryland-listing-item__description">
        <dl>
          <div class="inline"><dt>Email</dt> <dd><a href="mailto:elizabeth.hughs@maryland.gov">elizabeth.hughs@maryland.gov</a></dd></div>
          <div class="inline"><dt>Phone</dt> <dd><a href="tel:4106979556">410-697-9556</a></dd></div>
        </dl>
      </div>
    </div>
  </article>
</li>
```

## What each class does

| Class | Effect |
|---|---|
| `maryland-listing__body` | Intro paragraph wrapper. Uses `usa-prose` for typography. 48px bottom margin. |
| `maryland-listing__form` | Filter form `<form>`. Flex-wrap row with 24/16px row/column gap, end-aligned items. 56/64px bottom margin. |
| `maryland-listing__filter` | Each filter wrapper. Full-width on mobile, auto-width at tablet+. |
| `maryland-listing__filter--input` | Caps the input at 100% inline-size. |
| `maryland-listing__filter--select` | (No additional styling beyond the base filter wrapper.) |
| `maryland-listing__results` | (Defined in the CSS but not emitted in current MDWDS markup.) body-5 (16px) `base-dark`. |
| `maryland-listing__list-summary` | Result count line. body-4 italic. `role="status" aria-live="polite"`. |
| `maryland-listing__list` | The `<ul>` of items. List-style none, 32/16/32px vertical margins, 1px `base-light` bottom border. |
| `maryland-listing__list + .usa-pagination` | Selector: when pagination immediately follows the list, applies 32px top margin and allows the pagination list to wrap on narrow viewports. |
| `maryland-listing-item` | Each `<li>`. List-style none. 64px top margin between items (and 64px below the last item). |
| `maryland-listing-item__container` | Each `<article>`. 1px `base-light` top border. Flex-wrap row with 32/24px row/column gap. When a full-size image is present, the top border becomes transparent. |
| `maryland-listing-item__image` | Image wrapper. Default 591×333px (landscape). |
| `maryland-listing-item__image--small` | Smaller image variant (180×240px). |
| `maryland-listing-item__content` | Content column. 100% width with `flex: 0 1 100%`. When it's the first child (no image), gets 48/64px top padding. |
| `maryland-listing-item__eyebrow` | Uppercase eyebrow. body-4 (16px) semibold, `ls(2)` tracking, `base-dark` color. 24/32px bottom margin. |
| `maryland-listing-item__title` | Title wrapper `<a>`. `ink` color, no underline. CSS grid for title + icon. Hover underlines the title with a primary-color stroke (4% thickness). |
| `maryland-listing-item__subtitle` | Subtitle span. body-6 semibold. |
| `maryland-listing-item__date` | Date row. body-5 with regular spacing. |
| `maryland-listing-item__description` | Description block. Inherits from `usa-prose` rendering of HTML content. Supports `<p>`, `<ul>`, `<address>`, `<dl>`, etc. |
| `maryland-link__document-title` / `__document-divider` / `__document-format-size` | Document title typography pieces — same as `maryland-link.md`. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `custom` | bool | true | Use ad-hoc args (true) or per-`contentType` sample (false). |
| `contentType` | `location` \| `contact` \| `event` \| `news` \| `document` | `contact` | Selects content-type defaults. |
| `body` | string (HTML) | sample | Intro paragraph rendered above the filter form. |
| `title` | string | — | Item title. |
| `subtitle` | string | — | Item subtitle (contact). |
| `link` | string | — | Item title link URL. |
| `linkType` | `download` \| `external` | — | Adds the matching icon SVG next to the title. |
| `eyebrow` | string | — | Item eyebrow. |
| `date` | string | — | Item date row. |
| `description` | string (HTML) | — | Item description (allowed HTML). |
| `imageUrl` | string | — | Item image URL. |
| `imageSize` | `small` \| `default` | `small` | Image size. |
| `documentFormat` / `documentSize` | string | — | Document type + size for the document-title spans. |

## Heading level adjustment

Each item's title is `<h2>` because listing pages typically don't have an `<h1>`-titled hero (the page hero supplies the `<h1>`; item headings are page-level sections). If you wrap the listing inside a section that already uses `<h2>`, demote item titles to `<h3>`.

## Common mistakes

1. **Treating `maryland-listing-page` as a single component** — it isn't. Compose `maryland-listing__body`, `__form`, `__list`, and `maryland-listing-item` together. For the full page shell, follow `cdn/recipes/listing-page.md`.
2. **Skipping the `role="status" aria-live="polite"` on the summary** — the result count needs to be announced when filters change. Without these, screen-reader users won't hear the update.
3. **Item titles without the `<a>` wrapper** — the title is the click target. Wrap in `<a class="maryland-listing-item__title">`, then put the `<h2>` inside the link.
4. **Pagination outside the listing context** — the styling for `usa-pagination` next to the list relies on the adjacent sibling selector. Make sure pagination immediately follows `__list`.
5. **Forgetting `aria-labelledby` on each item's `<article>`** — items are landmarks; they need accessible names from their title.
6. **Image without alt text** — even decorative images in a listing need `alt=""` (preferred over omitting the attribute).
7. **Mixing content types in one list** — pick one (news OR events OR documents). Mixed types confuse the filter UI and the visual rhythm.
8. **Using `<h1>` inside an item** — item titles are `<h2>`. The page `<h1>` lives in the hero.
