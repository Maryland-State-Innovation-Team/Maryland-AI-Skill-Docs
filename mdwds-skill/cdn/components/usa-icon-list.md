# usa-icon-list

A vertical list where each item is prefixed by an inline SVG icon. Use for feature lists, eligibility criteria, checklists, or any time you want a visual marker stronger than a bullet.

> **Prefer `maryland-icon-list` on Maryland.gov pages.** The two components share the conceptual model (icon + text rows) but `maryland-icon-list` applies the Maryland visual treatment (palette, typography, spacing). Use `usa-icon-list` only inside internal tools or where Maryland branding is intentionally absent.

## What it looks like

A `usa-icon-list` is an unstyled `<ul>` whose `<li>` items lay out as horizontal flex rows. Each row has two columns:

1. **Icon column** (`usa-icon-list__icon`) — A square SVG icon on the left. Default size matches the body type scale (~24px square); `--size-lg` increases it to ~32–36px. Icon color is determined by the variant modifier on the `<ul>` (`primary`, `secondary`, `accent-cool`, `accent-warm`, or default base color).
2. **Content column** (`usa-icon-list__content`) — Text content on the right. Padding-left is calculated as `0.4 × icon size` for visual tightness with the icon. Default text is ~16px. The optional `<h3 class="usa-icon-list__title">` makes the row a rich block: bold heading on top, paragraph body below.

Successive `<li>` siblings are separated by `padding-top: units(1.5)` (12px) — tight enough that the list reads as one unit, loose enough to keep each row distinct.

The component supports the full USWDS color palette as variant modifiers. The MDWDS Storybook exposes the most common five: `default` (base), `primary` (Maryland blue), `secondary` (Maryland gold/orange), `accent-cool` (lighter blue), `accent-warm` (soft red/orange).

The icon column is centered against the first line of text via small offset tuning. Icons are decorative by default (`aria-hidden="true"` — the rendered markup includes this).

## Variants

| Variant | Icon color |
|---|---|
| `default` | Base / neutral (dark gray) |
| `primary` | Maryland blue (`color-primary`) |
| `secondary` | Maryland gold/orange (`color-secondary`) |
| `accent-cool` | Lighter blue (`color-accent-cool`) |
| `accent-warm` | Soft red/orange (`color-accent-warm`) |

Size modifier:

| Size | Effect |
|---|---|
| `default` | Icon sized to body text (~24px) |
| `lg` | Icon scaled up (~32–36px). Adds `usa-icon-list--size-lg`. Padding-left of the content column scales proportionally. |

## When to use which variant

- **`default`** → Neutral feature lists where the icon's color shouldn't compete with the content.
- **`primary`** → Lists of benefits, capabilities, or items that share a common positive theme.
- **`secondary`** → Sparingly, for callouts that need a warmer accent.
- **`accent-warm`** → Status/result lists where status icons (warning, error) carry their own meaning and a coordinated warm palette helps.
- **`lg`** → Large display sections (hero-adjacent feature lists) or when icons need to stand out from dense surrounding type.

## Default markup (simple content)

```html
<ul class="usa-icon-list">
  <li class="usa-icon-list__item">
    <div class="usa-icon-list__icon">
      <svg class="usa-icon" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z" />
      </svg>
    </div>
    <div class="usa-icon-list__content">
      Direct deposit available in 2–3 business days
    </div>
  </li>
  <li class="usa-icon-list__item">
    <div class="usa-icon-list__icon">
      <svg class="usa-icon" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z" />
      </svg>
    </div>
    <div class="usa-icon-list__content">
      Apply online — no in-person visit required
    </div>
  </li>
  <li class="usa-icon-list__item">
    <div class="usa-icon-list__icon">
      <svg class="usa-icon" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z" />
      </svg>
    </div>
    <div class="usa-icon-list__content">
      Status tracking by email and SMS
    </div>
  </li>
</ul>
```

## Markup — primary variant (colored icons)

```html
<ul class="usa-icon-list usa-icon-list--primary">
  <li class="usa-icon-list__item">
    <div class="usa-icon-list__icon">
      <svg class="usa-icon" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
        <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z" />
      </svg>
    </div>
    <div class="usa-icon-list__content">
      Eligible residents over age 18
    </div>
  </li>
  <!-- ... -->
</ul>
```

## Markup — rich content (title + description)

