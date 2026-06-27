# maryland-footer

The Maryland-branded agency footer. Dark navy block at the bottom of agency pages containing the agency name, social-media row, contact info, and link-group columns. Sits **above** the statewide footer (`<maryland-statewide-footer>`) — both go on agency pages, agency footer first.

> **Don't confuse this with `<maryland-statewide-footer>`.** This component is the agency-specific block (address, phone, email, agency links). The statewide footer is a separate web component that follows it with state-wide service links (services, government, policies, alerts). See `cdn/components/maryland-statewide-footer.md`.

## What it looks like

Full-width dark block with `ink` (near-black) background and light text. Content is constrained to a `widescreen` (1400px) `grid-container` with default site margins.

The footer renders two optional sections, controlled by `displayAgency` and `displaySitewide`:

**Agency section (`displayAgency: true`):**
- Top row: agency wordmark (vertical inverted, ~85×58px mobile / ~85×70px desktop) plus the agency name as an `<h2>` (22px / `body-11`, semibold, white). On the right side of the same row, the social-media icon row (`maryland-social`) — at desktop, pinned to the far right via `margin-inline-start: auto`.
- A 1px `base-darker` horizontal divider with 40px (`units(5)`) vertical margin.
- Below the divider, a two-area layout (at desktop): a 25% contact column on the left and a 75% link-groups column on the right. The contact column shows address, parent agency description, phone (telephone link), email (mailto link), and Maryland Relay 7-1-1. The link-groups column shows three nav groups (heading + bulleted list of links) plus optional standalone links. At tablet, the link-groups column flows into 2 columns; at desktop, 3 columns.
- Another 1px `base-darker` divider closes the agency section.

**Statewide section (`displaySitewide: true`):**
- An `<h2>` titled "Explore Maryland.gov" (22px, semibold, white).
- A grid of five `<nav>` link-groups: Top services, Government, Policies, Connect, Alerts. At tablet, the content lays out in 2 columns; at desktop, 4 columns.
- A 1px `base-darker` divider with `units(7)` margin at desktop.
- Bottom branding row: horizontal inverted Maryland wordmark on the left, copyright text on the right at desktop (stacked on mobile). Logo is 176×36px (11rem × 2.25rem). Copyright is 14px (`body-4`) `base-lighter`.

**Typography:** Link-group headings are 16px (`body-6`) semibold white. Link items are 14px (`body-4`) `base-lighter` with no underline by default, underline on hover.

**Sticky-to-bottom behavior:** when wrapped inside `.maryland-page`, the footer pins to the bottom of the viewport (`position: sticky; top: 100%`) so short pages still push the footer to the bottom.

## When to use which variant

- **Agency-only** (`displayAgency: true`, `displaySitewide: false`) — Most agency pages. Pair with `<maryland-statewide-footer>` after this in markup.
- **Statewide-only** (`displayAgency: false`, `displaySitewide: true`) — Pages that don't need agency-specific info. Note: the standalone `<maryland-statewide-footer>` web component covers this case with zero config — prefer it on the Maryland.gov state homepage.
- **Both** (`displayAgency: true`, `displaySitewide: true`) — Sometimes used to render the full footer from one template, but the canonical pattern is `maryland-footer` (agency) + `<maryland-statewide-footer>` (statewide) as two separate elements.

## Default markup — agency footer

