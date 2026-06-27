# Recipe: Agency Homepage

The agency homepage is the front door for a Maryland state agency website — Department of Natural Resources, Motor Vehicle Administration, Department of Health, and so on. It uses the `landing-agency` hero variant: a two-column hero with the agency logo, a long-form description, and primary/secondary CTAs on the left, with a hero illustration or photo on the right. Below the hero, the page typically shows featured-services cards, an alert or callout for in-progress initiatives, a press/news block, and the per-agency contact footer that sits above the statewide footer.

Visually, the page reads as: thin gray statewide banner → optional global emergency alert → white agency header with wordmark + agency name and primary nav → blue agency hero with two-up content → white body with stacked sections separated by `block-spacing` → dark navy agency footer → dark navy statewide footer.

> **Important:** Do not simplify the markup below — every BEM modifier class and wrapper element is required by either the CDN stylesheet or the JS bundle. If you need to modify a component, read its file under `cdn/components/` first.

## When to use this recipe

- The landing page for a Maryland state agency (cabinet department, commission, board).
- A program-level homepage that needs the full agency branding treatment.
- Any homepage that needs the two-column hero with agency logo + image plus CTAs.
- Sites where the visitor's first job is to discover services, not to read a press release or fill a form.

## Page structure

1. `usa-skipnav` link (keyboard accessibility, target = `#main-content`)
2. `usa-banner` — the statewide "Official website of the State of Maryland" strip
3. Optional global alert (`maryland-alert`) between banner and header
4. `maryland-header` with utility nav, agency wordmark, and primary nav
5. `<main id="main-content" tabindex="-1">` opens
6. `maryland-hero` with `variant="landing-agency"`, agency logo visible, `heroStyle="with-image"`
7. Page-content sections inside `<div class="grid-container">`:
   - Featured services — `maryland-card` group (`media` variant)
   - Page-level callout (`maryland-callout`) for in-progress initiative
   - Latest news — `usa-collection` (most-recent press releases)
   - Connect with us — `maryland-link-collection`
8. `<main>` closes
9. `maryland-footer` (agency contact info)
10. `<maryland-statewide-footer>` web component

## Full assembled HTML

