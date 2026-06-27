# maryland-nav

The Maryland primary navigation bar. The horizontal tab-style nav that sits inside `maryland-header` on desktop, and collapses to a slide-in hamburger panel on mobile. Supports two levels of hierarchy (top-level tabs + dropdown sub-items).

> **You rarely render `maryland-nav` directly.** It's composed automatically inside `maryland-header`. Reach for the standalone markup only when building a custom header layout. See `cdn/components/maryland-header.md`.

## What it looks like

**At desktop (≥1024px):** A horizontal row of top-level link tabs sitting at the bottom of the header, flush-left, with 16px gaps between items. Each top-level item is 16px (`body-6`) semibold dark text, padded `units(4)` (32px) - 3px top / `units(2)` (16px) horizontal / `units(2)` bottom. A 3px transparent top border becomes Maryland blue (`primary`) on hover and Maryland gold (`secondary-vivid`) when the link marks the current section (`maryland-nav__link--active-trail`).

Top-level items with children render as `<button>` elements with a small chevron (`units(3)` = 24px, rotated 90°) on the right that flips to 180° when the dropdown is open. The dropdown panel itself is white, positioned absolutely below the button, with a soft `0 0 5px 5px rgba(0,0,0,0.2)` shadow. Inside, sub-items render as 12px (`body-4`) plain links in a list; if there are 6+ children, the list breaks into 2 columns. Each child link has a Maryland blue underline (2px thick, 24% offset) on hover.

The dropdown footer holds a "See all {topic} topics" link (`maryland-nav__button`) styled as a flex row with a right-arrow icon (Material `arrow_forward`).

**Below desktop:** The nav collapses to a 24px square hamburger toggle button (top-right of the header). The icon is a CSS-masked Material `menu` glyph that swaps to `close` when `aria-expanded="true"`. Tapping the button opens a **full-viewport white panel** (`maryland-nav__mobile-panel`) that slides in over the page. Inside the panel:

- Top: the search form (`maryland-nav__mobile-slot` containing `maryland-search-form`).
- Middle: a vertical list of top-level items. Each item is 18px (`body-9`) semibold, padded `units(2.5)` top/bottom, separated by 1px `base-light` bottom borders. Items with children show a right-chevron icon and reveal their sub-items in a nested panel inside the same view. Sub-items are 14px (`body-7`) normal weight, also separated by 1px borders.
- Below the link list: the mobile copy of the utility nav.
- Optional bottom: a "Maryland.gov" link (used on agency sites to link back to the state portal) — 14px (`ui-7`), semibold, `base-darkest`.

The mobile panel has an `inset` driven by CSS custom properties (`--maryland-nav-inset-top`, etc.) so it can dock under a sticky banner if needed.

## When to use the standalone component

- Building a custom page shell that doesn't use `maryland-header`.
- Embedding nav in an unusual layout (rare).
- Otherwise: render `maryland-header` and let it compose the nav.

## Default markup

> **Every `maryland-nav__children` div MUST have a unique `id` attribute, and every `maryland-nav__item` should have one too.** The MDWDS JS bundle reads `.id` from these elements when wiring up `aria-controls` for dropdown toggle buttons it generates at runtime. **If `id` is empty or missing on a `__children` div, the page throws `Uncaught SyntaxError: Failed to execute 'querySelector' on 'Document': '#' is not a valid selector` the first time a user clicks a dropdown.** This is the most common silent-failure cause for navs that "look right but crash on interaction."

