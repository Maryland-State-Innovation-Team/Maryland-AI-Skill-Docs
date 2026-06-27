# maryland-card

Maryland Design System cards group related information in a visually distinct container. Designed for service cards, news items, events, and featured content on Maryland.gov pages.

> **Use this, not `usa-card`, on Maryland-branded pages.** The two components have different markup and visual style. See `cdn/components/usa-card.md` for the USWDS equivalent and `cdn/component-index.md` for the disambiguation table.

## What it looks like

A `maryland-card` is a white-background rectangular block with an optional image, a heading (Merriweather, light weight at h3 size), an optional subheading and body text, and a footer holding either a call-to-action button or an icon-only link. Cards typically appear in groups of 2–4 inside a `maryland-card-group` (`<ul>`), which lays them out responsively: a single column on mobile, multi-column on tablet+.

The default visual is clean and neutral — square corners (no border radius), no card border, body text in dark gray on white. The primary button is Maryland blue with white text. Each variant changes a different aspect of the layout — see below.

## Variants

Set `variant` to one of: `simple`, `media`, `full`, `flag`, `linked`.

| Variant | Visual |
|---|---|
| `simple` | Heading + body + button. No image. The "default" card. |
| `media` | Image on top (or bottom, via `mediaPlacement: "second"`), then heading, body, button. Image is full-width within the card. |
| `full` | Like `media`, but with a clickable heading link and support for a subheading, link list, an inline icon next to the button, and a "more link" below. The richest layout. |
| `flag` | Image on the left (or right via `mediaPlacement: "second"`), text on the other side. Horizontal layout above the `tablet` breakpoint; stacks on mobile. |
| `linked` | The entire card is a single `<a>`. No button — instead, an arrow/external/download icon sits in the footer and slides right on hover. Hover also darkens the footer's bottom border to Maryland blue. No internal links allowed (accessibility: nested anchors forbidden). |

## When to use which variant

- **`simple`** → Quick service tile or info block where an image would be distracting.
- **`media`** → Most common for service tiles with hero imagery.
- **`full`** → Press releases, multi-link service hubs, anything needing subheading + supporting links.
- **`flag`** → Featured-item layouts where horizontal emphasis is desirable (e.g., a single highlighted item between rows of `media` cards).
- **`linked`** → Maximum clickable area; best for short-titled tile grids ("Apply for a license", "Find a park").

## Default markup (simple variant)

```html
<ul class="maryland-card-group">
  <li class="maryland-card maryland-card--simple">
    <div class="maryland-card__container">
      <div class="maryland-card__header">
        <h3 class="maryland-card__heading">Apply for a fishing license</h3>
      </div>
      <div class="maryland-card__body">
        <p>Recreational fishing licenses are available online or at any DNR Service Center.</p>
      </div>
      <div class="maryland-card__footer maryland-card__footer--left">
        <div class="maryland-card__footer-content">
          <a href="#" class="usa-button usa-button--primary">Apply now</a>
        </div>
      </div>
    </div>
  </li>
  <!-- Repeat for additional cards -->
</ul>
```

**Important:** Cards are `<li>` elements. The wrapping `<ul class="maryland-card-group">` is required — it handles the responsive grid and removes default list styling.

## Markup — media variant

```html
<ul class="maryland-card-group">
  <li class="maryland-card maryland-card--media">
    <div class="maryland-card__container">
      <div class="maryland-card__media">
        <div class="maryland-card__img">
          <img src="/img/park.jpg" alt="Forest trail in Patapsco Valley State Park" />
        </div>
      </div>
      <div class="maryland-card__header">
        <h3 class="maryland-card__heading">Find a state park</h3>
      </div>
      <div class="maryland-card__body">
        <p>Explore Maryland's 76 state parks and forests.</p>
      </div>
      <div class="maryland-card__footer maryland-card__footer--left">
        <div class="maryland-card__footer-content">
          <a href="#" class="usa-button usa-button--primary">Find parks</a>
        </div>
      </div>
    </div>
  </li>
</ul>
```

Image dimensions: landscape default ~432×325; portrait (`maryland-card__img--portrait`) ~218×290 (3:4 aspect ratio).

To reverse image/header order (image *below* heading), add `maryland-card--header-first` to the `<li>`.

## Markup — full variant