```html
<!doctype html>
<!-- Pin to a specific version in production. See cdn/setup.md. -->
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Maryland Department of Natural Resources</title>

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
                href="https://maryland.gov"
                class="usa-banner__additional-link usa-banner__maryland-link"
                >Maryland.gov</a
              >
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
          <li><a href="/sign-in">Sign in</a></li>
          <li><a href="/contact">Contact</a></li>
          <li>
            <a href="/licenses" class="usa-button usa-button--small">Buy a license</a>
          </li>
        </ul>
      </div>

      <a class="maryland-header__home" href="/">
        <img
          class="maryland-header__logo"
          src="https://cdn.maryland.gov/mdwds/latest/img/md_wordmark_vertical.svg"
          alt="Department of Natural Resources home"
        />
        <span class="maryland-header__agency"
          >Department of Natural Resources</span
        >
      </a>

      <nav class="maryland-nav">
        <button
          class="maryland-nav__toggle"
          aria-label="Toggle Nav"
          type="button"
        ></button>
        <div class="maryland-nav__mobile-panel" id="md-nav-panel-dnr">
          <ul class="maryland-nav__items maryland-nav__items--level-one">
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/parks"
                >State parks</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <button
                type="button"
                class="maryland-nav__link maryland-nav__link--level-one"
              >
                Fishing &amp; hunting
              </button>
              <div class="maryland-nav__children" id="nav-children-1">
                <ul class="maryland-nav__items maryland-nav__items--level-two">
                  <li class="maryland-nav__item maryland-nav__item--level-two">
                    <a
                      class="maryland-nav__link maryland-nav__link--level-two"
                      href="/fishing"
                      >Fishing licenses</a
                    >
                  </li>
                  <li class="maryland-nav__item maryland-nav__item--level-two">
                    <a
                      class="maryland-nav__link maryland-nav__link--level-two"
                      href="/hunting"
                      >Hunting licenses</a
                    >
                  </li>
                  <li class="maryland-nav__item maryland-nav__item--level-two">
                    <a
                      class="maryland-nav__link maryland-nav__link--level-two"
                      href="/crabbing"
                      >Crabbing &amp; shellfish</a
                    >
                  </li>
                </ul>
              </div>
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/boating"
                >Boating</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/wildlife"
                >Wildlife</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/about"
                >About DNR</a
              >
            </li>
          </ul>
        </div>
      </nav>

      <hr aria-hidden="true" class="maryland-header__divider" />
    </header>

    <main id="main-content" tabindex="-1">
      <div class="grid-container">
        <div class="grid-row">
          <div class="grid-col-12">
            <section
              class="maryland-hero maryland-hero--landing-agency has-illustration has-image has-logo"
              aria-labelledby="hero-title"
            >
              <div class="maryland-hero__container">
                <div class="maryland-hero__row">
                  <div class="maryland-hero__content">
                    <div class="maryland-hero__agency-logo">
                      <img src="/img/dnr-seal.svg" alt="" />
                    </div>
                    <h1 id="hero-title" class="maryland-hero__title">
                      Protect, restore, and enjoy Maryland's natural resources
                    </h1>
                    <div class="maryland-hero__description">
                      <p>
                        The Department of Natural Resources manages 76 state
                        parks, 460,000 acres of public lands, and the Chesapeake
                        Bay. Get a fishing license, find a park, or learn how
                        we're restoring oyster reefs.
                      </p>
                    </div>
                    <div class="maryland-hero__buttons">
                      <a
                        href="/licenses/fishing"
                        class="usa-button usa-button--big"
                        >Buy a fishing license</a
                      >
                      <a
                        href="/parks/find"
                        class="usa-button usa-button--big usa-button--outline"
                        >Find a park</a
                      >
                    </div>
                  </div>
                  <div class="maryland-hero__img-container">
                    <figure class="maryland-hero__image">
                      <img src="/img/patapsco-valley.jpg" alt="" />
                    </figure>
                  </div>
                </div>
              </div>
            </section>
          </div>
        </div>

        <div
          id="page-content"
          class="grid-col-12 margin-y-8 desktop:margin-top-10 desktop:margin-bottom-15"
        >
          <section
            class="block-spacing"
            aria-labelledby="featured-services-heading"
          >
            <h2 id="featured-services-heading">Featured services</h2>
            <ul class="maryland-card-group">
              <li class="maryland-card maryland-card--media">
                <div class="maryland-card__container">
                  <div class="maryland-card__media">
                    <div class="maryland-card__img">
                      <img
                        src="/img/fishing-license.jpg"
                        alt="Angler casting a line into the Chesapeake Bay"
                      />
                    </div>
                  </div>
                  <div class="maryland-card__header">
                    <h3 class="maryland-card__heading">
                      Buy a fishing or hunting license
                    </h3>
                  </div>
                  <div class="maryland-card__body">
                    <p>
                      Recreational fishing, crabbing, and hunting licenses are
                      available online or at any DNR Service Center.
                    </p>
                  </div>
                  <div
                    class="maryland-card__footer maryland-card__footer--left"
                  >
                    <div class="maryland-card__footer-content">
                      <a
                        href="/licenses"
                        class="usa-button usa-button--primary"
                        >Buy a license</a
                      >
                    </div>
                  </div>
                </div>
              </li>
              <li class="maryland-card maryland-card--media">
                <div class="maryland-card__container">
                  <div class="maryland-card__media">
                    <div class="maryland-card__img">
                      <img
                        src="/img/state-park.jpg"
                        alt="Forest trail at Patapsco Valley State Park"
                      />
                    </div>
                  </div>
                  <div class="maryland-card__header">
                    <h3 class="maryland-card__heading">Find a state park</h3>
                  </div>
                  <div class="maryland-card__body">
                    <p>
                      Explore Maryland's 76 state parks, forests, and natural
                      resource management areas.
                    </p>
                  </div>
                  <div
                    class="maryland-card__footer maryland-card__footer--left"
                  >
                    <div class="maryland-card__footer-content">
                      <a href="/parks" class="usa-button usa-button--primary"
                        >Find parks</a
                      >
                    </div>
                  </div>
                </div>
              </li>
              <li class="maryland-card maryland-card--media">
                <div class="maryland-card__container">
                  <div class="maryland-card__media">
                    <div class="maryland-card__img">
                      <img
                        src="/img/boat-registration.jpg"
                        alt="Boats moored at a state-run marina on the Chesapeake"
                      />
                    </div>
                  </div>
                  <div class="maryland-card__header">
                    <h3 class="maryland-card__heading">Register a boat</h3>
                  </div>
                  <div class="maryland-card__body">
                    <p>
                      Maryland law requires registration for most motorized
                      vessels. Renew online in minutes.
                    </p>
                  </div>
                  <div
                    class="maryland-card__footer maryland-card__footer--left"
                  >
                    <div class="maryland-card__footer-content">
                      <a
                        href="/boating/register"
                        class="usa-button usa-button--primary"
                        >Register a boat</a
                      >
                    </div>
                  </div>
                </div>
              </li>
            </ul>
          </section>

          <section
            class="block-spacing"
            aria-labelledby="oyster-restoration-heading"
          >
            <section
              class="maryland-callout"
              aria-labelledby="oyster-restoration-heading"
            >
              <div class="maryland-callout__container">
                <div class="maryland-callout__content">
                  <h2
                    id="oyster-restoration-heading"
                    class="maryland-callout__title"
                  >
                    Help restore the Chesapeake Bay
                  </h2>
                  <div class="maryland-callout__description">
                    Maryland's oyster restoration program has planted more than
                    three billion oysters in five Chesapeake Bay tributaries
                    since 2014. Volunteer at a public planting day or donate to
                    Marylanders Grow Oysters.
                  </div>
                </div>
              </div>
            </section>
          </section>

          <section class="block-spacing" aria-labelledby="news-heading">
            <h2 id="news-heading">Latest news</h2>
            <ul class="usa-collection">
              <li class="usa-collection__item">
                <div class="usa-collection__body">
                  <h3 class="usa-collection__heading">
                    <a class="usa-link" href="/news/striped-bass-2026"
                      >2026 striped bass season opens April 18</a
                    >
                  </h3>
                  <p class="usa-collection__description">
                    The Maryland Department of Natural Resources today announced
                    spring trophy season rules for Chesapeake Bay striped bass.
                  </p>
                  <ul class="usa-collection__meta" aria-label="More information">
                    <li class="usa-collection__meta-item">
                      <time datetime="2026-03-12">March 12, 2026</time>
                    </li>
                    <li class="usa-collection__meta-item usa-tag">
                      Press release
                    </li>
                  </ul>
                </div>
              </li>
              <li class="usa-collection__item">
                <div class="usa-collection__body">
                  <h3 class="usa-collection__heading">
                    <a class="usa-link" href="/news/black-bear-permits"
                      >Black bear permit lottery applications open</a
                    >
                  </h3>
                  <p class="usa-collection__description">
                    Applications for the 2026 black bear hunting permit lottery
                    are open through May 31.
                  </p>
                  <ul class="usa-collection__meta" aria-label="More information">
                    <li class="usa-collection__meta-item">
                      <time datetime="2026-03-05">March 5, 2026</time>
                    </li>
                    <li class="usa-collection__meta-item usa-tag">
                      News article
                    </li>
                  </ul>
                </div>
              </li>
              <li class="usa-collection__item">
                <div class="usa-collection__body">
                  <h3 class="usa-collection__heading">
                    <a class="usa-link" href="/news/deep-creek-lake"
                      >Deep Creek Lake water-quality results released</a
                    >
                  </h3>
                  <p class="usa-collection__description">
                    Annual monitoring shows continued improvement in dissolved
                    oxygen and clarity at Maryland's largest freshwater lake.
                  </p>
                  <ul class="usa-collection__meta" aria-label="More information">
                    <li class="usa-collection__meta-item">
                      <time datetime="2026-02-28">February 28, 2026</time>
                    </li>
                    <li class="usa-collection__meta-item usa-tag">Report</li>
                  </ul>
                </div>
              </li>
            </ul>
          </section>

          <section
            class="maryland-link-collection"
            aria-labelledby="connect-heading"
          >
            <div class="maryland-link-collection__container">
              <div class="maryland-link-collection__header">
                <h2
                  id="connect-heading"
                  class="maryland-link-collection__title"
                >
                  Connect with DNR
                </h2>
              </div>
              <ul class="maryland-link-collection__list">
                <li class="maryland-link-collection__item">
                  <a href="/contact" class="maryland-link-collection__link">
                    <div class="maryland-link-collection__link-top">
                      <span class="maryland-link-collection__link-text"
                        >Contact a DNR service center</span
                      >
                      <span
                        class="maryland-link-collection__icon"
                        aria-hidden="true"
                      ></span>
                    </div>
                    <div class="maryland-link-collection__item-description">
                      Find the office nearest you.
                    </div>
                  </a>
                </li>
                <li class="maryland-link-collection__item">
                  <a
                    href="/news/subscribe"
                    class="maryland-link-collection__link"
                  >
                    <div class="maryland-link-collection__link-top">
                      <span class="maryland-link-collection__link-text"
                        >Subscribe to DNR News</span
                      >
                      <span
                        class="maryland-link-collection__icon"
                        aria-hidden="true"
                      ></span>
                    </div>
                    <div class="maryland-link-collection__item-description">
                      Weekly updates from the department.
                    </div>
                  </a>
                </li>
                <li class="maryland-link-collection__item">
                  <a href="/jobs" class="maryland-link-collection__link">
                    <div class="maryland-link-collection__link-top">
                      <span class="maryland-link-collection__link-text"
                        >Careers at DNR</span
                      >
                      <span
                        class="maryland-link-collection__icon"
                        aria-hidden="true"
                      ></span>
                    </div>
                    <div class="maryland-link-collection__item-description">
                      Park rangers, biologists, police, and seasonal staff.
                    </div>
                  </a>
                </li>
              </ul>
            </div>
          </section>
        </div>
      </div>
    </main>

    <footer class="maryland-footer">
      <div class="maryland-footer__container">
        <section
          aria-labelledby="agency-footer"
          class="maryland-footer__section"
        >
          <div class="maryland-footer__agency">
            <a class="maryland-footer__agency-home" href="/">
              <img
                class="maryland-footer__agency-logo"
                src="https://cdn.maryland.gov/mdwds/latest/img/md_wordmark_vertical_inverted.svg"
                alt="Department of Natural Resources home"
              />
              <h2 class="maryland-footer__agency-name" id="agency-footer">
                Department of Natural Resources
              </h2>
            </a>
          </div>

          <hr aria-hidden="true" class="maryland-footer__divider" />

          <div class="maryland-footer__agency-menu">
            <div class="maryland-footer__agency-contact">
              <div class="maryland-footer__link-group">
                <h3 class="maryland-footer__link-group-heading">Contact us</h3>
                <ul class="maryland-footer__link-group-list">
                  <li>580 Taylor Avenue, Annapolis, MD 21401</li>
                  <li>An official agency of the State of Maryland</li>
                  <li><a href="tel:8775552267">1-877-555-2267</a></li>
                  <li>
                    <a href="mailto:customerservice@dnr.maryland.gov"
                      >customerservice@dnr.maryland.gov</a
                    >
                  </li>
                  <li><a href="tel:711">Maryland Relay: 7-1-1</a></li>
                </ul>
              </div>
            </div>

            <div class="maryland-footer__agency-links">
              <nav
                class="maryland-footer__link-group"
                aria-labelledby="footer-services"
              >
                <h3
                  class="maryland-footer__link-group-heading"
                  id="footer-services"
                >
                  Services
                </h3>
                <ul class="maryland-footer__link-group-list">
                  <li><a href="/fishing">Fishing licenses</a></li>
                  <li><a href="/hunting">Hunting licenses</a></li>
                  <li><a href="/boating">Boating registration</a></li>
                </ul>
              </nav>

              <nav
                class="maryland-footer__link-group"
                aria-labelledby="footer-parks"
              >
                <h3
                  class="maryland-footer__link-group-heading"
                  id="footer-parks"
                >
                  Parks &amp; lands
                </h3>
                <ul class="maryland-footer__link-group-list">
                  <li><a href="/parks">State parks</a></li>
                  <li><a href="/forests">State forests</a></li>
                  <li><a href="/reservations">Camping reservations</a></li>
                </ul>
              </nav>

              <nav
                class="maryland-footer__link-group"
                aria-labelledby="footer-about"
              >
                <h3
                  class="maryland-footer__link-group-heading"
                  id="footer-about"
                >
                  About
                </h3>
                <ul class="maryland-footer__link-group-list">
                  <li><a href="/about">Our mission</a></li>
                  <li><a href="/jobs">Careers</a></li>
                  <li><a href="/news">News &amp; press</a></li>
                </ul>
              </nav>
            </div>
          </div>

          <hr aria-hidden="true" class="maryland-footer__divider" />
        </section>
      </div>
    </footer>

    <maryland-statewide-footer></maryland-statewide-footer>
  </body>
</html>
```

