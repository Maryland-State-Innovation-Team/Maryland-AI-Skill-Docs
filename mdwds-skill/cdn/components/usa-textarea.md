# usa-textarea

The USWDS multi-line text input — for free-form input longer than a single sentence: messages, descriptions, "tell us more" prompts, explanations, additional notes. Visually it shares the same border, font, padding, and focus ring as `usa-input`, but it's taller (defaults to 160px) and resizable.

Use this for long-form text on Maryland.gov pages; the CDN themes USWDS form colors to Maryland blue (focus ring, error border).

## What it looks like

A `usa-textarea` is a rectangular text area with a **1px solid `base-dark` (cool gray) border**, no border-radius (square corners), white background, and `color: ink` (near-black) typed text. Default height is **160px** (`units("card")`); the user can drag the bottom-right corner to resize vertically (the browser handles this — no JS). Internal padding matches `usa-input` at 8px (`units(1)`) all around; the field sits 8px below its associated `<label class="usa-label">`. Font is Source Sans Pro Web at body size with the input line-height — so multiple lines of typed text wrap naturally.

`rows` attribute controls the initial height in lines (overriding the CSS-set 160px when set higher); `cols` is generally not needed because the textarea fills its container up to the `max-width: 480px` (`units("mobile-lg")`) that USWDS sets. Inside a `<form class="usa-form">`, this per-textarea max-width is cleared so the form's max-width (320px default, 480px with `usa-form--large`) governs.

Focus, disabled, and error states match `usa-input`:
- Focus → 2px Maryland blue outline, 2px offset.
- Disabled → `disabled-lighter` background, `disabled-dark` text, `not-allowed` cursor.
- Validation states reuse `usa-input--error` / `usa-input--success` patterns conceptually, but for textareas the standard pattern is to wrap in `usa-form-group--error` and apply the error border styling at the form-group level.

## Variants

The textarea has no built-in variant classes of its own. Variation is done through:

- The `rows` attribute on `<textarea>` (sets initial visible line count).
- The wrapping `<form class="usa-form">` / `usa-form--large` for max-width control.
- Pairing with `usa-character-count` for a live character-count helper (separate component).

## Default markup

```html
<form class="usa-form">
  <label class="usa-label" for="message">Message</label>
  <textarea
    class="usa-textarea"
    id="message"
    name="message"
    rows="5"
  ></textarea>
</form>
```

## Markup — with hint

```html
<form class="usa-form">
  <label class="usa-label" for="incident-details">Describe the incident</label>
  <div class="usa-hint" id="incident-hint">
    Include the date, location, and any vehicle or vessel registration numbers
  </div>
  <textarea
    class="usa-textarea"
    id="incident-details"
    name="incident-details"
    rows="6"
    aria-describedby="incident-hint"
    required
  ></textarea>
</form>
```

## Markup — with error

```html
<form class="usa-form">
  <div class="usa-form-group usa-form-group--error">
    <label class="usa-label usa-label--error" for="comments">Additional comments</label>
    <span class="usa-error-message" id="comments-err" role="alert">
      Comments cannot exceed 2,000 characters
    </span>
    <textarea
      class="usa-textarea"
      id="comments"
      name="comments"
      rows="8"
      maxlength="2000"
      aria-describedby="comments-err"
      aria-invalid="true"
    ></textarea>
  </div>
</form>
```

## Markup — in a contact form (MDH example)

