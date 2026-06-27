# usa-button-group

A row of related buttons grouped as one visual unit. Used for two-button choice rows ("Back" / "Continue"), multi-action toolbars ("Cancel" / "Save draft" / "Publish"), and segmented toggles (map / hybrid / satellite). Wraps a `<ul>` whose items each contain a `usa-button`.

> **Disambiguation:** there is also a Maryland-specific `maryland-button-group` (see `cdn/components/maryland-button-group.md`) which supports a title row and a different visual treatment for promo-style action groups. Use `usa-button-group` for ordinary multi-button rows; use `maryland-button-group` when you need the titled MDWDS variant. See `cdn/component-index.md`.

## What it looks like

A `usa-button-group` is a horizontal row of `usa-button` controls separated by a small gap (the default variant) or fused together with shared borders (`usa-button-group--segmented`). It is rendered as a `<ul>` with no bullets, no list margins, and inline-flex layout.

- **Default** — Buttons sit side by side with a small horizontal gap (≈16px) between them. On mobile they stack vertically. Each child is wrapped in a `<li class="usa-button-group__item">`.
- **Segmented** — Buttons are stitched into a single block: no gap, shared border between buttons, only the outer edges keep the rounded corners. The currently-selected option uses the default (filled blue) variant; the others use `usa-button--outline`. The result reads like a tab strip.

The buttons inside are normal `usa-button` instances and inherit all the variant colors (primary, secondary, outline, base, etc.).

## Variants

| Variant | Class | Visual |
|---|---|---|
| Default | `usa-button-group` | Buttons with small gap, mobile-stacked. |
| Segmented | `usa-button-group usa-button-group--segmented` | Buttons fused into one strip — for view toggles and mutually exclusive choices. |

## When to use which variant

- **Default** — Action rows where the buttons are different actions ("Cancel", "Save draft", "Publish"). The gap visually communicates "these are separate choices".
- **Segmented** — Mutually exclusive view-state toggles where exactly one is "current" ("Map" / "Hybrid" / "Satellite"; "Day" / "Week" / "Month"). The fused appearance communicates "pick one of these". The selected option should be the filled primary variant; the others should be `usa-button--outline`.

For two-button decision rows on form steps ("Back" / "Continue"), use **default** (not segmented). Segmented is reserved for view toggles.

## Default markup

```html
<ul class="usa-button-group" aria-label="Form actions">
  <li class="usa-button-group__item">
    <button type="button" class="usa-button usa-button--outline">
      Cancel
    </button>
  </li>
  <li class="usa-button-group__item">
    <button type="button" class="usa-button usa-button--secondary">
      Save draft
    </button>
  </li>
  <li class="usa-button-group__item">
    <button type="submit" class="usa-button">Publish</button>
  </li>
</ul>
```

The wrapping `<ul>` is required — it provides the layout and the `aria-label` for the landmark. Each button must be inside a `<li class="usa-button-group__item">`.

## Markup — segmented (view toggle)

```html
<ul class="usa-button-group usa-button-group--segmented" aria-label="Map view">
  <li class="usa-button-group__item">
    <button type="button" class="usa-button" aria-pressed="true">
      Map
    </button>
  </li>
  <li class="usa-button-group__item">
    <button type="button" class="usa-button usa-button--outline" aria-pressed="false">
      Hybrid
    </button>
  </li>
  <li class="usa-button-group__item">
    <button type="button" class="usa-button usa-button--outline" aria-pressed="false">
      Satellite
    </button>
  </li>
</ul>
```

The selected option uses the default `usa-button` (filled Maryland blue); the others use `usa-button--outline`. Toggle `aria-pressed` and swap the variant classes as the user selects different options.

## Markup — two-button decision row

```html
<ul class="usa-button-group" aria-label="Application step navigation">
  <li class="usa-button-group__item">
    <button type="button" class="usa-button usa-button--outline">Back</button>
  </li>
  <li class="usa-button-group__item">
    <button type="submit" class="usa-button">Continue to review</button>
  </li>
</ul>
```

