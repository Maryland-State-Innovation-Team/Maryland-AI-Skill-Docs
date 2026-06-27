# usa-file-input

USWDS file upload control — used for document uploads (PDF applications, supporting evidence, image uploads). It progressively enhances the native `<input type="file">` with a drag-and-drop "Drag file here or choose from folder" target, accepted-file preview thumbnails (with type-specific icons for PDF, Word, Excel, video), and validation feedback. **Requires the USWDS JS bundle** to enable the drop target, file preview, and drag-state styling — without JS, it falls back to the browser's default file button.

Use this for file uploads on Maryland.gov pages; the CDN themes the drag/hover state to Maryland blue.

## What it looks like

A `usa-file-input` is a **block-level dashed rectangle** (the drop target). With JS loaded, USWDS injects extra DOM around the bare `<input type="file">` to create the rich drop zone — the markup you write is just the `<input>`; the rest is generated.

Rendered visual structure (after JS enhancement):

- **`.usa-file-input__target`** — Dashed rectangle: `border: 1px dashed base-light` (light cool-gray), full width up to `max-width: 480px` (`units("mobile-lg")`), `text-align: center`, font-size `2xs` (~14px). On hover, border-color darkens to `base` (mid-gray). On active drag-over, border-color becomes **Maryland blue (`primary`)** and the inner box background tints to `primary-lighter` (very light blue) — the same blue used for selected states elsewhere.
- **`.usa-file-input__instructions`** — Inner copy: "Drag file here or choose from folder" (default USWDS text). Padding `units(4) units(2)` (32px / 16px). The "choose from folder" portion is wrapped in `.usa-file-input__choose` and styled as a Maryland-blue link.
- **`.usa-file-input__box`** — White background filling the target. Becomes `primary-lighter` blue during drag.
- The actual `<input type="file">` (`.usa-file-input__input`) is positioned absolutely on top of the target, made transparent with `text-indent: -999em`, and given `cursor: pointer` — so clicking anywhere on the box opens the file picker.

After the user picks a file, USWDS injects a **preview row** above the target:
- **`.usa-file-input__preview-heading`** — A flex row showing "Selected file" + a "Change file" link, on a `primary-lighter` blue background, bold text.
- **`.usa-file-input__preview`** for each file — Flex row: a 40×40px (`units(5)`) icon thumbnail on the left, file name on the right, on `primary-lighter` background. The icon is type-specific: `.usa-file-input__preview-image--pdf`, `--word`, `--excel`, `--video`, or `--generic`. For image files, a real thumbnail of the chosen image renders.
- **`.usa-file-input__accepted-files-message`** — When the user picks a file whose extension doesn't match the `accept` attribute, this message ("This is not a valid file type") appears in bold `secondary-dark` red and the target's border switches to `accent-warm` red.

Error state (when `usa-form-group--error` wraps the input): the target's border becomes **2px solid `secondary-dark` red**.

Disabled state (`usa-file-input--disabled`): instructions and "choose" link gray out (`disabled-lighter` background, `disabled-dark` text); cursor becomes `not-allowed`; hover state suppressed.

## Variants

The file input has no built-in visual variant classes. Variation comes from `<input>` attributes and surrounding state classes:

| Modifier / attribute | Effect |
|---|---|
| `multiple` (on `<input>`) | Allow selecting multiple files. Preview shows one row per file. |
| `accept=".pdf,.doc,.docx"` etc. | Restrict allowed file types. Mismatched files trigger the rejection message and red target border. |
| `disabled` (on `<input>`) — combined with `usa-file-input--disabled` on the target after JS init | Greys out the control. |
| `usa-form-group usa-form-group--error` wrapping | Adds the red border on the target plus the standard error-message pattern. |
| `usa-file-input--drag` (added/removed by JS during a drag) | Drives the drag-active styling (blue border + blue-tinted background). Not something you set in HTML. |

## When to use which pattern

- **Single file (default)** → Most common — résumé, photo ID, signed PDF.
- **`multiple`** → Submitting several supporting documents at once. Each preview rendered separately.
- **`accept="image/*"`** → Photo evidence, profile photos, ID images. Browser shows a camera affordance on mobile.
- **`accept=".pdf,.doc,.docx"`** → Document uploads (applications, letters of support).

## Default markup

