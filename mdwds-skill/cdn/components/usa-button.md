# usa-button

USWDS button styled with the Maryland color palette. The button is the standard control for actions on every Maryland.gov page — primary CTAs in heroes, secondary actions in card footers, submit buttons in forms, "Apply now" links inside service cards. There is **no `maryland-button`** component; Maryland uses `usa-button` with the CDN-themed colors.

> **There is no `maryland-button`.** All buttons on Maryland.gov pages use `usa-button` plus a variant modifier. The visual styling (Maryland blue primary, etc.) is applied by the CDN stylesheet via the MDWDS color overrides — see `cdn/foundation.md`. See `cdn/component-index.md` for the disambiguation row.

## What it looks like

A standard `usa-button` is a solid rectangular control filled with **Maryland blue** (`primary` → `blue-60v`, approximately `#1A4480`) with **white** text. Text is **semibold** (`font-weight: 600`) in Source Sans Pro at the body font scale 3 (≈17px). Padding is **`units(1) units(2)` = 8px top/bottom, 16px left/right**. Line-height is exactly `1rem`. The border-radius comes from the USWDS `$theme-button-border-radius` token (default `sm` = 2px — a near-square corner, **not** a pill). On hover and focus, the background darkens to `primary-vivid` (`blue-warm-60v`); the focus state also gets the global 2px focus ring with 2px offset.

Each variant changes the fill/text color or the box shape:

- **default (primary)** — Maryland blue background, white text. The strongest visual weight. Use for the **one** primary action on a page or section.
- **`usa-button--secondary`** — Maryland red/cool-red background (`red-cool-50v`), white text. Used for destructive or contrasting actions.
- **`usa-button--accent-cool`** — Light cyan background (`cyan-30v`), dark text. A softer alternative for tertiary actions.
- **`usa-button--accent-warm`** — Gold background (`gold-30v`), dark text. A warm accent option.
- **`usa-button--base`** — Mid-gray background (`gray-cool-50`), white text. Neutral action — "Cancel", "Back".
- **`usa-button--outline`** — Transparent / white fill, **2px inset box-shadow border** in Maryland blue, blue text. Used for the secondary half of a two-button row. Hovers fill with light tint; the background stays white on hover via the MDWDS override.
- **`usa-button--white`** (inverse) — White background, Maryland blue text. **Use only on dark backgrounds** (dark hero, footer). On hover, background fades to `base-lighter` (off-white).
- **`usa-button--black`** — Near-black background (`ink` / `gray-90`), white text. Hover deepens to `base-darker`. Maximum-contrast button.
- **`usa-button--unstyled`** — Removes the box entirely. Renders as a link styled like body text (Maryland blue, underlined). Inherit-only — use when an `<a>` would be semantically wrong but no visual button is desired.

The size modifier:

- **`usa-button--big`** — Increases padding to `units(2) units(3)` (16px / 24px) and font size to scale 5 (≈22px). Used for top-of-page CTAs in heroes.

The disabled state (`disabled` attribute or `usa-button--disabled` class) renders ~50% opacity with no hover effect; cursor changes to `not-allowed`.

## Variants

| Variant | Class | Visual |
|---|---|---|
| Default / primary | `usa-button` | Maryland blue, white text |
| Secondary | `usa-button usa-button--secondary` | Red, white text |
| Accent cool | `usa-button usa-button--accent-cool` | Light cyan, dark text |
| Accent warm | `usa-button usa-button--accent-warm` | Gold, dark text |
| Base | `usa-button usa-button--base` | Gray, white text |
| Outline | `usa-button usa-button--outline` | Transparent fill, blue border + blue text |
| White / inverse | `usa-button usa-button--white` | White fill, blue text (for dark backgrounds) |
| Black | `usa-button usa-button--black` | Near-black, white text |
| Unstyled | `usa-button usa-button--unstyled` | No box — looks like a link |
| Big (size) | add `usa-button--big` | Larger padding + ≈22px font |
| Disabled | `disabled` attribute + `aria-disabled="true"` | Faded, non-interactive |

## When to use which variant

