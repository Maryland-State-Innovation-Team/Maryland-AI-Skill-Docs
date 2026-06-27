# usa-range-slider

The USWDS range slider is a styled `<input type="range">` — a draggable thumb on a horizontal track that selects a numeric value within a min/max bound. Use it for filtering (price/distance), settings (volume/zoom), or any value where the exact number matters less than its position within a range.

> Use this for numeric range selection on Maryland.gov pages. There is no `maryland-range-slider` — MDWDS inherits the USWDS component with Maryland color tokens. For a precise numeric entry (e.g., a tax-calculation field) use `usa-input` with `type="number"`; for a from-to date range, use `usa-date-range-picker`.

## What it looks like

A horizontal control with three pieces in a single row:

- **Track** — a thin (~12px tall) horizontal bar across the full available width. Light gray fill (`bg-base-lighter`) with the `bg-primary` Maryland-blue color filling the portion to the left of the thumb in supporting browsers, indicating the current value.
- **Thumb** — a circular Maryland-blue (`bg-primary`) handle ~24px in diameter, centered vertically on the track. The thumb has a thin white inner ring and a soft shadow. On focus, an outline draws around it (~2px solid `primary-dark`) per USWDS focus styling.
- **Tick stops** — none by default. The `step` attribute snaps the thumb to discrete values but no visible tick marks render.

Above the slider sits a standard `usa-label` (semibold body-size text). There is no built-in numeric readout — if you want the live value displayed, render your own `<output>` element and wire it with JS.

Keyboard support is native to `<input type="range">`: Left/Down arrow decrements by `step`, Right/Up increments by `step`, Page Up/Down adjusts by 10× step, Home/End jump to `min`/`max`.

Mobile rendering matches the browser default style modified by USWDS — the track is taller on iOS/Android for thumb hit-area, and the focus state is suppressed on touch.

## Default markup

```html
<form class="usa-form">
  <label class="usa-label" for="trail-distance">Trail length (miles)</label>
  <input
    id="trail-distance"
    name="trail-distance"
    class="usa-range"
    type="range"
    min="0"
    max="20"
    step="0.5"
    value="5"
  />
</form>
```

## Markup — fee calculator (0–500 dollars)

```html
<form class="usa-form">
  <label class="usa-label" for="permit-fee">Maximum permit fee (USD)</label>
  <input
    id="permit-fee"
    name="permit-fee"
    class="usa-range"
    type="range"
    min="0"
    max="500"
    step="25"
    value="100"
  />
</form>
```

## Markup — with live value readout

```html
<form class="usa-form">
  <label class="usa-label" for="zoom-level">Map zoom level</label>
  <input
    id="zoom-level"
    name="zoom-level"
    class="usa-range"
    type="range"
    min="1"
    max="18"
    step="1"
    value="10"
    aria-describedby="zoom-level-output"
    oninput="document.getElementById('zoom-level-output').value = this.value"
  />
  <output id="zoom-level-output" for="zoom-level">10</output>
</form>
```

The `<output>` element is a standard HTML form helper; pair it with an `oninput` handler (or your framework's equivalent) to display the live value. The slider itself doesn't render the number.

## Markup — with explicit ARIA label

```html
<form class="usa-form">
  <label class="usa-label" for="vol">Volume</label>
  <input
    id="vol"
    name="vol"
    class="usa-range"
    type="range"
    min="0"
    max="100"
    step="5"
    value="50"
    aria-label="Volume level percentage"
  />
</form>
```

Use `aria-label` only when the visible label is hidden or otherwise insufficient; the visible `<label for>` should be the primary association.

## What each class does

| Class | Effect |
|---|---|
| `usa-form` | Form wrapper. Constrains width and applies vertical spacing between fields. |
| `usa-label` | Block label above the slider. ~16px semibold, color `base-darkest`. |
| `usa-range` | Restyles the native `<input type="range">`: thin gray track, Maryland-blue circular thumb with white inner ring and soft shadow, USWDS focus ring on the thumb. Hides the browser's default chrome cross-platform. |
| `type="range"` (attr) | Native HTML5 range slider. Required — `usa-range` is a class on top of the native element, not a replacement. |
| `min` / `max` / `step` / `value` (attrs) | Native HTML5 attributes that define the range, the increment, and the initial value. |
| `aria-label` (attr) | Optional accessible name override; only use when the visible `<label>` isn't sufficient. |
| `aria-describedby` (attr) | Reference to a separate description element (e.g., a live `<output>`). |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `label` | string | `"Range slider"` | Visible label |
| `id` | string | `"usa-range"` | Required; matches `<label for=>` |
| `name` | string | `"usa-range"` | Form submission name |
| `min` | number | `0` | Lower bound |
| `max` | number | `100` | Upper bound |
| `step` | number | `5` | Increment between values |
| `value` | number | `20` | Initial value |
| `ariaLabel` | string | `""` | Optional screen-reader-only label |
| `ariaDescribedBy` | string | `""` | ID of a description element |
| `enableAnalytics` | bool | `false` | Toggle GA attributes |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Accessibility

- The `<label>` must associate with the slider via `for=`/`id`. Native `<input type="range">` exposes `aria-valuemin`, `aria-valuemax`, and `aria-valuenow` automatically based on the `min`/`max`/`value` attributes — do not duplicate them by hand.
- The native `<input type="range">` already announces the current value to screen readers as the user moves the thumb. If the slider's value carries an *unit* that the user needs to hear (e.g., "5 miles", "10%"), include the unit in the `<label>` or use `aria-valuetext` on the input to override the announced text.
- Keyboard support is fully native: Left/Down/Right/Up arrows step by `step`, Page Up/Down by ~10× step, Home/End jump to `min`/`max`.
- If you display a live numeric readout next to the slider, mirror it in an `aria-live` region only if it's not already announced — duplicating values can be noisy for screen readers.
- Do not use the slider for a value the user needs to know precisely (a phone number, a price within a few cents). Pair with a numeric `<input>` or use `usa-input` instead.

## JS requirements

No JS required. The control is a native HTML5 `<input type="range">`; all interactions (drag, keyboard, focus) are browser-native. Works fully with or without `mdwds-core.js` loaded. (You will still want the CDN CSS for styling — without it, the slider renders with the browser default look.)

If you add a live `<output>` next to the slider, the `oninput` handler is yours to write; USWDS does not provide one.

## Common mistakes

1. **Reading the value on `change` only** — `change` fires once when the user releases the thumb. For a live readout you need `input` (fires on every step). The documented example uses `oninput`.
2. **Using `usa-range` without `type="range"`** — the class restyles the native range input; on any other element it does nothing.
3. **Choosing a `step` that doesn't divide `max - min` evenly** — the slider can never reach `max`. E.g., `min=0`, `max=100`, `step=7` lands on 98, then jumps to 100 only if a final partial step is allowed.
4. **Using the slider for precise numeric entry** — sliders are inherently imprecise. Use a numeric `usa-input` for exact values; a slider is for "roughly this much" interactions.
5. **Forgetting to set `min` and `max`** — the browser default is 0–100, but always state both attributes so server-side handlers can validate the submitted range.
6. **Missing a visible label** — `<label for="...">` is required for accessibility. `aria-label` is a fallback, not a primary substitute.
