# usa-input-prefix-suffix

The USWDS prefix/suffix input attaches a non-editable text or icon affix at the left edge, the right edge, or both edges of a text input, inside the same outlined frame. Use it for currency (`$`), percentages (`%`), units (`lbs`, `mi`), URL pieces (`https://` / `.gov`), or a search-icon affordance.

> Use this for affix inputs on Maryland.gov pages. There is no `maryland-input-prefix-suffix` — MDWDS inherits the USWDS component with Maryland color tokens. For a masked format (phone/SSN/ZIP) where punctuation appears mid-value, use `usa-input-mask` instead.

## What it looks like

Visually it appears as a single bordered field: thin gray border, white background, square corners, ~48px tall, body-size text. The affixes (prefix on the left, suffix on the right) are inset inside the frame against a slightly lighter background tint, with vertical dividers between affix and input. Both affixes are in `text-base-darkest` body-size text by default; they are `aria-hidden="true"` so screen readers don't read them as form values.

- **Prefix only** — affix on the left ("$", "https://"), input fills the rest.
- **Suffix only** — input on the left, affix on the right ("lbs", "%", ".gov").
- **Both** — prefix on the left, input in the middle, suffix on the right.
- The affix area is ~2.5rem (40px) wide for short text. The text is centered vertically.

In error state (`usa-form-group--error` + `usa-input-group--error`), the entire frame gets a red left-border accent and the input + affixes share a red border. An `usa-error-message` (red, ~14px semibold) appears above the input group with `role="alert"`. The matching `usa-label--error` colors the label red as well.

Disabled state mutes the input + affix backgrounds to `bg-disabled-lighter` with a not-allowed cursor over the input.

To use a Material Symbols icon (such as a search magnifier) as the prefix or suffix, drop a `<span class="usa-icon">` containing an `<svg>` into the prefix/suffix `<div>`.

## Default markup — prefix only ("$ 0.00")

```html
<form class="usa-form">
  <div class="usa-form-group">
    <label class="usa-label" for="park-fee">Park entrance fee</label>
    <div class="usa-input-group">
      <div class="usa-input-prefix" aria-hidden="true">$</div>
      <input
        id="park-fee"
        class="usa-input"
        type="text"
        name="park-fee"
        placeholder="0.00"
      />
    </div>
  </div>
</form>
```

## Markup — suffix only ("lbs", "%")

```html
<form class="usa-form">
  <div class="usa-form-group">
    <label class="usa-label" for="catch-weight">Reported catch weight</label>
    <div class="usa-input-group">
      <input
        id="catch-weight"
        class="usa-input"
        type="text"
        name="catch-weight"
        placeholder="Enter weight"
      />
      <div class="usa-input-suffix" aria-hidden="true">lbs</div>
    </div>
  </div>
</form>
```

## Markup — prefix and suffix together (URL)

```html
<form class="usa-form">
  <div class="usa-form-group">
    <label class="usa-label" for="agency-url">Agency website</label>
    <div class="usa-hint" id="agency-url-hint">Enter your Maryland agency subdomain</div>
    <div class="usa-input-group">
      <div class="usa-input-prefix" aria-hidden="true">https://</div>
      <input
        id="agency-url"
        class="usa-input"
        type="text"
        name="agency-url"
        placeholder="example"
        aria-describedby="agency-url-hint"
      />
      <div class="usa-input-suffix" aria-hidden="true">.maryland.gov</div>
    </div>
  </div>
</form>
```

## Markup — icon suffix (search field)

```html
<form class="usa-form">
  <div class="usa-form-group">
    <label class="usa-label" for="park-search">Find a state park</label>
    <div class="usa-input-group">
      <input
        id="park-search"
        class="usa-input"
        type="search"
        name="park-search"
        placeholder="Park name or county"
      />
      <div class="usa-input-suffix" aria-hidden="true">
        <span class="usa-icon" aria-hidden="true">
          <!-- Material Symbols: search -->
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20" fill="currentColor">
            <path d="M15.5 14h-.79l-.28-.27a6.5 6.5 0 1 0-.7.7l.27.28v.79l5 5 1.5-1.5-5-5zm-6 0A4.5 4.5 0 1 1 14 9.5 4.49 4.49 0 0 1 9.5 14z"/>
          </svg>
        </span>
      </div>
    </div>
  </div>
</form>
```

## Markup — error state

