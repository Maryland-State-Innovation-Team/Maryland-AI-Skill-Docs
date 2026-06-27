# maryland-button-group

Maryland Design System button group displays 1–3 related action buttons with an optional title above. It wraps the USWDS `usa-button-group` to reset the default negative margins, set the right gap, and add an inline external-link icon for buttons that point off-site.

> **Use `maryland-button-group` for groups of related action buttons on Maryland.gov pages.** For a single button, use `usa-button` directly. For a multi-step form's primary action, use `usa-button` inside a `usa-form`. For a row of small icon buttons, use `usa-button-group` with `usa-button--unstyled`.

## What it looks like

A `<div>` with an optional `<h2>` title above a `<ul class="usa-button-group">`. The list flex-rows at mobile (480px+); buttons stack vertically below that. Buttons:

- Default size (body-5 ≈ 16px font), 16/20px padding.
- Inherit USWDS button colors: primary (Maryland blue) or secondary (`usa-button--outline` — outlined with primary color).
- External buttons (any URL starting with `http`) get a 16×16px `open_in_new` icon appended after the label, plus `target="_blank"`, `rel="noopener noreferrer"`, and an accessible-label suffix.

The title is `<h2>` using the MDWDS `h2` mixin (Merriweather light, 32–48px responsive). 32px bottom margin. Can be visually hidden via `usa-sr-only`.

The component sits in its own container with a 16px bottom margin.

## When to use

- A row of 2–3 primary actions at the end of a section ("Apply now" / "Learn more").
- Form action buttons (Submit + Cancel + Back).
- Top-of-page primary-actions strip when the hero doesn't already have buttons.

For single-button CTAs, drop the wrapper and use `<a class="usa-button">` directly.

## Default markup

```html
<div class="maryland-button-group">
  <h2 id="bg-title" class="maryland-button-group__title">Get started with your application</h2>
  <ul class="usa-button-group maryland-button-group__list" aria-labelledby="bg-title">
    <li class="usa-button-group__item maryland-button-group__item">
      <a href="/apply" class="usa-button maryland-button-group__button">Start your application</a>
    </li>
    <li class="usa-button-group__item maryland-button-group__item">
      <a href="/eligibility" class="usa-button maryland-button-group__button usa-button--outline">Check eligibility</a>
    </li>
    <li class="usa-button-group__item maryland-button-group__item">
      <a href="https://example.com/help" target="_blank" rel="noopener noreferrer" class="usa-button maryland-button-group__button usa-button--outline" aria-label="Get help (external link)">
        Get help
        <span class="maryland-button-group__icon" aria-hidden="true"></span>
      </a>
    </li>
  </ul>
</div>
```

## Markup — visually hidden title

When the surrounding context already names the group:

```html
<div class="maryland-button-group">
  <h2 id="bg-title-2" class="maryland-button-group__title usa-sr-only">Form actions</h2>
  <ul class="usa-button-group maryland-button-group__list" aria-labelledby="bg-title-2">
    <li class="usa-button-group__item maryland-button-group__item">
      <a href="/submit" class="usa-button maryland-button-group__button">Submit</a>
    </li>
    <li class="usa-button-group__item maryland-button-group__item">
      <a href="/cancel" class="usa-button maryland-button-group__button usa-button--outline">Cancel</a>
    </li>
  </ul>
</div>
```

## Markup — no title

Omit the `<h2>` entirely and drop the `aria-labelledby` from the `<ul>`:

```html
<div class="maryland-button-group">
  <ul class="usa-button-group maryland-button-group__list">
    <li class="usa-button-group__item maryland-button-group__item">
      <a href="/apply" class="usa-button maryland-button-group__button">Apply</a>
    </li>
    <li class="usa-button-group__item maryland-button-group__item">
      <a href="/cancel" class="usa-button maryland-button-group__button usa-button--outline">Cancel</a>
    </li>
  </ul>
</div>
```

## What each class does

| Class | Effect |
|---|---|
| `maryland-button-group` | Outer wrapper. 16px bottom margin. |
| `maryland-button-group__title` | The `<h2>`. Uses the `h2` mixin (Merriweather light, 32–48px responsive). 0/32px vertical margins. |
| `maryland-button-group__list` | The `<ul>`. Combined with `usa-button-group`. Resets the USWDS list negative margins, applies 16px gap. At mobile+ (480px), becomes a wrapping flex row; below 480px, items stack. |
| `maryland-button-group__item` | Each `<li>`. Resets USWDS item margins (using `gap` on the list instead). |
| `maryland-button-group__button` | Each button `<a>`. Sets `theme-button-font-family` size 5 (~16px) and 16/20px padding. Display inline-block. |
| `maryland-button-group__icon` | The external-link icon span. 16×16px, current text color, `open_in_new` Material Symbols mask, middle-aligned. |
| `usa-sr-only` | (USWDS) Visually hides the title while keeping it readable to screen readers. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `title` | string | sample | Group heading. Optional. 75 char limit per design. |
| `hideTitle` | bool | false | Visually hide title (adds `usa-sr-only`). |
| `buttons` | `Array<{text, url, style?: "primary" \| "secondary"}>` | sample | 1–3 button configs. `style: "secondary"` adds `usa-button--outline`. URLs starting with `http` are auto-treated as external. |

## Heading level adjustment

Title defaults to `<h2>`. Demote to `<h3>` if the button group is nested under an existing `<h2>` section. Keep the class.

## Common mistakes

1. **More than 3 buttons** — the design caps at 3. Beyond that, the row gets visually crowded and decision fatigue sets in. Consider grouping related actions differently or using a `maryland-action-items` block.
2. **Forgetting `aria-labelledby`** — when a title is present (even `usa-sr-only`), the `<ul>` should reference it. Without it, screen readers don't associate the group with its purpose.
3. **Mixing primary buttons in the same group** — at most one primary action; the rest should be `usa-button--outline` (secondary). Multiple primaries muddle the decision.
4. **Skipping `target="_blank"` for external URLs** — external links need `target="_blank"`, `rel="noopener noreferrer"`, and an accessible-label suffix. Set them when writing the markup by hand.
5. **Hard-coded external icon next to non-external buttons** — the icon belongs only on external links. For internal-but-action buttons (e.g., "Start application"), no icon.
6. **Using `<button>` instead of `<a>` for navigation** — links navigate; buttons trigger JavaScript. MDWDS uses `<a>` for these; only swap to `<button type="submit">` for form-submission actions.
