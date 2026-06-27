# usa-banner

**The required statewide banner.** Every Maryland.gov page must start with the `usa-banner` element identifying the site as official Maryland state government property. Pulls double duty with the .gov / HTTPS explainer that appears when the "Here's how you know" toggle is expanded.

> **This is non-negotiable.** State branding policy requires this banner at the top of every Maryland state web page. The `<maryland-statewide-banner>` web component is the equivalent for non-MDWDS sites — see `cdn/components/maryland-statewide-banner.md`. On full MDWDS pages, use this HTML version.

## What it looks like

A thin horizontal strip at the very top of the page (above `maryland-header`). White-ish gray background (USWDS `usa-banner` default — from upstream USWDS styles). At a glance:

- **Header row** — Maryland flag (18×13px, optional, `includeFlag`) → "An official website of the State of Maryland." in 14px (`ui-4`, line-height `ui-5`) Source Sans → "Here's how you know" toggle button with a chevron icon (20×20px, rotated -90° collapsed / 90° expanded) → (desktop only, right-aligned) "Maryland.gov" link + "Translate" link with a 20×20px globe icon, separated by a 1px `base-light` vertical divider.
- **Toggle** — `usa-banner__button` is a plain underlined button. Click toggles `aria-expanded` and shows/hides the explainer content.
- **Expanded content** — a two-column block at tablet+ (`grid-row grid-gap-lg`):
  - Left column: a `.gov` icon (gold globe with "USA"), then **"Official websites use .gov"** (bold) + "A **.gov** website belongs to an official government organization in the United States."
  - Right column: a closed-padlock icon, then **"Secure .gov websites use HTTPS"** (bold) + "A **lock** (icon) or **https://** means you've safely connected to the .gov website. Share sensitive information only on official, secure websites."

The site-margins mixin keeps content aligned with the page's grid container.

**Below `desktop` (1024px):** the "Maryland.gov" additional link hides (`display: none`); the Translate link stays. The "Here's how you know" toggle and the official-website text remain inline.

**Below `tablet` (640px):** the expanded block stacks the two columns into one.

## Variants

Two configuration variants via props (no separate class modifiers):

| Variant | Effect |
|---|---|
| Default | Flag off, Maryland.gov link on, Translate link on. |
| With flag (`includeFlag: true`) | Adds the Maryland flag image to the left of the official-website text. |
| With global alert (`includeAlert: true`) | Renders a `maryland-alert--warning` below the banner. Used for state-wide notices. |

## Default markup

```html
<section class="usa-banner" aria-label="Official website of the State of Maryland">
  <div class="usa-accordion">
    <div class="usa-banner__header">
      <div class="usa-banner__inner">
        <!-- Optional: Maryland flag -->
        <img
          aria-hidden="true"
          class="usa-banner__header-flag"
          src="/img/md_flag.svg"
          alt=""
          width="18"
          height="13"
        />

        <p class="usa-banner__header-text">
          An official website of the State of Maryland.
        </p>

        <button
          type="button"
          class="usa-banner__button"
          aria-expanded="false"
          aria-controls="gov-banner-default"
        >
          Here's how you know
          <svg role="img" aria-hidden="true" aria-label="Toggle button" xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="currentColor">
            <path d="M576-253.85 349.85-480 576-706.15 613.15-669l-189 189 189 189L576-253.85Z"/>
          </svg>
        </button>

        <!-- Right-side additional links (desktop only for Maryland.gov; always for Translate) -->
        <div class="usa-banner__additional-links">
          <a href="https://maryland.gov" class="usa-banner__additional-link usa-banner__maryland-link">
            Maryland.gov
          </a>
          <a
            href="https://translate.google.com/translate?u=https%3A%2F%2Fdnr.maryland.gov%2F"
            class="usa-banner__additional-link usa-banner__translate-link"
          >
            <svg role="img" aria-hidden="true" aria-label="Globe" xmlns="http://www.w3.org/2000/svg" fill="currentColor" height="20px" viewBox="0 -960 960 960" width="20px">
              <!-- Globe icon path -->
              <path d="M480-116q-75.15 0-141.5-28.46t-115.96-78.08..."/>
            </svg>
            Translate
          </a>
        </div>
      </div>
    </div>

    <!-- Expanded explainer content -->
    <div class="usa-banner__content" id="gov-banner-default" hidden>
      <div class="grid-row grid-gap-lg">
        <div class="usa-banner__guidance tablet:grid-col-6">
          <img class="usa-banner__icon usa-media-block__img" src="/img/icon-dot-gov.svg" role="img" alt="" aria-hidden="true" />
          <div class="usa-media-block__body">
            <p>
              <strong>Official websites use .gov</strong><br />
              A <strong>.gov</strong> website belongs to an official government organization in the United States.
            </p>
          </div>
        </div>
        <div class="usa-banner__guidance tablet:grid-col-6">
          <img class="usa-banner__icon usa-media-block__img" src="/img/icon-https.svg" role="img" alt="" aria-hidden="true" />
          <div class="usa-media-block__body">
            <p>
              <strong>Secure .gov websites use HTTPS</strong><br />
              A <strong>lock</strong> (<span class="icon-lock"><svg xmlns="http://www.w3.org/2000/svg" width="52" height="64" viewBox="0 0 52 64" class="usa-banner__lock-image" role="img" aria-labelledby="banner-lock-description-default" focusable="false"><title id="banner-lock-title-default">Lock</title><desc id="banner-lock-description-default">Locked padlock icon</desc><path fill="#000000" fill-rule="evenodd" d="M26 0c10.493 0 19 8.507 19 19v9h3a4 4 0 0 1 4 4v28a4 4 0 0 1-4 4H4a4 4 0 0 1-4-4V32a4 4 0 0 1 4-4h3v-9C7 8.507 15.507 0 26 0zm0 8c-5.979 0-10.843 4.77-10.996 10.712L15 19v9h22v-9c0-6.075-4.925-11-11-11z"/></svg></span>) or <strong>https://</strong> means you've safely connected to the .gov website. Share sensitive information only on official, secure websites.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

When the toggle button is clicked, the JS toggles `hidden` on `#gov-banner-default` and updates `aria-expanded` on the button.

