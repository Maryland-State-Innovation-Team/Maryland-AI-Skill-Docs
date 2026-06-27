# Recipe: Landing Page

A landing page is an interior section front — one level below an agency homepage. Examples: "Vehicle services" on the MVA site, "Behavioral health" on the Department of Health site, "Apprenticeship" on the Department of Labor site. It uses the `landing-regular` hero variant: a white hero with breadcrumb, title, optional description, optional primary/secondary buttons, and an optional photograph in a two-column layout. Below the hero, a sidebar + prose layout introduces the section and links into deeper pages.

Visually: gray banner → agency header → white hero with **blue** breadcrumb links at the top, title in dark text, optional description and CTAs on the left, photo on the right → two-column body with `maryland-sidenav` left and prose + components right → agency footer → statewide footer.

> **Important:** Do not simplify the markup below — every BEM modifier class and wrapper element is required by either the CDN stylesheet or the JS bundle. If you need to modify a component, read its file under `cdn/components/` first.

## When to use this recipe

- An interior section front (one step below the agency homepage).
- A landing page that needs breadcrumbs and a sidebar, but doesn't yet drop the user into a specific listing or form.
- Pages that introduce a topic area with an explanatory paragraph + child-page links.
- Where the agency wants buttons in the hero (e.g. "Apply now" + "Learn more").

## Page structure

1. `usa-skipnav`
2. `usa-banner`
3. `maryland-header` (with agency name)
4. `<main>` opens
5. `maryland-hero` with `variant="landing-regular"`, breadcrumb visible (light/blue link style), `heroStyle="with-image"`, primary + secondary buttons enabled
6. Two-column grid:
   - `<aside>`: `maryland-sidenav` (top-level)
   - `<div id="page-content">`: introduction `usa-prose` + a `maryland-summary-box` + a card group of child pages
7. `<main>` closes
8. `maryland-footer`
9. `<maryland-statewide-footer>`

## Full assembled HTML