- **Default / primary** — The one most important action in the current section (e.g., "Apply for fishing license", "Submit registration"). Use it sparingly — at most one per visual section.
- **Secondary (red)** — Cancellation, "Remove", or a strongly contrasting secondary option. Not a softer primary; the red carries weight.
- **Accent-cool / accent-warm** — Categorical contrast where neither primary nor base fits. Rare. Don't mix with primary in the same row.
- **Base (gray)** — Neutral non-primary actions like "Back", "Cancel" (non-destructive). Pair with a primary in two-button rows.
- **Outline** — The other half of a two-button row when you want both to read as equal-weight but with the primary still leading. "Back" (outline) + "Continue" (primary) is the canonical pattern.
- **White / inverse** — Use **only** on a dark background (dark hero, footer panel). On a white background it disappears.
- **Black** — Highest contrast on light backgrounds; rare. Reserve for emergency or extra-strong CTAs.
- **Unstyled** — When you semantically need `<button>` (e.g., toggle, JS action) but the design calls for plain link styling.
- **`--big`** — Hero CTAs and other top-of-page primary actions. Don't stack multiple big buttons in the same row.

## Default markup

```html
<button type="button" class="usa-button">Apply for fishing license</button>
```

For navigation (a button that takes the user to another URL), use an `<a>` styled as a button instead — same classes:

```html
<a href="/apply" class="usa-button">Apply for fishing license</a>
```

## Markup — secondary

```html
<button type="button" class="usa-button usa-button--secondary">
  Cancel registration
</button>
```

## Markup — accent-cool

```html
<button type="button" class="usa-button usa-button--accent-cool">
  View on map
</button>
```

## Markup — accent-warm

```html
<button type="button" class="usa-button usa-button--accent-warm">
  Download brochure
</button>
```

## Markup — base

```html
<button type="button" class="usa-button usa-button--base">Back</button>
```

## Markup — outline

```html
<button type="button" class="usa-button usa-button--outline">
  Save draft
</button>
```

Typical two-button row pairing outline with primary:

```html
<div class="usa-button-group">
  <button type="button" class="usa-button usa-button--outline">Back</button>
  <button type="submit" class="usa-button">Continue to payment</button>
</div>
```

## Markup — white (inverse)

```html
<section class="bg-primary-darker padding-y-6">
  <a href="/services" class="usa-button usa-button--white">
    Browse Maryland services
  </a>
</section>
```

## Markup — black

```html
<button type="button" class="usa-button usa-button--black">
  Report an outage
</button>
```

## Markup — unstyled

```html
<button type="button" class="usa-button usa-button--unstyled">
  Show all results
</button>
```

## Markup — big

```html
<a href="/apply" class="usa-button usa-button--big">Apply for benefits</a>
```

## Markup — disabled

```html
<button type="submit" class="usa-button" disabled aria-disabled="true">
  Submit registration
</button>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-button` | Base button. Semibold Source Sans, font-size scale 3 (≈17px), `line-height: 1rem`, padding `8px 16px`, border-radius `radius(sm)` (≈2px), no `margin-inline-end` on last child. Default fill is Maryland blue (`primary` = `blue-60v`) with white text. Hover/focus darkens to `primary-vivid`. |
| `usa-button--secondary` | Background `secondary` (`red-cool-50v`, Maryland red), white text. Hover darkens to `secondary-vivid`. |
| `usa-button--accent-cool` | Background `accent-cool` (`cyan-30v`, light cyan). Dark text for contrast. Hover darkens to `accent-cool-dark`. |
| `usa-button--accent-warm` | Background `accent-warm` (`gold-30v`). Dark text. Hover darkens to `accent-warm-dark`. |
| `usa-button--base` | Background `base` (`gray-cool-50`), white text. Hover darkens to `base-dark`. |
| `usa-button--outline` | Removes the fill (`background-color: white`), keeps a 2px inset box-shadow border in primary color, and switches text to primary. **MDWDS override**: hover and focus keep `background-color: white` (no fill change) — only the border color may deepen. |
| `usa-button--white` | White background, primary (Maryland blue) text. Hover background → `base-lighter` (off-white). Used on dark sections. |
| `usa-button--black` | Background `ink` (`gray-90`, near-black), white text. Hover → `base-darker`. Visited stays `ink`. |
| `usa-button--unstyled` | Removes all button box styling (background, padding, border). Renders as inline link with primary color and underline. |
| `usa-button--big` | Padding `units(2) units(3)` = 16/24px, font-size scale 5 (≈22px), same border-radius. Visually heavier — for hero CTAs. |
| `usa-button--disabled` | Alternative to the `disabled` HTML attribute. Sets opacity, removes hover/focus effects, sets `cursor: not-allowed`. Pair with `aria-disabled="true"`. |
| `data-ga-category` / `data-ga-action` / `data-ga-label` | Maryland Global Analytics tracking attributes. Read by the analytics layer; no visual effect. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `default` \| `secondary` \| `accent-cool` \| `accent-warm` \| `base` \| `white` \| `black` \| `outline` | `default` | Maps to `usa-button--{variant}`; `default` adds no modifier. |
| `size` | `default` \| `big` | `default` | `big` adds `usa-button--big`. |
| `label` | string | `"Primary Button"` | Button text content. |
| `type` | `button` \| `submit` \| `reset` | `button` | HTML `type` attribute. **Always set this** on buttons inside a `<form>` — without it the browser defaults to `submit`. |
| `disabled` | boolean | `false` | Adds `disabled` attribute. |
| `enableAnalytics` | boolean | `false` | Adds the `data-ga-*` attributes. |
| `gaCategory` | string | `"Button"` | GA event category. |
| `gaAction` | string | `"Click"` | GA event action. |
| `gaLabel` | string | `"Primary CTA"` | GA event label. |

