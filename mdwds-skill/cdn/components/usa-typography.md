# usa-typography

USWDS typography utility classes for headings, body text, font families, sizes, line heights, and line lengths. This file is a quick reference for the utility classes most commonly used inside MDWDS pages — see `cdn/foundation.md` for the comprehensive typography system (fonts, heading scale, body sizes), and `cdn/composition.md` for the `usa-prose` wrapper that applies all of these automatically inside free-form text blocks.

> **Default rule:** if you're authoring free-form body text (paragraphs, lists, headings together), wrap it in `<div class="usa-prose">` and let the design system do the work. Reach for individual typography utility classes only when `usa-prose` isn't applicable (inside a card, callout, or component body that handles its own typography).

## What it looks like

The MDWDS type system has two display families and one monospace, all loaded automatically by the CDN:

| Family | Used for | Font |
|---|---|---|
| `font-sans-*` | Body text, h4–h6, buttons, UI | **Source Sans Pro Web** |
| `font-serif-*` | h1, h2, h3 (display headings) | **Merriweather** (light weight, 300) |
| `font-mono-*` | Code, tabular data, monospaced needs | **Roboto Mono** |

Sizes use a numeric token scale: `font-{family}-{size}`. The same numeric scale also drives line-height (`line-height-{family}-{n}`), measure (`measure-{n}`), and heading utilities (`font-heading-{token}`). Higher numbers are larger; the scale isn't pixel-direct but ranges roughly from `micro` (10–11px) up through `12` (~5rem display sizes).

See `cdn/foundation.md` for the heading size table at each breakpoint and the full body-text scale.

## The most useful classes

### Apply prose styling to a body block

| Class | Effect |
|---|---|
| `usa-prose` | Wraps free-form text. Applies Source Sans Pro Web body (~19.2px / 1.6 line-height base, 22px at desktop), Merriweather light for h1–h3 with `0.02em` letter-spacing, USWDS list styling, USWDS link styling. See `cdn/composition.md` for full details. |
| `usa-intro` | Lead paragraph style. Larger text (~22px) and tuned line-height for an introductory paragraph. Use on the first `<p>` after a section heading. |
| `usa-dark-background` | Inverts text and link colors for use on dark backgrounds (white text, lighter link colors). |
| `usa-display` | Display-headline scale. Applied to `<h1>` to make it the largest hero-style heading on the page. |

### Heading-scale utilities

| Class | Effect |
|---|---|
| `font-heading-3xl` | Display-sized heading (largest). |
| `font-heading-2xl` | Large display heading. |
| `font-heading-xl` | XL heading. |
| `font-heading-lg` | Large heading. |
| `font-heading-md` | Medium heading. |
| `font-heading-sm` | Small heading. |
| `font-heading-xs` | Extra-small heading. |

Use these to apply heading typography to non-heading elements (e.g., a `<p>` that should look like a heading), or to deliberately give one heading the visual weight of a different level. **Keep the underlying HTML heading level semantically correct.** See `cdn/composition.md`.

### Font-family and size utilities

| Class | Effect |
|---|---|
| `font-sans-{size}` | Source Sans Pro Web at the given size token. Tokens: `micro`, `1`–`12`. |
| `font-serif-{size}` | Merriweather at the given size token. |
| `font-mono-{size}` | Roboto Mono at the given size token. |

Approximate sizes: `5` = ~16px (the recommended minimum for body text), `7` = ~20px, `9` = ~28px, `12` = ~64px (display).

### Line-height utilities

| Class | Effect |
|---|---|
| `line-height-sans-1` to `line-height-sans-6` | Sans-family line-height from tight (1) to loose (6). Use 4–5 for extended reading. |
| `line-height-serif-1` to `line-height-serif-6` | Serif-family equivalent. |
| `line-height-mono-1` to `line-height-mono-6` | Monospace equivalent. |

### Measure (line length) utilities

| Class | Effect |
|---|---|
| `measure-1` to `measure-6` | Max line length. `measure-2` (~66 characters) is the USWDS recommendation for extended reading. Lower numbers = shorter lines. |
| `measure-none` | Removes the measure constraint (no max-width). |

### Weight, case, alignment

| Class | Effect |
|---|---|
| `text-bold` | `font-weight: 700` |
| `text-semibold` | `font-weight: 600` |
| `text-light` | `font-weight: 300` |
| `text-italic` | `font-style: italic` |
| `text-uppercase` | `text-transform: uppercase` |
| `text-no-uppercase` | `text-transform: none` |
| `text-center` / `text-left` / `text-right` | Horizontal alignment |
| `text-no-underline` | Remove link underline |
| `text-tabular` | Tabular numerals (`font-variant-numeric: tabular-nums`) |

