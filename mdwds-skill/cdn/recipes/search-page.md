# Recipe: Search Page

The search page renders search results for a Maryland.gov site. It uses a dedicated `maryland-search-hero` block: a blue header strip with the page `<h1>` ("Search Results for ...") and a prominent re-search input + scope toggle ("this site" vs. "All Maryland.gov sites"). Below the hero, results are rendered by Google Custom Search Engine (GCSE), wrapped in a `maryland-search-results` container so the design system can theme the GCSE output to match Maryland branding.

Visually: gray banner → agency header (no agency name on search pages) → blue search hero with title and re-search form → result count + sort control → GCSE-rendered result list inside a `maryland-search-results` wrapper → pagination → statewide footer only (no agency footer on search pages).

> **Important:** Do not simplify the markup below — every BEM modifier class and wrapper element is required by either the CDN stylesheet or the JS bundle. If you need to modify a component, read its file under `cdn/components/` first.

## When to use this recipe

- A site-wide search results page for any Maryland.gov property.
- Pages that re-issue a query and render Google Custom Search Engine results.
- A "no results" or "did you mean?" page (same structure, different content state).

## Page structure

1. `usa-skipnav`
2. `usa-banner` — note that search pages hide the `Maryland.gov` and flag links
3. `maryland-header` — no agency name; no utility nav
4. `<main>` opens, `<div class="grid-container margin-top-10">`
5. `maryland-search-hero` — blue band with `<h1>` and the static search form (with scope toggle)
6. `maryland-search-results` — wrapper for the GCSE-rendered result list and pagination cursor
7. `<main>` closes
8. **No** `maryland-footer` — search pages render the statewide footer only (no agency footer)
9. `<maryland-statewide-footer>`

## Full assembled HTML

