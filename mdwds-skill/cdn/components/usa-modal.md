# usa-modal

A USWDS Modal is a dialog that appears over the page to capture focused user attention — confirmations, in-context forms, destructive-action warnings. MDWDS uses the upstream USWDS modal with one local override: the close button's hover background is forced transparent.

> There is no `maryland-modal`. `usa-modal` is the canonical dialog implementation on Maryland.gov pages.

## What it looks like

When closed: nothing visible. The modal markup sits in the page DOM but is not rendered.

When opened (typically by clicking a trigger button or link with `data-open-modal`):

- A semi-transparent dark overlay (`base-darkest` at ~70% opacity) fills the viewport, dimming the page content behind.
- A centered white panel — the dialog — sits in the middle of the viewport. The default panel is approximately 480px wide and auto-height; the large variant is approximately 720px wide.
- The panel has rounded corners (~4px), a soft shadow under it, and ~32px of padding.
- A close button — an "X" icon in `gray-cool-50` (MDWDS override of the USWDS default) — sits in the top-right corner. On hover the X darkens to `ink` (near-black). The close button is omitted when the modal is `data-force-action`.
- Inside the panel: a heading (`<h2 class="usa-modal__heading">` — Source Sans Pro semibold ~22px), a paragraph of body text, and a footer with a horizontal `usa-button-group`. The footer typically has a primary (`usa-button`) action on the left and an unstyled (`usa-button--unstyled`) cancel-style action to the right.

Focus is trapped inside the dialog while it is open — Tab and Shift+Tab cycle through the focusable elements (close button, primary action, cancel action) without escaping into the dimmed page beneath. Pressing ESC closes the dialog (except in `data-force-action` mode). When the dialog closes, focus returns to the trigger that opened it.

The modal opens via a `data-open-modal` trigger; it closes via any element inside it with `data-close-modal`.

## Variants

| Variant | Class / attribute | Visual |
|---|---|---|
| Default | `usa-modal` | ~480px wide centered dialog. ESC and X-button both dismiss. |
| Large | `usa-modal--lg` | ~720px wide centered dialog. Same behavior, more horizontal room for in-context forms or longer content. |
| Forced action | `data-force-action` (attribute on the trigger and on `usa-modal__close`-omitted markup) | No X close button; ESC does not dismiss. The user must choose one of the explicit action buttons (confirm or cancel) to close the modal. |

## When to use which variant

- **Default** → Confirmation prompts ("Are you sure you want to delete this draft?"), short alerts, anything fitting in a small dialog.
- **`usa-modal--lg`** → In-context forms, multi-paragraph terms-of-service review, anything needing room to breathe.
- **`data-force-action`** → Critical decisions where dismissing with ESC or a click outside would be unsafe — e.g., confirming an irreversible payment, accepting terms before continuing. Use sparingly; forcing the user is friction.

## Default markup

A confirmation modal for submitting a DNR fishing license application:

```html
<a
  href="#confirm-submit-modal"
  class="usa-button"
  aria-controls="confirm-submit-modal"
  data-open-modal
>
  Submit application
</a>

<div
  class="usa-modal"
  id="confirm-submit-modal"
  aria-labelledby="confirm-submit-heading"
  aria-describedby="confirm-submit-description"
>
  <div class="usa-modal__content">
    <div class="usa-modal__main">
      <h2 class="usa-modal__heading" id="confirm-submit-heading">
        Confirm submission of fishing license application
      </h2>
      <p id="confirm-submit-description">
        Once submitted, your application will be reviewed by DNR. Payment will be charged to the card you provided. You cannot edit the application after submission.
      </p>
      <div class="usa-modal__footer">
        <ul class="usa-button-group">
          <li class="usa-button-group__item">
            <button type="button" class="usa-button" data-close-modal>
              Submit application
            </button>
          </li>
          <li class="usa-button-group__item">
            <button
              type="button"
              class="usa-button usa-button--unstyled padding-105 text-center"
              data-close-modal
            >
              Go back
            </button>
          </li>
        </ul>
      </div>
    </div>
    <button
      type="button"
      class="usa-button usa-modal__close"
      aria-label="Close this window"
      data-close-modal
    >
      <svg class="usa-icon" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
        <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z" />
      </svg>
    </button>
  </div>
</div>
```

Key markup points:

- **The trigger is an `<a href="#{modalId}">`** with `data-open-modal` and `aria-controls`. Using an anchor with the modal's `id` as the href is the USWDS pattern — it provides a `:target` CSS fallback if JS is unavailable.
- **The modal `<div class="usa-modal" id="...">`** lives outside the trigger but inside `<body>`. Common practice: place it as the last child of `<main>` or just before `</body>` so it can grow without affecting page layout.
- **Three IDs** are bound together: the modal's `id` matches the trigger's `aria-controls`; `aria-labelledby` points to the heading; `aria-describedby` points to the description.
- **`data-close-modal`** on every element that should dismiss the dialog — the X button, the confirm action, and the cancel action. Without it, that element won't close the modal.

