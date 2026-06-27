# maryland-highlight

Maryland Design System highlight is a 1-, 2-, or 3-column block of featured links. Each column has its own optional sub-title and description, up to five borderless link rows with hover arrow animation, and an optional "more" link below. It's the most common "featured services" block on Maryland agency pages.

> **Use `maryland-highlight` for grouped, scannable featured links — typically 2 or 3 columns of services on a homepage.** For one promotional CTA, use `maryland-promo`. For a list of related links without column structure, use `maryland-link-collection`. For a card layout with images and buttons, use `maryland-card`.

## What it looks like

A highlight is a `<section>` with:

- An optional section heading (`<h2>`, Merriweather, 32–48px) and optional description (16–24px responsive).
- A 12-column grid below: each column takes 12/12 on mobile, 6/12 at tablet (640px), and `fill` (auto-distributed) at desktop-lg (1200px). So 3-column layouts become 4/4/4, 2-column layouts become 6/6, single columns are full width.

Within each column:

- Column title — Source Sans semibold (not Merriweather), 18–24px. Renders as `<h3>`.
- Column description — body text, 19.2px (mobile) → 22px (mobile-lg+).
- Link list — borderless rows separated by 1px `gray-40` horizontal lines. Each row is a flex `space-between` between the link text (left) and a 20px square arrow icon (right). On hover/focus, the bottom border thickens to 2px Maryland blue and the arrow slides right 12px while turning blue.
- "More" link — 16/18px body text, semibold, primary blue, underlined. 56px bottom margin (mobile) / 64px (mobile-lg+).

Icon options for link rows: default (`arrow_forward`), `external` (`open_in_new`), `download` (`download`). External links get `target="_blank"` and accessible-label suffix; download links get `download` attribute and similar suffix.

## When to use

- Three columns of categorized featured services on an agency homepage ("Benefits | Services | Business").
- Two columns of "Frequently visited" links on a topic landing page.
- A single column of priority links on a narrow sidebar layout (rare — usually a `maryland-card-group` works better).

## Default markup (3 columns)

```html
<section class="maryland-highlight" aria-labelledby="hl-title">
  <h2 class="maryland-highlight__section-title" id="hl-title">Benefits, services, and business</h2>
  <p class="maryland-highlight__section-description">Find the right information in these featured areas.</p>
  <div class="maryland-highlight__grid">
    <div class="maryland-highlight__item">
      <h3 class="maryland-highlight__title">Benefits</h3>
      <ul class="maryland-highlight__links">
        <li>
          <a href="/health" class="maryland-highlight__link">
            <span class="maryland-highlight__link-text">Health and medical</span>
            <span class="maryland-highlight__link-icon" aria-hidden="true"></span>
          </a>
        </li>
        <li>
          <a href="/unemployment" class="maryland-highlight__link">
            <span class="maryland-highlight__link-text">Unemployment and jobs</span>
            <span class="maryland-highlight__link-icon" aria-hidden="true"></span>
          </a>
        </li>
        <li>
          <a href="/benefits.pdf" download class="maryland-highlight__link" aria-label="Download benefits guide (download)">
            <span class="maryland-highlight__link-text">Download benefits guide (PDF)</span>
            <span class="maryland-highlight__link-icon maryland-highlight__link-icon--download" aria-hidden="true"></span>
          </a>
        </li>
      </ul>
      <a href="/benefits" class="maryland-highlight__more-link">More benefits</a>
    </div>
    <div class="maryland-highlight__item">
      <h3 class="maryland-highlight__title">Services</h3>
      <ul class="maryland-highlight__links">
        <li>
          <a href="/transportation" class="maryland-highlight__link">
            <span class="maryland-highlight__link-text">Driving and transportation</span>
            <span class="maryland-highlight__link-icon" aria-hidden="true"></span>
          </a>
        </li>
        <li>
          <a href="/parks" class="maryland-highlight__link">
            <span class="maryland-highlight__link-text">Recreation licenses and permits</span>
            <span class="maryland-highlight__link-icon" aria-hidden="true"></span>
          </a>
        </li>
        <li>
          <a href="https://ed.gov" target="_blank" rel="noopener noreferrer" class="maryland-highlight__link" aria-label="Federal education resources (opens in new window)">
            <span class="maryland-highlight__link-text">Federal education resources</span>
            <span class="maryland-highlight__link-icon maryland-highlight__link-icon--external" aria-hidden="true"></span>
          </a>
        </li>
      </ul>
      <a href="/services" class="maryland-highlight__more-link">More services</a>
    </div>
    <div class="maryland-highlight__item">
      <h3 class="maryland-highlight__title">Business and work</h3>
      <ul class="maryland-highlight__links">
        <li>
          <a href="/licenses" class="maryland-highlight__link">
            <span class="maryland-highlight__link-text">Licenses and permits for professionals</span>
            <span class="maryland-highlight__link-icon" aria-hidden="true"></span>
          </a>
        </li>
        <li>
          <a href="/business" class="maryland-highlight__link">
            <span class="maryland-highlight__link-text">Doing business in Maryland</span>
            <span class="maryland-highlight__link-icon" aria-hidden="true"></span>
          </a>
        </li>
      </ul>
      <a href="/business" class="maryland-highlight__more-link">More business and work</a>
    </div>
  </div>
</section>
```

## Markup — 2 columns

Same structure, only two `maryland-highlight__item` blocks inside the grid. At tablet+, each takes 6/12.

## Markup — single column