```html
<footer class="maryland-footer">
  <div class="maryland-footer__container">
    <section aria-labelledby="agency-footer" class="maryland-footer__section">

      <!-- Agency identity + social row -->
      <div class="maryland-footer__agency">
        <a class="maryland-footer__agency-home" href="/">
          <img
            class="maryland-footer__agency-logo"
            src="/img/md_wordmark_vertical_inverted.svg"
            alt="Department of Natural Resources home"
          />
          <h2 class="maryland-footer__agency-name" id="agency-footer">
            Department of Natural Resources
          </h2>
        </a>
        <!-- Social media row -->
        <ul class="maryland-social">
          <li>
            <a href="https://facebook.com/MarylandDNR" class="maryland-social__link maryland-social__link--facebook">
              <span class="usa-sr-only">Connect with Department of Natural Resources on facebook.com (external link)</span>
            </a>
          </li>
          <li>
            <a href="https://x.com/MarylandDNR" class="maryland-social__link maryland-social__link--x">
              <span class="usa-sr-only">Connect with Department of Natural Resources on x.com (external link)</span>
            </a>
          </li>
          <li>
            <a href="https://youtube.com/MarylandDNR" class="maryland-social__link maryland-social__link--youtube">
              <span class="usa-sr-only">Connect with Department of Natural Resources on youtube.com (external link)</span>
            </a>
          </li>
          <li>
            <a href="https://instagram.com/MarylandDNR" class="maryland-social__link maryland-social__link--instagram">
              <span class="usa-sr-only">Connect with Department of Natural Resources on instagram.com (external link)</span>
            </a>
          </li>
          <li>
            <a href="https://linkedin.com/company/MarylandDNR" class="maryland-social__link maryland-social__link--linkedin">
              <span class="usa-sr-only">Connect with Department of Natural Resources on linkedin.com (external link)</span>
            </a>
          </li>
          <li>
            <a href="https://flickr.com/photos/MarylandDNR" class="maryland-social__link maryland-social__link--flickr">
              <span class="usa-sr-only">Connect with Department of Natural Resources on flickr.com (external link)</span>
            </a>
          </li>
        </ul>
      </div>

      <hr aria-hidden="true" class="maryland-footer__divider" />

      <!-- Contact + link groups -->
      <div class="maryland-footer__agency-menu">
        <div class="maryland-footer__agency-contact">
          <div class="maryland-footer__link-group">
            <h3 class="maryland-footer__link-group-heading">Contact us</h3>
            <ul class="maryland-footer__link-group-list">
              <li>580 Taylor Avenue, Annapolis, MD 21401</li>
              <li>An official agency of the State of Maryland</li>
              <li><a href="tel:8778201990">(877) 620-8DNR</a></li>
              <li><a href="mailto:customerservice.dnr@maryland.gov">customerservice.dnr@maryland.gov</a></li>
              <li><a href="tel:711">Maryland Relay: 7-1-1</a></li>
            </ul>
          </div>
        </div>

        <div class="maryland-footer__agency-links">
          <nav class="maryland-footer__link-group" aria-labelledby="footer-services">
            <h3 class="maryland-footer__link-group-heading" id="footer-services">Services</h3>
            <ul class="maryland-footer__link-group-list">
              <li><a href="/fishing">Fishing licenses</a></li>
              <li><a href="/hunting">Hunting licenses</a></li>
              <li><a href="/boating">Boating registration</a></li>
            </ul>
          </nav>

          <nav class="maryland-footer__link-group" aria-labelledby="footer-parks">
            <h3 class="maryland-footer__link-group-heading" id="footer-parks">Parks &amp; lands</h3>
            <ul class="maryland-footer__link-group-list">
              <li><a href="/parks">State parks</a></li>
              <li><a href="/forests">State forests</a></li>
              <li><a href="/reservations">Camping reservations</a></li>
            </ul>
          </nav>

          <nav class="maryland-footer__link-group" aria-labelledby="footer-about">
            <h3 class="maryland-footer__link-group-heading" id="footer-about">About</h3>
            <ul class="maryland-footer__link-group-list">
              <li><a href="/about">Our mission</a></li>
              <li><a href="/jobs">Careers</a></li>
              <li><a href="/news">News &amp; press</a></li>
            </ul>
          </nav>

          <a href="/contact" class="maryland-footer__link-group">Contact form</a>
          <a href="/foia" class="maryland-footer__link-group">FOIA requests</a>
        </div>
      </div>

      <hr aria-hidden="true" class="maryland-footer__divider" />
    </section>
  </div>
</footer>
```

