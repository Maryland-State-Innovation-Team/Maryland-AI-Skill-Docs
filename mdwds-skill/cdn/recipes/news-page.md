# Recipe: News Page

The news page renders a single news article, press release, public notice, or media advisory. The hero is the `news` variant: a blue background with breadcrumb, news type label, published date, and the article title. The hero does **not** support a hero image — featured imagery goes inside the article body as a `<figure>`. The body is a long-form prose layout with optional "Updated:" date, headings, lists, blockquotes, a right-floated image, and an embedded video.

Visually: gray banner → agency header → blue news hero with breadcrumb, title, news-type tag, and published date → two-column body with `maryland-sidenav` left and full prose article right (featured figure, headings, lists, blockquote, floated image, video) → agency footer → statewide footer.

> **Important:** Do not simplify the markup below — every BEM modifier class and wrapper element is required by either the CDN stylesheet or the JS bundle. If you need to modify a component, read its file under `cdn/components/` first.

## When to use this recipe

- A single press release.
- A news article on an agency news section.
- A public notice or media advisory.
- Any standalone article-shaped page where the page identity is the article (not a section landing or service detail).

## Page structure

1. `usa-skipnav`
2. `usa-banner`
3. `maryland-header`
4. `<main>` opens
5. `maryland-hero` with `variant="news"`, breadcrumb, news type, published date — **no image** (the news variant ignores image input)
6. Two-column body with `<div class="grid-container">`:
   - `<aside>`: `maryland-sidenav` (siblings within the news section)
   - `<div id="page-content">`: `usa-prose` containing:
     - Optional "Updated:" date with `<hr>`
     - Featured `<figure>` with image + caption
     - `<h2>`, `<h3>`, `<h4>` body headings
     - `<p>`, `<ul>`, `<ol>`, `<blockquote>` body content
     - Right-floated `<figure class="float-right">`
     - Embedded video `<figure>` with `<iframe>` + `<figcaption>`
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
      MDOT awards $48M Purple Line construction contract — Department of
      Transportation
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
          alt="Department of Transportation home"
        />
        <span class="maryland-header__agency"
          >Department of Transportation</span
        >
      </a>
      <nav class="maryland-nav" aria-label="Primary navigation">
        <button
          class="maryland-nav__toggle"
          aria-label="Toggle Nav"
          type="button"
        ></button>
        <div class="maryland-nav__mobile-panel" id="md-nav-panel-news">
          <ul class="maryland-nav__items maryland-nav__items--level-one">
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/highways"
                >Highways</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/transit"
                >Transit</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/aviation"
                >Aviation</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one maryland-nav__link--active-trail"
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
      <section
        class="maryland-hero maryland-hero--news maryland-hero--flush has-illustration no-image"
        aria-labelledby="hero-title"
      >
        <div class="maryland-hero__container">
          <div class="maryland-hero__content">
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
                      href="/news"
                      class="usa-breadcrumb__link maryland-breadcrumb__link"
                      ><span>News</span></a
                    >
                  </li>
                  <li
                    class="usa-breadcrumb__list-item maryland-breadcrumb__list-item usa-current"
                    aria-current="page"
                  >
                    <span
                      class="usa-breadcrumb__link maryland-breadcrumb__link"
                      ><span
                        >MDOT awards $48M Purple Line construction contract</span
                      ></span
                    >
                  </li>
                </ol>
              </nav>
            </div>
            <h1 id="hero-title" class="maryland-hero__title">
              MDOT awards $48 million Purple Line construction contract
            </h1>
            <div class="maryland-hero__meta">
              <span class="maryland-hero__news-type">Press release</span>
              <span class="maryland-hero__meta-separator">|</span>
              <span class="maryland-hero__published-date"
                >March 18, 2026</span
              >
            </div>
            <div class="maryland-hero__description">
              <p>
                The Maryland Department of Transportation today announced a
                $48 million contract for the next phase of Purple Line light
                rail construction in Prince George's County.
              </p>
            </div>
          </div>
        </div>
      </section>

      <div class="grid-container">
        <div class="grid-row grid-gap">
          <aside
            class="layout-sidebar-first grid-col-12 desktop:grid-col-3 margin-top-8 desktop:margin-top-10 desktop:margin-bottom-15"
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
                    >News</a
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
                        aria-current="page"
                        >Press releases</a
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
                        href="/news/public-notices"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Public notices</a
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
              <div class="maryland-updated-date">
                Updated:
                <time datetime="2026-03-19">March 19, 2026</time>
              </div>
              <hr aria-hidden="true" />

              <figure>
                <img
                  src="/img/purple-line-construction.jpg"
                  alt="Purple Line construction crew installing track ballast near the New Carrollton station"
                />
                <figcaption>
                  Crews install ballast along the Purple Line route near New
                  Carrollton. Credit: MDOT MTA.
                </figcaption>
              </figure>

              <h2>About the contract</h2>
              <p>
                The contract, awarded to a joint venture led by a Maryland-based
                construction firm, covers grade-crossing improvements, track
                bedding, and station-area utility relocation between the New
                Carrollton and Riverdale Park-Kenilworth stations. Work begins
                in April 2026 and is expected to conclude by spring 2028.
              </p>

              <p>
                The Purple Line is a 16.2-mile light rail line connecting
                Bethesda in Montgomery County to New Carrollton in Prince
                George's County, with 21 stations across two counties. When
                complete it will be the first major east-west transit line
                serving the inner Maryland suburbs of Washington, D.C.
              </p>

              <h3>What this means for riders</h3>
              <p>
                The contract advances the Purple Line's projected revenue
                service date of late 2027. Riders in Prince George's County
                will benefit from improved Metrobus connections at three
                stations, and the line will offer direct light-rail transfers
                to the
                <a href="#" class="maryland-link"
                  >Washington Metro Red, Green, and Orange Lines</a
                >.
              </p>

              <h4>Construction impacts</h4>
              <ul>
                <li>
                  Annapolis Road (MD-450) between Veterans Parkway and 80th
                  Avenue: nightly lane closures, 10 p.m.–5 a.m. on weekdays.
                </li>
                <li>
                  Riverdale Road: temporary detour at Kenilworth Avenue
                  during track ballast deliveries.
                </li>
                <li>
                  Pedestrian crossings at the New Carrollton station will be
                  rerouted during construction.
                </li>
              </ul>

              <h4>Funding</h4>
              <ol>
                <li>$28M from the federal Capital Investment Grant program</li>
                <li>$16M from the Maryland Transportation Trust Fund</li>
                <li>$4M from Prince George's County municipal contributions</li>
              </ol>

              <blockquote>
                <p>
                  Today's announcement is a milestone for a project that
                  Marylanders have been waiting on for more than a decade.
                  The Purple Line will be transformative for inner-suburban
                  Maryland — connecting jobs, schools, and neighborhoods that
                  have never had a direct east-west transit option.
                </p>
                <cite>
                  — Holly Arnold, MDOT MTA Administrator
                </cite>
              </blockquote>

              <h4>Background</h4>
              <figure class="float-right">
                <img
                  src="/img/purple-line-map.jpg"
                  alt="Purple Line route map from Bethesda to New Carrollton"
                />
                <figcaption>
                  Purple Line route from Bethesda to New Carrollton. Credit:
                  MDOT.
                </figcaption>
              </figure>
              <p>
                The Purple Line broke ground in 2017 under a public-private
                partnership with Purple Line Transit Partners. Following
                contractor disputes that suspended construction in 2020,
                MDOT MTA restructured the project in 2022 under a new
                concessionaire, Maryland Transit Solutions. Construction has
                proceeded under the revised schedule since.
              </p>
              <p>
                When complete, the Purple Line is expected to carry
                approximately 60,000 daily riders, including new transit users
                and current Metrobus and MARC riders shifting to faster
                light-rail service.
              </p>

              <figure>
                <iframe
                  src="https://www.youtube.com/embed/32UYjzPsZ4E"
                  frameborder="0"
                  title="MDOT Purple Line construction progress, March 2026"
                  allowfullscreen
                ></iframe>
                <figcaption>
                  MDOT Purple Line construction progress, March 2026 (3:42).
                </figcaption>
              </figure>

              <h4>Media contact</h4>
              <p>
                Sarah Whitman, MDOT MTA Office of Communications,
                <a href="mailto:swhitman@mdot.maryland.gov" class="maryland-link"
                  >swhitman@mdot.maryland.gov</a
                >, <a href="tel:4105552240" class="maryland-link"
                  >410-555-2240</a
                >.
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
                alt="Department of Transportation home"
              />
              <h2 class="maryland-footer__agency-name" id="agency-footer">
                Department of Transportation
              </h2>
            </a>
          </div>
          <hr aria-hidden="true" class="maryland-footer__divider" />
          <div class="maryland-footer__agency-menu">
            <div class="maryland-footer__agency-contact">
              <div class="maryland-footer__link-group">
                <h3 class="maryland-footer__link-group-heading">Contact us</h3>
                <ul class="maryland-footer__link-group-list">
                  <li>7201 Corporate Center Drive, Hanover, MD 21076</li>
                  <li>An official agency of the State of Maryland</li>
                  <li><a href="tel:4108658000">410-555-8000</a></li>
                  <li>
                    <a href="mailto:public.info@mdot.maryland.gov"
                      >public.info@mdot.maryland.gov</a
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

