# Recipe: Location Page

A location page describes a single physical location — a Maryland field office, a state park headquarters, a DMV branch, a state historical site. It uses the `location` hero variant: a blue background with breadcrumb, plus a **white card overlay** floating below the hero that contains the location name, address, and optional photograph. The body provides mailing address, hours, contact information (phone, email, website), and driving directions.

Visually: gray banner → agency header → blue hero strip with breadcrumb → overlapping white location card with photo + name + address → two-column body with a short back-link sidebar left and structured content right (mailing address, office hours, contact info, directions) → agency footer → statewide footer.

> **Important:** Do not simplify the markup below — every BEM modifier class and wrapper element is required by either the CDN stylesheet or the JS bundle. If you need to modify a component, read its file under `cdn/components/` first.

## When to use this recipe

- The detail page for a single physical location (office, branch, service center, park).
- Pages that need an address, office hours, and one-tap contact links front-and-center.
- A child page of a "Locations" listing page (typically the listing-page recipe).

## Page structure

1. `usa-skipnav`
2. `usa-banner`
3. `maryland-header`
4. `<main>` opens
5. `maryland-hero` with `variant="location"`: blue header strip with breadcrumb + screen-reader-only title; a `maryland-location-card-container` immediately below holds the white card with image, location name, and address
6. Two-column body:
   - `<aside>`: short sidebar with a "Back to Locations" `maryland-sidenav`
   - `<div id="page-content">`: a `usa-prose maryland-location-content` block containing Mailing Address, Office Hours, Contact Information (website, email, phone labelled links), and Directions paragraphs
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
      Glen Burnie MVA Branch — Motor Vehicle Administration
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
        <div class="maryland-nav__mobile-panel" id="md-nav-panel-location">
          <ul class="maryland-nav__items maryland-nav__items--level-one">
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/vehicles"
                >Vehicle services</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/drivers"
                >Driver services</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/real-id"
                >Real ID</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one maryland-nav__link--active-trail"
                href="/locations"
                aria-current="page"
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
        class="maryland-hero maryland-hero--location maryland-hero--flush has-illustration has-image"
        aria-labelledby="hero-title"
      >
        <div class="maryland-hero__container">
          <div class="maryland-hero__breadcrumb">
            <nav
              class="usa-breadcrumb maryland-breadcrumb maryland-breadcrumb--dark"
              aria-label="Breadcrumb"
            >
              <ol class="usa-breadcrumb__list maryland-breadcrumb__list">
                <li
                  class="usa-breadcrumb__list-item maryland-breadcrumb__list-item"
                >
                  <a
                    href="/"
                    class="usa-breadcrumb__link maryland-breadcrumb__link"
                    ><span>Home</span></a
                  >
                </li>
                <li
                  class="usa-breadcrumb__list-item maryland-breadcrumb__list-item"
                >
                  <a
                    href="/locations"
                    class="usa-breadcrumb__link maryland-breadcrumb__link"
                    ><span>Find a branch</span></a
                  >
                </li>
                <li
                  class="usa-breadcrumb__list-item maryland-breadcrumb__list-item usa-current"
                  aria-current="page"
                >
                  <span class="usa-breadcrumb__link maryland-breadcrumb__link"
                    ><span>Glen Burnie</span></span
                  >
                </li>
              </ol>
            </nav>
          </div>
          <span id="hero-title" class="usa-sr-only"
            >Glen Burnie MVA Branch</span
          >
        </div>
      </section>

      <div class="grid-container maryland-location-card-container has-image">
        <div class="grid-row">
          <div
            class="grid-col-12 desktop:grid-col-3 maryland-hero__grid-spacer"
          ></div>
          <div
            class="grid-col-12 desktop:grid-col-8 maryland-hero__grid-content"
          >
            <div class="maryland-hero__location-card">
              <figure class="maryland-hero__image">
                <img
                  src="/img/glen-burnie-branch.jpg"
                  alt="Exterior of the Glen Burnie MVA branch office"
                />
              </figure>
              <div class="maryland-hero__content">
                <h1 class="maryland-hero__title">Glen Burnie MVA Branch</h1>
                <address class="maryland-hero__address">
                  <ul class="usa-list usa-list--unstyled">
                    <li>6601 Ritchie Highway NE</li>
                    <li>Glen Burnie, MD 21062</li>
                  </ul>
                </address>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="grid-container">
        <div class="grid-row grid-gap">
          <aside
            class="grid-col-12 desktop:grid-col-3 desktop:margin-bottom-15 margin-top-8 desktop:margin-0"
          >
            <a class="usa-skipnav" href="#page-content">Skip sidebar</a>
            <nav
              aria-labelledby="back-to-locations-label"
              class="maryland-sidenav"
            >
              <button
                class="maryland-sidenav__toggle"
                aria-controls="back-to-locations-list"
              >
                <span class="usa-sr-only">close</span>
                <h2
                  class="maryland-sidenav__title"
                  id="back-to-locations-label"
                >
                  Find a branch
                </h2>
              </button>
              <ul
                class="maryland-sidenav__list maryland-sidenav__list--level-1"
                id="back-to-locations-list"
              >
                <li
                  class="maryland-sidenav__item maryland-sidenav__item--level-1"
                >
                  <a
                    href="/locations"
                    class="maryland-sidenav__link maryland-sidenav__link--level-1"
                    >Find a branch</a
                  >
                </li>
              </ul>
            </nav>
          </aside>

          <div
            id="page-content"
            class="grid-col-12 desktop:grid-col-8 margin-y-8 desktop:margin-top-10 desktop:margin-bottom-15"
          >
            <div class="usa-prose maryland-location-content">
              <h2 class="maryland-location-content__heading">
                Mailing address
              </h2>
              <address>
                <ul class="usa-list usa-list--unstyled">
                  <li>6601 Ritchie Highway NE</li>
                  <li>Glen Burnie, MD 21062</li>
                </ul>
              </address>

              <h2 class="maryland-location-content__heading">Office hours</h2>
              <ul class="usa-list">
                <li>Sunday: Closed</li>
                <li>Monday: 8:30 am to 4:30 pm</li>
                <li>Tuesday: 8:30 am to 4:30 pm</li>
                <li>Wednesday: 8:30 am to 4:30 pm</li>
                <li>Thursday: 8:30 am to 4:30 pm</li>
                <li>Friday: 8:30 am to 4:30 pm</li>
                <li>Saturday: 8:00 am to 12:00 pm</li>
                <li>
                  <em>All hours are in Eastern Time. Closed on state holidays.</em>
                </li>
              </ul>

              <h2 class="maryland-location-content__heading">
                Contact information
              </h2>
              <a
                class="maryland-link maryland-link--labelled"
                href="https://mva.maryland.gov/locations/glen-burnie"
              >
                <span class="maryland-link__description">Website</span>
                <span class="maryland-link__label"
                  >Glen Burnie MVA Branch website</span
                >
              </a>
              <a
                class="maryland-link maryland-link--labelled"
                href="mailto:glenburnie@mdot.maryland.gov"
              >
                <span class="maryland-link__description">Email address</span>
                <span class="maryland-link__label"
                  >glenburnie@mdot.maryland.gov</span
                >
              </a>
              <a
                class="maryland-link maryland-link--labelled"
                href="tel:4105557000"
              >
                <span class="maryland-link__description">Main</span>
                <span class="maryland-link__label">410-555-7000</span>
              </a>
              <a
                class="maryland-link maryland-link--labelled"
                href="tel:8009507700"
              >
                <span class="maryland-link__description">Toll-free</span>
                <span class="maryland-link__label">1-800-555-7700</span>
              </a>

              <h2 class="maryland-location-content__heading">Directions</h2>
              <p>
                The Glen Burnie branch is on Ritchie Highway (MD Route 2) just
                south of Crain Highway. From I-695 (Baltimore Beltway), take
                exit 3A onto MD-2 South. The branch is 1.4 miles on the right;
                look for the MVA sign at the entrance to a large surface lot.
                Free parking is available, including 14 ADA-accessible spaces.
              </p>
              <p>
                MTA Bus Route 70 stops at Ritchie Highway and Aquahart Road,
                a five-minute walk to the entrance. Light Rail's Cromwell /
                Glen Burnie station is approximately one mile west; transfer
                to Bus 14 for a direct connection.
              </p>
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
                  <li>6601 Ritchie Highway NE, Glen Burnie, MD 21062</li>
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

