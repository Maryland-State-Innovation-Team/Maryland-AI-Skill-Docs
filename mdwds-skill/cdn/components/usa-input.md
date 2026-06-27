# usa-input

The USWDS single-line text input. Used for short typed values — names, email addresses, phone numbers, ZIP codes, license plate numbers, vehicle identification numbers, dates entered by keyboard. The visual styling is identical across all `type` values; the `type` attribute on `<input>` controls keyboard layout, browser-native validation, and small UI affordances (a date type opens a date picker, a number type shows up/down spinners, a password type masks the value).

Use this for text-entry fields on Maryland.gov pages; the CDN themes USWDS form colors to Maryland blue (focus ring, error border).

## What it looks like

A `usa-input` is a 40px-tall (`units(5)`) rectangular text field with a **1px solid `base-dark` (cool gray) border**, no border-radius (square corners), white background, and `color: ink` (near-black) typed text. Internal padding is 8px (`units(1)`) on all sides; the field sits 8px below its associated `<label class="usa-label">`. The font is Source Sans Pro Web at the theme body size (~16px) with the theme input line-height.

By default, the input's `max-width` is 480px (`units("mobile-lg")`) — fits a typical name or email comfortably without stretching across wide screens. Inside a `<form class="usa-form">`, this per-input max-width is cleared so the form's own max-width governs (320px / 480px). Size-modifier classes (`usa-input--2xs` through `usa-input--2xl`) override both to widths measured in `ex` (character widths) so a 5-digit ZIP field is visually 5 characters wide.

On focus the field draws a **2px Maryland blue outline** (the focus ring) with a 2px offset, no border-color change. On `disabled` the field gets a `disabled-lighter` background, a `disabled` border, and `disabled-dark` text; the cursor becomes `not-allowed`.

Validation states: `usa-input--error` swaps the border to **2px solid `error-dark` (red)** and `usa-input--success` swaps it to 2px solid `success` (green). Both bump up vertical padding by 4px to keep the total height stable across states.

## Variants

### State modifiers

| Variant | Visual |
|---|---|
| (none) | Default 1px base-dark border, 40px tall. |
| `usa-input--error` | 2px red (`error-dark`) border. Use when validation fails. |
| `usa-input--success` | 2px green (`success`) border. Use to confirm a value passed validation. |

### Width modifiers

| Class | Width | Typical use |
|---|---|---|
| `usa-input--2xs` | 5ex (~50px) | 1–3 digit codes (apartment/unit number) |
| `usa-input--xs` | 9ex (~90px) | ZIP 5-digit, short ID |
| `usa-input--sm` / `usa-input--small` | 13ex (~130px) | Phone area code, short ID |
| `usa-input--md` / `usa-input--medium` | 20ex (~200px) | ZIP+4, license plate, VIN segment |
| `usa-input--lg` | 30ex (~300px) | Name, short email |
| `usa-input--xl` | 40ex (~400px) | Email, address line |
| `usa-input--2xl` | 50ex (~500px) | Full address, long subject line |

These set `max-width` only; the input remains `width: 100%` until it hits that cap. The width modifier wins over the form's max-width because it's applied via a higher-specificity selector.

### Type values (set on the `<input>`)

The `type` attribute does not change the visual baseline — same border, height, font — but controls keyboard/UX:

| `type` | Effect |
|---|---|
| `text` | Default plain text. |
| `email` | Mobile keyboard shows `@` and `.com`; browser validates email format on submit. Pair with `autocomplete="email"`. |
| `tel` | Mobile keyboard shows the dial pad. Pair with `autocomplete="tel"` and a `pattern` for format enforcement. |
| `password` | Characters are masked. Pair with `autocomplete="current-password"` or `"new-password"`. |
| `number` | Spinner buttons (browser-dependent); decimal/numeric keyboard on mobile. Note: prefer `type="text" inputmode="numeric" pattern="[0-9]*"` for digit-only fields without spinners (ZIP, account numbers) — it's a more reliable UX. |
| `date` | Native date picker (browser-rendered popover). Format displayed is `MM/DD/YYYY` (US locale); value submitted is ISO `YYYY-MM-DD`. For a calendar-rich Maryland-themed picker, see `usa-date-picker` instead. |
| `url` | Mobile keyboard shows `/` and `.com`; browser validates URL format. |
| `search` | Subtle UA-specific affordances (some browsers render a clear button). |

## When to use which variant

