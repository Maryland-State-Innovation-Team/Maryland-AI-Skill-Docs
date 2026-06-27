# usa-grid

The USWDS 12-column layout grid. Three core utilities — `grid-container`, `grid-row`, `grid-col-*` — handle nearly every page layout on a Maryland.gov page. This file is a quick reference; **`cdn/composition.md` is the canonical guide** for grid usage in context (sidebar layouts, card rows, prose constraints, responsive behavior). Cross-reference that file when laying out a page.

## What it looks like

The grid is Flexbox-based. A `grid-container` is a centered max-width wrapper (default `desktop-lg` = ~1400px) with horizontal page padding. Inside it, `grid-row` creates a row of columns. Each `grid-col-N` child spans `N` of 12 columns (`grid-col-12` = full width, `grid-col-6` = half, `grid-col-4` = a third).

Each `grid-col-*` cell is a flex item — by default it has no internal padding. Add `grid-gap` (16px gutters) or `grid-gap-lg` (32px gutters) to the row when you want spacing between columns.

Responsive variants use breakpoint prefixes — `tablet:grid-col-6`, `desktop:grid-col-8` — to change the span at a breakpoint. Below the prefix's min-width, the cell falls back to its bare-class behavior (or to `grid-col-12` if no bare class is set). This is the foundation of MDWDS's mobile-first responsive layouts.

In MDWDS, `grid-row` and any element with a `grid-col` class also become CSS **container queries** via `container-name: row` / `container-name: column` — this means components inside a grid cell can adjust their typography or layout based on the cell's width (not the viewport's). For example, headings inside a narrow sidebar column automatically scale down even at desktop widths.

## Breakpoint scale (from `cdn/composition.md`)

| Name | Min width | Use as prefix |
|---|---|---|
| (none) | 0 | bare class (`grid-col-12`) |
| `mobile-lg` | 480px | `mobile-lg:grid-col-6` |
| `tablet` | 640px | `tablet:grid-col-6` |
| `tablet-lg` | 880px | `tablet-lg:grid-col-6` |
| `desktop` | 1024px | `desktop:grid-col-8` |
| `desktop-lg` | 1200px | `desktop-lg:grid-col-8` |
| `widescreen` | 1400px | `widescreen:grid-col-8` |

## The three core utilities

### `grid-container`

Centered max-width wrapper with horizontal page padding. Required around any grid layout.

```html
<div class="grid-container">
  <!-- grid rows go here -->
</div>
```

Default max-width is `desktop-lg` (~1400px). For a wider page, use `grid-container-widescreen`:

```html
<div class="grid-container-widescreen">
  <!-- wider content -->
</div>
```

### `grid-row`

A direct flex/grid row. Use `grid-gap` or `grid-gap-lg` for gutters between columns.

```html
<div class="grid-row grid-gap">
  <!-- columns -->
</div>
```

Gutter sizes:
- `grid-gap-sm` — small gutters
- `grid-gap` — default (~16px horizontal gutters)
- `grid-gap-lg` — large (~32px horizontal gutters)

### `grid-col-N`

Span `N` of 12 columns. Numbers 1 through 12. Use responsive prefixes to change span at a breakpoint.

```html
<div class="grid-col-12 desktop:grid-col-8">
  <!-- full-width on mobile, 8/12 at desktop+ -->
</div>
```

Auto / fill variants:
- `grid-col` — flex-fills available space
- `grid-col-auto` — sizes to content
- `grid-col-fill` — fills remaining space after `auto` siblings

Offset:
- `grid-offset-N` — left offset of N columns (shifts the column right)

## Default markup — three equal columns

```html
<div class="grid-container">
  <div class="grid-row grid-gap">
    <div class="grid-col-12 tablet:grid-col-4">
      <h3>Apply for benefits</h3>
      <p>Maryland Medical Assistance, SNAP, and TCA.</p>
    </div>
    <div class="grid-col-12 tablet:grid-col-4">
      <h3>Manage your case</h3>
      <p>Update income, household, and contact information.</p>
    </div>
    <div class="grid-col-12 tablet:grid-col-4">
      <h3>Find a local office</h3>
      <p>Department of Human Services field offices in every county.</p>
    </div>
  </div>
</div>
```

On mobile (<640px), columns stack full-width. At `tablet` (640px+) and above, they sit side-by-side at one-third width each.

## Sidebar + content layout

```html
<div class="grid-container">
  <div class="grid-row grid-gap">
    <aside class="grid-col-12 desktop:grid-col-3">
      <!-- maryland-sidenav -->
    </aside>
    <div class="grid-col-12 desktop:grid-col-8">
      <!-- main article content -->
    </div>
  </div>
</div>
```

On mobile and tablet, sidebar and content stack. At `desktop` (1024px+), sidebar takes 3/12 and content takes 8/12, leaving 1/12 of breathing space.

## Auto-sizing columns

