# usa-sidenav

The plain USWDS sidenav. Hierarchical vertical sidebar navigation supporting up to three levels of nesting. Each level uses progressive indentation and a left-border accent.

> **Prefer `maryland-sidenav` on Maryland-branded pages.** It has Maryland-specific styling: a 3px `ink` top border, mobile collapse with toggle button, and Maryland-blue underline hover states. Use `usa-sidenav` only for internal-tooling or non-Maryland-themed contexts. See `cdn/components/maryland-sidenav.md`.

## What it looks like

A vertical flex column. Each item is a full-width link, ~16px Source Sans, with a 4px-ish left border accent that turns Maryland blue (`primary`) on hover and stays blue when active.

- **Single-level:** Flat list. Each `<li>` is one link. Active item gets `usa-current` class — bold text, solid blue left border, light-blue background fill.
- **Two-level:** Active item reveals a nested `<ul class="usa-sidenav__sublist">` indented ~16-24px right, with smaller-text sub-items underneath.
- **Three-level:** A child of the active item can itself be active, revealing a third nested sublist further indented.

Hover state: text becomes `primary` with underline; left border darkens. Active state: 4px solid `primary` left border + bold text + tinted `base-lightest` background.

USWDS styles come from upstream — colors are themed to Maryland's primary blue token, but the layout and structure are pure USWDS.

## Variants

| Variant | Visual |
|---|---|
| `single-level` | Flat list. Active item is one of the top-level entries. |
| `two-level` | Active item shows a nested sublist of its children. |
| `three-level` | Active item is a grandchild, with its parent expanded and active. |

## Default markup — three-level

```html
<nav aria-label="Side navigation">
  <ul class="usa-sidenav">
    <li class="usa-sidenav__item">
      <a href="/parks" class="usa-current">State parks</a>
      <ul class="usa-sidenav__sublist">
        <li class="usa-sidenav__item">
          <a href="/parks/locations">Park locations</a>
          <ul class="usa-sidenav__sublist">
            <li class="usa-sidenav__item">
              <a href="/parks/locations/eastern">Eastern shore</a>
            </li>
            <li class="usa-sidenav__item">
              <a href="/parks/locations/central" class="usa-current">Central Maryland</a>
            </li>
            <li class="usa-sidenav__item">
              <a href="/parks/locations/western">Western Maryland</a>
            </li>
          </ul>
        </li>
        <li class="usa-sidenav__item">
          <a href="/parks/camping">Camping reservations</a>
        </li>
        <li class="usa-sidenav__item">
          <a href="/parks/activities">Activities</a>
        </li>
      </ul>
    </li>
    <li class="usa-sidenav__item">
      <a href="/fishing">Recreational fishing</a>
    </li>
    <li class="usa-sidenav__item">
      <a href="/wildlife">Wildlife</a>
    </li>
    <li class="usa-sidenav__item">
      <a href="/forestry">Forestry</a>
    </li>
  </ul>
</nav>
```

## Markup — single-level

```html
<nav aria-label="Side navigation">
  <ul class="usa-sidenav">
    <li class="usa-sidenav__item">
      <a href="/about" class="usa-current">About DNR</a>
    </li>
    <li class="usa-sidenav__item">
      <a href="/mission">Our mission</a>
    </li>
    <li class="usa-sidenav__item">
      <a href="/leadership">Leadership</a>
    </li>
    <li class="usa-sidenav__item">
      <a href="/jobs">Careers</a>
    </li>
  </ul>
</nav>
```

## Markup — two-level

```html
<nav aria-label="Side navigation">
  <ul class="usa-sidenav">
    <li class="usa-sidenav__item">
      <a href="/licenses" class="usa-current">Licenses</a>
      <ul class="usa-sidenav__sublist">
        <li class="usa-sidenav__item">
          <a href="/licenses/fishing">Fishing</a>
        </li>
        <li class="usa-sidenav__item">
          <a href="/licenses/hunting">Hunting</a>
        </li>
        <li class="usa-sidenav__item">
          <a href="/licenses/boating">Boating</a>
        </li>
      </ul>
    </li>
    <li class="usa-sidenav__item">
      <a href="/permits">Permits</a>
    </li>
    <li class="usa-sidenav__item">
      <a href="/regulations">Regulations</a>
    </li>
  </ul>
</nav>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-sidenav` | The outer `<ul>`. Vertical flex column. No list bullets. Each item gets a thin left border accent from `::before`. |
| `usa-sidenav__item` | Each `<li>`. Houses the link plus an optional nested `<ul class="usa-sidenav__sublist">`. |
| `usa-sidenav__sublist` | Nested `<ul>` for child levels. Indented ~16-24px from parent. Sub-items render at slightly smaller font size. |
| `usa-current` | Marker class on the active `<a>`. Switches the left border to a thicker (~4px) solid `primary` (Maryland blue) accent, makes the link text bold/semibold and `primary` color, and tints the background to `base-lightest`. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `single-level` \| `two-level` \| `three-level` | `three-level` | Choice of nesting depth. |
| `currentLabel` | string | `"Current page"` | Label for the active link. |
| `parentLabels` | array of string | 3 items | Labels for top-level peers of the active section. |
| `childLabels` | array of string | 3 items | Sub-items inside the active section (two/three-level variants). |
| `grandchildLabels` | array of string | 3 items | Items two levels deep (three-level variant only). |
| `ariaLabel` | string | `"Side navigation"` | Custom landmark label on the `<nav>`. |
| `ariaDescribedBy` | string | `""` | Optional `aria-describedby` referencing an ID of descriptive text. |

## Heading level adjustment

The sidenav contains no headings — the `<nav aria-label="...">` provides the landmark name. Don't add an `<h2>` inside.

## Common mistakes

1. **Using `usa-sidenav` on a Maryland-themed page** — reach for `maryland-sidenav` instead. It has the right top border, mobile toggle, and styling for Maryland.gov.
2. **Forgetting `aria-current="page"` on the active anchor** — the `usa-current` class is visual; pair it with the ARIA attribute so screen readers announce the current page.
3. **Skipping the `<nav>` wrapper** — without it, no landmark. The `<ul>` alone won't be announced as navigation.
4. **Nesting more than 3 levels** — USWDS supports up to three. Past that the indentation makes the deeper items unreadable. Restructure the content instead.
5. **Putting the sidenav inline with body text** — it belongs in a sidebar column (`grid-col-12 desktop:grid-col-3`), not inside a prose block.
6. **Linking the current page** — the active `<a>` should be a non-link (no `href`) or point to itself with `aria-current="page"`. Don't render it as an active link to another page.
7. **Adding custom styles to override the active state** — the `usa-current` class handles bold + colored border + background. Don't inline `style="font-weight: bold"`.
