# usa-date-range-picker

The USWDS date range picker is two coordinated `usa-date-picker` instances — a start date and an end date — wired so the end calendar disallows dates before the start. Use it for from-to selections: event scheduling, vacation booking, application date windows.

> Use this for date-range selection on Maryland.gov pages. There is no `maryland-date-range-picker` — MDWDS inherits the USWDS component with Maryland color tokens. For a single date, use `usa-date-picker`. For a memorable-date pair (e.g., employment start/end years) consider two `usa-memorable-date` fields side-by-side instead.

## What it looks like

Two `usa-date-picker` controls stacked vertically (start above end), each with its own label and hint, each rendered exactly like a standalone date picker (text input + Maryland-blue calendar-icon button). Each calendar opens below its own input.

The coordination is invisible until you interact with both:

- After picking a start date, the end calendar marks all dates **before** the start as disabled (muted gray, strikethrough cursor) and visually highlights the span from the start date to the hovered/focused day in light Maryland blue (`bg-primary-lighter`) so the user previews the range as they hover.
- Picking an end date earlier than the start is blocked.
- The outer wrapper's `data-min-date` and `data-max-date` constrain *both* pickers to a shared overall window (e.g., "anytime in calendar year 2026").
- A `data-range-date` is set internally on each picker as the user makes selections — agents do not author it manually.

Otherwise, layout, focus rings, calendar visuals, and keyboard navigation match `usa-date-picker` exactly.

## Default markup

```html
<div class="usa-date-range-picker">
  <div class="usa-form-group">
    <label class="usa-label" id="start-label" for="start-date">Event start date</label>
    <div class="usa-hint" id="start-hint">mm/dd/yyyy</div>
    <div class="usa-date-picker">
      <input
        class="usa-input"
        id="start-date"
        name="event-date-start"
        aria-labelledby="start-label"
        aria-describedby="start-hint"
      />
    </div>
  </div>

  <div class="usa-form-group">
    <label class="usa-label" id="end-label" for="end-date">Event end date</label>
    <div class="usa-hint" id="end-hint">mm/dd/yyyy</div>
    <div class="usa-date-picker">
      <input
        class="usa-input"
        id="end-date"
        name="event-date-end"
        aria-labelledby="end-label"
        aria-describedby="end-hint"
      />
    </div>
  </div>
</div>
```

The wrapper `<div class="usa-date-range-picker">` is what tells USWDS JS to link the two pickers together. Without it, you get two independent date pickers.

## Markup — with default values

```html
<div class="usa-date-range-picker">
  <div class="usa-form-group">
    <label class="usa-label" id="checkin-label" for="checkin-date">Check-in date</label>
    <div class="usa-hint" id="checkin-hint">mm/dd/yyyy</div>
    <div class="usa-date-picker" data-default-value="2026-07-04">
      <input class="usa-input" id="checkin-date" name="check-in"
        aria-labelledby="checkin-label" aria-describedby="checkin-hint" />
    </div>
  </div>
  <div class="usa-form-group">
    <label class="usa-label" id="checkout-label" for="checkout-date">Check-out date</label>
    <div class="usa-hint" id="checkout-hint">mm/dd/yyyy</div>
    <div class="usa-date-picker" data-default-value="2026-07-10">
      <input class="usa-input" id="checkout-date" name="check-out"
        aria-labelledby="checkout-label" aria-describedby="checkout-hint" />
    </div>
  </div>
</div>
```

`data-default-value` belongs on each inner `usa-date-picker`, not the outer wrapper.

## Markup — overall min/max constraint

```html
<div
  class="usa-date-range-picker"
  data-min-date="2026-01-01"
  data-max-date="2026-12-31"
>
  <div class="usa-form-group">
    <label class="usa-label" id="permit-start-label" for="permit-start">Permit valid from</label>
    <div class="usa-hint" id="permit-start-hint">mm/dd/yyyy</div>
    <div class="usa-date-picker">
      <input class="usa-input" id="permit-start" name="permit-start"
        aria-labelledby="permit-start-label" aria-describedby="permit-start-hint" required />
    </div>
  </div>
  <div class="usa-form-group">
    <label class="usa-label" id="permit-end-label" for="permit-end">Permit valid through</label>
    <div class="usa-hint" id="permit-end-hint">mm/dd/yyyy</div>
    <div class="usa-date-picker">
      <input class="usa-input" id="permit-end" name="permit-end"
        aria-labelledby="permit-end-label" aria-describedby="permit-end-hint" required />
    </div>
  </div>
</div>
```