Standard skipnav + banner + header from [page-shell.md](../page-shell.md), with the Department of Transportation header and the news section flagged as the current primary-nav page.

### 2. Hero — `news` variant

The `news` variant of `maryland-hero` is a blue hero ("flush" with the header — no white gap) that renders breadcrumb, title, a meta block with news type + published date, and an optional short description. The `no-image` modifier class is **always present** because the news variant never accepts a hero image; lead imagery belongs inside the body. The meta block uses `maryland-hero__news-type` for the tag-style label ("Press release") and `maryland-hero__published-date` for the date, with a pipe separator between them. See [maryland-hero](../components/maryland-hero.md).

### 3. Sidebar — `maryland-sidenav`

The sidebar lists sibling pages within the news section: Press releases, Media advisories, Public notices, Subscribe. The current sub-section is marked with `aria-current="page"`.

### 4. Updated date

A `maryland-updated-date` block with a machine-readable `<time>` element. Followed by an `<hr aria-hidden="true">` for visual separation. The published date is shown in the hero; the updated date in the body distinguishes "first posted" from "last edited." Omit this block if the article has never been updated.

### 5. Featured figure

A `<figure>` immediately under the Updated date with the lead image and a caption (credit included). Use specific alt text — describe what's in the image, not just "image."

### 6. Article body — `usa-prose`