```html
<form class="usa-form">
  <div class="usa-form-group">
    <label class="usa-label" for="application-upload">Upload your completed application</label>
    <div class="usa-hint" id="application-hint">
      Select a PDF, Word, or text file smaller than 20 MB
    </div>
    <input
      id="application-upload"
      class="usa-file-input"
      type="file"
      name="application-upload"
      accept=".pdf,.doc,.docx,.txt"
      aria-describedby="application-hint"
      required
    />
  </div>
</form>
```

## Markup — multiple files

```html
<form class="usa-form">
  <div class="usa-form-group">
    <label class="usa-label" for="supporting-docs">Supporting documents</label>
    <div class="usa-hint" id="docs-hint">
      Upload any documents that support your permit application. You can attach several at once.
    </div>
    <input
      id="supporting-docs"
      class="usa-file-input"
      type="file"
      name="supporting-docs"
      multiple
      accept=".pdf,.doc,.docx,.jpg,.png"
      aria-describedby="docs-hint"
    />
  </div>
</form>
```

## Markup — image only

```html
<form class="usa-form">
  <div class="usa-form-group">
    <label class="usa-label" for="vehicle-photo">Photo of the damaged vehicle</label>
    <div class="usa-hint" id="photo-hint">
      JPG, PNG, or GIF. Maximum 5 MB.
    </div>
    <input
      id="vehicle-photo"
      class="usa-file-input"
      type="file"
      name="vehicle-photo"
      accept="image/*"
      aria-describedby="photo-hint"
      required
    />
  </div>
</form>
```

## Markup — error state

```html
<form class="usa-form">
  <div class="usa-form-group usa-form-group--error">
    <label class="usa-label usa-label--error" for="required-doc">Upload required document</label>
    <div class="usa-hint" id="doc-hint">PDF or Word document only</div>
    <span class="usa-error-message" id="doc-err" role="alert">
      You must upload a valid document to continue
    </span>
    <input
      id="required-doc"
      class="usa-file-input"
      type="file"
      name="required-doc"
      accept=".pdf,.doc,.docx"
      aria-describedby="doc-hint doc-err"
      aria-invalid="true"
      required
    />
  </div>
</form>
```

## Markup — disabled

```html
<form class="usa-form">
  <div class="usa-form-group">
    <label class="usa-label" for="locked-upload">Upload a file</label>
    <div class="usa-hint" id="locked-hint">Uploads are paused while your application is under review</div>
    <input
      id="locked-upload"
      class="usa-file-input"
      type="file"
      name="locked-upload"
      disabled
      aria-describedby="locked-hint"
    />
  </div>
</form>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-file-input` | Block, full-width up to `max-width: 480px` (`units($theme-input-max-width)`). After USWDS JS init, USWDS wraps the `<input>` with the rich drop-target DOM (the classes below). On the bare `<input type="file">`, also sets `border: none`, `margin-top: 8px`, `padding-left: 0`, `padding-top: 0.2rem` so the native button (when present) sits cleanly under the label. |
| `usa-file-input__target` | The dashed-border drop zone. `border: 1px dashed base-light`, white background, full-width, centered text, font-size `2xs`. Hover darkens border to `base`. |
| `usa-file-input__instructions` | The "Drag file here or choose from folder" copy block. `padding: 32px 16px`. `pointer-events: none` so clicks pass through to the input behind. |
| `usa-file-input__choose` | The clickable "choose from folder" text inside the instructions, styled as a Maryland-blue link (regular weight). |
| `usa-file-input__box` | White background layer behind the instructions; becomes `primary-lighter` during drag. Absolute-positioned fill of the target. |
| `usa-file-input__input` | The hidden-but-positioned `<input type="file">` overlaying the target. `cursor: pointer`, `text-indent: -999em` to hide the native button label. Click anywhere on the target = open file picker. |
| `usa-file-input--drag` | Added by JS when a file is dragged over the target. Switches border to `primary` (Maryland blue) and box background to `primary-lighter`. **Don't apply manually.** |
| `usa-file-input--disabled` | Added by JS when the underlying `<input disabled>`. Instructions and "choose" link become `disabled-dark` on `disabled-lighter` background; cursor `not-allowed`; hover suppressed. |
| `usa-file-input__preview-heading` | The "Selected file" row above the previews. Flex row on `primary-lighter` background, bold text, includes a "Change file" link. |
| `usa-file-input__preview` | One row per selected file: 40×40px icon on the left + file name on the right, on `primary-lighter` background. |
| `usa-file-input__preview-image` | The 40×40px (`units(5)`) thumbnail. `object-fit: contain` for real images. |
| `usa-file-input__preview-image--pdf` | PDF icon background SVG. |
| `usa-file-input__preview-image--word` | Word doc icon background SVG. |
| `usa-file-input__preview-image--excel` | Excel doc icon background SVG. |
| `usa-file-input__preview-image--video` | Video file icon background SVG. |
| `usa-file-input__preview-image--generic` | Generic file icon for unknown types. |
| `usa-file-input__preview-image.is-loading` | A spinner SVG shown while the image preview is being generated. |
| `usa-file-input__accepted-files-message` | The "not a valid file type" rejection message. Bold; becomes `secondary-dark` red when shown. |
| `has-invalid-file` (on `__target`) | Added by JS when the picked file doesn't match `accept`. Target border switches to `accent-warm`. |
| `usa-form-group--error` (on the wrapper) | Forces the target's border to **2px solid `secondary-dark` red**. |
| `usa-label` / `usa-label--error` / `usa-hint` / `usa-error-message` / `usa-form-group` | Same behavior as on other form controls — see `cdn/components/usa-form.md`. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `label` | string | `"Upload a file"` | Label text |
| `hint` | string | `"Select PDF, Word, or text files smaller than 20MB"` | Optional hint copy |
| `multiple` | bool | `false` | Allow multiple files |
| `accept` | string | `".pdf,.doc,.docx,.txt"` | Comma-separated extensions or MIME types |
| `disabled` | bool | `false` | Disable the input |
| `error` | bool | `false` | Show error state (adds `usa-form-group--error` etc.) |
| `errorMessage` | string | `"This field is required"` | Error message text |
| `enableAnalytics` | bool | `false` | Add `data-ga-*` attributes |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Accessibility