## Markup — with embedded global alert below

```html
<section class="usa-banner" aria-label="Official website of the State of Maryland">
  <!-- ...same as default markup... -->
</section>

<!-- A maryland-alert immediately below for state-wide notices -->
<div class="maryland-alert maryland-alert--warning">
  <div class="maryland-alert__body">
    <h4 class="maryland-alert__heading">Severe weather advisory</h4>
    <div class="maryland-alert__text">
      <p>Coastal flood warning in effect through Friday evening. <a href="/alerts">More information</a></p>
    </div>
  </div>
</div>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-banner` | The outer `<section>`. The `aria-label="Official website of the State of Maryland"` is required for screen readers to announce the landmark. |
| `usa-accordion` | USWDS accordion wrapper enabling the toggle/expand behavior. Auto-binds the toggle button to the content panel via `aria-controls`. |
| `usa-banner__header` | The top strip (always visible). Adds `units(1.5)` vertical padding on mobile, `units(1)` at tablet+. |
| `usa-banner__inner` | Flex row inside the header. Applies site-margins so content aligns with the page grid, 4px (`units(0.5)`) gap between elements. |
| `usa-banner__header-flag` | Maryland flag image. Removes USWDS's default float; placed inline at start. |
| `usa-banner__header-text` | "An official website..." text. 14px (`ui-4`), line-height `ui-5`. On tablet+ becomes `display: inline` so it sits on the same line as the toggle. |
| `usa-banner__button` | The "Here's how you know" toggle. Inline-flex with underline, chevron SVG rotated -90° collapsed / 90° expanded. Suppresses USWDS's default `::before`/`::after` rules. |
| `usa-banner__additional-links` | Container for the right-side Maryland.gov + Translate links. Pushed to the right via `margin-inline-start: auto`. |
| `usa-banner__additional-link` | A right-side link. Uses the MDWDS `typeset-link` mixin (Maryland blue, underline). Adjacent links separated by 1px `base-light` vertical divider with 20px (`units(2.5)`) horizontal padding. |
| `usa-banner__maryland-link` | The Maryland.gov link specifically. **Hidden below desktop (1024px)** so it doesn't crowd the mobile banner. |
| `usa-banner__translate-link` | The Translate link. Always visible. The globe SVG icon precedes the text. |
| `usa-banner__content` | The expandable block. Hidden via `hidden` attribute (and `aria-hidden`) when collapsed; revealed when toggle is expanded. |
| `usa-banner__guidance` | One of the two columns in the expanded block. Each is `tablet:grid-col-6` (50/50 split at tablet+). |
| `usa-banner__icon` + `usa-media-block__img` | The .gov / lock icons in the expanded block. Sized to the USWDS media-block default. |
| `usa-banner__lock-image` | The inline SVG closed-padlock icon used inside the HTTPS explainer text. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `includeFlag` | bool | `false` | Show the Maryland flag image inside the header. |
| `includeMaryland` | bool | `true` | Render the "Maryland.gov" link in the right-side additional links. |
| `includeTranslate` | bool | `true` | Render the "Translate" link with the globe icon. The href auto-encodes the current page URL into a Google Translate URL. |
| `includeAlert` | bool | `false` | Render a `maryland-alert--warning` below the banner (used in the `WithGlobalAlert` variant). |

## Heading level adjustment

The banner has no heading by design — its landmark name comes from `aria-label="Official website of the State of Maryland"`. **Do not** add an `<h1>` or `<h2>` inside the banner. The page's `<h1>` belongs to the hero.

## Common mistakes

1. **Omitting `aria-label="Official website of the State of Maryland"`** — without it, screen readers announce the section as an unlabeled landmark. The state branding policy explicitly requires this label.
2. **Skipping the `<section class="usa-banner">` wrapper** — the banner's landmark, layout, and JS toggle all depend on this element. Without it, the toggle button doesn't work and screen readers don't announce the banner.
3. **Forgetting `aria-controls` on the toggle button** — USWDS's accordion JS needs the button's `aria-controls` to match the panel's `id`. Without it, the toggle does nothing.
4. **Hardcoding the Translate href to a specific URL** — the link should encode the **current page URL** as the parameter so users land on a translated version of the page they're on, not a fixed page. Use `?u=${encodeURIComponent(window.location.href)}` at runtime.
5. **Using this banner on a `.com` or `.org` site** — the banner says "official website of the State of Maryland" and explains how to verify a `.gov` domain. Don't use it on non-government sites; it's misleading.
6. **Wrapping it in a `<header>`** — the banner is its own landmark. An outer `<header>` makes it a `banner`-role descendant inside another `banner`, which is confusing.
7. **Reordering the banner below `maryland-header`** — the banner must come **first** in the body (after the skip-nav link). State branding before agency branding.
8. **Customizing the .gov / HTTPS explainer text** — that copy is mandated by USWDS guidance. Don't paraphrase or shorten it.
