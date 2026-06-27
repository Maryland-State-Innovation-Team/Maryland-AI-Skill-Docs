# usa-form

The USWDS form wrapper that establishes typography, line-height, max-width, and consistent vertical spacing for all form fields inside. Every Maryland.gov form should wrap its fields in `<form class="usa-form">` — without it, child `usa-label`, `usa-input`, `usa-select`, `usa-textarea`, `usa-radio`, `usa-checkbox`, and `usa-button` elements still render styled, but the form's horizontal max-width, the vertical rhythm between fields, and the responsive sizing won't take effect.

Use this for form layout on Maryland.gov pages; the CDN themes USWDS form colors to Maryland blue (focus ring, error/success borders, required asterisk).

## What it looks like

A `usa-form` is a vertical column of stacked form rows on a white background. Above the `mobile-lg` breakpoint (480px+), the form constrains its content to a fixed max-width: **320px** (`units("mobile")`) by default, or **480px** (`units("mobile-lg")`) with `usa-form--large`. Below that breakpoint the form fills the width of its parent.

Each `usa-label` sits flush-left in bold-ish Source Sans Pro (~17.6px at base) with `margin-top: units(3)` (24px) above. Inputs, textareas, and selects sit directly under their label with `margin-top: units(1)` (8px) of separation, height **40px** (`units(5)`), 1px solid base-dark border, **no border-radius** (square corners), and white background. The `<button class="usa-button">` inside a form gets `margin-top: units(1)` (8px) on mobile and `units(3)` (24px) at mobile-lg and up — extra breathing room before the submit action.

`usa-form` clears the `max-width` constraint that lives on `.usa-input`, `.usa-textarea`, `.usa-select`, `.usa-range` directly so the form's own max-width controls field width (but per-input size modifiers like `usa-input--md` still win).

`abbr[title="required"]` inside the form (used to render the red asterisk for required fields) has its dotted underline removed for legibility.

## Variants

| Variant | Visual |
|---|---|
| `usa-form` (default) | Max-width 320px at `mobile-lg`+ (fits short single-column forms — name, email, ZIP). |
| `usa-form--large` | Max-width 480px at `mobile-lg`+ (fits longer fields like mailing addresses, vehicle identification numbers). |

## When to use which variant

- **Default `usa-form`** → Short forms (sign-in, newsletter signup, single-field search) where compact width reinforces "this is a small task".
- **`usa-form--large`** → Multi-field forms with longer inputs (mailing addresses, license/permit applications, contact forms with a message field).

## Default markup

```html
<form class="usa-form">
  <label class="usa-label" for="first-name">First name</label>
  <input
    class="usa-input"
    id="first-name"
    name="first-name"
    type="text"
    autocomplete="given-name"
    required
  />

  <label class="usa-label" for="last-name">Last name</label>
  <input
    class="usa-input"
    id="last-name"
    name="last-name"
    type="text"
    autocomplete="family-name"
    required
  />

  <label class="usa-label" for="email">Email address</label>
  <input
    class="usa-input"
    id="email"
    name="email"
    type="email"
    autocomplete="email"
    required
  />

  <button type="submit" class="usa-button">Submit</button>
</form>
```

## Markup — usa-form--large

```html
<form class="usa-form usa-form--large">
  <label class="usa-label" for="street">Mailing address</label>
  <input
    class="usa-input"
    id="street"
    name="street"
    type="text"
    autocomplete="street-address"
    required
  />

  <label class="usa-label" for="city">City</label>
  <input
    class="usa-input"
    id="city"
    name="city"
    type="text"
    autocomplete="address-level2"
    required
  />

  <label class="usa-label" for="zip">ZIP code</label>
  <input
    class="usa-input usa-input--medium"
    id="zip"
    name="zip"
    type="text"
    inputmode="numeric"
    pattern="[0-9]{5}"
    autocomplete="postal-code"
    required
  />

  <button type="submit" class="usa-button">Update address</button>
</form>
```

## Markup — with fieldset and legend