- **Default size, no modifier** → Most fields. Lets the form's max-width control the row width.
- **Width modifiers** → When the value has a known short length (ZIP, area code, dollar amount). Visually communicates the expected size of input.
- **`usa-input--error` / `usa-input--success`** → Only after validation has run. Don't apply error styling to a field the user hasn't touched.
- **`type="email" / "tel" / "date" / "number"`** → Always match `type` to the data being collected — mobile keyboards depend on it.

## Default markup

```html
<form class="usa-form">
  <label class="usa-label" for="full-name">Full name</label>
  <input
    class="usa-input"
    id="full-name"
    name="full-name"
    type="text"
    autocomplete="name"
    required
  />
</form>
```

## Markup — email

```html
<form class="usa-form">
  <label class="usa-label" for="email">Email address</label>
  <input
    class="usa-input"
    id="email"
    name="email"
    type="email"
    autocomplete="email"
    required
  />
</form>
```

## Markup — phone (tel)

```html
<form class="usa-form">
  <label class="usa-label" for="phone">Phone number</label>
  <div class="usa-hint" id="phone-hint">10 digits, no spaces or dashes</div>
  <input
    class="usa-input"
    id="phone"
    name="phone"
    type="tel"
    autocomplete="tel"
    pattern="[0-9]{10}"
    aria-describedby="phone-hint"
  />
</form>
```

## Markup — password

```html
<form class="usa-form">
  <label class="usa-label" for="password">Password</label>
  <div class="usa-hint" id="pw-hint">At least 12 characters, including a number</div>
  <input
    class="usa-input"
    id="password"
    name="password"
    type="password"
    autocomplete="new-password"
    minlength="12"
    aria-describedby="pw-hint"
    required
  />
</form>
```

## Markup — number

```html
<form class="usa-form">
  <label class="usa-label" for="party-size">Number of attendees</label>
  <input
    class="usa-input usa-input--xs"
    id="party-size"
    name="party-size"
    type="number"
    min="1"
    max="20"
    step="1"
    required
  />
</form>
```

For a 5-digit ZIP code, prefer this pattern (no spinner UI):

```html
<label class="usa-label" for="zip">ZIP code</label>
<input
  class="usa-input usa-input--medium"
  id="zip"
  name="zip"
  type="text"
  inputmode="numeric"
  pattern="[0-9]{5}"
  maxlength="5"
  autocomplete="postal-code"
  required
/>
```

## Markup — date

```html
<form class="usa-form">
  <label class="usa-label" for="appt-date">Appointment date</label>
  <input
    class="usa-input"
    id="appt-date"
    name="appt-date"
    type="date"
    min="2026-06-26"
    required
  />
</form>
```

(For a Maryland-themed calendar widget instead of the browser-native picker, see `usa-date-picker`.)

## Markup — with error

