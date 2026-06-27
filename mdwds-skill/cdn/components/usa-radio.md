# usa-radio

USWDS radio buttons — used when the user picks **exactly one** option from a short, mutually exclusive list (2–7 options). Two visual styles: default (round bullet) and tile (a clickable rectangular card with an optional description). All options in a group share the same `name` attribute, and selecting one automatically deselects the others — that's how `<input type="radio">` works natively, no JS needed.

Use this for single-choice questions on Maryland.gov pages; the CDN themes the selected state to Maryland blue.

## What it looks like

### Default variant

The actual `<input type="radio">` element is **visually hidden** (positioned off-screen for accessibility) — all visual styling comes from the `<label>` next to it. The label renders as the option text with a **circular indicator** to its left:

- **Empty circle** when unselected: a `units(2.5)` (20×20px) circle drawn as a `::before` pseudo-element on the label, with a `theme-input-select-border-width` (~2px) border in `base-dark` (cool gray) and a white fill.
- **Filled circle with a centered dot** when selected: the border becomes Maryland blue (`primary`), and a smaller blue dot sits in the center. Implementation is a box-shadow trick (inset white shadow + inset primary shadow + outer primary shadow) so the circle pattern renders correctly in print as well.
- **Focus ring** (when the input is keyboard-focused): a 2px Maryland blue outline appears around the circle.

Label text uses Source Sans Pro at body size, normal weight, color base-darkest. Labels stack vertically with `margin-top: 12px` (`units(1.5)`) between options. The circle sits 12px left of the label text (`$input-select-margin-right: 1.5` + `$theme-input-select-size: 2.5` = effective padding-left of 4 units = 32px on the label so the circle has room).

Disabled options: text and circle dim to `disabled-dark` gray; cursor is `not-allowed`.

### Tile variant (`usa-radio__input--tile`)

Each option renders as a **rectangular card** with:
- Border: 2px solid `base-light` (light gray) by default; **Maryland blue when selected**.
- Border-radius: `radius("md")` (~4–8px) — softer corners than the default form chrome.
- Padding: 12px top/bottom, 16px right, 40px left (`units(1.5) units(2) units(1.5) units(5)`) to make room for the circle indicator inside the tile.
- The circle indicator is positioned absolutely inside the tile's left padding.
- An optional `<span class="usa-radio__label-description">` renders below the option text as smaller body-2xs gray text — useful for describing each choice ("Standard processing — 4 to 6 weeks", "Expedited — 7 to 10 business days").
- Tiles stack vertically with `margin-top: 8px` between them.

Tile variant is best when the choices need more than a label to be clear, or when you want a more visually substantial selection (e.g., delivery options, service tier picks).

## Variants

| Variant | Visual |
|---|---|
| Default (no modifier) | Circular bullet + label. Stacked vertically. |
| `usa-radio__input--tile` | Rectangular tile card. Optional description below option text. Selected = Maryland blue border. |

## When to use which variant

- **Default radios** → Compact lists of short labels: 2–7 options where each label fits on a single line ("Yes / No / Not sure", "Email / Phone / Mail").
- **Tile radios** → When each option needs a description, or when the choice is visually weighty (delivery speed with cost, service tier, processing time). Tile borders give the selected state more visual presence.

## Default markup

Always wrap a radio group in `<fieldset class="usa-fieldset">` with `<legend class="usa-legend">` — the legend names the question being asked. All inputs in the group share the same `name`.

```html
<form class="usa-form">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">Preferred contact method</legend>

    <div class="usa-radio">
      <input
        class="usa-radio__input"
        id="contact-email"
        type="radio"
        name="contact-method"
        value="email"
        checked
      />
      <label class="usa-radio__label" for="contact-email">Email</label>
    </div>

    <div class="usa-radio">
      <input
        class="usa-radio__input"
        id="contact-phone"
        type="radio"
        name="contact-method"
        value="phone"
      />
      <label class="usa-radio__label" for="contact-phone">Phone</label>
    </div>

    <div class="usa-radio">
      <input
        class="usa-radio__input"
        id="contact-mail"
        type="radio"
        name="contact-method"
        value="mail"
      />
      <label class="usa-radio__label" for="contact-mail">U.S. Mail</label>
    </div>
  </fieldset>
</form>
```

