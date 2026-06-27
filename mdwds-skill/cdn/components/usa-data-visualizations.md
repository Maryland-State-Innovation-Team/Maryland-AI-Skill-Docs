# usa-data-visualizations

USWDS Data Visualizations is **primarily a guidance pattern**, not a packaged widget. It defines the accessible container, ARIA roles, color palette, and supporting markup that every chart on a Maryland.gov page should follow — regardless of the charting library you use (D3, Chart.js, Highcharts, plain SVG).

> **Important:** there is no `usa-chart` element. You bring your own rendering library; USWDS gives you the accessible wrapper structure around it. The MDWDS Storybook example renders an HTML bar-chart for illustration only; production charts will typically be SVG/Canvas inside the same container pattern.

## What it looks like

A data visualization following this pattern is a `<div class="usa-data-visualization">` containing, in order:

1. **Chart title** — `<h3 class="chart-title">` — semibold, ~24px, the headline of the visualization. Associated via `aria-labelledby`.
2. **Narrative summary** — `<p class="chart-description">` — ~16px paragraph that conveys the same information as the chart in plain text. Critical for screen reader users and a contextual lead-in for everyone. Associated via `aria-describedby`.
3. **Visualization container** — `<div class="visualization-container" role="img" aria-hidden="true">` (or with appropriate ARIA depending on whether the chart is interactive). For decorative renderings, `aria-hidden="true"` hides them from assistive tech because the table + description carry the data.
4. **Data source** — `<p class="chart-source">` with a link to the original data, ~14px gray text below the chart.
5. **Accessible data table** — `<table class="usa-table usa-table--borderless">` exposing the exact data values for assistive technology. Often paired with `<caption class="usa-sr-only">` to hide the caption visually while keeping it for screen readers.

The chart bars in the example use Maryland-palette blues (`#005ea2`, `#00687d`, `#0076d6`, `#2378c3`) with white bar labels and ~40px bar height. The container has a pale neutral background (`#f0f0f0`) with a thin neutral border and slight rounding.

This is fundamentally an **accessibility pattern** — the visual chart is secondary to the table + description that everyone (sighted or not) can access. The MDWDS guidance is unambiguous: never embed information in images alone; always provide a textual and tabular path.

## Core principles

**Simplicity**
- Prefer common chart types (line, bar) for general audiences.
- Limit each chart to 1–2 central themes.
- Use high-contrast colors with pattern fills as alternatives.

**Lossless representation**
- Never put information only in the image.
- Provide textual axis labels and a data table.
- Minimize required interactions (hover, click) — the static image should convey the message.

**Clarity of intent**
- State the intended takeaway explicitly in the narrative summary.
- Include statistical trends in plain text ("Health spending increased 15% year-over-year").

## Accessible color palette

The `AccessibleColorPalette` story documents the colors that meet WCAG 2.1 AA contrast on white backgrounds. Use these for chart data series:

| Token | Hex | Usage |
|---|---|---|
| Primary Blue | `#005ea2` | Main data series |
| Accent Cyan | `#00687d` | Secondary series |
| Medium Blue | `#0076d6` | Tertiary series |
| Light Blue | `#2378c3` | Quaternary series |
| Error Red | `#b50909` | Negative trends |
| Success Green | `#00a91c` | Positive trends |

Never rely on color alone — always pair color encoding with another channel (pattern fill, label, or table data).

## Container pattern (markup template)

```html
<div class="usa-data-visualization"
     role="img"
     aria-labelledby="chart-title-budget"
     aria-describedby="chart-description-budget chart-table-budget">

  <h3 id="chart-title-budget" class="chart-title">
    Maryland State Agency Budgets, FY 2026
  </h3>

  <p id="chart-description-budget" class="chart-description">
    Transportation receives the largest budget allocation at $4.2B, followed by
    Education at $3.8B and Health at $3.5B. Health spending increased 15%
    year-over-year, the largest growth in any major category.
  </p>

  <!-- The visualization itself: SVG / canvas / library output goes here -->
  <div class="visualization-container" aria-hidden="true">
    <!-- chart rendering -->
  </div>

  <p class="chart-source">
    <small>
      Source:
      <a href="https://dbm.maryland.gov/budget" target="_blank" rel="noopener">
        Maryland Department of Budget and Management
      </a>
    </small>
  </p>

  <table id="chart-table-budget" class="usa-table usa-table--borderless"
         aria-label="Budget data table">
    <caption class="usa-sr-only">Maryland state agency budgets, billions of dollars</caption>
    <thead>
      <tr>
        <th scope="col">Agency</th>
        <th scope="col">Budget (Billions USD)</th>
      </tr>
    </thead>
    <tbody>
      <tr><th scope="row">Transportation</th><td>$4.2B</td></tr>
      <tr><th scope="row">Education</th><td>$3.8B</td></tr>
      <tr><th scope="row">Health</th><td>$3.5B</td></tr>
      <tr><th scope="row">Public Safety</th><td>$2.1B</td></tr>
    </tbody>
  </table>
</div>
```

