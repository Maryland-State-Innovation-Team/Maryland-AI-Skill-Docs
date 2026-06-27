# Foundation — Colors, Typography, Tokens

MDWDS inherits from USWDS and adds Maryland-specific colors and type tuning. The CDN stylesheet exposes everything as utility classes and CSS custom properties.

## Color palette

MDWDS uses the USWDS color system with Maryland-themed swatches. Every color has a name and up to 8 variations.

### Palette names (color families)

| Name | What it's for | Visual |
|---|---|---|
| `base` | Neutrals (grays). All text, borders, dividers. | Gray |
| `primary` | Brand primary, links, primary CTAs. | Maryland blue (cool blue, ~#1A4480) |
| `secondary` | Accent / call-out. | Maryland gold/orange |
| `accent-cool` | Cool accent (additional buttons, badges). | Lighter blue |
| `accent-warm` | Warm accent. | Soft red/orange |
| `info` | Informational alerts. | Light blue |
| `success` | Success alerts. | Green |
| `warning` | Warning alerts. | Amber |
| `error` | Error alerts. | Red |
| `emergency` | Emergency alerts. | Bright red |
| `disabled` | Disabled UI state. | Mid-gray |

### Variations (within a family)

`lightest`, `lighter`, `light`, (default), `vivid` (primary/secondary only), `dark`, `darker`, `darkest`

### Utility classes

```css
.text-{color}             /* default variation */
.text-{color}-{variation} /* e.g. text-base-darkest */
.bg-{color}-{variation}   /* e.g. bg-primary-lightest */
.border-{color}-{variation}
```

Examples:
- `text-base-darkest` — body text default (near-black)
- `text-primary` — link color (Maryland blue)
- `bg-base-lightest` — section background tint
- `bg-primary-darker` — dark blue panel
- `text-error` — error message text

### CSS custom properties

For custom CSS situations (rare — the utility classes should cover everything):

```css
.example {
  background-color: var(--maryland-color-primary);
  color: var(--maryland-color-base-darkest);
  border-color: var(--maryland-color-base-light);
}
```

### When to use color

- Use color **intentionally** and **consistently**. Pick the primary blue for primary actions; don't mix primary + accent-cool buttons in the same row.
- **Never** use color alone to convey meaning (e.g. don't make errors red-only — pair with an icon or text label).
- Stick to the palette. Don't introduce custom hex values.

## Typography

### Fonts

| Family | Where it's used | Source |
|---|---|---|
| **Source Sans Pro Web** | Body text, h4–h6, buttons, all UI | Loaded automatically via the CDN |
| **Merriweather** | h1, h2, h3 (display headings) | Loaded automatically |

Both fonts are auto-included by the CDN stylesheet. No `@font-face` rules needed.

### Heading sizes

| Level | Mobile (320px) | Mobile-lg (480px) | Desktop (1024px) | Desktop (narrow column) | Font |
|-------|---|---|---|---|---|
| `h1` | 32px | 40px | 48px | 40px | Merriweather light |
| `h2` | 24px | 40px | 40px | 32px | Merriweather light |
| `h3` | 22px | 28px | 28px | — | Merriweather light |
| `h4` | 22px | — | — | — | Source Sans Pro semibold |
| `h5` | 16px | — | — | — | Source Sans Pro semibold |
| `h6` | 16px | 17px | — | — | Source Sans Pro semibold |

- h1–h3 letter-spacing: `0.02em`
- h1–h3 font-weight: `light` (300)
- h4–h6 font-weight: `semibold` (600)
- At desktop, h1 and h2 reduce their size automatically when placed in a narrow column (e.g., alongside a sidebar) via container queries — no manual class needed.

### Body text

- **Base:** 19.2px / 1.6 line-height (Source Sans Pro)
- **Desktop (1024px+):** 22px / 40px line-height

The `paragraph-text` mixin applied to every `<p>` inside `usa-prose`.

### Lists

The `usa-list-styles` mixin applies:
- Colored markers (secondary color by default)
- Ordered list nesting cycle: decimal → lower-latin → lower-roman
- Definition list spacing

### Typography classes

The standard headings (`<h1>` through `<h6>`) inside `usa-prose` automatically get the styles above. For non-prose contexts (e.g. card headings), use the BEM class names from the component reference — e.g. `maryland-card__heading`.

For one-off typography overrides, USWDS provides:

| Class | Effect |
|---|---|
| `usa-prose` | Apply heading + body + list defaults to everything inside |
| `font-heading-{size}` | Heading font scale (1–18) |
| `font-body-{size}` | Body font scale |
| `text-bold`, `text-semibold`, `text-light` | Weight |
| `text-italic` | Italic |
| `text-uppercase`, `text-no-uppercase` | Case |
| `text-center`, `text-left`, `text-right` | Alignment |
| `text-no-underline` | Remove link underline |
| `text-tabular` | Tabular numerals |

## Spacing scale

USWDS spacing scale (used by `margin-*`, `padding-*`, `block-spacing`):

| Token | Pixels |
|---|---|
| 0 | 0 |
| 05 | 4 |
| 1 | 8 |
| 2 | 16 |
| 3 | 24 |
| 4 | 32 |
| 5 | 40 |
| 6 | 48 |
| 7 | 56 |
| 8 | 64 |
| 9 | 72 |
| 10 | 80 |
| 15 | 120 |

See `cdn/composition.md` for how to apply spacing.

## Iconography

MDWDS includes Material Symbols icons via `@material-symbols/svg-400`. Most icons appear inside components (e.g. the translation globe inside the banner). For standalone icon use, see the `maryland-icon` component reference.

## Accessibility tokens

- Color combinations in the palette are pre-checked against WCAG AA contrast (4.5:1 for body text, 3:1 for large text).
- Focus rings: 2px solid `#005ea2` (primary), 2px offset — applied automatically to focusable elements.
- Skip link (`usa-skipnav`) — visually hidden until focused.

## Common mistakes

1. **Hex codes in markup** (`color: #1A4480`) — use `text-primary` or `var(--maryland-color-primary)`.
2. **Custom @font-face rules** — fonts are loaded by the CDN; don't re-declare them.
3. **Inline font-family overrides** — let the component styles do it.
4. **Wrong heading level for visual size** — sizes adjust to level automatically. Use the semantically correct level; don't pick by appearance.
5. **Using accent colors as primary actions** — primary actions = primary color. Accent is for accents.

## Further reading

- USWDS Color: https://designsystem.digital.gov/design-tokens/color/
- USWDS Typography: https://designsystem.digital.gov/design-tokens/typesetting/
- W3C Contrast (AAA): https://www.w3.org/WAI/test-evaluate/preliminary/#contrast