```html
<ul class="usa-icon-list usa-icon-list--primary">
  <li class="usa-icon-list__item">
    <div class="usa-icon-list__icon">
      <svg class="usa-icon" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
        <path d="M2 20h2c.55 0 1-.45 1-1v-9c0-.55-.45-1-1-1H2v11zm19.83-7.12c.11-.25.17-.52.17-.8V11c0-1.1-.9-2-2-2h-5.5l.92-4.65c.05-.22.02-.46-.08-.66-.23-.45-.52-.86-.88-1.22L14 2 7.59 8.41C7.21 8.79 7 9.3 7 9.83v7.84C7 18.95 8.05 20 9.34 20h8.11c.7 0 1.36-.37 1.72-.97l2.66-6.15z" />
      </svg>
    </div>
    <div class="usa-icon-list__content">
      <h3 class="usa-icon-list__title">Recommended</h3>
      <p>Combine the SmartTrip card with the MTA monthly pass for the largest savings on cross-county commutes.</p>
    </div>
  </li>
  <li class="usa-icon-list__item">
    <div class="usa-icon-list__icon">
      <svg class="usa-icon" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
        <path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z" />
      </svg>
    </div>
    <div class="usa-icon-list__content">
      <h3 class="usa-icon-list__title">Heads up</h3>
      <p>Refunds for unused trips are issued only within 30 days of purchase.</p>
    </div>
  </li>
</ul>
```

## Markup — large size

```html
<ul class="usa-icon-list usa-icon-list--primary usa-icon-list--size-lg">
  <li class="usa-icon-list__item">
    <div class="usa-icon-list__icon">
      <svg class="usa-icon" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
        <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z" />
      </svg>
    </div>
    <div class="usa-icon-list__content">
      Statewide service available in every county
    </div>
  </li>
</ul>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-icon-list` | Outer `<ul>`. Removes list styling, sets the typed measure (~paragraph width, USWDS `measure-5` for the default size). Lays each child as a flex row. |
| `usa-icon-list--primary` | Sets icon color on every descendant `usa-icon-list__icon` to `color-primary` (Maryland blue). |
| `usa-icon-list--secondary` | Icon color = `color-secondary` (Maryland gold/orange). |
| `usa-icon-list--accent-cool` | Icon color = `color-accent-cool` (lighter blue). |
| `usa-icon-list--accent-warm` | Icon color = `color-accent-warm` (soft red/orange). |
| `usa-icon-list--size-lg` | Bumps icon size to ~32–36px, rescales content padding-left, removes the standard `measure-5` cap (longer lines allowed). |
| `usa-icon-list__item` | One row. Flex container — icon column on the left, content on the right. Adds top padding (~12px) when preceded by another item. |
| `usa-icon-list__icon` | Wraps the SVG icon. Sets a fixed square size (matches the variant's icon size). Its color is controlled by the parent `--{variant}` modifier. |
| `usa-icon` | The SVG element itself. ~24px square at default; `display: block`. `aria-hidden="true"` because the icon is decorative. |
| `usa-icon-list__content` | Right column. Flexible width, padding-left tuned to the icon size. Typography matches the variant. |
| `usa-icon-list__title` | Optional `<h3>` heading inside content. Same font family as the body, weighted to stand out (~17–19px, semibold). Followed by a `<p>` for the description. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `default` \| `primary` \| `secondary` \| `accent-cool` \| `accent-warm` | `default` | Adds `usa-icon-list--{variant}` |
| `size` | `default` \| `lg` | `default` | `lg` adds `usa-icon-list--size-lg` |
| `items` | `[{ icon, content, title? }]` | sample | `icon`: glyph name (Material Symbols), `content`: text body, `title`: optional bold heading above the body |
| `enableAnalytics` | bool | `false` | Adds `data-ga-*` attributes on the `<ul>` |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

### Available icon glyphs

`check_circle`, `cancel`, `thumb_up_alt`, `help`, `error`, `warning`, `info`, `check`, `close`. Unknown values fall back to `check_circle`.

When you author your own markup directly (not via the Storybook template), use any Material Symbols glyph — drop the path data inline as in the markup examples above, or use the sprite reference pattern shown in `cdn/components/usa-icon.md`.

## Heading level adjustment

`usa-icon-list__title` is rendered as `<h3>` in the documented variants. Inside a section already led by `<h2>`, `<h3>` is correct. If the icon list is nested deeper, bump to `<h4>`. The `__title` class itself does not enforce the level — it's a styling class. See `cdn/composition.md`.

## Common mistakes

1. **Using `usa-icon-list` on a Maryland-branded page** — switch to `maryland-icon-list`.
2. **Forgetting `aria-hidden="true"` on the SVG** — assistive tech then announces the decorative icon, polluting the row's text.
3. **Mixing icon shapes inconsistently** — each icon in the list should communicate the same kind of meaning. A check next to one item and a warning next to another (without intent) reads as a status list when it isn't one.
4. **Placing `__title` inside a plain `<li>` without `__content`** — the title styles depend on living inside `usa-icon-list__content`. Without the wrapper, padding and typography break.
5. **Using `<ol>` instead of `<ul>`** — the component is built around an unordered list; ordered semantics produce numbered markers (which the unstyled-list reset is meant to remove).
6. **Hard-coding inline icon `style="color: #1A4480"`** — the variant modifier on the `<ul>` already controls icon color. Inline overrides break the color contract with surrounding content.
