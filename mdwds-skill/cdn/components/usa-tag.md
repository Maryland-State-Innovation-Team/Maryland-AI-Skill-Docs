# usa-tag

A small pill-shaped label used to mark status, category, or metadata next to a content item. Common uses on Maryland.gov: marking a news article's topic ("Health", "Environment"), badging a service status ("Open", "Closed for renovation"), tagging a search result type ("Form", "Press release"), or annotating list items ("New", "Featured").

## What it looks like

A `usa-tag` is a tight, **uppercase**, **bold** label rendered as an inline `<span>`. The default fill is **Maryland blue** (`primary` → `blue-60v`, approximately `#1A4480`) with **white** text. The text is tracked uppercase via USWDS `text-uppercase` styling inside the component. Padding is small (≈4px top/bottom, ≈8px left/right) and the corners are slightly rounded — it reads as a compact rectangle, not a fully circular pill. Vertical alignment is baseline-friendly so it sits cleanly next to body text.

Variants change the background fill (and matching text color for contrast) or the size:

- **Default** (no color modifier) — Maryland blue background, white text.
- **`usa-tag--primary`** — Same as default. Explicit primary class for clarity when other colored tags are nearby.
- **`usa-tag--secondary`** — Maryland red/cool-red (`red-cool-50v`), white text. Use for elevated/urgent labels.
- **`usa-tag--accent-cool`** — Light cyan (`cyan-30v`), dark text. A softer tone.
- **`usa-tag--accent-warm`** — Gold (`gold-30v`), dark text. Warm accent.
- **`usa-tag--info`** — Light blue, dark text. Informational.
- **`usa-tag--success`** — Green, dark text. "Approved", "Open".
- **`usa-tag--warning`** — Amber, dark text. "Limited", "Closing soon".
- **`usa-tag--error`** — Red, white text. "Failed", "Rejected".
- **`usa-tag--emergency`** — Bright red, white text. "Emergency closure", state-of-emergency markers.

The size modifier:

- **`usa-tag--big`** — Increases font size and padding for tags that need to stand out (e.g., a hero badge or a single tag at the top of a listing card). The text-transform and weight stay the same.

Tags are inline. They flow with surrounding text. They do not break to a new line unless wrapped.

## Variants

| Variant | Class | Visual |
|---|---|---|
| Default / primary | `usa-tag` | Maryland blue, white text |
| Secondary | `usa-tag usa-tag--secondary` | Red, white text |
| Accent cool | `usa-tag usa-tag--accent-cool` | Light cyan, dark text |
| Accent warm | `usa-tag usa-tag--accent-warm` | Gold, dark text |
| Info | `usa-tag usa-tag--info` | Light blue, dark text |
| Success | `usa-tag usa-tag--success` | Green, dark text |
| Warning | `usa-tag usa-tag--warning` | Amber, dark text |
| Error | `usa-tag usa-tag--error` | Red, white text |
| Emergency | `usa-tag usa-tag--emergency` | Bright red, white text |
| Big (size) | add `usa-tag--big` | Larger font + padding |

## When to use which variant

- **Default / primary** — Categorical, neutral metadata. "Health", "Education", "Transportation" topics; document types ("PDF", "Form").
- **Secondary** — When you need to emphasize a tag among other primary tags (e.g., a "Featured" badge on one item in a list of standard-tag items).
- **Info / success / warning / error / emergency** — Status indicators. Mirror the matching alert semantics: success = approved/open, warning = limited, error = failed/closed, emergency = critical.
- **Accent-cool / accent-warm** — Categorical contrast where neither the default nor a semantic color fits.
- **`--big`** — One prominent tag (e.g., the topic badge inside a hero); not for ordinary in-line metadata where the default size keeps better rhythm with body text.

Never use tags as buttons. They are decorative labels; if a user must click to filter or navigate, use a link or button (or an `<a>` styled as a tag via the appropriate filter UI pattern).

## Default markup

```html
<span class="usa-tag">Health</span>
```

Used in context next to an article title:

```html
<h3>
  <a href="/news/clean-bay-grant" class="usa-link">
    DNR announces $4M Chesapeake Bay restoration grant
  </a>
  <span class="usa-tag">Environment</span>
</h3>
```

## Markup — secondary

```html
<span class="usa-tag usa-tag--secondary">Featured</span>
```

## Markup — semantic status colors

```html
<!-- Service is currently open -->
<span class="usa-tag usa-tag--success">Open</span>

<!-- Permits are limited -->
<span class="usa-tag usa-tag--warning">Limited availability</span>

<!-- Park is closed today -->
<span class="usa-tag usa-tag--error">Closed</span>

<!-- Emergency closure -->
<span class="usa-tag usa-tag--emergency">Emergency closure</span>

<!-- Informational -->
<span class="usa-tag usa-tag--info">Updated April 2026</span>
```

## Markup — big

```html
<span class="usa-tag usa-tag--big">Featured news</span>
```

## Markup — with screen-reader prefix for status

```html
<span class="usa-tag usa-tag--success">
  <span class="usa-sr-only">Status: </span>Open
</span>
```

