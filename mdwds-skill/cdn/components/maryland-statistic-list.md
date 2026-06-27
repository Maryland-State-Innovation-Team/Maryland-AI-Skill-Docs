# maryland-statistic-list

Maryland Design System statistic list displays 1–4 large numbers (with optional descriptions) in a horizontally-arranged row, with a header above containing the section title, description, and an optional "more" link. Used to surface dashboard-style impact metrics.

> **Use `maryland-statistic-list` for at-a-glance numeric impact data.** For featured-link blocks, use `maryland-highlight`. For visual data charts, use `usa-data-visualizations`. For a single statement-and-image highlight, use `maryland-callout`.

## What it looks like

A statistic list is a `<section>` containing a centered (or side-by-side, for single-stat) layout:

- **Header**: title (`<h2>`, Merriweather light, 32px → 40px → 48px responsive), description paragraph (17–22px responsive), optional "more" link below.
- **List**: a flex row of items at tablet+ (column on mobile). 1, 2, 3, or 4 items.

Each item has:

- A large italic-bold Merriweather number ("`#20,000,000`" or "`#2 in U.S.`" — usually short text). Sizes are dramatic: 54px on mobile, scaling to 77px at mobile-lg, then variable by item count and viewport. For 4-stat layouts at desktop, the number compresses to ~34px.
- An optional description below: 16px Merriweather, `base-darkest`, with a 20px top margin.

Items are separated by a 1px `gray-cool-40` vertical line at tablet+. On mobile, the separator becomes a horizontal 160px line above each item except the first, with 40px vertical margin.

Single-stat (`--one`) is a special layout at tablet+: the header sits left, the single statistic sits right with a vertical border between, in an 8/4-column split.

Multi-stat layouts (`--two`, `--three`, `--four`) cap the header max-width at 846px (`spacing-multiple(105.75)`) and center it.

## Variants

| Variant | Layout |
|---|---|
| `maryland-statistic-list--one` | Header + single stat side-by-side at tablet+ (centered/full-width on mobile). |
| `maryland-statistic-list--two` | Centered header above 2 stats in a row (tablet+) / column (mobile). |
| `maryland-statistic-list--three` | Centered header above 3 stats. |
| `maryland-statistic-list--four` | Centered header above 4 stats. Each statistic number is the smallest of the four variants. |

## When to use

- Agency-impact dashboard ("$2.1B distributed | 14,800 households served | #2 in U.S.").
- Year-in-review section on a homepage.
- "Maryland by the numbers" content blocks.

Avoid statistic lists for non-numeric content, or for more than 4 items (use `maryland-highlight` or `maryland-link-collection` instead).

## Default markup — three statistics

```html
<section class="maryland-statistic-list maryland-statistic-list--three" aria-labelledby="sl-1">
  <div class="maryland-statistic-list__container">
    <div class="maryland-statistic-list__header">
      <h2 class="maryland-statistic-list__title" id="sl-1">Maryland by the numbers</h2>
      <div class="maryland-statistic-list__description">
        <p>U.S. News ranks Maryland in the top 20 states overall in its Best States 2026 rankings.</p>
      </div>
      <div class="maryland-statistic-list__more-link">
        <a class="maryland-link" href="/about/rankings">Read about our recent achievements</a>
      </div>
    </div>
    <ul class="maryland-statistic-list__list">
      <li class="maryland-statistic-list__item">
        <span class="maryland-statistic-list__statistic-text">#2</span>
        <span class="maryland-statistic-list__statistic-description">
          <p>in the U.S. for K-12 education</p>
        </span>
      </li>
      <li class="maryland-statistic-list__item">
        <span class="maryland-statistic-list__statistic-text">$2.1B</span>
        <span class="maryland-statistic-list__statistic-description">
          <p>in benefits distributed last fiscal year</p>
        </span>
      </li>
      <li class="maryland-statistic-list__item">
        <span class="maryland-statistic-list__statistic-text">17,000</span>
        <span class="maryland-statistic-list__statistic-description">
          <p>miles of public waterways</p>
        </span>
      </li>
    </ul>
  </div>
</section>
```

## Markup — single statistic (side-by-side layout)

```html
<section class="maryland-statistic-list maryland-statistic-list--one" aria-labelledby="sl-2">
  <div class="maryland-statistic-list__container">
    <div class="maryland-statistic-list__header">
      <h2 class="maryland-statistic-list__title" id="sl-2">Helping more Marylanders every year</h2>
      <div class="maryland-statistic-list__description">
        <p>Since 2018, the Maryland Department of Human Services has expanded SNAP outreach to every county, bringing more eligible families into the program.</p>
      </div>
    </div>
    <ul class="maryland-statistic-list__list">
      <li class="maryland-statistic-list__item">
        <span class="maryland-statistic-list__statistic-text">670,000</span>
        <span class="maryland-statistic-list__statistic-description">
          <p>Marylanders receiving SNAP benefits</p>
        </span>
      </li>
    </ul>
  </div>
</section>
```

At tablet+, the header takes 8/12 of the row and the single stat sits in a 4/12 right column with a vertical divider.

## Markup — two statistics (no description)

```html
<section class="maryland-statistic-list maryland-statistic-list--two" aria-labelledby="sl-3">
  <div class="maryland-statistic-list__container">
    <div class="maryland-statistic-list__header">
      <h2 class="maryland-statistic-list__title" id="sl-3">Workforce reach</h2>
    </div>
    <ul class="maryland-statistic-list__list">
      <li class="maryland-statistic-list__item">
        <span class="maryland-statistic-list__statistic-text">3.2M</span>
      </li>
      <li class="maryland-statistic-list__item">
        <span class="maryland-statistic-list__statistic-text">23</span>
        <span class="maryland-statistic-list__statistic-description">
          <p>counties served</p>
        </span>
      </li>
    </ul>
  </div>
</section>
```

