# usa-combo-box

The USWDS combo box is an enhanced `<select>` that pairs a text input with a filterable list. The user can type to narrow long option lists, use arrow keys to highlight, and press enter to select. Use it for any dropdown with more than ~10 options on a Maryland.gov page.

> Use this for searchable dropdowns on Maryland.gov pages. There is no `maryland-combo-box` — MDWDS inherits the USWDS combo-box with Maryland color tokens applied automatically. For short, fixed lists (≤10 options, no search needed) use `usa-select` instead.

## What it looks like

When closed, the combo box looks like a standard text input: a single-line white field with a thin gray border, square corners, ~48px tall, body text inside in `text-base-darkest`. At the right edge sit two small icon buttons inside the input frame — a circular "X" clear button (appears only once a value is selected) and a caret/chevron toggle that opens the list.

When opened (by click, arrow-down, or typing), a white list panel drops down beneath the input, attached to the same border-color frame. Each option is one row of body-size text, left-aligned, with vertical padding ~8px. Hover or keyboard-focus highlights a row with the Maryland blue tint (`bg-primary-lighter`) and switches the row text to a darker blue. The selected option (after click or Enter) shows the same bold/highlighted treatment.

As the user types, the list filters in place. If no options match, the panel shows a single italic "No results found" row. The "X" clear button, when pressed, empties the input and re-shows the full list.

A `data-default-value` attribute pre-selects an option on page load. The disabled state shows the input grayed-out (`bg-disabled-lighter`) with a not-allowed cursor.

## Default markup

```html
<form class="usa-form">
  <label class="usa-label" for="park-select">Select a state park</label>
  <div class="usa-combo-box">
    <select id="park-select" name="park" class="usa-select">
      <option value="">Select a park</option>
      <option value="assateague">Assateague State Park</option>
      <option value="deep-creek">Deep Creek Lake State Park</option>
      <option value="patapsco-valley">Patapsco Valley State Park</option>
      <option value="rocky-gap">Rocky Gap State Park</option>
      <option value="sandy-point">Sandy Point State Park</option>
      <option value="susquehanna">Susquehanna State Park</option>
    </select>
  </div>
</form>
```

The USWDS JavaScript transforms this `<select>` at runtime into an input + listbox combo box. The original `<select>` is hidden but kept in the DOM so its value still submits with the form.

## Markup — with a pre-selected default value

```html
<form class="usa-form">
  <label class="usa-label" for="county-select">Select your county</label>
  <div class="usa-combo-box" data-default-value="anne-arundel">
    <select id="county-select" name="county" class="usa-select">
      <option value="">Select a county</option>
      <option value="allegany">Allegany</option>
      <option value="anne-arundel">Anne Arundel</option>
      <option value="baltimore">Baltimore</option>
      <option value="baltimore-city">Baltimore City</option>
      <option value="calvert">Calvert</option>
      <!-- additional Maryland counties -->
    </select>
  </div>
</form>
```

The `data-default-value` attribute on the wrapper matches an `<option>` value and pre-selects it on init.

## Markup — required field

```html
<form class="usa-form">
  <label class="usa-label" for="agency-select">Filing agency</label>
  <div class="usa-combo-box">
    <select id="agency-select" name="agency" class="usa-select" required>
      <option value="">Select an agency</option>
      <option value="mdot">Maryland Department of Transportation</option>
      <option value="mva">Motor Vehicle Administration</option>
      <option value="dnr">Department of Natural Resources</option>
      <option value="mde">Department of the Environment</option>
    </select>
  </div>
</form>
```

`required` is applied to the inner `<select>`, not the wrapper.

## Markup — disabled

