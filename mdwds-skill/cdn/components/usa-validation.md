# usa-validation

The USWDS validation pattern is a set of classes and ARIA conventions for showing inline form-field feedback: an error state (red border + error message), a success state (green border), and — for password-style fields — a live "requirements" checklist that ticks off green as the user types valid input. Use it on any field that needs feedback richer than the browser's default tooltip.

> Use this for inline form validation on Maryland.gov pages. There is no `maryland-validation` — MDWDS inherits the USWDS validation pattern with Maryland color tokens. For length capping, pair with `usa-character-count`. For format-based masks (phone, SSN, ZIP), pair with `usa-input-mask` (which already wires HTML5 `pattern` validation).

## What it looks like

The pattern reuses standard form-field markup with additional state classes:

- **Default state** — A standard `usa-input` inside `usa-form-group` with a `usa-label` and optional `usa-hint`. Identical to any other text input: ~48px tall, white background, thin gray border, square corners, body-size text.

- **Error state** — The `usa-form-group` gains `usa-form-group--error` (red 4px left-border accent + spacing); the `usa-label` gains `usa-label--error` (label text in `text-error` red); a `<span class="usa-error-message" role="alert">` appears between the hint and the input with red ~14px semibold text and a small alert icon prefix; the `usa-input` gains `usa-input--error` (red border around the input) and `aria-invalid="true"`. Screen readers announce the error via `role="alert"` when it renders.

- **Success state** — The `usa-input` gains `usa-input--success` (green left-border / green outline) signalling a passing field. No matching success message appears by default — just the border color. Used to confirm a previously-erroring field is now valid.

- **Live requirements checklist** (the canonical USWDS "validation" pattern from `designsystem.digital.gov/components/validation/`) — An `usa-alert usa-alert--info usa-alert--validation` block sits above the input, containing an `usa-alert__heading` and a `<ul class="usa-checklist">` of requirement items. Each `<li class="usa-checklist__item" data-validator="…">` has the rule label as text content (e.g., "Use at least one uppercase character"). As the user types, JS adds `usa-checklist__item--checked` to each `<li>` whose rule is satisfied — visually the bullet flips from a small open circle to a filled green checkmark, and the text color shifts from `base-dark` to a darker green. The associated `<input>` carries `data-validate-uppercase="[A-Z]"`, `data-validate-numerical="\d"`, etc., plus `data-validation-element="<id of the checklist>"` to bind them.

The documented MDWDS variants focus on the error/success/default state pattern. The checklist pattern is supported by the same upstream USWDS JS bundle and is the right choice when the rules are multi-part (passwords, codes).

## Default markup — neutral state with hint

```html
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <div class="usa-form-group">
    <label class="usa-label" for="email">
      Email address
    </label>
    <span class="usa-hint" id="email-hint">For example, name@example.com</span>
    <input
      class="usa-input"
      id="email"
      name="email"
      type="email"
      aria-describedby="email-hint"
    />
  </div>
</form>
```

## Markup — error state

```html
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <div class="usa-form-group usa-form-group--error">
    <label class="usa-label usa-label--error" for="email">
      Email address
      <abbr title="required" class="usa-hint usa-hint--required">*</abbr>
    </label>
    <span class="usa-hint" id="email-hint">For example, name@example.com</span>
    <span class="usa-error-message" id="email-error" role="alert">
      Enter an email address in the format name@example.com
    </span>
    <input
      class="usa-input usa-input--error"
      id="email"
      name="email"
      type="email"
      aria-describedby="email-hint email-error"
      aria-invalid="true"
      required
    />
  </div>
</form>
```

`role="alert"` on the error message makes screen readers announce the message when it appears (e.g., after a failed submit). `aria-invalid="true"` flags the input itself as invalid.

## Markup — success state