```html
<ul class="maryland-card-group">
  <li class="maryland-card maryland-card--full">
    <div class="maryland-card__container">
      <div class="maryland-card__media">
        <div class="maryland-card__img">
          <img src="/img/news.jpg" alt="Press conference at the State House" />
        </div>
      </div>
      <div class="maryland-card__header">
        <a class="maryland-link" href="/news/full-story">
          <h3 class="maryland-card__heading">Governor announces new program</h3>
        </a>
        <p class="maryland-card__subheading">Released March 12, 2026</p>
      </div>
      <div class="maryland-card__body">
        <p>The new initiative will provide grants to small businesses across the state.</p>
        <!-- Optional link list -->
        <div class="maryland-card__link-list">
          <h4 class="maryland-card__link-list-heading">Related</h4>
          <ul class="usa-list usa-list--unstyled">
            <li class="link-list-item">
              <a class="maryland-link" href="#">Read the full announcement</a>
            </li>
          </ul>
        </div>
      </div>
      <div class="maryland-card__footer maryland-card__footer--left">
        <div class="maryland-card__footer-content">
          <a href="/news/full-story" class="usa-button usa-button--primary">Read more</a>
          <a href="/news" class="maryland-card__more-link">All news</a>
        </div>
      </div>
    </div>
  </li>
</ul>
```

## Markup — flag variant

```html
<ul class="maryland-card-group">
  <li class="maryland-card maryland-card--flag">
    <div class="maryland-card__container">
      <div class="maryland-card__media">
        <div class="maryland-card__img">
          <img src="/img/featured.jpg" alt="..." />
        </div>
      </div>
      <div class="maryland-card__header">
        <h3 class="maryland-card__heading">Featured initiative</h3>
      </div>
      <div class="maryland-card__body">
        <p>Image left, text right (or vice versa with `maryland-card--media-right`).</p>
      </div>
      <div class="maryland-card__footer maryland-card__footer--left">
        <div class="maryland-card__footer-content">
          <a href="#" class="usa-button usa-button--primary">Learn more</a>
        </div>
      </div>
    </div>
  </li>
</ul>
```

For image on the right instead: add `maryland-card--media-right` to the `<li>`.

## Markup — linked variant

```html
<ul class="maryland-card-group">
  <li class="maryland-card maryland-card--linked">
    <a href="/parks" class="maryland-card__link" aria-label="Find a state park - 76 parks across Maryland">
      <div class="maryland-card__container">
        <div class="maryland-card__media">
          <div class="maryland-card__img">
            <img src="/img/park.jpg" alt="" />
          </div>
        </div>
        <div class="maryland-card__header">
          <h3 class="maryland-card__heading">Find a state park</h3>
        </div>
        <div class="maryland-card__body">
          <p>76 parks across Maryland.</p>
        </div>
        <div class="maryland-card__footer maryland-card__footer--right">
          <span class="maryland-card__icon maryland-card__icon--arrow" aria-hidden="true"></span>
        </div>
      </div>
    </a>
  </li>
</ul>
```

Icon options: `maryland-card__icon--arrow` (default, forward arrow), `maryland-card__icon--external-link` (open-in-new), `maryland-card__icon--download` (down arrow). On hover, the icon slides ~12px to the right and turns Maryland blue (`color: blue-60v`); the footer's bottom border also turns blue and thickens to 3px.

**Constraints:** no nested `<a>` elements inside a linked card (accessibility). The `aria-label` on the wrapping `<a>` should combine title + body for screen-reader context.

## What each class does

