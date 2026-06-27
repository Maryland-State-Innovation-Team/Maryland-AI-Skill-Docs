# Recipe: Action Page

An action page guides a visitor through a specific task or program — applying for benefits, scheduling an appointment, requesting records. It uses an "action hero" (built on the `landing-regular` variant) with a breadcrumb, title, description, and a column of **featured action items** in place of the usual hero photo. The body presents related actions grouped under headings, with descriptions and a deep-link for each, plus optional "related resources" and "related agencies" panels.

Visually: gray banner → agency header → white hero with breadcrumb, title, and description on the left, plus a stacked list of clickable featured-action links on the right (where a hero image would otherwise sit) → two-column body with `maryland-sidenav` left and `maryland-action-items` (heading + description + link per item) right → agency footer → statewide footer.

> **Important:** Do not simplify the markup below — every BEM modifier class and wrapper element is required by either the CDN stylesheet or the JS bundle. If you need to modify a component, read its file under `cdn/components/` first.

## When to use this recipe

- A program landing page focused on a single topic where the goal is "pick the action that fits you" (e.g. food assistance, housing help, behavioral health).
- Pages that need a featured-action panel up-front (3–5 specific tasks the visitor probably came here to do).
- Service-completion pages: "here's how to apply / what you'll need / what comes next."
- Where the page is content-light but action-heavy.

## Page structure