```html
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <div class="usa-form-group">
    <label class="usa-label" for="email-ok">Email address</label>
    <span class="usa-hint" id="email-ok-hint">For example, name@example.com</span>
    <input
      class="usa-input usa-input--success"
      id="email-ok"
      name="email-ok"
      type="email"
      value="name@example.com"
      aria-describedby="email-ok-hint"
    />
  </div>
</form>
```

## Markup — password validation with live requirements checklist

```html
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">Create a password</legend>

    <div class="usa-alert usa-alert--info usa-alert--validation">
      <div class="usa-alert__body">
        <h3 class="usa-alert__heading">Password requirements</h3>
        <ul class="usa-checklist" id="password-requirements">
          <li class="usa-checklist__item" data-validator="length">
            Use at least 8 characters
          </li>
          <li class="usa-checklist__item" data-validator="uppercase">
            Use at least one uppercase letter
          </li>
          <li class="usa-checklist__item" data-validator="number">
            Use at least one number
          </li>
          <li class="usa-checklist__item" data-validator="special">
            Use at least one special character
          </li>
        </ul>
      </div>
    </div>

    <label class="usa-label" for="password">Password</label>
    <input
      class="usa-input"
      id="password"
      name="password"
      type="password"
      autocomplete="new-password"
      data-validate-length=".{8,}"
      data-validate-uppercase="[A-Z]"
      data-validate-number="\d"
      data-validate-special="[!@#$%^&*(),.?\":{}|<>]"
      data-validation-element="password-requirements"
    />
  </fieldset>
</form>
```

How it works: each `data-validate-<name>` on the `<input>` is a regex; each `<li>` in the checklist whose `data-validator` matches gains `usa-checklist__item--checked` once the regex passes on the current input value. The `data-validation-element` on the input points at the `<ul>` id.

## Markup — phone with format error

```html
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <div class="usa-form-group usa-form-group--error">
    <label class="usa-label usa-label--error" for="phone">
      Phone number
      <abbr title="required" class="usa-hint usa-hint--required">*</abbr>
    </label>
    <span class="usa-hint" id="phone-hint">###-###-####</span>
    <span class="usa-error-message" id="phone-error" role="alert">
      Enter a phone number in the format ###-###-####.
    </span>
    <input
      class="usa-input usa-input--error"
      id="phone"
      name="phone"
      type="tel"
      pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
      aria-describedby="phone-hint phone-error"
      aria-invalid="true"
      required
    />
  </div>
</form>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-form` | Form wrapper. Constrains width and applies vertical field spacing. |
| `usa-form--large` | Wider variant (~30rem). |
| `usa-form-group` | Per-field vertical container. ~24px bottom margin. |
| `usa-form-group--error` | Adds a red 4px left-border accent (`bg-error`) on the group, with internal padding so all child elements (label, hint, error message, input) sit indented to the right of the accent. |
| `usa-label` | Block label above the field. ~16px semibold, `text-base-darkest`. |
| `usa-label--error` | Label text in red (`text-error`). Pair with `usa-form-group--error`. |
| `usa-hint` | Small gray helper text (~14px) below the label. |
| `usa-hint--required` | Modifier for the asterisk `<abbr>` that marks required fields. |
| `usa-error-message` | Red error text (~14px semibold, color `error`) below the label/hint. Includes a small alert-triangle icon prefix. `role="alert"` triggers screen-reader announcement. |
| `usa-input` | Standard text input: ~48px tall, white, thin gray border, square corners. |
| `usa-input--error` | Red border on the input (no fill change). Add `aria-invalid="true"` alongside. |
| `usa-input--success` | Green border accent on the input — passing state. |
| `usa-alert usa-alert--info usa-alert--validation` | Box for the requirements checklist. Light-blue background (`bg-info-lighter`), 4px left-border accent in `bg-info`, contains the heading + `usa-checklist`. |
| `usa-alert__body` | Inner padding container for alert content. |
| `usa-alert__heading` | The "Requirements" heading inside the alert. ~16px semibold. |
| `usa-checklist` | The `<ul>` of validation rules. Each rule is a `<li class="usa-checklist__item">`. |
| `usa-checklist__item` | A single rule. Default bullet is a small open circle to the left of the rule label, text in `base-dark`. |
| `usa-checklist__item--checked` | (Applied by JS when the rule passes.) Bullet flips to a filled green checkmark; text color shifts to a darker readable green. |
| `data-validate-<name>` (attr on input) | Regex string for one rule. The `<name>` matches a `data-validator="<name>"` on a `<li>`. |
| `data-validation-element` (attr on input) | The `id` of the `<ul class="usa-checklist">` this input is bound to. |
| `aria-invalid="true"` (attr) | Marks the input as failing validation; screen readers communicate the state. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `label` | string | `"Email address"` | Visible label |
| `inputType` | `text` \| `email` \| `tel` \| `password` \| `number` | `"email"` | Native `type` attribute |
| `validationState` | `default` \| `error` \| `success` | `"default"` | Drives which `--error` / `--success` modifiers are added |
| `errorMessage` | string | format-example string | Shown when `validationState === "error"` |
| `hint` | string | format-example string | Always shown when present |
| `required` | bool | `false` | Adds `required` + visible asterisk |
| `disabled` | bool | `false` | Disables the input |
| `enableAnalytics` | bool | `false` | Toggle GA attributes |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Accessibility