## Section-by-section breakdown

### 1. Skip nav, banner, and header

The first three blocks are shared with every page in this skill. The skipnav link targets `#main-content`; the `usa-banner` must carry `aria-label="Official website of the State of Maryland"` and uses `usa-banner__inner` → `usa-banner__additional-links` for the right-aligned Maryland.gov / Translate links; the expanded `usa-banner__content` uses `usa-banner__guidance` columns with `usa-media-block__img` icons.

The `maryland-header` includes a `maryland-header__util-nav-container` wrapping the `maryland-header__util-nav` `<ul>` (desktop-only utility links), a `maryland-header__home` anchor wrapping the vertical wordmark (`maryland-header__logo`) and the `maryland-header__agency` span, the `maryland-nav` (with its `__toggle` button and `__mobile-panel` div), and a closing `maryland-header__divider` hr. See [cdn/page-shell.md](../page-shell.md) and [cdn/components/maryland-header.md](../components/maryland-header.md) for the canonical order.

Inside `maryland-nav`, every list uses `maryland-nav__items maryland-nav__items--level-one` (or `--level-two` for dropdowns), every `<li>` uses `maryland-nav__item maryland-nav__item--level-one`, and every link uses `maryland-nav__link maryland-nav__link--level-one`. Dropdown parents are rendered as `<button type="button">` rather than `<a>`, with sub-items wrapped in `<div class="maryland-nav__children" id="nav-children-2">`. **Do not** flatten to `<ul class="maryland-nav__list">` — the JS bundle's nav init reads the `__toggle` / `__mobile-panel` / `__items--level-one` structure.