`data-min-date` / `data-max-date` on the **outer** wrapper apply to both pickers.

## What each class does

| Class | Effect |
|---|---|
| `usa-date-range-picker` | Outer wrapper. Tells USWDS JS to coordinate the two inner pickers (end disallows < start, start disallows > end). No visual effect on its own — it's a marker class. |
| `usa-form-group` | Per-field container. Vertical spacing between fields. Used twice, once for start and once for end. |
| `usa-label`, `usa-hint`, `usa-date-picker`, `usa-input` | See `usa-date-picker.md` — every class here has the same effect inside each inner picker. |
| `data-min-date` (attr on wrapper) | Earliest date allowed in **either** picker (ISO format). |
| `data-max-date` (attr on wrapper) | Latest date allowed in **either** picker. |
| `data-default-value` (attr on inner `usa-date-picker`) | Pre-fills that picker only. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `startLabel` | string | `"Event start date"` | Label for the first picker |
| `endLabel` | string | `"Event end date"` | Label for the second picker |
| `hintText` | string | `"mm/dd/yyyy"` | Shown above each input |
| `startName` | string | `"event-date-start"` | Form field name for start |
| `endName` | string | `"event-date-end"` | Form field name for end |
| `required` | bool | `false` | Applies `required` to both inputs |
| `disabled` | bool | `false` | Disables both inputs |
| `startDefaultValue` | string (ISO) | `""` | Pre-fill start (`YYYY-MM-DD`) |
| `endDefaultValue` | string (ISO) | `""` | Pre-fill end |
| `minDate` | string (ISO) | `""` | Overall earliest date (on wrapper) |
| `maxDate` | string (ISO) | `""` | Overall latest date (on wrapper) |
| `enableAnalytics` | bool | `false` | Toggle GA attributes (set on wrapper) |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Accessibility

- Each picker has its own `<label>` associated by `for=`/`id` pair, and its own hint via `aria-describedby`. Treat them as two independent labeled fields.
- The cross-picker constraint (end ≥ start) is communicated visually by disabling out-of-range cells in the end calendar. Screen-reader users see disabled `gridcell`s via the underlying date-picker semantics.
- If both fields are required, set `required` on both `<input>`s so native form validation catches each.
- Provide clear labels — "Event start date" / "Event end date", "Check-in" / "Check-out" — so the two roles are distinguishable without sighted context.
- Keyboard navigation matches `usa-date-picker`: arrows move days, Page Up/Down change month, Escape closes the popup.

## JS requirements

**Requires the `mdwds-core.js` bundle loaded** (which bundles both the USWDS date-picker and date-range-picker behaviors). Without it: each `usa-date-picker` falls back to a plain text input with no calendar popup, and — critically — the cross-field coordination doesn't exist. The end input will not prevent a date before the start, and no range-highlighting appears on hover.

## Common mistakes

1. **Forgetting `mdwds-core.js`** — without it, the two date pickers don't render their calendars and don't coordinate. Users can submit nonsense (e.g., end before start).
2. **Putting `data-min-date` / `data-max-date` on the inner pickers instead of the wrapper** — placing them on the wrapper applies the constraint to both. Placing them on one inner picker doesn't.
3. **Using `MM/DD/YYYY` in data attributes** — all `data-*-date` values are ISO (`YYYY-MM-DD`). Only the visible input text shows `MM/DD/YYYY`.
4. **Omitting the outer `usa-date-range-picker` wrapper** — without it you get two independent pickers and no end-after-start enforcement.
5. **Sharing one `<label>` across both pickers** — every input needs its own associated label.
6. **Reusing the same `id`** for both inputs — IDs must be unique; the JS uses them to wire the two pickers together.
