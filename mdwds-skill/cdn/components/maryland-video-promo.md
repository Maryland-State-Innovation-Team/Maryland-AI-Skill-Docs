# maryland-video-promo

Maryland Design System video promos pair a heading + short description + optional CTA link with an embedded video player. They are used to feature a single video and its surrounding context — service explainers, governor's addresses, public-service announcements.

> **Use `maryland-video-promo` instead of dropping a raw `<iframe>` into a page.** It handles the responsive 16:9 aspect ratio, caption styling, two-column layout, and proper heading/aria structure. For a non-video promotional block, see `maryland-promo`.

## What it looks like

The component has two layouts:

- **`side-by-side`** (`video-first` or `text-first`): Cream (`base-lightest`) background, rounded corners (4px), 1px white border. Text and video stack vertically on mobile, switch to a 50/50 row at `tablet` (640px). Title is in body-font semibold (not Merriweather), 20–32px responsive. Description is body text.
- **`full-width`**: No background — the video sits as a full-width 16:9 element with title above and description+link below. Title is Merriweather (`h2` style), 32–40px. The description switches to a side-by-side text + link layout at `tablet-lg` (880px), with the description on the left and the link aligned to the right.

The video is rendered inside a `<figure>` whose iframe is forced to `aspect-ratio: 16/9` and `width: 100%`. An optional `<figcaption>` appears below.

## Variants

Set via the `style` prop:

| Variant | Visual |
|---|---|
| `text-first` (side-by-side) | Text column on the left, video on the right at tablet+. Cream background, rounded card. |
| `video-first` (side-by-side) | Video column on the left (via `order: -1` on the video), text on the right at tablet+. |
| `full` (full-width) | Title on top, full-width video below, description + link at the bottom. No background. |

## Default markup — side-by-side, text first

```html
<section class="maryland-video-promo maryland-video-promo--side-by-side" aria-labelledby="vp-1">
  <div class="maryland-video-promo__container">
    <div class="maryland-video-promo__content">
      <h2 id="vp-1" class="maryland-video-promo__title">How to renew your driver's license online</h2>
      <div class="maryland-video-promo__description">
        <p>A two-minute walkthrough of the online renewal process at the Motor Vehicle Administration.</p>
        <a class="maryland-video-promo__link" href="/mva/renew">Start your renewal</a>
      </div>
    </div>
    <figure class="maryland-video-promo__video">
      <iframe src="https://www.youtube.com/embed/abc123" frameborder="0" allowfullscreen></iframe>
      <figcaption>Recorded at the MVA Glen Burnie office, March 2026.</figcaption>
    </figure>
  </div>
</section>
```

## Markup — side-by-side, video first

```html
<section class="maryland-video-promo maryland-video-promo--side-by-side maryland-video-promo--video-first" aria-labelledby="vp-2">
  <div class="maryland-video-promo__container">
    <div class="maryland-video-promo__content">
      <h2 id="vp-2" class="maryland-video-promo__title">Governor's weekly address</h2>
      <div class="maryland-video-promo__description">
        <p>This week the Governor discusses the Chesapeake Bay restoration plan.</p>
        <a class="maryland-video-promo__link" href="/governor/addresses">Watch all addresses</a>
      </div>
    </div>
    <figure class="maryland-video-promo__video">
      <iframe src="https://player.vimeo.com/video/123456" frameborder="0" allowfullscreen></iframe>
    </figure>
  </div>
</section>
```

The `--video-first` modifier reorders the video figure to come visually first at tablet+. The DOM order is unchanged for screen readers.

## Markup — full-width

```html
<section class="maryland-video-promo maryland-video-promo--full-width" aria-labelledby="vp-3">
  <div class="maryland-video-promo__container">
    <div class="maryland-video-promo__content">
      <h2 id="vp-3" class="maryland-video-promo__title">The 2026 Bay Cleanup, in two minutes</h2>
      <div class="maryland-video-promo__description">
        <p>This year's effort engaged over 12,000 volunteers across Maryland and removed an estimated 240 tons of debris from Chesapeake watershed sites.</p>
        <a class="maryland-video-promo__link" href="/bay/cleanup">Get involved next year</a>
      </div>
    </div>
    <figure class="maryland-video-promo__video">
      <iframe src="https://www.youtube.com/embed/xyz789" frameborder="0" allowfullscreen></iframe>
      <figcaption>Filmed across 10 counties, March 2026.</figcaption>
    </figure>
  </div>
</section>
```