Wrap related fields in `<fieldset class="usa-fieldset">` with a `<legend class="usa-legend">` to give the group a programmatic name. **Required** for radio and checkbox groups; recommended for any logical grouping (e.g., "Personal information", "Contact details").

```html
<form class="usa-form">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">Personal information</legend>

    <label class="usa-label" for="full-name">Full name</label>
    <input class="usa-input" id="full-name" name="full-name" type="text" required />

    <label class="usa-label" for="dob">Date of birth</label>
    <input class="usa-input" id="dob" name="dob" type="date" required />
  </fieldset>

  <button type="submit" class="usa-button">Continue</button>
</form>
```

## Markup — with hint text

Place a `<div class="usa-hint">` between the label and the input, and reference its `id` from the input's `aria-describedby`. The hint renders in muted gray below the label.

```html
<form class="usa-form">
  <label class="usa-label" for="phone">Phone number</label>
  <div class="usa-hint" id="phone-hint">10-digit US phone number, no spaces</div>
  <input
    class="usa-input"
    id="phone"
    name="phone"
    type="tel"
    autocomplete="tel"
    aria-describedby="phone-hint"
  />

  <button type="submit" class="usa-button">Save</button>
</form>
```

## Markup — with error state

When a field is invalid, wrap it in `<div class="usa-form-group usa-form-group--error">` to apply the red left border and indented padding, swap the label to `usa-label usa-label--error` (bold), and add a `<span class="usa-error-message">` linked via `aria-describedby`. The input itself gets `usa-input--error` (red border).

```html
<form class="usa-form">
  <div class="usa-form-group usa-form-group--error">
    <label class="usa-label usa-label--error" for="email-err">Email address</label>
    <span class="usa-error-message" id="email-err-msg" role="alert">
      Enter a valid email address (e.g., name@example.com)
    </span>
    <input
      class="usa-input usa-input--error"
      id="email-err"
      name="email"
      type="email"
      aria-describedby="email-err-msg"
      aria-invalid="true"
      required
    />
  </div>

  <button type="submit" class="usa-button">Submit</button>
</form>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-form` | The form wrapper. Applies Source Sans Pro body font at theme body size with the form line-height; sets `max-width: 320px` at `mobile-lg`+ so the form is a single readable column. Removes max-width from direct-child inputs/selects/textareas so the form's own max-width governs. Adds `margin-top: 8px` (mobile) / `24px` (mobile-lg+) to the submit `usa-button`. |
| `usa-form--large` | Widens the form's max-width to **480px** (`units("mobile-lg")`) at `mobile-lg`+. Used when input values are longer (addresses, identification numbers). |
| `usa-fieldset` | Resets browser default fieldset chrome: no border, no padding, no margin. Required wrapper for radio/checkbox groups; useful for grouping any related fields. |
| `usa-legend` | Styles the `<legend>` text as a label (Source Sans Pro, bold-ish weight, color base-darkest). Adds `margin-top` so the legend sits above its group with proper rhythm. |
| `usa-legend--large` | Larger legend: font size "xl" (~22.4px), bold weight, with extra top margin. Use for section-level groupings inside long forms. |
| `usa-label` | Styles a `<label>` element: Source Sans Pro at body size, color base-darkest, `margin-top: 24px` so it pushes off the previous field. |
| `usa-label--error` | Bold weight, `margin-top: 0` (it sits next to the form-group's red border, so no extra space above). |
| `usa-label--required` | Red text — use only on the required-asterisk `<abbr>`, not the label text itself. |
| `usa-hint` | Helper text under the label: same font family as `usa-label`, color base (mid-gray). Reference via `aria-describedby` on the input. |
| `usa-hint--required` | Red hint text (used for "Required" hint when the entire form is required-by-default). |
| `usa-form-group` | Wraps a single label + input + hint + error combo. Adds `margin-top: 24px` to space groups apart and resets the inner `usa-label`'s top margin to 0 (so the group's margin wins). |
| `usa-form-group--error` | Adds a 4px red left border (`error-dark`), `padding-left: 16px`, and on desktop shifts the group 20px left so the border lines up with the form's visual left edge — drawing the eye to the failing field. |
| `usa-error-message` | Red bold text shown above the input. `padding-y: 4px`. Add `role="alert"` so screen readers announce on dynamic insertion. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `large` | bool | `false` | Use the `usa-form--large` variant |
| `includeFieldset` | bool | `false` | Wrap fields in `<fieldset class="usa-fieldset">` + `<legend class="usa-legend">` |
| `legend` | string | `"Personal Information"` | Legend text |
| `enableAnalytics` | bool | `false` | Add `data-ga-*` attributes to the submit button |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Accessibility

