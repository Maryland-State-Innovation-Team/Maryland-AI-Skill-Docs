# usa-table

USWDS data table — semantic `<table>` markup with multiple style variants, responsive stacking on mobile, optional sortable columns, sticky headers, and a scrollable wrapper for wide datasets.

> **Prefer `maryland-table` on Maryland.gov pages.** `maryland-table` provides the Maryland visual treatment (palette, typography, border styling). Use `usa-table` only inside internal tools, USWDS-style microsites, or when Maryland branding is deliberately set aside.

## What it looks like

A `usa-table` is a fully-styled HTML table. By default each row has a `1px solid` USWDS neutral horizontal divider, headers sit on a subtle gray fill (`bg-base-lightest`), and cell padding is generous (~12px vertical / ~16px horizontal) for readability.

The first column uses `<th scope="row">` for the row header — visually identical to `<td>` cells but semantically labeled for screen readers. Column headers use `<th scope="col">`.

Tables include a `<caption>` element at the top describing the table's purpose. By USWDS default the caption is visible and styled as semibold text above the table; in some contexts (like inside data visualizations) it may be wrapped in `usa-sr-only` to hide it visually while keeping it for screen readers.

Style variants:

| Variant | Visual |
|---|---|
| `default` | Horizontal row dividers, header row tinted gray, generous padding |
| `borderless` | Removes the horizontal row dividers. Lighter visual feel; useful when the table needs to sit inside prose without competing |
| `striped` | Alternating row backgrounds (~`bg-base-lightest` on even rows) for at-a-glance row tracking |
| `stacked` | At mobile widths (<880px), the table collapses to a single-column stack: each row becomes a labeled block. Column headers appear as inline labels in front of each cell value. |
| `stacked-header` | Like `stacked` but with stronger header treatment on mobile (column header shown as a small label above each value) |
| `compact` | Reduces cell padding (~6px / 8px) for dense data |

Additional modifiers:

- **`usa-table--sticky-header`** — Column headers stay pinned at the top of the table while users scroll the table vertically (e.g., inside a long page).
- **`usa-table-container--scrollable`** — Wraps a table in a horizontally scrollable `<div>` with `tabindex="0"` so keyboard users can scroll wide tables.

Sortable columns receive a `data-sortable` attribute on the `<th>` plus USWDS JavaScript handling. When sortable, headers gain a click affordance and ascending/descending sort arrows on the active column.

## Variants — when to use which

- **`default`** → Any standard data table.
- **`borderless`** → Inside a body-text article where heavy dividers would clutter the read.
- **`striped`** → Long tables (10+ rows) where users need to track across wide rows.
- **`stacked` / `stacked-header`** → Mobile-first tables where collapsing to single-column on narrow screens improves legibility.
- **`compact`** → Dashboard-style dense data, financial reports.
- **`sortable`** → Tables users will want to reorder (by amount, date, name).
- **`scrollable`** → Wide tables with 6+ columns that don't fit on tablet widths.
- **`sticky-header`** → Tall tables where users will scroll within the table.

## Default markup

```html
<table class="usa-table">
  <caption>Maryland agency contact information</caption>
  <thead>
    <tr>
      <th scope="col">Agency</th>
      <th scope="col">Contact</th>
      <th scope="col">Email</th>
      <th scope="col">Phone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Department of Information Technology</th>
      <td>John Smith</td>
      <td>john.smith@maryland.gov</td>
      <td>(410) 555-1234</td>
    </tr>
    <tr>
      <th scope="row">Department of Health</th>
      <td>Jane Doe</td>
      <td>jane.doe@maryland.gov</td>
      <td>(410) 555-5678</td>
    </tr>
    <tr>
      <th scope="row">Department of Transportation</th>
      <td>Bob Johnson</td>
      <td>bob.johnson@maryland.gov</td>
      <td>(410) 555-9012</td>
    </tr>
  </tbody>
</table>
```

## Markup — striped