- `role="alert"` on `usa-error-message` causes screen readers to announce the message when it appears (e.g., after a failed submit handler renders the error). Do not put `role="alert"` on the input itself.
- `aria-invalid="true"` on the input must be set when the field is in error so assistive tech communicates the failure on focus.
- The input's `aria-describedby` should list **both** the hint id **and** the error message id, space-separated, so screen readers announce all context together.
- For the live checklist pattern, the `usa-checklist` doesn't need an `aria-live` region — the visible item change is enough for sighted users, and the input's progress is otherwise communicated through field state. If you want screen readers to hear each rule pass as the user types, add `aria-live="polite"` to the `<ul>`.
- Use the visible asterisk **and** the native `required` attribute for required fields; neither alone is sufficient.
- Color is never the only indicator of state — error has an icon prefix in `usa-error-message`, checklist items have a filled-vs-open bullet change. Do not strip these visual cues.

## JS requirements

**Requires the `mdwds-core.js` bundle loaded** for the live requirements checklist pattern (`data-validate-*` rules ticking checklist items as the user types). Without it: the checklist renders statically — every rule shows the unchecked bullet regardless of input — and the input has no automatic feedback as the user types.

The error / success / default state pattern itself is pure CSS and does **not** require JS. You can render `usa-form-group--error` + `usa-input--error` + `usa-error-message` server-side after a failed submit, and it will work without any JS at all. The JS is only needed for live, type-as-you-go validation.

## Common mistakes

1. **Forgetting `mdwds-core.js` when using `usa-checklist` + `data-validate-*`** — the checklist sits there statically and never updates. Users get no live feedback.
2. **Showing the error message without `role="alert"`** — screen readers don't announce the error when it appears post-submit.
3. **Setting `usa-input--error` but forgetting `aria-invalid="true"`** — sighted users see the red border but assistive-tech users don't hear that the field is invalid.
4. **Omitting the error message id from the input's `aria-describedby`** — the message renders visually but isn't read with the field.
5. **Combining `usa-input--error` and `usa-input--success` on the same input** — they're mutually exclusive; the modifier order in the cascade decides which wins, which is unpredictable. Pick one state.
6. **Putting `usa-form-group--error` *inside* the input** — it belongs on the wrapping `<div class="usa-form-group">`, not on the input.
7. **Validating only client-side** — server-side validation is mandatory for security. The visual feedback here is UX assist, not enforcement.
8. **Forgetting `data-validation-element` on an input paired with a `usa-checklist`** — the input has no way to know which `<ul>` of rules to update.
