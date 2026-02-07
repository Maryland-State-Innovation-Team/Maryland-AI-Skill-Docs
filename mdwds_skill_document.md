# Maryland Web Design System (MDWDS) - LLM Skill Document
*Generated on 2026-02-05*

## Overview

The Maryland Web Design System (MDWDS) is a design system for building Maryland state government websites. It is a fork of the U.S. Web Design System (USWDS), reflecting Maryland's natural features and state flag. This document provides comprehensive guidance on using MDWDS components via CDN.

## Getting Started

### CDN Setup

**IMPORTANT:** The version number in CDN URLs should NOT include the `v` prefix, even though version tags may show it.

Include the following in your HTML `<head>`:

```html
<link rel="stylesheet" href="https://cdn.maryland.gov/mdwds/0.36.0/css/mdwds.min.css">
<script src="https://cdn.maryland.gov/mdwds/0.36.0/js/mdwds-init.js" defer></script>
<script src="https://cdn.maryland.gov/mdwds/0.36.0/js/mdwds-core.js" defer></script>
```

### Additional Setup Notes

Add the stylesheet and scripts to your `<head>`. To prevent flashes of unstyled content (FOUC), use the `mdwds-init.js` script or inline its functionality to add the `usa-js-loading` class to the document element, removing it upon window load or after an 8-second timeout.

## Foundation

Foundation elements define the core visual language of MDWDS including colors, typography, spacing, and grid systems.

### Block Spacing

Each component manages its own block-spacing, and a `.block-spacing` class is available to manage spacing between component blocks on a page.

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

**Base Theme Colors:**
- **base**
- **primary**
- **secondary**
- **accent-cool**
- **accent-warm**
- **info**
- **success**
- **warning**
- **error**
- **emergency**
- **disabled**

Each color features the following variants: **lightest**, **lighter**, **light**, **default** (no suffix), **vivid**, **dark**, **darker**, **darkest**.

```html
<!-- Background Color Examples -->
<div class="bg-primary">...</div>
<div class="bg-primary-vivid">...</div>
<div class="bg-base-lightest">...</div>
<div class="bg-secondary-dark">...</div>
<div class="bg-accent-cool-lighter">...</div>
<div class="bg-success-darkest">...</div>

<!-- Text Color Examples -->
<p class="text-primary">This is primary theme text.</p>
<p class="text-base-dark">This is dark base text.</p>
<span class="text-error">Error text.</span>
```

**CSS Classes:**
- `.bg-[color]` / `.bg-[color]-[variant]` for backgrounds (e.g., `.bg-primary`, `.bg-base-lightest`, `.bg-accent-cool-lighter`)
- `.text-[color]` / `.text-[color]-[variant]` for text (e.g., `.text-primary`, `.text-base-dark`, `.text-error`)

**Usage Notes:**
Use `.bg-[color]-[variant]` for backgrounds and `.text-[color]-[variant]` for text. The system uses a palette reflecting Maryland's natural features and state flag.

**Accessibility:**
Ensure sufficient contrast when combining text and background colors. Refer to USWDS accessibility guidelines for color combinations.

### Logo

Usage guidelines, color variables, and HTML examples for the Maryland Logo.

```html
<!-- CDN link for colors stylesheet -->
<link rel="stylesheet" href="https://cdn.maryland.gov/mdwds/latest/css/colors.css"/>

<!-- Applying logo colors -->
<p class="maryland-color-logo-red">This text uses the red logo color</p>
```

**CSS Classes / Variables:**
- `maryland-color-logo-red` — Maryland Red (`--maryland-color-logo-red`: `#c8122c`)
- `maryland-color-logo-gold` — Maryland Gold (`--maryland-color-logo-gold`: `#ffc838`)
- `maryland-color-logo-black` — Black (`--maryland-color-logo-black`: `#231f20`)
- `maryland-color-logo-white` — White (`--maryland-color-logo-white`: `#ffffff`)

**Variants:**
- **Vertical Logo:** Use for general applications or as directed.
- **Horizontal Logo:** Use only when space constraints require it.

**Usage Notes:**
Do not outline, distort, or manipulate the logo. Do not use unapproved color variations or opacity. Do not alter logo colors, typefaces, or layout. Do not place logo over text, graphics, or patterns. Do not apply effects or use unapproved versions.

**Accessibility:**
Logo colors provided with specific hex codes for consistent reproduction.

### Typography

MDWDS typography guidelines featuring Source Sans Pro Web (default) and Merriweather (alternate) typefaces, including utility classes for sizing and best practices.

```html
<link rel="stylesheet" href="https://cdn.maryland.gov/mdwds/latest/css/mdwds.min.css" />
<p class="font-sans-md">Sans-serif text example</p>
<p class="font-serif-lg">Serif text example</p>
```

**CSS Classes (Sans-serif — Source Sans Pro Web):**
- `font-sans-3xs`, `font-sans-2xs`, `font-sans-xs`, `font-sans-sm`, `font-sans-md`, `font-sans-lg`, `font-sans-xl`, `font-sans-2xl`, `font-sans-3xl`

**CSS Classes (Serif — Merriweather):**
- `font-serif-3xs`, `font-serif-2xs`, `font-serif-xs`, `font-serif-sm`, `font-serif-md`, `font-serif-lg`, `font-serif-xl`, `font-serif-2xl`, `font-serif-3xl`

**Variants:**
- Source Sans Pro Web (default, automatically included via CDN/NPM)
- Merriweather (alternate, automatically included via CDN/NPM)

**Usage Notes:**
Set a base font size of 16px on `html` or `body` and scale text using relative units (`rem`, `em`). Use Source Sans Pro Web as the primary font across all components and pages. Maintain a clear visual hierarchy using defined heading levels (h1–h6). Use font sizes consistently throughout a website or application. Avoid mixing multiple font families unless required for a specific use case.