1. `usa-skipnav`
2. `usa-banner`
3. `maryland-header`
4. `<main>` opens, `<div class="grid-container">`
5. Action hero — `maryland-hero--landing-regular` with a `maryland-featured-actions` panel on the right
6. Two-column body:
   - `<aside>`: `maryland-sidenav`
   - `<div id="page-content">`: introductory prose + `maryland-action-items` group (each item has title, subtitle, description, and a link) + a `maryland-callout` or `maryland-action-resources` section
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
    <title>Food and nutrition assistance — Maryland Department of Human Services</title>

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
          alt="Department of Human Services home"
        />
        <span class="maryland-header__agency"
          >Department of Human Services</span
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
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/benefits"
                aria-current="page"
                >Benefits</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/family-services"
                >Family services</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/child-support"
                >Child support</a
              >
            </li>
            <li class="maryland-nav__item maryland-nav__item--level-one">
              <a
                class="maryland-nav__link maryland-nav__link--level-one"
                href="/find-office"
                >Find an office</a
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
              class="maryland-hero maryland-hero--landing-regular action-hero has-illustration has-image"
              aria-labelledby="hero-title"
            >
              <div class="maryland-hero__container">
                <div class="maryland-hero__row">
                  <div class="maryland-hero__content">
                    <div class="maryland-hero__breadcrumb">
                      <nav class="maryland-breadcrumb" aria-label="Breadcrumb">
                        <ol class="maryland-breadcrumb__list">
                          <li class="maryland-breadcrumb__item">
                            <a href="/" class="maryland-breadcrumb__link"
                              >Home</a
                            >
                          </li>
                          <li class="maryland-breadcrumb__item">
                            <a
                              href="/benefits"
                              class="maryland-breadcrumb__link"
                              >Benefits</a
                            >
                          </li>
                          <li
                            class="maryland-breadcrumb__item maryland-breadcrumb__item--current"
                          >
                            <span aria-current="page"
                              >Food and nutrition</span
                            >
                          </li>
                        </ol>
                      </nav>
                    </div>
                    <h1 id="hero-title" class="maryland-hero__title">
                      Food and nutrition
                    </h1>
                    <div class="maryland-hero__description">
                      <p>
                        Maryland supports healthy starts and good nutrition for
                        all ages. If you or your family need help affording
                        food, these programs can help.
                      </p>
                    </div>
                  </div>
                  <div class="maryland-hero__img-container">
                    <div class="maryland-featured-actions">
                      <ul class="maryland-featured-actions__list">
                        <li class="maryland-featured-actions__item">
                          <div>
                            <a
                              class="maryland-featured-actions__link"
                              href="/benefits/snap/apply"
                              >Apply for SNAP benefits</a
                            >
                          </div>
                        </li>
                        <li class="maryland-featured-actions__item">
                          <div>
                            <a
                              class="maryland-featured-actions__link"
                              href="/benefits/wic"
                              >Find a WIC clinic near you</a
                            >
                          </div>
                        </li>
                        <li class="maryland-featured-actions__item">
                          <div>
                            <a
                              class="maryland-featured-actions__link"
                              href="/benefits/screener"
                              >Check eligibility in 5 minutes</a
                            >
                          </div>
                        </li>
                      </ul>
                    </div>
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
                    href="/benefits"
                    class="maryland-sidenav__link maryland-sidenav__link--level-1"
                    >Benefits</a
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
                        >Food and nutrition</span
                      >
                    </li>
                    <li
                      class="maryland-sidenav__item maryland-sidenav__item--level-2"
                    >
                      <a
                        href="/benefits/cash"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Cash assistance</a
                      >
                    </li>
                    <li
                      class="maryland-sidenav__item maryland-sidenav__item--level-2"
                    >
                      <a
                        href="/benefits/energy"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Energy assistance</a
                      >
                    </li>
                    <li
                      class="maryland-sidenav__item maryland-sidenav__item--level-2"
                    >
                      <a
                        href="/benefits/medicaid"
                        class="maryland-sidenav__link maryland-sidenav__link--level-2"
                        >Medical assistance</a
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
                Several Maryland programs help cover the cost of food. Which
                one is right for you depends on your household size, income,
                and whether anyone is pregnant or under five. If you're not
                sure where to start, the eligibility screener will point you
                in the right direction in about five minutes.
              </p>
            </div>

            <section
              class="maryland-action-group block-spacing"
              aria-labelledby="programs-heading"
            >
              <h2 id="programs-heading" class="maryland-action-group__title">
                Food and nutrition programs
              </h2>
              <p class="maryland-action-group__description">
                Pick the program that matches your household situation.
              </p>
              <ul class="maryland-action-group__list">
                <li class="maryland-action-item">
                  <h3 class="maryland-action-item__heading">
                    Food assistance for women and young children
                  </h3>
                  <p class="maryland-action-item__subtitle">
                    Women, Infants, and Children (WIC)
                  </p>
                  <p class="maryland-action-item__description">
                    If you're pregnant, a new parent, or have a child under
                    five, WIC offers nutrition advice, breastfeeding support,
                    and healthy foods. Most Maryland households earning up to
                    185% of the federal poverty level qualify.
                  </p>
                  <a
                    class="maryland-action-item__link"
                    href="/benefits/wic"
                    >Learn more and make a WIC appointment</a
                  >
                </li>
                <li class="maryland-action-item">
                  <h3 class="maryland-action-item__heading">
                    Food assistance for low-income households
                  </h3>
                  <p class="maryland-action-item__subtitle">
                    Supplemental Nutrition Assistance Program (SNAP)
                  </p>
                  <p class="maryland-action-item__description">
                    SNAP helps low-income households buy the groceries they
                    need. Most Marylanders apply online and receive an EBT
                    card in the mail within 30 days.
                  </p>
                  <a
                    class="maryland-action-item__link"
                    href="/benefits/snap/apply"
                    >Apply for SNAP</a
                  >
                </li>
                <li class="maryland-action-item">
                  <h3 class="maryland-action-item__heading">
                    Community meals for seniors
                  </h3>
                  <p class="maryland-action-item__subtitle">
                    Maryland Senior Meals Program
                  </p>
                  <p class="maryland-action-item__description">
                    More than 250 senior centers across Maryland serve hot
                    meals and offer health programs. Most are free or low-cost
                    for residents 60+.
                  </p>
                  <a
                    class="maryland-action-item__link"
                    href="/benefits/senior-meals"
                    >Find a senior meal site near you</a
                  >
                </li>
                <li class="maryland-action-item">
                  <h3 class="maryland-action-item__heading">
                    Summer meals for school-age children
                  </h3>
                  <p class="maryland-action-item__subtitle">
                    Summer Food Service Program (SFSP)
                  </p>
                  <p class="maryland-action-item__description">
                    Free summer meals for children 18 and under at hundreds of
                    schools, libraries, parks, and faith communities across
                    Maryland. No application required.
                  </p>
                  <a
                    class="maryland-action-item__link"
                    href="/benefits/summer-meals"
                    >Find a summer meal site</a
                  >
                </li>
              </ul>
            </section>

            <section class="block-spacing">
              <section
                class="maryland-callout"
                aria-labelledby="next-steps-heading"
              >
                <div class="maryland-callout__container">
                  <div class="maryland-callout__content">
                    <h2
                      id="next-steps-heading"
                      class="maryland-callout__title"
                    >
                      Not sure where to start?
                    </h2>
                    <div class="maryland-callout__description">
                      <p>
                        The Maryland benefits screener walks you through a
                        short questionnaire and tells you which programs you
                        may qualify for. It takes about five minutes, is
                        confidential, and includes a direct link to apply
                        for any program you qualify for at
                        <a href="/benefits/screener">benefits.maryland.gov</a
                        >.
                      </p>
                    </div>
                  </div>
                </div>
              </section>
            </section>

            <section
              class="maryland-action-resources block-spacing"
              aria-labelledby="resources-heading"
            >
              <h2
                id="resources-heading"
                class="maryland-action-resources__title"
              >
                Related resources and agencies
              </h2>
              <p class="maryland-action-resources__description">
                More places to get help with food, nutrition, and benefits in
                Maryland.
              </p>
              <div class="maryland-action-resources__groups">
                <div class="maryland-action-resources__group">
                  <h3 class="maryland-action-resources__group-title">
                    Related resources
                  </h3>
                  <ul>
                    <li>
                      <a href="/benefits/snap/restaurant-meals"
                        >Use SNAP at participating restaurants</a
                      >
                    </li>
                    <li>
                      <a href="/benefits/snap/online-grocery"
                        >Use SNAP for online grocery shopping</a
                      >
                    </li>
                    <li>
                      <a href="/benefits/snap/p-ebt"
                        >Pandemic EBT (P-EBT) for school children</a
                      >
                    </li>
                    <li>
                      <a href="/benefits/food-banks"
                        >Find a food bank or pantry</a
                      >
                    </li>
                  </ul>
                </div>
                <div class="maryland-action-resources__group">
                  <h3 class="maryland-action-resources__group-title">
                    Related agencies
                  </h3>
                  <ul>
                    <li>
                      <a href="https://health.maryland.gov/wic"
                        >Department of Health (WIC program)</a
                      >
                    </li>
                    <li>
                      <a href="https://www.marylandhungersolutions.org"
                        >Maryland Hunger Solutions</a
                      >
                    </li>
                    <li>
                      <a href="https://aging.maryland.gov"
                        >Maryland Department of Aging</a
                      >
                    </li>
                  </ul>
                </div>
              </div>
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
                alt="Department of Human Services home"
              />
              <h2 class="maryland-footer__agency-name" id="agency-footer">
                Department of Human Services
              </h2>
            </a>
          </div>
          <hr aria-hidden="true" class="maryland-footer__divider" />
          <div class="maryland-footer__agency-menu">
            <div class="maryland-footer__agency-contact">
              <div class="maryland-footer__link-group">
                <h3 class="maryland-footer__link-group-heading">Contact us</h3>
                <ul class="maryland-footer__link-group-list">
                  <li>25 S. Charles Street, Baltimore, MD 21201</li>
                  <li>An official agency of the State of Maryland</li>
                  <li><a href="tel:8003329747">1-800-555-9747</a></li>
                  <li>
                    <a href="mailto:dhs.communications@maryland.gov"
                      >dhs.communications@maryland.gov</a
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

