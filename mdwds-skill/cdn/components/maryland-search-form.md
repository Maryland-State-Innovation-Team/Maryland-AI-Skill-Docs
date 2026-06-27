# maryland-search-form

Maryland Design System search form is the site search entry point. It comes in three flavors: a static inline form for the header, a pop-out form that toggles open from a search icon, and a hero block for use on a dedicated search-results page. Search results themselves are rendered into a `.maryland-search-results` container by Google Custom Search.

> **Use `maryland-search-form` for site search on Maryland-branded pages.** For form validation, see `usa-validation`. For data filters (not search), use the `maryland-listing-page` filter form. There is no MDWDS replacement for `usa-combo-box` autocomplete — use that for searchable selects.

## What it looks like

The form is a `<form role="search">` with three pieces:

- A `<label>` (`maryland-search-form__label`) — Source Sans body-8 (20px) semibold above the input.
- A `__widget` flex-row holding the input and submit button. A search-glyph icon is positioned absolutely on the left of the input via `::before`.
- The input — full width, 1px `base-darkest` border, 12px vertical / 8/48px horizontal padding (left-padding leaves room for the search glyph).
- A `__submit` ink-colored button with semibold text. 12/20px padding. Right-corner-rounded only (visually attached to the input). Hover/focus turns Maryland blue.
- An optional scope `<fieldset>` with two USWDS radios ("This site" vs "All Maryland.gov sites").

The **pop-out** variant adds a circular ink-colored icon button (`__toggle`) that expands the search form to its right via absolute positioning. When open, the toggle's icon swaps from `search` to `close`. The form is shown as a 240px-wide (`mobile-lg`) widget with drop shadow.

The **hero** variant wraps the static form in a `maryland-search-hero` section with a large `<h1>` ("Search Results for '{keywords}'", 40–48px Merriweather light), a 32px bottom padding, and a 1px `base-light` bottom border. Used at the top of a search-results page.

The results container (`maryland-search-results`) is just a `grid-container("tablet-lg")` styled wrapper around the Google CSE-rendered results.

## Variants

| Variant | Visual |
|---|---|
| Static (`staticForm`) | The default inline form. Label, input, button, optional scope radios. |
| Pop-out (`popOut`) | Hidden form behind a circular icon toggle. |
| Hero block (`heroBlock`) | Above-the-fold search results page header with the static form below an `<h1>`. |
| Results (`searchResults`) | A `maryland-search-results` wrapper around Google CSE markup. The MDWDS Google CSE wrapper relies on Google's default styling within the wrapper. |

## When to use

- **Static** — Site search in the header (paired with `maryland-header__search`). Or in a sidebar.
- **Pop-out** — Header search icon when space is tight.
- **Hero block + results** — Dedicated `/search` results page.

## Default markup — static form

```html
<div class="maryland-search-form">
  <form action="/search" role="search" class="maryland-search-form__form">
    <label class="maryland-search-form__label" for="site-search">Search Maryland.gov</label>
    <div class="maryland-search-form__widget">
      <input
        class="maryland-search-form__input"
        type="text"
        autocomplete="on"
        name="q"
        placeholder="How do I…"
        id="site-search"
      />
      <button type="submit" class="maryland-search-form__submit">Search</button>
    </div>
  </form>
</div>
```

## Markup — static form with scope radios

```html
<div class="maryland-search-form">
  <form action="/search" role="search" class="maryland-search-form__form">
    <label class="maryland-search-form__label" for="dnr-search">Search Maryland.gov</label>
    <div class="maryland-search-form__widget">
      <input class="maryland-search-form__input" type="text" name="q" id="dnr-search" placeholder="How do I…" />
      <button type="submit" class="maryland-search-form__submit">Search</button>
    </div>

    <fieldset class="usa-fieldset maryland-search-form__scope">
      <legend class="usa-sr-only">Select a search scope</legend>
      <div class="usa-radio">
        <input class="usa-radio__input" id="scope-site" type="radio" name="scope" value="dnr.maryland.gov" checked />
        <label class="usa-radio__label" for="scope-site">dnr.maryland.gov</label>
      </div>
      <div class="usa-radio">
        <input class="usa-radio__input" id="scope-all" type="radio" name="scope" value="all" />
        <label class="usa-radio__label" for="scope-all">All Maryland.gov sites</label>
      </div>
    </fieldset>
  </form>
</div>
```

## Markup — pop-out

```html
<div class="maryland-search-form maryland-search-form--toggleable">
  <form class="maryland-search-form__form" id="popout-search" role="search" action="/search" hidden>
    <label for="popout-input" class="usa-sr-only">Search</label>
    <div class="maryland-search-form__widget">
      <input class="maryland-search-form__input" type="text" name="q" autocomplete="on" id="popout-input" />
      <button type="submit" aria-label="Submit Search" class="maryland-search-form__submit"></button>
    </div>
  </form>
  <a href="#!" class="maryland-search-form__toggle" aria-label="Site search"></a>
</div>
```