```html
<!doctype html>
<!-- Pin to a specific version in production. See cdn/setup.md. -->
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Search results for "real id" — Maryland.gov</title>

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

    <!-- Google Custom Search Engine (renders the result list inside maryland-search-results below). -->
    <script async src="https://cse.google.com/cse.js?cx=YOUR_CSE_ID"></script>
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
        <div class="maryland-nav__mobile-panel" id="md-nav-panel-1">
          <div class="maryland-nav__mobile-slot">
            <div class="maryland-search-form">
              <form
                action="/search"
                role="search"
                class="maryland-search-form__form"
                id="mobile-nav-search-form"
              >
                <label
                  class="maryland-search-form__label usa-sr-only"
                  for="mobile-nav-search-input"
                  >Search</label
                >
                <div class="maryland-search-form__widget">
                  <input
                    class="maryland-search-form__input"
                    type="text"
                    autocomplete="on"
                    name="q"
                    placeholder="How do I..."
                    id="mobile-nav-search-input"
                  />
                  <button
                    type="submit"
                    class="maryland-search-form__submit"
                  >
                    Search
                  </button>
                </div>
              </form>
            </div>
          </div>
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
          </ul>
        </div>
      </nav>
      <hr aria-hidden="true" class="maryland-header__divider" />
    </header>

    <main id="main-content" tabindex="-1">
      <div class="grid-container margin-top-10">
        <div class="grid-row">
          <div class="grid-col-12">
            <section
              class="maryland-search-hero"
              aria-labelledby="search-hero-title"
            >
              <h1 class="maryland-search-hero__title" id="search-hero-title">
                Search Results for "real id"
              </h1>
              <div class="maryland-search-form">
                <form
                  action="/search"
                  method="get"
                  role="search"
                  class="maryland-search-form__form"
                  id="search-form"
                >
                  <label
                    class="maryland-search-form__label usa-sr-only"
                    for="search-input"
                    >Search</label
                  >
                  <div class="maryland-search-form__widget">
                    <input
                      class="maryland-search-form__input"
                      type="text"
                      autocomplete="on"
                      name="q"
                      value="real id"
                      placeholder="How do I..."
                      id="search-input"
                    />
                    <button
                      type="submit"
                      class="maryland-search-form__submit"
                    >
                      Search
                    </button>
                  </div>

                  <fieldset class="usa-fieldset maryland-search-form__scope">
                    <legend class="usa-sr-only">Select a search scope</legend>
                    <div class="usa-radio">
                      <input
                        class="usa-radio__input"
                        id="scope-site"
                        type="radio"
                        name="scope"
                        value="mva.maryland.gov"
                        checked
                      />
                      <label class="usa-radio__label" for="scope-site"
                        >mva.maryland.gov</label
                      >
                    </div>
                    <div class="usa-radio">
                      <input
                        class="usa-radio__input"
                        id="scope-all"
                        type="radio"
                        name="scope"
                        value="all"
                      />
                      <label class="usa-radio__label" for="scope-all"
                        >All Maryland.gov sites</label
                      >
                    </div>
                  </fieldset>
                </form>
              </div>
            </section>
          </div>
        </div>

        <div class="grid-row desktop:margin-bottom-15">
          <div class="grid-col-12">
            <div class="maryland-search-results">
              <!--
                The Google Custom Search Engine script (loaded in <head>)
                will inject the result list into this container at runtime.
                Below is an example of the rendered structure for
                documentation purposes. In a live page, gcse.js will replace
                this with the live results for the current query.
              -->
              <div class="gsc-results-wrapper-nooverlay gsc-results-wrapper-visible">
                <div class="gsc-above-wrapper-area">
                  <table class="gsc-above-wrapper-area-container">
                    <tbody>
                      <tr>
                        <td class="gsc-result-info-container">
                          <div class="gsc-result-info">
                            About 12,300 results (0.18 seconds)
                          </div>
                        </td>
                        <td class="gsc-orderby-container">
                          <div class="gsc-orderby">
                            <div class="gsc-orderby-label gsc-inline-block">
                              Sort by:
                            </div>
                            <div
                              class="gsc-option-menu-container gsc-inline-block"
                            >
                              <div
                                class="gsc-selected-option-container gsc-inline-block"
                              >
                                <div class="gsc-selected-option">Relevance</div>
                              </div>
                            </div>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <div class="gsc-wrapper">
                  <div class="gsc-resultsbox-visible">
                    <div class="gsc-resultsRoot gsc-tabData gsc-tabdActive">
                      <div class="gsc-results gsc-webResult">
                        <div class="gsc-expansionArea">
                          <div class="gsc-webResult gsc-result">
                            <div class="gs-webResult gs-result">
                              <div class="gs-title">
                                <a
                                  class="gs-title"
                                  href="https://mva.maryland.gov/Pages/realid.aspx"
                                  >Maryland <b>REAL ID</b> — Motor Vehicle
                                  Administration</a
                                >
                              </div>
                              <div class="gsc-url-top">
                                <div class="gs-visibleUrl gs-visibleUrl-short">
                                  mva.maryland.gov
                                </div>
                              </div>
                              <div class="gs-snippet">
                                Beginning May 7, 2026, federal agencies will
                                only accept a <b>REAL ID</b>-compliant Maryland
                                driver's license or another federally-accepted
                                document to board domestic flights.
                              </div>
                            </div>
                          </div>

                          <div class="gsc-webResult gsc-result">
                            <div class="gs-webResult gs-result">
                              <div class="gs-title">
                                <a
                                  class="gs-title"
                                  href="https://mva.maryland.gov/realid/documents"
                                  >What documents do I need for a
                                  <b>REAL ID</b>?</a
                                >
                              </div>
                              <div class="gsc-url-top">
                                <div class="gs-visibleUrl gs-visibleUrl-short">
                                  mva.maryland.gov › realid › documents
                                </div>
                              </div>
                              <div class="gs-snippet">
                                Bring documents proving identity, Social
                                Security number, and two proofs of Maryland
                                residency to your MVA appointment.
                              </div>
                            </div>
                          </div>

                          <div class="gsc-webResult gsc-result">
                            <div class="gs-webResult gs-result">
                              <div class="gs-title">
                                <a
                                  class="gs-title"
                                  href="https://mva.maryland.gov/realid/appointments"
                                  >Schedule a <b>REAL ID</b> appointment</a
                                >
                              </div>
                              <div class="gsc-url-top">
                                <div class="gs-visibleUrl gs-visibleUrl-short">
                                  mva.maryland.gov › realid › appointments
                                </div>
                              </div>
                              <div class="gs-snippet">
                                You must appear in person at an MVA branch to
                                upgrade to a <b>REAL ID</b>. Schedule online
                                or call 410-555-7000.
                              </div>
                            </div>
                          </div>
                        </div>

                        <div class="gsc-cursor-box gs-bidi-start-align">
                          <div class="gsc-cursor">
                            <div
                              class="gsc-cursor-page gsc-cursor-current-page"
                              tabindex="0"
                            >
                              1
                            </div>
                            <div
                              class="gsc-cursor-page"
                              aria-label="Page 2"
                              role="link"
                              tabindex="0"
                            >
                              2
                            </div>
                            <div
                              class="gsc-cursor-page"
                              aria-label="Page 3"
                              role="link"
                              tabindex="0"
                            >
                              3
                            </div>
                            <div
                              class="gsc-cursor-page"
                              aria-label="Page 4"
                              role="link"
                              tabindex="0"
                            >
                              4
                            </div>
                            <div
                              class="gsc-cursor-page"
                              aria-label="Page 5"
                              role="link"
                              tabindex="0"
                            >
                              5
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <maryland-statewide-footer></maryland-statewide-footer>
  </body>
</html>
```