- **Always pair every input with a `<label class="usa-label" for="ID">`.** The `for` attribute on the label must equal the `id` attribute on the input. Without this, screen readers can't announce the field name.
- **Use placeholders only as examples, never as the only label.** Placeholders disappear on input, leaving the field nameless for assistive tech.
- **Required fields:** set `required` on the input and include a visible indicator (the form rendering convention is `<abbr title="required" class="usa-hint usa-hint--required">*</abbr>` after the label text, or — more accessibly — append the word "(required)" in the label).
- **Group radio/checkbox sets in `<fieldset class="usa-fieldset">` with `<legend class="usa-legend">`.** The legend names the group; screen readers announce it before each option.
- **Errors:** add `aria-invalid="true"` on the failing input, link the error message via `aria-describedby="<error-id>"`, and use `role="alert"` on `usa-error-message` so screen readers announce inline. Don't rely on red color alone — the bold weight and text content carry the meaning.
- **Hints:** use `<div class="usa-hint" id="X">` and `aria-describedby="X"` on the input. If an input has both a hint and an error, list both IDs: `aria-describedby="hint-id error-id"`.
- **Form landmark:** `<form>` is itself a landmark only when it has an `aria-label` or `aria-labelledby`. For most short forms this is unnecessary; for sub-forms inside a larger page, give the form a label.
- **Autocomplete:** set `autocomplete` to the standard token (`given-name`, `family-name`, `email`, `tel`, `street-address`, `postal-code`, `bday`, etc.) — this is both an accessibility benefit (mobile keyboards, password managers) and a usability one.

## JS requirements

No JS required — `<form>`, `<input>`, `<textarea>`, `<select>`, `<fieldset>`, and `<legend>` are native HTML form controls styled by the CDN stylesheet. The MDWDS init script (see `cdn/setup.md`) handles font loading and FOUC prevention only.

For interactive form features (`usa-date-picker`, `usa-combo-box`, `usa-character-count`, file-input drag-and-drop, password-show toggle), the USWDS JS bundle must be loaded — see the respective component docs.

## Common mistakes

1. **Omitting the `<label class="usa-label">` and using `placeholder` as the only label.** Placeholders vanish on focus and aren't announced consistently by screen readers. Always have a visible, persistent label.
2. **`for`/`id` mismatch** between `<label for="x">` and `<input id="y">`. The click-to-focus and screen-reader association both break silently.
3. **Wrapping a radio or checkbox group without `<fieldset class="usa-fieldset"><legend class="usa-legend">`.** Without the legend, screen-reader users hear each option label but never the question the options answer.
4. **Missing `name` attribute on inputs.** Browsers won't submit the value with the form. Always set `name` (and conventionally make it match the `id` or use kebab-case of the label).
5. **Inline `<style>` to recolor the focus ring, border, or background.** The CDN sets the focus ring to Maryland blue and the borders to base-dark; overriding produces an off-brand form. If a field needs a different color, it's almost certainly the wrong component or the wrong state class.
6. **Putting `style="max-width: 600px"` on the `<form>` to widen it.** Use `usa-form--large` (480px) or remove the wrapper if you need a fluid full-width form.
7. **Setting `margin-top` on inputs via inline style.** Use `usa-form-group` to separate field groups, and let `usa-label`'s built-in `margin-top: 24px` handle the rhythm.