`mdwds-core.js` wires up the toggle to show/hide the `__form` and update the toggle's `aria-expanded`.

## Markup — hero block (search results page header)

```html
<section class="maryland-search-hero" aria-labelledby="search-title">
  <h1 class="maryland-search-hero__title" id="search-title">Search Results for "fishing license"</h1>
  <div class="maryland-search-form">
    <form action="/search" role="search" class="maryland-search-form__form">
      <label class="maryland-search-form__label usa-sr-only" for="results-search">Search</label>
      <div class="maryland-search-form__widget">
        <input class="maryland-search-form__input" type="text" name="q" id="results-search" placeholder="How do I…" value="fishing license" />
        <button type="submit" class="maryland-search-form__submit">Search</button>
      </div>
      <!-- scope radios as above -->
    </form>
  </div>
</section>
<div class="maryland-search-results">
  <!-- Google CSE renders results here -->
</div>
```

## What each class does

| Class | Effect |
|---|---|
| `maryland-search-form` | Outer wrapper. Position relative. |
| `maryland-search-form--toggleable` | Marker for pop-out behavior. Positions the form absolutely to the left of the toggle when expanded; adds a drop shadow. |
| `maryland-search-form__form` | The `<form>`. In pop-out mode, becomes a 240px absolutely-positioned panel; in static mode, full-width inline. |
| `maryland-search-form__label` | The `<label>`. body-8 (20px) semibold. 16px bottom margin. |
| `maryland-search-form__widget` | Flex row holding input + button. body-6 (20px) line-1 font. Has a `::before` search-glyph icon positioned absolutely on the left of the input (mask via `search` Material Symbols). |
| `maryland-search-form__input` | The `<input>`. Full-width, 1px `base-darkest` border, 12px vertical / 48px left / 8px right padding. Placeholder uses `base-darkest`. Focus outline 3px. |
| `maryland-search-form__submit` | The submit `<button>`. Ink background, white text, semibold, 12/20px padding, right corners rounded. Hover/focus turns Maryland blue. In pop-out, often icon-only with `aria-label`. |
| `maryland-search-form__scope` | Scope `<fieldset>`. Flex row of radios with 12/32px gap. 16px top margin. |
| `maryland-search-form__toggle` | Pop-out circular icon button. 48×48px ink-colored disc with white search icon. Hover turns Maryland blue. When `aria-expanded="true"`, the icon swaps to `close`. |
| `maryland-search-hero` | Search-results page hero. `grid-container("tablet-lg")`. 32px bottom padding, 1px `base-light` bottom border, 24px bottom margin. |
| `maryland-search-hero__title` | The `<h1>`. Heading-11 (40px) / heading-14 (48px at tablet+) Merriweather light. 32px bottom margin. |
| `maryland-search-results` | Wrapper around the rendered Google CSE results. `grid-container("tablet-lg")` so results align to the same width as the hero. |

## Prop schema

| Function | Prop | Type | Default | Notes |
|---|---|---|---|---|
| `staticForm` | `hideSearchLabel` | bool | false | Visually hide the label (still readable to screen readers). |
| `staticForm` | `includeScope` | bool | false | Show the "this site / all sites" scope radios. |
| `heroBlock` | `keywords` | string | — | Initial search query (shown in the `<h1>`). |
| `popOut` | — | — | — | Pop-out has no args; the JS handles toggling. |

## Heading level adjustment

The hero block uses `<h1>` because it's a page-level hero on a dedicated search-results page. Static and pop-out forms have no heading of their own — they live inside other sections.

## Common mistakes

1. **Multiple `<h1>` on a page** — if the search form sits on a page that already has a hero `<h1>`, use the static form (no `<h1>`) instead of `heroBlock`.
2. **Forgetting `role="search"` on the `<form>`** — the form needs the search landmark for screen-reader navigation.
3. **Skipping the `<label>` (or `usa-sr-only` label)** — every input needs a label. Visually hidden labels are fine for icon-only contexts.
4. **Static markup for what should be a pop-out** — if header space is tight, use the pop-out and let the JS toggle handle the visibility.
5. **Manually styling the GSE results** — the MDWDS Google CSE wrapper relies on Google's defaults. Rely on Google's defaults and only override at the wrapper level.
6. **Search button without an accessible name in icon-only mode** — supply `aria-label="Submit Search"` when the button has no visible text.
7. **Forgetting to load `mdwds-core.js`** — the pop-out toggle won't work without it.