```html
<form class="usa-form">
  <div class="usa-form-group usa-form-group--error">
    <label class="usa-label usa-label--error" for="permit-fee">Permit fee</label>
    <span class="usa-error-message" id="permit-fee-error" role="alert">
      Please enter a valid dollar amount.
    </span>
    <div class="usa-input-group usa-input-group--error">
      <div class="usa-input-prefix" aria-hidden="true">$</div>
      <input
        id="permit-fee"
        class="usa-input"
        type="text"
        name="permit-fee"
        placeholder="0.00"
        aria-describedby="permit-fee-error"
        aria-invalid="true"
      />
    </div>
  </div>
</form>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-form` | Form wrapper. Constrains width, applies vertical spacing between fields. |
| `usa-form-group` | Per-field container. ~24px bottom margin. |
| `usa-form-group--error` | Adds the red left border + spacing for the error state at the group level. |
| `usa-label` | Block label above the field. ~16px semibold, `text-base-darkest`. |
| `usa-label--error` | Label text turns red when the field is in error. |
| `usa-hint` | Small gray helper text (~14px) below the label. |
| `usa-error-message` | Red error message (~14px semibold, color `error`) below the label, with `role="alert"`. |
| `usa-input-group` | Flex container with one shared outlined border around prefix + input + suffix. The visual "single frame". |
| `usa-input-group--error` | Applies red border treatment to the shared frame. |
| `usa-input` | The text input. Loses its own border when inside `usa-input-group` (the group provides the visible frame). |
| `usa-input-prefix` | Affix on the left side of the frame. Inset against a slightly tinted background, vertical divider separating it from the input. `aria-hidden="true"` because it's decorative. |
| `usa-input-suffix` | Same as prefix but on the right side. |
| `usa-icon` | Material Symbols icon wrapper. Use inside `usa-input-prefix` or `usa-input-suffix` for icon affixes (search magnifier, etc.). |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `label` | string | `"Price"` | Visible label |
| `prefix` | string | `"$"` | Text rendered inside `usa-input-prefix`. Empty string = no prefix |
| `suffix` | string | `""` | Text rendered inside `usa-input-suffix`. Empty string = no suffix |
| `hint` | string | `""` | Optional hint above the input |
| `placeholder` | string | `"0.00"` | Input placeholder |
| `disabled` | bool | `false` | Disables the input (affixes appear muted) |
| `error` | bool | `false` | Toggles error state and renders `usa-error-message` |
| `errorMessage` | string | `"This field is required"` | Error text |
| `enableAnalytics` | bool | `false` | Toggle GA attributes (on the input) |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Accessibility

- The `<label>` must associate with the input via `for=`/`id`. Do not put an `aria-label` on the prefix/suffix `<div>` — they are decorative and `aria-hidden="true"`.
- If the affix carries semantic meaning that the visible label doesn't (e.g., the suffix `.gov` clarifies "this is a domain"), echo that meaning in the visible label, the hint, or a separately-rendered text node that *isn't* `aria-hidden`. Screen readers do not announce affix text.
- Hint and error messages must be referenced from the input's `aria-describedby` so they're announced with the field.
- For error state, set `aria-invalid="true"` on the input in addition to applying the `--error` classes.
- For currency, do not rely on the `$` prefix alone for accessibility — say "in U.S. dollars" in the label or hint.

## JS requirements

No JS required. Prefix/suffix is pure CSS — the affixes are static `<div>` elements styled to look attached to the input. Works fully with or without `mdwds-core.js` loaded. (You will still want the CDN CSS for styling.)

## Common mistakes

1. **Putting the prefix or suffix outside `usa-input-group`** — without the group wrapper there's no shared frame; the affix `<div>` floats above the input with no visual connection.
2. **Omitting `aria-hidden="true"` on the affix `<div>`** — screen readers will announce "$" or "lbs" as part of the field value, which is confusing. The semantics belong in the label or hint.
3. **Stacking two prefixes or two suffixes** — only one prefix and one suffix are supported. For combined punctuation (e.g., `+1` country code + phone formatting), use `usa-input-mask` instead.
4. **Forgetting that `usa-input` loses its own border inside `usa-input-group`** — applying a custom border to the input alone with inline CSS will create double borders. The frame is the group's job.
5. **Using an icon without an accessible name where the icon carries meaning** — for a search button, the search behavior should be in a separate `<button>` outside the affix. The affix icon is purely decorative.
6. **Validating the value with the affix included** — the affix is not in `input.value`. Only the user-typed digits/text submit.