**Accessibility:**
Ensure color contrast and spacing meet or exceed WCAG AA requirements.

## MDWDS Components

Components are reusable UI elements that can be combined to build pages.

### Accordion (Drupal)

Accordions are a list of headings that hide or reveal additional content when selected. Use when users only need specific pieces of content or space is limited.

```html
<section class="maryland-accordion" aria-labelledby="id-rk2ic9kcwib">
  <div class="maryland-accordion__list">
    <h2 class="maryland-accordion__list--heading" id="id-rk2ic9kcwib">
      Accordion Title
    </h2>
    <p class="maryland-accordion__list--content">Accordion description text.</p>
  </div>
  <div class="maryland-accordion__items">
    <div class="maryland-accordion__item">
      <h3 class="maryland-accordion__heading">
        <button type="button" class="maryland-accordion__button" id="id-btn1" aria-expanded="true" aria-controls="id-content1">
          First Amendment
        </button>
      </h3>
      <div class="maryland-accordion__content" role="region" id="id-content1" aria-labelledby="id-btn1">
        <div class="usa-prose">
          Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof...
        </div>
      </div>
    </div>
    <div class="maryland-accordion__item">
      <h3 class="maryland-accordion__heading">
        <button type="button" class="maryland-accordion__button" id="id-btn2" aria-expanded="false" aria-controls="id-content2">
          Second Amendment
        </button>
      </h3>
      <div class="maryland-accordion__content" role="region" id="id-content2" hidden="" aria-labelledby="id-btn2">
        <div class="usa-prose">
          A well regulated Militia, being necessary to the security of a free State...
        </div>
      </div>
    </div>
    <div class="maryland-accordion__item">
      <h3 class="maryland-accordion__heading">
        <button type="button" class="maryland-accordion__button" id="id-btn3" aria-expanded="false" aria-controls="id-content3">
          Rich Text Example
        </button>
      </h3>
      <div class="maryland-accordion__content" role="region" id="id-content3" hidden="" aria-labelledby="id-btn3">
        <div class="usa-prose">
          <h4>This is a Heading 4</h4>
          <p>
            This paragraph contains <strong>bold text</strong> and <em>italic text</em> to demonstrate editor formatting capabilities. You can also combine <strong><em>bold and italic together</em></strong>.
          </p>
        </div>
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
- **When to use:** If users will only need a few specific pieces of content within a page, or if you have only a small space to display a lot of content.
- **When to use something else:** If most of the page should be visible, use clear, well-formatted text instead. If there isn't much content, skip accordions as they add unnecessary clicks.
- **How to use:** Include the CSS as outlined in the developer quickstart. Use controls to customize. Copy the HTML output from "show code".

**Accessibility:**
Uses `aria-expanded` and `aria-controls` on buttons, and `aria-labelledby` on content regions. Headings (h2, h3) provide document structure.

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
- Featured Actions — A straightforward list of tasks or links.
- Action Spotlight — A prominent section with a heading, description, and a specific call-to-action button or list of guides.
- Action Group — A collection of actions under a shared heading and optional description. Each item includes a title, subtitle, description, and CTA link.
- Action Hero — Action items integrated into the top Hero section of a page, following breadcrumbs and the page title.
- Action Page Contents — A complex layout incorporating section menus, spotlights, action groups, and "Keep learning" sections.

**Usage Notes:**
Used to guide users through specific processes or provide quick access to resources.

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
- info, warning, success, error, emergency
- slim (removes the heading)
- noIcon (hides the icon)

**Usage Notes:**
Use for important information. HTML is allowed in message content (should be escaped or sanitized). The `status` property controls the visual style. The `slim` variant removes the heading by default. Icons can be toggled off with `noIcon`.

**Accessibility:**
Supports ARIA roles (`role="status"`), live region updates, `aria-labelledby`, and `aria-describedby` for screen readers.

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
          <div class="maryland-card__header"><h3 class="maryland-card__heading">Card Title</h3></div>
          <div class="maryland-card__body"><p>Card description...</p></div>
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
- `maryland-automatic-list`
- `maryland-automatic-list__header`
- `maryland-automatic-list__header-content`
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
Uses `aria-labelledby` for the section title. Cards use `aria-label` for descriptive link text.

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
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <a class="usa-breadcrumb__link maryland-breadcrumb__link" href="/level2"><span>Link Level 2</span></a>
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
- `maryland-breadcrumb__wrapper--light` / `maryland-breadcrumb__wrapper--dark`
- `usa-breadcrumb` / `maryland-breadcrumb`
- `maryland-breadcrumb--light` / `maryland-breadcrumb--dark`
- `usa-breadcrumb__list` / `maryland-breadcrumb__list`
- `usa-breadcrumb__list-item` / `maryland-breadcrumb__list-item`
- `usa-breadcrumb__link` / `maryland-breadcrumb__link`
- `usa-current`

**Variants:**
- **Light (Default):** White background with dark gray text.
- **Dark:** Blue background (`blue-60v`) with white text. Typically used within the Hero component.

**Usage Notes:**
Pass an array of page strings or objects with `label` and `href` properties. The last item in the array is automatically marked as the current page (not linked). Supports wrapping (`wrapping` boolean) and RDFa metadata (`rdfa` boolean).

**Accessibility:**
Uses `aria-label="Breadcrumbs"` on `<nav>` and `aria-current="page"` on the current page item. Current page is rendered as plain text, not a link.

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
Use to highlight important info. Title and image are optional. Description is required. The title can be visually hidden while remaining accessible. Image alt text can be left empty for decorative images.

**Accessibility:**
Uses `aria-labelledby` to associate the section with the title. The title can be visually hidden while remaining accessible to screen readers using the `hideTitle` control.

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
- `maryland-card__media`
- `maryland-card__img`
- `maryland-card__footer`
- `maryland-card__footer--left` / `maryland-card__footer--center` / `maryland-card__footer--right`
- `maryland-card__footer-content`
- `maryland-card__link` (for linked cards)
- `maryland-card__icon` / `maryland-card__icon--arrow`

**Variants:**
- **Simple (Default):** Basic container for a title, body text, and a "More Link."
- **Media Card:** Includes an image placeholder along with the title, body, and link.
- **Flag Card:** Features media alongside text content in a horizontal layout.
- **Linked Card:** The entire card is clickable as one large link. Link lists are not available due to accessibility constraints (to avoid nested links).
- **Full Card:** Comprehensive variant with subheadings, link lists, analytics tracking, custom footer alignment, media placement options, and additional links.

**Configuration Properties:**
- `variant`: simple, media, flag, linked
- `title`: Card heading text
- `body`: Main content text
- `buttonText`: Label for the CTA button/link
- `buttonUrl`: Destination URL for the button
- `footerAlignment`: left, center, right
- `enableAnalytics`: Boolean for GA tracking
- `gaCategory` / `gaAction` / `gaLabel`: Google Analytics event attributes

**Usage Notes:**
Cards manage their own block-spacing. A `.block-spacing` utility class is available. Images and links in examples use placeholders.

**Accessibility:**
Ensure heading levels follow a logical hierarchy within the card and the page.

### Footer

The Footer component provides a consistent global or agency-specific footer for Maryland state websites, including links to services, government information, policies, and contact details.

```html
<!-- The Footer component uses Maryland-specific classes for structure. -->
<!-- Below is the general structural pattern: -->
<footer class="maryland-footer">
  <div class="maryland-footer__container">
    <div class="maryland-footer__section">
      <h2 class="maryland-footer__title">Explore Maryland.gov</h2>
      <div class="maryland-footer__content">
        <div class="maryland-footer__link-group">
          <h3 class="maryland-footer__link-group-heading">Top services</h3>
          <ul class="maryland-footer__link-group-list">
            <li><a href="#">Vehicle services</a></li>
            <li><a href="#">Food assistance / SNAP</a></li>
            <!-- Additional links -->
          </ul>
        </div>
        <!-- Additional link groups: Government, Policies, Connect, Alerts -->
      </div>
    </div>
  </div>
