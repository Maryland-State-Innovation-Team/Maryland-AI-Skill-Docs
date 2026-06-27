# usa-checkbox

USWDS checkboxes — used when the user can select **zero, one, or many** options from a list, or to confirm a single boolean ("I agree to the terms"). Two visual styles: default (square check) and tile (clickable rectangular card with optional description). Visually similar to `usa-radio` but with a square indicator and an independent checked state per option — no shared `name`-based mutual exclusivity.

Use this for multi-select and boolean inputs on Maryland.gov pages; the CDN themes the checked state to Maryland blue.

## What it looks like

### Default variant

The actual `<input type="checkbox">` element is **visually hidden** (`sr-only`) — all visual styling is on the `<label>` next to it. The label renders option text with a **square indicator** to its left:

- **Empty square** when unchecked: a `units(2.5)` (20×20px) square drawn as a `::before` pseudo-element on the label, with a `theme-input-select-border-width` (~2px) border in `base-dark`, white fill, and a small border-radius (`radius("sm")` ≈ 2px) — slightly rounded corners.
- **Filled blue square with a white checkmark** when checked: the square fills with Maryland blue (`primary`) and shows a white checkmark SVG centered inside (12×12px / `units(1.5)`). In print mode, falls back to a `\2714` heavy check mark character.
- **Focus ring** when keyboard-focused: 2px Maryland blue outline around the square.

Label text uses Source Sans Pro at body size, normal weight, color base-darkest. Options stack vertically with `margin-top: 12px` (`units(1.5)`) between them. The square sits 12px left of the text.

### Tile variant (`usa-checkbox__input--tile`)

Each option renders as a **rectangular card**:
- Border: 2px solid `base-light` by default; **Maryland blue when checked**.
- Border-radius: `radius("md")` — softer than the default chrome.
- Padding: 12px top/bottom, 16px right, 40px left to clear the square indicator inside.
- Optional `<span class="usa-checkbox__label-description">` renders below the option text as smaller, muted helper copy.
- Tiles stack with `margin-top: 8px`.

Tile variant is best when each option needs a description, or when you want the multi-select to feel like a substantive choice (e.g., service add-ons, notification preferences).

## Variants

| Variant | Visual |
|---|---|
| Default (no modifier) | Square check + label. Stacked vertically. |
| `usa-checkbox__input--tile` | Rectangular tile card. Optional description below option text. Checked = Maryland blue border. |

## When to use which variant

- **Default checkboxes** → Compact lists of short labels (newsletter preferences, applicable counties, agreement boxes).
- **Tile checkboxes** → When each option needs descriptive text (service add-ons with fees, accessibility accommodations with details).
- **Single boolean** (one checkbox, "I agree…") → Always default — no need for a tile for a binary toggle.

## Default markup

Wrap a checkbox group in `<fieldset class="usa-fieldset">` with `<legend class="usa-legend">`. For a true multi-select, give each input the **same `name`** (the form submits the values as an array) or distinct `name`s if each is an independent boolean.

```html
<form class="usa-form">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">Which Maryland services interest you?</legend>

    <div class="usa-checkbox">
      <input
        class="usa-checkbox__input"
        id="svc-parks"
        type="checkbox"
        name="services"
        value="parks"
        checked
      />
      <label class="usa-checkbox__label" for="svc-parks">State parks &amp; recreation</label>
    </div>

    <div class="usa-checkbox">
      <input
        class="usa-checkbox__input"
        id="svc-licenses"
        type="checkbox"
        name="services"
        value="licenses"
      />
      <label class="usa-checkbox__label" for="svc-licenses">Hunting and fishing licenses</label>
    </div>

    <div class="usa-checkbox">
      <input
        class="usa-checkbox__input"
        id="svc-vehicle"
        type="checkbox"
        name="services"
        value="vehicle"
      />
      <label class="usa-checkbox__label" for="svc-vehicle">Vehicle registration and titling</label>
    </div>

    <div class="usa-checkbox">
      <input
        class="usa-checkbox__input"
        id="svc-health"
        type="checkbox"
        name="services"
        value="health"
      />
      <label class="usa-checkbox__label" for="svc-health">Health programs and benefits</label>
    </div>
  </fieldset>
</form>
```

## Markup — single confirmation checkbox

For a single boolean (agreement, opt-in), you still need a label — but the `<fieldset>` + `<legend>` wrapping is optional if the checkbox stands alone.

```html
<form class="usa-form">
  <div class="usa-checkbox">
    <input
      class="usa-checkbox__input"
      id="agree-terms"
      type="checkbox"
      name="agree-terms"
      value="yes"
      required
    />
    <label class="usa-checkbox__label" for="agree-terms">
      I have read and agree to the Maryland Department of Natural Resources licensing terms
    </label>
  </div>

  <button type="submit" class="usa-button">Submit</button>
</form>
```

## Markup — tile variant with descriptions

```html
<form class="usa-form">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">Choose notification preferences</legend>

    <div class="usa-checkbox">
      <input
        class="usa-checkbox__input usa-checkbox__input--tile"
        id="notify-email"
        type="checkbox"
        name="notify"
        value="email"
        checked
      />
      <label class="usa-checkbox__label" for="notify-email">
        Email
        <span class="usa-checkbox__label-description">
          Permit renewal reminders, program updates, and policy changes sent to your inbox.
        </span>
      </label>
    </div>

    <div class="usa-checkbox">
      <input
        class="usa-checkbox__input usa-checkbox__input--tile"
        id="notify-sms"
        type="checkbox"
        name="notify"
        value="sms"
      />
      <label class="usa-checkbox__label" for="notify-sms">
        Text message
        <span class="usa-checkbox__label-description">
          Urgent alerts only (closures, emergency notices). Message and data rates may apply.
        </span>
      </label>
    </div>

    <div class="usa-checkbox">
      <input
        class="usa-checkbox__input usa-checkbox__input--tile"
        id="notify-mail"
        type="checkbox"
        name="notify"
        value="mail"
      />
      <label class="usa-checkbox__label" for="notify-mail">
        U.S. Mail
        <span class="usa-checkbox__label-description">
          Paper renewal notices mailed to the address on file. Slower than electronic options.
        </span>
      </label>
    </div>
  </fieldset>
</form>
```