```html
<nav class="maryland-nav">
  <button class="maryland-nav__toggle" aria-label="Toggle Nav" type="button"></button>
  <div class="maryland-nav__mobile-panel" id="md-nav-panel">

    <!-- Search slot (shown only on mobile) -->
    <div class="maryland-nav__mobile-slot">
      <form class="maryland-search-form" role="search">
        <label class="usa-sr-only" for="mobile-search">Search</label>
        <input id="mobile-search" class="usa-input" type="search" name="q" />
        <button class="usa-button" type="submit">Search</button>
      </form>
    </div>

    <!-- Top-level items -->
    <ul class="maryland-nav__items maryland-nav__items--level-one">

      <!-- Item with no children -->
      <li class="maryland-nav__item maryland-nav__item--level-one" id="nav-item-parks">
        <a class="maryland-nav__link maryland-nav__link--level-one" href="/parks">Parks</a>
      </li>

      <!-- Item with dropdown — id on the <li> AND id on the __children div -->
      <li class="maryland-nav__item maryland-nav__item--level-one" id="nav-item-licenses">
        <button type="button" class="maryland-nav__link maryland-nav__link--level-one">
          Licenses &amp; permits
        </button>
        <div class="maryland-nav__children" id="nav-children-licenses">
          <a class="maryland-nav__button maryland-nav__button--level-two" href="/licenses">
            Explore licenses &amp; permits
          </a>
          <ul class="maryland-nav__items maryland-nav__items--level-two">
            <li class="maryland-nav__item maryland-nav__item--level-two">
              <a class="maryland-nav__link maryland-nav__link--level-two" href="/fishing">Fishing</a>
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-two">
              <a class="maryland-nav__link maryland-nav__link--level-two" href="/hunting">Hunting</a>
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-two">
              <a class="maryland-nav__link maryland-nav__link--level-two" href="/boating">Boating</a>
            </li>
          </ul>
          <a class="maryland-nav__button maryland-nav__button--level-two" href="/licenses">
            See all licenses &amp; permits topics
          </a>
        </div>
      </li>

      <!-- Active trail (current section) -->
      <li class="maryland-nav__item maryland-nav__item--level-one" id="nav-item-wildlife">
        <a
          class="maryland-nav__link maryland-nav__link--level-one maryland-nav__link--active-trail"
          href="/wildlife"
        >
          Wildlife
        </a>
      </li>
    </ul>

    <!-- Optional Maryland.gov link (mobile-only, agency sites) -->
    <div class="maryland-nav__mobile-slot">
      <div class="maryland-nav__mobile-agency-link">
        <a href="https://maryland.gov">Maryland.gov</a>
      </div>
    </div>
  </div>
</nav>
```

### Required `id` attributes — summary

| Element | `id` required? | Why |
|---|---|---|
| `<div class="maryland-nav__mobile-panel">` | **Yes** | JS wires this id into the toggle's `aria-controls`. |
| `<li class="maryland-nav__item">` | Recommended | The component puts a `uid()` here; some interaction patterns key off it. |
| `<div class="maryland-nav__children">` | **Required for dropdowns** | JS wires this id into the auto-generated Back button's and parent button's `aria-controls`. Empty id → `querySelector('#')` SyntaxError on first click. |

Use any unique string — `nav-children-{topic}` is a simple convention.

## What each class does