</footer>
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
- **Global:** Standardized Maryland.gov links and branding.
- **Agency:** Agency-specific contact info, social media links, and link groups.
- **Full:** Combines Agency and Global footer sections.

**Footer Content Sections:**
- **Top Services:** Vehicle services, Food assistance / SNAP, Unemployment services, Taxes, Register to vote, Resident resources, Visit Maryland, More online services.
- **Government:** Governor, Maryland cabinet agencies, All state agencies, For state employees, Maryland state jobs, Report state government fraud.
- **Policies:** Accessibility, Privacy & security.
- **Connect:** Maryland Relay: 7-1-1, State employee directory, Maryland news, Customer service survey.
- **Alerts:** Emergency alerts, Travel alerts, Cybersecurity, Report human trafficking.

**Usage Notes:**
Each component manages its own block-spacing. A `.block-spacing` class is available for use with components on the page.

**Accessibility:**
Uses `aria-labelledby` for sections and navigation groups. Includes a screen-reader-only heading for the footer.

### Header (Drupal)

A header helps users identify where they are and provides a quick, organized way to reach the main sections of a website. Includes agency title, utility menu, primary navigation, and search.

```html
<!-- The Header is a complex composite component. Its general structure: -->
<header class="maryland-header">
  <!-- Utility Navigation -->
  <div class="maryland-header__util-nav-container">
    <ul class="maryland-header__util-nav">
      <li><a href="#">Link One</a></li>
      <li><a href="#">Link Two</a></li>
      <li><a class="usa-button usa-button--small" href="#">Button</a></li>
    </ul>
  </div>
  <!-- Logo / Home Link -->
  <div class="maryland-header__home">
    <a class="maryland-header__logo" href="/">
      <img src="md_wordmark_horizontal.svg" alt="Agency Title" />
    </a>
  </div>
  <!-- Search -->
  <div class="maryland-search-form maryland-search-form--toggleable">
    <form class="maryland-search-form__form" role="search" action="#">
      <label class="usa-sr-only" for="search-input">Search</label>
      <div class="maryland-search-form__widget">
        <input class="maryland-search-form__input" type="text" name="q" autocomplete="on" id="search-input" />
        <button type="submit" aria-label="Submit Search" class="maryland-search-form__submit"></button>
      </div>
    </form>
    <a href="#!" class="maryland-search-form__toggle" aria-label="Site search"></a>
  </div>
  <!-- Primary Navigation -->
  <nav class="maryland-nav" aria-label="Primary navigation">
    <!-- Navigation items -->
  </nav>
</header>
```

**CSS Classes:**
- `maryland-header`
- `maryland-header__util-nav-container`
- `maryland-header__util-nav`
- `maryland-header__home`
- `maryland-header__logo`
- `maryland-search-form`
- `maryland-search-form--toggleable`
- `maryland-nav`

**Internal Structure:**
- **Agency Title:** The name of the agency, displayed as logo/wordmark.
- **Utility Menu:** Optional secondary navigation at the top of the header.
- **Primary Navigation:** Main navigation items with dropdown/mega-menu support.
- **Search:** Toggleable search interface.
- **Maryland.gov Link:** Optional link at the bottom of mobile navigation.

