# Recipe: Listing Page

A listing page shows a filterable, paginated collection of items — news articles, events, locations, contacts, or documents. The hero is the `landing-regular` variant (white background) so the search/filter strip and result list sit visually on the page rather than on a colored band. The hero title is derived from the content type ("News", "Events", "Locations", etc.), and a sidebar plus filter bar drive the result list, which is rendered as a `usa-collection`.

Visually: gray banner → agency header → white hero with breadcrumb, content-type title, short description → two-column body with `maryland-sidenav` left and (intro text, filter row, `usa-collection`, pagination) right → agency footer → statewide footer.

> **Important:** Do not simplify the markup below — every BEM modifier class and wrapper element is required by either the CDN stylesheet or the JS bundle. If you need to modify a component, read its file under `cdn/components/` first.

## When to use this recipe

- Any page that surfaces a list of things from a content type: news, press releases, events, public notices, locations, agency contacts, documents.
- Pages that need filtering, sorting, and pagination of a homogeneous collection.
- Where the visitor's task is "browse and narrow," not "do" or "read."

## Page structure

1. `usa-skipnav`
2. `usa-banner`
3. `maryland-header`
4. `<main>` opens, with `<div class="grid-container">`
5. `maryland-hero` with `variant="landing-regular"`, breadcrumb, title (e.g. "News"), description, no buttons, optional image
6. Two-column grid:
   - `<aside>`: `maryland-sidenav` listing sibling section-level pages
   - `<div id="page-content">`:
     - Intro paragraph (`usa-prose`)
     - Filter strip (`usa-search` / `usa-select` / `maryland-button-group`)
     - Results list — `usa-collection` (default variant with images, dates, tags, descriptions)
     - Pagination — `usa-pagination`
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
    <title>News and press releases — Maryland Department of Health</title>

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
          alt="Department of Health home"
        />
        <span class="maryland-header__agency">Department of Health</span>
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
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/health-care"
                >Health care</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/programs"
                >Programs</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/data"
                >Data and research</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/news"
                aria-current="page"
                >News</a
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
              class="maryland-hero maryland-hero--landing-regular has-illustration no-image no-description-buttons"
              aria-labelledby="hero-title"
            >
              <div class="maryland-hero__container">
                <div class="maryland-hero__content">
                  <div class="maryland-hero__breadcrumb">
                    <nav class="maryland-breadcrumb" aria-label="Breadcrumb">
                      <ol class="maryland-breadcrumb__list">
                        <li class="maryland-breadcrumb__item">
                          <a href="/" class="maryland-breadcrumb__link">Home</a>
                        </li>
                        <li
                          class="maryland-breadcrumb__item maryland-breadcrumb__item--current"
                        >
                          <span aria-current="page"
                            >News and press releases</span
                          >
                        </li>
                      </ol>
                    </nav>
                  </div>
                  <h1 id="hero-title" class="maryland-hero__title">
                    News and press releases
                  </h1>
                  <div class="maryland-hero__description">
                    <p>
                      Announcements, public health advisories, and press
                      releases from the Maryland Department of Health.
                    </p>
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
                  <a
                    href="/news"
                    class="maryland-sidenav__link maryland-sidenav__link--level-1"
                    aria-current="page"
                    >News and press releases</a
                  >
                  <ul
                    class="maryland-sidenav__list maryland-sidenav__list--level-2"
                  >
                    <li
                      class="maryland-sidenav__item maryland-sidenav__item--level-2"
                    >
                      <a
                        href="/news/press-releases"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Press releases</a
                      >
                    </li>
                    <li
                      class="maryland-sidenav__item maryland-sidenav__item--level-2"
                    >
                      <a
                        href="/news/advisories"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Public health advisories</a
                      >
                    </li>
                    <li
                      class="maryland-sidenav__item maryland-sidenav__item--level-2"
                    >
                      <a
                        href="/news/media-advisories"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Media advisories</a
                      >
                    </li>
                    <li
                      class="maryland-sidenav__item maryland-sidenav__item--level-2"
                    >
                      <a
                        href="/news/subscribe"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Subscribe</a
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
            <div class="usa-prose">
              <p>
                Browse news from the Maryland Department of Health. Filter by
                category or search by keyword. For breaking public health
                alerts, see
                <a href="/news/advisories">public health advisories</a>.
              </p>
            </div>

            <form
              class="usa-form maryland-listing-page__filters margin-y-6"
              role="search"
              aria-label="Filter news"
            >
              <div class="grid-row grid-gap">
                <div class="grid-col-12 tablet:grid-col-6">
                  <label class="usa-label" for="news-search"
                    >Search news</label
                  >
                  <input
                    class="usa-input"
                    id="news-search"
                    type="search"
                    name="q"
                    placeholder="e.g. measles, opioid, Medicaid"
                  />
                </div>
                <div class="grid-col-6 tablet:grid-col-3">
                  <label class="usa-label" for="news-type">Type</label>
                  <select class="usa-select" id="news-type" name="type">
                    <option value="">All types</option>
                    <option>Press release</option>
                    <option>Media advisory</option>
                    <option>Public notice</option>
                    <option>News article</option>
                  </select>
                </div>
                <div class="grid-col-6 tablet:grid-col-3">
                  <label class="usa-label" for="news-year">Year</label>
                  <select class="usa-select" id="news-year" name="year">
                    <option value="">All years</option>
                    <option>2026</option>
                    <option>2025</option>
                    <option>2024</option>
                  </select>
                </div>
              </div>
              <div class="margin-top-3">
                <button class="usa-button" type="submit">Apply filters</button>
                <button
                  class="usa-button usa-button--unstyled"
                  type="reset"
                >
                  Clear
                </button>
              </div>
            </form>

            <p class="text-base">
              <strong>1–10</strong> of <strong>247</strong> results
            </p>

            <ul class="usa-collection">
              <li class="usa-collection__item">
                <img
                  class="usa-collection__img"
                  src="/img/measles-clinic.jpg"
                  alt="A nurse administers an MMR vaccine at a Prince George's County clinic"
                />
                <div class="usa-collection__body">
                  <h2 class="usa-collection__heading">
                    <a href="/news/measles-cluster-pg"
                      >MDH responds to measles cluster in Prince George's
                      County</a
                    >
                  </h2>
                  <p class="usa-collection__description">
                    The Department is offering free MMR vaccinations at three
                    pop-up clinics through April 30. Residents born after 1957
                    who haven't been vaccinated are encouraged to attend.
                  </p>
                  <ul class="usa-collection__meta" aria-label="Article details">
                    <li class="usa-collection__meta-item">
                      Published April 14, 2026
                    </li>
                    <li class="usa-collection__meta-item">
                      <span class="usa-tag">Press release</span>
                    </li>
                  </ul>
                </div>
              </li>
              <li class="usa-collection__item">
                <img
                  class="usa-collection__img"
                  src="/img/opioid-summit.jpg"
                  alt="Panelists at the Maryland Opioid Operational Command Center summit"
                />
                <div class="usa-collection__body">
                  <h2 class="usa-collection__heading">
                    <a href="/news/opioid-grants"
                      >$48 million in opioid settlement grants awarded to 19
                      counties</a
                    >
                  </h2>
                  <p class="usa-collection__description">
                    The Opioid Restitution Fund will support community-based
                    treatment, harm reduction, and prevention programs across
                    Maryland.
                  </p>
                  <ul class="usa-collection__meta" aria-label="Article details">
                    <li class="usa-collection__meta-item">
                      Published April 9, 2026
                    </li>
                    <li class="usa-collection__meta-item">
                      <span class="usa-tag">Press release</span>
                    </li>
                  </ul>
                </div>
              </li>
              <li class="usa-collection__item">
                <img
                  class="usa-collection__img"
                  src="/img/medicaid-renewal.jpg"
                  alt="Person reading a Maryland Medicaid renewal letter"
                />
                <div class="usa-collection__body">
                  <h2 class="usa-collection__heading">
                    <a href="/news/medicaid-renewal-window"
                      >Medicaid renewal window opens for 2026 enrollees</a
                    >
                  </h2>
                  <p class="usa-collection__description">
                    Maryland Medicaid will begin sending renewal notices in
                    rolling 60-day windows starting May 1. Recipients can
                    update their information online.
                  </p>
                  <ul class="usa-collection__meta" aria-label="Article details">
                    <li class="usa-collection__meta-item">
                      Published April 2, 2026
                    </li>
                    <li class="usa-collection__meta-item">
                      <span class="usa-tag">Media advisory</span>
                    </li>
                  </ul>
                </div>
              </li>
            </ul>

            <nav class="usa-pagination" aria-label="Pagination">
              <ul class="usa-pagination__list">
                <li class="usa-pagination__item usa-pagination__arrow">
                  <a
                    href="?page=0"
                    class="usa-pagination__link usa-pagination__previous-page"
                    aria-label="Previous page"
                    ><span class="usa-pagination__link-text">Previous</span></a
                  >
                </li>
                <li
                  class="usa-pagination__item usa-pagination__page-no usa-current"
                >
                  <a
                    href="?page=1"
                    class="usa-pagination__button"
                    aria-current="page"
                    aria-label="Page 1"
                    >1</a
                  >
                </li>
                <li class="usa-pagination__item usa-pagination__page-no">
                  <a
                    href="?page=2"
                    class="usa-pagination__button"
                    aria-label="Page 2"
                    >2</a
                  >
                </li>
                <li class="usa-pagination__item usa-pagination__page-no">
                  <a
                    href="?page=3"
                    class="usa-pagination__button"
                    aria-label="Page 3"
                    >3</a
                  >
                </li>
                <li class="usa-pagination__item usa-pagination__overflow">
                  <span>…</span>
                </li>
                <li class="usa-pagination__item usa-pagination__page-no">
                  <a
                    href="?page=25"
                    class="usa-pagination__button"
                    aria-label="Page 25"
                    >25</a
                  >
                </li>
                <li class="usa-pagination__item usa-pagination__arrow">
                  <a
                    href="?page=2"
                    class="usa-pagination__link usa-pagination__next-page"
                    aria-label="Next page"
                    ><span class="usa-pagination__link-text">Next</span></a
                  >
                </li>
              </ul>
            </nav>
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
                alt="Department of Health home"
              />
              <h2 class="maryland-footer__agency-name" id="agency-footer">
                Department of Health
              </h2>
            </a>
          </div>
          <hr aria-hidden="true" class="maryland-footer__divider" />
          <div class="maryland-footer__agency-menu">
            <div class="maryland-footer__agency-contact">
              <div class="maryland-footer__link-group">
                <h3 class="maryland-footer__link-group-heading">Contact us</h3>
                <ul class="maryland-footer__link-group-list">
                  <li>201 W. Preston Street, Baltimore, MD 21201</li>
                  <li>An official agency of the State of Maryland</li>
                  <li><a href="tel:4105556500">410-555-6500</a></li>
                  <li>
                    <a href="mailto:mdh.publicaffairs@maryland.gov"
                      >mdh.publicaffairs@maryland.gov</a
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

