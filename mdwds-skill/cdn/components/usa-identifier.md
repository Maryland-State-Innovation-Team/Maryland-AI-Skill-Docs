# usa-identifier

The USWDS agency identifier strip — a federal-style "parent agency, required links, USA.gov" block at the very bottom of a page. Identifies the publishing agency, lists required legal/policy links (FOIA, privacy, accessibility, etc.), and ends with a portal link.

> **Rarely used in Maryland-branded sites.** The MDWDS `<maryland-statewide-footer>` covers similar needs with Maryland-specific styling, link sets, and state-portal branding. Use `usa-identifier` only for federal-style pages or where the USWDS three-section identifier pattern is specifically required. See `cdn/components/maryland-statewide-footer.md`.

## What it looks like

A dark-gray (`base-darkest`) full-width strip at the very bottom of the page, separated into three horizontal sections stacked vertically:

1. **Masthead** — agency logo on the left + parent agency name/domain on the right. Logo is a small ~40px square image (`usa-identifier__logo-img`). Below the logo block: the domain (e.g., `maryland.gov`) in 16px semibold, then "An official website of the {Agency Name}" in 14-16px normal weight with the agency name as a link.

2. **Required links** — a horizontal `<ul>` of small (12-14px) underlined links pointing to:
   - About {agency}
   - Accessibility statement
   - FOIA requests
   - No FEAR Act data
   - Office of the Inspector General
   - Performance reports
   - Privacy policy

   At desktop, the list lays out as two columns; on mobile, single column.

3. **State portal** (themed for Maryland in this MDWDS variant — the USWDS upstream version says "USA.gov") — a one-line block with descriptive text "Looking for Maryland state government information and services?" on the left and a "Visit Maryland.gov" link on the right (or stacked on mobile).

Styling is upstream USWDS — dark background, white text, white-ish link colors. Themed to Maryland's primary blue for link hover states.

## Variants

No class-driven variants — the component has a fixed three-section structure. Customization is per-instance content (agency name, domain, logo URL, links).

## Default markup

