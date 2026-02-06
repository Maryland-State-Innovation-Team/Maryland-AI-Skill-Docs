# Maryland Web Design System (MDWDS) - LLM Skill Document

*Generated on 2026-02-05*

## Overview

The Maryland Web Design System (MDWDS) is a design system for building Maryland state government websites. This document provides comprehensive guidance on using MDWDS components via CDN.

## Getting Started

### CDN Setup

**IMPORTANT:** The version number in CDN URLs should NOT include the `v` prefix, even though version tags may show it.

Include the following in your HTML `<head>`:

```html
<link rel="stylesheet" href="https://cdn.maryland.gov/mdwds/0.37.0/css/mdwds.min.css">
<script src="https://cdn.maryland.gov/mdwds/0.36.0/js/mdwds-init.js, https://cdn.maryland.gov/mdwds/0.36.0/js/mdwds-core.js" defer></script>
```

### Additional Setup Notes

Add the stylesheet and scripts to your <head>. To prevent flashes of unstyled content (FOUC), use the mdwds-init.js script or inline its functionality to add the 'usa-js-loading' class to the document element, removing it upon window load or after an 8-second timeout.

## Foundation

Foundation elements define the core visual language of MDWDS including colors, typography, spacing, and grid systems.

### Block Spacing

Each component manages its own block-spacing, and a .block-spacing class is available to manage spacing between component blocks on a page.

```html
<!-- Use the .block-spacing class on component wrappers -->
<div class="block-spacing">
  <!-- Component content -->
</div>
```

**CSS Classes:**
- `block-spacing`

**Variants:**
- Full Width
- Single Column
- With Sidebar

**Usage Notes:**
The blocks represent components placed on the page. Each component manages its own block-spacing.

**Accessibility:**
No specific accessibility notes provided for block spacing.

### Colors

Maryland Theme Colors and utility classes for text and background, based on USWDS and Maryland's state colors.

```html
<!-- Background Color Example -->
<div class="bg-primary">...</div>

<!-- Text Color Example -->
<p class="text-primary">...</p>
```

**CSS Classes:**
- `.bg-primary`
- `.bg-secondary`
- `.bg-accent-cool`
- `.bg-accent-warm`
- `.bg-base`
- `.text-primary`
- `.text-base-dark`

**Variants:**
- lightest
- lighter
- light
- default
- vivid
- dark
- darker
- darkest

**Usage Notes:**
Use .bg-[color]-[variant] for backgrounds and .text-[color]-[variant] for text. The system uses a palette reflecting Maryland's natural features and state flag.

**Accessibility:**
Ensure sufficient contrast when combining text and background colors. Refer to USWDS accessibility guidelines for color combinations.

### Logo

Usage guidelines, color variables, and HTML examples for the Maryland Logo.

```html
<p class="maryland-color-logo-red">This text uses the red logo color</p>
```

**CSS Classes:**
- `maryland-color-logo-red`
- `maryland-color-logo-gold`
- `maryland-color-logo-black`
- `maryland-color-logo-white`

**Variants:**
- Vertical Logo
- Horizontal Logo

**Usage Notes:**
Use Vertical Logo for general applications. Use Horizontal Logo only when space constraints require it. Do not outline, distort, or manipulate the logo. Do not use unapproved color variations.

