# maryland-table

Maryland Design System table renders tabular data with Maryland-themed colors and typography. Internally it composes the USWDS table mixins (`usa-table`, `usa-table--borderless`, `usa-table--striped`) under Maryland-namespaced class names, then layers Tabled.js on top for responsive horizontal-scroll navigation on narrow screens.

> **Use `maryland-table` for tabular data on Maryland-branded pages.** For internal tools where USWDS branding is fine, use `usa-table`. Captions are limited to 200 characters per design guideline; if you need a richer table description, use a heading + paragraph above the table.

## What it looks like

A `.maryland-table` wrapper container holds a `<table>` element styled by `maryland-table__*` classes. The container is centered on the page with a max-width of 846px (`spacing-multiple(105.75)`).

Header cells:

- 16px (mobile) / 20px (mobile-lg+) Source Sans semibold. Line-height 23px / 28px.
- `base-lightest` (cream) background, `ink` text.
- 1px `base` (medium gray) bottom border.
- Vertical-aligned bottom.
- 32px top padding (mobile) / 48px (mobile-lg+), 16px / 24px bottom padding.
- Horizontal padding: 24px first/last cells (mobile), 36px first/last + 24px middle (mobile-lg+).

Body cells:

- body-sm (mobile) / body-7 (20px at mobile-lg+). 19px / 32px line-height.
- No borders by default (borderless variant).
- 24px vertical padding.

Whole table has a 2px `base-lightest` outer border.

Tabled.js (when active) clones the `<caption>` into a `.tabled__caption` and adds prev/next navigation arrows for horizontal column scrolling. The caption is rendered above the table in italic body-xs (~13px) `base-darkest`. The header wrapper combines caption (75% width) + navigation (25%) at mobile-lg+.

The container is `block-spacing`-managed for vertical rhythm with the rest of the page.

## Variants

Set via boolean modifiers on the `<table>` element:

| Modifier | Effect |
|---|---|
| `maryland-table__table--borderless` | Removes vertical and horizontal cell borders (default on per the design). |
| `maryland-table__table--striped` | Alternating row backgrounds (default on per the design). |

Combine both for the standard MDWDS look.

## When to use

- Comparison tables (e.g., fee schedules, license types).
- Numeric data tables (e.g., dashboard exports).
- Reference lists where row/column structure communicates the relationship.

Avoid tables for non-tabular content (use definition lists, summary boxes, or accordions instead).

## Default markup

```html
<div class="maryland-table" id="fees-table">
  <table class="maryland-table__table maryland-table__table--borderless maryland-table__table--striped">
    <caption class="maryland-table__caption">
      Maryland recreational fishing license fees for residents and non-residents, effective FY2026.
    </caption>
    <thead class="maryland-table__head">
      <tr class="maryland-table__row">
        <th class="maryland-table__header-cell" scope="col">License type</th>
        <th class="maryland-table__header-cell" scope="col">Resident fee</th>
        <th class="maryland-table__header-cell" scope="col">Non-resident fee</th>
        <th class="maryland-table__header-cell" scope="col">Valid for</th>
      </tr>
    </thead>
    <tbody class="maryland-table__body">
      <tr class="maryland-table__row">
        <td class="maryland-table__cell">Freshwater annual</td>
        <td class="maryland-table__cell">$20.50</td>
        <td class="maryland-table__cell">$30.50</td>
        <td class="maryland-table__cell">365 days</td>
      </tr>
      <tr class="maryland-table__row">
        <td class="maryland-table__cell">Tidal annual</td>
        <td class="maryland-table__cell">$15.00</td>
        <td class="maryland-table__cell">$22.50</td>
        <td class="maryland-table__cell">365 days</td>
      </tr>
      <tr class="maryland-table__row">
        <td class="maryland-table__cell">7-day short-term</td>
        <td class="maryland-table__cell">$10.50</td>
        <td class="maryland-table__cell">$15.00</td>
        <td class="maryland-table__cell">7 days</td>
      </tr>
      <tr class="maryland-table__row">
        <td class="maryland-table__cell">Chesapeake Bay sport</td>
        <td class="maryland-table__cell">$15.00</td>
        <td class="maryland-table__cell">$22.50</td>
        <td class="maryland-table__cell">365 days</td>
      </tr>
    </tbody>
  </table>
</div>
```

`id` is required when Tabled.js is in use (it looks up the container by id to install nav controls).