**Variants:**
- Default

**Usage Notes:**
The Header component includes an optional utility menu, primary navigation, and search interface. It also features the Maryland wordmark. The utility menu can be enabled/disabled. The primary navigation can be enabled/disabled. An optional Maryland.gov link can be shown at the bottom of mobile navigation.

**Accessibility:**
Includes skip-to-main-content links and `aria-labels` for navigation toggles.

### Hero

The Hero component is designed for landing and detail pages, featuring various layouts ranging from full-width landscape backgrounds to structured cards with metadata.

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
- `maryland-hero--landing-agency`
- `maryland-hero--landing-regular`
- `maryland-hero--basic`
- `maryland-hero--news`
- `maryland-hero--location`
- `maryland-hero__background-image`
- `maryland-hero__container`
- `maryland-hero__content`
- `maryland-hero__title`
- `maryland-hero__eyebrow`
- `maryland-hero__title-text`

**Variants:**
- **Landing Main:** Full-width background image (gradients must be baked into the image). Titles starting with "Welcome to " auto-detect and style the prefix as eyebrow text. Use for: Maryland.gov homepage.
- **Landing Agency:** Supports agency logos, titles, descriptions, and buttons. Does not use breadcrumbs. White background/dark text. Four layout combinations: with/without image, with/without logo. Use for: Agency-specific landing pages.
- **Landing Regular:** Includes breadcrumb navigation, title, description, and optional images with a diamond pattern illustration. White background/dark text. Two-column layout when an image is present (33:35 aspect ratio). Use for: General non-home landing pages.
- **Basic:** Blue background with a flag illustration and breadcrumb navigation. Desktop layout places images on the right (3:4 aspect ratio); mobile stacks image above content. Use for: Standard internal pages.
- **News:** Blue background with flag illustration. Includes breadcrumbs, news type (displayed in uppercase), and published date. Does not support images. Use for: Press releases and announcements.
- **Location:** Features a white card containing an image and address that overlaps a blue background with a reversed diamond pattern. Grid-aligned layout matching a two-column structure. Use for: Office or location detail pages.

**Usage Notes:**
Ideal for Maryland.gov homepage (Landing Main). Background image should have gradient layers merged into the image asset, not applied via CSS.

**Accessibility:**
Uses `aria-labelledby` to associate the section with the hero title.

### Highlight

The Highlight component displays up to 3 columns of featured links with a header with optional visibility and optional description.

```html
<section class="maryland-highlight" aria-labelledby="id-7cyg9t97sg3">
  <h2 class="maryland-highlight__section-title" id="id-7cyg9t97sg3">Benefits, services and business</h2>
  <p class="maryland-highlight__section-description">Find the right information you need today in these featured areas.</p>
  <div class="maryland-highlight__grid">
    <div class="maryland-highlight__item">
      <h3 class="maryland-highlight__title">Benefits</h3>
      <ul class="maryland-highlight__links">
        <li class="maryland-highlight__link">
          <a href="javascript:void(0)">
            <span class="maryland-highlight__link-text">Health and medical</span>
            <span aria-hidden="true" class="maryland-highlight__link-icon"></span>
          </a>
        </li>
        <!-- Up to 5 links per column -->
      </ul>
      <a class="maryland-highlight__more-link" href="javascript:void(0)">More benefits</a>
    </div>
    <!-- Up to 3 columns total -->
  </div>
</section>
```

**CSS Classes:**
- `maryland-highlight`
- `maryland-highlight__section-title`
- `maryland-highlight__section-description`
- `maryland-highlight__grid`
- `maryland-highlight__item`
- `maryland-highlight__title`
- `maryland-highlight__links`
- `maryland-highlight__link`
- `maryland-highlight__link-text`
- `maryland-highlight__link-icon`
- `maryland-highlight__more-link`

**Variants:**
- Default
- With Sidebar

**Usage Notes:**
Displays up to 3 columns of featured links. Each column can contain a title, description, up to 5 links (each with text, URL, and icon type), and an optional "more" link.

**Accessibility:**
Uses `aria-labelledby` for the section title. Decorative icons use `aria-hidden="true"`.

### LinkCollection (Drupal)

Use a link collection to present a curated list of related links with an optional description and call-to-action.

```html
<section class="maryland-link-collection">
  <div class="maryland-link-collection__container">
    <div class="maryland-link-collection__header">
      <h2 class="maryland-link-collection__title">Collection Title</h2>
      <p class="maryland-link-collection__description">A brief description providing context for the links.</p>
    </div>
    <ul class="maryland-link-collection__list">
      <li class="maryland-link-collection__item">
        <a class="maryland-link-collection__link" href="#">Link Title One</a>
        <p>Optional description for this link.</p>
      </li>
      <li class="maryland-link-collection__item">
        <a class="maryland-link-collection__link" href="#">Link Title Two</a>
      </li>
    </ul>
    <a class="maryland-link" href="#">More in business and work</a>
  </div>
</section>
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
- **Default:** A list of links with a title, description, and "More" link.
- **With Item Descriptions:** Each link in the collection includes its own descriptive text.
- **Without More Link:** A collection of links without the bottom call-to-action.
- **Mixed Descriptions:** A collection where some links have descriptions and others do not.
- **Stacked:** Multiple link collections placed sequentially on a page.

**Component Properties:**
- **Title (Required):** A clear, concise, and descriptive title relevant to the content.
- **Description (Optional):** A brief message that provides context for the links.
- **More Link Text (Optional):** Text for the call-to-action link (e.g., "More in business and work").
- **More Link URL (Optional):** Destination URL for the "More Link."
- **Links:** An array of link items, each with a Title, URL, and optional Description.

**Usage Notes:**
Use for curated lists of related links. Title is required, description and more-link are optional.

**Accessibility:**
Ensure links have descriptive text. External links should have appropriate `aria-labels`.

### Links (Drupal)

Maryland Design System links provide enhanced styling and accessibility features for various link types. They handle standard navigation, file downloads, external site redirection, and accessibility shortcuts.

**Default Link:**
```html
<a class="maryland-link" href="#">Maryland Link</a>
```

**Document Link** — for downloadable files, displays file type and size inline:
```html
<a class="maryland-link maryland-link--document" href="#document">
  Maryland 2019 state constitution - PDF 2MB
