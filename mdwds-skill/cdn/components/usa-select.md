# usa-select

The USWDS native `<select>` dropdown — styled to match the rest of the form controls. Used when the user picks **one** option from a short, finite list (state, county, agency, service type, language). For long lists where filtering helps, use `usa-combo-box` instead. For very short lists where you want all options visible at once, use `usa-radio`.

Use this for native dropdowns on Maryland.gov pages; the CDN themes USWDS form colors to Maryland blue (focus ring, error border).

## What it looks like

A `usa-select` is a 40px-tall (`units(5)`) rectangular dropdown with a **1px solid `base-dark` (cool gray) border**, no border-radius (square corners), white background, and `color: ink` (near-black) text. Internal padding is 8px on the left/top/bottom; the **right padding is 32px** (`units(4)`) to leave room for the chevron icon. At the right edge sits a downward-pointing chevron (USWDS `unfold_more` icon SVG, 20×20px / `units(2.5)`) positioned with `right: 8px` (`units(1)`) center-vertical. The chevron is part of the background image (CSS), not an HTML element — `appearance: none` removes the browser's native dropdown arrow.

When the user clicks the field, the browser's native option list opens (matches the OS — looks different on macOS, Windows, iOS, Android, but always functional). The triggering field itself remains the styled 40px box.

Inside `<form class="usa-form">`, the per-select max-width (`units("mobile-lg")` = 480px) is cleared so the form's max-width governs.

`select[multiple]` (a multi-select list) gets `height: auto` and **drops the chevron** — the field expands to show several options at once (a list-box visual). This is rarely used on Maryland.gov; prefer checkboxes for multi-select.

The placeholder option — `<option value="">- Select -</option>` — is the first option and has no value, so the form won't submit a meaningless selection. Pair with `required` on the `<select>` to force the user to choose a real value.

Focus, disabled, and error states match the other form controls (Maryland-blue focus ring, disabled gray, error red border via the surrounding `usa-form-group--error`).

## Variants

The select has no built-in visual variant classes. Variation comes from:

- The `<option selected>` attribute to pre-select an option.
- The `<option disabled>` attribute to disable a single option.
- The `multiple` attribute on `<select>` (rare — list-box view, no chevron).
- The wrapping `<form class="usa-form">` / `usa-form--large` for max-width.
- Wrap in `usa-form-group--error` for the error state styling.

## When to use which pattern

- **Default `<select>` with placeholder + `required`** → User must pick exactly one option from a finite list (5–25 options). Maryland county, state agency, language preference.
- **`usa-combo-box`** (separate component) → Long lists (50+) where typing-to-filter helps.
- **`usa-radio` instead** → Short lists (2–5) where seeing all options matters more than saving space.
- **`<select multiple>`** → Rare. Prefer checkboxes — multi-select dropdowns are confusing on touch devices.

## Default markup

```html
<form class="usa-form">
  <label class="usa-label" for="agency">Maryland agency</label>
  <select class="usa-select" id="agency" name="agency" required>
    <option value="">- Select -</option>
    <option value="dnr">Department of Natural Resources</option>
    <option value="mdot">Department of Transportation</option>
    <option value="mdh">Department of Health</option>
    <option value="mva">Motor Vehicle Administration</option>
    <option value="mde">Department of the Environment</option>
    <option value="dllr">Department of Labor, Licensing &amp; Regulation</option>
  </select>
</form>
```

## Markup — county selector

```html
<form class="usa-form">
  <label class="usa-label" for="county">Maryland county</label>
  <div class="usa-hint" id="county-hint">Where you live or where the service is requested</div>
  <select
    class="usa-select"
    id="county"
    name="county"
    aria-describedby="county-hint"
    required
  >
    <option value="">- Select a county -</option>
    <option value="allegany">Allegany</option>
    <option value="anne-arundel">Anne Arundel</option>
    <option value="baltimore-city">Baltimore City</option>
    <option value="baltimore-county">Baltimore County</option>
    <option value="calvert">Calvert</option>
    <option value="caroline">Caroline</option>
    <option value="carroll">Carroll</option>
    <option value="cecil">Cecil</option>
    <option value="charles">Charles</option>
    <option value="dorchester">Dorchester</option>
    <option value="frederick">Frederick</option>
    <option value="garrett">Garrett</option>
    <option value="harford">Harford</option>
    <option value="howard">Howard</option>
    <option value="kent">Kent</option>
    <option value="montgomery">Montgomery</option>
    <option value="prince-georges">Prince George's</option>
    <option value="queen-annes">Queen Anne's</option>
    <option value="somerset">Somerset</option>
    <option value="st-marys">St. Mary's</option>
    <option value="talbot">Talbot</option>
    <option value="washington">Washington</option>
    <option value="wicomico">Wicomico</option>
    <option value="worcester">Worcester</option>
  </select>
</form>
```

## Markup — with a default selection and a disabled option