> **CDN limitation:** Tabled.js (the responsive horizontal-scroll navigation) is **not bundled in `mdwds-core.js`** on the CDN. The Storybook build wires Tabled.js into each table, but adopter pages get the **base table only** — no responsive nav arrows, no `.tabled__header`. The visual styling (Maryland colors, striped rows, borderless variant) all works fine, but on narrow screens a wide table will simply overflow its container. If you need the responsive scroll feature on production sites, wrap the table in your own overflow scroller: `<div style="overflow-x:auto">` around the `<table>`, or design tables to fit `desktop-lg` (≤1200px content width) without horizontal overflow.

## Markup — without caption

Omit the `<caption>` element. The table sits without an introductory line; rely on the surrounding section heading.

## Markup — without striping or with cell borders

Drop `maryland-table__table--striped` or `--borderless` (or both) from the `<table>` element:

```html
<table class="maryland-table__table">
  <!-- All borders + no stripes -->
</table>
```

## What each class does

| Class | Effect |
|---|---|
| `maryland-table` | Outer container `<div>`. Applies `block-spacing`, `grid-container`, and max-width 846px centered. Holds the `<table>` and the Tabled.js-generated `.tabled__header` if present. |
| `maryland-table__table` | The `<table>`. 2px `base-lightest` outer border. Inherits USWDS `usa-table` typography. |
| `maryland-table__table--borderless` | Removes inner row/column borders. |
| `maryland-table__table--striped` | Alternating row backgrounds (per USWDS). |
| `maryland-table__caption` | The `<caption>`. Italic body-xs (~13px) `base-darkest`. Tabled.js may clone this into a `.tabled__caption` rendered above the navigation. |
| `maryland-table__head` | The `<thead>`. No visual override; cells handle styling. |
| `maryland-table__body` | The `<tbody>`. No visual override. |
| `maryland-table__row` | A `<tr>`. No visual override; striping is applied via `usa-table--striped`. |
| `maryland-table__header-cell` | `<th scope="col">`. 16/20px Source Sans semibold, `ink` color, `base-lightest` background, 1px `base` bottom border. `text-transform: none` (overrides USWDS's uppercase). Vertical-align bottom. |
| `maryland-table__cell` | `<td>`. body-sm / body-7 (16/20px). 19/32px line-height. No borders by default. 24px vertical padding. Horizontal padding scales with breakpoint. |
| `.tabled__header` (Tabled.js) | Flex row at mobile-lg+ holding the caption (75%) and the navigation arrows (25%). 4–8px bottom margin. |
| `.tabled__caption` (Tabled.js) | The cloned caption used in the responsive layout. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `firstHeader` | string | sample | Text for the first column header. |
| `firstCell` | string | sample | Text for the first column cells (row number appended). |
| `caption` | string | sample | `<caption>` text. Max 200 chars per design guideline. |
| `striped` | bool | true | Enable striping. |
| `borderless` | bool | true | Remove cell borders. |
| `rows` | number (1–20) | 5 | Number of body rows rendered by Storybook. |
| `columns` | number (2–8) | 7 | Number of columns. |

## Heading level adjustment

Tables don't have an internal heading. The `<caption>` is the table's accessible label; for additional context, place a heading and intro paragraph above the table.

## Common mistakes

1. **Missing `scope="col"` on `<th>`** — without it, screen-reader users lose the column-header association. Always set `scope="col"` (or `scope="row"` for row headers).
2. **Forgetting the `<div class="maryland-table">` wrapper** — the styling, max-width, and Tabled.js integration all rely on the wrapper.
3. **Skipping the `id` on the wrapper** — Tabled.js looks for the wrapper by id to install the responsive navigation. Without it, the scroll arrows won't appear.
4. **Captions longer than 200 characters** — design constraint. Use a heading + paragraph above the table for long descriptions.
5. **Using `<th>` for both row and column headers without `scope`** — every `<th>` should have either `scope="col"` (in `<thead>`) or `scope="row"` (in `<tbody>`).
6. **Inline-styling cell widths** — let the design system handle column sizing. If a column needs a fixed width, set `<colgroup><col style="width: 20%"></colgroup>` instead of styling each `<th>` separately.
7. **Skipping `maryland-table__table--borderless --striped`** — by design, MDWDS tables are striped + borderless. Reverting to bordered tables looks out of place.