```html
<!doctype html>
<!-- Pin to a specific version in production. See cdn/setup.md. -->
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Vehicle services — Motor Vehicle Administration</title>

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
              <p>
                <strong>Official websites use .gov</strong><br />A
                <strong>.gov</strong> website belongs to an official government
                organization in the United States.
              </p>
            </div>
            <div class="usa-banner__guidance tablet:grid-col-6">
              <p>
                <strong>Secure .gov websites use HTTPS</strong><br />A
                <strong>lock</strong> or <strong>https://</strong> means you've
                safely connected to the .gov website.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <header class="maryland-header">
      <a class="maryland-header__home" href="/">
        <img
          class="maryland-header__logo"
          src="https://cdn.maryland.gov/mdwds/latest/img/md_wordmark_vertical.svg"
          alt="Motor Vehicle Administration home"
        />
        <span class="maryland-header__agency"
          >Motor Vehicle Administration</span
        >
      </a>
      <nav class="maryland-nav" aria-label="Primary navigation">
        <button
          class="maryland-nav__toggle"
          aria-label="Toggle Nav"
          type="button"
        ></button>
        <div class="maryland-nav__mobile-panel" id="md-nav-panel-1">
          <ul class="maryland-nav__items maryland-nav__items--level-one">
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                href="/vehicles"
                class="maryland-nav__link maryland-nav__link--level-one maryland-nav__link--active-trail"
                aria-current="page"
                >Vehicle services</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                href="/drivers"
                class="maryland-nav__link maryland-nav__link--level-one"
                >Driver services</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                href="/real-id"
                class="maryland-nav__link maryland-nav__link--level-one"
                >Real ID</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                href="/locations"
                class="maryland-nav__link maryland-nav__link--level-one"
                >Find a branch</a
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
              class="maryland-hero maryland-hero--landing-regular has-illustration has-image"
              aria-labelledby="hero-title"
            >
              <div class="maryland-hero__container">
                <div class="maryland-hero__row">
                  <div class="maryland-hero__content">
                    <div class="maryland-hero__breadcrumb">
                      <nav
                        class="maryland-breadcrumb maryland-breadcrumb--light"
                        aria-label="Breadcrumb"
                      >
                        <ol class="maryland-breadcrumb__list">
                          <li class="maryland-breadcrumb__list-item">
                            <a href="/" class="maryland-breadcrumb__link"
                              >Home</a
                            >
                          </li>
                          <li class="maryland-breadcrumb__list-item">
                            <a
                              class="maryland-breadcrumb__link"
                              aria-current="page"
                              href="/vehicles"
                              >Vehicle services</a
                            >
                          </li>
                        </ol>
                      </nav>
                    </div>
                    <h1 id="hero-title" class="maryland-hero__title">
                      Vehicle services
                    </h1>
                    <div class="maryland-hero__description">
                      <p>
                        Register a vehicle, renew tags, transfer a title, or
                        replace a lost registration card. Most services are
                        available online — no MVA visit required.
                      </p>
                    </div>
                    <div class="maryland-hero__buttons">
                      <a
                        href="/vehicles/renew"
                        class="usa-button usa-button--big"
                        >Renew online</a
                      >
                      <a
                        href="/locations"
                        class="usa-button usa-button--big usa-button--outline"
                        >Find a branch</a
                      >
                    </div>
                  </div>
                  <div class="maryland-hero__img-container">
                    <figure class="maryland-hero__image">
                      <img src="/img/mva-renewal.jpg" alt="" />
                    </figure>
                  </div>
                </div>
              </div>
            </section>
          </div>
        </div>

        <div class="grid-row grid-gap">
          <aside
            class="grid-col-12 desktop:grid-col-3 margin-top-8 desktop:margin-top-10 desktop:margin-bottom-15"
          >
            <a class="usa-skipnav" href="#page-content">Skip sidebar</a>
            <nav aria-labelledby="section-menu-label" class="maryland-sidenav">
              <button
                class="maryland-sidenav__toggle"
                aria-controls="section-menu-list"
              >
                <span class="usa-sr-only">close</span>
                <h2 class="maryland-sidenav__title" id="section-menu-label">
                  Section menu
                </h2>
              </button>
              <ul
                class="maryland-sidenav__list maryland-sidenav__list--level-1"
                id="section-menu-list"
              >
                <li
                  class="maryland-sidenav__item maryland-sidenav__item--level-1"
                >
                  <span
                    class="maryland-sidenav__link maryland-sidenav__link--level-1"
                    aria-current="page"
                    >Vehicle services</span
                  >
                  <ul class="maryland-sidenav__list maryland-sidenav__list--level-2">
                    <li class="maryland-sidenav__item maryland-sidenav__item--level-2">
                      <a
                        href="/vehicles/registration"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Registration</a
                      >
                    </li>
                    <li class="maryland-sidenav__item maryland-sidenav__item--level-2">
                      <a
                        href="/vehicles/title"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Titles</a
                      >
                    </li>
                    <li class="maryland-sidenav__item maryland-sidenav__item--level-2">
                      <a
                        href="/vehicles/tags"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Tags and plates</a
                      >
                    </li>
                    <li class="maryland-sidenav__item maryland-sidenav__item--level-2">
                      <a
                        href="/vehicles/inspection"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Safety inspection</a
                      >
                    </li>
                    <li class="maryland-sidenav__item maryland-sidenav__item--level-2">
                      <a
                        href="/vehicles/emissions"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Emissions (VEIP)</a
                      >
                    </li>
                    <li class="maryland-sidenav__item maryland-sidenav__item--level-2">
                      <a
                        href="/vehicles/disabled-placards"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Disabled placards</a
                      >
                    </li>
                  </ul>
                </li>
              </ul>
            </nav>
          </aside>

          <div
            id="page-content"
            class="grid-col-12 desktop:grid-col-8 margin-y-8 desktop:margin-top-10 desktop:margin-bottom-15"
          >
            <div class="maryland-summary-box">
              <h2 class="maryland-summary-box__heading">Before you start</h2>
              <div class="maryland-summary-box__body">
                <ul>
                  <li>
                    Have your current Maryland registration card or VIN ready.
                  </li>
                  <li>
                    Most online renewals charge $2.00 less than counter
                    transactions.
                  </li>
                  <li>
                    You'll need a current Maryland emissions (VEIP)
                    certification if your vehicle is due.
                  </li>
                </ul>
              </div>
            </div>

            <div class="usa-prose margin-top-6">
              <h2>About vehicle services</h2>
              <p>
                The Maryland Motor Vehicle Administration (MVA) handles vehicle
                registration, titling, and licensing for nearly 4.3 million
                vehicles on Maryland roads. Most transactions can be completed
                at <a href="https://mva.maryland.gov">mva.maryland.gov</a>,
                through MyMVA, at a self-service kiosk, or by mail. Save a trip
                — use the online renewal tool to receive your new registration
                card and stickers by mail within 7 business days.
              </p>
              <p>
                If your transaction requires a visit (e.g. transferring a title
                from out of state, registering a custom-built vehicle, or
                obtaining a Real ID), schedule an appointment at the
                <a href="/locations">branch nearest you</a>.
              </p>
            </div>

            <section
              class="block-spacing"
              aria-labelledby="popular-tasks-heading"
            >
              <h2 id="popular-tasks-heading">Popular tasks</h2>
              <ul class="maryland-card-group">
                <li class="maryland-card maryland-card--simple">
                  <div class="maryland-card__container">
                    <div class="maryland-card__header">
                      <h3 class="maryland-card__heading">
                        Renew vehicle registration
                      </h3>
                    </div>
                    <div class="maryland-card__body">
                      <p>
                        Renew online up to a year early or one year late. New
                        tags arrive in 7 business days.
                      </p>
                    </div>
                    <div
                      class="maryland-card__footer maryland-card__footer--left"
                    >
                      <div class="maryland-card__footer-content">
                        <a
                          href="/vehicles/renew"
                          class="usa-button usa-button--primary"
                          >Renew now</a
                        >
                      </div>
                    </div>
                  </div>
                </li>
                <li class="maryland-card maryland-card--simple">
                  <div class="maryland-card__container">
                    <div class="maryland-card__header">
                      <h3 class="maryland-card__heading">
                        Transfer a vehicle title
                      </h3>
                    </div>
                    <div class="maryland-card__body">
                      <p>
                        New residents and private-sale buyers have 60 days to
                        title and register a vehicle in Maryland.
                      </p>
                    </div>
                    <div
                      class="maryland-card__footer maryland-card__footer--left"
                    >
                      <div class="maryland-card__footer-content">
                        <a
                          href="/vehicles/title/transfer"
                          class="usa-button usa-button--primary"
                          >Get started</a
                        >
                      </div>
                    </div>
                  </div>
                </li>
                <li class="maryland-card maryland-card--simple">
                  <div class="maryland-card__container">
                    <div class="maryland-card__header">
                      <h3 class="maryland-card__heading">
                        Replace a lost registration card
                      </h3>
                    </div>
                    <div class="maryland-card__body">
                      <p>
                        Order a duplicate card online for $20. It arrives in
                        the mail in about a week.
                      </p>
                    </div>
                    <div
                      class="maryland-card__footer maryland-card__footer--left"
                    >
                      <div class="maryland-card__footer-content">
                        <a
                          href="/vehicles/duplicate"
                          class="usa-button usa-button--primary"
                          >Order duplicate</a
                        >
                      </div>
                    </div>
                  </div>
                </li>
              </ul>
            </section>
          </div>
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
                alt="Motor Vehicle Administration home"
              />
              <h2 class="maryland-footer__agency-name" id="agency-footer">
                Motor Vehicle Administration
              </h2>
            </a>
          </div>
          <hr aria-hidden="true" class="maryland-footer__divider" />
          <div class="maryland-footer__agency-menu">
            <div class="maryland-footer__agency-contact">
              <div class="maryland-footer__link-group">
                <h3 class="maryland-footer__link-group-heading">Contact us</h3>
                <ul class="maryland-footer__link-group-list">
                  <li>
                    6601 Ritchie Highway NE, Glen Burnie, MD 21062
                  </li>
                  <li>An agency of the Maryland Department of Transportation</li>
                  <li><a href="tel:4109237000">410-555-7000</a></li>
                  <li>
                    <a href="mailto:mvacs@mdot.maryland.gov"
                      >mvacs@mdot.maryland.gov</a
                    >
                  </li>
                  <li><a href="tel:711">Maryland Relay: 7-1-1</a></li>
                </ul>
              </div>
            </div>
          </div>
        </section>
      </div>
    </footer>

    <maryland-statewide-footer></maryland-statewide-footer>
  </body>
</html>
```