```html
<form class="usa-form usa-form--large">
  <label class="usa-label" for="contact-name">Full name</label>
  <input class="usa-input" id="contact-name" name="name" type="text" autocomplete="name" required />

  <label class="usa-label" for="contact-email">Email address</label>
  <input class="usa-input" id="contact-email" name="email" type="email" autocomplete="email" required />

  <label class="usa-label" for="question">Your question for the Maryland Department of Health</label>
  <div class="usa-hint" id="question-hint">Please provide as much detail as you can</div>
  <textarea
    class="usa-textarea"
    id="question"
    name="question"
    rows="6"
    aria-describedby="question-hint"
    required
  ></textarea>

  <button type="submit" class="usa-button">Send</button>
</form>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-textarea` | Base styles: 1px solid `base-dark` border, square corners, white background, `color: ink` text, 8px padding all around, Source Sans Pro at body size with input line-height. **Height: 160px** (`units("card")`) — overridable by `rows` attribute. `max-width: 480px` outside a form (cleared inside `usa-form`). Disabled: `disabled-lighter` background, `disabled-dark` text. |
| `usa-label` | Styles the `<label>`: Source Sans Pro at body size, color base-darkest, `margin-top: 24px`. Sits 8px above the textarea. |
| `usa-label--error` | Bold weight, `margin-top: 0`. |
| `usa-hint` | Helper text below the label, color base (mid-gray). Wire to the textarea via `aria-describedby`. |
| `usa-error-message` | Bold red message. `padding-y: 4px`, `role="alert"` so dynamic insertion is announced. |
| `usa-form-group` | Wraps label + hint + textarea + error. `margin-top: 24px`. |
| `usa-form-group--error` | Adds 4px red left border, `padding-left: 16px`, and a left shift at desktop to align the red border with the form's left edge. |

The textarea inherits the same `border: 1px solid base-dark` and `:focus` outline behavior as `usa-input`, so visual updates to inputs apply to textareas automatically.

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `label` | string | `"Text area label"` | Visible label text |
| `id` | string | `"input-type-textarea"` | Textarea id, matches label's `for` |
| `name` | string | `"input-type-textarea"` | Form submission key |
| `placeholder` | string | `""` | Optional — never use as the only label |
| `rows` | number | `5` | Initial visible line count |
| `ariaLabel` | string | `""` | Only when label is hidden (rare) |
| `ariaDescribedBy` | string | `""` | ID of a hint or error message |

## Accessibility

- **Always pair the textarea with `<label class="usa-label" for="ID">`** matching the textarea's `id`. Placeholder text is not a label.
- **Set a meaningful `rows`** so the visible area matches the expected answer length. A 1-row textarea looks like an input but doesn't auto-grow; a 12-row textarea suggests an essay. 4–8 is typical.
- **Hints:** `<div class="usa-hint" id="X">…</div>` + `aria-describedby="X"` on the textarea. Use for input format expectations, length guidance, or what kinds of info to include.
- **Character limits:** set `maxlength` to enforce; pair with `usa-character-count` (separate component, requires USWDS JS) for a live countdown announced to screen readers via `aria-live`.
- **Errors:** `aria-invalid="true"`, `aria-describedby` pointing at the error id, `role="alert"` on `usa-error-message`. Don't rely on color alone — the red border, bold message, and `aria-invalid` together carry the meaning.
- **Resize handle** is built into browsers; don't disable it via `resize: none` unless there's a hard layout reason — users with limited dexterity benefit from being able to enlarge the input area.
- **Spell-check** is on by default (`spellcheck="true"`). For inputs that aren't natural language (license numbers, codes), set `spellcheck="false"`.

## JS requirements

No JS required — `<textarea>` is a native HTML form control styled by the CDN stylesheet.

For a live character counter, see `usa-character-count` — that requires the USWDS JS bundle.

## Common mistakes

1. **Using `usa-input` (a `<input type="text">`) for long-form input.** A single-line input forces the user to scroll horizontally inside a 40px-tall field. Use `usa-textarea` whenever the expected answer is longer than a phrase.
2. **`for`/`id` mismatch** between `<label>` and `<textarea>`. Click-to-focus and screen-reader association both break.
3. **Missing `name` attribute** — the value won't submit with the form.
4. **Placeholder as the only label.** Disappears on input, unreliable for assistive tech.
5. **Error message not linked** via `aria-describedby`. Screen-reader users hear the field name without the error.
6. **`rows` set too small for the task** (e.g., `rows="2"` for a "describe the incident" prompt). The visible height should suggest the expected answer length.
7. **Disabling browser resize via inline `style="resize: none"`.** Robs users who want to see more of their text. Trust the default.
8. **Inline `<style>` for border color, focus ring, or padding.** The CDN handles all of these; overriding produces off-brand styling.