The visually-hidden `usa-sr-only` text adds the word "Status" for screen-reader users so the tag reads as "Status: Open" rather than just "Open".

## What each class does

| Class | Effect |
|---|---|
| `usa-tag` | Base tag styling: inline-block `<span>`, **uppercase**, **bold** text, small padding (≈4px / 8px), small border-radius, default fill Maryland blue (`primary`) with white text. Font size is body scale 1 (smaller than body copy). |
| `usa-tag--big` | Increases font size and padding to roughly body-copy size. Use for one prominent badge; don't bulk-apply. |
| `usa-tag--primary` | Explicit primary background. Same look as plain `usa-tag` — use when other colored tags are present and you want to be explicit. |
| `usa-tag--secondary` | Background `secondary` (`red-cool-50v`), white text. |
| `usa-tag--accent-cool` | Background `accent-cool` (`cyan-30v`), dark text. |
| `usa-tag--accent-warm` | Background `accent-warm` (`gold-30v`), dark text. |
| `usa-tag--info` | Background `info` (light blue), dark text. |
| `usa-tag--success` | Background `success` (green), dark text. |
| `usa-tag--warning` | Background `warning` (amber), dark text. |
| `usa-tag--error` | Background `error` (red), white text. |
| `usa-tag--emergency` | Background `emergency` (bright red), white text. |

All color modifiers use the USWDS `set-text-and-bg` mixin, which automatically picks a contrast-AA-compliant text color for the chosen background.

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `size` | `default` \| `big` | `default` | Adds `usa-tag--big` when `big`. |
| `color` | `primary` \| `secondary` \| `accent-cool` \| `accent-warm` \| `info` \| `success` \| `warning` \| `error` \| `emergency` | `null` (no color modifier → primary fill) | Adds `usa-tag--{color}`. |
| `label` | string | `"Info"` | Text content. Will be auto-uppercased by CSS. |
| `ariaLabel` | string | `""` | Overrides the visible text for screen readers (rarely needed). |
| `ariaDescribedBy` | string | `""` | ID of an element describing the tag (optional). |
| `role` | string | `""` | Optional ARIA role (e.g., `"status"` for live-updating tags). |

## Accessibility

- **Tags convey meaning visually only.** If the color is the only thing distinguishing "Open" from "Closed", a colorblind user can't tell them apart. Always include a textual label that stands alone ("Open" / "Closed", not just a green/red dot).
- **Status semantics** — For tags that announce a live state ("Open"), prefix the label with a screen-reader-only word using `<span class="usa-sr-only">Status: </span>` so screen-reader users hear "Status: Open" instead of a bare "Open" in isolation.
- **Live status updates** — If the tag changes value based on application state (e.g., a real-time "Open" / "Closed" indicator), set `role="status"` so screen readers announce the change.
- **Don't wrap tags in `<button>` or `<a>`** — Tags are not interactive. If users must filter by tag, use a separate filter control (a chip-style filter UI is not a `usa-tag`).
- **Contrast** — Each variant pairs the background with an AA-contrast text color automatically. Don't override `color` inline.

## JS requirements

None. Tags are pure CSS, applied to a `<span>` (or another inline element).

## Common mistakes

1. **Putting long multi-word strings inside a tag.** `usa-tag` is `display: inline-block` with `text-transform: uppercase` and minimal padding (4px/8px). It's designed for **short, single-token labels** — `NEW`, `OPEN`, `URGENT`, `DRAFT`, `BETA`. Three-word descriptors like `UNHEALTHY FOR SENSITIVE GROUPS` will wrap mid-tag across multiple lines inside a table cell or card footer, with the uppercase + small font compounding the awkwardness. **Use a tag only when the label fits on one line and reads as one categorical token.** For longer status descriptors like AQI levels, severity ratings, or compliance states, use a colored `<span>` with utility classes instead — for example `<span class="text-bold text-error">Unhealthy for sensitive groups</span>` — or split the level into a short tag plus prose: `<span class="usa-tag usa-tag--secondary">USG</span> <span>Unhealthy for sensitive groups</span>`.
2. **Styling tags inline with custom colors** — `style="background: #1A4480"` defeats the design system. Pick a built-in color variant. If you need a color that isn't in the palette, the answer is almost always "use one that is".
2. **Using a tag as a button** — Tags are decorative. Wrapping a tag in `<a>` for a filter link is fine, but the click target must be the link, not the tag itself. Better: use the listing component's own filter UI.
3. **Color alone for status** — Green vs. red for "Open" vs. "Closed" without a textual difference fails WCAG 1.4.1. Always include the word.
4. **Mixing `--big` with body-paragraph tags** — A single big tag at the top of a card is fine; a paragraph full of `--big` tags throws off vertical rhythm.
5. **Hand-rolling uppercase or bold** — `usa-tag` already applies `text-transform: uppercase` and `font-weight: bold`. Adding `text-uppercase` or `text-bold` utilities is redundant.
6. **Forgetting a screen-reader prefix on status tags** — A bare "Open" tag inside a card is decoration; screen reader users may miss what it's labeling.