```html
<table class="usa-table usa-table--striped">
  <caption>FY2026 budget allocations by department</caption>
  <thead>
    <tr>
      <th scope="col">Department</th>
      <th scope="col">Allocation</th>
      <th scope="col">% Change YoY</th>
    </tr>
  </thead>
  <tbody>
    <tr><th scope="row">Education</th><td>$8.4B</td><td>+3.2%</td></tr>
    <tr><th scope="row">Transportation</th><td>$4.2B</td><td>+1.8%</td></tr>
    <tr><th scope="row">Health</th><td>$3.5B</td><td>+5.1%</td></tr>
    <tr><th scope="row">Public Safety</th><td>$2.1B</td><td>+0.6%</td></tr>
  </tbody>
</table>
```

## Markup — borderless

```html
<table class="usa-table usa-table--borderless">
  <caption>Recreational fishing license fees, 2026</caption>
  <thead>
    <tr><th scope="col">License type</th><th scope="col">Resident</th><th scope="col">Non-resident</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">Annual freshwater</th><td>$20.50</td><td>$30.00</td></tr>
    <tr><th scope="row">7-day freshwater</th><td>$7.00</td><td>$12.00</td></tr>
    <tr><th scope="row">Trout stamp</th><td>$5.00</td><td>$5.00</td></tr>
  </tbody>
</table>
```

## Markup — stacked (mobile collapse with headers per cell)

```html
<table class="usa-table usa-table--stacked">
  <caption>Office locations</caption>
  <thead>
    <tr>
      <th scope="col">Agency</th>
      <th scope="col">Address</th>
      <th scope="col">Phone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row" data-label="Agency">Comptroller of Maryland</th>
      <td data-label="Address">80 Calvert Street, Annapolis, MD 21401</td>
      <td data-label="Phone">(410) 260-7980</td>
    </tr>
    <tr>
      <th scope="row" data-label="Agency">Department of Assessments and Taxation</th>
      <td data-label="Address">301 W Preston Street, Baltimore, MD 21201</td>
      <td data-label="Phone">(410) 767-1184</td>
    </tr>
  </tbody>
</table>
```

The `data-label` on each `<th>`/`<td>` provides the column header text shown alongside each cell when the table collapses on mobile. Use `usa-table--stacked-header` for an emphasized label treatment.

## Markup — sortable

```html
<table class="usa-table">
  <caption>Maryland counties by population (2025)</caption>
  <thead>
    <tr>
      <th scope="col" data-sortable>County</th>
      <th scope="col" data-sortable>Population</th>
      <th scope="col" data-sortable>Median household income</th>
    </tr>
  </thead>
  <tbody>
    <tr><th scope="row">Montgomery</th><td>1,073,000</td><td>$117,800</td></tr>
    <tr><th scope="row">Prince George's</th><td>956,000</td><td>$95,500</td></tr>
    <tr><th scope="row">Baltimore County</th><td>854,000</td><td>$88,200</td></tr>
    <tr><th scope="row">Anne Arundel</th><td>591,000</td><td>$108,400</td></tr>
  </tbody>
</table>
```

Sortable tables require USWDS JavaScript. The `data-sortable` attribute on a `<th>` enables sort UI for that column. The MDWDS CDN bundle includes USWDS JS, so sortable works out of the box.

## Markup — scrollable wrapper (wide tables)

```html
<div class="usa-table-container--scrollable" tabindex="0">
  <table class="usa-table">
    <caption>Statewide procurement summary, FY 2026</caption>
    <thead>
      <tr>
        <th scope="col">Agency</th>
        <th scope="col">Contract ID</th>
        <th scope="col">Vendor</th>
        <th scope="col">Award date</th>
        <th scope="col">Award amount</th>
        <th scope="col">Term</th>
        <th scope="col">Status</th>
      </tr>
    </thead>
    <tbody>
      <!-- many wide rows -->
    </tbody>
  </table>
</div>
```

`tabindex="0"` on the wrapper is required so keyboard users can scroll the table horizontally with arrow keys.

## Markup — sticky header

