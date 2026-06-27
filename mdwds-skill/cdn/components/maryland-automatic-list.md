# maryland-automatic-list

Maryland Design System automatic list is a CMS-driven list of Maryland-card items that adapts based on a `contentType` switch — `news`, `event`, `document`, `location`, or `contact`. The Drupal/CMS layer picks the content type; the component then applies the right card variant, image format, and per-item metadata layout for each type.

> **Use `maryland-automatic-list` for CMS-generated lists of recurring content (news, events, locations, etc.) where the editor selects a content type rather than configuring each card.** For a hand-curated set of feature tiles, use `maryland-visual-link-collection`. For a flat list of plain links, use `maryland-link-collection`. For the standalone card primitive, use `maryland-card-group`.

## What it looks like

The component is structurally similar to `maryland-visual-link-collection`: a `<section>` with a `maryland-card-group__header` and a `<ul class="maryland-card-group">`. The difference is in how each item is rendered:

- **`news`** — `linked` cards with landscape image, formatted date above the heading, optional description.
- **`event`** — `linked` cards with eyebrow (event type — "Webinar", "Workshop"), heading, then a date row below.
- **`document`** — `linked` cards with eyebrow (document category), `documentTitle` (title + " — PDF 64.56KB" smaller suffix), and a `download` footer icon.
- **`location`** — `linked` cards with heading + `<address>` description (line breaks rendered as `<br>`).
- **`contact`** — `full` cards (not linked): portrait image, clickable heading, subheading (role), then a body with labelled links (`Email | …`, `Phone | …`) using `maryland-link--labelled`.

The card variant (`linked` vs `full`) and the image format (`landscape` vs `portrait`) are set per content type, not per item.

## When to use

- Driving the body of a listing page (news index, events calendar, document library) where the editor only chooses content type + how many items.
- "Recent news" / "Upcoming events" / "Featured locations" feeds on agency homepages.
- Staff directory grids.

For a single static set of items where each card needs its own bespoke configuration, prefer `maryland-card-group` or `maryland-visual-link-collection`.

## Default markup — news (linked, landscape)

```html
<section class="maryland-automatic-list" aria-labelledby="al-1">
  <div class="maryland-card-group__header">
    <div class="maryland-card-group__header-content">
      <h2 id="al-1" class="maryland-card-group__title">Featured news</h2>
      <p class="maryland-card-group__description">The latest from Maryland state government.</p>
    </div>
    <div class="maryland-card-group__more-link">
      <a class="maryland-link" href="/news">See all news</a>
    </div>
  </div>
  <ul class="maryland-card-group">
    <li class="maryland-card maryland-card--linked">
      <a href="/news/microsoft-quantum" class="maryland-card__link" aria-label="Governor Moore announces Microsoft Quantum Research Center">
        <div class="maryland-card__container">
          <div class="maryland-card__media">
            <div class="maryland-card__img">
              <img src="/img/quantum.jpg" alt="Quantum research facility" />
            </div>
          </div>
          <div class="maryland-card__header">
            <div class="maryland-card__date">October 25, 2026</div>
            <h3 class="maryland-card__heading">Governor Moore announces Microsoft Quantum Research Center</h3>
          </div>
          <div class="maryland-card__body">
            <p>The University of Maryland Discovery District will host the new center.</p>
          </div>
          <div class="maryland-card__footer maryland-card__footer--right">
            <span class="maryland-card__icon maryland-card__icon--arrow" aria-hidden="true"></span>
          </div>
        </div>
      </a>
    </li>
    <!-- Repeat for additional news items -->
  </ul>
</section>
```

## Markup — events (linked, landscape, with eyebrow + date)

```html
<li class="maryland-card maryland-card--linked">
  <a href="/events/community-garden" class="maryland-card__link" aria-label="Learn how to join a community garden">
    <div class="maryland-card__container">
      <div class="maryland-card__header">
        <span class="maryland-card__eyebrow">Webinar</span>
        <h3 class="maryland-card__heading">Learn how to join a community garden</h3>
        <div class="maryland-card__date">Thursday, October 23, 2026 5:00 p.m. to 7:00 p.m.</div>
      </div>
      <div class="maryland-card__footer maryland-card__footer--right">
        <span class="maryland-card__icon maryland-card__icon--arrow" aria-hidden="true"></span>
      </div>
    </div>
  </a>
</li>
```

## Markup — documents (linked, with download icon)

```html
<li class="maryland-card maryland-card--linked">
  <a href="/documents/annual-report-2026.pdf" class="maryland-card__link" download aria-label="Annual Report - PDF 64.56KB">
    <div class="maryland-card__container">
      <div class="maryland-card__header">
        <span class="maryland-card__eyebrow">Annual Report</span>
        <h3 class="maryland-card__heading">
          <span class="maryland-link__document-title">FY2026 Annual Report</span>
          <span class="maryland-link__document-divider"> - </span>
          <span class="maryland-link__document-format-size">PDF 64.56KB</span>
        </h3>
      </div>
      <div class="maryland-card__footer maryland-card__footer--right">
        <span class="maryland-card__icon maryland-card__icon--download" aria-hidden="true"></span>
      </div>
    </div>
  </a>
</li>
```