</a>
```

**Labelled Link** — displays a descriptive label above the link text:
```html
<div class="maryland-link--labelled">
  <span class="maryland-link__label" id="id-yx55cc8o7e">Download</span>
  <a class="maryland-link" href="#pdf" aria-describedby="id-yx55cc8o7e">
    PDF Documentation
  </a>
</div>
```

**External Link** — navigates away from the current site, opens in a new tab:
```html
<a class="maryland-link maryland-link--external" href="https://example.com" rel="noreferrer" aria-label="External Website (external link)">
  External Website
  <span class="maryland-link__icon" aria-hidden="true"></span>
</a>
```

**Skip Link** — accessibility link for keyboard users to bypass navigation:
```html
<a class="usa-skipnav maryland-link maryland-link--skipnav" href="#main-content">
  Skip to main content
</a>
```

**Skip Link Sidebar** — variant placed at the top of sidebar navigation:
```html
<a class="usa-skipnav maryland-link maryland-link--skipnav" href="#main-content">
  Skip sidebar navigation
</a>
```

**CSS Classes:**
- `maryland-link`
- `maryland-link--document`
- `maryland-link--labelled`
- `maryland-link--external`
- `maryland-link--skipnav`
- `maryland-link__label`
- `maryland-link__icon`
- `usa-skipnav`

**Variants:**
- Default
- Document Link
- Labelled Link
- External Link
- Skip Link
- Skip Link Sidebar

**Usage Notes:**
- **Default Links:** Standard links with Maryland styling.
- **Document Links:** For downloadable files in body content. Display file information (type and size) inline.
- **Labelled Links:** Display a descriptive label above the link text. The label is connected via `aria-describedby`.
- **External Links:** Open in a new tab with `rel="noreferrer"` and an external link icon.
- **Skip Links:** Hidden until they receive keyboard focus. Essential for accessibility.

**Accessibility:**
Includes skip links for keyboard navigation, `aria-describedby` for labelled links, `aria-label` for external links, and `aria-hidden="true"` on decorative icons.

### Listing Page

Listing page components are used to display grouped items such as services, resources, or agency listings, often including filtering and pagination.

```html
<!-- Listing page structure (representative, not a literal code block from docs) -->
<section class="maryland-listing-page">
  <!-- Introductory Content -->
  <div class="maryland-listing-page__body">
    <p>Introductory text above the filters (supports basic HTML).</p>
  </div>

  <!-- Filters -->
  <div class="maryland-listing-page__filters">
    <input type="text" placeholder="Filter text" />
    <select><option>Category</option></select>
    <button>Filter</button>
  </div>

  <!-- Results Metadata -->
  <div class="maryland-listing-page__results-count">Showing 1-25 of 315 results</div>

  <!-- Listing Items -->
  <ul class="maryland-listing-page__items">
    <li class="maryland-listing-item">
      <img src="..." alt="..." />
      <span class="maryland-listing-item__eyebrow">Category</span>
      <h2 class="maryland-listing-item__title"><a href="#">Item Title</a></h2>
      <time class="maryland-listing-item__date">January 15, 2026</time>
      <p class="maryland-listing-item__description">Brief description...</p>
    </li>
  </ul>

  <!-- Pagination -->
  <nav aria-label="Pagination">
    <a href="#">Previous</a>
    <a href="#">1</a>
    <a href="#">2</a>
    <a href="#">Next</a>
  </nav>
</section>
```

**CSS Classes:**
- `maryland-listing-page`
- `maryland-listing-item`

**Component Properties:**
- **custom:** Boolean toggle for custom content.
- **Content type:** Controls page titles and listing item data (options: contact, location, event, news, document).
- **Body:** Introductory text displayed above filters (supports basic HTML).
- **eyebrow:** Category label above the title.
- **title:** The title of the listing item.
- **subtitle:** Subtitle displayed below the title.
- **link:** URL for the title link.
- **date:** Date displayed above the title.
- **description:** Brief description (supports HTML paragraphs and lists).
- **imageUrl:** URL for the item's image.
- **imageSize:** Size of the image (`small` or `default`).
- **linkType:** Type of link (`download` or `external`).

**Variants:**
- Listing Results
- Listing Item

**Usage Notes:**
Supports introductory body text, filtering by type/category, and pagination. Configurable item media and metadata. Results metadata shows the range of results being viewed.

**Accessibility:**
Includes skip links and ARIA labels for pagination and filters.

### Navigation

The navigation component provides a primary way for users to move through a site, including search and nested menu items.

```html
<!-- The Navigation component is a complex mega-menu structure. -->
<nav class="maryland-nav" aria-label="Primary navigation">
  <ul class="maryland-nav__items">
    <li><a href="#">Link</a></li>
    <li>
      <button class="maryland-nav__toggle" aria-expanded="false">Benefits</button>
      <!-- Dropdown with sub-categories: Health and medical, Housing and property, 
           Unemployment, Food and nutrition, etc. -->
      <!-- Includes a "See all benefits topics" link -->
    </li>
    <li>
      <button class="maryland-nav__toggle" aria-expanded="false">Services</button>
      <!-- Dropdown with: Driving and transportation, Public safety, Education, etc. -->
    </li>
    <li>
      <button class="maryland-nav__toggle" aria-expanded="false">Business and Work</button>
      <!-- Dropdown with: Professional licenses, Workers' rights, 
           Doing business in Maryland, etc. -->
    </li>
    <li>
      <button class="maryland-nav__toggle" aria-expanded="false">Visit and Explore</button>
      <!-- Dropdown with: Explore Maryland, Move to Maryland -->
    </li>
    <li>
      <button class="maryland-nav__toggle" aria-expanded="false">Your Government</button>
      <!-- Dropdown with: State agencies, Elections and voting, Press releases, etc. -->
    </li>
  </ul>