Standard skipnav + banner + header. The header's primary nav highlights "Find a branch" with `aria-current="page"`.

### 2. Hero — `location` variant

The `location` variant is unique among heroes: the blue hero band itself contains *only* the breadcrumb and a screen-reader-only `<span>` with the location name. The actual visible `<h1>` lives **inside the white location card** that overlays the blue band — `maryland-location-card-container` immediately below the hero `<section>`. The card holds image + name + address. See [maryland-hero](../components/maryland-hero.md) for the two-part structure.

### 3. Sidebar — "Back to Locations"

Unlike other recipes, the location-page sidebar is a single-link `maryland-sidenav` whose only entry is the back-link to the parent locations listing.

### 4. Mailing address — `<address>` + `usa-list usa-list--unstyled`

A semantic `<address>` element wraps an unstyled list of address lines. Use this even when the address is identical to the one shown in the hero card — search engines and assistive tech expect mailing data inside `<address>`.

### 5. Office hours — `usa-list`

A plain `<ul class="usa-list">` of day-time pairs, with a closing `<em>` line for timezone and holiday closures. Each `<li>` is a day + time pair; the timezone note goes in a final `<li><em>`.

### 6. Contact information — `maryland-link--labelled`

Each contact channel (website, email, phones) is rendered as a `maryland-link` with the `labelled` variant — `<span class="maryland-link__description">` for the channel name and `<span class="maryland-link__label">` for the value/anchor text. Phone numbers must use `tel:` hrefs (strip non-digits); emails use `mailto:`. See [maryland-link](../components/maryland-link.md).