```html
<div class="grid-row">
  <div class="grid-col-auto">Sized to content</div>
  <div class="grid-col-fill">Fills remaining space</div>
  <div class="grid-col-auto">Sized to content</div>
</div>
```

## Offset

```html
<div class="grid-row">
  <div class="grid-col-8 grid-offset-2">
    Centered 8/12 column with 2-column left offset (and 2-column gap on the right)
  </div>
</div>
```

## Gutter variants

```html
<div class="grid-row grid-gap">
  <div class="grid-col-4">Default 16px gutters</div>
  <div class="grid-col-4">Default 16px gutters</div>
  <div class="grid-col-4">Default 16px gutters</div>
</div>

<div class="grid-row grid-gap-lg">
  <div class="grid-col-4">Large 32px gutters</div>
  <div class="grid-col-4">Large 32px gutters</div>
  <div class="grid-col-4">Large 32px gutters</div>
</div>
```

## What each class does

| Class | Effect |
|---|---|
| `grid-container` | Centered max-width wrapper with page horizontal padding. Default max-width = `desktop-lg` (~1400px). |
| `grid-container-widescreen` | Wider wrapper with `widescreen` (~1600px) max-width. |
| `grid-row` | Direct flex/grid row. Holds columns. In MDWDS, also a CSS container query context (`container-name: row`). |
| `grid-gap-sm` | Small gutters between columns (~8px). |
| `grid-gap` | Default gutters (~16px horizontal). |
| `grid-gap-lg` | Large gutters (~32px horizontal). |
| `grid-col-1` to `grid-col-12` | Span N of 12 columns at the bare (no-prefix) breakpoint. |
| `grid-col` | Flex-grow column — shares remaining space equally with siblings. |
| `grid-col-auto` | Sizes to content width. |
| `grid-col-fill` | Fills remaining space after `auto` siblings. |
| `grid-offset-1` to `grid-offset-11` | Left offset of N columns. |
| `mobile-lg:`, `tablet:`, `tablet-lg:`, `desktop:`, `desktop-lg:`, `widescreen:` prefixes | Apply the suffixed class at the named breakpoint and above. |

In MDWDS, every `grid-row` and `[class*="grid-col"]` element is also a **CSS container** for container-query-based responsive typography inside components (e.g., heading sizes shrink inside narrow sidebar columns).

## Common patterns

### Three-up cards

```html
<div class="grid-container">
  <div class="grid-row grid-gap">
    <div class="grid-col-12 tablet:grid-col-4">card 1</div>
    <div class="grid-col-12 tablet:grid-col-4">card 2</div>
    <div class="grid-col-12 tablet:grid-col-4">card 3</div>
  </div>
</div>
```

**But for `maryland-card`, use `<ul class="maryland-card-group">` instead** — it handles its own column math. Don't wrap individual `maryland-card` items in `grid-col-*`.

### Centered narrow content (for a form or article)

```html
<div class="grid-container">
  <div class="grid-row">
    <div class="grid-col-12 tablet:grid-col-10 tablet:grid-offset-1 desktop:grid-col-8 desktop:grid-offset-2">
      <!-- centered content -->
    </div>
  </div>
</div>
```

### Two-column with main + sidebar (reversed on mobile)

```html
<div class="grid-container">
  <div class="grid-row grid-gap">
    <div class="grid-col-12 desktop:grid-col-8">
      <!-- main content -->
    </div>
    <aside class="grid-col-12 desktop:grid-col-4">
      <!-- sidebar -->
    </aside>
  </div>
</div>
```

## Heading level adjustment

Not applicable — `usa-grid` is layout, not content. Headings inside cells follow the page outline as documented in `cdn/composition.md`.

## Common mistakes

1. **Forgetting `grid-container`** — content runs edge-to-edge. Always wrap rows in a container.
2. **Wrapping `maryland-card` in `grid-col-*`** — `maryland-card-group` handles columns. See `cdn/components/maryland-card.md`.
3. **Skipping the base `grid-col-12`** — without it, the column doesn't take full width on mobile and the layout breaks at narrow widths.
4. **Mismatched columns adding up to >12** — they wrap onto a new row. Math the totals; for true 4+4+4 use only three `grid-col-4`s.
5. **Inline `style="display: grid; grid-template-columns: ..."`** — use the built-in utilities. Custom CSS grid breaks responsive prefixes.
6. **Using `tablet:grid-col-6` without a base class** — at mobile widths the cell has no width rule. Always pair: `grid-col-12 tablet:grid-col-6`.
7. **Nesting `grid-row` directly inside `grid-row`** — nest a `grid-col-*` between them. Rows live inside columns, not directly inside other rows.

## Full guide

For the canonical grid + composition guidance — sidebar patterns, prose wrappers, vertical rhythm with `block-spacing` and `margin-y-*` — see **`cdn/composition.md`**. This file is just the utility-class reference; composition.md tells you how to use the grid effectively in real page layouts.