</nav>
```

**CSS Classes:**
- `maryland-nav`
- `maryland-nav__items`
- `maryland-nav__toggle`
- `maryland-search-form`

**Properties:**
- `items`: Array of navigation items.
- `showMarylandGovLink`: Boolean; shows Maryland.gov link at the bottom of mobile navigation.

**Variants:**
- Default

**Usage Notes:**
Includes search and multi-level navigation items. Mobile navigation features "Back" functionality for nested menus.

**Accessibility:**
Uses `aria-label` for navigation toggle and search labels. Uses `aria-expanded` on dropdown toggle buttons.

### Promo (Drupal)

Use a promo to visually highlight a single call-to-action link. Variants include Plain, Image, and Illustration.

```html
<section class="maryland-promo maryland-promo--plain" aria-labelledby="id-onu840emoim">
  <div class="maryland-promo__container">
    <div class="maryland-promo__row">
      <div class="maryland-promo__title-container">
        <h2 class="maryland-promo__title" id="id-onu840emoim">Your voice, your state: building a better tomorrow</h2>
      </div>
      <div class="maryland-promo__content-container">
        <div class="maryland-promo__description">We're committed to serving you...</div>
        <div class="maryland-promo__link"><a href="#">Share your feedback</a></div>
      </div>
    </div>
  </div>
</section>
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
- **Default:** Standard promo layout.
- **Contained:** A contained variant of the promo.
- **Stacked:** A stacked layout variant.
- **Plain Promo:** A version without images or illustrations.
- **Image Promo:** Includes a single image (e.g., 510x680). A multiple-image variant includes a slideshow/toggle.
- **Illustration Promo:** Includes a background illustration.

**Component Properties:**
- **Title (Required):** Clear, concise, descriptive, and relevant title.
- **Description (Optional):** Brief message providing information or context.
- **Link Title (Required):** Call-to-action link title using an active verb.
- **Link URL (Required):** Destination URL for the call to action.
- **Promo Style:** "No image," "With image," or "With background illustration."

**Usage Notes:**
Use for single call-to-action links. Title, Link Title, and Link URL are required.

**Accessibility:**
The section uses `aria-labelledby` to associate the title with the promo container.

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
- `maryland-search-form` — The main container for the search component.
- `maryland-search-form--toggleable` — Modifier for a search form that can be toggled open/closed.
- `maryland-search-form__form` — The internal form element.
- `maryland-search-form__widget` — Container for the input and submit button.
- `maryland-search-form__input` — The text input field for the search query.
- `maryland-search-form__submit` — The button used to submit the search.
- `maryland-search-form__toggle` — The anchor/button used to trigger the visibility of the search form.
- `usa-sr-only` — Utility class for screen-reader-only content (used on the label).

**Variants:**
- **Pop Out:** A toggleable search interface.
- **Static:** A fixed search bar.
- **Hero:** A prominent search feature typically used in header or landing areas.
- **Results:** A layout for displaying search results, including sorting options (Relevance, Date) and result counts.

**Component Properties:**
- **keywords (string):** Search terms (e.g., "Maryland").
- **scope (string):** Defines the scope of the search.
- **Title (string):** Required. Clear, concise, descriptive, and relevant.
- **Description (string):** Optional. Brief message providing context.

**Usage Notes:**
The Search component manages search functionality and layout across multiple variant contexts.

**Accessibility:**
Uses `aria-label` for search toggle and submit button. Includes a screen-reader-only label (`usa-sr-only`) for the search input.

### Side Navigation

Hierarchical, vertical navigation to place at the side of a page.

```html
<!-- Side Navigation follows the USWDS sidenav pattern with Maryland styling. -->
<nav aria-label="Section navigation">
  <ul class="usa-sidenav">
    <li class="usa-sidenav__item">
      <a href="#">Your government</a>
      <ul class="usa-sidenav__sublist">
        <li class="usa-sidenav__item"><a href="#">State government</a></li>
        <li class="usa-sidenav__item"><a href="#">Elections and voting</a></li>
        <li class="usa-sidenav__item"><a href="#">State agencies and departments</a></li>
        <li class="usa-sidenav__item"><a href="#">State goals and initiatives</a></li>
        <li class="usa-sidenav__item"><a href="#">State holidays</a></li>
        <li class="usa-sidenav__item"><a href="#">Emergency closings</a></li>
        <li class="usa-sidenav__item"><a href="#">Press releases</a></li>
        <li class="usa-sidenav__item"><a href="#">Public records</a></li>
        <li class="usa-sidenav__item"><a href="#">Share your feedback</a></li>
        <li class="usa-sidenav__item"><a href="#">Federal representatives</a></li>
      </ul>
    </li>
  </ul>
</nav>
```

**CSS Classes:**
- `usa-sidenav`
- `usa-sidenav__item`
- `usa-sidenav__sublist`

**Variants:**
- Default
- In Sidebar

**Usage Notes:**
Used for hierarchical, vertical navigation placed at the side of a page. Typically used within a "Section menu" context.