## Markup — pagination controls

```html
<ul class="usa-button-group" aria-label="Pagination controls">
  <li class="usa-button-group__item">
    <button type="button" class="usa-button usa-button--outline">Previous</button>
  </li>
  <li class="usa-button-group__item">
    <button type="button" class="usa-button">Next</button>
  </li>
</ul>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-button-group` | The wrapping `<ul>`. Removes list bullets and margins. Lays children inline with a horizontal gap (≈16px); stacks vertically on mobile. |
| `usa-button-group--segmented` | Removes the gap and welds buttons together so they share borders. Inner buttons lose the outer side's border-radius — only the leftmost and rightmost ends remain rounded. Used for tab-strip / view-toggle patterns. |
| `usa-button-group__item` | The `<li>` wrapper around each button. Removes list-item bullet styling and supplies the alignment hooks the parent uses. **Required** — buttons placed directly inside `usa-button-group` won't line up correctly. |

The buttons inside use all the standard `usa-button` classes — see `cdn/components/usa-button.md`.

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `default` \| `segmented` | `default` | Adds `usa-button-group--segmented` when `segmented`. |
| `buttons` | array of `{ label, variant, disabled }` | two-item back/continue pair | Each entry becomes a `<li>` + `<button>`. Inner `variant` values: `default`, `secondary`, `accent-cool`, `accent-warm`, `base`, `outline`. |
| `ariaLabel` | string | `"Navigation buttons"` | The group's `aria-label`. Required for screen reader context. |
| `disabled` | boolean | `false` | Disables every button in the group. |
| `enableAnalytics` | boolean | `false` | Adds `data-ga-*` attributes to each child button. |
| `gaCategory` | string | `"Button Group"` | GA event category. |
| `gaAction` | string | `"Click"` | GA event action. |
| `gaLabel` | string | `"Navigation"` | GA event label (each button gets `${gaLabel} - ${button label}`). |

## Accessibility

- **Always set `aria-label` on the `<ul>`.** The group is a landmark with no visible name; without it screen readers announce just "list, 3 items".
- **`role` is not required** — the `<ul>` element already conveys a list. Don't add `role="group"` unless you've removed the `<ul>` structure.
- **Segmented = toggle state.** When using the segmented variant as a single-select control, set `aria-pressed="true"` on the selected button and `aria-pressed="false"` on the others. Update on user action.
- **Button types** — Inside a `<form>`, set `type="button"` on every button that doesn't submit, and `type="submit"` on the one that does. Without `type`, browsers default to submit.
- **Keyboard focus** — Each button is independently focusable via Tab (no arrow-key navigation needed for the default variant). For segmented toggles where arrow-key navigation is desirable, add a `role="radiogroup"` to the `<ul>` and `role="radio"` + `aria-checked` to each button — but the simpler `aria-pressed` pattern is fine for most cases.

## JS requirements

None. The group is purely structural CSS. Any selection state (e.g., updating `aria-pressed` and swapping `usa-button--outline` ↔ `usa-button` on the selected option) is your application code.

## Common mistakes

1. **Putting buttons directly inside `usa-button-group`** — Skipping the `<li class="usa-button-group__item">` wrapper breaks the layout. Each button must be in a list item.
2. **Forgetting `aria-label` on the `<ul>`** — The group becomes an unnamed landmark. Screen-reader users hear "list" with no context.
3. **Using segmented for unrelated actions** — Segmented communicates "pick one of these mutually exclusive options". A "Cancel" / "Save" / "Publish" row is not a toggle — use the default variant.
4. **Mixing too many variants** — A single row should have at most one primary, and the rest as outline or base. Three different colored buttons in one row is visual noise.
5. **No `type` attribute inside a form** — Every `<button>` in a `<form>` should declare `type` explicitly. Otherwise the "Cancel" button submits.
6. **Wrong `aria-pressed` value** — In a segmented toggle, only the currently-selected button has `aria-pressed="true"`. Forgetting to update it on click means the announced state lies.