## Markup — large variant

Add `usa-modal--lg` alongside `usa-modal`:

```html
<a href="#renewal-form-modal" class="usa-button" aria-controls="renewal-form-modal" data-open-modal>
  Renew license
</a>

<div
  class="usa-modal usa-modal--lg"
  id="renewal-form-modal"
  aria-labelledby="renewal-heading"
  aria-describedby="renewal-description"
>
  <div class="usa-modal__content">
    <div class="usa-modal__main">
      <h2 class="usa-modal__heading" id="renewal-heading">Renew your fishing license</h2>
      <p id="renewal-description">Confirm your information before completing the renewal.</p>
      <!-- Form fields would go here -->
      <div class="usa-modal__footer">
        <ul class="usa-button-group">
          <li class="usa-button-group__item">
            <button type="button" class="usa-button" data-close-modal>Renew now</button>
          </li>
          <li class="usa-button-group__item">
            <button type="button" class="usa-button usa-button--unstyled padding-105 text-center" data-close-modal>
              Cancel
            </button>
          </li>
        </ul>
      </div>
    </div>
    <button type="button" class="usa-button usa-modal__close" aria-label="Close this window" data-close-modal>
      <svg class="usa-icon" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
        <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z" />
      </svg>
    </button>
  </div>
</div>
```

## Markup — forced action

Two changes from the default: add `data-force-action` to the trigger (the USWDS JS reads it from there to disable ESC and outside-click dismissal), and **omit** the `usa-modal__close` X-button entirely so the user has no way to dismiss except through the explicit action buttons:

```html
<a
  href="#accept-terms-modal"
  class="usa-button"
  aria-controls="accept-terms-modal"
  data-open-modal
  data-force-action
>
  Continue to payment
</a>

<div
  class="usa-modal"
  id="accept-terms-modal"
  aria-labelledby="accept-terms-heading"
  aria-describedby="accept-terms-description"
  data-force-action
>
  <div class="usa-modal__content">
    <div class="usa-modal__main">
      <h2 class="usa-modal__heading" id="accept-terms-heading">Accept terms before continuing</h2>
      <p id="accept-terms-description">
        You must accept Maryland's online services terms before submitting payment. This decision cannot be skipped.
      </p>
      <div class="usa-modal__footer">
        <ul class="usa-button-group">
          <li class="usa-button-group__item">
            <button type="button" class="usa-button" data-close-modal>I accept</button>
          </li>
          <li class="usa-button-group__item">
            <button type="button" class="usa-button usa-button--secondary" data-close-modal>
              Cancel and return
            </button>
          </li>
        </ul>
      </div>
    </div>
    <!-- No usa-modal__close button when data-force-action is set -->
  </div>
</div>
```

In `data-force-action` mode the user cannot ESC or click outside to dismiss. Provide a real "cancel" action button (`usa-button--secondary` is fine) so they aren't trapped.

## What each class does

| Class / attribute | Effect |
|---|---|
| `usa-modal` | Base modal. Hidden by default (display:none). When opened by the USWDS JS, it positions itself centered in the viewport, renders a semi-transparent dark overlay behind, and traps focus inside. |
| `usa-modal--lg` | Wider modal — approximately 720px vs the default ~480px. Same vertical behavior. |
| `usa-modal__content` | Direct child wrapper of `.usa-modal`. Renders the white dialog panel: rounded corners, soft shadow, max-width set per size variant. Holds `__main` plus the close button. |
| `usa-modal__main` | Inner container for heading + body + footer. Sets the internal padding (~32px) and stacking of those children. |
| `usa-modal__heading` | The dialog's heading. Source Sans Pro semibold, ~22px (display heading scale). Bottom-margined to separate from the description. |
| `usa-modal__footer` | Bottom strip holding the action button group. Top-margined from the body text. |
| `usa-modal__close` | The X close button in the top-right corner. **MDWDS override**: background transparent, color `gray-cool-50`; on hover, color shifts to `ink`. Omit this button when using `data-force-action`. |
| `data-open-modal` | Attribute on the trigger element. The USWDS JS treats any element with this attribute as a modal opener and reads `aria-controls` to find the modal to open. |
| `data-close-modal` | Attribute on any element inside the modal (or its `__close` button). Clicking it closes the modal. The X-icon, confirm button, and cancel button all carry this attribute. |
| `data-force-action` | Attribute placed on both the trigger and the modal. Disables ESC-to-close and outside-click-to-close. The X close button should be omitted in the markup. |
| `aria-controls="{modalId}"` | Set on the trigger. Points to the modal's `id`. |
| `aria-labelledby="{headingId}"` | Set on the modal. Points to the `id` of `usa-modal__heading` so screen readers announce the dialog by its heading text. |
| `aria-describedby="{descId}"` | Set on the modal. Points to the `id` of the description paragraph for screen-reader context. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `heading` | string | `"Are you sure you want to continue?"` | Heading text rendered inside `usa-modal__heading`. |
| `description` | string | `"You have unsaved changes that will be lost."` | Body paragraph. Wired to the modal via `aria-describedby`. |
| `triggerLabel` | string | `"Open Modal"` | Label of the trigger anchor/button. |
| `confirmLabel` | string | `"Continue without saving"` | Primary action label. |
| `cancelLabel` | string | `"Go back"` | Cancel action label (renders as `usa-button--unstyled`). |
| `size` | `default` \| `lg` | `default` | When `lg`, applies `usa-modal--lg`. |
| `forcedAction` | bool | `false` | When `true`, omits `usa-modal__close` and the trigger/modal both carry `data-force-action`. |