```html
<form class="usa-form">
  <label class="usa-label" for="license-type">License type</label>
  <select class="usa-select" id="license-type" name="license-type" required>
    <option value="">- Select -</option>
    <option value="resident-fishing" selected>Resident fishing license</option>
    <option value="non-resident-fishing">Non-resident fishing license</option>
    <option value="hunting">Hunting license</option>
    <option value="trapping" disabled>Trapping license (currently unavailable)</option>
  </select>
</form>
```

## Markup — with error

```html
<form class="usa-form">
  <div class="usa-form-group usa-form-group--error">
    <label class="usa-label usa-label--error" for="service">Service requested</label>
    <span class="usa-error-message" id="service-err" role="alert">
      Choose a service to continue
    </span>
    <select
      class="usa-select"
      id="service"
      name="service"
      aria-describedby="service-err"
      aria-invalid="true"
      required
    >
      <option value="">- Select -</option>
      <option value="renew">Renew driver's license</option>
      <option value="title">Title and registration</option>
      <option value="id-card">Maryland ID card</option>
    </select>
  </div>
</form>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-select` | Base styles: 40px tall (`units(5)`), 1px solid `base-dark` border, square corners, white background, `color: ink` text. `padding-right: 32px` (`units(4)`) to clear the chevron, 8px padding on the other sides. Sets `appearance: none` to suppress the browser's native arrow and adds the USWDS `unfold_more` chevron SVG as a background image at `right: 8px` center, 20×20px. Disabled state: `disabled-lighter` background, `disabled-dark` text. `select[multiple]` removes the chevron and lets the box auto-size. Forced-colors (Windows high-contrast) restores the native listbox appearance for accessibility. |
| `usa-label` | Source Sans Pro at body size, color base-darkest, `margin-top: 24px`. Sits 8px above the select. |
| `usa-label--error` | Bold, `margin-top: 0`. |
| `usa-hint` | Helper text below the label, color `base`. Link via `aria-describedby`. |
| `usa-error-message` | Bold red message, `padding-y: 4px`, use `role="alert"` for dynamic insertion. |
| `usa-form-group` | Wrapper for label + hint + select + error. `margin-top: 24px`. |
| `usa-form-group--error` | 4px red left border, `padding-left: 16px`, left-shift on desktop to align the border with the form edge. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `label` | string | `"Dropdown label"` | Visible label text |
| `id` | string | `"options"` | Select id, matches label's `for` |
| `name` | string | `"options"` | Form submission key |
| `placeholder` | string | `"- Select -"` | First option text (with empty `value`) |
| `options` | array of `{label, value, selected?, disabled?}` | 3 sample options | Real options |
| `ariaDescribedBy` | string | `""` | ID of a hint or error |
| `enableAnalytics` | bool | `false` | Add `data-ga-*` attributes |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Accessibility

- **Always pair with `<label class="usa-label" for="ID">`.** A bare select is unnameable to screen readers.
- **Use a placeholder option with an empty `value`:** `<option value="">- Select -</option>` as the first option. Combined with `required` on the select, the form won't submit until the user picks a real value.
- **`required` attribute** on the `<select>` triggers the browser's "Please select an item in the list" validation message and is announced by screen readers.
- **Hints and errors:** wire via `aria-describedby` exactly as with other inputs. Use `aria-invalid="true"` on the select when in error state.
- **Avoid `<select multiple>` for accessibility:** Ctrl/Cmd-click is invisible to most users and very hard on mobile and assistive tech. Use checkboxes for multi-select.
- **Keep option labels short and scannable** — long options wrap to ellipsis (`text-overflow: ellipsis`), hiding part of the text. If options are long, use `usa-radio` or `usa-combo-box`.
- **Group related options** with `<optgroup label="...">` when you have 15+ items; screen readers announce the group label before reading options inside.

## JS requirements

No JS required — `<select>` is a native HTML form control styled by the CDN stylesheet. The browser handles the open/close, keyboard navigation (arrow keys, type-to-find), and form submission.

For a searchable, filterable dropdown with autocomplete, see `usa-combo-box` — that requires the USWDS JS bundle.

## Common mistakes

1. **No placeholder option, so the first real option is auto-selected.** Users may submit without noticing — silent wrong data. Always have `<option value="">- Select -</option>` as the first option, plus `required` on the select.
2. **`for`/`id` mismatch** between label and select. Click-to-focus and screen-reader association break.
3. **Missing `name` attribute** — the selected value won't submit.
4. **Using a select for 2–4 options.** Radio buttons (with all options visible) are easier to scan and click. Reserve selects for lists of 5+ where vertical space matters.
5. **Using a select for 50+ options.** Native selects don't filter; the user must scroll. Use `usa-combo-box` instead.
6. **`<select multiple>` on a public form.** Confusing on touch, invisible affordance for keyboard, terrible on assistive tech. Use checkboxes.
7. **Inline `<style>` to change the chevron color or hide it.** The chevron is a CSS background image positioned by the CDN. Don't override; if you need a different control, use the right component.
8. **Forgetting `aria-describedby` to link hint or error text.** Sighted users see the red border; assistive-tech users hear only the field name.
