# usa-date-picker

The USWDS date picker is a single-date input paired with a calendar popup. The user can type a date directly (mm/dd/yyyy) or click the calendar icon to open a month grid and pick a day visually. Use it for any single-date field where browsing nearby dates helps — appointment scheduling, license renewal, application deadlines.

> Use this for single-date selection on Maryland.gov pages. There is no `maryland-date-picker` — MDWDS inherits the USWDS date-picker with Maryland color tokens applied automatically. For dates the user *already knows* (birthdays, anniversaries) prefer `usa-memorable-date`. For a from-to range, use `usa-date-range-picker`.

## What it looks like

The closed control is a single-line text input (`usa-input` styling: ~48px tall, white background, thin gray border, square corners) with a calendar icon button attached to the right edge. The icon button is a square ~48px Maryland-blue (`bg-primary`) tile with a white calendar glyph — clicking it opens the calendar popup.

The popup is a floating white card with a subtle shadow that hangs below the input. The top row holds three controls: a "previous month" arrow on the left, a centered button reading the current month and year (e.g. "February 2026") that opens a month/year picker on click, and a "next month" arrow on the right. Below that is a row of 7 short weekday labels (S M T W T F S) in small uppercase gray text, then a 6-row grid of day cells.

Each day cell is a square ~48px button. Day numbers sit centered in body-size text. Cells outside the current month appear lighter gray (`text-base-light`). Hover or keyboard-focus draws a Maryland-blue outline around the cell and tints its background. The currently selected day is filled in Maryland blue (`bg-primary`) with white text. Today's date has a thin underline beneath the number when it isn't selected. Disabled dates (outside the min/max range, or before the `rangeDate` highlight start) appear muted with a strikethrough cursor.

Clicking the month/year button swaps the day grid for a 3×4 month grid; clicking again swaps to a year grid (current decade with prev/next arrows). Pressing Escape or clicking outside closes the popup without changing the value.

Once a date is selected, the input field updates to `MM/DD/YYYY` text and the popup closes. The same value can be typed directly into the input; the calendar reads and reflects the typed date when reopened.

## Default markup

```html
<div class="usa-form-group">
  <label class="usa-label" id="renewal-label" for="renewal-date">Vehicle registration renewal date</label>
  <div class="usa-hint" id="renewal-hint">mm/dd/yyyy</div>
  <div class="usa-date-picker">
    <input
      class="usa-input"
      id="renewal-date"
      name="renewal-date"
      aria-labelledby="renewal-label"
      aria-describedby="renewal-hint"
    />
  </div>
</div>
```

The USWDS JavaScript wraps the `<input>` with the calendar button and popup at runtime.

## Markup — with default value

```html
<div class="usa-form-group">
  <label class="usa-label" id="appt-label" for="appt-date">Appointment date</label>
  <div class="usa-hint" id="appt-hint">mm/dd/yyyy</div>
  <div class="usa-date-picker" data-default-value="2026-08-15">
    <input
      class="usa-input"
      id="appt-date"
      name="appt-date"
      aria-labelledby="appt-label"
      aria-describedby="appt-hint"
    />
  </div>
</div>
```

`data-default-value` uses ISO format (`YYYY-MM-DD`); the displayed input shows the user-facing `MM/DD/YYYY` format.

## Markup — min/max range

```html
<div class="usa-form-group">
  <label class="usa-label" id="permit-label" for="permit-date">Hunting permit start date</label>
  <div class="usa-hint" id="permit-hint">mm/dd/yyyy</div>
  <div
    class="usa-date-picker"
    data-min-date="2026-09-01"
    data-max-date="2027-01-31"
  >
    <input
      class="usa-input"
      id="permit-date"
      name="permit-date"
      aria-labelledby="permit-label"
      aria-describedby="permit-hint"
    />
  </div>
</div>
```

Dates outside `data-min-date`–`data-max-date` are visually disabled in the calendar and rejected if typed.

## Markup — range highlight

```html
<div class="usa-form-group">
  <label class="usa-label" id="checkout-label" for="checkout-date">Checkout date</label>
  <div class="usa-hint" id="checkout-hint">mm/dd/yyyy</div>
  <div class="usa-date-picker" data-range-date="2026-07-04">
    <input
      class="usa-input"
      id="checkout-date"
      name="checkout-date"
      aria-labelledby="checkout-label"
      aria-describedby="checkout-hint"
    />
  </div>
</div>
```

`data-range-date` tells the calendar to visually highlight the span between that anchor and the hovered/selected date — used for date-range-picker coordination but valid on a standalone date picker.