```html
<section class="maryland-highlight" aria-labelledby="hl-single">
  <h2 class="maryland-highlight__section-title" id="hl-single">Apply for unemployment</h2>
  <div class="maryland-highlight__grid">
    <div class="maryland-highlight__item">
      <ul class="maryland-highlight__links">
        <li>
          <a href="/apply" class="maryland-highlight__link">
            <span class="maryland-highlight__link-text">Start a new claim</span>
            <span class="maryland-highlight__link-icon" aria-hidden="true"></span>
          </a>
        </li>
        <li>
          <a href="/file" class="maryland-highlight__link">
            <span class="maryland-highlight__link-text">File a weekly certification</span>
            <span class="maryland-highlight__link-icon" aria-hidden="true"></span>
          </a>
        </li>
      </ul>
    </div>
  </div>
</section>
```

`:only-child` rule promotes a single item to 12/12 at tablet+.

## What each class does

| Class | Effect |
|---|---|
| `maryland-highlight` | Base `<section>`. Applies `block-spacing` and `grid-container`. |
| `maryland-highlight__section-title` | Optional `<h2>`. Uses the MDWDS `h2` mixin (Merriweather light, 32/40/48px). 16px bottom margin. |
| `maryland-highlight__section-description` | Optional section intro paragraph. 16 → 22 → 24px. 24/24/40px bottom margin. Color `base-darkest`. |
| `maryland-highlight__grid` | The 12-column grid row. Applies USWDS `grid-row` + `grid-gap(8)` (64px gap). |
| `maryland-highlight__item` | A column. 12/12 (mobile), 6/12 (tablet), fill (desktop-lg). Sole-child gets 12/12 at tablet. |
| `maryland-highlight__title` | Column sub-heading (`<h3>`). Source Sans semibold, 18px (mobile) → 24px (mobile-lg+). 16/24px bottom margin. **Not** Merriweather. |
| `maryland-highlight__description` | Optional per-column description. Body text 19.2/22px responsive. 16/24px bottom margin. |
| `maryland-highlight__links` | `<ul>` of link rows. List style none, no padding. First link gets a 1px `gray-40` top border (so all rows are visually separated). |
| `maryland-highlight__link` | Each row's `<a>`. Display flex space-between, vertically centered. 20/16/20/0 padding. Text color `base-darkest`. 1px `gray-40` bottom border. On hover/focus, the border becomes 2px Maryland blue and the icon translates 12px right and recolors to Maryland blue. |
| `maryland-highlight__link-text` | The link label span. Applies the `text-trim` mixin to remove inherited line-height bumps. |
| `maryland-highlight__link-icon` | The right-side icon. 20px square, Material Symbols `arrow_forward` mask, `base-darkest` background. Transitions on transform with 0.2s ease. |
| `maryland-highlight__link-icon--external` | Swaps mask to `open_in_new`. Pair with `target="_blank"` and accessible-label suffix. |
| `maryland-highlight__link-icon--download` | Swaps mask to `download`. Pair with `download` attribute and accessible-label suffix. |
| `maryland-highlight__more-link` | The bottom "more" link. Body-5 (16px) / body-7 (20px) at mobile-lg+, semibold, underlined, primary color. 56/64px bottom margin to separate from the next column or section. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `title` | string | — | Section heading. Optional. |
| `description` | string | — | Section description. Optional. |
| `columnCount` | `1` \| `2` \| `3` | `3` | Number of columns rendered. |
| `col1Title` … `col3Title` | string | — | Column sub-headings. |
| `col1Description` … `col3Description` | string | — | Per-column descriptions. |
| `col{N}Link{1-5}Text` | string | — | Link label. |
| `col{N}Link{1-5}Url` | string | — | Link URL. Both text and URL must be set for the link to render. |
| `col{N}Link{1-5}IconType` | `""` \| `external` \| `download` | `""` | Icon style. External links get `target="_blank" rel="noopener noreferrer"`; downloads get the `download` attribute. |
| `col{N}MoreText` | string | — | More-link label. |
| `col{N}MoreUrl` | string | — | More-link URL. |

## Heading level adjustment

- `maryland-highlight__section-title` defaults to `<h2>`.
- `maryland-highlight__title` (column sub-headings) defaults to `<h3>`.

If the highlight is nested under a section that already uses `<h2>`, promote the section title to `<h3>` and the column titles to `<h4>`. Keep the classes — they control styling, not outline.

## Common mistakes

1. **Wrapping the highlight in another `grid-container`** — it already applies `grid-container` via `maryland-highlight`. Double-wrapping introduces extra padding.
2. **Forgetting `aria-hidden="true"` on the icon `<span>`** — the icon is decorative; without `aria-hidden`, screen readers may try to announce the empty span.
3. **Mismatching `iconType` and link attributes** — `external` icon without `target="_blank"` (or `download` icon without `download` attribute) is inconsistent. In hand-written markup, set the matching attribute alongside the icon class.
4. **Using `<h4>` for column titles when the section has no `<h2>`** — the column title needs to be the right level for the page outline. Default `<h3>` only works when the section has an `<h2>`.
5. **Skipping the `<ul>` wrapper around link rows** — the borders, hover behavior, and padding all rely on `.maryland-highlight__links` being a `<ul>` with the right class. Loose `<a>` elements won't pick up the styling.
6. **More than 5 links per column** — design constraint; if you have more, use a `maryland-link-collection` below the highlight or split into two columns.
7. **Inline `<style>` to change the arrow color** — colors come from the design system. If the arrow needs to be different, you're using the wrong component.