**Accessibility:**
Ensure proper heading levels and link descriptions are used within the navigation structure. Use `aria-label` on the `<nav>` element.

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

**CSS Classes (noscript fallback):**
- `maryland-alert`
- `maryland-alert--warning`
- `maryland-alert__body`
- `maryland-alert__heading`
- `maryland-alert__text`

**Custom Element:**
- `<maryland-statewide-banner>`

**Variants:**
- Default

**Usage Notes:**
- **What is it?** The Banner tells people that the site (or application) is a secure and official Maryland government site. It displays key information without being visually distracting.
- **When to use it?** Required on all pages of a website or application. Positioned at the top of all pages.
- Uses a custom element and a script module from the CDN. Include the `<noscript>` fallback with a warning alert if JavaScript is disabled.

**Accessibility:**
Includes a `<noscript>` fallback with a warning alert if JavaScript is disabled.

### Statewide Footer

A standardized footer component for Maryland.gov websites, providing consistent navigation and branding via a CDN-hosted custom element.

```html
<script type="module" src="https://cdn.maryland.gov/mdwds/latest/components/maryland-statewide-footer.js"></script>
<maryland-statewide-footer></maryland-statewide-footer>
```

**Custom Element:**
- `<maryland-statewide-footer>`

**Key Features:**
- Responsive layout with mobile-first design.
- Structured links to Maryland state services, government portals, privacy policies, emergency alerts and notifications.
- Zero configuration required — plug-and-play with built-in styles.

**Customization Guidance:**
This component is intended to be non-editable in most use cases. If you need to override layout or behavior (e.g., embedding it inside other components), it is recommended to do so only through scoped CSS or by submitting a feature request.

**Usage Notes:**
Recommended for use via CDN to ensure latest updates. Using the CDN ensures downstream applications stay up to date with the latest layout, links, and accessibility improvements without requiring manual deployments.

**Accessibility:**
Reinforces public trust and aligns with Maryland's digital service standards and USWDS.

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
Use for highlighting key information, action items, or warnings that users should not miss. Items can contain HTML including links.

**Accessibility:**
Uses `role="region"` and `aria-labelledby` to provide context to screen readers.

### Table of Contents (Drupal)

Use a table of contents to provide in-page navigation to the various sections of the page.

```html
<!-- The Table of Contents component uses Maryland-specific classes and 
     follows a sidenav pattern for in-page navigation. -->
<nav class="maryland-toc" aria-labelledby="toc-heading">
  <h2 id="toc-heading">On this page</h2>
  <ul class="maryland-sidenav">
    <li><a href="#section-1">Section #1</a></li>
    <li><a href="#section-2">Section #2</a></li>
    <li><a href="#section-3">Section #3</a></li>
  </ul>
</nav>
```

**CSS Classes:**
- `maryland-toc`
- `maryland-sidenav`

**Variants:**
- Default

**Usage Notes:**
Provides in-page navigation. Often used with a sidebar layout. The component displays a list of links to specific sections on the current page.

**Accessibility:**
Uses `<nav>` element with `aria-labelledby`. Buttons for toggles where applicable.

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

**Item Types:**
- **Plain link:** `{ label: "Text", url: "#" }`
- **Button-styled link:** `{ label: "Text", url: "#", isButton: true }`
- **Button (no link):** `{ label: "Text", isButton: true }` (contains no `url` property)

**Properties:**
- `enableUtil`: Boolean to enable or disable the utility navigation.
- `util`: An array of navigation items (labels, URLs, and button states).

**Variants:**
- Desktop (top of header)
- Mobile (integrated into mobile menu)

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

**Component Properties:**
- **Title (Required):** A clear, concise, and descriptive title.
- **Visually Hide Title:** Option to hide the title visually while keeping it accessible to screen readers.
- **Description (Optional):** Brief message providing context for the CTA link.
- **Video:** An iFrame embed code for a YouTube or Vimeo video player.
- **Caption:** Descriptive caption below the video player.
- **Link Text:** Text for the optional CTA link.
- **Link URL:** Destination URL for the CTA link.

**Usage Notes:**
Use to visually highlight a single call-to-action link alongside video content. Requires a title. Description and link are optional. Layout can be adjusted via properties.

**Accessibility:**
The title is used as the `aria-label` for the section. Title can be visually hidden while remaining accessible to screen readers.

### Visual Link Collection (Drupal)

A collection of visual links or cards used to highlight specific content or services. Displays a group of related links with visual emphasis using linked cards.

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
- `maryland-visual-link-collection__header-content`
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
Used to display a group of related links with visual emphasis using cards. Ideal for visual navigation to key sections or updates.

**Accessibility:**
Uses `aria-labelledby` for the section and `aria-hidden="true"` for decorative icons.

## Templates

Templates are pre-built page layouts combining multiple components.

### Maryland Homepage

The primary landing page for the State of Maryland, featuring a statewide banner, header with search, mega-menu navigation, hero section, and comprehensive footer.

**Page Structure:**
1. **Statewide Banner** — Official "Maryland.gov" verification.
2. **Header** — Horizontal Maryland wordmark logo and search interface.
3. **Navigation** — Mega-menu with: Benefits, Services, Business and Work, Visit and Explore, Your Government.
4. **Hero Section** — Large visual (e.g., forest imagery) with "Welcome to Maryland" heading.
5. **Footer Section** — Explore Maryland.gov / Top Services, Government, Policies, Connect, Alerts.
6. **Statewide Footer** — Inverted Maryland wordmark and copyright notice.

**Semantic Flow:**
```
Statewide Banner → Header → Navigation → Hero → Content → Footer → Statewide Footer
```