## Markup — tile variant with descriptions

```html
<form class="usa-form">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">Choose a vehicle title processing option</legend>

    <div class="usa-radio">
      <input
        class="usa-radio__input usa-radio__input--tile"
        id="title-standard"
        type="radio"
        name="title-processing"
        value="standard"
        checked
      />
      <label class="usa-radio__label" for="title-standard">
        Standard processing
        <span class="usa-radio__label-description">
          Title and registration mailed within 4 to 6 weeks. No additional fee.
        </span>
      </label>
    </div>

    <div class="usa-radio">
      <input
        class="usa-radio__input usa-radio__input--tile"
        id="title-expedited"
        type="radio"
        name="title-processing"
        value="expedited"
      />
      <label class="usa-radio__label" for="title-expedited">
        Expedited processing
        <span class="usa-radio__label-description">
          Title and registration mailed within 7 to 10 business days. $20 additional fee.
        </span>
      </label>
    </div>

    <div class="usa-radio">
      <input
        class="usa-radio__input usa-radio__input--tile"
        id="title-instant"
        type="radio"
        name="title-processing"
        value="instant"
      />
      <label class="usa-radio__label" for="title-instant">
        Instant title at MVA branch
        <span class="usa-radio__label-description">
          Pick up your title in person at any MVA branch the same day. $50 additional fee.
        </span>
      </label>
    </div>
  </fieldset>
</form>
```

## Markup — with a disabled option

```html
<form class="usa-form">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">License type</legend>

    <div class="usa-radio">
      <input
        class="usa-radio__input"
        id="lic-resident"
        type="radio"
        name="license-type"
        value="resident"
        checked
      />
      <label class="usa-radio__label" for="lic-resident">Resident fishing license</label>
    </div>

    <div class="usa-radio">
      <input
        class="usa-radio__input"
        id="lic-non-resident"
        type="radio"
        name="license-type"
        value="non-resident"
      />
      <label class="usa-radio__label" for="lic-non-resident">Non-resident fishing license</label>
    </div>

    <div class="usa-radio">
      <input
        class="usa-radio__input"
        id="lic-trapping"
        type="radio"
        name="license-type"
        value="trapping"
        disabled
      />
      <label class="usa-radio__label" for="lic-trapping">Trapping license (currently unavailable)</label>
    </div>
  </fieldset>
</form>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-radio` | Wrapper `<div>` around one input + label pair. Provides positioning context for the circle indicator. |
| `usa-radio__input` | The actual `<input type="radio">`. **Visually hidden** via `sr-only()` — positioned off-screen but focusable for keyboard and announceable by screen readers. All visual state is drawn on the `<label>`. On `:focus`, applies a Maryland blue 2px outline to the label's `::before` circle. |
| `usa-radio__input--tile` | Tile variant: changes the label's `::before` placement and adds a 2px `base-light` border + `border-radius` to the label so the whole option renders as a card. When the input is `:checked`, the border becomes Maryland blue. `margin-top: 8px` (`units(1)`) between tiles. |
| `usa-radio__label` | Styles the option text and draws the circular indicator as a `::before` pseudo-element: 20×20px circle, 2px border in base-dark, white fill (`u-circle($theme-input-select-size)`). Label is Source Sans Pro body size, normal weight, color base-darkest, `padding-left: 32px` so text clears the circle, `margin-top: 12px`. When the matching `usa-radio__input` is `:checked`, the circle fills Maryland blue with a centered dot via box-shadow. Cursor is `pointer`. |
| `usa-radio__label-description` | Block-displayed `<span>` inside the label (tile variant). Smaller text (`font-size: size("ui", "2xs")` ≈ 14px), `margin-top: 8px`, color follows the label. Used for the secondary description line in tile radios. |
| `usa-fieldset` | **Required wrapper** for the group. Resets browser default fieldset chrome (no border, no padding, no margin). |
| `usa-legend` | The question text. Styled like a label — Source Sans Pro body size, color base-darkest. Sits above the radio options. |
| `usa-legend--large` | Larger legend variant: font-size `xl` (~22.4px), bold, with extra top margin. Use for section-level groupings. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `default` \| `tile` | `default` | Visual style |
| `legend` | string | `"Select one historical figure"` | Question text in the `<legend>` |
| `name` | string | `"historical-figures"` | Shared `name` attribute on all radios in the group |
| `options` | array of `{label, value, description?, checked?, disabled?}` | 4 samples | Per-option data. `description` only used in `tile` variant. |
| `ariaDescribedBy` | string | `""` | ID of an element describing the group (typically a hint) |
| `ariaLabel` | string | `""` | Overrides the legend for assistive tech (rare — use only if the legend itself is decorative) |
| `enableAnalytics` | bool | `false` | Add `data-ga-*` attributes to each input |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Accessibility