The description span is optional per item.

## Markup — four statistics

```html
<section class="maryland-statistic-list maryland-statistic-list--four" aria-labelledby="sl-4">
  <div class="maryland-statistic-list__container">
    <div class="maryland-statistic-list__header">
      <h2 class="maryland-statistic-list__title" id="sl-4">Maryland economic impact</h2>
      <div class="maryland-statistic-list__description">
        <p>Fiscal year 2026 results across the Maryland Department of Commerce programs.</p>
      </div>
    </div>
    <ul class="maryland-statistic-list__list">
      <li class="maryland-statistic-list__item">
        <span class="maryland-statistic-list__statistic-text">$2.1B</span>
        <span class="maryland-statistic-list__statistic-description">
          <p>in business loans</p>
        </span>
      </li>
      <li class="maryland-statistic-list__item">
        <span class="maryland-statistic-list__statistic-text">14,800</span>
        <span class="maryland-statistic-list__statistic-description">
          <p>jobs supported</p>
        </span>
      </li>
      <li class="maryland-statistic-list__item">
        <span class="maryland-statistic-list__statistic-text">#2</span>
        <span class="maryland-statistic-list__statistic-description">
          <p>in U.S. innovation ranking</p>
        </span>
      </li>
      <li class="maryland-statistic-list__item">
        <span class="maryland-statistic-list__statistic-text">540</span>
        <span class="maryland-statistic-list__statistic-description">
          <p>small businesses launched</p>
        </span>
      </li>
    </ul>
  </div>
</section>
```

At desktop, the statistic-text size compresses (~34px) so all four numbers fit on a single row with vertical separators between them.

## What each class does

| Class | Effect |
|---|---|
| `maryland-statistic-list` | Base `<section>`. Applies `block-spacing` and `grid-container`. |
| `maryland-statistic-list--one` / `--two` / `--three` / `--four` | Sets the layout. `--one` uses an 8/4 side-by-side at tablet+. `--two`/`--three`/`--four` center the header and arrange stats horizontally with progressively smaller statistic-text sizes. |
| `maryland-statistic-list__container` | Inner wrapper. Center-aligned text. For `--one` at tablet+, becomes a flex row holding header and list. |
| `maryland-statistic-list__header` | Header block. 32/48/64px bottom margin (responsive). Centered (or left-aligned in `--one` at tablet+). Max-width 846px in multi-stat variants. |
| `maryland-statistic-list__title` | Heading (`<h2>`). Uses the `h2` mixin (Merriweather light), but at mobile-lg+ in stat-list context becomes heading-14 (40px). Zero margin. `ls(1)` letter-spacing. |
| `maryland-statistic-list__description` | Intro paragraph. body-6/7/9 (17/18/22px responsive). `base-darkest` color. 24/32px top margin. |
| `maryland-statistic-list__more-link` | Optional "more" link wrapper below the description. Body-4/6 size with 24/40/32px top margin (responsive). |
| `maryland-statistic-list__list` | The stats `<ul>`. List-style none. Flex column (mobile) → row (tablet+). |
| `maryland-statistic-list__item` | Each stat. Flex 1, position relative. Has a `::before` separator: horizontal 160×1px line above (mobile) or vertical 1px line on the left (tablet+). First item suppresses its `::before`. |
| `maryland-statistic-list__statistic-text` | The big number. Merriweather, italic, bold, `ls(-2)` (-0.02em). Size scales with item count and viewport: 54px (mobile, 320px+) → 77px (mobile-lg, 480px+); 48–64px in 3-stat; 24–46px in 4-stat depending on viewport. |
| `maryland-statistic-list__statistic-description` | Small label below the number. Heading-5 (16px) Merriweather with 28px line-height. 20px top margin. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `title` | string | — | Section heading |
| `hideTitle` | bool | false | Visually hide title (adds `usa-sr-only`) |
| `description` | string (HTML) | — | Description text — rendered via `unsafeHTML` |
| `hideDescription` | bool | false | Omit the description block entirely |
| `linkTitle` | string | — | "More" link label |
| `linkUrl` | string | — | "More" link URL |
| `hideLink` | bool | false | Omit the more-link |
| `items` | `Array<{statisticText, statisticDescription?}>` | — | 1–4 stats. Items without `statisticText` are filtered out. |

## Heading level adjustment

The title defaults to `<h2>`. When nested inside an already-`<h2>`-headed section, demote to `<h3>` and keep the class. The class supplies the typography; the element supplies the outline.

## Common mistakes

1. **More than 4 statistics** — the component caps out at 4. Beyond that, switch to a `usa-collection` or chart.
2. **Long statistic text** — the design assumes short numbers ("$2.1B", "17,000", "#2"). For long strings, line-breaks may look awkward at desktop sizes. Use a `maryland-callout` for prose-style emphasis.
3. **Skipping the variant class** — `maryland-statistic-list` alone gives no row layout. Set `--one`/`--two`/`--three`/`--four` to match the item count.
4. **Mismatching variant class with item count** — e.g., setting `--three` but supplying 2 items. The component auto-selects the variant; in hand-written markup, match them.
5. **Centering text further** — already centered via the container. Adding alignment utilities is redundant.
6. **Description spans without a `<p>` inside** — the component wraps the description in `<p>`; preserve that structure in hand-written markup so margins work.