## Section-by-section breakdown

### 1. Shell

Standard skipnav + banner + header. On search pages, the banner is configured without the Maryland flag and without the Maryland.gov link, but the Translate widget stays. The header runs with no agency name and no utility nav — a logo-only horizontal header. The primary nav stays enabled.

### 2. Search hero — `maryland-search-hero`

The search hero is a standalone block (not a `maryland-hero` variant). It renders a blue band containing:
- `<h1 class="maryland-search-hero__title">` with the current query (`Search Results for "real id"`).
- A `maryland-search-form` with the input, submit button, and a scope `<fieldset>` (radio choice between the current site and all Maryland.gov sites).

The hero label is hidden because the page title already names the action. See [maryland-search-form](../components/maryland-search-form.md).

### 3. Result wrapper — `maryland-search-results`

A `<div class="maryland-search-results">` wraps the GCSE output. The CDN ships styles that re-theme the GCSE markup (`gsc-result`, `gs-title`, `gsc-cursor-page`, etc.) to match Maryland's typography, link color, and spacing. When the GCSE script (`cse.js`) loads, it injects the live results into this container at runtime, replacing any placeholder content.

### 4. Result count + sort

GCSE generates the result-count line ("About 12,300 results (0.18 seconds)") and the "Sort by: Relevance / Date" toggle inside `gsc-above-wrapper-area`. The Maryland stylesheet themes these to Maryland body text and link colors. You don't write this markup — GCSE does.

### 5. Result items

GCSE renders each result as a `gsc-result` block with title link, visible URL, snippet, and breadcrumb. Maryland's stylesheet hides the visible URL's long-form variant, restyles the title link to MDWDS blue, and tightens the spacing between items.

### 6. Pagination cursor

GCSE's `gsc-cursor-box` produces a numeric page cursor. The CDN restyles this to look like `usa-pagination` (without the prev/next arrows, since GCSE doesn't provide them).

### 7. Footer — statewide only

Search pages explicitly omit the agency footer. The search page belongs to the platform, not to any single agency, so only `<maryland-statewide-footer>` goes at the bottom.

## Common customizations

- **Switch from GCSE to a custom search backend.** Replace the `maryland-search-results` content with your own result-list markup. The stylesheet's GCSE-specific selectors won't apply, so you'd need to use the design system's body typography and link colors directly. Consider using `usa-collection` for the results (similar to the listing-page recipe).
- **Hide the scope toggle.** Remove the `<fieldset class="usa-fieldset maryland-search-form__scope">` block. Useful when the page is search for one site only with no option to broaden.
- **Add an agency footer.** Include a `<footer class="maryland-footer">` block above `<maryland-statewide-footer>`. Use this only on agency-branded search pages.
- **Add a global alert above the header** — `<div class="maryland-alert">…</div>` between `usa-banner` and `maryland-header`.
- **Customize the empty-results state.** When GCSE returns no results, it renders a "Your search did not match any documents" message inside the same `maryland-search-results` wrapper. Style overrides should target `.gsc-no-results-found`.

## What you should NOT do

1. **Don't include an agency footer by default.** Search pages omit it. Search pages are platform-level; reintroducing the agency footer turns the page into an agency page, which is the wrong framing.
2. **Don't use `maryland-hero--landing-regular` or any other hero variant.** Search has its own `maryland-search-hero` block. Reusing a hero variant means losing the integrated search form and scope toggle.
3. **Don't render your own GCSE markup.** GCSE rewrites the DOM at runtime — anything you put inside `maryland-search-results` is replaced by `cse.js` once it loads. Use the placeholder structure only for static documentation or styling reference.
4. **Don't omit the `<h1>` from the hero.** Even with a strong visual identity ("Search Results for …"), screen readers need the `<h1>` to identify the page.
5. **Don't write the query in plain text.** Echo the user's query inside quotes (`"real id"`) and ensure the value is HTML-escaped on the server before render — bare text from the URL is an XSS vector.
6. **Don't put a `maryland-sidenav` on this page.** Search results stand alone; there's no sibling-page navigation to offer.