| Class | Effect |
|---|---|
| `maryland-card-group` | Flex/grid container for a list of cards. Removes list bullets and margins, applies vertical stacking on mobile, multi-column grid on tablet+. **Required wrapper.** |
| `maryland-card` | Base card class. Applied to each `<li>`. By itself, applies `margin-bottom` for vertical spacing between cards (~24px+) and sets `max-width: none` to override `usa-prose` constraints. |
| `maryland-card--simple` | Marker class for the simple variant; no visual effect on its own but used by other rules. |
| `maryland-card--media` | Enables top-of-card image rendering. |
| `maryland-card--full` | Enables clickable heading, subheading, link list, more-link, and inline button icon. |
| `maryland-card--flag` | Horizontal layout: image and content side-by-side at `tablet` breakpoint (≥640px). Stacks on mobile. |
| `maryland-card--linked` | Entire card becomes one `<a>`. Hover effects on icon + footer border. |
| `maryland-card--header-first` | For `media`, `full`, `linked` variants: places header above the image (default is image above header). |
| `maryland-card--media-right` | For `flag` variant: image on the right instead of left. |
| `maryland-card__container` | White background, full-height flex column. **Borders removed** (MDWDS overrides USWDS card border). The inner box that holds header/body/footer. |
| `maryland-card__media` | Image wrapper. Becomes `order: first` in the flex container by default. |
| `maryland-card__media--inset` | Adds horizontal padding so image is inset from card edges. |
| `maryland-card__media--exdent` | Negative horizontal margin — image extends beyond card edges (used in flush layouts). |
| `maryland-card__img` | Image wrapper. **Removes border-radius** (cards have square corners). |
| `maryland-card__img--portrait` | 3:4 aspect ratio, max-width ~216px. Forces portrait orientation. |
| `maryland-card__header` | Top section containing heading + subheading. Has perimeter padding (~24px) and reduced bottom padding (~12px). When no media is present, top padding is removed. |
| `maryland-card__eyebrow` | Small uppercase label above the heading (e.g., "ANNOUNCEMENT"). 14px, semibold, letter-spacing ~2px, color `base-dark`. |
| `maryland-card__heading` | Card title. Default is `<h3>` element styled per variant: full = Source Sans 18px semibold, linked = Source Sans 16px semibold (mobile) / 22px (mobile-lg+). **Adjust heading level** to match page outline — see `cdn/composition.md`. |
| `maryland-card__subheading` | Smaller text below heading. ~16px, ~5 line-height. |
| `maryland-card__date` | Date metadata. 16px semibold, color `base-darkest`. |
| `maryland-card__body` | Body content area. ~16px text, top margin ~24px from heading. |
| `maryland-card__link-list` | Container for a list of related links inside the body. |
| `maryland-card__link-list-heading` | Small heading for the link list (e.g., "Related"). |
| `maryland-card__footer` | Footer with the button/icon. Top padding ~16px. |
| `maryland-card__footer--left` / `--center` / `--right` | Horizontal alignment of footer content. |
| `maryland-card__footer-content` | Flex column wrapper for footer items. Vertical gap ~8px. |
| `maryland-card__more-link` | "More link" below the primary button. Small body-sm font size (~14px). |
| `maryland-card__icon` | Icon-only footer link (linked variant). 18.75px square mask-based icon, color `base-darkest`. Slides right on hover. |
| `maryland-card__icon--arrow` / `--external-link` / `--download` | Icon glyph (Material Symbols: arrow_forward, open_in_new, download). |
| `maryland-card__link` | Used inside linked variant — applied to the wrapping `<a>`. Removes underline, inherits color, applies 4px outline on focus, hover effects on internal icon and footer. |
| `maryland-card__button` | Secondary button-shaped wrapper around the inline icon (in full variant with `useIcon: true`). |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `simple` \| `media` \| `full` \| `flag` \| `linked` | `simple` | Card style |
| `title` | string | `"Maryland Card Title"` | Heading text |
| `subheading` | string | `""` | Optional subheading (full variant) |
| `body` | string | sample text | Body paragraph |
| `buttonText` | string | `"More Link"` | Primary button label |
| `buttonUrl` | string | `"#"` | Button href |
| `cardCount` | number | `6` | Number of cards rendered in the documented variants |
| `mediaPlacement` | `first` \| `second` | `first` | Where the image sits relative to header |
| `mediaStyle` | `default` \| `inset` \| `exdent` | `default` | How the image bleeds within the card |
| `imageUrl` | string | placeholder | Image src |
| `imageAlt` | string | placeholder | Image alt text |
| `imageFormat` | `landscape` \| `portrait` | `landscape` | Aspect ratio |
| `useIcon` | bool | `false` | Show icon instead of button (linked variant; or alongside button in full/media) |
| `iconType` | `arrow` \| `external-link` \| `download` | `arrow` | Icon glyph |
| `linkList` | array | `[]` | List of related links: `[{label?, text, url}]`. `label` makes it a "labelled" link with description. Not available in `linked` variant. |
| `footerAlignment` | `left` \| `center` \| `right` | `left` | Footer content alignment |
| `moreLinkText` | string | `""` | Optional "more link" below button |
| `moreLinkUrl` | string | `""` | URL for the more link |
| `enableAnalytics` | bool | `false` | Add `data-ga-*` attributes |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

## Heading level adjustment

MDWDS defaults `maryland-card__heading` to `<h3>` because cards usually live under an `<h2>` section. **If the card group is itself a top-level section, use `<h2>`.** If cards are nested deeper (e.g. inside a `<details>` block under an `<h2>` and `<h3>`), use `<h4>`. See `cdn/composition.md` for the hierarchy rule.

## Common mistakes

1. **Forgetting `<ul class="maryland-card-group">`** — without it, cards lose their list reset, layout, and spacing. Cards rendered alone look broken.
2. **Using `usa-card` markup with `maryland-card` classes (or vice versa)** — they're different components with different DOM structure. Pick one.
3. **Nested links inside `maryland-card--linked`** — accessibility violation. The linked variant doesn't support `linkList` or any internal `<a>`.
4. **Wrapping cards in `grid-col-*`** — the `maryland-card-group` handles columns. Don't add your own grid columns around individual cards.
5. **Copying the `<h3>` heading level blindly** — adjust to fit page outline (see "Heading level adjustment" above).
6. **Inline `<style>` to add a border or shadow** — the design system has no card border by deliberate decision. If you need separation, use `block-spacing` between groups, not custom CSS.
