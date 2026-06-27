# usa-language-selector

A language switcher dropdown for multi-language Maryland.gov pages. Renders as a single button labeled "Languages" (or your custom label) that expands a menu of language options listing each language's native name (Español, 中文, العربية, Tiếng Việt, etc.). Each option links to the equivalent page in that language.

## What it looks like

The USWDS Language Selector is built on the USWDS accordion pattern. It consists of:

- A wrapping `<div class="usa-language-container">` (with `usa-language--small` modifier in the small variant).
- An outer list `<ul class="usa-language__primary usa-accordion">`.
- A single list item `<li class="usa-language__primary-item">` containing:
  - A trigger `<button class="usa-button usa-language__link">` — visually a small Maryland blue button (`usa-button` styling) showing the trigger label ("Languages") with `aria-expanded` state. The button toggles the submenu.
  - A `<ul class="usa-language__submenu" hidden>` with one `<li>` per language. Each `<li class="usa-language__submenu-item">` contains an `<a>` to the localized URL. The link content is a `<span lang="es" xml:lang="es"><strong>Español</strong></span>` — the native name in bold, with the correct `lang` attribute so screen readers pronounce it in the right language.

When the trigger is clicked, `aria-expanded` flips to `true`, the `hidden` attribute is removed from the submenu, and the dropdown appears below the trigger. Visually the dropdown is a white panel with a thin border / drop shadow, listing the languages stacked vertically. Each link has hover (darkens), focus (focus ring), and visited states.

Variants:

- **Default** — Trigger button at standard `usa-button` size (semibold, ≈17px, padding 8/16px). Dropdown panel is the normal width.
- **`usa-language--small`** — Compact trigger and dropdown. Useful for tight header strips (utility nav).
- **`usa-language--big`** — Larger trigger button to match a `usa-button--big` size, for prominent placement (e.g., a centered language picker on the homepage).

Two structural patterns:

- **Two-language toggle** — When only two languages are offered, the language selector is sometimes rendered as a single inline button labeled with the *other* language ("Español" when on the English page) rather than a dropdown — but the canonical USWDS pattern still uses the dropdown structure with two items inside. The Maryland stories use the dropdown pattern uniformly.
- **Multi-language dropdown** — Three or more languages. The dropdown is the only ergonomic option; a row of inline buttons consumes too much space.

## Variants

| Variant | Class | Visual |
|---|---|---|
| Default | `usa-language-container` | Standard trigger + dropdown |
| Small | `usa-language-container usa-language--small` | Compact for utility-nav strips |
| Big | `usa-language-container usa-language--big` | Larger trigger for prominent placement |

## When to use which variant

- **Default** — Most Maryland.gov pages with multiple language options. Place it in the utility nav at the top of `maryland-header`.
- **Small** — When space is at a premium (e.g., a compact utility strip alongside other nav items).
- **Big** — On the homepage hero or a dedicated language-selection page where the picker is the primary affordance.
- **Two-language case** — Even for English + Spanish only, use the dropdown pattern. It scales gracefully if more languages are added later.

## Default markup

```html
<div class="usa-language-container">
  <ul class="usa-language__primary usa-accordion">
    <li class="usa-language__primary-item">
      <button
        class="usa-button usa-language__link"
        aria-expanded="false"
        aria-controls="language-menu"
      >
        Languages
      </button>
      <ul id="language-menu" class="usa-language__submenu" hidden>
        <li class="usa-language__submenu-item">
          <a href="/" title="English">
            <span lang="en" xml:lang="en"><strong>English</strong></span>
          </a>
        </li>
        <li class="usa-language__submenu-item">
          <a href="/es" title="Español | Spanish">
            <span lang="es" xml:lang="es"><strong>Español</strong></span>
          </a>
        </li>
        <li class="usa-language__submenu-item">
          <a href="/zh" title="中文 | Chinese">
            <span lang="zh" xml:lang="zh"><strong>中文</strong></span>
          </a>
        </li>
        <li class="usa-language__submenu-item">
          <a href="/ko" title="한국어 | Korean">
            <span lang="ko" xml:lang="ko"><strong>한국어</strong></span>
          </a>
        </li>
        <li class="usa-language__submenu-item">
          <a href="/vi" title="Tiếng Việt | Vietnamese">
            <span lang="vi" xml:lang="vi"><strong>Tiếng Việt</strong></span>
          </a>
        </li>
        <li class="usa-language__submenu-item">
          <a href="/language-assistance">Language assistance services</a>
        </li>
      </ul>
    </li>
  </ul>
</div>
```