## Markup — locations (linked, with `<address>`)

```html
<li class="maryland-card maryland-card--linked">
  <a href="/locations/state-house" class="maryland-card__link" aria-label="State House - 100 State Circle, Annapolis, MD 21401">
    <div class="maryland-card__container">
      <div class="maryland-card__header">
        <h3 class="maryland-card__heading">Maryland State House</h3>
      </div>
      <div class="maryland-card__body">
        <address>
          100 State Circle<br>
          Annapolis, MD 21401
        </address>
      </div>
      <div class="maryland-card__footer maryland-card__footer--right">
        <span class="maryland-card__icon maryland-card__icon--arrow" aria-hidden="true"></span>
      </div>
    </div>
  </a>
</li>
```

## Markup — contact (full variant, portrait, labelled links)

```html
<li class="maryland-card maryland-card--full">
  <div class="maryland-card__container">
    <div class="maryland-card__media">
      <div class="maryland-card__img maryland-card__img--portrait">
        <img src="/img/elizabeth.jpg" alt="Photo of Dr. Elizabeth Hughs" />
      </div>
    </div>
    <div class="maryland-card__header">
      <a class="maryland-link" href="/staff/elizabeth-hughs">
        <h3 class="maryland-card__heading">Dr. Elizabeth Mary Hughs, PhD</h3>
      </a>
      <p class="maryland-card__subheading">Director, State Historic Preservation Officer</p>
    </div>
    <div class="maryland-card__body">
      <div class="maryland-link--labelled">
        <span class="maryland-link__label" id="ll-email-1">Email</span>
        <a class="maryland-link" href="mailto:elizabeth.hughs@maryland.gov" aria-describedby="ll-email-1">elizabeth.hughs@maryland.gov</a>
      </div>
      <div class="maryland-link--labelled">
        <span class="maryland-link__label" id="ll-phone-1">Phone</span>
        <a class="maryland-link" href="tel:4106979556" aria-describedby="ll-phone-1">410-697-9556</a>
      </div>
    </div>
  </div>
</li>
```

## What each class does

| Class | Effect |
|---|---|
| `maryland-automatic-list` | Base `<section>`. Applies `block-spacing` and `grid-container`. The content-type logic lives in the component runtime; the CSS is a thin wrapper that defers all visual behavior to `maryland-card` and `maryland-card-group`. |
| `maryland-card-group__header` and its children | Header block. See `maryland-visual-link-collection.md` and `maryland-card.md`. |
| `maryland-card-group` | The `<ul>` grid. |
| `maryland-card`, `maryland-card--linked` / `--full` | The card variants used per content type. See `cdn/components/maryland-card.md` for the full class reference. |
| `maryland-card__eyebrow` | Small uppercase category label above the heading (events, documents). |
| `maryland-card__date` | Date metadata. For news, sits between media and heading (with link wrapping). For events, sits below the heading. |
| `maryland-link__document-title` / `__document-divider` / `__document-format-size` | Document title typography parts. Body font, semibold, with a smaller suffix for format/size. |
| `maryland-link--labelled` / `__label` | Labelled link pair (used in contact variant): `<div>` wrapping a `<span class="maryland-link__label">` (with an `id`) and an `<a class="maryland-link">` (with matching `aria-describedby` so screen readers announce the label before the value). |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `contentType` | `news` \| `event` \| `document` \| `location` \| `contact` | `news` | Picks card variant, image format, sample items, and per-item layout. |
| `variant` | `linked` \| `full` | (derived from `contentType`) | Card variant. Set automatically. |
| `imageFormat` | `landscape` \| `portrait` | (derived from `contentType`) | Aspect ratio for images. |
| `title` | string | (per content type) | Section heading. |
| `description` | string | — | Section description. |
| `moreLinkText` / `moreLinkUrl` | string | — | "More" link. |
| `items` | per content-type schema | — | Item list. |
| `listItems` | 3–9 | 6 | Number of items to render. |
| `enableAnalytics` / `gaCategory` | bool / string | — | GA tracking. |

## Heading level adjustment

`maryland-card-group__title` defaults to `<h2>`; each `maryland-card__heading` defaults to `<h3>`. Demote both by one level when nested under an existing `<h2>` section.

## Common mistakes

1. **Hard-coding a content type's markup when a different type was intended** — pick the content type that matches the data; don't graft news markup onto location data.
2. **Mixing card variants in a single automatic list** — the contract is one variant per list. Mixing breaks the visual rhythm.
3. **Forgetting the `download` attribute on document items** — combine `iconType: "download"` with the `download` HTML attribute and an accessible-label suffix.
4. **Skipping the `<address>` semantic for location addresses** — the location variant intentionally uses `<address>`. Replacing with `<p>` loses semantics.
5. **Putting plain `<a>` links inside the `contact` variant body instead of labelled-link markup** — the labelled-link spans give the "Email"/"Phone" label its own typography and screen-reader pairing.
6. **Wrapping in another `grid-container`** — already applied. Don't double-wrap.