- **Always pair with `<label class="usa-label" for="ID">`.** The label is the field name announced by screen readers.
- **`accept` attribute** restricts the file picker's default filter but **doesn't enforce** the rule on the client — server-side validation is still required. Visually, USWDS does mark a mismatch with the rejection message and red target border.
- **`multiple`** lets users pick more than one file in one operation. The hint should make this clear ("You can select multiple files at once").
- **Hints:** `<div class="usa-hint" id="X">` describing accepted types, max size, and any naming conventions. Wire to the input via `aria-describedby="X"`.
- **Errors:** wrap in `usa-form-group--error`, link `usa-error-message` via `aria-describedby` (space-separated with the hint id), set `aria-invalid="true"`. Use `role="alert"` so screen readers announce the error on insertion.
- **Drag-and-drop is a progressive enhancement** — keyboard users tab into the input and press Enter/Space to open the file picker. Don't disable keyboard access.
- **File size limits** — there's no HTML attribute for max file size. Validate client-side via JS (and server-side always). Mention the limit in the hint.
- **The visible drop target is decorative** — assistive tech focuses the underlying `<input>`. Don't make the target itself focusable.

## JS requirements

**USWDS JS is required** for the drop target, file previews, drag-state styling, and accepted-files validation message. Without it, the input falls back to the browser's default "Choose file" button — functional but visually plain. On a CDN-built page, the standard MDWDS JS bundle (`mdwds-core.js` plus the USWDS init) handles initialization automatically.

If you're embedding this in a non-MDWDS host, ensure the USWDS file-input module is loaded before the input is rendered, or call `window.uswdsFileInput.init()` after dynamic insertion.

## Common mistakes

1. **Missing `<label class="usa-label">`** — the field is unnameable. Even with a placeholder-style heading inside the target, screen readers need the explicit label.
2. **`accept` used as the only validation** — `accept` filters the OS file picker but doesn't reject manually-selected files (and never restricts size). Always validate on the server.
3. **`accept` written with wildcards browsers don't understand** — use either MIME types (`image/*`, `application/pdf`) or extensions (`.pdf`, `.docx`). Don't mix in glob patterns like `*.pdf`.
4. **Error not linked via `aria-describedby`.** Sighted users see the red target border; AT users hear nothing about what's wrong.
5. **Hint omits file-size limit** — users only learn the file is too big after trying to upload. State the limit in the hint up front.
6. **Disabling the input via CSS instead of the `disabled` attribute.** Without the attribute, the field is still submittable and focusable. Use `disabled` on the `<input>`.
7. **Inline `<style>` to recolor the dashed border or the drag-state background.** The CDN handles all states (Maryland blue on drag, red on error, gray on disabled). Overriding produces off-brand styling.
8. **Forgetting to load the USWDS JS** in a non-MDWDS host. The styled target disappears and you're left with the browser's plain file button.