## Accessibility

- The modal element does **not** carry `role="dialog"` in the USWDS markup — the USWDS JS adds it (along with `aria-modal="true"`) when the dialog opens. Don't set those attributes manually in your HTML; the JS owns them.
- `aria-labelledby` must point to the heading; `aria-describedby` must point to the description paragraph. Both are required so screen readers announce "{Heading} dialog, {description}" on open.
- Focus must move into the dialog when it opens and return to the trigger when it closes. The USWDS JS handles this automatically — do not implement custom focus management.
- Focus is trapped inside the dialog while open: Tab and Shift+Tab cycle through focusable elements (close button, action buttons, any form fields) without escaping to the dimmed background.
- ESC closes the dialog unless `data-force-action` is set. When ESC is suppressed, provide a clearly labeled cancel action so users still have a way out.
- The trigger should be a real `<a>` or `<button>`. Anchors are conventional in USWDS (the `href="#modalId"` provides a `:target` no-JS fallback).
- Modal markup should sit at the same DOM level as the trigger (siblings inside the same container, or both inside `<main>`) — not inside a deeply nested ancestor that has CSS `transform`, `filter`, or `overflow: hidden`, all of which break fixed-position centering.

## JS requirements

`usa-modal` **requires `mdwds-core.js` to function.** Without it:

- The trigger's `data-open-modal` attribute does nothing; clicking the trigger does not open the dialog. (USWDS does provide a CSS `:target` fallback via the `href="#modalId"` pattern, which will display the modal in the page flow — but the result is not a true overlay, has no dark backdrop, and does not center over the viewport.)
- No dark overlay is drawn behind the dialog.
- Focus is not trapped — Tab continues into the page beneath, defeating the modal's purpose.
- ESC does not close the dialog.
- Focus is not returned to the trigger when the dialog closes.
- `role="dialog"` and `aria-modal="true"` are never added, so the dialog isn't announced as a modal by screen readers.
- `data-force-action` has no effect (its enforcement is JS-driven).

If you must support a no-JS audience for a critical confirmation, build that confirmation as a real page (server round-trip) rather than relying on the modal's `:target` fallback.

## Common mistakes

1. **Forgetting `mdwds-core.js`** — the modal sits in the DOM but never opens as a true overlay; focus is not trapped; ESC does nothing.
2. **Mismatched IDs** between trigger's `aria-controls`, modal's `id`, `aria-labelledby`, and `aria-describedby` — the modal opens but is unlabeled or untargeted by the trigger.
3. **Placing the modal inside an element with `transform`, `filter`, or `overflow: hidden`** — these create new stacking/containing contexts that prevent the fixed-positioned overlay from covering the viewport. Move the modal markup out to `<main>` or just before `</body>`.
4. **Including `usa-modal__close` while also setting `data-force-action`** — defeats the purpose of forced action by giving the user a one-click escape. Omit the close button when forcing.
5. **Omitting `data-close-modal` on the action buttons** — clicking "Submit" or "Cancel" runs the button's normal handler but never closes the modal. Both attributes are needed: `data-close-modal` to dismiss, plus whatever click handler completes the action.
6. **Setting `role="dialog"` and `aria-modal="true"` manually on the markup** — the USWDS JS adds these on open. Setting them on the closed modal causes screen readers to announce a hidden dialog.
7. **Triggering the modal from a `<div>` with `onclick`** — use an `<a>` or `<button>`. Non-interactive elements with click handlers aren't keyboard-accessible and break the USWDS pattern.
