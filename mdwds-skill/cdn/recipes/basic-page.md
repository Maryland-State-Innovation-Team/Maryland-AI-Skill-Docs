# Recipe: Basic Page

The basic page is the workhorse content template — for explanatory pages that aren't a section landing, a listing, an action form, or news. Examples: "About the Department of Health," "How emissions inspections work," "Driver's license eligibility requirements," "Behavioral health crisis response." It uses the `basic` hero variant: a **blue** background with breadcrumb, title, optional description, and an optional photograph on the right. Below the hero, the page is a two-column read with sidebar + prose, optional summary box, optional table of contents, and optional "Updated:" date.

Visually: gray banner → agency header → blue hero (flush against the header — no white gap), breadcrumb in white, title in white, optional photo on the right → two-column body with `maryland-sidenav` left and prose + components right (summary box, ToC, updated date, headings, lists, embedded video) → agency footer → statewide footer.

> **Important:** Do not simplify the markup below — every BEM modifier class and wrapper element is required by either the CDN stylesheet or the JS bundle. If you need to modify a component, read its file under `cdn/components/` first.

## When to use this recipe

- A long-form explanatory page (eligibility rules, program details, policy summaries).
- Any page that is not a landing/listing/action/location/news/search page.
- Content pages that need a Table of Contents, "Updated:" date, or summary box at the top.
- The default choice for an inner page if you're not sure which other recipe fits.

## Page structure

