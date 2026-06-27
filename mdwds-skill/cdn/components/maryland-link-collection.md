# maryland-link-collection

Maryland Design System link collection presents a curated list of related links in a 2-column (at tablet+) layout, with an optional header (title + description + "more" link) above. Each link row has hover-state arrow animation and supports plain links, external links, and document downloads.

> **Use `maryland-link-collection` for a flat list of related links — typically 6–12 — that don't need separate column sub-headings.** For a 1–3 column grouped layout with column titles, use `maryland-highlight`. For an icon-prefixed feature grid with descriptions, use `maryland-icon-list`. For card-style featured items, use `maryland-card-group`.

## What it looks like

A link collection is a `<section>` with:

- An optional header. At mobile, title → description → "more" link stack vertically. At tablet-lg+, the description fills the row's left side and the "more" link is right-aligned at the bottom of the row. The title is Merriweather light, 32 → 40 → 48px responsive, `ls(1)` letter-spacing.
- A `<ul>` of link rows. CSS `column-count: 2` at tablet+ creates two text-flow columns with 64px gap. On mobile, items stack in a single column.

Each link row:

- Display flex column, 20/16/24px padding (mobile/tablet horizontal).
- Title text on the left, arrow icon on the right (top row); optional description below.
- 2px `gray-40` underline (`::after` scaled to 0.5 — so 1px visual) that thickens to full + Maryland blue on hover, and the arrow translates 12px right + recolors.
- External links get `target="_blank"`, `rel="noopener noreferrer"`, and the icon changes to `open_in_new`.
- Download links get the `download` attribute and a `download` icon; the link title can include a "PDF — 2MB" suffix.

Link size: body-7 (20px) on mobile, body-9 (22px) at mobile-lg+. Descriptions: body-4 / body-6 (16/20px).

## When to use

- 6–12 related resource links on a topic landing page.
- Service-directory subsections ("All licensing forms", "All applications").
- Document collections (with download icons and file format/size metadata).
- "More resources" rounders below another component.

## Default markup

```html
<section class="maryland-link-collection" aria-labelledby="lc-1">
  <div class="maryland-link-collection__container">
    <div class="maryland-link-collection__header">
      <h2 id="lc-1" class="maryland-link-collection__title">Grow your career in Maryland</h2>
      <div class="maryland-link-collection__header-bottom">
        <div class="maryland-link-collection__description">
          Discover how Maryland works for you — find a job, volunteer, or start your own business.
        </div>
        <div class="maryland-link-collection__more-link">
          <a class="maryland-link" href="/business">More in business and work</a>
        </div>
      </div>
    </div>
    <ul class="maryland-link-collection__list">
      <li class="maryland-link-collection__item">
        <a href="/jobs" class="maryland-link-collection__link">
          <div class="maryland-link-collection__link-top">
            <span class="maryland-link-collection__link-text">Jobs and career support</span>
            <span class="maryland-link-collection__icon" aria-hidden="true"></span>
          </div>
        </a>
      </li>
      <li class="maryland-link-collection__item">
        <a href="/licensing" class="maryland-link-collection__link">
          <div class="maryland-link-collection__link-top">
            <span class="maryland-link-collection__link-text">Professional licenses and permits</span>
            <span class="maryland-link-collection__icon" aria-hidden="true"></span>
          </div>
        </a>
      </li>
      <li class="maryland-link-collection__item">
        <a href="https://example.com" target="_blank" rel="noopener noreferrer" class="maryland-link-collection__link" aria-label="State of Maryland job openings (opens in new window)">
          <div class="maryland-link-collection__link-top">
            <span class="maryland-link-collection__link-text">State of Maryland job openings</span>
            <span class="maryland-link-collection__icon maryland-link-collection__icon--external" aria-hidden="true"></span>
          </div>
        </a>
      </li>
      <li class="maryland-link-collection__item">
        <a href="/apprenticeships" class="maryland-link-collection__link">
          <div class="maryland-link-collection__link-top">
            <span class="maryland-link-collection__link-text">Apprenticeships and training</span>
            <span class="maryland-link-collection__icon" aria-hidden="true"></span>
          </div>
        </a>
      </li>
    </ul>
  </div>
</section>
```

## Markup — with per-item descriptions

```html
<li class="maryland-link-collection__item">
  <a href="/business/start" class="maryland-link-collection__link">
    <div class="maryland-link-collection__link-top">
      <span class="maryland-link-collection__link-text">Start a business</span>
      <span class="maryland-link-collection__icon" aria-hidden="true"></span>
    </div>
    <div class="maryland-link-collection__item-description">
      Form an LLC, register a tax ID, and pick a business structure in one online application.
    </div>
  </a>
</li>
```