| Class | Effect |
|---|---|
| `maryland-nav` | The outer `<nav>` element. Below desktop: contains the hamburger toggle + slide-in panel. At desktop: lays out as a horizontal flex row of top-level tabs and removes the hamburger button. |
| `maryland-nav--hamburgered` | Modifier that forces hamburger behavior even at desktop (e.g., for a narrow layout). When this class is present at desktop, the desktop tab styles do **not** apply. |
| `maryland-nav__toggle` | The hamburger button. 48×48px (`units(6)` square), transparent background, CSS-masked `menu` icon at 90% size. Swaps to `close` icon when `aria-expanded="true"`. Hidden at desktop. |
| `maryland-nav__mobile-panel` | The slide-in white panel. Fixed position covering the full viewport (minus inset CSS variables). Hidden by default (`visibility: hidden`); shown via `.is-open`. White background with a soft layered box-shadow. At desktop becomes a relative flex row inside the header. |
| `maryland-nav__mobile-slot` | A sub-section of the mobile panel that holds either the search form, utility-nav items, or the Maryland.gov link. Hidden at desktop. |
| `maryland-nav__mobile-header` | The top strip of the mobile panel (close button, etc.). Hidden at desktop. |
| `maryland-nav__mobile-agency-link` | Wrapper for the "Maryland.gov" link at the bottom of the mobile panel. 40px top margin, 32px bottom. The link itself is 14px (`ui-7`) semibold `base-darkest`, with primary-blue underline on hover. |
| `maryland-nav__items` | The `<ul>` of nav items. Unstyled (no bullets, no padding). |
| `maryland-nav__items--level-one` | Top-level item list. Mobile: vertical stack with bottom borders. Desktop: flex row with 16px gaps. |
| `maryland-nav__items--level-two` | Sub-item list inside a dropdown. Mobile: vertical stack with bottom borders. Desktop: max-width `card-lg`; if it has 6+ children, becomes a 2-column layout. |
| `maryland-nav__item--level-one` | Top-level `<li>`. Mobile: bottom border + `body-10` (`~22px`) semibold typography. Desktop: borderless, 250ms shadow transition on dropdown open. |
| `maryland-nav__item--level-two` | Sub-item `<li>`. Mobile: bottom border + `body-8` (~18px) normal. Desktop: card-lg width, borderless. |
| `maryland-nav__link` | Base class for nav links. Mobile: full-width block, `units(4)` vertical padding. When the element is a `<button>`, adds a chevron-right icon at 24×24px. Hover/focus: underline. |
| `maryland-nav__link--level-one` | Top-level link. Mobile: `body-9` (20px), 20px (`units(2.5)`) vertical padding. Desktop: 16px (`body-6`), `units(2)` horizontal padding, 3px transparent top border that becomes Maryland blue on hover. |
| `maryland-nav__link--level-two` | Sub-item link. Mobile: `body-7` (~16px). Desktop: 14px (`body-4`), 16px / 20px padding, Maryland blue underline on hover. |
| `maryland-nav__link--active-trail` | Marks the link for the current page's section. Desktop: top border becomes Maryland gold (`secondary-vivid`) instead of transparent. |
| `maryland-nav__children` | Dropdown panel inside a top-level item. Mobile: stacks below the parent in the panel. Desktop: positioned absolutely below the tab; hidden by default, shown via `.is-open` or `:focus-within`. |
| `maryland-nav__button` | "Explore {topic}" / "See all topics" CTA inside a dropdown. Mobile: full-width centered pill, `ink` bg, white text. Desktop: full-width left-aligned link with top border + arrow-forward icon, hover state turns text Maryland blue. |
| `maryland-nav__button--level-two` | Modifier for the bottom "See all" CTA — adds extra top padding at desktop. |
| `maryland-nav__panel` | An optional standalone panel container (used internally for some dropdown variants). Hidden until `.is-open`. |
| `maryland-nav__link-back` | "Back" link inside a mobile sub-panel for users to return to the top-level list. Has a chevron-left prefix icon. |
| `maryland-nav__dropdown-parent` | JS-applied class on a top-level item whose dropdown is currently open. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `items` | array of `{label, url, children?}` | extensive default | Top-level items. Each `children` entry is `{label, url}`. |
| `util` | array of `{label, url, isButton?}` | — | Utility-nav items shown inside the mobile panel. |
| `enableUtil` | bool | — | Whether to render the utility nav inside the mobile panel. |
| `showMarylandGovLink` | bool | `false` | Append a "Maryland.gov" link to the bottom of the mobile panel. |

## Heading level adjustment

The nav contains no headings. Top-level "items" are links or buttons, not headings — don't promote them to `<h2>`/`<h3>` even though they appear in a hierarchy.

## Common mistakes

1. **Missing the `maryland-nav__toggle` button** — the mobile panel won't open without it. The button must have `aria-label="Toggle Nav"` for screen readers.
2. **Rendering top-level items as `<a>` when they have children** — items with children should be `<button type="button">` so the click opens the dropdown rather than navigating. The component does this conditionally; preserve it.
3. **Missing the `maryland-nav__children` wrapper around sub-items** — without it, sub-items don't get the dropdown panel styling and won't hide/show correctly.
4. **Forgetting the `--level-one` / `--level-two` modifier classes** — typography and borders are tied to these modifiers, not the base class alone. The base `maryland-nav__link` only sets layout; visual sizing comes from the modifier.
5. **Hard-coding `display: none` on the toggle** — the published CSS handles desktop visibility via `@media`. Overriding with inline style breaks the responsive behavior.
6. **Loading the nav JS twice** — the nav behaviors register on `document.body`. Re-initializing causes double-bound click handlers.
7. **Adding inline navigation styles** — colors, borders, and typography all come from the published CSS. If a tab "looks wrong," it's almost always missing `maryland-nav__link--level-one`, not missing custom CSS.