The final `<li>` ("Language assistance services") is the optional **additional link** at the bottom of the dropdown — used to point to a state language-access policy or assistance page.

## Markup — small (utility nav)

```html
<div class="usa-language-container usa-language--small">
  <ul class="usa-language__primary usa-accordion">
    <li class="usa-language__primary-item">
      <button
        class="usa-button usa-language__link"
        aria-expanded="false"
        aria-controls="utility-language-menu"
      >
        Languages
      </button>
      <ul id="utility-language-menu" class="usa-language__submenu" hidden>
        <li class="usa-language__submenu-item">
          <a href="/" title="English">
            <span lang="en" xml:lang="en"><strong>English</strong></span>
          </a>
        </li>
        <li class="usa-language__submenu-item">
          <a href="/es" title="Español | Spanish">
            <span lang="es" xml:lang="es"><strong>Español</strong></span>
          </a>
        </li>
      </ul>
    </li>
  </ul>
</div>
```

## Markup — big

```html
<div class="usa-language-container usa-language--big">
  <ul class="usa-language__primary usa-accordion">
    <li class="usa-language__primary-item">
      <button
        class="usa-button usa-language__link"
        aria-expanded="false"
        aria-controls="big-language-menu"
      >
        Select your language
      </button>
      <ul id="big-language-menu" class="usa-language__submenu" hidden>
        <li class="usa-language__submenu-item">
          <a href="/es" title="Español | Spanish">
            <span lang="es" xml:lang="es"><strong>Español</strong></span>
          </a>
        </li>
        <li class="usa-language__submenu-item">
          <a href="/zh" title="中文 | Chinese">
            <span lang="zh" xml:lang="zh"><strong>中文</strong></span>
          </a>
        </li>
      </ul>
    </li>
  </ul>
</div>
```

## Markup — two-language inline toggle

When only two languages are supported and a dropdown feels heavy, the same structure can render as a single-item dropdown:

```html
<div class="usa-language-container">
  <ul class="usa-language__primary usa-accordion">
    <li class="usa-language__primary-item">
      <button
        class="usa-button usa-language__link"
        aria-expanded="false"
        aria-controls="two-lang-menu"
      >
        Languages
      </button>
      <ul id="two-lang-menu" class="usa-language__submenu" hidden>
        <li class="usa-language__submenu-item">
          <a href="/es" title="Español | Spanish">
            <span lang="es" xml:lang="es"><strong>Español</strong></span>
          </a>
        </li>
      </ul>
    </li>
  </ul>
</div>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-language-container` | Outer wrapper. Sets positioning context for the absolutely-positioned dropdown panel. |
| `usa-language--small` | Compact modifier — reduces trigger button size and dropdown padding to fit a utility nav. |
| `usa-language--big` | Enlarges the trigger button to match `usa-button--big` proportions for hero / homepage placement. |
| `usa-language__primary` | The outer `<ul>` holding the trigger item. Removes list bullets. |
| `usa-accordion` | Marks the wrapping list as an accordion so the USWDS JS toggles `aria-expanded` on click and shows/hides the submenu. **Required** for the dropdown to function. |
| `usa-language__primary-item` | The `<li>` containing the trigger button + its submenu. |
| `usa-language__link` | The trigger `<button>`. Combined with `usa-button` for the Maryland-blue filled appearance; adds a chevron / down-arrow indicator after the label and rotates it when `aria-expanded="true"`. |
| `usa-language__submenu` | The dropdown `<ul>`. Hidden by default via the HTML `hidden` attribute. When the trigger expands, the JS removes `hidden` and the dropdown appears below the trigger with a white background, thin border, and subtle shadow. |
| `usa-language__submenu-item` | Each `<li>` inside the dropdown. Vertical padding for tap-target sizing. The contained `<a>` fills the row; hover darkens the row background. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `triggerLabel` | string | `"Languages"` | Text on the dropdown trigger button. |
| `languages` | array of `{ native, english, lang, url }` | seven sample languages | Each entry becomes a `<li>` with `<a>` containing `<span lang="{lang}">{native}</span>`. The `english` value is used for the `title` tooltip. |
| `size` | `default` \| `small` | `default` | Adds `usa-language--small`. (The Maryland stories don't expose `big` explicitly, but the USWDS class is supported.) |
| `includeAdditionalLink` | boolean | `true` | Appends a final `<li>` linking to a language-assistance page. |
| `additionalLinkText` | string | `"Selected content in additional languages"` | Label for the additional link. |
| `additionalLinkUrl` | string | `"javascript:void(0)"` | URL for the additional link. |
| `ariaLabel` | string | `""` | Overrides the trigger button's screen-reader label. |
| `enableAnalytics` | boolean | `false` | Adds `data-ga-*` to trigger and each language link. |
| `gaCategory` | string | `"Language Selector"` | GA category. |
| `gaAction` | string | `"Change Language"` | GA action. |
| `gaLabel` | string | `"Language Selection"` | GA label. |

## Accessibility

- **Native language names** — Always display the language name in its own language: `Español`, not `Spanish`. Add `lang="es"` and `xml:lang="es"` on the `<span>` so screen readers pronounce it with the correct phonetic engine.
- **`title` attribute** — Provide both native and English names in the `title` attribute (`title="Español | Spanish"`) so a sighted user hovering over the link can confirm.
- **`aria-expanded` on the trigger** — Toggles `true` / `false` as the dropdown opens and closes. Required for screen reader users to know whether the menu is open.
- **`aria-controls`** — On the trigger, points to the submenu's `id`. Pairs the toggle with the panel.
- **`hidden` attribute on the submenu** — Required initial state. The USWDS JS toggles it. Don't use `display: none` inline — `hidden` is the standard hook.
- **Keyboard navigation** — The USWDS accordion JS handles Enter / Space to toggle and Escape to close. Tab moves focus through the language links inside the open dropdown.
- **Focus visible** — Trigger button gets the 2px Maryland blue focus ring; each language link gets the standard link focus treatment.
- **`<strong>` inside the link** — Used to bold the language name. Decorative; screen readers don't treat `<strong>` as a heading.
- **Page `<html lang>`** — Once the user clicks a language link and lands on the localized page, update `<html lang="es">` (etc.) so the entire page's pronunciation switches.

## JS requirements

**Yes — requires the USWDS JavaScript** for the accordion / dropdown behavior. The MDWDS CDN bundle includes the USWDS JS automatically (`mdwds-core.js`); when that's loaded, the language selector dropdown works without additional configuration.

The JS:
- Listens for clicks on `.usa-language__link`,
- Toggles `aria-expanded` on the trigger,
- Toggles the `hidden` attribute on `.usa-language__submenu`,
- Closes the dropdown on outside click and on Escape.

If you're embedding this in a non-MDWDS context (without `mdwds-core.js`), you must load `@uswds/uswds/dist/js/uswds.min.js` for the accordion behavior.

## Common mistakes

1. **Missing `lang` on the language name `<span>`** — Without `lang="es"`, screen readers pronounce "Español" using the English phonetic engine ("Es-pa-NOL"). Always add `lang` + `xml:lang`.
2. **Showing English names ("Spanish") instead of native names ("Español")** — A Spanish speaker may not recognize "Spanish". Native names first.
3. **No `aria-expanded` / `aria-controls`** — Screen reader users can't tell the dropdown is open or which panel the button controls. Required.
4. **Forgetting the `hidden` attribute initially** — The submenu shows on page load, then snaps closed when JS runs. Mark it `hidden` initially.
5. **Loading the component without the USWDS JS** — The dropdown won't open. The CDN's `mdwds-core.js` covers this; if you're outside MDWDS, load USWDS JS separately.
6. **Translating the dropdown trigger label** — On a Spanish page, the trigger should say "Idiomas" (or "Cambiar idioma"), not "Languages". Localize the `triggerLabel`.
7. **Duplicate `id` on `<ul class="usa-language__submenu">`** — If multiple language selectors appear on the page (header + footer), each must have a unique `id` since `aria-controls` is keyed by `id`.
