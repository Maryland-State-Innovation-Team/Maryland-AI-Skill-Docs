# Recipe: Maryland Homepage

This is the recipe for the maryland.gov state homepage itself — the single front door for the whole state government. It uses the `landing-main` hero variant: a full-bleed landscape photograph (Maryland forests, farmland, or the Chesapeake Bay Bridge) overlaid with a centered "Welcome to Maryland" eyebrow + title, and a short subhead. Below the hero, the page surfaces agency tiles and top tasks rather than a single agency's services.

Visually the page reads: thin gray banner → maryland-branded header (no agency name, since this *is* Maryland.gov) → enormous photographic hero with eyebrow + title → agency tiles → top tasks → news strip → statewide footer (no per-agency footer above it).

> **Important:** Do not simplify the markup below — every BEM modifier class and wrapper element is required by either the CDN stylesheet or the JS bundle. If you need to modify a component, read its file under `cdn/components/` first.

## When to use this recipe

- The maryland.gov landing page — the single state-level homepage.
- A whole-of-state campaign landing page (e.g. a multi-agency initiative front page) that follows maryland.gov branding rather than any single agency's.
- Any page where the visitor's first job is "pick an agency or a top task" rather than "do an agency-specific thing."

This is **not** the recipe for an agency homepage — use `agency-homepage.md` for that. The distinguishing trait of this recipe is the `landing-main` hero, which has no buttons and no description-with-CTAs; it's branding-first.

## Page structure

1. `usa-skipnav`
2. `usa-banner` (statewide; the `Maryland.gov` link is hidden because this *is* Maryland.gov)
3. Optional global alert
4. `maryland-header` with **no** agency name — just the horizontal Maryland wordmark
5. `<main>` opens
6. `maryland-hero` with `variant="landing-main"`, full-bleed `backgroundImage` (forest / farmland / bridge)
7. Page-content sections inside `<div class="grid-container">`:
   - Top services — `maryland-card` (`linked` variant) for tile-style quick links
   - Government & agencies — `maryland-card` (`simple` variant) group
   - Stats — `maryland-statistic-list`
   - News from Maryland — `usa-collection`
8. `<main>` closes
9. **No** `maryland-footer` (per-agency footer is omitted on the state homepage — see `cdn/page-shell.md`)
10. `<maryland-statewide-footer>` web component

## Full assembled HTML