Skipnav + banner + `maryland-header` with Department of Health branding.

### 2. Hero — `landing-regular` (no image, no description-buttons modifier)

We use the white `landing-regular` variant because the body of the page is itself busy (filters + collection); a colored hero would compete. The hero's title is derived from the content type ("News and press releases") and the description is a short orientation sentence. The listing-page convention sets the page title from the content type — so `news` produces "News" + "/news", `location` produces "Locations" + "/locations", etc. See [maryland-hero](../components/maryland-hero.md).

### 3. Sidebar — `maryland-sidenav`

The listing-page template typically renders a richer sidenav than the basic shell, with a longer item list. We've simplified to four sibling entries here, which is closer to what a real agency news section actually has.

### 4. Intro paragraph

A single short `usa-prose` paragraph orients the visitor before the filters and result list.

### 5. Filter strip — `usa-form` + `usa-input` + `usa-select` + `usa-button`

A `<form role="search">` with one text input and two selects, plus apply/clear buttons. Using `usa-form` gives consistent spacing between fields; the `grid-row grid-gap` arranges them inline on tablet+. See [usa-form](../components/usa-form.md), [usa-input](../components/usa-input.md), [usa-select](../components/usa-select.md), and [usa-button](../components/usa-button.md).

### 6. Result count

A single line of body text ("1–10 of 247 results") above the collection — pure markup, no special component.

