# usa-memorable-date

The USWDS memorable date is a three-field date input — a month dropdown plus day and year text fields — sitting side-by-side under a single fieldset legend. Use it for dates the user *already knows* and types from memory: birthdate, employment start date, marriage date. **Do not** use it for picking an unknown date in the near future (use `usa-date-picker` for that — a calendar popup is more useful when browsing).

> Use this for memorable-date entry on Maryland.gov pages. There is no `maryland-memorable-date` — MDWDS inherits the USWDS component with Maryland color tokens. For a calendar-driven date selector see `usa-date-picker`.

## What it looks like

A `<fieldset>` with a top legend (the field name in semibold body-size text, e.g., "Date of birth") and optional hint underneath in small gray text (e.g., "For example: 4 28 1986"). Below the hint sit three controls in a single horizontal row at desktop, stacking on narrow mobile.

- **Month** — a small `<select>` dropdown (~5rem / 80px wide) with a "Month" label above it. Options are "01 - January" through "12 - December" plus a "-Select-" placeholder. Visually it's a standard USWDS select: white background, thin gray border, square corners, ~48px tall, caret on the right edge.
- **Day** — a small text input (~4rem / 64px wide) with a "Day" label above. `type="text"`, `maxlength="2"`, `pattern="[0-9]*"`, `inputmode="numeric"` — keeps the on-screen mobile keyboard numeric and the input narrow.
- **Year** — a slightly wider text input (~6rem / 96px wide) with a "Year" label above. Same numeric constraints with `minlength="4"` / `maxlength="4"`.

Each child sits in its own `usa-form-group` with a narrow-width modifier (`--month`, `--day`, `--year`) and has a small `usa-label` above it. Spacing between fields is ~16px.

In error state, the wrapping `usa-form-group--error` applies a 4px left border in red (`bg-error`), the legend turns red, an inline error message appears with `usa-error-message` (red text, alert role), and each child input gains an `usa-input--error` border. In success state, no visual change appears at the fieldset level — only individual inputs get `usa-input--success` (green left-border).

## Default markup

```html
<form class="usa-form usa-form--large">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">Date of birth</legend>
    <span class="usa-hint" id="dob-hint">For example: 4 28 1986</span>

    <div class="usa-memorable-date">
      <div class="usa-form-group usa-form-group--month usa-form-group--select">
        <label class="usa-label" for="dob-month">Month</label>
        <select
          class="usa-select"
          id="dob-month"
          name="date-of-birth-month"
          aria-describedby="dob-hint"
        >
          <option value="">-Select-</option>
          <option value="1">01 - January</option>
          <option value="2">02 - February</option>
          <option value="3">03 - March</option>
          <option value="4">04 - April</option>
          <option value="5">05 - May</option>
          <option value="6">06 - June</option>
          <option value="7">07 - July</option>
          <option value="8">08 - August</option>
          <option value="9">09 - September</option>
          <option value="10">10 - October</option>
          <option value="11">11 - November</option>
          <option value="12">12 - December</option>
        </select>
      </div>

      <div class="usa-form-group usa-form-group--day">
        <label class="usa-label" for="dob-day">Day</label>
        <input
          class="usa-input"
          id="dob-day"
          name="date-of-birth-day"
          type="text"
          maxlength="2"
          pattern="[0-9]*"
          inputmode="numeric"
          aria-describedby="dob-hint"
        />
      </div>

      <div class="usa-form-group usa-form-group--year">
        <label class="usa-label" for="dob-year">Year</label>
        <input
          class="usa-input"
          id="dob-year"
          name="date-of-birth-year"
          type="text"
          minlength="4"
          maxlength="4"
          pattern="[0-9]*"
          inputmode="numeric"
          aria-describedby="dob-hint"
        />
      </div>
    </div>
  </fieldset>
</form>
```

## Markup — required fields

```html
<form class="usa-form usa-form--large">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">License issue date</legend>
    <span class="usa-hint" id="issue-hint">As shown on the front of your Maryland driver's license.</span>

    <div class="usa-memorable-date">
      <div class="usa-form-group usa-form-group--month usa-form-group--select">
        <label class="usa-label" for="issue-month">Month</label>
        <select class="usa-select" id="issue-month" name="issue-month" required aria-describedby="issue-hint">
          <option value="">-Select-</option>
          <!-- months -->
        </select>
      </div>
      <div class="usa-form-group usa-form-group--day">
        <label class="usa-label" for="issue-day">Day</label>
        <input class="usa-input" id="issue-day" name="issue-day" type="text"
          maxlength="2" pattern="[0-9]*" inputmode="numeric" required aria-describedby="issue-hint" />
      </div>
      <div class="usa-form-group usa-form-group--year">
        <label class="usa-label" for="issue-year">Year</label>
        <input class="usa-input" id="issue-year" name="issue-year" type="text"
          minlength="4" maxlength="4" pattern="[0-9]*" inputmode="numeric" required aria-describedby="issue-hint" />
      </div>
    </div>
  </fieldset>
</form>
```

`required` goes on each child control.

## Markup — error state