The whole article sits inside `<div class="usa-prose">`. Heading levels are `<h2>` (section-level: "About the contract", "Background", "Media contact"), `<h3>` (sub-section), `<h4>` (sub-sub-section). The body uses `<p>`, `<ul>`, `<ol>`, `<blockquote>` with `<cite>`, and a right-floated `<figure class="float-right">` to wrap text around a secondary image.

### 7. Embedded video — `<figure>` + `<iframe>`

A `<figure>` with a YouTube iframe and a `<figcaption>` describing the video. Always provide an iframe `title` attribute for assistive tech.

### 8. Media contact

Last block of the article: a short paragraph with the press contact's name, email link, and phone link.

### 9. Footers

`maryland-footer` (MDOT contact) → `<maryland-statewide-footer>`.

## Common customizations

- **Change the news type.** Set `maryland-hero__news-type` to one of: `Press release`, `Media advisory`, `Public notice`, `News article`. These are the four case-sensitive labels the documented variants support.
- **Omit the published date or news type.** Drop the corresponding span. The pipe separator only renders when both are present.
- **No Updated date.** Remove the `maryland-updated-date` block and its `<hr>`.
- **Single video, no featured image.** Move the `<figure><iframe></figure>` block up to the top of `usa-prose` and skip the static featured image.
- **No floated image.** Drop the `<figure class="float-right">`. Body paragraphs go full width.
- **Add a global alert above the header** — `<div class="maryland-alert">…</div>` between `usa-banner` and `maryland-header`. Useful for live press conferences ("Live: Governor's announcement at 2 PM").
- **Change footer agency info** — edit the `maryland-footer` block.

## What you should NOT do

1. **Don't put an image in the hero.** The `news` variant ignores any image input and always renders as `no-image`. Lead imagery goes inside the body, immediately under the Updated date.
2. **Don't use the `landing-regular` or `basic` heroes here.** Neither has the news-type + published-date meta block. The `news` variant is the only one that exposes those.
3. **Don't render the published date as plain text inside the meta block.** While a plain `<span>` will display correctly, you should also include a `<time datetime="YYYY-MM-DD">` element if the date is machine-readable. The meta block is a good place for a `<time>` wrapper.
4. **Don't omit `<figcaption>` on images or videos.** Captions are required for accessibility; even a one-line credit is enough.
5. **Don't skip heading levels.** Article sections are `<h2>`. If you go straight from the hero `<h1>` to `<h4>`, you've broken WCAG 1.3.1.