## Markup — checklist styling

The MDWDS CDN forwards the upstream `usa-checklist` package. This gives you a tighter, list-style checkbox layout for completion checklists (e.g., "items needed for your application"). Use the standard `usa-checkbox` markup; the styling is applied through the same classes.

## What each class does

| Class | Effect |
|---|---|
| `usa-checkbox` | Wrapper `<div>` around one input + label pair. Provides positioning context for the square indicator. |
| `usa-checkbox__input` | The actual `<input type="checkbox">`. **Visually hidden** via `sr-only()`. All visual state lives on the `<label>`. On `:focus`, applies a 2px Maryland blue outline to the label's `::before` square. |
| `usa-checkbox__input--tile` | Tile variant: changes the label's `::before` placement and adds a 2px `base-light` border + `border-radius` to the label so the whole option renders as a card. When checked, the border becomes Maryland blue. `margin-top: 8px` between tiles. |
| `usa-checkbox__label` | Styles the option text and draws the square indicator as `::before`: 20×20px square (`u-square($theme-input-select-size)`), 2px border in base-dark, white fill, slight border-radius (`radius("sm")`). When the matching input is `:checked`, the square fills Maryland blue and shows a centered white check (12×12px SVG background). `padding-left: 32px` clears the indicator. Cursor `pointer`. |
| `usa-checkbox__label-description` | Block `<span>` inside the label (tile variant). Smaller text (`size("ui", "2xs")` ≈ 14px), `margin-top: 8px`. Used for secondary description line. |
| `usa-fieldset` | **Required wrapper** for grouped checkboxes. Resets browser default fieldset chrome. |
| `usa-legend` | The group question. Source Sans Pro body size, color base-darkest. |
| `usa-legend--large` | Larger legend (font-size xl, bold) for section-level groupings. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `default` \| `tile` | `default` | Visual style |
| `legend` | string | `"Select any historical figure"` | Group question text |
| `fieldName` | string | `"historical-figures"` | The shared `name` attribute (kebab-cased) for all options in the group |
| `options` | array of `{label, value, description?, checked?, disabled?}` | 4 samples | Per-option data. `description` only used in `tile` variant. |
| `enableAnalytics` | bool | `false` | Add `data-ga-*` attributes |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Accessibility

- **Group related checkboxes in `<fieldset class="usa-fieldset"><legend class="usa-legend">…</legend>`.** The legend names the question being answered; screen readers announce it before each option.
- **Single boolean checkbox** (terms-of-service style) doesn't strictly need a fieldset, but it must have a clearly written `<label>` describing exactly what checking the box agrees to.
- **Each input has a `<label class="usa-checkbox__label" for="ID">`** matching the input's `id`. Label text **is** the option name — don't put it elsewhere.
- **For multi-select groups**, all inputs share `name="…"` and the form submits the checked values as `name=value1&name=value2&...`. For independent booleans, give each its own unique `name`.
- **`required`** on a checkbox forces it to be checked before submit — useful for "I agree" boxes. For multi-select groups, `required` doesn't enforce "at least one" — that requires JS validation.
- **Disabled options** dim to gray. Pair with text in the label ("(currently unavailable)") because color alone isn't accessible.
- **Hints:** `<div class="usa-hint" id="X">` after the legend, link via `aria-describedby="X"` on the fieldset.
- **Errors:** wrap the fieldset in `usa-form-group--error`, link a single `usa-error-message` via `aria-describedby` on the fieldset, set `aria-invalid="true"` on the fieldset.
- **Keyboard:** Tab to focus each checkbox, Space to toggle. Native browser behavior — don't override.
- **Don't rely on color alone** to indicate checked state; the white checkmark inside the blue square does most of the work, but the change in shape/symbol is what makes it accessible.

## JS requirements

No JS required — `<input type="checkbox">` is a native HTML form control styled by the CDN stylesheet.

## Common mistakes

1. **No `<fieldset>` + `<legend>` around a checkbox group.** Screen readers hear individual labels with no context for what the user is being asked. Mandatory for groups of 2+ related options.
2. **Using checkboxes for mutually exclusive choices.** If only one can be picked, use `usa-radio` instead.
3. **`for`/`id` mismatch** between label and input. Click-to-focus on the visible label fails; screen-reader association breaks.
4. **All checkboxes in a group given different `name` attributes** when you wanted them grouped. The form submits each as a separate boolean field — usually fine, but if your backend expects a single multi-value field, share the name.
5. **Missing `<label>` text** ("I agree" with no text — just the checkbox). The user has nothing to read and nothing for AT to announce.
6. **Pre-checking marketing opt-ins.** Many jurisdictions and accessibility guidelines treat this as dark-pattern. Pre-check only when the value is a sensible default for the user's task.
7. **Adding `disabled` without explaining why** in the label text. Color dim alone isn't accessible — name the reason.
8. **Inline `<style>` to recolor the check, the focus ring, or the tile border.** The CDN handles all states. Overriding produces off-brand styling.