### 7. Results — `usa-collection`

`usa-collection` is the canonical Maryland listing component (there is no `maryland-collection`). Each `<li class="usa-collection__item">` has an optional thumbnail (`usa-collection__img`), a heading link, a description, and `usa-collection__meta` for date + tag pills. The headings are `<h2>` because each item is a top-level result on this page. See [usa-collection](../components/usa-collection.md).

### 8. Pagination — `usa-pagination`

USWDS pagination with previous/next arrows, individual page numbers, and an overflow `…` ellipsis between distant pages. Set `aria-current="page"` on the active page button. See [usa-pagination](../components/usa-pagination.md).

### 9. Footers

`maryland-footer` then `<maryland-statewide-footer>`, in that order.

## Common customizations

- **Switch content type.** The listing-page template supports `news`, `event`, `location`, `contact`, and `document`. Update the hero title, breadcrumb label, sidenav links, and the collection item shape (e.g. events have date pills + venue, documents have file-size + format pills).
- **Use the headings-only `usa-collection` variant.** For a denser list without images or descriptions, swap the items for `<li class="usa-collection__item usa-collection__item--headings-only">` and keep only the heading + meta. See [usa-collection](../components/usa-collection.md).
- **Add the hero image.** Change `no-image` to `has-image` on the hero `<section>` and add a `<div class="maryland-hero__img-container">` block. The hero will go two-column.
- **Add a global alert above the header** — `<div class="maryland-alert">…</div>` between banner and header.
- **Hide the sidebar.** Replace the two-column `grid-row` with a single `<div class="grid-col-12 desktop:grid-col-8 desktop:grid-offset-2">`. Useful for top-level listing pages where there's no sibling-page list to show.
- **Change footer agency info** — edit the `maryland-footer` block.

## What you should NOT do

1. **Don't use `maryland-card-group` for the results.** Cards are for tile-like browsing of related-but-different items (e.g. service tiles). For homogeneous lists where each row has the same metadata shape (date, tag, description), `usa-collection` is the design system's answer.
2. **Don't omit the result count.** Users navigating with pagination need a reference for where they are in the list. Even "Showing 1–10 of 247" is enough.
3. **Don't put the filter form *above* the hero.** The hero is the page identity; filters belong inside the content column.
4. **Don't use `<h1>` on collection items.** Each result is `<h2>` (one level below the hero `<h1>`). If you skip from `<h1>` to `<h3>` you've broken WCAG 1.3.1.
5. **Don't add a "Sort by" select with no implementation.** If the page can't actually re-sort, omit the control. Half-functional filters frustrate users more than no filters.