**Accessibility:**
Logo colors provided with specific hex codes: Red (#c8122c), Gold (#ffc838), Black (#231f20), White (#ffffff).

### Typography

MDWDS typography guidelines featuring Source Sans Pro Web (default) and Merriweather (alternate) typefaces, including utility classes for sizing and best practices.

```html
<link rel="stylesheet" href="https://cdn.maryland.gov/mdwds/latest/css/mdwds.min.css" />
<p class="font-sans-md">Sans-serif text example</p>
<p class="font-serif-lg">Serif text example</p>
```

**CSS Classes:**
- `font-sans-3xs`
- `font-sans-2xs`
- `font-sans-xs`
- `font-sans-sm`
- `font-sans-md`
- `font-sans-lg`
- `font-sans-xl`
- `font-sans-2xl`
- `font-sans-3xl`
- `font-serif-3xs`
- `font-serif-2xs`
- `font-serif-xs`
- `font-serif-sm`
- `font-serif-md`
- `font-serif-lg`
- `font-serif-xl`
- `font-serif-2xl`
- `font-serif-3xl`

**Variants:**
- Source Sans Pro Web
- Merriweather

**Usage Notes:**
Set a base font size of 16px on html or body. Use Source Sans Pro Web as the primary font. Maintain clear visual hierarchy with h1-h6 levels.

**Accessibility:**
Ensure color contrast and spacing meet or exceed WCAG AA requirements.

## MDWDS Components

Components are reusable UI elements that can be combined to build pages.

### Accordion (Drupal)

Accordions are a list of headings that hide or reveal additional content when selected. Use when users only need specific pieces of content or space is limited.

```html
<section class="maryland-accordion" aria-labelledby="id-rk2ic9kcwib">
  <div class="maryland-accordion__list">
    <h2 class="maryland-accordion__list--heading" id="id-rk2ic9kcwib">Accordion Title</h2>
    <p class="maryland-accordion__list--content">Accordion description text.</p>
  </div>
  <div class="maryland-accordion__items">
    <div class="maryland-accordion__item">
      <h3 class="maryland-accordion__heading">
        <button type="button" class="maryland-accordion__button" aria-expanded="true">First Amendment</button>
      </h3>
      <div class="maryland-accordion__content" role="region">
        <div class="usa-prose">Congress shall make no law...</div>
      </div>
    </div>
  </div>
</section>
```

**CSS Classes:**
- `maryland-accordion`
- `maryland-accordion__list`
- `maryland-accordion__list--heading`
- `maryland-accordion__list--content`
- `maryland-accordion__items`
- `maryland-accordion__item`
- `maryland-accordion__heading`
- `maryland-accordion__button`
- `maryland-accordion__content`

**Variants:**
- Drupal implementation

**Usage Notes:**
Use when users need specific pieces of content. Avoid if most of the page should be visible or if there isn't much content.

**Accessibility:**
Uses aria-expanded and aria-controls for accessibility. Headings (h2, h3) provide structure.

### Action Items

Action items provide a list of tasks or steps that users need to complete. They can be displayed with icons, status indicators, and optional descriptions.

```html
<div class="maryland-featured-actions">
  <ul class="maryland-featured-actions__list">
    <li class="maryland-featured-actions__item">
      <div class="maryland-featured-actions__link">
        <a href="#">Learn more and make an appointment today</a>
      </div>
    </li>
  </ul>
</div>
```

**CSS Classes:**
- `maryland-featured-actions`
- `maryland-featured-actions__list`
- `maryland-featured-actions__item`
- `maryland-featured-actions__link`

**Variants:**
- Featured Actions
- Action Spotlight
- Action Group
- Action Hero
- Action Page Contents

**Usage Notes:**
Used to guide users through specific processes or provide quick access to resources. Variants include spotlights, groups, and hero integrations.

**Accessibility:**
Ensure links have descriptive text and the list structure is maintained for screen readers.

### Alert (Drupal)

Alerts communicate important information to users in a clear, timely, and accessible manner. Supports ARIA roles, live region updates, and labeling.

```html
<div class="maryland-alert maryland-alert--info" role="status" aria-labelledby="maryland-alert-id-m9truts10b">
  <div class="maryland-alert__container">
    <div class="maryland-alert__body">
      <h2 class="maryland-alert__heading" id="maryland-alert-id-m9truts10b">Informational status</h2>
      <div class="maryland-alert__text">
        <p>Lorem ipsum dolor sit amet, <a class="usa-link maryland-link" href="#">consectetur adipiscing</a> elit, sed do eiusmod.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
      </div>
    </div>
  </div>
</div>
```

**CSS Classes:**
- `maryland-alert`
- `maryland-alert--info`
- `maryland-alert--warning`
- `maryland-alert--success`
- `maryland-alert--error`
- `maryland-alert--emergency`
- `maryland-alert__container`
- `maryland-alert__body`
- `maryland-alert__heading`
- `maryland-alert__text`

**Variants:**
- info
- warning
- success
- error
- emergency
- slim
- noIcon

**Usage Notes:**
Use for important information. HTML is allowed in message content. Supports slim variant and icon toggling.

**Accessibility:**
Supports ARIA roles (role='status'), live region updates, and aria-labelledby for screen readers.

### Automatic List (Drupal)

Automatic List displays a grid of linked cards that guide users to different sections or resources. Each card is fully clickable and uses the Linked variant of the Maryland Cards component.

```html
<section class="maryland-automatic-list" aria-labelledby="id-6ggdirxmld">
  <div class="maryland-automatic-list__header">
    <div class="maryland-automatic-list__header-content">
      <h2 class="maryland-automatic-list__title" id="id-6ggdirxmld">Latest updates</h2>
      <p class="maryland-automatic-list__description">Maryland is the perfect place to start your business...</p>
    </div>
    <div class="maryland-automatic-list__more-link">
      <a class="maryland-link" href="#all-services">Learn more about our latest updates and more</a>
    </div>
  </div>
  <ul class="maryland-card-group">
    <li class="maryland-card maryland-card--linked tablet-lg:grid-col-6 desktop-lg:grid-col-4">
      <a class="maryland-card__link" href="/services/business">
        <div class="maryland-card__container">
          <div class="maryland-card__media"><div class="maryland-card__img"><img src="..." alt="..." /></div></div>
          <div class="maryland-card__header"><h3 class="maryland-card__heading">...</h3></div>
          <div class="maryland-card__body"><p>...</p></div>
          <div class="maryland-card__footer maryland-card__footer--right"><span aria-hidden="true" class="maryland-card__icon maryland-card__icon--arrow"></span></div>
        </div>
      </a>
    </li>
  </ul>
</section>
```

**CSS Classes:**
- `maryland-automatic-list`
- `maryland-automatic-list__header`
- `maryland-automatic-list__title`
- `maryland-automatic-list__description`
- `maryland-automatic-list__more-link`
- `maryland-card-group`
- `maryland-card`
- `maryland-card--linked`

**Variants:**
- Default
- With Sidebar

**Usage Notes:**
Used for content types: Basic Page, Contacts, Documents, Locations, News, Videos. Cards are fully clickable.

**Accessibility:**
Uses aria-labelledby for the section title. Cards use aria-label for descriptive link text.

### Breadcrumb

The MDWDS Breadcrumb component helps users navigate back to previous pages. It's based on USWDS Breadcrumb with Maryland-specific styling.

```html
<div class="maryland-breadcrumb__wrapper maryland-breadcrumb__wrapper--light">
  <nav aria-label="Breadcrumbs" class="usa-breadcrumb maryland-breadcrumb maryland-breadcrumb--light">
    <ol class="usa-breadcrumb__list maryland-breadcrumb__list">
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <a class="usa-breadcrumb__link maryland-breadcrumb__link" href="/"><span>Home</span></a>
      </li>
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <a class="usa-breadcrumb__link maryland-breadcrumb__link" href="/level1"><span>Link Level 1</span></a>
      </li>
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item usa-current" aria-current="page">
        <span class="usa-breadcrumb__link maryland-breadcrumb__link"><span>Current Page</span></span>
      </li>
    </ol>
  </nav>
</div>
```

**CSS Classes:**
- `maryland-breadcrumb__wrapper`
- `maryland-breadcrumb__wrapper--light`
- `maryland-breadcrumb__wrapper--dark`
- `usa-breadcrumb`
- `maryland-breadcrumb`
- `usa-breadcrumb__list`
- `maryland-breadcrumb__list`
- `usa-breadcrumb__list-item`
- `maryland-breadcrumb__list-item`
- `usa-breadcrumb__link`
- `maryland-breadcrumb__link`
- `usa-current`

**Variants:**
- Light
- Dark

**Usage Notes:**
Pass an array of page strings or objects with label and href properties. The last item in the array is automatically marked as the current page (not linked). Support for wrapping and RDFa metadata. Accessible with ARIA attributes.

**Accessibility:**
Accessible with ARIA attributes. Current page is marked with aria-current='page' and is not linked.

### Callout (Drupal)

Use a callout to highlight important information with a description and optional title and image.

```html
<section class="maryland-callout" aria-labelledby="id-7h784218eol">
  <div class="maryland-callout__container">
    <div class="maryland-callout__image">
      <img src="https://placehold.co/400x400/1976d2/white/webp" alt="" />
    </div>
    <div class="maryland-callout__content">
      <h2 id="id-7h784218eol" class="maryland-callout__title">Your government is committed to serving Marylanders</h2>
      <div class="maryland-callout__description">
        The goal of Maryland's state government is to serve the public and represent Marylanders' interests.
      </div>
    </div>
  </div>
</section>
```

**CSS Classes:**
- `maryland-callout`
- `maryland-callout__container`
- `maryland-callout__image`
- `maryland-callout__content`
- `maryland-callout__title`
- `maryland-callout__description`

**Variants:**
- Default

**Usage Notes:**
Use to highlight important info. Title and image are optional. Description is required.

**Accessibility:**
The title can be visually hidden while remaining accessible to screen readers using the hideTitle control.

### Cards (Drupal)

Maryland Design System cards are modular containers that group related information in a visually distinct format. Ideal for highlighting articles, events, news, or services. Supports images, headings, subheadings, text, links, link lists, and link buttons.

```html
<ul class="maryland-card-group">
  <li class="maryland-card maryland-card--simple tablet-lg:grid-col-6 desktop-lg:grid-col-4">
    <div class="maryland-card__container">
      <div class="maryland-card__header">
        <h3 class="maryland-card__heading">Maryland Card Title</h3>
      </div>
      <div class="maryland-card__body">
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
      </div>
      <div class="maryland-card__footer maryland-card__footer--left">
        <div class="maryland-card__footer-content">
          <a class="usa-button usa-button--primary" href="#">More Link</a>
        </div>
      </div>
    </div>
  </li>
</ul>
```

**CSS Classes:**
- `maryland-card-group`
- `maryland-card`
- `maryland-card--simple`
- `maryland-card--media`
- `maryland-card--flag`
- `maryland-card--linked`
- `maryland-card--full`
- `maryland-card__container`
- `maryland-card__header`
- `maryland-card__heading`
- `maryland-card__body`
- `maryland-card__footer`

**Variants:**
- Simple
- Media Card
- Flag Card
- Linked Card
- Full Card

**Usage Notes:**
Cards manage their own block-spacing. A .block-spacing utility class is available. Images and links in examples use placeholders.

**Accessibility:**
Ensure heading levels follow a logical hierarchy within the card and the page.

### Footer

The Footer component provides a consistent global or agency-specific footer for Maryland state websites, including links to services, government information, policies, and contact details.

```html
HTML code retrieved via evaluate in this step.
```

**CSS Classes:**
- `maryland-footer`
- `maryland-footer__container`
- `maryland-footer__section`
- `maryland-footer__title`
- `maryland-footer__content`
- `maryland-footer__link-group`
- `maryland-footer__link-group-heading`
- `maryland-footer__link-group-list`

**Variants:**
- Global
- Agency
- Full

**Usage Notes:**
Each component manages its own block-spacing. A .block-spacing class is available for use with components on the page.

**Accessibility:**
Uses aria-labelledby for sections and navigation groups. Includes a screen-reader only heading for the footer.

### Header (Drupal)

A header helps users identify where they are and provides a quick, organized way to reach the main sections of a website. Includes agency title, utility menu, primary navigation, and search.

```html
See extracted_content_10.md and evaluate result
```

**CSS Classes:**
- `maryland-header`
- `maryland-header__util-nav-container`
- `maryland-header__util-nav`
- `maryland-header__home`
- `maryland-header__logo`
- `maryland-search-form`
- `maryland-nav`

**Variants:**
- Default

**Usage Notes:**
The Header component includes an optional utility menu, primary navigation, and search interface. It also features the Maryland wordmark.

**Accessibility:**
Includes skip to main content links and aria-labels for navigation toggles.

### Hero

The Landing Main Hero component displays a full-width landscape background image with text overlay for landing pages. Features include a full-width background image, title with auto-detected eyebrow, and optional description.

```html
<section class="maryland-hero maryland-hero--landing-main" aria-labelledby="id-n0xh1rx54gp">
  <img alt="" class="maryland-hero__background-image" src="https://designsystem.maryland.gov/assets/md_forest-DB-269v5.png" />
  <div class="maryland-hero__container">
    <div class="grid-container">
      <div class="grid-row">
        <div class="grid-col-12">
          <div class="maryland-hero__content">
            <h1 class="maryland-hero__title" id="id-n0xh1rx54gp">
              <span class="maryland-hero__eyebrow">Welcome to</span>
              <span class="maryland-hero__title-text">Maryland</span>
            </h1>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

**CSS Classes:**
- `maryland-hero`
- `maryland-hero--landing-main`
- `maryland-hero__background-image`
- `maryland-hero__container`
- `maryland-hero__content`
- `maryland-hero__title`
- `maryland-hero__eyebrow`
- `maryland-hero__title-text`

**Variants:**
- Landing Main
- Landing Agency
- Landing Regular
- Basic
- News
- Location

**Usage Notes:**
Ideal for Maryland.gov homepage. Background image should have gradient layers merged. Titles starting with 'Welcome to ' auto-style the prefix as an eyebrow.

**Accessibility:**
Uses aria-labelledby to associate the section with the hero title.

### Highlight

The Highlight component displays up to 3 columns of featured links with a header with optional visibility, optional description.

```html
<section class="maryland-highlight" aria-labelledby="id-7cyg9t97sg3"><h2 class="maryland-highlight__section-title" id="id-7cyg9t97sg3">Benefits, services and business</h2><p class="maryland-highlight__section-description">Find the right information you need today in these featured areas.</p><div class="maryland-highlight__grid"><div class="maryland-highlight__item"><h3 class="maryland-highlight__title">Benefits</h3><ul class="maryland-highlight__links"><li class="maryland-highlight__link"><a href="javascript:void(0)"><span class="maryland-highlight__link-text">Health and medical</span><span aria-hidden="true" class="maryland-highlight__link-icon"></span></a></li></ul><a class="maryland-highlight__more-link" href="javascript:void(0)">More benefits</a></div></div></section>
```

**CSS Classes:**
- `.maryland-highlight`
- `.maryland-highlight__section-title`
- `.maryland-highlight__section-description`
- `.maryland-highlight__grid`
- `.maryland-highlight__item`
- `.maryland-highlight__title`
- `.maryland-highlight__links`
- `.maryland-highlight__link`
- `.maryland-highlight__link-text`
- `.maryland-highlight__link-icon`
- `.maryland-highlight__more-link`

**Variants:**
- Default
- With Sidebar

**Usage Notes:**
Displays up to 3 columns of featured links. Each column can contain a title, description, up to 5 links, and an optional 'more' link.

**Accessibility:**
Uses aria-labelledby for the section title. External links should include appropriate aria-labels.

### LinkCollection (Drupal)

Use a link collection to present a curated list of related links with an optional description and call-to-action.

```html
See previous extraction for HTML structure.
```

**CSS Classes:**
- `maryland-link-collection`
- `maryland-link-collection__container`
- `maryland-link-collection__header`
- `maryland-link-collection__title`
- `maryland-link-collection__description`
- `maryland-link-collection__list`
- `maryland-link-collection__item`
- `maryland-link-collection__link`

**Variants:**
- Default
- With Item Descriptions
- Without More Link
- Mixed Descriptions
- Stacked

**Usage Notes:**
Use for curated lists of related links. Title is required, description and more-link are optional.

**Accessibility:**
Ensure links have descriptive text. External links should have appropriate aria-labels.

### Links (Drupal)

A collection of link styles including document, labelled, external, and skip links.

```html
See extracted documentation for multiple variants.
```

**CSS Classes:**
- `maryland-link`
- `maryland-link--document`
- `maryland-link--labelled`
- `maryland-link--external`
- `maryland-link--skipnav`

**Variants:**
- Default
- Document Link
- Labelled Link
- External Link
- Skip Link
- Skip Link Sidebar

**Usage Notes:**
Used for various navigation and action purposes. Skip links are essential for accessibility.

**Accessibility:**
Includes skip links for keyboard navigation and aria-describedby for labelled links.

### Listing Page

Listing page components are used to display grouped items such as services, resources, or agency listings, often including filtering and pagination.

```html
See extracted content for full structural HTML.
```

**CSS Classes:**
- `maryland-listing-page`
- `maryland-listing-item`

**Variants:**
- Listing Results
- Listing Item

**Usage Notes:**
Supports introductory body text, filtering by type/category, and pagination. Configurable item media and metadata.

**Accessibility:**
Includes skip links and ARIA labels for pagination and filters.

### Navigation

The navigation component provides a primary way for users to move through a site, including search and nested menu items.

```html
Captured via evaluate
```

**CSS Classes:**
- `maryland-nav`
- `maryland-search-form`
- `maryland-nav__items`
- `maryland-nav__toggle`

**Variants:**
- Default

**Usage Notes:**
Overview TBD. Includes search and multi-level navigation items.

**Accessibility:**
Uses aria-label for navigation toggle and search labels.

### Promo (Drupal)

Use a promo to visually highlight a single call to action link. Variants include Plain, Image, and Illustration.

```html
<section class="maryland-promo maryland-promo--plain" aria-labelledby="id-onu840emoim"><div class="maryland-promo__container"><div class="maryland-promo__row"><div class="maryland-promo__title-container"><h2 class="maryland-promo__title" id="id-onu840emoim">Your voice, your state: building a better tomorrow</h2></div><div class="maryland-promo__content-container"><div class="maryland-promo__description">We’re committed to serving you...</div><div class="maryland-promo__link"><a href="#">Share your feedback</a></div></div></div></div></section>
```

**CSS Classes:**
- `maryland-promo`
- `maryland-promo--plain`
- `maryland-promo--contained`
- `maryland-promo--stacked`
- `maryland-promo__container`
- `maryland-promo__row`
- `maryland-promo__title-container`
- `maryland-promo__title`
- `maryland-promo__content-container`
- `maryland-promo__description`
- `maryland-promo__link`

**Variants:**
- Default
- Contained
- Stacked
- Plain
- Image
- Illustration

**Usage Notes:**
Use for single call-to-action links. Title is required. Link Title and URL are required.

**Accessibility:**
The section uses aria-labelledby to associate the title with the promo container.

### Search

The Search component provides a search interface for the site.

```html
<div class="maryland-search-form maryland-search-form--toggleable">
  <form class="maryland-search-form__form" role="search" action="#" hidden="" id="id-3hx45ck3e9u">
    <label class="usa-sr-only" for="id-5s0vlq1zh0t">Search</label>
    <div class="maryland-search-form__widget">
      <input class="maryland-search-form__input" type="text" name="q" autocomplete="on" id="id-5s0vlq1zh0t" />
      <button type="submit" aria-label="Submit Search" class="maryland-search-form__submit"></button>
    </div>
  </form>
  <a href="#!" class="maryland-search-form__toggle" aria-label="Site search"></a>
</div>
```

**CSS Classes:**
- `maryland-search-form`
- `maryland-search-form--toggleable`
- `maryland-search-form__form`
- `maryland-search-form__widget`
- `maryland-search-form__input`
- `maryland-search-form__submit`
- `maryland-search-form__toggle`

**Variants:**
- Pop Out
- Static
- Hero
- Results

**Usage Notes:**
Overview: TBD

**Accessibility:**
Uses aria-label for search toggle and submit button. Includes a screen-reader-only label for the search input.

### Side Navigation

Hierarchical, vertical navigation to place at the side of a page.

```html
See extracted_content_20.md
```

**CSS Classes:**
- `usa-sidenav`
- `usa-sidenav__item`
- `usa-sidenav__sublist`

**Variants:**
- Default
- In Sidebar

**Usage Notes:**
Used for hierarchical, vertical navigation.

**Accessibility:**
Ensure proper heading levels and link descriptions are used within the navigation structure.

### Statewide Banner

The Banner tells people that the site (or application) is a secure and official Maryland government site. It is required on all pages and positioned at the top.

```html
<script type="module" src="https://cdn.maryland.gov/mdwds/latest/components/maryland-statewide-banner.js"></script>
<maryland-statewide-banner>
  <noscript>
    <link rel="stylesheet" href="https://cdn.maryland.gov/mdwds/latest/css/mdwds.min.css">
    <div class="maryland-alert maryland-alert--warning">
      <div class="maryland-alert__body">
        <h4 class="maryland-alert__heading">JavaScript Required</h4>
        <p class="maryland-alert__text">JavaScript is required to use content on this page.</p>
      </div>
    </div>
  </noscript>
</maryland-statewide-banner>
```

**CSS Classes:**
- `maryland-alert`
- `maryland-alert--warning`
- `maryland-alert__body`
- `maryland-alert__heading`
- `maryland-alert__text`

**Variants:**
- Default

**Usage Notes:**
Required on all pages. Positioned at the top. Uses a custom element and a script module from the CDN.

**Accessibility:**
Includes a noscript fallback with a warning alert if JavaScript is disabled.

### Statewide Footer

A standardized footer component for Maryland.gov websites, providing consistent navigation and branding via a CDN-hosted custom element.

```html
<script type="module" src="https://cdn.maryland.gov/mdwds/latest/components/maryland-statewide-footer.js"></script>
<maryland-statewide-footer></maryland-statewide-footer>
```

**Usage Notes:**
Recommended for use via CDN to ensure latest updates. Intended to be non-editable in most cases.

**Accessibility:**
Reinforces public trust and aligns with Maryland’s digital service standards and USWDS.

### Summary Box (Drupal)

The Maryland Summary Box component highlights important information in a visually prominent container. It is ideal for surfacing key takeaways, action items, or warnings.

```html
<div role="region" class="maryland-summary-box" aria-labelledby="maryland-summary-box-id-6ng37uluhvv">
  <div class="maryland-summary-box__inner">
    <h2 class="maryland-summary-box__heading" id="maryland-summary-box-id-6ng37uluhvv">Key information</h2>
    <div class="maryland-summary-box__text">
      <ul class="maryland-summary-box__list">
        <li>If you are under a winter storm warning, <a href="#">find shelter</a> right away.</li>
        <li>Sign up for <a href="#">your community's warning system</a>.</li>
        <li>Learn the signs of, and basic treatments for, <a href="#">frostbite</a> and <a href="#">hypothermia</a>.</li>
        <li>Gather emergency supplies for your <a href="#">home</a> and your <a href="#">car</a>.</li>
        <li>Review and update your <a href="#">emergency plan</a> annually.</li>
      </ul>
    </div>
  </div>
</div>
```

**CSS Classes:**
- `maryland-summary-box`
- `maryland-summary-box__inner`
- `maryland-summary-box__heading`
- `maryland-summary-box__text`
- `maryland-summary-box__list`

**Variants:**
- Default

**Usage Notes:**
Use for highlighting key information, action items, or warnings that users should not miss.

**Accessibility:**
Uses role='region' and aria-labelledby to provide context to screen readers.

### Table of Contents (Drupal)

Use a table of contents to provide in-page navigation to the various sections of the page.

```html
Captured in previous step
```

**CSS Classes:**
- `maryland-toc`
- `maryland-sidenav`

**Variants:**
- Default

**Usage Notes:**
Provides in-page navigation. Often used with a sidebar layout.

**Accessibility:**
Uses nav element with aria-labelledby and buttons for toggles.

### Utility Nav

The utility navigation provides quick access to secondary actions and account-related links in the header. It supports both standard links and button-styled CTAs.

```html
<div class="maryland-header__util-nav-container">
  <ul class="maryland-header__util-nav">
    <li><a href="#!">Link One</a></li>
    <li><a href="#!">Link Two</a></li>
    <li><a class="usa-button usa-button--small" href="#!">Button</a></li>
  </ul>
</div>
```

**CSS Classes:**
- `maryland-header__util-nav-container`
- `maryland-header__util-nav`
- `usa-button`
- `usa-button--small`

**Variants:**
- Desktop
- Mobile

**Usage Notes:**
The utility nav appears at the top of the header on desktop viewports and in the mobile menu on smaller screens. Supports plain links and button-styled links.

**Accessibility:**
Ensure links have descriptive labels.

### Video Promo

The Video Promo component is used to visually highlight a single call-to-action link alongside video content. It supports various layouts including full-width, video-first, and text-first.

```html
<section class="maryland-video-promo maryland-video-promo--side-by-side" aria-labelledby="id-p5x7nbu1olh">
  <div class="maryland-video-promo__container">
    <div class="maryland-video-promo__content">
      <h2 id="id-p5x7nbu1olh" class="maryland-video-promo__title">Video Promo</h2>
      <p class="maryland-video-promo__description">Culpa esse excepteur commodo velit mollit amet amet mollit consequat irure ipsum sint sint.</p>
      <a class="maryland-video-promo__link" href="https://example.com">Call to action</a>
    </div>
    <figure class="maryland-video-promo__video">
      <iframe src="https://player.vimeo.com/video/1084537" frameborder="0"></iframe>
      <figcaption>Big Buck Bunny is an open source film commonly used for demo purposes.</figcaption>
    </figure>
  </div>
</section>
```

**CSS Classes:**
- `maryland-video-promo`
- `maryland-video-promo--side-by-side`
- `maryland-video-promo__container`
- `maryland-video-promo__content`
- `maryland-video-promo__title`
- `maryland-video-promo__description`
- `maryland-video-promo__link`
- `maryland-video-promo__video`

**Variants:**
- Full-width
- Video first
- Text first

**Usage Notes:**
Use a promo to visually highlight a single call to action link. Requires a title. Description and link are optional. Layout can be adjusted via properties.

**Accessibility:**
The title is used as the aria-label for the section. Title can be visually hidden while remaining accessible to screen readers.

### Visual Link Collection (Drupal)

A collection of visual links or cards used to highlight specific content or services.

```html
<section class="maryland-visual-link-collection" aria-labelledby="id-wk8ua0s1j9">
  <div class="maryland-visual-link-collection__header">
    <div class="maryland-visual-link-collection__header-content">
      <h2 class="maryland-visual-link-collection__title" id="id-wk8ua0s1j9">Latest updates</h2>
      <p class="maryland-visual-link-collection__description">Maryland is the perfect place to start your business...</p>
    </div>
    <div class="maryland-visual-link-collection__more-link">
      <a class="maryland-link" href="#all-services">Learn more about our latest updates and more</a>
    </div>
  </div>
  <ul class="maryland-card-group">
    <li class="maryland-card maryland-card--linked">
      <a class="maryland-card__link" href="/services/business">
        <div class="maryland-card__container">
          <div class="maryland-card__media">
            <div class="maryland-card__img">
              <img src="https://placehold.co/432x325/blue/white/webp" alt="Business services illustration" />
            </div>
          </div>
          <div class="maryland-card__header">
            <h3 class="maryland-card__heading">Federal Financial Assistance for Farmers Affected by Drought</h3>
          </div>
          <div class="maryland-card__body">Lorem ipsum dolor sit amet...</div>
          <div class="maryland-card__footer maryland-card__footer--right">
            <span aria-hidden="true" class="maryland-card__icon maryland-card__icon--arrow"></span>
          </div>
        </div>
      </a>
    </li>
  </ul>
</section>
```

**CSS Classes:**
- `maryland-visual-link-collection`
- `maryland-visual-link-collection__header`
- `maryland-visual-link-collection__title`
- `maryland-visual-link-collection__description`
- `maryland-visual-link-collection__more-link`
- `maryland-card-group`
- `maryland-card`
- `maryland-card--linked`

**Variants:**
- Default
- With Sidebar

**Usage Notes:**
Used to display a group of related links with visual emphasis using cards.

**Accessibility:**
Uses aria-labelledby for the section and aria-hidden for decorative icons.

### Visual Link Collection (Drupal)

A collection of cards with images and links used to highlight latest updates or services.

```html
See extracted code
```

**CSS Classes:**
- `maryland-visual-link-collection`
- `maryland-visual-link-collection__header`
- `maryland-card-group`

**Variants:**
- Default
- With Sidebar

**Usage Notes:**
Used for visual navigation to key sections or updates.

**Accessibility:**
Uses aria-labelledby for the section title.

## Templates

Templates are pre-built page layouts combining multiple components.

### Maryland Homepage

The primary landing page for the State of Maryland, featuring a statewide banner, header with search, mega-menu navigation, hero section, and comprehensive footer.

```html
Code not available in Docs view.
```

**Usage Notes:**
High-level landing page for state-level information and services. Follows a semantic flow: Statewide Banner -> Header -> Navigation -> Hero -> Footer -> Statewide Footer.

### Action Page

A standard governmental layout designed to facilitate specific user tasks, featuring a two-column layout with a sidebar and primary action-oriented content.

```html
<header>
  <!-- Statewide Banner Component -->
  <!-- Agency Header with Search and Utility Nav -->
</header>

<nav aria-label="Main navigation">
  <!-- Main Navigation Component -->
</nav>

<nav aria-label="Breadcrumbs">
  <!-- Breadcrumb Component -->
</nav>

<main>
  <div class="layout-grid">
    <aside>
      <!-- Side Navigation / Section Menu -->
    </aside>
    
    <article>
      <h1>Page Title</h1>
      <p class="intro">Summary text...</p>
      <ul class="action-items">
        <!-- Action Item Links -->
      </ul>
      <section class="content">
        <!-- Body Text -->
      </section>
    </article>
  </div>
</main>

<footer>
  <!-- Agency Footer Section -->
  <!-- Statewide Footer Section -->
</footer>
```

**Usage Notes:**
Used for pages where the primary goal is for the user to take specific actions or find specific resources. Includes a section menu for deep navigation within a department.

### Landing Page

A template for landing pages, featuring a hero section, navigation, and various content blocks.

```html
HTML code not directly available via 'Show code' button.
```

**Usage Notes:**
Used for high-level landing pages like Maryland.gov.

### Listing Page

A template for displaying a collection of related items with filtering and pagination capabilities.

```html
<header>
  <!-- Statewide Banner -->
  <!-- Agency Header (Title & Search) -->
  <!-- Primary Navigation -->
</header>

<main>
  <nav aria-label="Breadcrumb">...</nav>
  
  <div class="layout-container">
    <h1>Contacts listing page</h1>
    <p class="description">...</p>

    <div class="grid-row">
      <!-- Sidebar -->
      <aside class="side-navigation">
        <h2>Section menu</h2>
        <ul>...</ul>
      </aside>

      <!-- Main Listing Area -->
      <section class="listing-content">
        <div class="filters">
          <input type="text" placeholder="Filter text">
          <select>...</select>
          <button>Filter</button>
        </div>

        <div class="results-count">Showing X-Y of Z results</div>

        <ul class="listing-items">
          <li class="listing-item">
            <img src="..." alt="...">
            <span>Category</span>
            <h2>Item Title</h2>
            <time>Date</time>
            <p>Description...</p>
            <ul>...</ul>
          </li>
        </ul>

        <nav aria-label="Pagination">...</nav>
      </section>
    </div>
  </div>
</main>

<footer>
  <!-- Agency Contact & Social Links -->
  <!-- Statewide Links & Policies -->
  <!-- Maryland.gov Wordmark -->
</footer>
```

**Usage Notes:**
Designed to display a collection of related items (such as contacts, news, or services) with filtering and pagination capabilities.

### Location Page

A template for displaying specific location information, including address, office hours, and contact details.

```html
HTML structure involves Header, Navigation, Breadcrumbs, Main content with location details and sidebar for contact info, and Footer.
```

**Usage Notes:**
Used for agency locations or service centers.

## Utilities

Utility classes for common styling needs.

### Layout Grid

A responsive 12-column layout system based on Flexbox, designed for flexible and consistent page structures. Supports fixed-width, auto-layout, fill, and offset column behaviors.

```html
<div class="grid-container">
  <div class="grid-row">
    <div class="tablet:grid-col bg-base-lightest padding-2 border text-center font-mono">
      tablet:grid-col
    </div>
    <div class="tablet:grid-col bg-base-lightest padding-2 border text-center font-mono">
      tablet:grid-col
    </div>
    <div class="tablet:grid-col bg-base-lightest padding-2 border text-center font-mono">
      tablet:grid-col
    </div>
  </div>
</div>
```

**CSS Classes:**
- `grid-container`
- `grid-row`
- `grid-col-[1-12]`
- `grid-col-auto`
- `grid-col-fill`
- `tablet:grid-col-[n]`
- `grid-gap-sm`
- `grid-gap-lg`

**Usage Notes:**
Use .grid-container to constrain the grid. Use .grid-row for rows and .grid-col variants for columns. Combine with utility classes for padding and alignment.

## Best Practices

1. **Always use the CDN** - Use the official Maryland CDN for CSS and JS files
2. **Version pinning** - Pin to a specific version to avoid breaking changes
3. **Semantic HTML** - Use appropriate HTML5 semantic elements
4. **Accessibility** - Follow WCAG 2.1 AA guidelines
5. **Mobile-first** - MDWDS is designed mobile-first; test on all screen sizes
6. **Component composition** - Combine components as documented; avoid custom overrides