## Accessibility

- **Use `<button>` for actions, `<a class="usa-button">` for navigation.** A control that changes the page (submits, opens a modal, toggles) is a `<button>`. A control that goes to a URL is an `<a>`. Don't put `onclick="location.href=..."` on a `<button>`.
- **Set `type` explicitly** on every `<button>` inside a form. Without `type`, the browser defaults to `type="submit"` and a "Cancel" button can submit the form.
- **Disabled state** — Pair the HTML `disabled` attribute with `aria-disabled="true"`. The HTML attribute removes the button from the tab order; `aria-disabled` ensures screen readers announce it. Prefer the HTML attribute unless the button must remain focusable (e.g., to show a tooltip explaining why it's disabled — in that case use only `aria-disabled="true"` and intercept the click).
- **Toggle buttons** — Add `aria-pressed="true"` or `"false"` to communicate state to assistive tech (e.g., a "Subscribe" toggle).
- **Buttons-as-links** — When using `<a class="usa-button">`, ensure it goes to a real `href`. Don't use `href="#"` without `role` adjustment; if there is no destination, use `<button>` and `usa-button--unstyled`.
- **Focus visibility** — The CDN applies a 2px Maryland blue focus ring with 2px offset automatically. Don't override `outline: none`.
- **Contrast** — All variant color combinations meet WCAG AA. Don't override `color` or `background-color` inline.

## JS requirements

None. Buttons are pure CSS. Form submission is handled by the surrounding `<form>` element. Click handling is whatever you wire up (a real link `href`, a `<form>` submission, or your own JavaScript).

## Common mistakes

1. **Hand-rolling button colors** — `style="background: #1A4480"` is always wrong. The CDN already paints `usa-button` Maryland blue. If a button looks unstyled, you forgot the class — not the inline color.
2. **Missing `type="button"` inside a form** — A "Cancel" or "Open modal" button without `type="button"` becomes a submit button. Always declare `type` on buttons in forms.
3. **Using `<a>` for an action without `role="button"`** — A link that performs an in-page action (modal open, expand, etc.) should be a `<button>`. If you must use `<a>`, add `role="button"`, keyboard handling, and a real `href` fallback.
4. **Mixing primary + secondary in the same row** — Two equally-weighted buttons fight for attention. Pair primary with outline or base instead, and reserve `secondary` (red) for destructive actions.
5. **`--big` everywhere** — Big buttons signal "the action of this page". Multiple big buttons dilute the signal.
6. **Using `--white` on a light background** — The white button vanishes. Only use it on `bg-primary-darker`, `bg-base-darkest`, or a dark image hero.
7. **Forgetting `aria-disabled`** — Disabled with the HTML attribute removes the button from the tab order, but a button you want to keep visible-and-focusable (with a "why" tooltip) needs `aria-disabled="true"` instead.