### 2. Hero — `landing-agency` variant

We use `maryland-hero` with the `landing-agency` variant because the agency homepage is the only page where we want both the agency logo *and* a hero image in a two-column layout. The `has-image` and `has-logo` modifier classes turn on the side-by-side layout; the description sits between title and CTAs.

The required internal structure is `maryland-hero__container` → `maryland-hero__row` → `maryland-hero__content` (with `maryland-hero__agency-logo`, `maryland-hero__title`, `maryland-hero__description`, `maryland-hero__buttons`) sitting next to `maryland-hero__img-container` (containing a `<figure class="maryland-hero__image">`). See [maryland-hero](../components/maryland-hero.md) for all variants.

```html
<section class="maryland-hero maryland-hero--landing-agency has-illustration has-image has-logo" aria-labelledby="hero-title">
  <div class="maryland-hero__container">
    <div class="maryland-hero__row">
      <div class="maryland-hero__content">
        <div class="maryland-hero__agency-logo"><img src="/img/dnr-seal.svg" alt="" /></div>
        <h1 id="hero-title" class="maryland-hero__title">Title</h1>
        <div class="maryland-hero__description"><p>Description.</p></div>
        <div class="maryland-hero__buttons">
          <a href="#" class="usa-button usa-button--big">Primary</a>
          <a href="#" class="usa-button usa-button--big usa-button--outline">Secondary</a>
        </div>
      </div>
      <div class="maryland-hero__img-container">
        <figure class="maryland-hero__image"><img src="/img/photo.jpg" alt="" /></figure>
      </div>
    </div>
  </div>
</section>
```

