# usa-character-count

The USWDS character count is an `<input>` or `<textarea>` paired with a live "characters left" message below it. The counter updates as the user types and switches to an error state when the limit is exceeded. Use it for any free-text field with a hard length cap: short answer questions, public comment forms, agency-feedback fields.

> Use this for length-limited text input on Maryland.gov pages. There is no `maryland-character-count` — MDWDS inherits the USWDS component with Maryland color tokens. Wrap either a `usa-input` (single line) or `usa-textarea` (multi-line) — both are supported.

## What it looks like

The field above is a standard `usa-input` (single-line, ~48px tall) or `usa-textarea` (multi-line, ~12rem tall by default) — white background, thin gray border, square corners, body-size text.

Below the field, ~8px of vertical space, sits the counter message: small gray text (`usa-character-count__message`, ~14px, color `base`) reading "{N} characters allowed" before typing, then switching to a live "{N} characters left" countdown while under the limit, and to "{N} characters over limit" (in red, color `error`) once the user types past the cap.

When the limit is exceeded:
- The counter message turns red and switches wording to "over limit".
- The input's border turns red (`usa-input--error` is added automatically by the JS).
- Screen readers receive the new message because the counter span has `aria-live="polite"`.

The `maxlength` attribute is set to the cap *and* enforces a hard browser-level cap — typing past it is normally blocked. The "over limit" state appears mostly through paste actions or after a programmatic value change.

## Default markup — textarea (200-char limit)

```html
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <label class="usa-label" for="comment">
    Public comment on the proposed regulation
  </label>
  <span class="usa-hint" id="comment-hint">
    Share your views with the Maryland Department of the Environment.
  </span>
  <div class="usa-character-count" data-maxlength="200">
    <textarea
      class="usa-textarea usa-character-count__field"
      id="comment"
      name="comment"
      maxlength="200"
      aria-describedby="comment-hint comment-message"
    ></textarea>
    <span
      id="comment-message"
      class="usa-character-count__message"
      aria-live="polite"
    >
      200 characters allowed
    </span>
  </div>
</form>
```

## Markup — single-line input (50-char limit)

```html
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <label class="usa-label" for="username">Username</label>
  <span class="usa-hint" id="username-hint">Choose a unique username (max 50 characters).</span>
  <div class="usa-character-count" data-maxlength="50">
    <input
      class="usa-input usa-character-count__field"
      id="username"
      name="username"
      type="text"
      maxlength="50"
      aria-describedby="username-hint username-message"
    />
    <span
      id="username-message"
      class="usa-character-count__message"
      aria-live="polite"
    >
      50 characters allowed
    </span>
  </div>
</form>
```

## Markup — pre-filled value

```html
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <label class="usa-label" for="bio">Profile bio</label>
  <span class="usa-hint" id="bio-hint">Up to 150 characters.</span>
  <div class="usa-character-count" data-maxlength="150">
    <textarea
      class="usa-textarea usa-character-count__field"
      id="bio"
      name="bio"
      maxlength="150"
      aria-describedby="bio-hint bio-message"
    >Outreach coordinator at the Maryland Department of Natural Resources.</textarea>
    <span
      id="bio-message"
      class="usa-character-count__message"
      aria-live="polite"
    >
      150 characters allowed
    </span>
  </div>
</form>
```

## Markup — required field