```html
<table class="usa-table usa-table--sticky-header">
  <caption>Maryland licensed daycare providers</caption>
  <thead>
    <tr>
      <th scope="col">Provider</th>
      <th scope="col">County</th>
      <th scope="col">License #</th>
      <th scope="col">Expires</th>
    </tr>
  </thead>
  <tbody>
    <!-- many rows; headers stay pinned while scrolling -->
  </tbody>
</table>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-table` | Base table. Sets ~12/16px cell padding, horizontal row dividers (1px solid USWDS neutral), header row with subtle gray fill (`bg-base-lightest`), Source Sans Pro Web body type. |
| `usa-table--borderless` | Removes horizontal row dividers. Lighter visual feel. |
| `usa-table--striped` | Alternating row backgrounds (~`bg-base-lightest` on even rows). |
| `usa-table--stacked` | At mobile widths (<880px), each row becomes a vertically stacked block. Cells use their `data-label` attribute to show the column header inline. |
| `usa-table--stacked-header` | Variant of `--stacked` where the column header appears as a small label above each cell value on mobile. |
| `usa-table--compact` | Reduces cell padding (~6/8px) for dense tables. |
| `usa-table--sticky-header` | Column headers stick to the top of the table's container while scrolling. |
| `usa-table-container--scrollable` | Wrapper `<div>` for wide tables. Adds horizontal scroll, requires `tabindex="0"` for keyboard access. |
| `<caption>` | Title above the table. Default styled as semibold text. Use `class="usa-sr-only"` to hide it visually while keeping it for screen readers. |
| `<th scope="col">` | Column header. Bold, slightly larger than body text. |
| `<th scope="row">` | Row header (first column). Bold text, marked as a row label for screen readers. |
| `data-sortable` (on `<th>`) | Enables sort controls on that column. Requires USWDS JS. |
| `data-label` (on `<th>`/`<td>`) | Used by stacked variants to display the column header inline next to each cell on mobile. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `default` \| `borderless` \| `striped` \| `stacked` \| `stacked-header` \| `compact` | `default` | Adds `usa-table--{variant}` |
| `caption` | string | sample | Becomes `<caption>` content |
| `columns` | `[{ header, accessor, sortable }]` | sample | Column definitions; `accessor` maps to keys in `rows`; `sortable: true` enables `data-sortable` per column |
| `rows` | array of objects | sample | Each row object's keys must match column `accessor` values |
| `scrollable` | bool | `false` | Wraps the table in `usa-table-container--scrollable` |
| `sortable` | bool | `false` | Enables sortable behavior. Loads USWDS JS. Only columns with `sortable: true` are interactive. |
| `stickyHeader` | bool | `false` | Adds `usa-table--sticky-header` |
| `enableAnalytics` | bool | `false` | Adds `data-ga-*` attributes |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Heading level adjustment

Tables don't have a heading slot — the `<caption>` is the table's title. If you need a heading **above** the table, use a regular `<h2>`/`<h3>` per the surrounding page outline. The caption itself is a separate semantic element; do not nest a heading inside it.

## Common mistakes

1. **Using `usa-table` on a Maryland-branded page** — switch to `maryland-table` for the Maryland palette.
2. **First column as `<td>` instead of `<th scope="row">`** — row headers are accessibility-critical. Always make the row-identifying cell a `<th scope="row">`.
3. **Omitting `<caption>`** — every data table needs a caption (use `usa-sr-only` to visually hide it if you don't want it shown).
4. **Forgetting `data-label` on stacked variants** — without it, mobile collapse hides which value belongs to which column.
5. **Forgetting `tabindex="0"` on the scrollable wrapper** — keyboard users can't scroll the table horizontally.
6. **Combining `--stacked` with a horizontally-scrollable wrapper** — they're opposite strategies. Pick one for wide tables: stack on mobile, or scroll on mobile.
7. **Hard-coding `style="border: 1px solid #000"` to add borders** — the variant modifiers control this. Default has the borders you need.
