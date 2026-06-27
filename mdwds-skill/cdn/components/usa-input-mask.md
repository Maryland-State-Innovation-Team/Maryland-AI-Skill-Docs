# usa-input-mask

The USWDS input mask is a text input that auto-formats as the user types. Use it for fixed-format strings: phone numbers (`###-###-####`), Social Security Numbers (`###-##-####`), ZIP codes (`#####` or `#####-####`), or other patterns where punctuation is part of the format.

> Use this for masked input on Maryland.gov pages. There is no `maryland-input-mask` — MDWDS inherits the USWDS component with Maryland color tokens. For a free-form text field with no formatting, use plain `usa-input`. For currency or unit affixes, use `usa-input-prefix-suffix`.

## What it looks like

The control is a standard `usa-input` text field (~48px tall, white background, thin gray border, square corners) with a small gray hint above (`usa-hint`, ~14px) showing the expected format (e.g., "###-###-####"). The `placeholder` attribute shows the same pattern with underscores instead of `#` (`___-___-____`) inside the input until the user starts typing.

As the user types digits, the formatting characters (dashes, parentheses, spaces) appear automatically. The cursor steps over the punctuation so the user can keep typing digits without manually inserting separators. Backspace removes the most recent digit and pulls the cursor back through any punctuation as needed.

The visible value matches the masked pattern: typing "4105551234" produces "410-555-1234" in the field for the phone mask. The submitted form value is the same masked string by default.

If the `pattern` constraint doesn't match on submit, the field gets the standard `usa-input--error` red border and the browser shows its native invalid tooltip — there's no built-in inline error message. To add one, pair this with `usa-validation` markup.

Disabled state grays the input out (`bg-disabled-lighter`) with a not-allowed cursor.

## Default markup

```html
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <label class="usa-label" for="phone">Phone number</label>
  <span class="usa-hint" id="phone-hint">###-###-####</span>
  <input
    class="usa-input"
    id="phone"
    name="phone"
    type="text"
    data-input-mask
    data-mask-type="phone"
    pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
    placeholder="___-___-____"
    aria-describedby="phone-hint"
  />
</form>
```

`data-input-mask` is the marker that triggers MDWDS' masking JS for this input. `data-mask-type` selects one of the predefined masks: `"phone"`, `"ssn"`, `"zip"`, or `"custom"`.

## Markup — Social Security Number (required)

```html
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <label class="usa-label" for="ssn">
    Social Security Number
    <abbr title="required" class="usa-hint usa-hint--required">*</abbr>
  </label>
  <span class="usa-hint" id="ssn-hint">###-##-####</span>
  <input
    class="usa-input"
    id="ssn"
    name="ssn"
    type="text"
    data-input-mask
    data-mask-type="ssn"
    pattern="[0-9]{3}-[0-9]{2}-[0-9]{4}"
    placeholder="___-__-____"
    aria-describedby="ssn-hint"
    required
  />
</form>
```

## Markup — ZIP code (5 or 9 digits)

```html
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <label class="usa-label" for="zip">ZIP code</label>
  <span class="usa-hint" id="zip-hint">##### or #####-####</span>
  <input
    class="usa-input"
    id="zip"
    name="zip"
    type="text"
    data-input-mask
    data-mask-type="zip"
    pattern="[0-9]{5}(-[0-9]{4})?"
    placeholder="_____-____"
    aria-describedby="zip-hint"
  />
</form>
```

The ZIP mask accepts the short 5-digit and the long ZIP+4 forms — the `pattern` makes the `-####` portion optional.

## Markup — disabled