### 3. Featured services — `maryland-card` (`media` variant)

Three top-tasks cards (license, parks, boat registration) use the `media` variant because each task benefits from a recognizable photo. We chose `maryland-card`, not `usa-card`, because we're on a Maryland-branded page (see [component-index](../component-index.md)). The `<ul class="maryland-card-group">` wrapper handles the responsive 1/2/3-column layout — don't wrap cards in your own `grid-col-*`. Every card requires the `maryland-card__container` wrapper inside the `<li>` — without it, the header/body/footer flex layout collapses. See [maryland-card](../components/maryland-card.md).

### 4. Initiative callout — `maryland-callout`

A single `maryland-callout` highlights an in-flight program. Callouts get a centered headline with a thin divider underneath and a body sentence — they read as "stop and notice this" without being as alarming as a `maryland-alert`. The required structure is `<section class="maryland-callout">` → `maryland-callout__container` → `maryland-callout__content` → `maryland-callout__title` (`<h2>`) + `maryland-callout__description`. There is **no** `maryland-callout__body` or `maryland-callout__actions`; callouts do not support a button or link. If you need a CTA, use `maryland-promo` instead. See [maryland-callout](../components/maryland-callout.md).

### 5. Latest news — `usa-collection`

There is no `maryland-collection`; the USWDS `usa-collection` is the canonical Maryland pattern for news/press-release lists. We use the default variant — each item has a heading `<a class="usa-link">` link inside `usa-collection__heading`, a `usa-collection__description` paragraph, and a `usa-collection__meta` `<ul>` of `usa-collection__meta-item` entries (with the dates rendered inside `<time datetime="...">` for machine-readability). See [usa-collection](../components/usa-collection.md).