## Typical patterns

### A section heading and intro paragraph

```html
<h2>Apply for a small business grant</h2>
<p class="usa-intro">
  Maryland businesses with fewer than 50 employees can apply for grants up to $25,000 to cover equipment, training, or facility upgrades. Applications open quarterly.
</p>
<p>
  Eligibility, application materials, and review timelines vary by program. Use the program selector below to find the grant best suited to your business.
</p>
```

Inside a `usa-prose` block this works without explicit `usa-intro` styling needing extra setup — the lead paragraph class still applies.

### A small uppercase label (eyebrow)

```html
<p class="text-uppercase text-bold font-sans-2">Service category</p>
<h2 class="font-heading-xl">Driver and vehicle services</h2>
```

### Tabular financial figures

```html
<p class="text-tabular font-mono-5">
  Tax owed: $2,481.50
</p>
```

### Body text with a controlled measure

```html
<p class="font-sans-5 line-height-sans-5 measure-2">
  This paragraph is constrained to roughly 66 characters per line for comfortable reading. Long, full-viewport-width paragraphs are exhausting to read; the measure utility caps them at a comfortable width without requiring a layout column.
</p>
```

## What each class does

See the tables above for the full effect of each class. Key takeaways:

- **`usa-prose`** is the single most powerful class. Use it whenever you have a block of mixed paragraphs, headings, lists, and links — it sets everything correctly. Don't reach for individual utility classes inside `usa-prose`; they'll mostly be redundant.
- **`font-{family}-{n}` + `line-height-{family}-{n}` + `measure-{n}`** is the standard combination outside of prose blocks (e.g., inside a card body).
- **`font-heading-*`** lets you give any element the appearance of a heading level without changing its semantic element. Use sparingly.
- **`text-tabular`** is essential for any column of numbers — without it, proportional digits make columns ragged.

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `headingLevel` | `display` \| `h1` \| `h2` \| `h3` \| `h4` \| `h5` \| `h6` | `h2` | The HTML heading level. `display` renders an `<h1>` with `font-heading-3xl`. |
| `headingText` | string | sample | Heading content |
| `showLead` | bool | `true` | Render a `<p class="usa-intro">` introductory paragraph |
| `leadText` | string | sample | Lead paragraph content |
| `bodyText` | string | sample | Body paragraph content |
| `fontFamily` | `sans` \| `serif` \| `mono` | `sans` | Selects `font-{family}-{size}` |
| `fontSize` | `micro` \| `1`–`12` | `5` | Selects the size token (5 ≈ 16px) |
| `lineHeight` | `1`–`6` | `5` | Selects `line-height-{family}-{n}` |
| `measure` | `none` \| `1`–`6` | `2` | Selects `measure-{n}` (or removes it) |

## When to reach for the prose wrapper vs utilities

- **Free-form body content** (article text, FAQs answer bodies, "About this service" sections) → wrap in `<div class="usa-prose">`. Done. Don't add per-element utility classes inside.
- **Inside a component body** (card, summary box, alert, callout) — the component handles typography. Use utility classes only for one-off overrides.
- **A single non-prose element** that needs heading-style typography or specific weight — use individual utilities (`font-heading-xl`, `text-bold`, etc.).
- **A column of numbers** — `text-tabular` plus a font-mono-* size.

For full guidance see `cdn/composition.md` (prose wrapper) and `cdn/foundation.md` (palette, fonts, type scale, accessibility tokens).

## Common mistakes

1. **Hand-typed `font-family: 'Source Sans Pro';` declarations** — fonts are loaded by the CDN. Use the utility class (`font-sans-*`) instead.
2. **Wrapping a whole page in `usa-prose`** — components inside lose their tuned typography. Use `usa-prose` for free-form text blocks only.
3. **Picking a heading level by visual size instead of outline** — semantic level must match the page outline. Use `font-heading-*` to adjust visual size while keeping the semantic level correct. See `cdn/composition.md`.
4. **Forgetting `text-tabular` on number columns** — proportional digits create uneven column edges. Always add `text-tabular` for figures.
5. **Inline `style="font-size: 16px"`** — use `font-sans-5`. The scale exists so spacing, line-height, and measure stay consistent across the page.
6. **Reusing `usa-intro` on every paragraph** — it's meant for one lead paragraph per section, not for emphasis. For emphasis use `text-bold`.