```html
<!doctype html>
<!-- Pin to a specific version in production. See cdn/setup.md. -->
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Maryland.gov — The Official Website of the State of Maryland</title>

    <!-- Inline init script for FOUC prevention. See cdn/setup.md. -->
    <script>
      "use strict";
      const loadingClass = "usa-js-loading";
      document.documentElement.classList.add(loadingClass);
      function revertClass() {
        document.documentElement.classList.remove(loadingClass);
      }
      const fallback = setTimeout(revertClass, 8000);
      function verifyLoaded() {
        if (window.uswdsPresent) {
          clearTimeout(fallback);
          revertClass();
          window.removeEventListener("load", verifyLoaded, true);
        }
      }
      window.addEventListener("load", verifyLoaded, true);
    </script>

    <link
      rel="stylesheet"
      data-mdwds
      href="https://cdn.maryland.gov/mdwds/latest/css/mdwds.min.css"
    />
    <script
      type="module"
      src="https://cdn.maryland.gov/mdwds/latest/js/mdwds-core.js"
    ></script>
    <script
      type="module"
      src="https://cdn.maryland.gov/mdwds/latest/js/mdwds-elements.js"
    ></script>
  </head>
  <body>
    <a class="usa-skipnav" href="#main-content">Skip to main content</a>

    <section
      class="usa-banner"
      aria-label="Official website of the State of Maryland"
    >
      <div class="usa-accordion">
        <div class="usa-banner__header">
          <div class="usa-banner__inner">
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
            </button>
            <div class="usa-banner__additional-links">
              <a
                href="https://translate.google.com/"
                class="usa-banner__additional-link usa-banner__translate-link"
                >Translate</a
              >
            </div>
          </div>
        </div>
        <div class="usa-banner__content" id="gov-banner-default" hidden>
          <div class="grid-row grid-gap-lg">
            <div class="usa-banner__guidance tablet:grid-col-6">
              <img
                class="usa-banner__icon usa-media-block__img"
                src="https://cdn.maryland.gov/mdwds/latest/img/icon-dot-gov.svg"
                role="img"
                alt=""
                aria-hidden="true"
              />
              <div class="usa-media-block__body">
                <p>
                  <strong>Official websites use .gov</strong><br />A
                  <strong>.gov</strong> website belongs to an official government
                  organization in the United States.
                </p>
              </div>
            </div>
            <div class="usa-banner__guidance tablet:grid-col-6">
              <img
                class="usa-banner__icon usa-media-block__img"
                src="https://cdn.maryland.gov/mdwds/latest/img/icon-https.svg"
                role="img"
                alt=""
                aria-hidden="true"
              />
              <div class="usa-media-block__body">
                <p>
                  <strong>Secure .gov websites use HTTPS</strong><br />A
                  <strong>lock</strong> or <strong>https://</strong> means you've
                  safely connected to the .gov website.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <header class="maryland-header">
      <div class="maryland-header__util-nav-container">
        <ul class="maryland-header__util-nav">
          <li><a href="/services">Services</a></li>
          <li><a href="/agencies">Agencies</a></li>
        </ul>
      </div>

      <a class="maryland-header__home" href="/">
        <img
          class="maryland-header__logo"
          src="https://cdn.maryland.gov/mdwds/latest/img/md_wordmark_horizontal.svg"
          alt="Maryland.gov home"
        />
      </a>

      <nav class="maryland-nav">
        <button
          class="maryland-nav__toggle"
          aria-label="Toggle Nav"
          type="button"
        ></button>
        <div class="maryland-nav__mobile-panel" id="md-nav-panel-state">
          <ul class="maryland-nav__items maryland-nav__items--level-one">
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/residents"
                >Residents</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/businesses"
                >Businesses</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/government"
                >Government</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/agencies"
                >Agencies</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/visiting"
                >Visiting</a
              >
            </li>
          </ul>
        </div>
      </nav>

      <hr aria-hidden="true" class="maryland-header__divider" />
    </header>

    <main id="main-content" tabindex="-1">
      <section
        class="maryland-hero maryland-hero--landing-main"
        aria-labelledby="hero-title"
      >
        <div class="maryland-hero__background-image">
          <img
            src="https://cdn.maryland.gov/mdwds/latest/img/md_forest.png"
            alt=""
          />
        </div>
        <div class="maryland-hero__container">
          <div class="grid-container">
            <div class="grid-row">
              <div class="grid-col-12">
                <div class="maryland-hero__content">
                  <h1 id="hero-title" class="maryland-hero__title">
                    <span class="maryland-hero__eyebrow">Welcome to</span>
                    <span class="maryland-hero__title-text">Maryland</span>
                  </h1>
                  <div class="maryland-hero__description">
                    <p>
                      Services, programs, and information for the people of the
                      Old Line State.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <div class="grid-container">
        <div
          id="page-content"
          class="grid-col-12 margin-y-8 desktop:margin-top-10 desktop:margin-bottom-15"
        >
          <section class="block-spacing" aria-labelledby="top-services-heading">
            <h2 id="top-services-heading">Top services</h2>
            <ul class="maryland-card-group">
              <li class="maryland-card maryland-card--linked">
                <a
                  href="https://mva.maryland.gov"
                  class="maryland-card__link"
                  aria-label="Vehicle services - renew tags, transfer titles, get a Real ID"
                >
                  <div class="maryland-card__container">
                    <div class="maryland-card__header">
                      <h3 class="maryland-card__heading">Vehicle services</h3>
                    </div>
                    <div class="maryland-card__body">
                      <p>
                        Renew tags, transfer titles, get a Real ID at the MVA.
                      </p>
                    </div>
                    <div
                      class="maryland-card__footer maryland-card__footer--right"
                    >
                      <span
                        class="maryland-card__icon maryland-card__icon--arrow"
                        aria-hidden="true"
                      ></span>
                    </div>
                  </div>
                </a>
              </li>
              <li class="maryland-card maryland-card--linked">
                <a
                  href="https://dhs.maryland.gov/supplemental-nutrition-assistance-program/"
                  class="maryland-card__link"
                  aria-label="Food assistance and SNAP - apply for SNAP, WIC, and other nutrition programs"
                >
                  <div class="maryland-card__container">
                    <div class="maryland-card__header">
                      <h3 class="maryland-card__heading">
                        Food assistance &amp; SNAP
                      </h3>
                    </div>
                    <div class="maryland-card__body">
                      <p>
                        Apply for SNAP, WIC, and other nutrition programs.
                      </p>
                    </div>
                    <div
                      class="maryland-card__footer maryland-card__footer--right"
                    >
                      <span
                        class="maryland-card__icon maryland-card__icon--arrow"
                        aria-hidden="true"
                      ></span>
                    </div>
                  </div>
                </a>
              </li>
              <li class="maryland-card maryland-card--linked">
                <a
                  href="https://www.marylandtaxes.gov/individual/index.php"
                  class="maryland-card__link"
                  aria-label="Pay state taxes - file Maryland income tax online"
                >
                  <div class="maryland-card__container">
                    <div class="maryland-card__header">
                      <h3 class="maryland-card__heading">Pay state taxes</h3>
                    </div>
                    <div class="maryland-card__body">
                      <p>File Maryland income tax online.</p>
                    </div>
                    <div
                      class="maryland-card__footer maryland-card__footer--right"
                    >
                      <span
                        class="maryland-card__icon maryland-card__icon--arrow"
                        aria-hidden="true"
                      ></span>
                    </div>
                  </div>
                </a>
              </li>
              <li class="maryland-card maryland-card--linked">
                <a
                  href="https://elections.maryland.gov/voter_registration/index.html"
                  class="maryland-card__link"
                  aria-label="Register to vote in Maryland"
                >
                  <div class="maryland-card__container">
                    <div class="maryland-card__header">
                      <h3 class="maryland-card__heading">Register to vote</h3>
                    </div>
                    <div class="maryland-card__body">
                      <p>
                        Sign up online, by mail, or at any MVA office.
                      </p>
                    </div>
                    <div
                      class="maryland-card__footer maryland-card__footer--right"
                    >
                      <span
                        class="maryland-card__icon maryland-card__icon--arrow"
                        aria-hidden="true"
                      ></span>
                    </div>
                  </div>
                </a>
              </li>
            </ul>
          </section>

          <section class="block-spacing" aria-labelledby="agencies-heading">
            <h2 id="agencies-heading">Explore Maryland agencies</h2>
            <ul class="maryland-card-group">
              <li class="maryland-card maryland-card--simple">
                <div class="maryland-card__container">
                  <div class="maryland-card__header">
                    <h3 class="maryland-card__heading">
                      Department of Health
                    </h3>
                  </div>
                  <div class="maryland-card__body">
                    <p>
                      Medicaid, public health, vital records, and more.
                    </p>
                  </div>
                  <div
                    class="maryland-card__footer maryland-card__footer--left"
                  >
                    <div class="maryland-card__footer-content">
                      <a
                        href="https://health.maryland.gov"
                        class="usa-button usa-button--primary"
                        >Visit MDH</a
                      >
                    </div>
                  </div>
                </div>
              </li>
              <li class="maryland-card maryland-card--simple">
                <div class="maryland-card__container">
                  <div class="maryland-card__header">
                    <h3 class="maryland-card__heading">
                      Department of Transportation
                    </h3>
                  </div>
                  <div class="maryland-card__body">
                    <p>
                      MVA, transit, highways, BWI Marshall, and the Port of
                      Baltimore.
                    </p>
                  </div>
                  <div
                    class="maryland-card__footer maryland-card__footer--left"
                  >
                    <div class="maryland-card__footer-content">
                      <a
                        href="https://www.mdot.maryland.gov"
                        class="usa-button usa-button--primary"
                        >Visit MDOT</a
                      >
                    </div>
                  </div>
                </div>
              </li>
              <li class="maryland-card maryland-card--simple">
                <div class="maryland-card__container">
                  <div class="maryland-card__header">
                    <h3 class="maryland-card__heading">
                      Department of Natural Resources
                    </h3>
                  </div>
                  <div class="maryland-card__body">
                    <p>
                      State parks, fishing and hunting, boating, and the
                      Chesapeake Bay.
                    </p>
                  </div>
                  <div
                    class="maryland-card__footer maryland-card__footer--left"
                  >
                    <div class="maryland-card__footer-content">
                      <a
                        href="https://dnr.maryland.gov"
                        class="usa-button usa-button--primary"
                        >Visit DNR</a
                      >
                    </div>
                  </div>
                </div>
              </li>
            </ul>
            <p class="margin-top-4">
              <a href="/agencies" class="maryland-link"
                >See all Maryland agencies</a
              >
            </p>
          </section>

          <section class="block-spacing" aria-labelledby="stats-heading">
            <h2 id="stats-heading">Maryland by the numbers</h2>
            <ul class="maryland-statistic-list">
              <li class="maryland-statistic-list__item">
                <span class="maryland-statistic-list__value">6.2M</span>
                <span class="maryland-statistic-list__label">Residents</span>
              </li>
              <li class="maryland-statistic-list__item">
                <span class="maryland-statistic-list__value">23</span>
                <span class="maryland-statistic-list__label"
                  >Counties + Baltimore City</span
                >
              </li>
              <li class="maryland-statistic-list__item">
                <span class="maryland-statistic-list__value">76</span>
                <span class="maryland-statistic-list__label"
                  >State parks</span
                >
              </li>
              <li class="maryland-statistic-list__item">
                <span class="maryland-statistic-list__value">3,190</span>
                <span class="maryland-statistic-list__label"
                  >Miles of Chesapeake Bay shoreline</span
                >
              </li>
            </ul>
          </section>

          <section class="block-spacing" aria-labelledby="news-heading">
            <h2 id="news-heading">News from Maryland</h2>
            <ul class="usa-collection">
              <li class="usa-collection__item">
                <div class="usa-collection__body">
                  <h3 class="usa-collection__heading">
                    <a class="usa-link" href="/news/governor-budget-2026"
                      >Governor signs FY 2027 budget into law</a
                    >
                  </h3>
                  <p class="usa-collection__description">
                    The bipartisan budget invests in education, transportation,
                    and the Chesapeake Bay.
                  </p>
                  <ul class="usa-collection__meta" aria-label="More information">
                    <li class="usa-collection__meta-item">
                      <time datetime="2026-04-22">April 22, 2026</time>
                    </li>
                    <li class="usa-collection__meta-item usa-tag">
                      Office of the Governor
                    </li>
                  </ul>
                </div>
              </li>
              <li class="usa-collection__item">
                <div class="usa-collection__body">
                  <h3 class="usa-collection__heading">
                    <a class="usa-link" href="/news/real-id-deadline"
                      >Federal REAL ID enforcement deadline approaches</a
                    >
                  </h3>
                  <p class="usa-collection__description">
                    Marylanders flying domestically after May 7 will need a
                    REAL ID or another federally-accepted document.
                  </p>
                  <ul class="usa-collection__meta" aria-label="More information">
                    <li class="usa-collection__meta-item">
                      <time datetime="2026-04-18">April 18, 2026</time>
                    </li>
                    <li class="usa-collection__meta-item usa-tag">MVA</li>
                  </ul>
                </div>
              </li>
            </ul>
          </section>
        </div>
      </div>
    </main>

    <maryland-statewide-footer></maryland-statewide-footer>
  </body>
</html>
```