The DOM order is content → video; the full-width variant's CSS controls visual stacking (title above, video in the middle, description+link below).

## Markup — visually hidden title

Use `hideTitle: true` (or add `usa-sr-only` directly) when the surrounding context already names the video:

```html
<h2 id="vp-4" class="maryland-video-promo__title usa-sr-only">Driver's license renewal walkthrough</h2>
```

## What each class does

| Class | Effect |
|---|---|
| `maryland-video-promo` | Base `<section>`. Applies `block-spacing` vertical rhythm. |
| `maryland-video-promo--side-by-side` | Cream (`base-lightest`) background, 4px rounded corners, 12px padding (mobile). Sets body-5 (20px) typography. |
| `maryland-video-promo--video-first` | Reorders the video to come first visually at tablet+ via `order: -1`. |
| `maryland-video-promo--full-width` | No background. Title uses the `h2` heading mixin. At tablet-lg+, the description becomes a flex row with text left and link right. |
| `maryland-video-promo__container` | Inner wrapper. For side-by-side, becomes a flex container with column-to-row switch at tablet, 16px border, 4px rounded, 40px (mobile) → 64px (tablet) vertical padding. |
| `maryland-video-promo__content` | Text column. Side-by-side: flex 1/2 of the row, 24px horizontal padding. Full-width: bottom margin 36px (mobile) → 48px (mobile-lg) → 64px (tablet). |
| `maryland-video-promo__title` | The `<h2>`. Side-by-side: body-6 (20px) semibold — **not** Merriweather. Full-width: full `h2` mixin (Merriweather light, 32–40px). |
| `maryland-video-promo__description` | Description block. Bottom margin 16px, scales with breakpoint. Removes default `<p>` margins inside. At tablet-lg+ on full-width, becomes a flex row aligning description + link side-by-side. |
| `maryland-video-promo__link` | Primary link. Uses the `typeset-link` mixin. 16px (mobile) → 20px (mobile-lg) → 24px (tablet+). 16px top margin at tablet+. |
| `maryland-video-promo__video` | The video `<figure>`. Full width, no margin. iframe is forced to `aspect-ratio: 16/9`. Side-by-side at tablet: `flex: 1 1 calc(50% - 32px)`. |
| `usa-sr-only` | (USWDS) Visually hide an element while keeping it readable to screen readers. Add to the title when needed. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `title` | string | `"Video Promo"` | Required. Title text. |
| `hideTitle` | bool | false | Visually hide the title (keeps it for screen readers via `usa-sr-only`). |
| `description` | string | — | Body text. |
| `video` | string (HTML) | sample iframe | iframe embed code as a string. Inserted via `unsafeHTML` — make sure the HTML is trusted. |
| `caption` | string | — | Optional `<figcaption>` under the video. |
| `linkText` | string | — | CTA link text. Omit `linkText` or `linkUrl` to hide the link. |
| `linkUrl` | string | — | CTA link URL. |
| `style` | `full` \| `video-first` \| `text-first` | `text-first` | Layout. `full` sets `--full-width`; the others both set `--side-by-side` (with `video-first` adding an extra modifier). |

## Heading level adjustment

The component renders the title as `<h2>`. If the video sits inside an existing `<h2>`-led section, use `<h3>` and apply the same `maryland-video-promo__title` class — the styling stays applied via the class regardless of element. Use `hideTitle` only when the parent context already names the video.

## Common mistakes

1. **Embedding the iframe outside the `<figure>` wrapper** — the responsive 16:9 sizing is applied via `.maryland-video-promo__video iframe`. Without the wrapper class, the iframe gets default dimensions.
2. **Forgetting `aria-labelledby`** — pair the `<section>` with the title's `id`. Without it, the section landmark is unnamed.
3. **Passing raw video URLs as `src`** — `video` is the entire iframe HTML, not a URL. Provide `<iframe src="..." ...></iframe>` as a string.
4. **Using `<iframe title="...">` and `hideTitle`** — the iframe still needs an accessible title (e.g., `<iframe title="Renewal walkthrough">`) even when the section title is visible. They serve different a11y purposes.
5. **Side-by-side at low viewport** — at <640px the layout stacks vertically; don't assume the visual two-column will hold on mobile.
6. **Treating the title as Merriweather in side-by-side mode** — it isn't. Side-by-side uses Source Sans semibold for visual hierarchy parity with cards.