1. `usa-skipnav`
2. `usa-banner`
3. `maryland-header`
4. `<main>` opens
5. `maryland-hero` with `variant="basic"`, breadcrumb visible (dark/white-text variant), `heroStyle="with-image"`
6. Two-column grid inside `<div class="maryland-page--basic-page grid-container">`:
   - `<aside>`: `maryland-sidenav` (top-level)
   - `<div id="page-content">`: `maryland-summary-box` (optional) + `usa-prose` with optional Updated date + ToC + headings + body + `maryland-video-promo`
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
    <title>
      How Maryland's emissions inspection program works — Motor Vehicle
      Administration
    </title>

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
      <section
        class="maryland-hero maryland-hero--basic maryland-hero--flush has-illustration has-image"
        aria-labelledby="hero-title"
      >
        <div class="maryland-hero__container">
          <div class="maryland-hero__row">
            <div class="maryland-hero__content">
              <div class="maryland-hero__breadcrumb">
                <nav
                  class="maryland-breadcrumb maryland-breadcrumb--dark"
                  aria-label="Breadcrumb"
                >
                  <ol class="maryland-breadcrumb__list">
                    <li class="maryland-breadcrumb__list-item">
                      <a href="/" class="maryland-breadcrumb__link">Home</a>
                    </li>
                    <li class="maryland-breadcrumb__list-item">
                      <a href="/vehicles" class="maryland-breadcrumb__link"
                        >Vehicle services</a
                      >
                    </li>
                    <li class="maryland-breadcrumb__list-item">
                      <a
                        href="/vehicles/emissions"
                        class="maryland-breadcrumb__link"
                        >Emissions (VEIP)</a
                      >
                    </li>
                    <li class="maryland-breadcrumb__list-item">
                      <a
                        class="maryland-breadcrumb__link"
                        aria-current="page"
                        href="/vehicles/emissions/how-it-works"
                        >How the emissions inspection program works</a
                      >
                    </li>
                  </ol>
                </nav>
              </div>
              <h1 id="hero-title" class="maryland-hero__title">
                How Maryland's emissions inspection program works
              </h1>
              <div class="maryland-hero__description">
                <p>
                  Most Maryland gasoline vehicles get a Vehicle Emissions
                  Inspection (VEIP) once every two years. Here's what to
                  expect, who's exempt, and how to pass.
                </p>
              </div>
            </div>
            <div class="maryland-hero__img-container">
              <figure class="maryland-hero__image">
                <img src="/img/veip-station.jpg" alt="" />
              </figure>
            </div>
          </div>
        </div>
      </section>

      <div class="maryland-page--basic-page grid-container">
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
                  <a
                    href="/vehicles/emissions"
                    class="maryland-sidenav__link maryland-sidenav__link--level-1"
                    >Emissions (VEIP)</a
                  >
                  <ul
                    class="maryland-sidenav__list maryland-sidenav__list--level-2"
                  >
                    <li
                      class="maryland-sidenav__item maryland-sidenav__item--level-2"
                    >
                      <span
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        aria-current="page"
                        >How the program works</span
                      >
                    </li>
                    <li
                      class="maryland-sidenav__item maryland-sidenav__item--level-2"
                    >
                      <a
                        href="/vehicles/emissions/locations"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Find a VEIP station</a
                      >
                    </li>
                    <li
                      class="maryland-sidenav__item maryland-sidenav__item--level-2"
                    >
                      <a
                        href="/vehicles/emissions/self-service"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Self-service kiosks</a
                      >
                    </li>
                    <li
                      class="maryland-sidenav__item maryland-sidenav__item--level-2"
                    >
                      <a
                        href="/vehicles/emissions/extensions"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Waivers and extensions</a
                      >
                    </li>
                    <li
                      class="maryland-sidenav__item maryland-sidenav__item--level-2"
                    >
                      <a
                        href="/vehicles/emissions/fees"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Fees</a
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
              <h2 class="maryland-summary-box__heading">Key information</h2>
              <div class="maryland-summary-box__body">
                <ul>
                  <li>
                    Most Maryland gasoline vehicles need a VEIP test every two
                    years.
                  </li>
                  <li>
                    The standard test fee is <strong>$14.00</strong>; self-service
                    kiosks are <strong>$10.00</strong>.
                  </li>
                  <li>
                    You can use any VEIP station — your assignment letter is a
                    suggestion, not a requirement.
                  </li>
                  <li>
                    Vehicles less than 36 months old, motorcycles, and
                    farm-use vehicles are exempt.
                  </li>
                </ul>
              </div>
            </div>

            <div class="usa-prose margin-top-6">
              <div class="maryland-updated-date">
                Updated:
                <time datetime="2026-02-14">February 14, 2026</time>
              </div>
              <hr aria-hidden="true" />

              <nav class="maryland-table-of-contents" aria-label="On this page">
                <h2 class="maryland-table-of-contents__heading">
                  On this page
                </h2>
                <ol class="maryland-table-of-contents__list">
                  <li>
                    <a href="#who-needs-veip">Who needs a VEIP test</a>
                  </li>
                  <li>
                    <a href="#what-to-expect">What to expect at the station</a>
                  </li>
                  <li>
                    <a href="#what-if-i-fail">What happens if I fail</a>
                  </li>
                  <li>
                    <a href="#exemptions">Exemptions and waivers</a>
                  </li>
                </ol>
              </nav>

              <h2 id="who-needs-veip">Who needs a VEIP test</h2>
              <p>
                Maryland law requires biennial emissions testing for most
                gasoline-powered vehicles registered in Anne Arundel,
                Baltimore, Calvert, Carroll, Cecil, Charles, Frederick,
                Harford, Howard, Montgomery, Prince George's, Queen Anne's, or
                Washington county, or in Baltimore City. The MVA mails an
                assignment notice about 60 days before your due date.
              </p>
              <p>
                You may complete the test at any state-operated VEIP station or
                approved self-service kiosk. You do not need to use the station
                listed on your notice. See
                <a href="/vehicles/emissions/locations">find a VEIP station</a>
                for a map.
              </p>

              <h2 id="what-to-expect">What to expect at the station</h2>
              <p>
                The test takes about 15 minutes. A technician will check your
                vehicle's on-board diagnostic (OBD) system for emission-related
                trouble codes, verify your gas cap holds pressure, and confirm
                the dashboard "check engine" light is off.
              </p>
              <ol>
                <li>Drive into the lane and stay in the vehicle.</li>
                <li>
                  Hand the technician your assignment letter and registration
                  card.
                </li>
                <li>
                  The technician plugs an OBD reader into the port under your
                  dash.
                </li>
                <li>
                  Pay the $14.00 fee. Major credit cards and EZ-Pass are
                  accepted.
                </li>
                <li>
                  You'll receive a printed Vehicle Inspection Report.
                </li>
              </ol>

              <h2 id="what-if-i-fail">What happens if I fail</h2>
              <p>
                If your vehicle fails, you have 60 days to make repairs and
                return for a free retest. Keep your repair receipts — if you
                spend more than the state's
                <strong>cost-to-cure</strong> threshold ($450 in 2026)
                and the vehicle still fails, you may qualify for a waiver.
              </p>

              <blockquote>
                <p>
                  "Drivers who keep up with routine maintenance — oil changes,
                  spark plugs, and a properly seated gas cap — pass VEIP on the
                  first attempt more than 92% of the time."
                </p>
                <cite>
                  — MDOT MVA 2025 Vehicle Emissions Inspection Annual Report
                </cite>
              </blockquote>

              <h2 id="exemptions">Exemptions and waivers</h2>
              <p>
                The following vehicles are exempt from VEIP testing:
              </p>
              <ul>
                <li>Vehicles less than 36 months old (from initial sale).</li>
                <li>
                  Motorcycles and motor scooters.
                </li>
                <li>Diesel-powered vehicles built before model year 2008.</li>
                <li>Farm-use vehicles registered as Class F.</li>
                <li>
                  Vehicles registered as historic (Class L) and over 20 years
                  old.
                </li>
              </ul>

              <figure>
                <iframe
                  src="https://player.vimeo.com/video/1084537"
                  frameborder="0"
                  title="How to prepare for your VEIP inspection"
                  allowfullscreen
                ></iframe>
                <figcaption>
                  How to prepare for your VEIP inspection (2:14).
                </figcaption>
              </figure>
            </div>
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
                  <li>
                    An agency of the Maryland Department of Transportation
                  </li>
                  <li><a href="tel:4105557000">410-555-7000</a></li>
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