## Markup — statewide footer

Set `displaySitewide: true` to add (or use standalone). This block sits inside the same `<footer class="maryland-footer"><div class="maryland-footer__container">` wrapper as the agency block.

```html
<section aria-labelledby="global-footer" class="maryland-footer__section">
  <h2 class="maryland-footer__title" id="global-footer">Explore Maryland.gov</h2>
  <div class="maryland-footer__content">
    <nav class="maryland-footer__link-group" aria-labelledby="top-services">
      <h3 class="maryland-footer__link-group-heading" id="top-services">Top services</h3>
      <ul class="maryland-footer__link-group-list">
        <li><a href="https://mva.maryland.gov/vehicles">Vehicle services</a></li>
        <li><a href="https://dhs.maryland.gov/supplemental-nutrition-assistance-program/">Food assistance / SNAP</a></li>
        <li><a href="https://www.labor.maryland.gov/employment/unemployment.shtml">Unemployment services</a></li>
        <li><a href="https://www.marylandtaxes.gov/individual/index.php">Taxes</a></li>
        <li><a href="https://elections.maryland.gov/voter_registration/index.html">Register to vote</a></li>
        <li><a href="https://www.maryland.gov/pages/residents.aspx">Resident resources</a></li>
        <li><a href="https://www.visitmaryland.org/">Visit Maryland</a></li>
        <li><a href="https://www.maryland.gov/pages/online_services.aspx">More online services</a></li>
      </ul>
    </nav>

    <nav class="maryland-footer__link-group" aria-labelledby="government">
      <h3 class="maryland-footer__link-group-heading" id="government">Government</h3>
      <ul class="maryland-footer__link-group-list">
        <li><a href="https://governor.maryland.gov/">Governor Wes Moore</a></li>
        <li><a href="https://governor.maryland.gov/leadership/cabinet/">Maryland cabinet agencies</a></li>
        <li><a href="http://www.maryland.gov/pages/agency_directory.aspx">All state agencies</a></li>
        <li><a href="https://www.maryland.gov/pages/state_employees.aspx">For state employees</a></li>
        <li><a href="https://www.maryland.gov/pages/jobs.aspx">Maryland state jobs</a></li>
        <li><a href="https://www.ola.state.md.us/fraud/ola-fraud-hotline/">Report state government fraud</a></li>
      </ul>
    </nav>

    <nav class="maryland-footer__link-group" aria-labelledby="policies">
      <h3 class="maryland-footer__link-group-heading" id="policies">Policies</h3>
      <ul class="maryland-footer__link-group-list">
        <li><a href="https://www.maryland.gov/pages/accessibility.aspx">Accessibility</a></li>
        <li><a href="https://www.maryland.gov/pages/privacy_security.aspx">Privacy &amp; security</a></li>
        <li><a href="https://www.maryland.gov/terms-use">Terms of use</a></li>
      </ul>
    </nav>

    <nav class="maryland-footer__link-group" aria-labelledby="connect">
      <h3 class="maryland-footer__link-group-heading" id="connect">Connect</h3>
      <ul class="maryland-footer__link-group-list">
        <li><a href="https://mdrelay.maryland.gov/Pages/default.aspx">Maryland Relay: 7-1-1</a></li>
        <li><a href="http://www.doit.state.md.us/phonebook/">State employee directory</a></li>
        <li><a href="https://news.maryland.gov/">Maryland news</a></li>
        <li><a href="https://www.doit.state.md.us/selectsurvey/TakeSurvey.aspx?SurveyID=86M2956">Customer service survey</a></li>
      </ul>
    </nav>

    <nav class="maryland-footer__link-group" aria-labelledby="alerts">
      <h3 class="maryland-footer__link-group-heading" id="alerts">Alerts</h3>
      <ul class="maryland-footer__link-group-list">
        <li><a href="https://mdready.maryland.gov/be-informed/Pages/sign-up-for-alerts.aspx">Emergency alerts</a></li>
        <li><a href="https://chart.maryland.gov/Incidents/GetIncidents">Travel alerts</a></li>
        <li><a href="https://doit.maryland.gov/cybersecurity/">Cybersecurity</a></li>
        <li><a href="https://goccp.maryland.gov/victim-services/human-trafficking/">Report human trafficking</a></li>
        <li><a href="https://response.maryland.gov/bridge">Key bridge</a></li>
      </ul>
    </nav>
  </div>

  <hr aria-hidden="true" class="maryland-footer__divider" />

  <div class="maryland-footer__branding">
    <a class="maryland-footer__logo-link" href="https://maryland.gov">
      <img
        class="maryland-footer__logo"
        src="/img/md_wordmark_horizontal_inverted.svg"
        alt="Maryland.gov home"
      />
    </a>
    <div class="maryland-footer__copyright">
      &copy; 2026 State of Maryland. All rights reserved.
    </div>
  </div>
</section>
```

