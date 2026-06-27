# maryland-link

Maryland Design System link element provides typography, focus styling, and variant patterns for hyperlinks on Maryland.gov pages. Most of the time you won't reach for `maryland-link` directly — other components (cards, link collections, highlights) compose it internally. The component exists as the canonical implementation of the Maryland link look, plus a small set of specialty variants (skipnav, document, labelled).

> **Use `maryland-link` for standalone Maryland-themed links and special-purpose variants.** For inline links inside `usa-prose`-wrapped body text, USWDS link styles already apply. For external-link helpers in body text, also consider `usa-link`. For skip navigation, only use the `skipnav` variant.

## What it looks like

The base `maryland-link` is an `<a>` styled by the `typeset-link` mixin: primary-blue color, underlined, focus outline. The `--external` variant appends a 16×16px `open_in_new` icon (current text color, masked SVG) after the label and adds `aria-label="… (external link)"`.

Specialty variants:

- **`skipnav`** — Hidden-until-focused link at the top of every Maryland page. Position absolute, 1×1px clipped when not focused; expands to a visible block on focus.
- **`document`** — Standalone link to a downloadable document. Semibold, with a primary-colored underline at 4% thickness.
- **`document-heading`** — Document link wrapping a heading (e.g., inside a card). Removes underline by default; adds underline on hover.
- **`document-card`** — Same as `document-heading` but suppresses the hover underline (the card's hover handles it).
- **`labelled`** — A label + link pair: small `body-8 semibold ink` label above, normal Maryland link below. Used in contact directories and metadata blocks.

Document variants compose three sub-spans for the document-title typography: `maryland-link__document-title` (the title — body font, semibold), `maryland-link__document-divider` (` - `), `maryland-link__document-format-size` (smaller suffix: "PDF 2.1MB").

When a document title is wrapped in an `<h2>`–`<h6>`, the typography automatically becomes body-7 (18px) / body-9 (22px at mobile-lg+) semibold for the title, with a smaller `body-5` / `body-7` suffix.

## Variants

| Variant | Use for |
|---|---|
| `default` | A standalone Maryland-themed link. |
| `external` (modifier on default) | Off-site link. Adds icon + `aria-label` + `rel="noreferrer"`. |
| `skipnav` | Page skip-navigation link at the top of every page. |
| `document` | Standalone download link with file format + size. |
| `document-heading` | Document link wrapping an `<h2>`–`<h6>`. |
| `document-card` | Same as `document-heading` but no hover underline (used inside `maryland-card`). |
| `labelled` | A label ("Email") above the link ("info@maryland.gov"). |

## When to use

- **`default`** — A standalone link in a sidebar or under a paragraph where you want the canonical Maryland link styling.
- **`external`** — Any off-Maryland.gov link, especially when an icon helps users notice they're leaving the site.
- **`skipnav`** — Always, as the first focusable element on every page. See `cdn/page-shell.md`.
- **`document`** / `document-heading` / `document-card` — Linking to a downloadable document where the format and size matter.
- **`labelled`** — Contact-info pairs (Email, Phone, Office hours).

## Markup — default

```html
<a class="maryland-link" href="/dnr/about">About the Department of Natural Resources</a>
```

## Markup — external

```html
<a class="maryland-link maryland-link--external" href="https://example.com" rel="noreferrer" target="_blank" aria-label="Federal small business resources (external link)">
  Federal small business resources
  <span class="maryland-link__icon" aria-hidden="true"></span>
</a>
```

## Markup — skipnav

```html
<a class="usa-skipnav maryland-link maryland-link--skipnav" href="#main-content">Skip to main content</a>
```

Place this as the **first focusable element** on the page, immediately after `<body>`. The `usa-skipnav` class (USWDS) handles the hidden-until-focused behavior; `maryland-link--skipnav` keeps the focus styling on-brand. Alternative `skipTo: "sidebar"` skips the sidebar nav instead of jumping to main.

## Markup — document

```html
<a class="maryland-link maryland-link--document" href="/dnr/annual-report.pdf">
  <span class="maryland-link__document-title">FY2026 Annual Report</span>
  <span class="maryland-link__document-divider"> - </span>
  <span class="maryland-link__document-format-size">PDF 2.1MB</span>
</a>
```

## Markup — document-heading

```html
<a class="maryland-link--document-heading" href="/dnr/budget.pdf">
  <h3>
    <span class="maryland-link__document-title">FY2026 Budget</span>
    <span class="maryland-link__document-divider"> - </span>
    <span class="maryland-link__document-format-size">PDF 1.3MB</span>
  </h3>
</a>
```

## Markup — document-card

```html
<a class="maryland-link--document-card" href="/dnr/strategic-plan.pdf">
  <h3>
    <span class="maryland-link__document-title">DNR Strategic Plan</span>
    <span class="maryland-link__document-divider"> - </span>
    <span class="maryland-link__document-format-size">PDF 3.4MB</span>
  </h3>
</a>
```

Identical DOM to `document-heading`; only the class differs. Use this when the link sits inside a `maryland-card` so the card's hover state is the sole hover affordance (no underline on link hover).

## Markup — labelled

```html
<div class="maryland-link--labelled">
  <span class="maryland-link__label" id="email-label">Email</span>
  <a class="maryland-link" href="mailto:dnr@maryland.gov" aria-describedby="email-label">dnr@maryland.gov</a>
</div>
```

The `aria-describedby` ties the link to its label so screen readers announce "Email — dnr@maryland.gov".

## What each class does

| Class | Effect |
|---|---|
| `maryland-link` | Base link. Applies the `typeset-link` mixin (primary blue color, underlined, focus outline). |
| `maryland-link--external` | Marker modifier. Combined with `__icon`, renders an `open_in_new` glyph after the label. Display inline. |
| `maryland-link--skipnav` | Skipnav modifier. Combined with USWDS's `.usa-skipnav`, makes the link visually hidden (1×1 clipped) unless focused. On focus, expands to a visible 8/16px-padded block. |
| `maryland-link--document` | Document download style. Semibold, primary-color underline at 4% thickness. Underline disappears on hover. |
| `maryland-link--document-heading` | Document link wrapping a heading. Uses the `typeset-heading-link` mixin (no default underline; underline appears on hover). |
| `maryland-link--document-card` | Same as `--document-heading` but suppresses the hover underline (parent card already handles hover). |
| `maryland-link--labelled` | Wrapper for a label + link pair. Flex column, 4px gap, 16px bottom margin. |
| `maryland-link__icon` | The external-link icon span. 16×16px. `base-darkest` color via `open_in_new` Material Symbols mask. Vertical-align middle. |
| `maryland-link__label` | The label text in the labelled variant. Body font, 16px (`units(2)`) at mobile, body-6 (20px) at mobile-lg+. Semibold. `ink` color. |
| `maryland-link__document-title` | Document title typography. Body font, 18px (or 22px in a heading). Semibold. `ink` color. |
| `maryland-link__document-divider` | The " - " separator between document title and format/size. Same typography as the title. |
| `maryland-link__document-format-size` | "PDF 2.1MB" suffix. body-5 (14px) / body-7 (18px at mobile-lg+) semibold `ink`. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `default` \| `external` \| `skipnav` \| `document` \| `document-heading` \| `document-card` \| `labelled` | `default` | Variant. |
| `label` | string | — | Link text. |
| `href` | string | — | URL. |
| `external` | bool | false | Add the external-link icon, `target="_blank"`, and `aria-label` suffix (default variant only). |
| `target` | `_self` \| `_blank` | `_self` | `target` attribute. |
| `fileType` | `PDF` \| `DOC` \| `DOCX` \| `XLS` \| `XLSX` \| `PPT` \| `PPTX` \| `ZIP` | `PDF` | File format label (document variants). |
| `fileSize` | string | — | File size label (document variants). |
| `description` | string | — | Label text (labelled variant). |
| `skipTo` | `main` \| `sidebar` | `main` | Skipnav target (skipnav variant). |

## Heading level adjustment

`maryland-link` has no heading of its own. For `document-heading`, the inner heading should be `<h3>` (most common — used inside card lists). Adjust based on the surrounding outline.

## Common mistakes

1. **Using `usa-skipnav` without `maryland-link maryland-link--skipnav`** — the link still works, but the focus styling won't match the Maryland design. Combine both.
2. **Forgetting `aria-describedby` on a labelled link** — without it, screen readers announce just the link without context. Pair the link with `id` on the label.
3. **Inline `<style>` to recolor a link** — Maryland links are primary blue by design. If the surrounding context calls for a different color (e.g., white on a blue background), use `set-link-from-bg` mixin contexts (handled by individual components like alerts), not a direct color override.
4. **Mixing `document` and `document-heading` variants** — `document` is a standalone `<a>` block; `document-heading` wraps a `<hN>` element. Match the variant to your DOM structure.
5. **Skipping `aria-label` on external links** — sighted users see the icon; screen-reader users need an "(external link)" suffix in the label.
6. **Multiple skipnav links** — only one per page, and it should be the first focusable element.
