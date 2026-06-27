# usa-collection

The USWDS Collection is the canonical component for **vertical lists of related items** — news articles, press releases, events, search results, resource directories. Each item supports a heading, a description, metadata (author, date, tags), and either a thumbnail image **or** a calendar-style date block on the left.

> **There is no `maryland-collection`.** `usa-collection` is the standard component for article/news/event lists on Maryland.gov pages. Use it directly; the MDWDS CDN restyles it to fit the Maryland visual system (Maryland-tuned typography, link colors, and the filled-blue `usa-tag--new` style).

## What it looks like

A `usa-collection` is an unstyled `<ul>` where each `<li class="usa-collection__item">` is a horizontal row with two regions:

1. **Left visual** — either a small thumbnail image (`usa-collection__img`, ~80px square at default size) **or** a calendar-date block (`usa-collection__calendar-date`, a square card with the abbreviated month at the top and the day number below). If neither is present, the body fills the full width.
2. **Right body** — heading at the top (rendered as `<h2>`–`<h6>` per the `headingLevel` arg; styled with semibold Source Sans Pro Web at ~16px in the default variant), an optional description paragraph (~16px, color `text-base-dark`), and a metadata strip at the bottom (`usa-collection__meta`) showing author, date, and tags as inline pills.

Between items there is a horizontal `1px solid` divider (USWDS border color). The **condensed** variant tightens the vertical padding between items. The **headings-only** variant removes the description and metadata, leaving only the heading and an optional source line, making it ideal for a compact list-of-links treatment.

External link icons (a small launch SVG ~16×16, vertically centered with `margin-left: 0.25rem`) sit next to the heading when `item.isExternal` is true.

The `usa-tag--new` modifier — used inside the metadata strip — receives the MDWDS override: solid `#005ea2` blue background with white text (instead of the USWDS default outlined treatment).

## Variants

| Variant | Visual |
|---|---|
| `default` | Full layout: heading, description, metadata strip, optional thumbnail or calendar date. |
| `condensed` | Same content layout but with reduced vertical spacing between items. Adds `usa-collection--condensed` modifier. |
| `headings-only` | Heading + optional source line only. No description, no author/date/tag metadata. Calendar dates and thumbnails are also suppressed. |

## When to use which variant

- **`default`** → News landing pages, press release lists, event listings — anywhere the description and metadata give meaningful context.
- **`condensed`** → Sidebar lists, dashboards, dense indices — when you need to fit more items into limited vertical space.
- **`headings-only`** → Lists of outbound links or resources where the title and source domain are all that matter.

## Default markup

```html
<ul class="usa-collection">
  <li class="usa-collection__item">
    <div class="usa-collection__body">
      <h3 class="usa-collection__heading">
        <a class="usa-link" href="/news/health-equity-grants">
          Maryland Department of Health awards $4.2M in health equity grants
        </a>
      </h3>
      <p class="usa-collection__description">
        The grants will fund community-based programs in Baltimore City, Prince George's County, and the Eastern Shore focused on reducing maternal health disparities.
      </p>
      <ul class="usa-collection__meta" aria-label="More information">
        <li class="usa-collection__meta-item">By Office of Communications</li>
        <li class="usa-collection__meta-item">
          <time datetime="2026-05-12">May 12, 2026</time>
        </li>
        <li class="usa-collection__meta-item usa-tag usa-tag--new">NEW</li>
        <li class="usa-collection__meta-item usa-tag">PRESS RELEASE</li>
        <li class="usa-collection__meta-item usa-tag">HEALTH EQUITY</li>
      </ul>
    </div>
  </li>
  <li class="usa-collection__item">
    <div class="usa-collection__body">
      <h3 class="usa-collection__heading">
        <a class="usa-link" href="/news/transit-expansion">
          MDOT announces Purple Line schedule adjustments
        </a>
      </h3>
      <p class="usa-collection__description">
        Service changes take effect June 1 across the College Park, Silver Spring, and Bethesda segments.
      </p>
      <ul class="usa-collection__meta" aria-label="More information">
        <li class="usa-collection__meta-item">By Maryland Transit Administration</li>
        <li class="usa-collection__meta-item">
          <time datetime="2026-05-08">May 8, 2026</time>
        </li>
        <li class="usa-collection__meta-item usa-tag">TRANSIT</li>
      </ul>
    </div>
  </li>
</ul>
```

