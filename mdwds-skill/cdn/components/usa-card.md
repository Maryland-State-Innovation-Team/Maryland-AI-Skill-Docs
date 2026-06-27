# usa-card

The plain USWDS card component: a container with header, optional media, body, and footer. Wrapped in a `usa-card-group` for responsive grid layout.

> **Prefer `maryland-card` on Maryland.gov pages.** `usa-card` and `maryland-card` are different components with **different class namespaces, different DOM structure, and different visual style**. The Maryland Design System ships `maryland-card` as the canonical card for state-branded surfaces; `usa-card` is only for internal tools, USWDS-style microsites, or contexts where the Maryland visual identity is deliberately set aside. See `cdn/components/maryland-card.md` and `cdn/component-index.md` for the disambiguation.
>
> Key structural differences from `maryland-card`:
>
> | Concern | `usa-card` | `maryland-card` |
> |---|---|---|
> | Class prefix on every element | `usa-card__*` | `maryland-card__*` |
> | Group wrapper | `<ul class="usa-card-group">` (rows of `grid-col-*` siblings) | `<ul class="maryland-card-group">` (handles its own responsive grid) |
> | Borders/corners | Has a default border and rounded corners from USWDS theme | Square corners, **no border** by design |
> | Heading typography | Source Sans Pro Web (USWDS default) | Merriweather light in most variants, tuned per variant |
> | Linked-card variant | Not provided — entire card cannot be one `<a>` | `maryland-card--linked` exists with hover icon slide |
> | Header-first toggle | `usa-card--header-first` | `maryland-card--header-first` |
> | Footer button | `usa-card__footer > .usa-button` (left aligned) | `maryland-card__footer` with `--left/--center/--right` modifier and a `maryland-card__footer-content` flex wrapper |
> | Variants offered in MDWDS Storybook | `simple`, `media`, `flag` (with `media-right`), `header-first` (via `mediaPlacement`) | `simple`, `media`, `full`, `flag`, `linked` |
>
> If you find yourself reaching for `usa-card` on a Maryland page, stop and use `maryland-card` instead.

## What it looks like

A `usa-card` is a vertical rectangle with a thin USWDS border (`1px solid` neutral gray), slightly rounded corners (USWDS default radius), and a white background. Each card contains an optional media block (full-bleed image at the top), a header (with the card heading), a body (paragraph text), and a footer (typically a single `usa-button` left-aligned). Cards are flex columns so the footer sticks to the bottom of the card regardless of body height.

Cards live inside a `<ul class="usa-card-group">` — an unstyled flex/grid wrapper. The Storybook template adds responsive sizing utilities (`tablet-lg:grid-col-6 desktop-lg:grid-col-4` for non-flag cards, `tablet-lg:grid-col-12 desktop-lg:grid-col-6` for flag) directly to each `<li>`, which differs from `maryland-card-group` — that group handles its own column math.

The **flag** variant rearranges the card into a horizontal layout above the `tablet-lg` breakpoint (880px+): media on the left, header/body/footer stacked on the right. Below the breakpoint, it stacks vertically. The `usa-card--media-right` modifier flips the media to the right side.

The **header-first** modifier (`usa-card--header-first`) places the heading **above** the media even when media is enabled — useful when the title needs to anchor the card before the image draws the eye.

## Variants

The MDWDS Storybook exposes three primary variants via the `variant` arg: `simple`, `media`, `flag`. `mediaPlacement` (`first`/`second`) toggles header-first behavior on `media`, and toggles `media-right` on `flag`. `mediaStyle` (`default`/`inset`/`exdent`) controls how the image bleeds within the card.

| Variant | Visual |
|---|---|
| `simple` | Header + body + footer button. No image. |
| `media` | Image on top, then header + body + footer button. Use `mediaPlacement: "second"` to put the heading above the image. |
| `flag` | Horizontal layout at `tablet-lg`+: image left, content right. `mediaPlacement: "second"` puts image on the right. |