```html
<form class="usa-form usa-form--large">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">Date of birth</legend>
    <span class="usa-hint" id="dob-hint">For example: 4 28 1986</span>
    <span class="usa-error-message" id="dob-error" role="alert">
      Please enter a valid date of birth. February 30 is not a valid date.
    </span>

    <div class="usa-memorable-date">
      <div class="usa-form-group usa-form-group--month usa-form-group--select">
        <label class="usa-label" for="dob-month">Month</label>
        <select class="usa-select" id="dob-month" name="dob-month" aria-describedby="dob-hint dob-error">
          <option value="">-Select-</option>
          <option value="2" selected>02 - February</option>
          <!-- … -->
        </select>
      </div>
      <div class="usa-form-group usa-form-group--day">
        <label class="usa-label" for="dob-day">Day</label>
        <input class="usa-input" id="dob-day" name="dob-day" type="text"
          maxlength="2" pattern="[0-9]*" inputmode="numeric"
          value="30" aria-describedby="dob-hint dob-error" />
      </div>
      <div class="usa-form-group usa-form-group--year">
        <label class="usa-label" for="dob-year">Year</label>
        <input class="usa-input" id="dob-year" name="dob-year" type="text"
          minlength="4" maxlength="4" pattern="[0-9]*" inputmode="numeric"
          value="1986" aria-describedby="dob-hint dob-error" />
      </div>
    </div>
  </fieldset>
</form>
```

The `usa-error-message` is a single message scoped to the whole fieldset, not per-field. `aria-describedby` on each child references both the hint and the error message.

## What each class does

| Class | Effect |
|---|---|
| `usa-form` | Form wrapper. Constrains form width and spacing. |
| `usa-form--large` | Wider variant of `usa-form` (~30rem). Used here so the three fields fit comfortably side-by-side. |
| `usa-fieldset` | Resets browser `<fieldset>` styling: no border, zero padding, block layout. |
| `usa-legend` | The fieldset title. ~16px semibold body text, color `base-darkest`. |
| `usa-hint` | Small gray helper text (~14px) below the legend. |
| `usa-error-message` | Red inline error text (~14px semibold, color `error`) below the legend. `role="alert"` triggers screen-reader announcement. |
| `usa-memorable-date` | Flex container for the three child form-groups. Lays them out in a row at desktop with ~16px gap; stacks vertically on narrow mobile. |
| `usa-form-group` | Single labeled control wrapper. |
| `usa-form-group--month` | Constrains the month dropdown's width (~5rem). |
| `usa-form-group--day` | Constrains the day input's width (~4rem). |
| `usa-form-group--year` | Constrains the year input's width (~6rem). |
| `usa-form-group--select` | Applied alongside `--month` to flag the field as a `<select>`. |
| `usa-form-group--error` | Adds the red left border + spacing for the error state (apply on the parent of an errored field if showing per-field errors). |
| `usa-label` | Small label above each child (`Month`, `Day`, `Year`). Same styling as elsewhere — ~16px semibold. |
| `usa-select` | Native `<select>` styled: white, thin gray border, square corners, caret on the right edge. |
| `usa-input` | Text input styling: ~48px tall, white, thin gray border. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `label` | string | `"Date of birth"` | Legend text |
| `hintText` | string | `"For example: 4 28 1986"` | Hint below the legend |
| `required` | bool | `false` | Applies `required` to all three fields |
| `disabled` | bool | `false` | Disables all three fields |
| `errorMessage` | string | `""` | If set, renders an `usa-error-message` and links via `aria-describedby` |
| `monthValue` | string | `""` | Pre-selected month (1–12) |
| `dayValue` | string | `""` | Pre-filled day (1–31) |
| `yearValue` | string | `""` | Pre-filled year (4 digits) |
| `enableAnalytics` | bool | `false` | Toggle GA attributes (set on the `<fieldset>`) |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Accessibility

- The `<fieldset>` groups the three controls as one logical date field; the `<legend>` provides the accessible name for the whole group ("Date of birth").
- Each child has its own `<label>` (`Month`, `Day`, `Year`) associated by `for=`/`id`, so screen readers announce both the group name and the field role.
- The hint and (when present) error message are referenced from every child's `aria-describedby` so the context is announced regardless of which field has focus.
- `inputmode="numeric"` and `pattern="[0-9]*"` give mobile users a numeric on-screen keyboard and block non-digit input.
- `maxlength`/`minlength` limit input length client-side; server-side validation should still enforce a valid calendar date.
- `role="alert"` on the error message causes screen readers to announce changes when the message appears after submission.

## JS requirements

No JS required. Memorable date is three native form controls inside a fieldset — works fully with or without `mdwds-core.js` loaded. (You will still want the CDN CSS for styling.)

## Common mistakes

1. **Sending three separate form fields without a `<fieldset>`/`<legend>`** — loses the grouping semantics. Screen readers won't announce "Date of birth" as the group name when focus moves to "Day".
2. **Using `type="number"` on day/year** — `type="number"` strips leading zeros, allows scrolling/incrementing, and produces inconsistent mobile keyboards. Stick with `type="text"` + `inputmode="numeric"` + `pattern="[0-9]*"`.
3. **Reaching for `usa-date-picker` when the user already knows the date** — the calendar popup is wasted UI for a birthdate. Memorable date is faster.
4. **Omitting `aria-describedby` linkage to the hint or error** — screen reader users miss the format example and the validation feedback.
5. **Putting the error message inside one of the three child `usa-form-group`s** — the error belongs at the fieldset level, after the legend/hint, so all three controls reference it via `aria-describedby`.
6. **Not validating the calendar combination server-side** — client-side `maxlength` doesn't catch "February 30". Always re-check the assembled date on the server.
7. **Omitting `inputmode="numeric"`** — mobile users get the full alphabetic keyboard, which is slower and error-prone for digits.