```html
<div class="usa-identifier">

  <!-- Section 1: Masthead -->
  <section class="usa-identifier__section usa-identifier__section--masthead" aria-label="Agency identifier">
    <div class="usa-identifier__container">
      <div class="usa-identifier__logos">
        <a href="/" class="usa-identifier__logo">
          <img
            class="usa-identifier__logo-img"
            src="/img/mdwds-logo-wings.png"
            alt="Maryland Department of Natural Resources logo"
            role="img"
          />
        </a>
      </div>
      <section class="usa-identifier__identity" aria-label="Agency description">
        <p class="usa-identifier__identity-domain">dnr.maryland.gov</p>
        <p class="usa-identifier__identity-disclaimer">
          <span aria-hidden="true">An </span>official website of the
          <a href="/">Maryland Department of Natural Resources</a>
        </p>
      </section>
    </div>
  </section>

  <!-- Section 2: Required links -->
  <nav class="usa-identifier__section usa-identifier__section--required-links" aria-label="Important links">
    <div class="usa-identifier__container">
      <ul class="usa-identifier__required-links-list">
        <li class="usa-identifier__required-links-item">
          <a href="/about" class="usa-identifier__required-link usa-link">
            About Maryland Department of Natural Resources
          </a>
        </li>
        <li class="usa-identifier__required-links-item">
          <a href="/accessibility" class="usa-identifier__required-link usa-link">Accessibility statement</a>
        </li>
        <li class="usa-identifier__required-links-item">
          <a href="/foia" class="usa-identifier__required-link usa-link">FOIA requests</a>
        </li>
        <li class="usa-identifier__required-links-item">
          <a href="/no-fear-act" class="usa-identifier__required-link usa-link">No FEAR Act data</a>
        </li>
        <li class="usa-identifier__required-links-item">
          <a href="/oig" class="usa-identifier__required-link usa-link">Office of the Inspector General</a>
        </li>
        <li class="usa-identifier__required-links-item">
          <a href="/reports" class="usa-identifier__required-link usa-link">Performance reports</a>
        </li>
        <li class="usa-identifier__required-links-item">
          <a href="/privacy" class="usa-identifier__required-link usa-link">Privacy policy</a>
        </li>
      </ul>
    </div>
  </nav>

  <!-- Section 3: State portal pointer -->
  <section class="usa-identifier__section usa-identifier__section--usagov" aria-label="Maryland state government information and services">
    <div class="usa-identifier__container">
      <div class="usa-identifier__usagov-description">
        Looking for Maryland state government information and services?
      </div>
      <a href="https://maryland.gov" class="usa-link">Visit Maryland.gov</a>
    </div>
  </section>

</div>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-identifier` | Outer wrapper. Sets dark `base-darkest` background, white text, full-width. |
| `usa-identifier__section` | One of the three horizontal sections. Stacks vertically; each section has padding (~24-32px vertical). |
| `usa-identifier__section--masthead` | Marker for section 1 — logo + agency name/domain layout. |
| `usa-identifier__section--required-links` | Marker for section 2 — links list. Two-column layout at desktop. |
| `usa-identifier__section--usagov` | Marker for section 3 — state-portal pointer. Flex row at desktop, stacked on mobile. |
| `usa-identifier__container` | Inner grid-container wrapper that keeps content within the page max-width. |
| `usa-identifier__logos` | Wraps the logo `<a>`. |
| `usa-identifier__logo` | The logo `<a>`. |
| `usa-identifier__logo-img` | The logo `<img>`. Sized to ~40-48px square. |
| `usa-identifier__identity` | Wraps the domain + disclaimer text. |
| `usa-identifier__identity-domain` | The domain line. 16-18px, semibold, white. |
| `usa-identifier__identity-disclaimer` | The "An official website of..." line. 14-16px normal weight; agency-name link uses underlined primary color. |
| `usa-identifier__required-links-list` | The `<ul>` of links. No bullets. Two-column at desktop. |
| `usa-identifier__required-links-item` | Each `<li>`. |
| `usa-identifier__required-link` | The link inside the item. Underlined, white-ish, primary-blue hover. |
| `usa-identifier__usagov-description` | Descriptive text in the portal-pointer section. |
| `usa-link` | USWDS link helper (underline, primary color, hover state). |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `agencyName` | string | `"Parent agency"` | Agency name used in the "An official website of..." line and in "About {agency}" link text. |
| `domain` | string | `"maryland.gov"` | Domain shown in the masthead. |
| `logoSrc` | string | `"/assets/img/mdwds-logo-wings.png"` | Logo image URL. |
| `logoAlt` | string | `"Parent agency logo"` | Alt text for the logo image. |
| `enableAnalytics` | bool | `false` | Adds `data-ga-*` attributes to each link for GA tracking. |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values. |

## Heading level adjustment

The identifier uses `<section aria-label>` for each block (no visible headings). **Do not** add `<h2>` titles to the sections — the ARIA labels provide the landmark names.

## Common mistakes

1. **Using this instead of `<maryland-statewide-footer>`** — on Maryland.gov agency pages, the statewide footer covers the agency-identification and state-portal-link needs in a Maryland-themed way. The identifier is a federal pattern; using it on a Maryland page produces a mismatched federal-style footer.
2. **Omitting required links** — the seven canonical required links (About, Accessibility, FOIA, No FEAR Act, OIG, Performance, Privacy) are part of the federal pattern. Removing any of them defeats the component's purpose. If you don't need them all, you probably don't need this component.
3. **Forgetting `aria-label` on each section** — each `<section>` and `<nav>` inside the identifier has its own `aria-label`. Skipping them leaves the landmarks unnamed.
4. **Linking the logo to an external site** — the logo should link to the agency's homepage (or the `/` root of the site), not to USA.gov.
5. **Replacing "Visit Maryland.gov" with another link** — the third section is for the state portal pointer. Don't repurpose it for unrelated links.
6. **Stacking this **and** `<maryland-statewide-footer>`** — they cover overlapping ground. Pick one.
7. **Hardcoding `<span aria-hidden="true">An </span>` removal** — the visually-hidden "An " before "official website" is intentional. It improves screen-reader phrasing ("An official website of the...") while keeping the visible text starting with "official website."