Media style modifiers (combine with `media` or `flag`):

| Class | Effect |
|---|---|
| `usa-card__media--inset` | Adds horizontal padding so the image is inset from the card edges. |
| `usa-card__media--exdent` | Negative horizontal margin — image extends beyond card padding. |

## When to use which variant

- **`simple`** → Text-only tile when an image would distract.
- **`media`** → Standard service tile with hero imagery.
- **`flag`** → Featured-item layouts where horizontal emphasis is desirable.
- **None of the above on Maryland pages.** Use `maryland-card`.

## Default markup (simple variant)

```html
<ul class="usa-card-group">
  <li class="usa-card tablet-lg:grid-col-6 desktop-lg:grid-col-4">
    <div class="usa-card__container">
      <div class="usa-card__header">
        <h3 class="usa-card__heading">Department of Information Technology</h3>
      </div>
      <div class="usa-card__body">
        <p>Manages statewide IT infrastructure, cybersecurity, and digital services for Maryland agencies.</p>
      </div>
      <div class="usa-card__footer">
        <a href="/agencies/doit" class="usa-button">Visit DoIT</a>
      </div>
    </div>
  </li>
  <!-- Repeat for additional cards -->
</ul>
```

## Markup — media variant

```html
<ul class="usa-card-group">
  <li class="usa-card tablet-lg:grid-col-6 desktop-lg:grid-col-4">
    <div class="usa-card__container">
      <div class="usa-card__media">
        <div class="usa-card__img">
          <img src="/img/chesapeake-bay.jpg" alt="Sunrise over the Chesapeake Bay" />
        </div>
      </div>
      <div class="usa-card__header">
        <h3 class="usa-card__heading">Chesapeake Bay Program</h3>
      </div>
      <div class="usa-card__body">
        <p>Track restoration progress, water quality data, and partnership initiatives for the Bay watershed.</p>
      </div>
      <div class="usa-card__footer">
        <a href="/programs/chesapeake-bay" class="usa-button">View dashboard</a>
      </div>
    </div>
  </li>
</ul>
```

To put the heading above the image, add `usa-card--header-first` to the `<li>`.

## Markup — flag variant

```html
<ul class="usa-card-group">
  <li class="usa-card usa-card--flag tablet-lg:grid-col-12 desktop-lg:grid-col-6">
    <div class="usa-card__container">
      <div class="usa-card__media">
        <div class="usa-card__img">
          <img src="/img/state-house.jpg" alt="Maryland State House dome at dusk" />
        </div>
      </div>
      <div class="usa-card__header">
        <h3 class="usa-card__heading">2026 Legislative Session</h3>
      </div>
      <div class="usa-card__body">
        <p>The Maryland General Assembly convenes on January 14. Read the Governor's priorities and watch live floor sessions.</p>
      </div>
      <div class="usa-card__footer">
        <a href="/legislature/2026" class="usa-button">Read more</a>
      </div>
    </div>
  </li>
</ul>
```

For image on the right side: add `usa-card--media-right` to the `<li>`.

## What each class does