Standard skipnav + banner + header from [page-shell.md](../page-shell.md). The header carries the Department of Human Services brand.

### 2. Action hero

The action page reuses the `maryland-hero--landing-regular` markup but swaps the right-column photo for a `maryland-featured-actions` list — 3–5 prominent action links. The action-page variant adds the `action-hero` class to the hero `<section>` for spacing tweaks. Breadcrumb uses the "light" (blue-on-white) variant. See [maryland-hero](../components/maryland-hero.md) and [maryland-action-items](../components/maryland-action-items.md).

### 3. Sidebar — `maryland-sidenav`

Same two-column sidebar pattern. The current page (`"Food and nutrition"`) is shown as plain text with `aria-current="page"`, with siblings ("Cash assistance," "Energy assistance," "Medical assistance") linked.

### 4. Intro paragraph — `usa-prose`

A single paragraph orients the user. Wrapped in `usa-prose` so links and body text pick up Maryland defaults.

### 5. Programs — `maryland-action-items`

A `<section class="maryland-action-group">` containing a heading, optional description, and a `<ul class="maryland-action-group__list">` of action items. Each `<li class="maryland-action-item">` has heading, subtitle (program code/name), description, and a link. This is the core of the action page. See [maryland-action-items](../components/maryland-action-items.md).

