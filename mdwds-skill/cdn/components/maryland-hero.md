# maryland-hero

Maryland Design System heroes sit at the top of every Maryland.gov page, immediately below the header. They carry the page's `<h1>`, optional breadcrumb, description, and primary call-to-action buttons. Heroes are the single biggest visual element on the page and the only place an `<h1>` belongs.

> **There is one hero component — `maryland-hero`. It has multiple variants for different page types (landing, agency landing, basic interior page, news, event, location). Pick the variant that matches the page type rather than mixing hero-style markup from other sources.** The Storybook stories list seven variants; the four most common are documented in depth below (`landing-main`, `landing-agency`, `landing-regular`, `basic`), with shorter notes on `news`, `event`, and `location`.

## What it looks like

Every hero is a `<section>` with `aria-labelledby` pointing at the inner `<h1>` (`maryland-hero__title`). Inside the section, a `maryland-hero__container` wraps the variant-specific content. Heroes never use the standard `block-spacing` rhythm of the rest of the page — they manage their own top/bottom margins.

Two big stylistic families:

- **Dark heroes (`basic`, `news`, `event`):** Maryland blue background (`primary` color, ~#1A4480), white text. Title is Merriweather light at 32px (mobile) / 40px (mobile-lg) / 48px (desktop), 1.4 line-height. A horizontally-flipped Maryland flag illustration sits at the bottom-right of the section at 75% opacity. The hero is constrained to 1288px max-width and sits inset from the page edges by 56px on tablet-lg+.
- **Light heroes (`landing-main`, `landing-agency`, `landing-regular`):** White background, dark text (`base-darkest`, near-black). Title sizes are similar to the dark variants. Light variants use either a full-bleed landscape background image (`landing-main`), a side image with a Maryland blue "diamond pattern" decoration (`landing-agency` / `landing-regular` with image), or a flag illustration on the right side (no-image variants).

Heroes responsively step from single-column at mobile to a two-column 6/6 (or 7/5) grid at `tablet-lg` (880px) when an image or logo is present. The `<h1>` is on the left and the image is on the right; on mobile they stack vertically with the image above the content (except `basic`, which positions the image absolutely so it overlaps the section above on desktop).

## Variants

| Variant | Background | Image support | Buttons | Breadcrumb | When to use |
|---|---|---|---|---|---|
| `landing-main` | Full-bleed photo (forest/farmland/bridge) | Required (background) | No | No | Maryland.gov state homepage |
| `agency-home` | Background photo + dark content card | Required (background) | Yes | No | An agency's home page |
| `landing-agency` | White, diamond-pattern accent, or agency-logo accent | Optional (side image) | Yes | No | Agency landing pages below the home |
| `landing-regular` | White, diamond-pattern accent, or flag illustration | Optional (side image) | Yes (toggle via `showButtons`) | Yes | Generic landing pages |
| `basic` | Maryland blue + flag illustration | Optional (side image, protrudes above hero) | No | Yes | Interior content pages |
| `news` | Maryland blue + flag illustration | No | No | Yes | Press releases, news articles |
| `event` | Maryland blue + flag illustration | No | One (right-aligned CTA) | Yes | Event detail pages |
| `location` | Maryland blue + reversed flag, with a white card overlapping below | Yes (inside card) | No | Yes | Office / location detail pages |

## Modifier classes

Many variants pick up additional modifier classes alongside the base variant class:

| Modifier | Applied when | Effect |
|---|---|---|
| `has-illustration` | All non-`landing-main` variants | Enables the flag-illustration background layer |
| `has-image` | `image` is set or `heroStyle === "with-image"` | Switches to two-column layout with side image |
| `no-image` | No image present | Single-column layout; for landing variants, swaps in flag illustration on the right |
| `has-logo` | `landing-agency` only, when `showLogo` and `agencyLogo` are set | Adds agency logo to layout |
| `no-description-buttons` | `landing-regular` only, when both are hidden | Reduces vertical height of the hero |
| `maryland-hero--flush` | `basic`, `news`, `location`, `event` | Removes any divider between header and hero so the dark hero sits flush against the header |

## When to use which variant

- **`landing-main`** — Reserved for the Maryland.gov state homepage. Full-width scenic photo, "Welcome to Maryland" title with the "Welcome to" auto-styled as an eyebrow.
- **`agency-home`** — An agency's home page (e.g., Department of Natural Resources home). Dark text card overlays a hero photo with configurable alignment (left/center/right).
- **`landing-agency`** — Top of an agency's secondary landing pages where the agency's logo or a feature image is the focal point. White background.
- **`landing-regular`** — Most other landing pages (sub-section overviews) on Maryland.gov. White background, optional image, optional buttons.
- **`basic`** — Interior content pages — programs, services, FAQs. Blue background. With an image, the image protrudes above the hero by 37px on tablet-lg+.
- **`news`** — Press releases, news articles, public notices. Blue, no image, includes a metadata line with news type and published date below the title.
- **`event`** — Event detail pages. Blue, includes event type + date metadata, a right-aligned CTA button (e.g., "Register today"), and an optional "Past event" yellow tag.
- **`location`** — Office or facility detail pages. The hero itself is a thin blue strip with breadcrumb and screen-reader-only title; a white card with the visible title, image, and address overlaps below.

## Heading level adjustment

`maryland-hero__title` is always `<h1>` and there is **exactly one per page**. If you find yourself wanting a second `<h1>`, you're on the wrong template — use a `<h2>` inside the page body and demote whatever competed with it.

The hero's `<h1>` becomes the implicit landmark name for the `<main>` region via `aria-labelledby`.

## Default markup — landing-main (Maryland.gov homepage)

```html
<section class="maryland-hero maryland-hero--landing-main" aria-labelledby="hero-title">
  <div class="maryland-hero__background-image">
    <img src="/img/md-forest.png" alt="" />
  </div>
  <div class="maryland-hero__container">
    <div class="grid-container">
      <div class="grid-row">
        <div class="grid-col-12">
          <div class="maryland-hero__content">
            <h1 id="hero-title" class="maryland-hero__title">
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

In hand-written markup, include both `<span>`s yourself — the inner `maryland-hero__eyebrow` carries the "Welcome to" prefix and `maryland-hero__title-text` carries the main title. Pick the background image to suit the page — the three Maryland-supplied options are `forest`, `farmland`, and `bridge` (Chesapeake Bay Bridge).

## Markup — agency-home (an agency's home page)

```html
<section class="maryland-hero maryland-hero--agency-home" aria-labelledby="hero-title">
  <div class="maryland-hero__background-image">
    <img src="/img/dnr-neighborhood.jpg" alt="" />
  </div>
  <div class="maryland-hero__container">
    <div class="maryland-hero__content maryland-hero__content--left">
      <div class="maryland-hero__agency-logo">
        <img src="/img/dnr-logo.png" alt="" />
      </div>
      <h1 id="hero-title" class="maryland-hero__title">
        <span class="maryland-hero__title-text">Protecting Maryland's land, water, and wildlife</span>
      </h1>
      <div class="maryland-hero__description">
        <p>The Department of Natural Resources stewards more than 470,000 acres of public land and 17,000 miles of waterways.</p>
      </div>
      <div class="maryland-hero__buttons">
        <a href="/parks" class="usa-button usa-button--big">Find a state park</a>
        <a href="/licenses" class="usa-button usa-button--big usa-button--outline">Get a license</a>
      </div>
    </div>
  </div>
</section>
```

`maryland-hero__content--left` / `--center` / `--right` controls horizontal alignment of the content card over the background photo. The content card is `ink` (near-black) on mobile-lg+ and uses `rgb(0, 0, 0, 0.7)` translucent overlay on mobile-lg+; on desktop it's solid `ink` and 845px wide.

## Markup — landing-agency with image (agency landing page)

```html
<section class="maryland-hero maryland-hero--landing-agency has-illustration has-image has-logo" aria-labelledby="hero-title">
  <div class="maryland-hero__container">
    <div class="maryland-hero__row">
      <div class="maryland-hero__content">
        <div class="maryland-hero__agency-logo">
          <img src="/img/mva-logo.png" alt="" />
        </div>
        <h1 id="hero-title" class="maryland-hero__title">
          Driver and vehicle services
        </h1>
        <div class="maryland-hero__description">
          <p>Renew your license, register a vehicle, or schedule a road test with the Motor Vehicle Administration.</p>
        </div>
        <div class="maryland-hero__buttons">
          <a href="#" class="usa-button usa-button--big">Renew online</a>
          <a href="#" class="usa-button usa-button--big usa-button--outline">Find a branch</a>
        </div>
      </div>
      <div class="maryland-hero__img-container">
        <figure class="maryland-hero__image">
          <img src="/img/mva-branch.jpg" alt="" />
        </figure>
      </div>
    </div>
  </div>
</section>
```

The image is **fixed-width** at each breakpoint (198px → 297px → 350px → 400px → 450px → 510px) with a 33:35 (or 17:18) aspect ratio. A Maryland-blue diamond pattern decoration sits at 10% opacity behind and to the right of the image. Logo max-height is 115px.

## Markup — landing-agency, no image, no logo (flag illustration)

```html
<section class="maryland-hero maryland-hero--landing-agency has-illustration no-image" aria-labelledby="hero-title">
  <div class="maryland-hero__container">
    <div class="maryland-hero__content">
      <h1 id="hero-title" class="maryland-hero__title">
        Maryland Department of Health
      </h1>
      <div class="maryland-hero__description">
        <p>Protecting and promoting the health and safety of every Marylander.</p>
      </div>
      <div class="maryland-hero__buttons">
        <a href="#" class="usa-button usa-button--big">Find a service</a>
      </div>
    </div>
  </div>
</section>
```

A horizontally-flipped Maryland flag illustration appears at the bottom-right at `tablet-lg+` (420–600px tall depending on breakpoint). On mobile it appears as a full-bleed flag strip at the bottom (80px on mobile, 120px on mobile-lg).

## Markup — landing-agency, no image, with logo

```html
<section class="maryland-hero maryland-hero--landing-agency has-illustration no-image has-logo" aria-labelledby="hero-title">
  <div class="maryland-hero__container">
    <div class="maryland-hero__row">
      <div class="maryland-hero__content">
        <h1 id="hero-title" class="maryland-hero__title">
          Maryland Department of Transportation
        </h1>
        <div class="maryland-hero__description">
          <p>Connecting Marylanders to the places and people that matter.</p>
        </div>
        <div class="maryland-hero__buttons">
          <a href="#" class="usa-button usa-button--big">Plan a trip</a>
        </div>
      </div>
      <div class="maryland-hero__logo-container">
        <div class="maryland-hero__agency-logo">
          <img src="/img/mdot-logo.png" alt="" />
        </div>
      </div>
    </div>
  </div>
</section>
```

Logo sits on the right side at `tablet-lg+` with a gradient background; on mobile it stacks above the title.

## Markup — landing-regular with image (generic landing page)

```html
<section class="maryland-hero maryland-hero--landing-regular has-illustration has-image" aria-labelledby="hero-title">
  <div class="maryland-hero__container">
    <div class="maryland-hero__row">
      <div class="maryland-hero__content">
        <div class="maryland-hero__breadcrumb">
          <nav class="maryland-breadcrumb maryland-breadcrumb--light" aria-label="Breadcrumb">
            <ol class="maryland-breadcrumb__list">
              <li class="maryland-breadcrumb__list-item">
                <a class="maryland-breadcrumb__link" href="/">Home</a>
              </li>
              <li class="maryland-breadcrumb__list-item">
                <a class="maryland-breadcrumb__link" aria-current="page" href="/health">Health</a>
              </li>
            </ol>
          </nav>
        </div>
        <h1 id="hero-title" class="maryland-hero__title">Public health programs</h1>
        <div class="maryland-hero__description">
          <p>Maryland offers hundreds of public health programs that may be available to you or your family.</p>
        </div>
        <div class="maryland-hero__buttons">
          <a href="#" class="usa-button usa-button--big">Find a program</a>
          <a href="#" class="usa-button usa-button--big usa-button--outline">Eligibility checker</a>
        </div>
      </div>
      <div class="maryland-hero__img-container">
        <figure class="maryland-hero__image">
          <img src="/img/health-clinic.jpg" alt="" />
        </figure>
      </div>
    </div>
  </div>
</section>
```

Notice the **breadcrumb sits inside the hero**, before the `<h1>`. It uses the **light** variant of `maryland-breadcrumb` because the hero background is white. The hero has a thin light-gray (`gray-cool-40`) bottom border below the content at `tablet-lg+`.

## Markup — landing-regular, no image, no description/buttons

```html
<section class="maryland-hero maryland-hero--landing-regular has-illustration no-image no-description-buttons" aria-labelledby="hero-title">
  <div class="maryland-hero__container">
    <div class="maryland-hero__content">
      <div class="maryland-hero__breadcrumb">
        <nav class="maryland-breadcrumb maryland-breadcrumb--light" aria-label="Breadcrumb">
          <!-- breadcrumb items -->
        </nav>
      </div>
      <h1 id="hero-title" class="maryland-hero__title">Programs</h1>
    </div>
  </div>
</section>
```

Use this minimal form for very simple landing pages where you don't want a description or buttons. The hero is shorter overall.

## Markup — basic with image (interior page)

```html
<section class="maryland-hero maryland-hero--basic maryland-hero--flush has-illustration has-image" aria-labelledby="hero-title">
  <div class="maryland-hero__container">
    <div class="maryland-hero__row">
      <div class="maryland-hero__content">
        <div class="maryland-hero__breadcrumb">
          <nav class="maryland-breadcrumb maryland-breadcrumb--dark" aria-label="Breadcrumb">
            <ol class="maryland-breadcrumb__list">
              <li class="maryland-breadcrumb__list-item">
                <a class="maryland-breadcrumb__link" href="/">Home</a>
              </li>
              <li class="maryland-breadcrumb__list-item">
                <a class="maryland-breadcrumb__link" href="/services">Services</a>
              </li>
              <li class="maryland-breadcrumb__list-item">
                <a class="maryland-breadcrumb__link" aria-current="page" href="/services/fishing-license">Apply for a fishing license</a>
              </li>
            </ol>
          </nav>
        </div>
        <h1 id="hero-title" class="maryland-hero__title">Apply for a fishing license</h1>
      </div>
      <div class="maryland-hero__img-container">
        <figure class="maryland-hero__image">
          <img src="/img/fishing.jpg" alt="" />
        </figure>
      </div>
    </div>
  </div>
</section>
```

**Important constraint:** `maryland-hero--basic.has-image` positions the image absolutely on `tablet-lg+`, sticking 37px **above** the hero section. The parent of the hero must allow `overflow-y: visible` for this to render correctly — page templates handle this by default; don't wrap the hero in a `overflow: hidden` container.

The breadcrumb uses the **dark** variant because the background is blue. All breadcrumb text and separators are forced to white by the hero's CSS.

## Markup — basic without image

```html
<section class="maryland-hero maryland-hero--basic maryland-hero--flush has-illustration no-image" aria-labelledby="hero-title">
  <div class="maryland-hero__container">
    <div class="maryland-hero__content">
      <div class="maryland-hero__breadcrumb">
        <nav class="maryland-breadcrumb maryland-breadcrumb--dark" aria-label="Breadcrumb">
          <!-- breadcrumb items -->
        </nav>
      </div>
      <h1 id="hero-title" class="maryland-hero__title">Apply for a fishing license</h1>
    </div>
  </div>
</section>
```

## Markup — news

```html
<section class="maryland-hero maryland-hero--news maryland-hero--flush has-illustration no-image" aria-labelledby="hero-title">
  <div class="maryland-hero__container">
    <div class="maryland-hero__content">
      <div class="maryland-hero__breadcrumb">
        <nav class="maryland-breadcrumb maryland-breadcrumb--dark" aria-label="Breadcrumb">
          <ol class="maryland-breadcrumb__list">
            <li class="maryland-breadcrumb__list-item"><a class="maryland-breadcrumb__link" href="/">Home</a></li>
            <li class="maryland-breadcrumb__list-item"><a class="maryland-breadcrumb__link" href="/news">News</a></li>
            <li class="maryland-breadcrumb__list-item"><a class="maryland-breadcrumb__link" aria-current="page" href="/news/grants">Governor announces small business grants</a></li>
          </ol>
        </nav>
      </div>
      <h1 id="hero-title" class="maryland-hero__title">Governor announces small business grants</h1>
      <div class="maryland-hero__meta">
        <span class="maryland-hero__news-type">Press release</span>
        <span class="maryland-hero__meta-separator">|</span>
        <span class="maryland-hero__published-date">March 12, 2026</span>
      </div>
      <div class="maryland-hero__description">
        <p>The new initiative will provide grants to small businesses across the state.</p>
      </div>
    </div>
  </div>
</section>
```

News heroes never support side images. The news type renders in uppercase via CSS.

## Markup — event

```html
<section class="maryland-hero maryland-hero--event maryland-hero--flush has-illustration no-image" aria-labelledby="hero-title">
  <div class="maryland-hero__container">
    <div class="maryland-hero__content">
      <div class="maryland-hero__breadcrumb">
        <nav class="maryland-breadcrumb maryland-breadcrumb--dark" aria-label="Breadcrumb">
          <!-- breadcrumb items -->
        </nav>
      </div>
      <h1 id="hero-title" class="maryland-hero__title">Bay Restoration Public Meeting</h1>
      <div class="maryland-hero__details">
        <span class="maryland-hero__event-type">Public meeting</span>
        <span class="maryland-hero__meta-separator">|</span>
        <time class="maryland-hero__event-date">October 25, 2026 from 8:00 a.m. to 10:00 a.m.</time>
      </div>
    </div>
    <div class="maryland-hero__cta">
      <a href="/events/register" class="usa-button usa-button--big usa-button--white">Register today</a>
    </div>
  </div>
</section>
```

For past events, add a yellow tag immediately above the title (and you can also use a different label):

```html
<span class="usa-tag usa-tag--warning">Past event</span>
<h1 id="hero-title" class="maryland-hero__title">Bay Restoration Public Meeting</h1>
```

## Markup — location

The location hero renders **two** sibling elements: a thin hero strip with only the breadcrumb and a screen-reader-only title, followed by a white card outside the hero that contains the visible `<h1>`, image, and address.

```html
<section class="maryland-hero maryland-hero--location maryland-hero--flush has-illustration has-image" aria-labelledby="loc-title">
  <div class="maryland-hero__container">
    <div class="maryland-hero__breadcrumb">
      <nav class="maryland-breadcrumb maryland-breadcrumb--dark" aria-label="Breadcrumb">
        <!-- breadcrumb items -->
      </nav>
    </div>
    <span id="loc-title" class="usa-sr-only">Annapolis MVA Branch</span>
  </div>
</section>

<div class="grid-container maryland-location-card-container has-image">
  <div class="grid-row">
    <div class="grid-col-12 desktop:grid-col-3 maryland-hero__grid-spacer"></div>
    <div class="grid-col-12 desktop:grid-col-8 maryland-hero__grid-content">
      <div class="maryland-hero__location-card">
        <figure class="maryland-hero__image">
          <img src="/img/mva-annapolis.jpg" alt="" />
        </figure>
        <div class="maryland-hero__content">
          <h1 class="maryland-hero__title">Annapolis MVA Branch</h1>
          <address class="maryland-hero__address">
            <ul class="usa-list usa-list--unstyled">
              <li>160 Harry S. Truman Parkway</li>
              <li>Annapolis, MD 21401</li>
            </ul>
          </address>
        </div>
      </div>
    </div>
  </div>
</div>
```

Note: the visible title on the card is technically a second visual `<h1>`. The hero's `<span class="usa-sr-only">` carries the section's accessible name; the card's `<h1>` is the page's true heading. The address uses an unstyled USWDS list inside an `<address>` element.

## What each class does

| Class | Effect |
|---|---|
| `maryland-hero` | Base hero `<section>`. Provides positioning context, contains background-image and content layers. |
| `maryland-hero--landing-main` | Maryland.gov homepage variant. Fluid height (188px at 320px → 456px at 1400px viewport), full-bleed background photo, white background underneath. Top margin 0 mobile, 24px desktop; bottom margin 32px mobile, 64px desktop. |
| `maryland-hero--agency-home` | Agency homepage variant. Background photo with overlaid content card; content card is `ink` (near-black) background with white text. Padding 64px vertical at mobile-lg, 80px at desktop. |
| `maryland-hero--landing-agency` | Agency landing page variant. White background, dark text, max-width 1288px, top margin 48px at tablet-lg, bottom padding 120px at tablet-lg+. |
| `maryland-hero--landing-regular` | Generic landing page variant. Same dimensions as `landing-agency` but supports breadcrumb. White background, dark text. |
| `maryland-hero--basic` | Interior page variant. Maryland blue (`primary`) background, white text, flag illustration overlay at 75% opacity. Max-width 1288px, 56px horizontal margin at tablet-lg+, 48px top margin. |
| `maryland-hero--news` | News article variant. Same blue background and dimensions as `basic`, but no image support and a metadata line below the title. |
| `maryland-hero--event` | Event detail variant. Blue background, includes a details line and a right-aligned CTA. |
| `maryland-hero--location` | Location detail variant. Blue strip with only breadcrumb + sr-only title; a separate white card renders below the section. |
| `maryland-hero--flush` | Removes the divider between the page header and the hero so the hero sits flush against the header. Applied automatically to `basic`, `news`, `location`, `event`. |
| `has-illustration` | Enables the flag illustration overlay layer on dark variants and the diamond/flag decoration on light variants. |
| `has-image` | Two-column layout: content on the left, image on the right at `tablet-lg+`. On mobile the image stacks above content (except `basic`, which keeps it positioned). |
| `no-image` | Single-column layout, no side image. For light variants, swaps in flag illustration on the right. |
| `has-logo` | `landing-agency` only — enables agency-logo rendering (above title with image; on the right gradient block without image). |
| `no-description-buttons` | `landing-regular` only — removes the hero's min-height so a description-less hero is shorter. |
| `maryland-hero__background-image` | Absolutely-positioned wrapper for the full-bleed background photo. Image covers the full section, `object-fit: cover`, z-index 0. |
| `maryland-hero__container` | Inner wrapper that holds the content and sits above the background (z-index 1+). Becomes a `grid-container` widescreen wrapper for `basic`, `news`, `event`. |
| `maryland-hero__row` | Flex/grid row that creates the two-column layout when an image is present. Column on mobile, row at `tablet-lg`. |
| `maryland-hero__content` | Content column. For `agency-home`, the content card itself. Modifiers `--left`, `--center`, `--right` align content on `agency-home`. |
| `maryland-hero__img-container` | Image column wrapper. Sized to `grid-col(6)` at tablet-lg, `grid-col(5)` at desktop. |
| `maryland-hero__image` | The image `<figure>`. Fixed pixel widths per breakpoint with 33:35 (mobile) → 17:18 (tablet-lg+) aspect ratio. A blue diamond-pattern mask appears as a `::after` decoration behind and to the right. |
| `maryland-hero__logo-container` | Right-side column for the agency logo (landing-agency, no-image, has-logo). Aligned to the right at tablet-lg+. |
| `maryland-hero__agency-logo` | Logo wrapper. Max-height 115px. On `agency-home`, becomes an `ink`-colored rounded badge holding the logo image. |
| `maryland-hero__breadcrumb` | Wrapper for the inline breadcrumb. Adds 32px top padding and 24/32/48px bottom margin at mobile/mobile-lg/tablet-lg. Forces the breadcrumb to take full content width. |
| `maryland-hero__title` | The `<h1>`. Sizes differ by variant; for `landing-main` it's 35px → 55px → 96px; for `basic`/`landing-regular` it's 32px → 40px → 48px. Letter-spacing 0–3px. Font weight 300 (light) on white-backed variants, 400 (normal) on `landing-main`. |
| `maryland-hero__title-text` | Title text span inside the `<h1>` when an eyebrow is present (landing-main only). Renders on its own line. |
| `maryland-hero__eyebrow` | Uppercase prefix above the title (landing-main only — "Welcome to"). 14px (mobile) → 16px → 24px desktop, semibold, letter-spacing 1.28–1.92px, color gray-cool-50 (#71767A). |
| `maryland-hero__description` | Description text. 18px → 24px at mobile-lg+, line-height 1.6, dark text. 32–36px top margin. |
| `maryland-hero__buttons` | Button group. Stacks vertically on mobile, switches to horizontal row at `tablet-lg`. 16px gap. Buttons are full-width on mobile, auto-width at tablet-lg+. |
| `maryland-hero__cta` | Right-aligned CTA wrapper for the event variant. Sits at the bottom-right of the hero. |
| `maryland-hero__meta` | News metadata line (type + date). |
| `maryland-hero__news-type` | News type label. Uppercased via CSS. |
| `maryland-hero__published-date` | Published date label. |
| `maryland-hero__meta-separator` | `|` separator between type and date. |
| `maryland-hero__details` | Event metadata line (event type + date). |
| `maryland-hero__event-type` | Event type label. Uppercased. |
| `maryland-hero__event-date` | Event date / time string. Rendered inside a `<time>` element. |
| `maryland-hero__address` | Location card address block. Maps to `<address>` element. |
| `maryland-hero__location-card` | White card below the location hero that holds the visible title, image, and address. |
| `maryland-location-card-container` | Outer grid container for the location card. `has-image` / `no-image` modifier controls card layout. |
| `maryland-hero__grid-spacer` / `__grid-content` | Grid cells inside the location card container to align it to the page's two-column structure. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `landing-main` \| `agency-home` \| `landing-agency` \| `landing-regular` \| `basic` \| `news` \| `event` \| `location` | `landing-main` | Hero variant |
| `title` | string | varies | The `<h1>` text. For `landing-main`, a leading `"Welcome to "` prefix renders as an eyebrow. |
| `heroStyle` | `with-image` \| `no-image` | varies | Toggles image layout for `basic`, `landing-regular`, `landing-agency`, `location` |
| `description` | string | — | Body text under title (`landing-regular`, `landing-agency`, `agency-home`, `news`, `basic`) |
| `showDescription` | bool | varies | Toggle for `landing-regular` and `landing-agency` |
| `backgroundImage` | `forest` \| `farmland` \| `bridge` \| `neighborhood` | `forest` | Background photo (landing-main, agency-home) |
| `breadcrumb` | object `{ pages: [{ label, href }] }` | — | Breadcrumb (basic, news, landing-regular, event, location) |
| `image` | string (URL) | — | Side image (basic, landing-regular, landing-agency, location) |
| `primaryButton` | object `{ label, href }` | — | First button |
| `secondaryButton` | object `{ label, href }` | — | Second button |
| `showButtons` | bool | varies | Toggle buttons (landing-regular, landing-agency) |
| `showLogo` | bool | false | Show agency logo (landing-agency, agency-home) |
| `agencyLogo` | string (URL) | — | Agency logo image URL |
| `alignment` | `left` \| `center` \| `right` | `left` | Content alignment for `agency-home` |
| `newsType` | `Media advisory` \| `News article` \| `Press release` \| `Public notice` | — | News variant only |
| `publishedDate` | string | — | News variant only |
| `eventType` | `Public meeting` \| `Webinar` \| `Workshop` \| `Conference` \| `Ceremony` | — | Event variant only |
| `eventDate` | string | — | Event variant only |
| `isPastEvent` | bool | false | Event variant — adds "Past event" tag |
| `address` | object `{ line1, line2, cityStateZip }` | — | Location variant only |

## Common mistakes

1. **Adding a second `<h1>` later in the page** — the hero owns the page's only `<h1>`. Subsequent sections start at `<h2>`.
2. **Placing the breadcrumb outside the hero on landing/basic pages** — the breadcrumb belongs inside `maryland-hero__breadcrumb`, before the title. Mounting it above the hero in `<main>` breaks the dark-background styling override.
3. **Using `maryland-breadcrumb--light` inside a `basic` / `news` / `event` hero** — these heroes are dark; the breadcrumb must be `maryland-breadcrumb--dark`. The reverse is true for `landing-regular` / `landing-agency`.
4. **Wrapping the hero in a `overflow: hidden` container** — the `basic` variant's image sits 37px above the hero on tablet-lg+; clipping breaks this layout.
5. **Adding `block-spacing` to the hero** — heroes manage their own vertical rhythm. The first content section *after* the hero gets `block-spacing` (and its CSS already accounts for `margin-block-start: 0` on the first child).
6. **Putting `maryland-hero--flush` on a `landing-main` or `landing-regular`** — those are white-backed and naturally sit beneath the header; `--flush` is only for the dark variants that need to abut the header.
7. **Editing the description or title color with inline `<style>`** — color is determined by the variant. If text looks wrong, you've picked the wrong variant for the page type.