**Usage Notes:**
High-level landing page for state-level information and services.

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
  <!-- Breadcrumb Component (e.g., Home > Benefits > Food and nutrition) -->
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
  <!-- Agency Footer Section (social icons, contact details, agency link groups) -->
  <!-- Statewide Footer Section (Top Services, Government, Policies, Connect, Alerts) -->
</footer>
```

**Components Used:**
Statewide Banner, Header, Utility Nav, Navigation, Breadcrumb, Side Navigation, Action Items, Agency Footer, Statewide Footer.

**Usage Notes:**
Used for pages where the primary goal is for the user to take specific actions or find specific resources. Includes a section menu for deep navigation within a department.

### Landing Page

A template for agency landing pages, featuring a hero section with call-to-action buttons, navigation, and various content blocks.

**Page Structure:**
1. **Statewide Banner** — Official "Maryland.gov" identification.
2. **Header** — Agency Title, Search, Utility links.
3. **Main Navigation** — Horizontal menu with dropdown/mega-menu.
4. **Breadcrumbs** — Navigation path.
5. **Hero Section** — H1 title, summary text, Primary and Secondary CTA buttons, featured image (510x540).
6. **Main Content** — Side Navigation ("Section menu") and Body Content.
7. **Agency Footer** — Agency contact info, social media links, link groups.
8. **Statewide Footer** — Standardized Maryland.gov links and copyright.

**Components Used:**
Statewide Banner, Header, Navigation, Breadcrumbs, Hero (Landing Regular or Landing Agency variant), Side Navigation, Footer (Agency + Statewide).

**Usage Notes:**
Used for agency-level landing pages. Features a hero section with CTA buttons and a sidebar for sub-page navigation.

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

**Components Used:**
Statewide Banner, Header, Navigation, Breadcrumb, Side Navigation, Search/Filter Bar, Listing Items, Pagination, Agency Footer, Statewide Footer.

**Usage Notes:**
Designed to display a collection of related items (such as contacts, news, or services) with filtering and pagination capabilities. Uses a two-column layout (Sidebar + Content).

### Location Page

A template for displaying specific location information, including address, office hours, and contact details.

**Page Structure:**
1. **Statewide Banner** — Official identification.
2. **Header** — Agency Title and Search.
3. **Navigation** — Primary site navigation.
4. **Breadcrumb** — e.g., Home > Locations > Location name.
5. **Hero/Location Header** — Location Name (`<h1>`) and representative image.
6. **Main Content (Two-Column):**
   - **Main Column:** Physical address and detailed descriptive text.
   - **Sidebar:** Side Navigation ("Locations" menu), Mailing Address, Office Hours (Sunday–Saturday with time zone), and Contact Information (Website, Email, Phone numbers).
7. **Agency Footer** — Social media links, agency contact info, internal agency links.
8. **Statewide Footer** — Global Maryland.gov links.

**Components Used:**
Statewide Banner, Header, Navigation, Breadcrumb, Hero (Location variant), Side Navigation, Location Details (Address, Hours, Contact), Agency Footer, Statewide Footer.

**Usage Notes:**
Used for agency locations or service centers. Features a two-column layout with location metadata in the sidebar.

## Utilities

Utility classes for common styling needs.

### Layout Grid

A responsive 12-column layout system based on Flexbox, designed for flexible and consistent page structures. It mirrors the principles of the U.S. Web Design System (USWDS) and supports fixed-width, auto-layout, fill, and offset column behaviors.

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
- **Container:** `grid-container`
- **Row:** `grid-row`
- **Column Variants:**
  - Numeric Width: `grid-col-[1-12]` (e.g., `grid-col-4`, `grid-col-6`, `grid-col-8`)
  - Auto/Fill: `grid-col-auto`, `grid-col-fill`
  - Responsive: `[breakpoint]:grid-col-[n]` (e.g., `tablet:grid-col-4`)
- **Gutters:** Default (normal), `grid-gap-sm` (small), `grid-gap-lg` (large)

**Use When:**
- Laying out content in columns that must adapt to different screen sizes.
- Seeking consistent spacing, alignment, and responsive design without custom CSS.
- Building interfaces with equal-width, fixed-width, or auto-sized content blocks.

**Best Practices:**
- Use `.grid-container` to constrain the grid within page margins.
- Use `.grid-row` for each row.
- Place columns inside rows using combinations such as `.grid-col-6` for fixed-width, `tablet:grid-col-4` for responsive width, or `.grid-col-auto` and `.grid-col-fill` for flexible layouts.
- Combine with utility classes like `padding-2`, `margin-top-2`, `text-center`, and `bg-base-lightest`.

**Accessibility:**
Grids are visual constructs; use appropriate heading levels and landmarks inside the grid. Ensure visual grouping is conveyed semantically.

**Testing:**
Verify behavior on multiple screen sizes, ensure consistent spacing/alignment, and check that the grid does not break when content wraps or expands.

## Best Practices

1. **Always use the CDN** — Use the official Maryland CDN for CSS and JS files.
2. **Version pinning** — Pin to a specific version to avoid breaking changes.
3. **Semantic HTML** — Use appropriate HTML5 semantic elements.
4. **Accessibility** — Follow WCAG 2.1 AA guidelines.
5. **Mobile-first** — MDWDS is designed mobile-first; test on all screen sizes.
6. **Component composition** — Combine components as documented; avoid custom overrides.
7. **Block spacing** — Use the `.block-spacing` class to manage spacing between component blocks.
8. **Typography** — Use Source Sans Pro Web as the primary font; set a 16px base font size and scale with relative units.
9. **Color contrast** — Ensure sufficient contrast when combining text and background color utilities.
10. **Logo integrity** — Never distort, outline, recolor, or manipulate the Maryland logo.
