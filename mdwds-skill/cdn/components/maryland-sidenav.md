# maryland-sidenav

Maryland-styled hierarchical sidebar navigation for documentation, multi-page section pages, and any layout where the user is deep inside a section and needs to see siblings/children. Sits to the left of `<main>` content (usually `desktop:grid-col-3`).

> **Use this, not `usa-sidenav`, on Maryland-branded pages.** The two share a similar concept but have different markup and visual style. See `cdn/components/usa-sidenav.md` for the USWDS counterpart.

## What it looks like

**Desktop (≥1024px):** A white card-style block with a 3px Maryland-black (`ink`) top border. No border-radius at this size. Max width `card-lg` (~480px). The collapsible toggle button is hidden — the list is always open.

**Below desktop:** Light-gray background (`base-lightest`) rounded card (`units(0.5)` border radius). At the top, a dark `ink` toggle button (`maryland-sidenav__toggle`) spans the full width with `units(2)` `units(3)` padding. Inside the button: the "Section menu" `<h2>` title (14px / `body-7`, semibold) on the left and a chevron-down Material icon (24×24px) on the right that rotates 180° when the menu is expanded. The list below collapses (`display: none`) when the toggle's `aria-expanded` is false.

**The list:**

- **Level 1** (the parent/top item): 16px (`body-6`) semibold. If the current page is the top-level page, renders as a plain `<span>` with no decoration. Otherwise renders as a link with a small (20×20px) Material `keyboard_arrow_left` glyph prefix — implying "go back up". 20px (`units(2.5)`) padding around items.
- **Level 2** (sub-items, the siblings of the current page within this section): 14px (`body-4`) normal weight. Indented to align with the level-1 text (no chevron on level 2 items). The active item (current page) renders as a `<span>` with `aria-current="page"` and gets the level-2 item wrapped with 1px `base-light` top + bottom borders + `units(1)` vertical padding + `units(2)` margin — visually pinching the active item between two thin lines.
- **Level 3** (children of the active level-2 item, when the current page is a level-3 page): 14px (`body-4`), indented an additional 16px (`units(2)` `padding-inline-start`). Only shown when the current page is itself a level-3 page (the `topLevel: false` story variant).

**Link styling:** All links get a Maryland-blue underline `text-decoration` that's hidden by default and appears on hover (`text-decoration-line: underline`). Underline is 6% thick, 24% offset.

## When to use