```html
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <label class="usa-label" for="locked-phone">Phone number on file</label>
  <span class="usa-hint" id="locked-phone-hint">###-###-####</span>
  <input
    class="usa-input"
    id="locked-phone"
    name="locked-phone"
    type="text"
    data-input-mask
    data-mask-type="phone"
    pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
    placeholder="___-___-____"
    aria-describedby="locked-phone-hint"
    value="410-555-0199"
    disabled
  />
</form>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-form` | Form wrapper. Constrains form width (default ~24rem) and applies vertical spacing between fields. |
| `usa-form--large` | Wider variant (~30rem). |
| `usa-label` | Block label above the field. ~16px semibold, color `base-darkest`. |
| `usa-hint` | Small gray helper text (~14px) below the label. |
| `usa-hint--required` | Modifier for the asterisk `<abbr>` that marks required fields. |
| `usa-input` | The text input itself. ~48px tall, white, thin gray border, square corners, body-size text. |
| `usa-input--error` | (Applied by JS or markup on validation failure.) Red left-border + red border highlight. |
| `data-input-mask` (attr) | MDWDS marker that activates the masking behavior on this input. |
| `data-mask-type` (attr) | Selects a predefined mask: `"phone"`, `"ssn"`, `"zip"`, or `"custom"`. |
| `pattern` (attr) | HTML5 regex constraint. Enforces format on form submit via native validation. |
| `placeholder` (attr) | Shows the empty mask with underscores when the field is empty. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `label` | string | `"Phone number"` | Visible label |
| `maskType` | `phone` \| `ssn` \| `zip` \| `custom` | `"phone"` | Selects mask + placeholder + pattern |
| `hint` | string | `"###-###-####"` | Hint shown above the field |
| `required` | bool | `false` | Adds `required` + visible asterisk |
| `disabled` | bool | `false` | Disables the input |
| `enableAnalytics` | bool | `false` | Toggle GA attributes |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

### Mask presets

| `maskType` | `pattern` | `placeholder` | Default hint |
|---|---|---|---|
| `phone` | `[0-9]{3}-[0-9]{3}-[0-9]{4}` | `___-___-____` | `###-###-####` |
| `ssn` | `[0-9]{3}-[0-9]{2}-[0-9]{4}` | `___-__-____` | `###-##-####` |
| `zip` | `[0-9]{5}(-[0-9]{4})?` | `_____-____` | `##### or #####-####` |
| `custom` | (none) | (none) | (none) — supply your own |

## Accessibility

- The `<label>` must use `for="..."` matching the input's `id`.
- The format hint must be referenced via `aria-describedby` so screen readers announce the expected pattern alongside the label.
- For required fields, the visible asterisk (`<abbr title="required">*</abbr>`) communicates required-ness to sighted users; the `required` attribute on the `<input>` communicates it to assistive tech via native ARIA mapping.
- For sensitive fields like SSN, consider `autocomplete="off"` and `inputmode="numeric"` to suppress autofill and surface the numeric keyboard on mobile.
- If you display an error inline, wrap with `usa-form-group--error`, add `usa-input--error` to the input, render a `<span class="usa-error-message" role="alert">…</span>` above the input, and append its `id` to `aria-describedby`.

## JS requirements

**Requires the `mdwds-core.js` bundle loaded** for live cursor-stepping and digit auto-formatting. Without it: the placeholder still shows the format, and the HTML5 `pattern` still validates on submit, but the field does not auto-insert dashes as the user types — they must type "410-555-1234" by hand including the dashes, or submit and get a validation error.

## Common mistakes

1. **Forgetting `mdwds-core.js`** — the input still works as a plain text field with HTML5 `pattern` validation, but the dash-skipping cursor magic is gone. Users have to type punctuation manually.
2. **Omitting `data-input-mask` on the `<input>`** — the JS won't attach. The mask is recognized via this attribute, not via a class.
3. **Mismatched `pattern` and `data-mask-type`** — if you pick `data-mask-type="phone"` but write your own `pattern` that doesn't match `###-###-####`, the input formats one way and validation rejects the result.
4. **Using `type="tel"` for SSN or ZIP** — `type="tel"` is fine for phone (surfaces numeric keyboard on mobile) but inappropriate for SSN/ZIP. Use `type="text"` plus `inputmode="numeric"`.
5. **Forgetting `aria-describedby` to link the hint** — screen reader users miss the format guidance.
6. **Putting `data-input-mask` on a non-`<input>`** — masking is an `<input>`-only behavior. It does nothing on `<textarea>` or `<select>`.
7. **Storing the masked value in the database** — strip dashes on the server before persisting if your data model wants raw digits.
