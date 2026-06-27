# maryland-action-items

The Maryland action-items system is a family of related building blocks for an "action page" (a service hub that helps a Marylander complete a specific task). It is **not a single component** — it's five companion pieces (`maryland-spotlight`, `maryland-featured-actions`, `maryland-action-group`, `maryland-action-resources`, and the action-hero variant of `maryland-hero`) that compose together. They are typically assembled by the `cdn/recipes/action-page.md` recipe; this file documents each piece individually.

> **Use these components together to build a Maryland.gov action / service page.** For a single decorative service tile, use `maryland-card`. For a multi-column featured-links block, use `maryland-highlight`. For step-by-step instructions, use `maryland-step-list`. For an alert/notification, use `maryland-alert`.

## What it looks like

The action page composition stacks vertically:

1. **`maryland-spotlight`** — A Maryland-blue rounded rectangle with a small white-circle-and-lightbulb icon next to an uppercase tracked-out title (e.g., "SPOTLIGHT"). Holds free-form content (headings, paragraphs, lists, links) with white text on blue. 12px outer padding, 36px inner padding, 4px radius, with a 1px `primary-dark` inner border.
2. **`maryland-divider`** — A thin horizontal separator (not documented here; see component-index).
3. **`maryland-action-group`** — A titled section with a 1/2/3-column grid of `maryland-action-item` cards. At desktop, the grid is 3 columns wide (or 2 if the container is 8/12 or narrower).
4. **`maryland-action-item`** — A single action card inside the group: title, optional subtitle, description, optional link.
5. **`maryland-action-resources`** — A two-column (at desktop) block of supplementary links — "Related resources" and "Related agencies" side by side.
6. **`maryland-featured-actions`** — A boxed call-to-action list typically rendered inside an action-hero (right column). White background, 3px Maryland-blue top border, 4px bottom corners, drop shadow. Each link is body-8 (20px) and gets a small arrow icon.
7. **Action-hero** — A specific layout of `maryland-hero--landing-regular.has-image.no-image.action-hero` that places `maryland-featured-actions` in the right column instead of an image. See `cdn/components/maryland-hero.md` for the base hero.

Typography highlights:

- `maryland-action-group__title` uses the `h2` mixin (Merriweather, 32–48px responsive).
- `maryland-action-item__heading` is body-9 semibold (22px) — NOT Merriweather. Render as `<h3>`.
- `maryland-spotlight__title` is uppercase body-7 (18–20px) with `ls(3)` tracking and a leading icon.
- `maryland-action-resources__title` is heading-12 (32px) Merriweather light.
- `maryland-action-resources__group-title` is body-10 (24px) semibold.

## When to use

- `maryland-spotlight` — A single emphasized recommendation at the top of an action page (e.g., "Check eligibility first").
- `maryland-action-group` — The main list of related services on an action page (e.g., 3 different food-assistance programs).
- `maryland-action-resources` — Supplementary related-resources block at the bottom of an action page.
- `maryland-featured-actions` — A small list of top CTAs inside an action-hero or sidebar.

## Markup — maryland-spotlight

```html
<section class="maryland-spotlight" aria-labelledby="sl-1">
  <div class="maryland-spotlight__wrapper">
    <h2 class="maryland-spotlight__title" id="sl-1">Spotlight</h2>
    <div>
      <h3>Check eligibility for food and nutrition benefits</h3>
      <p>Learn about the benefits you may qualify for in just five minutes with the Maryland benefits screener.</p>
      <p><a href="/benefits/screener">Check eligibility now</a></p>

      <h3>SNAP guides for participants</h3>
      <ul>
        <li><a href="/snap/online-shopping">Use SNAP for online grocery shopping</a></li>
        <li>Check out the <a href="/snap/quality">SNAP quality control guide</a></li>
      </ul>
    </div>
  </div>
</section>
```

The leading icon and circle background come from the title's `::before` and `::after` — no markup needed beyond the heading. Children headings inside the wrapper are body-9 semibold (22px), and links are styled white with focus-dark and visited-color logic.

## Markup — maryland-action-group (with action-items)

