# usa-time-picker

The USWDS time picker is a combo-box-style dropdown for times of day. The user can type a time directly (e.g. "2:30 pm" or "14:30") or click to open a dropdown listing every step within the allowed range. Use it for appointment scheduling, meeting times, business-hour selection.

> Use this for time-of-day selection on Maryland.gov pages. There is no `maryland-time-picker` — MDWDS inherits the USWDS component with Maryland color tokens. For a date plus a time, pair this with `usa-date-picker` (or `usa-date-range-picker` if a range is needed).

## What it looks like

The closed control is a single-line text input (`usa-input` styling: ~48px tall, white, thin gray border, square corners) with a caret/chevron toggle inside the right edge — visually almost identical to `usa-combo-box`. There is no separate calendar-style button.

When the user types or focuses the input and presses arrow-down, a white listbox drops below, anchored to the input's bottom border. Each row is one time formatted in user-locale 12-hour form (e.g., "8:00am", "8:30am", "9:00am"…) — body-size text, left-aligned, ~8px vertical padding. The list scrolls if the range produces too many rows to display at once.

Hover or keyboard-focus highlights a row with `bg-primary-lighter` (light Maryland blue) and switches its text to a darker blue. The selected option after click or Enter is bold and tinted. Typing filters the list in real time: "2" narrows to times starting with 2, "2:3" narrows further. If nothing matches, a single italic "No results found" row appears.

The step interval (`data-step`, default 30 minutes) determines spacing. With `data-step="15"` the list shows 4 times per hour; with `data-step="60"`, one per hour. `data-min-time` and `data-max-time` constrain the range — outside those bounds, no rows are generated.

The value submitted with the form is the text in the input (typically in the locale-formatted "9:00am" form). The input does not use `type="time"`; it stays `type="text"` and USWDS controls parsing.

## Default markup

```html
<div class="usa-form-group">
  <label class="usa-label" id="appt-time-label" for="appt-time">Appointment time</label>
  <div class="usa-hint" id="appt-time-hint">Select a time from the dropdown. Type to filter options.</div>
  <div class="usa-time-picker" data-step="30">
    <input
      class="usa-input"
      id="appt-time"
      name="appointment-time"
      type="text"
      aria-describedby="appt-time-hint"
    />
  </div>
</div>
```

## Markup — with default value

```html
<div class="usa-form-group">
  <label class="usa-label" id="meeting-label" for="meeting-time">Meeting start time</label>
  <div class="usa-hint" id="meeting-hint">Choose a 15-minute slot.</div>
  <div class="usa-time-picker" data-step="15">
    <input
      class="usa-input"
      id="meeting-time"
      name="meeting-time"
      type="text"
      value="14:30"
      aria-describedby="meeting-hint"
    />
  </div>
</div>
```

The `value="14:30"` is a 24-hour string; the user-facing display becomes "2:30pm" once the JS initializes.

## Markup — business hours with 15-minute steps

```html
<div class="usa-form-group">
  <label class="usa-label" id="dmv-label" for="dmv-time">MVA appointment time</label>
  <div class="usa-hint" id="dmv-hint">Available 8:00 AM to 5:00 PM, 15-minute slots.</div>
  <div
    class="usa-time-picker"
    data-step="15"
    data-min-time="08:00"
    data-max-time="17:00"
  >
    <input
      class="usa-input"
      id="dmv-time"
      name="dmv-time"
      type="text"
      aria-describedby="dmv-hint"
      required
    />
  </div>
</div>
```

`data-min-time` and `data-max-time` use 24-hour `HH:MM` format.

## Markup — hourly intervals

```html
<div class="usa-form-group">
  <label class="usa-label" id="bus-label" for="bus-time">Departure hour</label>
  <div class="usa-hint" id="bus-hint">MDOT shuttles depart on the hour.</div>
  <div
    class="usa-time-picker"
    data-step="60"
    data-min-time="06:00"
    data-max-time="22:00"
  >
    <input
      class="usa-input"
      id="bus-time"
      name="bus-time"
      type="text"
      aria-describedby="bus-hint"
    />
  </div>
</div>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-form-group` | Per-field vertical container. ~24px bottom margin. |
| `usa-label` | Block label above the input. ~16px semibold, color `base-darkest`. |
| `usa-hint` | Small gray helper text (~14px) below the label. |
| `usa-time-picker` | Wrapper around the `<input>`. After JS init, becomes the combo-box-style anchor: input plus generated listbox and toggle. |
| `usa-input` | Text input styling: ~48px tall, white, thin gray border, square corners. |
| `usa-time-picker__list` | (Generated at runtime.) The dropdown `<ul>` of time options. Inherits combo-box list styling. |
| `usa-time-picker__list-option` | (Generated at runtime.) Each time row. Hover/focus → `bg-primary-lighter`. |
| `data-step` (attr) | Minutes between options. Common values: 15, 30, 60. |
| `data-min-time` (attr) | Earliest time in 24-hour `HH:MM`. |
| `data-max-time` (attr) | Latest time in 24-hour `HH:MM`. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `label` | string | `"Appointment time"` | Visible label |
| `hintText` | string | `"Select a time…"` | Hint shown above the input |
| `name` | string | derived | Form field name |
| `required` | bool | `false` | Adds `required` to the input |
| `disabled` | bool | `false` | Disables input and toggle |
| `defaultValue` | string (24h) | `""` | Pre-filled time, e.g. `"14:30"` |
| `minTime` | string (24h) | `""` | Earliest selectable, e.g. `"09:00"` |
| `maxTime` | string (24h) | `""` | Latest selectable, e.g. `"17:00"` |
| `step` | number | `30` | Minutes between options |
| `enableAnalytics` | bool | `false` | Toggle GA attributes |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Accessibility

- The `<label>` must associate with the input via `for=`/`id`. The hint should be referenced via `aria-describedby`.
- USWDS JS gives the input combo-box semantics at runtime: `role="combobox"`, `aria-expanded`, `aria-controls`, `aria-activedescendant` — do not author these manually.
- Keyboard support: ArrowDown opens the list and focuses the next time; ArrowUp opens and focuses the previous; Enter selects; Escape closes; typing filters; Home/End jump to the first/last visible option.
- For required fields, put `required` on the `<input>` so native form validation triggers.
- The input remains `type="text"` for accessibility and consistency across browsers — using `type="time"` would invoke a native picker that bypasses the component.

## JS requirements

**Requires the `mdwds-core.js` bundle loaded** (which bundles the USWDS time-picker behavior). Without it: only the bare `<input>` is visible. No dropdown list opens, no step intervals appear, no min/max constraint is enforced, and no formatting happens. Users can type free text and submit anything.

## Common mistakes

1. **Forgetting `mdwds-core.js`** — the picker is inert without it. You get a plain text input.
2. **Using `type="time"` on the input** — that triggers the browser's native time picker and bypasses USWDS entirely. Leave it `type="text"`.
3. **Putting times in 12-hour format in `data-min-time` / `data-max-time` / `data-step`** — the data attributes are 24-hour `HH:MM`. The list *displays* 12-hour locale text but is configured in 24-hour.
4. **Setting `data-step` to a non-divisor of 60** (e.g., 7 or 11) — produces an odd time list. Stick to 15, 20, 30, or 60.
5. **Forgetting `aria-describedby` to link the hint** — screen readers don't announce the available range.
6. **Putting `required` on the wrapper instead of the input** — `required` belongs on the `<input>`.