```html
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <label class="usa-label" for="feedback">
    Service feedback
    <abbr title="required" class="usa-hint usa-hint--required">*</abbr>
  </label>
  <span class="usa-hint" id="feedback-hint">Tell us about your MVA visit (max 300 characters).</span>
  <div class="usa-character-count" data-maxlength="300">
    <textarea
      class="usa-textarea usa-character-count__field"
      id="feedback"
      name="feedback"
      maxlength="300"
      required
      aria-describedby="feedback-hint feedback-message"
    ></textarea>
    <span
      id="feedback-message"
      class="usa-character-count__message"
      aria-live="polite"
    >
      300 characters allowed
    </span>
  </div>
</form>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-form` | Form wrapper. Constrains form width and field spacing. |
| `usa-form--large` | Wider variant of `usa-form` (~30rem). |
| `usa-label` | Block label above the field. ~16px semibold, `text-base-darkest`. |
| `usa-hint` | Small gray helper text (~14px) below the label. |
| `usa-hint--required` | Modifier for the asterisk `<abbr>` that marks required fields. |
| `usa-character-count` | Wrapper around the input/textarea + counter. Holds the `data-maxlength` attribute that the JS reads. |
| `usa-character-count__field` | Class on the actual `<input>` or `<textarea>` that the counter is tracking. Applied **in addition** to `usa-input` or `usa-textarea`. |
| `usa-character-count__message` | The live counter span below the field. ~14px, color `base`. Has `aria-live="polite"` so screen readers announce changes. |
| `usa-character-count__message--invalid` | (Applied by JS when the value exceeds `data-maxlength`.) Switches the message text to red (color `error`) and changes the wording to "over limit". |
| `usa-input` | Single-line text input styling: ~48px tall, white, thin gray border, square corners. |
| `usa-textarea` | Multi-line input. ~12rem tall by default, same border/background as `usa-input`, resizable vertically. |
| `usa-input--error` / `usa-textarea--error` | (Applied by JS in over-limit state.) Red border on the field. |
| `data-maxlength` (attr) | The character cap. The JS reads this — it does **not** read the input's `maxlength` attribute. Always set both to the same value. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `label` | string | `"Message"` | Visible label |
| `inputType` | `input` \| `textarea` | `"textarea"` | Single-line vs multi-line |
| `maxLength` | number | `200` | Sets both `data-maxlength` on the wrapper and `maxlength` on the field |
| `hint` | string | `"Enter your message"` | Hint above the field |
| `defaultValue` | string | `""` | Pre-fills the field |
| `required` | bool | `false` | Adds `required` + visible asterisk |
| `enableAnalytics` | bool | `false` | Toggle GA attributes (on the wrapper) |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Accessibility

- The `<label>` must associate with the field via `for=`/`id`. The counter span needs its own `id` and must be referenced from the field's `aria-describedby` so screen readers tie the running count to the input.
- `aria-live="polite"` on the counter span tells assistive tech to announce updates without interrupting. The USWDS JS rate-limits the announcements so users aren't flooded with every keystroke — they hear summary milestones (e.g., "10 characters left").
- The counter is **in addition** to the visible label and hint; it must not replace them.
- For required fields, include both the visible asterisk (`<abbr title="required" class="usa-hint usa-hint--required">*</abbr>`) and the `required` attribute on the input.
- When the over-limit state activates, `usa-input--error` is applied, but you may also want to manage form submission to block submit while the message says "over limit".
- Keep `data-maxlength` and `maxlength` identical so the visible count and the browser's enforcement match.

## JS requirements

**Requires the `mdwds-core.js` bundle loaded** for live counting. Without it: the counter span shows the initial "{N} characters allowed" text and never updates as the user types. The HTML5 `maxlength` attribute still enforces the cap at the browser level (you can't type past it), but the visual countdown and the over-limit error state never appear.

## Common mistakes

1. **Forgetting `mdwds-core.js`** — the counter is frozen at the initial message. Users get no live feedback.
2. **Setting `maxlength` without `data-maxlength`** (or vice versa) — the JS reads `data-maxlength`; the browser enforces `maxlength`. Mismatched values cause the count to disagree with what the user can type.
3. **Missing `usa-character-count__field` class on the input/textarea** — without it the JS can't find the tracked field. The counter never updates.
4. **Omitting `aria-describedby` linkage to the counter** — screen reader users hear no count updates.
5. **Missing `aria-live="polite"` on the counter span** — even with `aria-describedby`, dynamic changes don't trigger announcements without `aria-live`.
6. **Using both `usa-input` and `usa-textarea` classes on the same element** — they're mutually exclusive. Pick the one matching the element type.
7. **Treating the counter as the only validation** — server-side validation must still cap length. Don't trust client behavior alone.