- Documentation-style pages with siblings and grandchildren.
- An agency section with several pages under one heading.
- **Not** for top-level site navigation (use `maryland-header`'s primary nav instead).

## Default markup — top-level page (current page is the parent)

```html
<nav aria-labelledby="sidenav-title" class="maryland-sidenav">
  <button class="maryland-sidenav__toggle" aria-controls="sidenav-list" aria-expanded="false">
    <span class="usa-sr-only">close</span>
    <h2 class="maryland-sidenav__title" id="sidenav-title">Section menu</h2>
  </button>
  <ul class="maryland-sidenav__list maryland-sidenav__list--level-1" id="sidenav-list">
    <li class="maryland-sidenav__item maryland-sidenav__item--level-1">
      <span
        class="maryland-sidenav__link maryland-sidenav__link--level-1"
        aria-current="page"
      >Recreational fishing</span>
      <ul class="maryland-sidenav__list maryland-sidenav__list--level-2">
        <li class="maryland-sidenav__item maryland-sidenav__item--level-2">
          <a class="maryland-sidenav__link maryland-sidenav__link--level-2" href="/fishing/licenses">Buy a license</a>
        </li>
        <li class="maryland-sidenav__item maryland-sidenav__item--level-2">
          <a class="maryland-sidenav__link maryland-sidenav__link--level-2" href="/fishing/regulations">Regulations</a>
        </li>
        <li class="maryland-sidenav__item maryland-sidenav__item--level-2">
          <a class="maryland-sidenav__link maryland-sidenav__link--level-2" href="/fishing/seasons">Seasons</a>
        </li>
        <li class="maryland-sidenav__item maryland-sidenav__item--level-2">
          <a class="maryland-sidenav__link maryland-sidenav__link--level-2" href="/fishing/locations">Where to fish</a>
        </li>
        <li class="maryland-sidenav__item maryland-sidenav__item--level-2">
          <a class="maryland-sidenav__link maryland-sidenav__link--level-2" href="/fishing/records">State records</a>
        </li>
      </ul>
    </li>
  </ul>
</nav>
```

## Markup — sub-page (current page is a level-3 item)

```html
<nav aria-labelledby="sidenav-title" class="maryland-sidenav">
  <button class="maryland-sidenav__toggle" aria-controls="sidenav-list" aria-expanded="false">
    <span class="usa-sr-only">close</span>
    <h2 class="maryland-sidenav__title" id="sidenav-title">Section menu</h2>
  </button>
  <ul class="maryland-sidenav__list maryland-sidenav__list--level-1" id="sidenav-list">
    <li class="maryland-sidenav__item maryland-sidenav__item--level-1">
      <!-- Parent renders as a link with back-chevron, since the current page is deeper -->
      <a href="/fishing" class="maryland-sidenav__link maryland-sidenav__link--level-1">Recreational fishing</a>
      <ul class="maryland-sidenav__list maryland-sidenav__list--level-2">
        <li class="maryland-sidenav__item maryland-sidenav__item--level-2">
          <a class="maryland-sidenav__link maryland-sidenav__link--level-2" href="/fishing/licenses">Buy a license</a>
        </li>
        <li class="maryland-sidenav__item maryland-sidenav__item--level-2">
          <!-- Active level-2 item: span + aria-current; the parent li gets pinch borders -->
          <span class="maryland-sidenav__link maryland-sidenav__link--level-2" aria-current="page">Regulations</span>
          <ul class="maryland-sidenav__list maryland-sidenav__list--level-3">
            <li class="maryland-sidenav__item maryland-sidenav__item--level-3">
              <a class="maryland-sidenav__link maryland-sidenav__link--level-3" href="/fishing/regulations/freshwater">Freshwater</a>
            </li>
            <li class="maryland-sidenav__item maryland-sidenav__item--level-3">
              <a class="maryland-sidenav__link maryland-sidenav__link--level-3" href="/fishing/regulations/tidal">Tidal</a>
            </li>
            <li class="maryland-sidenav__item maryland-sidenav__item--level-3">
              <a class="maryland-sidenav__link maryland-sidenav__link--level-3" href="/fishing/regulations/charter">Charter boats</a>
            </li>
          </ul>
        </li>
        <li class="maryland-sidenav__item maryland-sidenav__item--level-2">
          <a class="maryland-sidenav__link maryland-sidenav__link--level-2" href="/fishing/seasons">Seasons</a>
        </li>
      </ul>
    </li>
  </ul>
</nav>
```

## What each class does

| Class | Effect |
|---|---|
| `maryland-sidenav` | The outer `<nav>`. Mobile: `base-lightest` (light gray) background, 4px (`units(0.5)`) rounded corners, full width. Desktop: white background, 3px top border (color `ink`), no border-radius, max-width ~480px (`units("card-lg")`). |
| `maryland-sidenav__toggle` | The mobile collapse button. Dark `ink` background, white text. Spans full width with flex layout: title on left, chevron-down icon (24×24px, masked currentColor) on right. Rotated 180° when `aria-expanded="true"`. **Hidden at desktop.** |
| `maryland-sidenav__title` | The "Section menu" label inside the toggle. 14px (`body-7`), semibold, zero margin. |
| `maryland-sidenav__list` | The base `<ul>`. No list bullets, zero margin/padding. |
| `maryland-sidenav__list--level-1` | Top-level list. `units(2) units(3) units(5)` padding on mobile (so items don't sit flush against the toggle); flush at desktop. Hidden when collapsed (`html.js .maryland-sidenav__list--level-1:not(.is-open)` matches the JS-injected toggle state). |
| `maryland-sidenav__list--level-2` | Nested list. 8px top margin (`units(1)`). |
| `maryland-sidenav__list--level-3` | Deeper nested list. Inherits unstyled-list base. |
| `maryland-sidenav__item` | Base list item. Unstyled. |
| `maryland-sidenav__item--level-2:has(> [aria-current])` | When the immediate child is the current page, applies 1px `base-light` top + bottom borders, `units(1)` vertical padding, `units(2)` vertical margin. Visually pinches the active item between two thin lines. |
| `maryland-sidenav__link` | Base link/span class. Inherits color, text-trim mixin, `units(2)` vertical padding. On `<a>` elements: invisible underline that becomes visible on hover (Maryland-primary 6% thickness, 24% offset). |
| `maryland-sidenav__link--level-1` | Top-level link. 16px (`body-6`), semibold. Flex row with a 20×20px `keyboard_arrow_left` chevron prefix when the link is **not** the current page; no chevron when it has `aria-current`. |
| `maryland-sidenav__link--level-2` | Sub-item link. 14px (`body-4`). Becomes semibold when `aria-current="page"`. |
| `maryland-sidenav__link--level-3` | Deeper link. 14px (`body-4`), 16px (`units(2)`) extra left padding (indentation). |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `topLevel` | bool | `true` | When `true`, the parent (level-1) item renders as a plain `<span>` with `aria-current="page"`, and the current level-2 active item is rendered as a `<span>` instead of a link with grand-children. When `false`, the parent renders as a `<a>` back-link, and a chosen level-2 item renders as the current page with its level-3 children expanded. |

## Heading level adjustment

`maryland-sidenav__title` is an `<h2>` ("Section menu") used to label the nav for assistive tech. **This is acceptable as a sibling of the page's hero `<h1>`** because the sidenav is a top-level page section. Don't change it to `<h3>` unless the sidenav is nested under another labeled `<h2>` (unusual).

## Common mistakes

1. **Wrapping the sidenav in a `grid-container` plus a column class** — pick one approach. The sidenav itself doesn't apply a container; you place it inside `<aside class="grid-col-12 desktop:grid-col-3">` per `cdn/composition.md`. Don't add a second `grid-container` inside the aside.
2. **Linking the current page** — the current item must render as `<span aria-current="page">`, not `<a aria-current="page">`. Anchors imply navigation; spans don't.
3. **Skipping the `--level-1`/`--level-2`/`--level-3` modifiers on `__link`** — typography and indentation are driven entirely by the modifier. Without it, all links default to base size and look identical.
4. **Putting the toggle `<button>` outside the `<nav>`** — the JS expects the toggle to be the first child of `.maryland-sidenav` so it can find the list via `aria-controls`. Misplacing it breaks collapse on mobile.
5. **Adding `usa-sidenav` classes to a `maryland-sidenav`** — they're entirely different components (different DOM, different CSS). Pick one.
6. **Manually styling the active item with `font-weight: bold`** — use `aria-current="page"` and let the `level-2[aria-current]` selector handle the bold + pinch borders.
7. **Forgetting the `aria-controls` linkage on the toggle** — without it, screen readers can't announce what the button controls and the JS won't find the list to toggle.