Skipnav + banner + header as documented in [page-shell.md](../page-shell.md).

### 2. Hero — `basic` variant

`maryland-hero` with `variant="basic"`. Visually this is the **blue-background** hero — distinct from the white `landing-regular` hero. The basic hero is "flush" (sits directly against the header's bottom border with no white gap) and applies the `maryland-hero--flush` modifier. The breadcrumb inside is dark-variant (white text on blue). The basic hero supports a breadcrumb and an optional image but does **not** support buttons (those belong on `landing-regular`). See [maryland-hero](../components/maryland-hero.md).

### 3. Sidebar — `maryland-sidenav`

Same two-column sidebar pattern as the landing page recipe. The current page is the second-level item with `aria-current="page"`. See [maryland-sidenav](../components/maryland-sidenav.md).

### 4. Summary box — `maryland-summary-box`

The basic-page template positions the summary box *above* the prose `<div>`, not inside it. It surfaces 3–4 bullet-form key facts. See [maryland-summary-box](../components/maryland-summary-box.md).

### 5. Updated date

The `maryland-updated-date` block with a `<time datetime="YYYY-MM-DD">` element gives content owners a "last updated" timestamp. The template draws a horizontal rule below it. If you have a ToC, drop the rule and add the `maryland-updated-date--no-rule` modifier.

### 6. Table of contents — `maryland-table-of-contents`

A `maryland-table-of-contents` element with anchor links to each `<h2>` in the body. The component handles its own heading + list styling. See [maryland-table-of-contents](../components/maryland-table-of-contents.md).

### 7. Prose body

Inside `<div class="usa-prose">`: `<h2>` section headings with matching `id` attributes, `<p>`, `<ol>`/`<ul>`, `<blockquote>`, and an embedded video `<figure>` with `<iframe>` + `<figcaption>`. The basic page can also embed a `maryland-video-promo` near the bottom; here we've used a plain `<figure>` to keep the recipe self-contained, but either is correct.

### 8. Footers

`maryland-footer` (agency contact) + `<maryland-statewide-footer>` (statewide directory).

## Common customizations

- **Hide the Updated date** — remove the `maryland-updated-date` block and its `<hr>`.
- **Hide the Summary Box** — remove the `maryland-summary-box` block. Move the prose `<div>` up.
- **Hide the Table of Contents** — remove the `maryland-table-of-contents` block.
- **Drop the hero image** — remove `maryland-hero__img-container` and replace `has-image` with `no-image`. The basic hero collapses to a single column with its decorative illustration on the right.
- **Drop the description** — remove `maryland-hero__description`. The basic hero is happy with title-only.
- **Remove the sidebar** — replace the two-column `grid-row` with `<div class="grid-col-12 desktop:grid-col-8 desktop:grid-offset-2">`.
- **Add an in-page navigation** — instead of (or in addition to) the ToC, use `usa-in-page-navigation` for sticky anchor-link navigation that follows the user as they scroll. See [usa-in-page-navigation](../components/usa-in-page-navigation.md).
- **Add a global alert above the header** — insert `<div class="maryland-alert maryland-alert--info">…</div>` between `usa-banner` and `maryland-header`.
- **Change footer agency info** — edit `agencyTitle`, `contactAddress`, `parentAgency`, `contactPhone`, `contactEmail` in the `maryland-footer` block.

## What you should NOT do

1. **Don't use the `landing-regular` hero here.** White-background `landing-regular` is for section fronts. Inner content pages use the blue `basic` hero.
2. **Don't put primary/secondary buttons in the basic hero.** The `basic` variant doesn't render buttons by design. If your page needs CTAs in the hero, you probably want a `landing-regular` hero (`cdn/recipes/landing-page.md`) or the `maryland-action-items` hero on an action page (`cdn/recipes/action-page.md`).
3. **Don't write `<h1>` headings in the prose.** The hero title is the only `<h1>`. ToC entries and section headings use `<h2>` — the ids on `<h2>` elements are what the ToC anchors target.
4. **Don't use plain `<details>` or `<usa-accordion>` for the ToC.** The `maryland-table-of-contents` component handles the responsive layout and heading style; using a generic `<details>` will look unstyled and ignore the design system's rules.
5. **Don't render the Updated date as plain text.** Always use `<time datetime="YYYY-MM-DD">` so machine readers (search engines, archives) can parse the date. The visible label can be friendlier (e.g. "February 14, 2026").