## Markup — with thumbnail image

```html
<ul class="usa-collection">
  <li class="usa-collection__item">
    <img class="usa-collection__img"
         src="/img/news/chesapeake-cleanup.jpg"
         alt="Volunteers collecting trash along the Chesapeake shoreline" />
    <div class="usa-collection__body">
      <h3 class="usa-collection__heading">
        <a class="usa-link" href="/news/cleanup-day">
          Annual Chesapeake Bay cleanup draws 12,000 volunteers
        </a>
      </h3>
      <p class="usa-collection__description">
        Statewide volunteer crews removed over 200 tons of debris from Bay tributaries during the April 26 event.
      </p>
      <ul class="usa-collection__meta" aria-label="More information">
        <li class="usa-collection__meta-item">By Department of Natural Resources</li>
        <li class="usa-collection__meta-item">
          <time datetime="2026-04-28">April 28, 2026</time>
        </li>
        <li class="usa-collection__meta-item usa-tag">ENVIRONMENT</li>
        <li class="usa-collection__meta-item usa-tag">VOLUNTEER</li>
      </ul>
    </div>
  </li>
</ul>
```

## Markup — with calendar date (event list)

```html
<ul class="usa-collection">
  <li class="usa-collection__item">
    <div class="usa-collection__calendar-date">
      <time datetime="2026-07-04">
        <span class="usa-collection__calendar-date-month">JUL</span>
        <span class="usa-collection__calendar-date-day">04</span>
      </time>
    </div>
    <div class="usa-collection__body">
      <h3 class="usa-collection__heading">
        <a class="usa-link" href="/events/independence-day-annapolis">
          Independence Day Celebration on the State House grounds
        </a>
      </h3>
      <p class="usa-collection__description">
        Live music, family activities, and fireworks over Annapolis Harbor. Gates open at 4:00 PM.
      </p>
    </div>
  </li>
  <li class="usa-collection__item">
    <div class="usa-collection__calendar-date">
      <time datetime="2026-09-12">
        <span class="usa-collection__calendar-date-month">SEP</span>
        <span class="usa-collection__calendar-date-day">12</span>
      </time>
    </div>
    <div class="usa-collection__body">
      <h3 class="usa-collection__heading">
        <a class="usa-link" href="/events/maryland-million">
          Maryland Million Day at Laurel Park
        </a>
      </h3>
      <p class="usa-collection__description">
        Maryland-bred thoroughbreds compete in nine stakes races. Post time 12:25 PM.
      </p>
    </div>
  </li>
</ul>
```

**Important:** thumbnail (`usa-collection__img`) and calendar date (`usa-collection__calendar-date`) are **mutually exclusive** — use one or the other for a given item.

## Markup — condensed variant

```html
<ul class="usa-collection usa-collection--condensed">
  <li class="usa-collection__item">
    <div class="usa-collection__body">
      <h4 class="usa-collection__heading">
        <a class="usa-link" href="/news/budget-update">FY26 budget signed into law</a>
      </h4>
      <p class="usa-collection__description">
        Governor signs $63B operating budget with record investment in education.
      </p>
      <ul class="usa-collection__meta" aria-label="More information">
        <li class="usa-collection__meta-item">
          <time datetime="2026-05-30">May 30, 2026</time>
        </li>
      </ul>
    </div>
  </li>
  <!-- More items, same structure, no images -->
</ul>
```

## Markup — headings-only variant