## What each class does

| Class | Effect |
|---|---|
| `usa-form-group` | Vertical container for one labeled field. Bottom margin ~24px to separate from the next field. |
| `usa-label` | Block label above the field. ~16px semibold, color `base-darkest`. |
| `usa-hint` | Small gray helper text (~14px) below the label and above the input. Use it to show the expected format (`mm/dd/yyyy`). |
| `usa-date-picker` | Wrapper around the `<input>`. After JS init, becomes a flex row with the input on the left and a calendar-icon button on the right; serves as anchor for the popup. |
| `usa-input` | Standard text input styling: ~48px tall, white, thin gray border, square corners, body-size text. |
| `usa-date-picker__external-input` | (Generated at runtime.) The text input the user types into (the original `<input>` is preserved alongside as the hidden form control with ISO value). |
| `usa-date-picker__button` | (Generated at runtime.) Calendar-icon launcher button. Square Maryland-blue tile attached to the input's right edge. |
| `usa-date-picker__calendar` | (Generated at runtime.) Floating popup container. White background, subtle shadow, sits anchored below the input. |
| `usa-date-picker__calendar__date` | (Generated at runtime.) Each day cell in the month grid. ~48px square, body text centered. |
| `usa-date-picker__calendar__date--selected` | Filled Maryland blue with white text. |
| `usa-date-picker__calendar__date--today` | Underline under the day number. |
| `usa-date-picker__calendar__date--focused` | Outlined Maryland blue (keyboard navigation marker). |
| `data-default-value` (attr) | On the wrapper. ISO date string (`YYYY-MM-DD`) that pre-fills the input. |
| `data-min-date` (attr) | Earliest selectable date in ISO format. |
| `data-max-date` (attr) | Latest selectable date in ISO format. |
| `data-range-date` (attr) | Anchor date for range highlighting (used by `usa-date-range-picker`). |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `label` | string | `"Appointment date"` | Visible label |
| `hintText` | string | `"mm/dd/yyyy"` | Hint shown above the field |
| `name` | string | derived | Form field name |
| `required` | bool | `false` | Adds `required` to the input |
| `disabled` | bool | `false` | Disables input and calendar button |
| `defaultValue` | string (ISO) | `""` | Pre-fills the date (`YYYY-MM-DD`) |
| `minDate` | string (ISO) | `""` | Earliest selectable date |
| `maxDate` | string (ISO) | `""` | Latest selectable date |
| `rangeDate` | string (ISO) | `""` | Range-highlight anchor |
| `enableAnalytics` | bool | `false` | Toggle GA attributes |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Accessibility

- The `<label>` must associate with the input via `for=` matching the input's `id`. The documented variants additionally use `aria-labelledby` pointing at the label's `id` for redundancy with the generated DOM.
- The hint text should be referenced via `aria-describedby` so screen readers announce the expected format alongside the label.
- The calendar popup is exposed as a `dialog` with day cells as `gridcell`s (set automatically by USWDS JS). Keyboard support: arrow keys move day-by-day, Page Up/Down change month, Shift+Page Up/Down change year, Home/End jump to start/end of week, Enter selects, Escape closes.
- The calendar-icon button is `aria-haspopup="dialog"` with an accessible name "Toggle calendar" — applied by the JS, not hand-authored.
- For required fields, `required` belongs on the `<input>` so native HTML form validation triggers on submit.

## JS requirements

**Requires the `mdwds-core.js` bundle loaded** (which bundles the USWDS date-picker behavior). Without it: the calendar popup and icon button never render — only a plain `<input>` appears with no formatting help, no min/max enforcement, no keyboard date navigation. The user can still type a date as free text, but every interactive affordance is gone.

## Common mistakes

1. **Forgetting `mdwds-core.js`** — without it the component is an unstyled text input. The whole point of the picker (the calendar popup) doesn't exist.
2. **Using `MM/DD/YYYY` format in `data-default-value` / `data-min-date` / `data-max-date`** — the data attributes require ISO format (`YYYY-MM-DD`). Only the *visible* input text uses `MM/DD/YYYY`.
3. **Putting `required` on the wrapper `<div class="usa-date-picker">`** — it belongs on the inner `<input>`.
4. **Omitting `aria-describedby` linkage to the hint** — screen reader users miss the format hint.
5. **Hand-authoring `<button>` for the calendar icon** — the JS injects the toggle button; adding your own breaks layout.
6. **Setting `type="date"` on the input** — leave it as `type="text"` (the default). USWDS controls the parsing; `type="date"` triggers the native browser picker instead, defeating the component.