```html
<form class="usa-form">
  <label class="usa-label" for="locked-select">Locked selection</label>
  <div class="usa-combo-box" data-default-value="md">
    <select id="locked-select" name="state" class="usa-select" disabled>
      <option value="">Select a state</option>
      <option value="md">Maryland</option>
      <option value="va">Virginia</option>
      <option value="de">Delaware</option>
    </select>
  </div>
</form>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-form` | Form wrapper. Constrains form width (default ~24rem) and applies vertical spacing between fields. |
| `usa-label` | Block label above the field. ~16px semibold, color `base-darkest`, ~8px bottom margin. |
| `usa-combo-box` | Wrapper element. Once JS runs, this becomes a relative-positioned container holding the generated input, listbox, toggle button, and clear button. Establishes the dropdown anchor. |
| `usa-select` | Class on the inner `<select>`. Visible only as a fallback when JS hasn't loaded; replaced by a text input at runtime. |
| `usa-combo-box__input` | (Generated at runtime.) The text input the user actually sees. White background, ~48px tall, thin gray border, square corners. |
| `usa-combo-box__toggle-list` | (Generated at runtime.) Caret/chevron button at the right edge of the input that opens/closes the list. |
| `usa-combo-box__clear-input` | (Generated at runtime.) "X" button that appears only when a value is selected. Resets the field. |
| `usa-combo-box__list` | (Generated at runtime.) The dropdown `<ul>` of options. White background, same border color as the input, drops below with no visible gap. |
| `usa-combo-box__list-option` | (Generated at runtime.) Each option row. Hover/focus highlights with `bg-primary-lighter`. |
| `usa-combo-box__list-option--focused` | Highlighted row during keyboard navigation. |
| `usa-combo-box__list-option--selected` | Currently-selected option (after enter/click). Persistent bold/highlight treatment. |
| `usa-combo-box__list-option--no-results` | Italic gray "No results found" row shown when the filter matches nothing. |
| `data-default-value` (attr) | On the `usa-combo-box` wrapper. Value matches an option `value` to pre-select on init. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `label` | string | `"Select a fruit"` | Visible label text |
| `id` | string | auto | Inner `<select>` id |
| `name` | string | derived from label | Form submission name |
| `placeholder` | string | `"Select a fruit"` | Text of the empty-value first `<option>` |
| `options` | array | demo data | `[{ label, value, selected?, disabled? }]` |
| `required` | bool | `false` | Adds `required` to `<select>` |
| `disabled` | bool | `false` | Adds `disabled` to `<select>` |
| `defaultValue` | string | `""` | Pre-selected option value; sets `data-default-value` on wrapper |
| `ariaLabel` | string | `""` | ARIA label on the `<select>` (use only if visible label is hidden) |
| `ariaDescribedBy` | string | `""` | ID of a separate description element |
| `enableAnalytics` | bool | `false` | Toggles GA data attributes |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Accessibility

- The `<label>` must use `for="..."` matching the `<select>` id. The combo box's generated input inherits that label association.
- The combo box exposes itself with `role="combobox"`, `aria-expanded`, `aria-controls` pointing at the generated listbox, and `aria-activedescendant` for the currently highlighted option — all applied automatically by the USWDS JS. Do not hand-author them on the markup.
- Keyboard support (provided by the JS): Tab focuses the input; ArrowDown opens the list and moves to the next option; ArrowUp moves to the previous; Enter selects; Escape closes without changing the selection; Home/End jump to first/last; typing filters.
- For required fields, the `required` attribute belongs on the inner `<select>` so native form validation still triggers.
- Use `aria-describedby` to associate hint text below the label.

## JS requirements

**Requires the `mdwds-core.js` bundle loaded** (which bundles the USWDS combo-box behavior). Without it: the combo box renders as a plain native `<select>` dropdown — no type-ahead, no filtering, no clear button, no styled listbox. Form submission still works because the `<select>` is the actual form control, but users lose the search interaction the component exists to provide.

## Common mistakes

1. **Forgetting `mdwds-core.js`** — without the JS bundle the component is just a native `<select>`. The "combo-box" appearance and behavior never activate.
2. **Putting `required` or `disabled` on the wrapper `<div class="usa-combo-box">`** — those attributes belong on the inner `<select>`. The wrapper isn't a form control.
3. **Hand-writing `role="combobox"` / `aria-expanded` / `aria-controls`** — USWDS JS adds and toggles these. Manually setting them will conflict.
4. **Replacing the `<select>` with a custom listbox** — the `<select>` is the actual form control and must remain in the DOM. The component only swaps the visible UI.
5. **Setting `data-default-value` to an option *label* instead of *value*** — it must match an `<option value="...">`.
6. **Using `usa-combo-box` for short lists** — under ~10 options, a plain `usa-select` is simpler and doesn't need JS.
