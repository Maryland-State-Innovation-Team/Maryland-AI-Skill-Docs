# usa-icon

Inline SVG icon helper for using Material Symbols (Google's open-source icon set, included in the MDWDS CDN bundle) anywhere in body content. Provides a consistent size scale, automatic color inheritance, and accessibility defaults.

## What it looks like

A `usa-icon` is an `<svg>` element styled to display as a block-level square sized by the USWDS type scale. Default size is `usa-icon--size-3` (~16px square at base font size, though the rendered icon may scale up depending on the size modifier).

Icons inherit their color from `currentColor`, so they pick up the text color of their parent. You can change the color via:
- A nearby USWDS color utility class (`text-primary`, `text-error`, `text-success`).
- An inline `style="color: ...;"` (rare — prefer utility classes).
- The `color` property on the surrounding component (e.g., `usa-icon-list--primary` sets icon color via `currentColor`).

Icons are **decorative by default** (`aria-hidden="true"`). For icons that carry meaning, set `aria-hidden="false"` and provide an `aria-label`.

The size scale (USWDS tokens 3 through 9) maps to incremental pixel sizes:

| Size token | Pixel size (at base type) |
|---|---|
| `usa-icon--size-3` | ~16px (small inline icon) |
| `usa-icon--size-4` | ~22px |
| `usa-icon--size-5` | ~24px (default for many components) |
| `usa-icon--size-6` | ~32px |
| `usa-icon--size-7` | ~40px |
| `usa-icon--size-8` | ~56px |
| `usa-icon--size-9` | ~64px (display-sized) |

The MDWDS CDN bundle includes the full Material Symbols set via `@material-symbols/svg-400`. Common glyphs:

- Navigation: `arrow_forward`, `arrow_back`, `arrow_upward`, `arrow_downward`, `menu`, `more_vert`, `more_horiz`, `close`
- Status: `check`, `check_circle`, `error`, `warning`, `info`, `help`
- Actions: `add`, `remove`, `edit`, `delete`, `settings`, `search`, `file_download`
- Content: `mail`, `phone`, `calendar_today`

(The MDWDS Storybook bundles inline SVG paths for the most-used glyphs — `check`, `close`, `search`, four arrows, `add`, `remove`, `delete`, `edit`, `check_circle`, `error`, `warning`, `info`, `calendar_today`, `mail`, `phone`, `file_download`, `settings`, `menu`, `more_vert`, `more_horiz`. For any other Material Symbols glyph, render via the sprite reference pattern documented below.)

## Two ways to render an icon

### 1. Inline SVG with path data

The simplest form — embed the SVG path data directly:

```html
<svg class="usa-icon usa-icon--size-5" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
  <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z" />
</svg>
```

### 2. Sprite reference (USWDS standard)

For sites that include the USWDS icon sprite file:

```html
<svg class="usa-icon usa-icon--size-5" aria-hidden="true" focusable="false" role="img">
  <use xlink:href="/assets/img/sprite.svg#check"></use>
</svg>
```

The sprite reference is the canonical USWDS pattern. Inline path data is shown in the MDWDS Storybook for self-contained example markup.

## Default markup

```html
<svg class="usa-icon usa-icon--size-5" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
  <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z" />
</svg>
```

## Markup — small icon

```html
<svg class="usa-icon usa-icon--size-3" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
  <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z" />
</svg>
```

## Markup — colored icon (via utility class)

```html
<span class="text-success">
  <svg class="usa-icon usa-icon--size-7" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z" />
  </svg>
</span>
```

The icon picks up `currentColor`, which inherits from `text-success` on the wrapper (`color-success` green).

## Markup — meaningful icon with accessibility

```html
<button type="button" class="usa-button usa-button--unstyled">
  <svg class="usa-icon usa-icon--size-5" aria-hidden="false" aria-label="Delete record" focusable="false" role="img" viewBox="0 0 24 24">
    <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z" />
  </svg>
</button>
```

When the icon is the only content of an interactive element (a button, a link), it must carry an accessible label. Set `aria-hidden="false"` and add `aria-label`.

## Markup — icon next to text (decorative)

```html
<a class="usa-link" href="/forms/W-4">
  Download Form W-4
  <svg class="usa-icon usa-icon--size-3" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
    <path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z" />
  </svg>
</a>
```

The text already describes the action; the icon is purely decorative.

## What each class does

| Class | Effect |
|---|---|
| `usa-icon` | Base icon class. Sets `display: block`, default square dimensions matching `usa-icon--size-3` (~16px), `fill: currentColor` so the icon's color inherits from the parent. |
| `usa-icon--size-3` | Smallest size, ~16px square. |
| `usa-icon--size-4` | ~22px square. |
| `usa-icon--size-5` | ~24px square. Default for many components (alerts, summary boxes). |
| `usa-icon--size-6` | ~32px square. |
| `usa-icon--size-7` | ~40px square. |
| `usa-icon--size-8` | ~56px square. |
| `usa-icon--size-9` | ~64px square. Largest size, display-headline scale. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `iconName` | enum (Material Symbols glyph) | `check` | Selects which path data to render. See full list above. |
| `size` | `3`–`9` | `5` | Applies `usa-icon--size-{N}` |
| `color` | string (color value) | `""` | Inline `color` style. Prefer USWDS color utility classes on a wrapper. |
| `ariaLabel` | string | `""` | Accessible label for meaningful icons. Used when `ariaHidden` is false. |
| `ariaHidden` | bool | `true` | `true` for decorative icons (default); `false` for meaningful icons that carry information not present in surrounding text. |
| `enableAnalytics` | bool | `false` | Adds `data-ga-*` attributes |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Coloring icons

Three approaches, in order of preference:

1. **Inherit from a wrapper utility class** (best for design-system consistency):
   ```html
   <span class="text-error">
     <svg class="usa-icon usa-icon--size-5">...</svg>
   </span>
   ```
2. **Inherit from a component variant** — e.g., `usa-icon-list--primary` sets icon color via descendant rules.
3. **Inline `style="color: #..."`** — last resort. Breaks design tokens; use only for one-off colors not in the palette.

Never set `fill` directly on the `<svg>` — icons use `fill: currentColor`, so `color` controls everything.

## Common mistakes

1. **Forgetting `aria-hidden="true"` on decorative icons** — screen readers read out the SVG's title/path, producing noise.
2. **`aria-hidden="true"` on a meaningful icon-only button** — the button has no accessible name. Use `aria-hidden="false"` + `aria-label`.
3. **`focusable="false"` omitted** — without it, some browsers (older IE/Edge) allow tabbing into the SVG.
4. **Setting `fill="#1A4480"` on the `<svg>`** — overrides `currentColor` and breaks color inheritance from utility classes.
5. **Picking a glyph that isn't in the Material Symbols set** — the CDN bundle covers the official set. For custom glyphs, embed inline SVG path data and skip the sprite reference.
6. **Forgetting `viewBox="0 0 24 24"`** — Material Symbols paths assume this viewBox. Without it, the icon won't render correctly when sized.
7. **Stretching icons via inline `width`/`height`** — use a `usa-icon--size-N` class instead so the icon matches the design-system scale.