| Class | Effect |
|---|---|
| `usa-card-group` | Unstyled flex container for a row of cards. Removes default list styling. Children supply their own `grid-col-*` utilities for width. |
| `usa-card` | Base card class on each `<li>`. Sets flex layout (column) and base spacing. |
| `usa-card--flag` | Horizontal flag layout at `tablet-lg` (880px+): media beside content. Stacks on smaller widths. |
| `usa-card--media-right` | When combined with `--flag`, puts the media on the right side. |
| `usa-card--header-first` | Reorders the inner flex so the header sits above the media block. |
| `usa-card__container` | White-background inner box that holds header, media, body, and footer. Has the USWDS card border (1px solid neutral) and rounded corners. Full-height flex column so the footer can pin to the bottom. |
| `usa-card__media` | Media wrapper. Default fills the card width edge-to-edge. |
| `usa-card__media--inset` | Adds horizontal padding equal to the card's padding so the image is inset from the card edges. |
| `usa-card__media--exdent` | Negative horizontal margin so the image visually extends beyond the card's padding boundary (useful for flush hero shots). |
| `usa-card__img` | Image wrapper. Sets `display: block` and ensures the `<img>` fills its container. USWDS keeps slight rounding consistent with the card. |
| `usa-card__header` | Top section holding the heading. Padded ~16px horizontal / ~16px vertical (USWDS default). |
| `usa-card__heading` | The card title. Source Sans Pro Web, semibold, ~17–22px depending on theme. Rendered as `<h4>` in the MDWDS Storybook template — **adjust to match page outline** (`<h2>` or `<h3>` is more common in practice). |
| `usa-card__body` | Body text region. Padded same as header; uses `flex-grow: 1` so the footer can stay at the bottom. ~16px body text. |
| `usa-card__footer` | Bottom footer region holding a button or links. Padded ~16px. Content is left-aligned by default. |

Note: `usa-card` does **not** ship with `--simple`, `--media`, `--full`, or `--linked` BEM modifier classes the way `maryland-card` does. The variant differences are produced by:
- whether you include the media block,
- whether you add `usa-card--flag`,
- whether you add `usa-card--header-first` / `usa-card--media-right`.

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `simple` \| `media` \| `flag` | `simple` | Card style |
| `title` | string | `"Card Title"` | Heading text |
| `body` | string | sample text | Body paragraph |
| `buttonText` | string | `"Learn More"` | Footer button label |
| `buttonUrl` | string | `"#"` | Footer button href |
| `cardCount` | number | `6` | Number of cards rendered by the Storybook template |
| `mediaPlacement` | `first` \| `second` | `first` | On `media`, `second` adds `usa-card--header-first`; on `flag`, `second` adds `usa-card--media-right` |
| `mediaStyle` | `default` \| `inset` \| `exdent` | `default` | Adds `usa-card__media--inset` or `--exdent` |
| `imageUrl` | string | placeholder | Image src (media/flag variants) |
| `imageAlt` | string | placeholder | Accessible image alt text |
| `enableAnalytics` | bool | `false` | Adds `data-ga-*` attributes to the footer link |
| `gaCategory` / `gaAction` / `gaLabel` | string | — | GA tracking values |

The Storybook template renders the heading as `<h4>`. The class name on the heading is `usa-card__heading` regardless of HTML element used.

## Heading level adjustment

The MDWDS Storybook for `usa-card` uses `<h4>` because the Storybook page wrapper already contains an `<h2>`/`<h3>`. **In production, choose the level that fits the surrounding outline.** A card group placed directly inside a `<section>` led by `<h2>` should use `<h3 class="usa-card__heading">`. See `cdn/composition.md` for the hierarchy rule.

## Common mistakes

1. **Using `usa-card` on a Maryland-branded page** — switch to `maryland-card`. The USWDS card visual (border, rounded corners, Source Sans heading) clashes with the Maryland visual identity.
2. **Mixing `usa-card__*` and `maryland-card__*` class names in the same card** — they are different components. Choose one fully.
3. **Wrapping `<ul class="usa-card-group">` itself in a `<div class="grid-col-*">`** — the cards inside the group carry their own `grid-col-*` utility classes. Wrap the group in `grid-container > grid-row` only.
4. **Forgetting `usa-card__container`** — without the inner container the border, padding, and flex layout don't apply and the card collapses.
5. **Putting the footer button outside `usa-card__footer`** — it loses the bottom-pinning behavior, leaving the button mid-card on tall cards.
6. **Adding rounded corners or shadows via inline `<style>`** — USWDS already provides them. If you don't see them, the CDN stylesheet didn't load (see `cdn/setup.md`).