```html
<section class="maryland-action-group" aria-labelledby="ag-1">
  <h2 class="maryland-action-group__title" id="ag-1">Food and nutrition benefits</h2>
  <p class="maryland-action-group__description">
    Maryland supports healthy starts and good nutrition for residents of all ages.
  </p>
  <ul class="maryland-action-group__list">
    <li class="maryland-action-item">
      <h3 class="maryland-action-item__heading">Food assistance for women and young children</h3>
      <p class="maryland-action-item__subtitle">Women, Infants, and Children (WIC)</p>
      <p class="maryland-action-item__description">
        If you are pregnant, a new mother, or have a child under five, WIC offers nutrition advice, breastfeeding support, and healthy foods.
      </p>
      <a class="maryland-action-item__link" href="/wic">Learn more and make an appointment today</a>
    </li>
    <li class="maryland-action-item">
      <h3 class="maryland-action-item__heading">Food assistance for low-income households</h3>
      <p class="maryland-action-item__subtitle">Supplemental Nutrition Assistance Program (SNAP)</p>
      <p class="maryland-action-item__description">
        SNAP helps low-income households buy the food they need for good health.
      </p>
      <a class="maryland-action-item__link" href="/snap">Find out how to apply for SNAP</a>
    </li>
    <li class="maryland-action-item">
      <h3 class="maryland-action-item__heading">Community meals for seniors</h3>
      <p class="maryland-action-item__description">
        More than 250 places in Maryland serve meals to seniors. Many also host nutrition and health programming.
      </p>
      <a class="maryland-action-item__link" href="/seniors/meals">Find a group near you</a>
    </li>
  </ul>
</section>
```

The group's `<ul>` becomes a 1-/2-/3-column grid based on viewport and container size (see "What each class does" for breakpoints).

## Markup — maryland-action-resources

```html
<section class="maryland-action-resources" aria-labelledby="ar-1">
  <h2 class="maryland-action-resources__title" id="ar-1">Keep learning</h2>
  <p class="maryland-action-resources__description">
    Additional Maryland resources and partner agencies you may find useful.
  </p>
  <div class="maryland-action-resources__groups">
    <div class="maryland-action-resources__group">
      <h3 class="maryland-action-resources__group-title">Related resources</h3>
      <ul>
        <li><a href="/dhs/income">Maryland Income Supports</a></li>
        <li><a href="/health/wic">WIC clinic locator</a></li>
        <li><a href="/snap/eligibility">SNAP eligibility tool</a></li>
        <li><a href="/foodbanks">Find a Maryland food bank</a></li>
      </ul>
    </div>
    <div class="maryland-action-resources__group">
      <h3 class="maryland-action-resources__group-title">Related agencies</h3>
      <ul>
        <li><a href="/dhs">Department of Human Services</a></li>
        <li><a href="/mdh">Maryland Department of Health</a></li>
        <li><a href="/aging">Department of Aging</a></li>
      </ul>
    </div>
  </div>
</section>
```

The `__groups` wrapper becomes a 2-column CSS columns block at desktop+; each group breaks atomically.

## Markup — maryland-featured-actions (standalone)

```html
<div class="maryland-featured-actions">
  <ul class="maryland-featured-actions__list">
    <li class="maryland-featured-actions__item">
      <div>
        <a class="maryland-featured-actions__link" href="/wic">Apply for WIC</a>
      </div>
    </li>
    <li class="maryland-featured-actions__item">
      <div>
        <a class="maryland-featured-actions__link" href="/snap">Apply for SNAP</a>
      </div>
    </li>
    <li class="maryland-featured-actions__item">
      <div>
        <a class="maryland-featured-actions__link" href="/benefits/screener">Check benefits eligibility</a>
      </div>
    </li>
  </ul>
</div>
```

Inside a hero (action-hero variant), the box stretches to 100% width and aligns to the right of the hero content; on mobile it spans the column. Each link has a small forward-arrow icon after the text.

## What each class does