## Section-by-section breakdown

### 1. Shell — skipnav, banner, header

Standard skipnav + statewide banner. Note that on the state homepage we **omit** the `Maryland.gov` link in the banner's `usa-banner__additional-links` (since you're already on Maryland.gov) and the `maryland-header` uses the horizontal wordmark with no agency name suffix. The banner's expanded content uses `usa-banner__guidance` columns with `usa-media-block__img` icons inside `usa-media-block__body`. See [page-shell.md](../page-shell.md), [usa-banner](../components/usa-banner.md), and [maryland-header](../components/maryland-header.md).

The header uses `maryland-header__util-nav-container` wrapping the `maryland-header__util-nav` `<ul>`, the `maryland-header__home` anchor wrapping the horizontal `maryland-header__logo` image (no `maryland-header__agency` span here — state homepage only), the `maryland-nav` block, and a closing `maryland-header__divider` hr.

Inside `maryland-nav`, the canonical structure is `<nav class="maryland-nav">` → `<button class="maryland-nav__toggle">` + `<div class="maryland-nav__mobile-panel">` → `<ul class="maryland-nav__items maryland-nav__items--level-one">` → `<li class="maryland-nav__item maryland-nav__item--level-one">` → `<a class="maryland-nav__link maryland-nav__link--level-one">`. **Do not** flatten to `<ul class="maryland-nav__list">` with bare `__item` / `__link` — the JS bundle's nav init looks for the `__toggle` button + `__mobile-panel` panel and the `--level-one` modifier classes are required for the correct typography, borders, and hover states. See [maryland-nav](../components/maryland-nav.md).