### 6. Connect with us — `maryland-link-collection`

For a flat "more resources" list without images, `maryland-link-collection` is lighter than a row of `linked` cards. The required structure is `<section class="maryland-link-collection">` → `maryland-link-collection__container` → `maryland-link-collection__header` (with the `maryland-link-collection__title` `<h2>`) → `maryland-link-collection__list` `<ul>`. Each list item wraps an `<a class="maryland-link-collection__link">` containing `maryland-link-collection__link-top` (with `__link-text` span and `__icon` span) and optionally `maryland-link-collection__item-description`. See [maryland-link-collection](../components/maryland-link-collection.md).

```html
<section class="maryland-link-collection" aria-labelledby="connect-heading">
  <div class="maryland-link-collection__container">
    <div class="maryland-link-collection__header">
      <h2 id="connect-heading" class="maryland-link-collection__title">Connect with DNR</h2>
    </div>
    <ul class="maryland-link-collection__list">
      <li class="maryland-link-collection__item">
        <a href="/contact" class="maryland-link-collection__link">
          <div class="maryland-link-collection__link-top">
            <span class="maryland-link-collection__link-text">Contact a DNR service center</span>
            <span class="maryland-link-collection__icon" aria-hidden="true"></span>
          </div>
          <div class="maryland-link-collection__item-description">Find the office nearest you.</div>
        </a>
      </li>
    </ul>
  </div>
</section>
```

### 7. Agency footer — `maryland-footer`

