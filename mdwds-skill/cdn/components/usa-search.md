# usa-search

The USWDS search form — an input + submit button combo with a magnifying glass icon. Used as a generic site-search entry point in headers, alert pages, or section pages.

> **Disambiguation: prefer `maryland-search-form` on Maryland.gov pages.** The Maryland search form is the standard search entry point used in the Maryland header (with a toggle-to-expand pattern and the MDWDS visual treatment). See `cdn/components/maryland-search-form.md` for the Maryland version. Use `usa-search` only when:
> - You're embedding the standard USWDS search pattern inside USWDS-styled content;
> - You need a search input outside the header context (e.g., a "filter this listing" search at the top of a results page);
> - The Maryland search-form's toggle-button affordance is undesirable.
>
> See `cdn/component-index.md` for the disambiguation row.

## What it looks like

A `usa-search` is a `<form role="search">` containing two elements that sit flush against each other:

1. A `<input type="search" class="usa-search__input usa-input">` — an open white input box. The input has rounded corners on the **left** edge and **square corners on the right** (so it can butt up against the submit button), with a thin gray border. Default height is `units(4)` = 32px.
2. A `<button class="usa-button" type="submit">` — a **Maryland blue** (`primary`) submit button. The button has rounded corners on the **right** edge and square corners on the left. It contains either:
   - A visible label (e.g., "Search") wrapped in `<span class="usa-search__submit-text">`, **plus** an icon (`<img class="usa-search__submit-icon">`) — at mobile-lg and above, only the text shows; on small screens, only the icon shows.
   - Icon only — for the small variant.

Together they form a single rounded pill shape with the text input and the blue search button joined seamlessly.

The `<label>` is `usa-sr-only` (visually hidden but read by screen readers) — the visual placeholder text serves sighted users.

Variants:

- **Default** — Input height 32px, button at `units(4)` height. Icon hides on mobile-lg+ in favor of the label.
- **`usa-search--big`** — Input and button heights both `units(6)` = 48px. Larger font size. Padding on the button increases to `units(4)` horizontal. For prominent search bars at the top of a search-results page.
- **`usa-search--small`** — Compact: smaller padding on the submit button, icon-only (the `usa-search__submit-text` is omitted from the markup). The icon (`__submit-icon`) is `units(3)` = 24px square. For tight space (e.g., a sidebar or compact header strip).

## Variants

| Variant | Class | Visual |
|---|---|---|
| Default | `usa-search` | 32px height, text label on mobile-lg+, icon on small screens |
| Big | `usa-search usa-search--big` | 48px height, larger font, more button padding |
| Small | `usa-search usa-search--small` | Icon-only submit button, compact padding |

## When to use which variant

- **Default** — Page-level search inputs at the top of a content area. Most "Search MDOT", "Search forms", "Search press releases" patterns.
- **Big** — The primary search affordance on a dedicated search-results page or hero search. One per page, near the top.
- **Small** — Header utility-row searches, in-page filter searches, or any tight context where the icon-only button suffices.

## Default markup

```html
<section aria-label="Search component">
  <form class="usa-search" role="search">
    <label class="usa-sr-only" for="search-field">Search</label>
    <input
      class="usa-search__input usa-input"
      id="search-field"
      type="search"
      name="search"
      placeholder="Search MDOT services"
    />
    <button class="usa-button" type="submit">
      <span class="usa-search__submit-text">Search</span>
      <img
        src="https://cdn.maryland.gov/mdwds/latest/img/usa-icons-bg/search--white.svg"
        class="usa-search__submit-icon"
        alt="Search"
      />
    </button>
  </form>
</section>
```

The wrapping `<section aria-label="...">` is optional but recommended — it gives the search a named landmark so screen-reader users can jump to it.

## Markup — big

```html
<form class="usa-search usa-search--big" role="search">
  <label class="usa-sr-only" for="big-search-field">Search Maryland.gov</label>
  <input
    class="usa-search__input usa-input"
    id="big-search-field"
    type="search"
    name="search"
    placeholder="Search Maryland.gov"
  />
  <button class="usa-button" type="submit">
    <span class="usa-search__submit-text">Search</span>
    <img
      src="https://cdn.maryland.gov/mdwds/latest/img/usa-icons-bg/search--white.svg"
      class="usa-search__submit-icon"
      alt="Search"
    />
  </button>
</form>
```

## Markup — small (icon-only submit)

```html
<form class="usa-search usa-search--small" role="search">
  <label class="usa-sr-only" for="small-search-field">Search</label>
  <input
    class="usa-search__input usa-input"
    id="small-search-field"
    type="search"
    name="search"
    placeholder="Search"
  />
  <button class="usa-button" type="submit">
    <img
      src="https://cdn.maryland.gov/mdwds/latest/img/usa-icons-bg/search--white.svg"
      class="usa-search__submit-icon"
      alt="Search"
    />
  </button>
</form>
```

Notice: the small variant drops the `<span class="usa-search__submit-text">` so only the icon shows.

## Markup — Spanish localization