**Key accessibility attributes:**
- `role="img"` — Identifies the visualization container as an image for assistive technology.
- `aria-labelledby` — Points to the title's id.
- `aria-describedby` — Points to the narrative paragraph's id and the data table's id.
- `aria-hidden="true"` (on the decorative rendering) — Hides the SVG/canvas because the description + table carry the data.
- `usa-sr-only` (on the caption) — Hides the caption visually while keeping it for screen readers.

## Pattern fills for color-blind users

When using color to encode data series, supplement with a pattern fill so users with color-vision deficiencies can still distinguish series:

```html
<div class="chart-bar chart-bar--pattern"
     style="width: 80%; background-color: #005ea2;"
     data-pattern="diagonal">
  <span class="chart-bar-value">$4.2B</span>
</div>
```

Common patterns: `diagonal` (45° stripes), `dots`, `grid`, `horizontal`. The MDWDS Storybook implements diagonal as `repeating-linear-gradient(45deg, transparent 0 10px, rgba(255,255,255,0.3) 10px 20px)`.

## What each class does

| Class | Effect |
|---|---|
| `usa-data-visualization` | Outer container. Provides vertical rhythm (`margin: 2rem 0`) and inherits MDWDS typography. Receives the ARIA labeling that links title, description, and table. |
| `usa-data-visualization--high-contrast` | Adds borders to bars (2px solid black) and uses higher-contrast colors for low-vision support. |
| `usa-data-visualization--accessible` | Uses pre-verified accessible color tokens for all data series. |
| `chart-title` | Heading style: ~24px, semibold, color `#1b1b1b`. The element is `<h3>` (or `<h2>` per page outline). |
| `chart-description` | Narrative paragraph: ~16px, line-height 1.5, color `#3d4551`. Reads as a standalone summary. |
| `visualization-container` | Wraps the rendered chart. Pale gray background (`#f0f0f0`), thin neutral border (`#dfe1e2`), rounded corners (~4px), generous padding (~32px). |
| `chart-bars` | Flex column wrapper for stacked bar groups (~16px gap). |
| `chart-bar-group` | One bar row. Flex row with label on the left, bar on the right, ~16px gap. |
| `chart-bar-label` | Bar label text. ~150px min-width, semibold, color `#1b1b1b`. |
| `chart-bar-wrapper` | Background track for the bar (~white, rounded corners). |
| `chart-bar` | The colored bar. ~40px height, padding ~16px, rounded corners, hover state at 0.8 opacity. Inline `style` controls width % and background color. |
| `chart-bar--pattern` | Adds a diagonal-stripe `repeating-linear-gradient` overlay for pattern-fill accessibility. |
| `chart-bar-value` | Value label inside the bar. Bold white text with a subtle dark text-shadow for legibility against any color background. |
| `chart-source` | Data source line: small (~14px), gray (`#71767a`). Link inside is `#005ea2` underlined. |
| `usa-table` / `usa-table--borderless` | The accessible data table beneath the chart. See `cdn/components/usa-table.md`. |
| `usa-sr-only` | Visually hides content while keeping it announced by screen readers. Used on the table caption so the chart's title doesn't double as the table's. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `title` | string | sample | Chart heading text |
| `description` | string | sample | Narrative summary paragraph |
| `dataSource` | string (URL) | sample | Source link href |
| `showDataTable` | bool | `true` | Render the accessible data table beneath the chart |
| `visualizationType` | `bar` \| `line` \| `stacked-bar` \| `multi-line` | `bar` | Demonstrated chart type (Storybook only — pick your own renderer in production) |
| `usePatternFills` | bool | `false` | Adds pattern overlays for color-blind users |
| `colorPalette` | `default` \| `high-contrast` \| `accessible` | `default` | Selects palette variant |
| `enableAnalytics` | bool | `false` | Adds `data-ga-*` attributes |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Heading level adjustment

`chart-title` is rendered as `<h3>` in the Storybook template. **Pick the heading level that matches the page outline** — a visualization that is itself the lead section after the hero should use `<h2 class="chart-title">`. See `cdn/composition.md`.

## Common mistakes

1. **Treating this as a turn-key chart component** — it isn't. You provide the rendering (SVG, canvas, library); USWDS provides the accessible scaffolding around it.
2. **Skipping the data table** — without it, screen reader users get only the narrative summary. The data table is the lossless accessible representation.
3. **Omitting `aria-labelledby` / `aria-describedby`** — the chart loses its association with its title and description, leaving screen readers without context.
4. **Hex colors that haven't been contrast-checked** — use the accessible palette tokens; verify any custom color at 4.5:1 against white before shipping.
5. **Color alone to encode data series** — pair with patterns, labels, or distinct shapes. Test in a color-blindness simulator.
6. **Heavy hover-to-reveal interactions** — minimize required interactions; key information must be visible without hover or click.
7. **No narrative summary** — a chart without a paragraph explaining the takeaway is harder to read for everyone and inaccessible to screen readers. Always include the "so what" in plain prose.