## What each class does

| Class | Effect |
|---|---|
| `maryland-footer` | The outer `<footer>`. Dark `ink` background, white-ish text. `contain: layout` for isolation. When nested in `.maryland-page`, `position: sticky; top: 100%` pins it to the bottom of short pages. |
| `maryland-footer__container` | Inner container that applies the `widescreen` (1400px) `grid-container`. Required for content to stay within the page max-width. |
| `maryland-footer__section` | One vertical section of footer content (agency section, statewide section). Adds top margin between sections; the last one has extra bottom margin so the copyright doesn't sit flush to the viewport edge. |
| `maryland-footer__agency` | Flex row holding the logo + agency name on the left and the social-media row on the right. Wraps on mobile, becomes nowrap at tablet+. |
| `maryland-footer__agency-home` | The wrapping `<a>` around the logo + agency name. Inline-flex column on mobile, row at `mobile-lg` (480px+). |
| `maryland-footer__agency-logo` | The wordmark image. ~85×58px (mobile) / ~85×70px (desktop). Vertical inverted wordmark — used because the dark background needs the inverted variant. |
| `maryland-footer__agency-name` | The agency name as an `<h2>`. 22px (`body-11`) semibold, color inherited (white-on-ink). Trims max-width at tablet+ so it doesn't push the social row off-screen. |
| `maryland-footer__agency-menu` | The flex row holding the contact column (25%) and link-groups column (75%) at desktop. Stacks on mobile. |
| `maryland-footer__agency-contact` | Left column at desktop (25% width, with right padding of 48px). Holds the contact link group. |
| `maryland-footer__agency-links` | Right column at desktop (75% width, ~8px left padding). Holds 1-3 `<nav>` link-groups plus optional standalone link items. CSS `column-count: 3` at desktop, `column-count: 2` at tablet — link-groups flow into multi-column layout. |
| `maryland-footer__title` | Heading for the statewide-services section ("Explore Maryland.gov"). 22px semibold, white. |
| `maryland-footer__content` | Multi-column grid for statewide link groups. 2 columns at tablet, 4 at desktop. |
| `maryland-footer__link-group` | Container for a heading + link list. Can also be used as a single link (rendered as an `<a class="maryland-footer__link-group">`) for standalone link items. 40px (`units(5)`) vertical margin between groups (collapsed on outer edges). |
| `maryland-footer__link-group-heading` | Group heading (typically `<h3>`). 16px (`body-6`) semibold, color inherited (white). 24px (`units(3)`) bottom margin. |
| `maryland-footer__link-group-list` | The `<ul>`. Unstyled (no bullets, no margin/padding). |
| `maryland-footer__link-group-list li` | Each list item. 14px (`body-4`). 12px (`units(1.5)`) vertical margin between items. |
| `maryland-footer__divider` | Horizontal rule. 1px, color `base-darker`, no border. Used to separate agency identity from contact/links, and to separate statewide content from branding. |
| `maryland-footer__branding` | Bottom row of statewide section with horizontal wordmark + copyright. Stacks on mobile, becomes a flex space-between row at desktop. |
| `maryland-footer__logo-link` | The `<a>` wrapping the horizontal wordmark in the branding row. Links to `https://maryland.gov`. |
| `maryland-footer__logo` | Horizontal inverted wordmark in the branding row. 176×36px (11rem × 2.25rem). |
| `maryland-social` | Social-media icon row. Flex row, no list bullets. At desktop, `margin-inline-start: auto` pins it to the right side of the `maryland-footer__agency` row. |
| `maryland-social__link` | Base social-link `<a>`. Square icon button (~32–40px) with a background-image mask. Hover/focus brightens the icon. |
| `maryland-social__link--facebook` / `--x` / `--youtube` / `--instagram` / `--linkedin` / `--flickr` | Per-platform modifier that sets the icon glyph via CSS background-image. **Required** — without it, the icon is missing. |
| `maryland-footer__copyright` | Copyright text. 14px (`body-4`), color `base-lighter`. |
| `maryland-footer a` | Footer links. Color `base-lighter`, no underline, underline on hover. Inherits the `focus--dark` mixin so focus rings remain visible on the dark background. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `displayAgency` | bool | `false` | Render the agency identity + contact + agency-link-groups block. |
| `displaySitewide` | bool | `false` | Render the "Explore Maryland.gov" statewide section. |
| `agencyTitle` | string | `"Agency Title"` | Agency display name. |
| `contactAddress` | string | sample address | Agency mailing address. |
| `parentAgency` | string | sample text | Parent-agency description line (e.g., "An official agency of the State of Maryland"). |
| `contactPhone` | string | `"(202) 555-5555"` | Phone number. Auto-linked as `tel:` with non-digit characters stripped. |
| `contactEmail` | string | `"example@maryland.gov"` | Email address. Auto-linked as `mailto:`. |