```html
<form class="usa-form">
  <div class="usa-form-group usa-form-group--error">
    <label class="usa-label usa-label--error" for="vin">Vehicle identification number (VIN)</label>
    <span class="usa-error-message" id="vin-err" role="alert">
      Enter all 17 characters of the VIN, letters and numbers only
    </span>
    <input
      class="usa-input usa-input--error usa-input--xl"
      id="vin"
      name="vin"
      type="text"
      pattern="[A-HJ-NPR-Z0-9]{17}"
      maxlength="17"
      aria-describedby="vin-err"
      aria-invalid="true"
      required
    />
  </div>
</form>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-input` | Base styles: 40px tall (`units(5)`), 1px solid `base-dark` border, square corners (no radius), white background, `color: ink` text, 8px internal padding, 8px top margin (separation from label above), `max-width: 480px` outside a form. Disabled state: `disabled-lighter` background, `disabled-dark` text, `not-allowed` cursor. |
| `usa-input--error` | Replaces border with **2px solid `error-dark` (red)**; reduces vertical padding by 4px so total height matches default. Apply only after validation runs. |
| `usa-input--success` | Replaces border with 2px solid `success` (green); padding adjustment matches `--error`. Use sparingly to confirm validation pass. |
| `usa-input--2xs` | `max-width: 5ex` (about 50px). Smallest size — single-character codes. |
| `usa-input--xs` | `max-width: 9ex` (about 90px). 5-digit ZIP, area code. |
| `usa-input--sm` / `usa-input--small` | `max-width: 13ex` (about 130px). |
| `usa-input--md` / `usa-input--medium` | `max-width: 20ex` (about 200px). |
| `usa-input--lg` | `max-width: 30ex` (about 300px). |
| `usa-input--xl` | `max-width: 40ex` (about 400px). |
| `usa-input--2xl` | `max-width: 50ex` (about 500px). |
| `usa-label` | Styles the associated `<label>`: Source Sans Pro body size, color base-darkest, `margin-top: 24px`. Sits directly above the input. |
| `usa-label--error` | Bold weight, `margin-top: 0` (sits flush below the form-group's red border). |
| `usa-hint` | Helper text below the label, color `base` (mid-gray), same font as label. Use with `aria-describedby` on the input. |
| `usa-error-message` | Bold red (`error-dark`) message above the input. `padding-y: 4px`. Set `role="alert"` so dynamic errors are announced. |
| `usa-form-group` | Wraps label + hint + input + error. `margin-top: 24px` separates groups; resets first-child label's top margin. |
| `usa-form-group--error` | Adds a 4px red left border and `padding-left: 16px`; on desktop shifts the group left by 20px so the red border aligns with the form's left edge. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `label` | string | `"Text input label"` | Visible label text |
| `id` | string | `"input-type-text"` | Input id, must match label's `for` |
| `name` | string | `"input-type-text"` | Form submission key |
| `placeholder` | string | `""` | Optional placeholder — **never use as the only label** |
| `ariaLabel` | string | `""` | Only when the visible label is hidden (rare) |
| `ariaDescribedBy` | string | `""` | ID of a hint or error message |

The documented variants render only `type="text"`; the `type` attribute is set directly on the `<input>` element in markup — there's no story-level prop for it because the visual classes are identical across types.

## Accessibility

- **Every input needs a `<label class="usa-label" for="ID">` with `for` matching the input's `id`.** Click-to-focus and screen-reader name both depend on this pairing.
- **Don't use `placeholder` as the only label** — it disappears on input and isn't reliably announced.
- **`autocomplete`** — set the appropriate token: `name`, `given-name`, `family-name`, `email`, `tel`, `street-address`, `address-level2` (city), `address-level1` (state), `postal-code`, `bday`, `cc-number`, etc. Improves both autofill UX and assistive-tech support.
- **`type` matters for mobile**: `email`, `tel`, `number`, `url`, `date` all show different keyboards. Pick the right one.
- **Required:** set `required` on the input and indicate visually (asterisk after the label or "(required)" in the label text). Don't rely on `required` alone — screen readers do announce it, but sighted users won't see it.
- **Errors:** add `aria-invalid="true"`, link the message via `aria-describedby="<error-id>"`, and put `role="alert"` on the `usa-error-message`.
- **Hints:** wire `<div class="usa-hint" id="X">` to the input via `aria-describedby="X"`. If both a hint and an error apply, use a space-separated list: `aria-describedby="hint-id error-id"`.
- **`inputmode`** for digit-only fields: `inputmode="numeric"` brings up a numeric keypad on mobile without the visual spinner of `type="number"`. Pair with `pattern="[0-9]*"` and `type="text"` for ZIP codes, account numbers, etc.

## JS requirements

No JS required — `<input>` is a native HTML form control styled by the CDN stylesheet. The browser handles validation (HTML5 `pattern`, `required`, `type="email"`, etc.), date pickers (`type="date"`), and password masking.

For Maryland-themed date pickers, masked inputs (phone/SSN format guides), input prefix/suffix, and character counts, see the corresponding component docs (`usa-date-picker`, `usa-input-mask`, `usa-input-prefix-suffix`, `usa-character-count`) — those require the USWDS JS bundle.

## Common mistakes

1. **Placeholder used as the label.** `<input placeholder="Email" />` with no label — invisible to screen readers, vanishes the moment the user types. Always pair with `<label class="usa-label">`.
2. **`for`/`id` mismatch** between label and input. Browsers won't show an error; the click-to-focus and screen-reader name silently break.
3. **Wrong `type` attribute** — `type="text"` for an email field robs the user of the mobile email keyboard and bypasses browser email-format validation. Pick the right type: `email`, `tel`, `number`, `date`, `password`, `url`.
4. **Error message not linked** via `aria-describedby`. The red border and message are visible to sighted users; assistive tech reads the input name alone and the user doesn't know what's wrong.
5. **`type="number"` for ZIP codes, account numbers, or anything with leading zeros.** Spinner UI is wrong for these, and `type="number"` strips leading zeros. Use `type="text" inputmode="numeric" pattern="[0-9]*"` instead.
6. **Missing `name` attribute.** The form will submit without the field's value — silent data loss.
7. **Inline `<style>` to recolor focus ring or border.** The CDN sets focus to Maryland blue and borders to base-dark/error-dark/success. Overriding produces off-brand styling. Use the `--error` / `--success` state classes instead.