Per-item descriptions can be mixed with description-less items in the same list.

## Markup — document download item

```html
<li class="maryland-link-collection__item">
  <a href="/dnr/guide.pdf" download class="maryland-link-collection__link" aria-label="Download business formation guide (download)">
    <div class="maryland-link-collection__link-top">
      <span class="maryland-link-collection__link-text">
        <span class="maryland-link__document-title">Business formation guide</span>
        <span class="maryland-link__document-divider"> - </span>
        <span class="maryland-link__document-format-size">PDF 2.1MB</span>
      </span>
      <span class="maryland-link-collection__icon maryland-link-collection__icon--download" aria-hidden="true"></span>
    </div>
  </a>
</li>
```

The nested `maryland-link__document-*` spans give the document title typography (body font, semibold) and a smaller "PDF 2.1MB" suffix.

## What each class does

| Class | Effect |
|---|---|
| `maryland-link-collection` | Base `<section>`. Applies `block-spacing` and `grid-container`. |
| `maryland-link-collection__container` | Inner wrapper. No styling on its own. |
| `maryland-link-collection__header` | Optional header block. 24/32/48px bottom margin (responsive). Margin collapses when no description is present. |
| `maryland-link-collection__header-bottom` | Wraps description + more-link. At tablet-lg+, becomes a 12-col grid row with the description filling and the more-link right-aligned at the bottom. |
| `maryland-link-collection__title` | The `<h2>`. Uses the `h2` mixin (Merriweather light, 32 → 48px). `ls(1)` letter-spacing. Bottom margin scales 24 → 32 → 48px. |
| `maryland-link-collection__description` | Description block. body-4 → body-7 → body-9 (16 → 20 → 22px). `base-darkest` color. Removes nested first/last `<p>` margins. |
| `maryland-link-collection__more-link` | "More" link wrapper. body-4 (mobile) / body-6 (mobile-lg+). At tablet-lg+, becomes `grid-col("auto")` and aligns to the right. Inner `<a>` capped at 210px width. |
| `maryland-link-collection__list` | The `<ul>`. List-style none. body-7 (20px) / body-9 (22px) text. At tablet+: `column-count: 2`, `column-gap: 64px`. |
| `maryland-link-collection__item` | Each `<li>`. Position relative. `break-inside: avoid` so items don't split across the CSS column boundary. |
| `maryland-link-collection__link` | The `<a>`. Display flex column, `base-darkest` color, no text-decoration. 20/16/24px padding. Has a 2px `gray-40` `::after` underline that thickens to full + Maryland blue on hover/focus. Focus ring 2px primary 2px offset. |
| `maryland-link-collection__link-top` | Flex row holding title + icon, space-between. |
| `maryland-link-collection__link-text` | Title text span. Applies `text-trim` and `flex: 1`. |
| `maryland-link-collection__icon` | Arrow icon (16/20/24px responsive). `base-darkest` color via `arrow_forward` rounded mask. Translates 12px right on hover, recolors to primary. |
| `maryland-link-collection__icon--external` | Swap to `open_in_new` mask. |
| `maryland-link-collection__icon--download` | Swap to `download` mask. |
| `maryland-link-collection__item-description` | Optional description below the link top row. body-4/body-6 (16/20px). 12px top padding. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `title` | string | — | Section heading. Optional. |
| `description` | string | — | Section description. Optional. |
| `moreLinkText` | string | `"Learn more"` | More-link label. |
| `moreLinkUrl` | string | — | More-link URL. Required for the link to render. |
| `items` | `Array<{title, url, description?, iconType?: "external" \| "download", documentFormat?, documentSize?}>` | — | Link items. `iconType` adds the matching attributes. `documentFormat`/`documentSize` enable the document-title typography. |

## Heading level adjustment

The title defaults to `<h2>`. When nested inside an already-`<h2>`-headed section, demote to `<h3>` (keep the class). The class supplies typography; the element supplies outline.

## Common mistakes

1. **Forgetting `aria-label` on external/download links** — In hand-written markup, set `aria-label="{title} (opens in new window)"` for external and `(download)` for downloads.
2. **Using inline-block link text** — the design assumes the title is a block-level span. The flex `__link-top` handles alignment.
3. **More than ~12 links** — the column-flow gets unwieldy. Split into themed groups or paginate.
4. **Mixing items with and without `aria-label`** — be consistent. External and download icons need accessible-text equivalents.
5. **Wrapping the list in a `grid-col-*`** — the `grid-container` is already applied. Adding columns introduces double-padding.
6. **Using `<p>` inside the link text** — keep titles as inline content. For multi-line descriptions, use `__item-description` below the top row.