| Class | Effect |
|---|---|
| **Spotlight** | |
| `maryland-spotlight` | Maryland-blue (`primary`) rounded rectangle. 4px outer radius, 12px outer padding. Body-6 (20px) text. Links are inherited color, underlined, focus-dark; visited links go primary-lighter. Headings inside become body-9 semibold (22px) with `text-trim` and 48/16px vertical margin. |
| `maryland-spotlight__wrapper` | Inner border. 1px solid `primary-dark`, 4px radius. 36px padding (mobile), 36/52px at desktop. |
| `maryland-spotlight__title` | The `<h2>`. body-7 (18px) semibold, uppercase, `ls(3)` letter-spacing (~0.7px). Has a white-circle `::before` (48px diameter) and a 32px ink-colored lightbulb-icon `::after` masked into it (rotated 180deg). |
| **Action group** | |
| `maryland-action-group__title` | The `<h2>`. Uses the MDWDS `h2` mixin (Merriweather light, 32 → 40 → 48px). 32px bottom margin. |
| `maryland-action-group__description` | Intro paragraph. body-10 (24px), `base-dark` color, 32px top margin / 64px bottom. |
| `maryland-action-group__list` | The `<ul>`. List-style none. Grid: 1 col (mobile) / 2 col (tablet) / 3 col (desktop), with column count clamped to 2 when container is ≤8/12. Gap 48px (mobile/tablet), 64px (desktop). |
| `maryland-action-item` | A single card. body-6 (20px) text. |
| `maryland-action-item__heading` | Item title (`<h3>`). White background per `set-text-and-bg("white")`. body-9 (22px) semibold, NOT Merriweather. 0/32px vertical margin. |
| `maryland-action-item__subtitle` | Optional smaller title (`<p>`). body-6 (20px) semibold, `base-dark` color. 32/16px vertical margin. |
| `maryland-action-item__description` | Body paragraph. 16px vertical margin. |
| `maryland-action-item__link` | The CTA link. Display block, semibold, with the Maryland typeset-link styling (underlined primary blue, focus outline). 24px top margin. |
| **Action resources** | |
| `maryland-action-resources__title` | Section heading (`<h2>`). Heading-12 (32px) Merriweather light. 32px bottom margin. |
| `maryland-action-resources__description` | Intro paragraph. body-10 (24px). 48px bottom margin. |
| `maryland-action-resources__groups` | Container for the resource groups. At desktop+, becomes a 2-column CSS columns block with 64px column-gap. |
| `maryland-action-resources__group` | Each list block. body-6 text. `break-inside: avoid` inside the columns. 48px bottom margin. |
| `maryland-action-resources__group-title` | Group sub-heading (`<h3>`). body-10 (24px) semibold. 24px bottom margin. |
| **Featured actions** | |
| `maryland-featured-actions` | White background, fit-content width, 3px Maryland-blue top border, 4px bottom corners, drop shadow `0 4px 8px rgba(0,0,0,.15)`. 40px vertical / 16px horizontal padding. Inside a `maryland-hero`, it becomes 100% width and is positioned via `align-self`. |
| `maryland-featured-actions__list` | The `<ul>`. List-style none, zero margin/padding. |
| `maryland-featured-actions__item` | Each `<li>`. Adjacent items get 24px top margin. |
| `maryland-featured-actions__link` | The link. body-8 (20px), display inline-block, with a 20×20px arrow-forward icon appended via `::after`. Uses the Maryland typeset-link styling; on hover, color becomes `$theme-link-color` and underline is removed. |

## Prop schema

The component is split across multiple documented variants — `featuredActions`, `actionSpotlight`, `actionGroup`, `actionResources`, `actionHero` — each with its own args:

| Template | Prop | Type | Default | Notes |
|---|---|---|---|---|
| `actionSpotlight` | `title` | string | `"Spotlight"` | Heading text |
| `actionSpotlight` | `description` | string (HTML) | sample | Free-form HTML content rendered inside the wrapper |
| `actionGroup` | `title` | string | — | Group heading |
| `actionGroup` | `hideTitle` | bool | false | Visually hide title (adds `usa-sr-only`) |
| `actionGroup` | `description` | string | — | Intro paragraph |
| `actionGroup` | `items` | `Array<{title, subtitle?, description, link: {text, url}}>` | sample list | Action items |
| `actionResources` | `title` | string | — | Section heading |
| `actionResources` | `description` | string | — | Intro paragraph |
| `featuredActions` | `items` | `Array<{link: {text, url}}>` | sample list | Featured-action links |
| `actionHero` | `title` | string | — | Hero title |
| `actionHero` | `description` | string | — | Hero description |
| `actionHero` | `items` | featured-action items | — | Inline `maryland-featured-actions` content |
| `actionHero` | `showFeaturedItems` | bool | true | Toggle the featured-actions column |

## Heading level adjustment

Action-page components default to:

- `maryland-spotlight__title` → `<h2>`
- `maryland-action-group__title` → `<h2>`
- `maryland-action-item__heading` → `<h3>`
- `maryland-action-resources__title` → `<h2>`
- `maryland-action-resources__group-title` → `<h3>`

When the page hero already supplies the `<h1>`, these defaults give the correct outline. If you compose them inside an already-`<h2>`-led wrapper section, demote each by one level. Keep the class — it controls styling.

## Common mistakes

1. **Treating `maryland-action-items` as a single component** — it isn't. Pick the specific sub-component (`spotlight`, `action-group`, `action-resources`, etc.) you need.
2. **Putting more than ~6 items in a single `maryland-action-group`** — the grid is built for 3–6. For longer lists, use `maryland-link-collection` or paginate.
3. **Using Merriweather mixin on `maryland-action-item__heading`** — it's Source Sans semibold by design. Overriding it breaks the visual hierarchy with the group title.
4. **Linking inside `maryland-action-item` with a plain `<a>`** — use `maryland-action-item__link` so the link gets the design system's focus + underline styles.
5. **Forgetting `aria-labelledby` on each `<section>`** — every action sub-component has a heading and should use `aria-labelledby` to bind it to the section landmark.
6. **Using `maryland-featured-actions` for a long list** — it's designed for 3–5 top CTAs. For longer lists, use a `maryland-link-collection` or `maryland-highlight`.
7. **Replacing the spotlight icon with inline SVG** — the lightbulb is built from `::before` + `::after` on the title. Adding a custom icon breaks layout.