- **Always wrap in `<fieldset class="usa-fieldset"><legend class="usa-legend">…</legend>`.** The legend is the question; screen readers announce it before each option label. Without it, the user hears "Email, radio button, 1 of 3" with no context for what they're choosing.
- **Each radio has a `<label class="usa-radio__label" for="ID">`** matching the input's `id`. The label's text is the option name. Without the `for`/`id` pair, click-to-focus and the screen-reader name break.
- **All inputs in a group share `name="…"`** — that's how the browser enforces "only one selected at a time".
- **`checked` attribute** on the option that should be pre-selected. Often you should not pre-select anything for a true free choice; pre-selecting biases the user.
- **`required`** on at least one input in the group (or on all — the browser treats them equivalently) prevents the form from submitting without a selection.
- **`disabled` option** removes that choice from the tab order and lightens its color; pair the label text with explanation ("(currently unavailable)") since color alone isn't accessible.
- **Hints:** put a `<div class="usa-hint" id="X">` inside the fieldset, after the legend, and reference it via `aria-describedby="X"` on the `<fieldset>` (or on each input — fieldset is preferred).
- **Errors:** wrap the fieldset (or the form-group containing it) with `usa-form-group--error`, add `aria-invalid="true"` on the fieldset, and use a single `usa-error-message` linked via `aria-describedby` on the fieldset.
- **Keyboard:** Tab to enter the group, arrow keys (↑↓ or ←→) to move within, Space to select. This is native browser behavior — don't override it.
- **Don't visually re-style the circle** with inline CSS. The CDN handles the selected/focus/disabled states with correct contrast.

## JS requirements

No JS required — `<input type="radio">` is a native HTML form control styled by the CDN stylesheet. Browser handles selection, keyboard navigation, and form submission.

## Common mistakes

1. **No `<fieldset>` + `<legend>` wrapper.** Screen readers hear individual labels without the question that ties them together — completely unusable.
2. **Different `name` attributes across the group.** Each radio behaves like its own independent yes/no choice — multiple can be selected. All radios in one group must share the same `name`.
3. **`for`/`id` mismatch** between label and input. Click-to-focus on the visible label fails; screen reader association breaks.
4. **Using radios for multi-select.** If the user can pick more than one, use `usa-checkbox`, not radios.
5. **Pre-selecting an option as "the default"** without good reason. Pre-selection biases the choice and can mask the user accidentally not answering.
6. **Missing `usa-radio` wrapper `<div>`** around each input+label pair. The CSS positions the circle relative to this wrapper.
7. **Adding `disabled` without explaining why** in the label text. Sighted users see gray; AT users hear "dimmed" — neither knows the reason.
8. **Inline `<style>` to recolor the bullet, the focus ring, or the tile border.** The CDN handles all states with Maryland-blue selected color. Overriding produces off-brand styling.