### 7. Directions

A short prose section with one or two `<p>` paragraphs describing routes by car and by transit. If your agency wants an embedded map, drop a Google Maps or Mapbox embed inside a `<figure>` here.

### 8. Footers

`maryland-footer` (agency-level contact) → `<maryland-statewide-footer>`.

## Common customizations

- **Drop the hero image.** Remove the `<figure class="maryland-hero__image">` inside the location card and change `has-image` to `no-image` on `maryland-location-card-container` and on the hero `<section>`. The card collapses to name + address only.
- **Add an embedded map.** Inside the Directions section, add `<figure><iframe src="https://www.google.com/maps/embed?..." …></iframe><figcaption>Map of Glen Burnie MVA branch</figcaption></figure>`. Always include a `<figcaption>` for screen readers.
- **Multiple phone numbers.** Add additional `<a class="maryland-link maryland-link--labelled">` blocks — one labelled link per phone number.
- **No website / no email.** Omit the corresponding `maryland-link--labelled` block — these blocks are independent and any can be skipped.
- **Change the back-link label/href.** Edit the sidebar's `maryland-sidenav__title` text and the sole `<a>`'s `href`.
- **Add a global alert above the header** — `<div class="maryland-alert">…</div>` between `usa-banner` and `maryland-header`. Useful for "This branch is temporarily closed due to weather" notices.
- **Change footer agency info** — edit the `maryland-footer` block.

## What you should NOT do

1. **Don't put a second `<h1>` in the body.** The location card's name is the page's `<h1>`. The "Mailing address," "Office hours," etc. are `<h2>`. The hero band itself contains a *visually hidden* sr-only span with the name so screen readers announce it before the breadcrumb — that's not a second `<h1>`.
2. **Don't write the hours as a `<table>`.** A semantic `<ul>` is correct here; a hours table is a row-per-day grid that doesn't add structure for assistive tech and looks heavier on mobile.
3. **Don't render phone numbers as plain text.** Always use `<a href="tel:...">` so mobile users can tap to call.
4. **Don't omit the `<address>` element around the mailing address.** It's the correct semantic wrapper for contact information.
5. **Don't use the location card structure on non-location pages.** It's tightly coupled to the `location` hero variant; reusing the white-card overlay elsewhere will misalign with the missing blue hero behind it.