## Section-by-section breakdown

### 1. Shell

Same skipnav + banner + header pattern from [page-shell.md](../page-shell.md). The header here includes the agency name "Motor Vehicle Administration."

### 2. Hero — `landing-regular` variant

The `landing-regular` variant of `maryland-hero` is white-background (vs. `basic` which is blue), and the breadcrumb links inside use the "light" (blue-on-white) color. This variant is the only one that supports both a description and a button row in a single-column or two-column layout. We pass `heroStyle="with-image"`, breadcrumb data, and primary + secondary buttons. See [maryland-hero](../components/maryland-hero.md).

### 3. Sidebar — `maryland-sidenav`

The two-column `<div class="grid-row grid-gap">` puts a sidenav (`desktop:grid-col-3`) next to the content (`desktop:grid-col-8`). The sidenav uses a "top-level" structure with the current page expanded so visitors can see siblings. See [maryland-sidenav](../components/maryland-sidenav.md).

### 4. Summary box — `maryland-summary-box`

A `maryland-summary-box` at the top of the content column tells the visitor what they'll need before they start. It's visually distinct from prose without being as loud as a callout. See [maryland-summary-box](../components/maryland-summary-box.md).

### 5. Introduction prose

Wrapped in `<div class="usa-prose">` so paragraphs, links, and lists pick up Maryland body typography (Source Sans Pro Web, MDWDS link blue, proper line-height). See [composition.md](../composition.md).