### 2. Hero — `landing-main` variant

`maryland-hero` with `variant="landing-main"` is the only variant that takes a full-bleed `backgroundImage` (options: `forest`, `farmland`, `bridge`). The title "Welcome to Maryland" auto-styles "Welcome to" as a small eyebrow above the large word "Maryland"; in hand-written markup, include the `<span class="maryland-hero__eyebrow">` and `<span class="maryland-hero__title-text">` explicitly inside the `<h1 class="maryland-hero__title">`. The hero requires the `maryland-hero__container` wrapper, and on `landing-main` the content sits inside a nested `grid-container > grid-row > grid-col-12 > maryland-hero__content`. There are no description-with-buttons here: the hero is purely a brand statement. See [maryland-hero](../components/maryland-hero.md).

```html
<section class="maryland-hero maryland-hero--landing-main" aria-labelledby="hero-title">
  <div class="maryland-hero__background-image"><img src="..." alt="" /></div>
  <div class="maryland-hero__container">
    <div class="grid-container">
      <div class="grid-row">
        <div class="grid-col-12">
          <div class="maryland-hero__content">
            <h1 id="hero-title" class="maryland-hero__title">
              <span class="maryland-hero__eyebrow">Welcome to</span>
              <span class="maryland-hero__title-text">Maryland</span>
            </h1>
            <div class="maryland-hero__description"><p>Description.</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

### 3. Top services — `maryland-card` (`linked` variant)

The `linked` variant turns each tile into a single `<a class="maryland-card__link">` wrapping a `maryland-card__container` with `maryland-card__header`, `maryland-card__body`, and a `maryland-card__footer maryland-card__footer--right` containing a `maryland-card__icon maryland-card__icon--arrow` span — denser and more clickable than the `media` variant. Use 4 tiles on the homepage because that's a comfortable two-row layout on mobile (2x2) and one row on desktop (4x1). The `aria-label` on each link combines title + description. See [maryland-card](../components/maryland-card.md).

### 4. Explore Maryland agencies — `maryland-card` (`simple` variant)

For top-level agency tiles, the `simple` variant (no image, button-style CTA) reads as a directory more than as a service card. Each `<li class="maryland-card maryland-card--simple">` still requires the `maryland-card__container` wrapper around its header/body/footer. We finish the section with a `<a class="maryland-link">` pointing at the full agency directory.

### 5. By the numbers — `maryland-statistic-list`

A row of impact numbers (`6.2M residents`, `23 counties`, etc.) using `maryland-statistic-list`. This component handles the responsive 1-up / 2-up / 4-up grid and the large-numeral typography. See [maryland-statistic-list](../components/maryland-statistic-list.md).

### 6. News — `usa-collection`

Same component as on agency pages — `usa-collection` is the canonical list for news/press releases. Each `<li class="usa-collection__item">` holds a `usa-collection__body` containing a `usa-collection__heading` (with the heading link wrapped in `<a class="usa-link">`), a `usa-collection__description`, and a `usa-collection__meta` `<ul>` with `usa-collection__meta-item` entries. Dates are wrapped in `<time datetime="...">` for machine-readability. On the state homepage we'd usually link out to the cross-agency `news.maryland.gov` feed. See [usa-collection](../components/usa-collection.md).

### 7. Statewide footer — `<maryland-statewide-footer>` only

The state homepage uses **only** the statewide footer; there's no agency to put above it. The `<maryland-statewide-footer>` web component renders the full statewide directory (top services, government, policies, connect, alerts). Zero config — but the CDN stylesheet `<link>` **must carry the `data-mdwds` attribute** so the web component can adopt the styles into its shadow root. Without it, the footer renders blank. See [maryland-statewide-footer](../components/maryland-statewide-footer.md) and the note in [page-shell.md](../page-shell.md) about state-homepage footer omission.

## Common customizations

- **Change the hero background image.** Swap `md_forest.png` for `md_farmland.png` or `md_bridge.png` — those are the three documented asset names. Custom images are possible but should still be a landscape photograph of Maryland.
- **Add buttons or a description to the hero.** The `landing-main` variant doesn't render buttons by design. If you need them, you almost certainly want the `landing-agency` variant — see `cdn/recipes/agency-homepage.md`.
- **Add a global alert above the header** — drop a `<div class="maryland-alert maryland-alert--emergency">…</div>` between `usa-banner` and `maryland-header`. Use `emergency` for live incidents (hurricane warnings, statewide closures) and `info` for non-urgent notices.
- **Customize the agency tile set.** The "Explore Maryland agencies" cards can be any number of agencies; the `maryland-card-group` will reflow on its own.
- **Swap statistics for a `maryland-visual-link-collection`.** If you'd rather feature initiatives than numbers, replace the statistic list with `maryland-visual-link-collection`. See [component-index](../component-index.md).

## What you should NOT do

1. **Don't add a `maryland-footer` between `<main>` and `<maryland-statewide-footer>`.** The state homepage has no agency to represent — only the statewide footer goes on this page. (Agency homepages do show both; this one does not.)
2. **Don't put an agency name in the header.** The header logo here is the horizontal Maryland wordmark with no `<span class="maryland-header__agency">`. Adding an agency name changes the meaning of the page from "the state" to "this agency, branded as state."
3. **Don't use `landing-agency` or `landing-regular` here.** Those variants are for agency pages and interior landing pages. Only `landing-main` produces the full-bleed photographic hero.
4. **Don't write more than one `<h1>`.** The hero's `Welcome to Maryland` is the page's `<h1>`. Section headings ("Top services", "News from Maryland") are `<h2>`.
5. **Don't use a Maryland.gov link in the statewide banner.** You're already on Maryland.gov — the link goes nowhere. Set `includeMaryland: false` (or omit the `usa-banner__maryland-link`).
6. **Don't simplify `maryland-nav` markup.** The bundle's nav init requires the `__toggle` button, the `__mobile-panel` div, and the `__items--level-one` / `__item--level-one` / `__link--level-one` modifier classes. Writing `<ul class="maryland-nav__list">` with bare `__item` / `__link` breaks JS init and unstyles the nav.
7. **Don't forget the `data-mdwds` attribute on the CDN stylesheet `<link>`.** The `<maryland-statewide-footer>` web component looks up `link[rel="stylesheet"][data-mdwds]` to adopt the global stylesheet into its shadow root. Without it the footer renders blank.