```html
<form class="usa-search" role="search">
  <label class="usa-sr-only" for="search-field-es">Buscar</label>
  <input
    class="usa-search__input usa-input"
    id="search-field-es"
    type="search"
    name="search"
    placeholder="Buscar"
  />
  <button class="usa-button" type="submit">
    <span class="usa-search__submit-text">Buscar</span>
    <img
      src="https://cdn.maryland.gov/mdwds/latest/img/usa-icons-bg/search--white.svg"
      class="usa-search__submit-icon"
      alt="Buscar"
    />
  </button>
</form>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-search` | The `<form>` base. Sets `position: relative`, applies `border-box` sizing, applies the search font family, and turns the form into a flex row when `role="search"` is present so input + button sit side-by-side. |
| `usa-search--big` | At mobile-lg and above, input + button heights become `units(6)` = 48px, font-size jumps to scale `lg`, button horizontal padding is `units(4)` = 32px. |
| `usa-search--small` | Submit button horizontal padding `units(1.5)` = 12px, minimum width `units($theme-button-small-width)`. The submit icon is forced visible at `units(3)` = 24px square. |
| `usa-search__input` | The text input. Sets `appearance: none`, removes vertical padding, sets `font-size` to search-font-family scale `xs`, **removes the right border and bottom-right + top-right border-radius** so it joins seamlessly to the button. Height `units(4)` = 32px in default. Floats left. |
| `usa-input` | Standard USWDS input styling — applied alongside `usa-search__input` for the base input look (border, padding, font). |
| `usa-search__submit-text` | The `<span>` wrapping the visible button label. Hidden on the smallest screens (`display: none`); revealed at `mobile-lg` (480px+) via `display: block`. So small screens show only the icon. |
| `usa-search__submit-icon` | The magnifying glass `<img>`. Visible by default; **hidden at `mobile-lg` and above** (so the text label takes over) and hidden when forced-colors mode is active. The small variant overrides to keep the icon visible. |
| `usa-button` | The submit button — Maryland blue background, white text. See `cdn/components/usa-button.md`. In the search context, the button's top-left and bottom-left border-radius are removed (`border-bottom-left-radius: 0; border-top-left-radius: 0`) and its height is forced to `units(4)` = 32px (default) so it matches the input. |
| `usa-sr-only` | Visually hides the `<label>` while keeping it readable by screen readers. **Required** for accessibility. |
| `role="search"` | On the `<form>`, marks it as a search landmark. Screen reader users can jump to it. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `default` \| `big` \| `small` | `default` | Maps to `usa-search--{variant}`. |
| `language` | `english` \| `spanish` | `english` | Switches button text to "Buscar" and `aria-label` text to Spanish equivalents. |
| `placeholder` | string | `"Search"` | Input `placeholder` attribute. |
| `buttonText` | string | `"Search"` | Visible label inside `usa-search__submit-text` (ignored in Spanish). |
| `id` | string | `"search-field"` | Input `id`, referenced by `<label for="...">`. **Must be unique** if multiple search forms appear on the page. |
| `name` | string | `"search"` | Input `name` attribute (the query string key on submit). |
| `iconUrl` | string | `"https://cdn.maryland.gov/mdwds/latest/img/usa-icons-bg/search--white.svg"` | URL for the magnifying-glass icon. |
| `ariaDescribedBy` | string | `""` | ID of an element describing the input (optional, e.g., a hint paragraph). |
| `enableAnalytics` | boolean | `false` | Adds `data-ga-*` attributes to the input for Maryland Global Analytics. |
| `gaCategory` | string | `"Search"` | GA category. |
| `gaAction` | string | `"Submit"` | GA action. |
| `gaLabel` | string | `"Header Search"` | GA label. |

## Accessibility

- **`role="search"` on the `<form>`** — Marks the form as a search landmark. Required.
- **`<label class="usa-sr-only" for="...">` is required.** Don't omit the label even if the placeholder is descriptive — screen readers may not announce placeholders, and the placeholder disappears when the user types. The visually-hidden label is the canonical solution.
- **Unique `id` per form** — The `<label for="...">` references the input by `id`. If you have multiple search forms on a page (header + footer + inline), each must have a unique `id`.
- **`type="search"`** — Use `type="search"` (not `type="text"`) so the input gets the right mobile keyboard and the browser's clear-X affordance.
- **Icon `alt` text** — The submit-icon `<img>` should have `alt="Search"` (or the localized equivalent). When the text label is also visible, the icon could be `alt=""` (decorative), but USWDS keeps `alt="Search"` for the small/forced-colors paths where the icon stands alone.
- **Submit button** — Always `type="submit"` so Enter inside the input submits the form.
- **`aria-describedby`** — If there's hint text below the input (e.g., "Search press releases from 2020 onward"), give it an `id` and reference it from the input.

## JS requirements

None for the form itself. The form submits to the URL in its `action` attribute (the documented default has none — set `action` to your search endpoint, e.g., `action="/search"`).

If you want **autocomplete** suggestions as the user types, that's a separate component — use `usa-combo-box` instead. The plain `usa-search` is a no-JS, full-page-reload search.

## Common mistakes

1. **No `<label>` element** — Relying on the `placeholder` for accessibility. The placeholder disappears on typing and may not be announced. Always include `<label class="usa-sr-only" for="...">`.
2. **`type="text"` instead of `type="search"`** — Loses mobile keyboard optimization and the browser's clear-X button.
3. **No `role="search"`** — The form is just a generic form; screen reader users can't jump to it as a search landmark.
4. **Duplicate `id`s when multiple search forms exist** — Both label clicks land on the first input. Give each form a unique `id`.
5. **Setting button to `type="button"`** — Then Enter inside the input doesn't submit. The button must be `type="submit"` (default for a button inside a `<form>`, but the markup explicitly sets it for clarity).
6. **Mixing `usa-search` with `maryland-search-form` markup** — They're different components with different DOM. Pick one (and on Maryland.gov pages, prefer `maryland-search-form`).
7. **Removing the right border-radius from the input manually** — `usa-search__input` already does it. Don't add inline `border-radius: 0` rules.