### 6. Not-sure callout — `maryland-callout`

A `maryland-callout` recommending the benefits screener. Callouts are the right pattern for "stop and notice" content that isn't urgent enough to be a `maryland-alert`. See [maryland-callout](../components/maryland-callout.md).

### 7. Related resources and agencies — `maryland-action-resources`

A `<section class="maryland-action-resources">` containing two side-by-side groups: one for related resources, one for related agencies. Each group is a simple `<ul>` of links. The component renders these in a two-column grid at tablet+ and stacks them on mobile.

### 8. Footers

`maryland-footer` (DHS contact) → `<maryland-statewide-footer>`.

## Pattern: a form with a submit/cancel button row

If your action page is **the form itself** (not a launchpad into a form), here's the canonical pattern for the submit row at the bottom. **The submit row must be a `<ul class="usa-button-group">` with each button wrapped in a `<li class="usa-button-group__item">` — without the `__item` wrapper, the buttons collapse together with no spacing.** See `cdn/components/usa-button-group.md`.

```html
<form class="usa-form" action="/submit" method="post">
  <!-- ... form fields ... -->

  <ul class="usa-button-group margin-top-6" aria-label="Form actions">
    <li class="usa-button-group__item">
      <a href="/cancel" class="usa-button usa-button--outline">Cancel</a>
    </li>
    <li class="usa-button-group__item">
      <button type="submit" class="usa-button">Continue to step 2</button>
    </li>
  </ul>
</form>
```

Bare `<div class="usa-button-group">` with two `<button>`s as direct children is **wrong** — the buttons render touching each other.

For multi-step forms, pair this row with a `<ol class="usa-step-indicator__segments">` at the top (see `cdn/components/usa-step-indicator.md`).

## Common customizations

- **Drop the featured-actions panel.** Remove the `maryland-hero__img-container` (the panel sits there). The hero becomes single-column with just breadcrumb + title + description.
- **More/fewer featured actions.** 3 is typical, 5 is the practical max — beyond that the list outgrows the hero column.
- **Skip the Related resources section.** Drop the entire `maryland-action-resources` block if there's nothing meaningful to link to.
- **Replace the callout with a `maryland-step-list`.** For service-completion flows where order matters ("Step 1: Apply. Step 2: Submit documents. Step 3: Interview."), `maryland-step-list` is a stronger fit than `maryland-callout`.
- **Remove the sidebar.** Replace the two-column row with `<div class="grid-col-12 desktop:grid-col-8 desktop:grid-offset-2">`.
- **Add a global alert above the header** — `<div class="maryland-alert maryland-alert--warning">…</div>` between `usa-banner` and `maryland-header`.
- **Change footer agency info** — edit `agencyTitle`, `contactAddress`, `parentAgency`, `contactPhone`, `contactEmail` in `maryland-footer`.

## What you should NOT do

1. **Don't use the `basic` hero for action pages.** The blue `basic` hero has no place to put the featured-actions column. Use `landing-regular` (this recipe's choice).
2. **Don't replace `maryland-action-items` with a `maryland-card-group`.** Cards are for browsing, not for guiding through a specific task list. Action items are visually denser, lighter on chrome, and lead with the description rather than an image.
3. **Don't write the featured-actions list as a `<ol>` (ordered).** Featured actions are alternatives, not sequential steps. If you need a sequence, use `maryland-step-list` in the body instead.
4. **Don't omit the page `<h1>`.** The hero title is the page's only `<h1>`. Action group titles ("Food and nutrition programs") are `<h2>`, action item titles are `<h3>`.
5. **Don't link the featured-actions to anchors on the same page.** They should be deep links to the actual application/eligibility flow. If you only have anchor links, you don't have featured actions — you have a Table of Contents, and the basic-page recipe is a better fit.