Per-agency contact info: agency name, address, parent agency line, phone, email, Maryland Relay, plus optional link groups. Required wrappers: `<footer class="maryland-footer">` → `maryland-footer__container` → `maryland-footer__section` → `maryland-footer__agency` (logo + agency name, optional social row) → `maryland-footer__divider` → `maryland-footer__agency-menu` (containing `maryland-footer__agency-contact` and `maryland-footer__agency-links`) → closing `maryland-footer__divider`. See [maryland-footer](../components/maryland-footer.md).

### 8. Statewide footer — `<maryland-statewide-footer>`

Zero-config web component. Renders the statewide directory (top services, government, policies, connect, alerts). See [maryland-statewide-footer](../components/maryland-statewide-footer.md).

## Common customizations

- **Hide the agency logo in the hero** — remove the `maryland-hero__agency-logo` block and the `has-logo` class from the hero `<section>`.
- **Drop the hero image** — remove `maryland-hero__img-container` and replace `has-image` with `no-image`. The hero collapses to a single column with the flag illustration on the right.
- **Add a global alert above the header** — insert a `<div class="maryland-alert maryland-alert--info">…</div>` (or `--warning`, `--error`, `--emergency`) between the `usa-banner` and the `maryland-header`. See [maryland-alert](../components/maryland-alert.md).
- **Add a sidebar** — wrap the featured-services / news / connect sections in a `<div class="grid-row grid-gap">` with a `<aside class="grid-col-12 desktop:grid-col-3">` (containing `maryland-sidenav`) and a `<div class="grid-col-12 desktop:grid-col-8">` for content.
- **Switch service cards to `linked` variant** — for a denser, fully-clickable grid (e.g. "Apply for a license" / "Find a park" / "Register a boat" with no descriptions), change `maryland-card--media` to `maryland-card--linked`, wrap the `maryland-card__container` in a single `<a class="maryland-card__link">`, and replace the footer button with a `maryland-card__icon maryland-card__icon--arrow` span. See [maryland-card](../components/maryland-card.md).
- **Change footer agency info** — edit the address, parent agency, phone, and email in the `maryland-footer__agency-contact` block. The phone link should use `tel:` and the email should use `mailto:`.

## What you should NOT do

1. **Don't use `<maryland-hero variant="landing-main">` here.** That variant is for the maryland.gov state homepage only — it has no description, no buttons, and a full-bleed photographic background. The agency homepage needs CTAs and a logo, so use `landing-agency`.
2. **Don't include the `<h1>` anywhere except inside the hero.** The hero title is the page's only `<h1>`. The "Featured services" heading is `<h2>`, the card titles are `<h3>`, and so on. See [composition.md](../composition.md).
3. **Don't omit the agency footer when you have the statewide footer.** On agency pages, the order is `<footer class="maryland-footer">` (agency contact) → `<maryland-statewide-footer>` (statewide directory). The maryland.gov homepage is the only page that uses the statewide footer alone.
4. **Don't drop `usa-prose` around free-form body text.** It applies the right link color, list bullets, and Merriweather/Source Sans defaults. In this recipe the body is component-driven so we don't need `usa-prose` around the cards/collection, but if you add a "About this agency" paragraph block, wrap it.
5. **Don't write inline `style` to space the sections.** Use `block-spacing` on each `<section>` — it applies the responsive 48/64/120px rhythm that matches the design system. See [composition.md](../composition.md).
6. **Don't simplify `maryland-nav`, `maryland-link-collection`, or `maryland-callout` markup.** Each has BEM modifier classes the JS bundle and CSS depend on — for example, `maryland-nav` requires `__toggle` + `__mobile-panel` + `__items--level-one`, `maryland-link-collection` requires `__container` + `__list` + `__link` + `__link-top` + `__link-text` + `__icon`, and `maryland-callout` requires `__container` + `__content` + `__title` + `__description` (no `__body` or `__actions`). Skipping them produces unstyled or broken components.
7. **Don't forget the `data-mdwds` attribute on the CDN stylesheet `<link>`.** `<maryland-statewide-footer>` adopts the global stylesheet into its shadow root by looking up `link[rel="stylesheet"][data-mdwds]`. Without it, the footer renders blank.