## Heading level adjustment

`maryland-footer__agency-name` is an `<h2>` and `maryland-footer__link-group-heading` is an `<h3>`. These are the canonical levels because:

- The page's `<h1>` is the hero title.
- The footer is a major section of the page (alongside `<main>`), so the agency name is `<h2>`.
- Each link-group is a sub-section, so the headings are `<h3>`.

**Don't change these.** Footer hierarchy is fixed.

## Common mistakes

1. **Putting the statewide footer above the agency footer** — order is fixed: agency `maryland-footer` first, then `<maryland-statewide-footer>` below it. See `cdn/page-shell.md`.
2. **Using the non-inverted (dark) wordmark on the dark background** — the footer background is `ink`. Use `md_wordmark_vertical_inverted.svg` (white) for the agency logo and `md_wordmark_horizontal_inverted.svg` for the statewide branding row.
3. **Omitting `<div class="maryland-footer__container">`** — without it, content runs edge-to-edge of the viewport instead of staying within the page max-width.
4. **Making link-group headings `<h2>`** — they're `<h3>` because the agency name (`maryland-footer__agency-name`) is the section's `<h2>`. Skipping levels breaks the outline.
5. **Forgetting to wrap the email in `<a href="mailto:">`** — the published CSS styles `a` elements specifically; plain text won't get the hover state.
6. **Reaching for the standalone `<maryland-statewide-footer>` when the agency footer is already rendering both blocks** — pick one approach. Either use `maryland-footer` with `displaySitewide: true` *or* `maryland-footer` (agency only) + `<maryland-statewide-footer>` below it. Don't render the statewide content twice.
7. **Adding custom margin or padding to push the footer down** — when wrapped in `.maryland-page`, the footer's sticky positioning handles this. Don't add `margin-top: auto` or similar.