### 6. Popular tasks — `maryland-card` (`simple` variant)

Three cards using the `simple` variant — no image, button-style CTA. Use `simple` (not `media`) for service tiles where a photo would distract from the task. See [maryland-card](../components/maryland-card.md).

### 7. Agency + statewide footers

Standard footer pair: agency contact info (`maryland-footer`) then the statewide directory (`<maryland-statewide-footer>`).

## Common customizations

- **Drop the hero image.** Remove `maryland-hero__img-container` and switch `has-image` to `no-image` on the hero `<section>`. The hero collapses to single-column on the left.
- **Hide hero buttons.** Remove the `maryland-hero__buttons` block. The template's `showButtons` arg controls this.
- **Hide hero description.** Remove `maryland-hero__description`. `landing-regular` is the only variant where the description is optional.
- **Add a sidebar back link only** (no nested nav). For pages two-or-more levels deep where the sidenav is just "← Back to {section}", use the single-link sidenav pattern documented in [maryland-sidenav](../components/maryland-sidenav.md).
- **Remove the sidebar entirely.** Replace the two-column `grid-row` with a single `<div class="grid-col-12 desktop:grid-col-8 desktop:grid-offset-2">` to keep the content readable-width without a sidebar.
- **Change card variant.** Swap `simple` for `media` to add task imagery, or for `linked` to make each tile fully clickable.
- **Add a global alert above the header** — drop a `maryland-alert` between `usa-banner` and `maryland-header`.

## What you should NOT do

1. **Don't use the `basic` hero here.** `basic` has a blue background and shorter chrome — it's for inner content pages, not section fronts. The white-background `landing-regular` is the section-front variant.
2. **Don't use `usa-breadcrumb`.** Maryland pages use `maryland-breadcrumb`. The `landing-regular` hero wraps the breadcrumb in `maryland-hero__breadcrumb` and applies the light variant.
3. **Don't add a second `<h1>` for the section name.** The hero title is the only `<h1>`. "Popular tasks" and "About vehicle services" are `<h2>`.
4. **Don't manually wrap cards in `grid-col-*`.** The `<ul class="maryland-card-group">` handles the responsive grid. Adding your own columns will double-grid them.
5. **Don't omit the sidebar's "Skip sidebar" link.** When you have a sidenav, add a `<a class="usa-skipnav" href="#page-content">` so keyboard users can jump past the sidenav to the content.