```html
<ul class="usa-collection">
  <li class="usa-collection__item">
    <div class="usa-collection__body">
      <h3 class="usa-collection__heading">
        <a class="usa-link" href="https://designsystem.maryland.gov/">
          Maryland Web Design System documentation
          <svg class="usa-icon" aria-hidden="true" focusable="false" role="img">
            <use xlink:href="/assets/img/sprite.svg#launch"></use>
          </svg>
        </a>
      </h3>
      <p class="usa-collection__meta-item usa-collection__source">
        <svg class="usa-icon" aria-hidden="true" focusable="false" role="img">
          <use xlink:href="/assets/img/sprite.svg#public"></use>
        </svg>
        designsystem.maryland.gov
      </p>
    </div>
  </li>
  <li class="usa-collection__item">
    <div class="usa-collection__body">
      <h3 class="usa-collection__heading">
        <a class="usa-link" href="/services/business-licensing">
          Apply for a Maryland business license
        </a>
      </h3>
    </div>
  </li>
</ul>
```

The `usa-collection__source` line is rendered as a small gray (`color: #71767a`) flex row with a public/globe icon, ~0.93rem font, sitting directly below the heading.

## The `usa-collection__meta` pattern (read this)

The metadata strip is an `<ul class="usa-collection__meta" aria-label="More information">` placed **inside** `usa-collection__body`, below the description. Every metadata item is a child `<li class="usa-collection__meta-item">`. The strip is flex-wrapped so items lay out horizontally and wrap onto a second line on narrow widths. Items are separated by built-in horizontal padding (no manual separators or pipes).

Each sub-element class has a specific role:

| Sub-element | Markup | Purpose |
|---|---|---|
| **Author** | `<li class="usa-collection__meta-item">By Office of Communications</li>` | Free-form author or byline. Plain text — no extra class. |
| **Standard date** | `<li class="usa-collection__meta-item"><time datetime="2026-05-12">May 12, 2026</time></li>` | Use `<time>` with `datetime` in ISO 8601 (machine-readable) and human-readable text inside. |
| **Calendar date** | `<div class="usa-collection__calendar-date"><time datetime="2026-07-04"><span class="usa-collection__calendar-date-month">JUL</span><span class="usa-collection__calendar-date-day">04</span></time></div>` | Placed **outside** the meta strip — it sits to the **left** of `usa-collection__body`, replacing the thumbnail. Use for event lists. |
| **Tag (default)** | `<li class="usa-collection__meta-item usa-tag">PMA</li>` | Standard pill: small uppercase text, outlined treatment per USWDS theme. |
| **Tag (new)** | `<li class="usa-collection__meta-item usa-tag usa-tag--new">NEW</li>` | MDWDS override fills the pill: solid `#005ea2` blue background, white text. |
| **Source (headings-only)** | `<p class="usa-collection__meta-item usa-collection__source">...</p>` | Placed **inside** `usa-collection__body`, **outside** the `<ul class="usa-collection__meta">`, for the headings-only variant. Renders a small globe icon plus the source label in gray (#71767a). |

**Important:** the `aria-label="More information"` on the meta `<ul>` is required so screen readers describe the list of metadata items as a unit.

## What each class does

| Class | Effect |
|---|---|
| `usa-collection` | Unstyled `<ul>` (no bullets, no left padding). Vertical container for items. |
| `usa-collection--condensed` | Tightens vertical padding between items for dense lists. |
| `usa-collection__item` | One row in the list. Flex container: left visual (image or calendar) on the left, body on the right. Bottom border `1px solid` USWDS neutral divides items. |
| `usa-collection__img` | Thumbnail image. ~80px square, sits left of the body, vertically aligned top. Has `display: block`. |
| `usa-collection__calendar-date` | Mutually exclusive with `__img`. Small square card on the left showing month abbreviation over day number. Inside it: `<time>` with two `<span>`s for month and day. |
| `usa-collection__calendar-date-month` | Top line: ~0.875rem, semibold, uppercase, color base-dark. |
| `usa-collection__calendar-date-day` | Bottom line: ~1.5rem, bold, color base-darkest. |
| `usa-collection__body` | Right column wrapping heading, description, and meta. `flex: 1` so it consumes remaining width. |
| `usa-collection__heading` | The item title. Source Sans Pro Web semibold, ~17px default. The level of the heading element (`<h2>`–`<h6>`) is set by the `headingLevel` story arg. |
| `usa-collection__description` | Description paragraph below the heading. ~16px, color `text-base-dark`, top margin ~0.5rem. |
| `usa-collection__meta` | Flex-wrapped `<ul>` for metadata pills. `aria-label="More information"` recommended. Horizontal layout with USWDS-tuned spacing. |
| `usa-collection__meta-item` | Each metadata cell. Inline-block / flex item. Includes inherent horizontal spacing between siblings. |
| `usa-collection__source` | Headings-only source line. Small gray (`#71767a`) flex row with a public icon at 1rem. `font-size: 0.93rem`, `gap: 0.25rem`. |
| `usa-tag` | Standard USWDS pill (outlined). Combined with `__meta-item` for tag pills. |
| `usa-tag--new` | MDWDS override: solid `#005ea2` blue background, white text. Use to call out new items. |
| `usa-icon` (inside heading) | External-link icon next to the heading anchor. ~1rem square, vertically centered, ~0.25rem left margin. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `default` \| `condensed` \| `headings-only` | `default` | Collection style |
| `headingLevel` | `h2` \| `h3` \| `h4` \| `h5` \| `h6` | `h4` | Element type used for `usa-collection__heading` — choose to fit page outline |
| `items` | array of item objects | sample news | See item schema below |
| `enableAnalytics` | bool | `false` | Adds `data-ga-*` attributes to each item link |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

### Item schema

Each entry in `items` is an object with these fields:

| Field | Type | Notes |
|---|---|---|
| `title` | string | **Required.** Heading text. |
| `href` | string | **Required.** Link URL. |
| `isExternal` | bool | When true, renders an external-link icon next to the title. |
| `description` | string | Item teaser paragraph (omitted in `headings-only`). |
| `author` | string | E.g., `"Office of the Comptroller"`. Renders as a `__meta-item`. |
| `date` | string | Human-readable, e.g., `"May 12, 2026"`. Pairs with `isoDate`. |
| `isoDate` | string | ISO 8601 for the `datetime` attribute, e.g., `"2026-05-12"`. |
| `calendarDate` | `{ month, day, isoDate }` | Replaces thumbnail. **Mutually exclusive with `media`.** |
| `tags` | `[{ label, isNew? }]` | Array of pill labels. `isNew: true` applies `usa-tag--new`. |
| `media` | `{ src, alt }` | Thumbnail image. **Mutually exclusive with `calendarDate`.** |
| `source` | `{ label, href? }` | Headings-only variant only. Renders the source line with globe icon. |

## Heading level adjustment

`headingLevel` defaults to `h4` in the Storybook template because the docs page already has higher-level headings around it. **In production, pick the level that fits the section's outline** — a collection used as the body of an `<h2>`-led section should typically use `h3`. See `cdn/composition.md` for the hierarchy rule.

## Common mistakes

1. **Inventing a `maryland-collection`** — it doesn't exist. The MDWDS CDN themes `usa-collection` directly; use it as written here.
2. **Putting both a thumbnail and a calendar date on the same item** — they're mutually exclusive and one will visually break the other.
3. **Omitting `aria-label="More information"` on the meta `<ul>`** — screen readers lose the cue that those items belong together as metadata for the item above.
4. **Putting tags outside `usa-collection__meta`** — they lose their inline layout and gain `<li>` bullet markers.
5. **Hard-coding the `<h4>` heading level from the Storybook example** — adjust for the page outline. The component supports `h2`–`h6` directly.
6. **Using a free-form date string without `<time datetime="...">`** — breaks machine-readable date parsing and accessibility.
7. **Using the `headings-only` variant with descriptions or tags** — the headings-only variant suppresses them; the visual will silently drop content. Switch to `condensed` if you want short rows with metadata.
