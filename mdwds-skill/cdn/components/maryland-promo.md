# maryland-promo

Maryland Design System promos are large, full-width promotional blocks that highlight a single call-to-action link. They occupy their own page section and visually anchor a chunk of content with a title, brief description, and a prominent text link.

> **Use `maryland-promo` for a single promotional call-to-action.** If you need a smaller, group-format set of services or links, use `maryland-card`. If you need a video, use `maryland-video-promo`. The promo is one section, one link.

## What it looks like

A promo is a `<section>` that occupies the full content width. It has three top-level styles:

- **`plain`** — Maryland blue (`primary`) background, white text, two-column at desktop (5/12 title left, 6/12 description+link right with a 1-col offset). 48px vertical padding (mobile), 64px (mobile-lg), 128px (widescreen).
- **`image`** / **`image-multiple`** — Light cream (`base-lightest`) background for a single image, or near-black (`base-darkest`) background for multiple images. Two-column at tablet+ with the image on the left or right (configurable). The image is a 3:4 aspect ratio rectangle and protrudes ~80px above and below the section, with a Maryland-blue diamond pattern decoration appearing below the section.
- **`illustration`** — Maryland blue background with a Maryland-themed line illustration (`flag`, `statehouse`, `dome`, `boat`, `lighthouse`, `dune`, `tractor`, `barn`) etched into the background.

Titles are styled via the `h2` mixin — Merriweather, light, 32–48px responsive. Body text is 16/20/24px responsive. The "link" is a primary link (underlined, inheriting color) on its own line below the description.

## Variants

| Variant | Layout | Background | When to use |
|---|---|---|---|
| `plain` | Two-column (title \| content) at desktop | Maryland blue | A focused promo when no image is appropriate. |
| `image` | Two-column with single 3:4 image | Cream | The most common promotional layout — featured story with a hero photo. |
| `image-multiple` | Same as `image`, but cycles through multiple images | Near-black | Showcasing a series of related images (the MDWDS JS cycles through them). |
| `illustration` | Same as plain with an illustration backdrop | Maryland blue with line illustration | Adds visual Maryland character without a photo. |

## When to use which variant

- **`plain`** — Default choice when imagery would distract.
- **`image`** — Featured-story promotion. A single hero image gives the most impact.
- **`image-multiple`** — Only when 2–5 related images add narrative value (e.g., showing the same scene across seasons).
- **`illustration`** — Themed sections (e.g., a "Tourism" promo with the lighthouse illustration; "Agriculture" with the barn).

## Default markup (plain)

```html
<section class="maryland-promo maryland-promo--plain" aria-labelledby="promo-1">
  <div class="maryland-promo__container">
    <div class="maryland-promo__row">
      <div class="maryland-promo__title-container">
        <h2 id="promo-1" class="maryland-promo__title">Your voice, your state: building a better tomorrow</h2>
      </div>
      <div class="maryland-promo__content-container">
        <div class="maryland-promo__description">
          <p>We're committed to serving Marylanders. Share your suggestions and feedback with the Governor's office.</p>
        </div>
        <a class="maryland-promo__link" href="/feedback">Share your feedback</a>
      </div>
    </div>
  </div>
</section>
```

## Markup — image (single image, image on left)

```html
<section class="maryland-promo maryland-promo--image maryland-promo--image-left" aria-labelledby="promo-2">
  <div class="maryland-promo__container">
    <div class="maryland-promo__row">
      <div class="maryland-promo__img-container">
        <figure class="maryland-promo__img">
          <img src="/img/chesapeake-bay.jpg" alt="" />
        </figure>
      </div>
      <div class="maryland-promo__content-container">
        <h2 id="promo-2" class="maryland-promo__title">Help protect the Chesapeake Bay</h2>
        <div class="maryland-promo__description">
          <p>The Department of Natural Resources runs volunteer programs across all 23 counties.</p>
        </div>
        <a class="maryland-promo__link" href="/dnr/volunteer">Find a volunteer opportunity</a>
      </div>
    </div>
  </div>
</section>
```

For image on the right, use `maryland-promo--image-right` instead of `--image-left`.

## Markup — image-multiple (cycling images)

```html
<section class="maryland-promo maryland-promo--image-multiple maryland-promo--image-left" aria-labelledby="promo-3">
  <div class="maryland-promo__container">
    <div class="maryland-promo__row">
      <div class="maryland-promo__img-container maryland-promo__img-container--multiple">
        <figure class="maryland-promo__img">
          <img src="/img/park-spring.jpg" alt="" />
          <img src="/img/park-summer.jpg" alt="" />
          <img src="/img/park-fall.jpg" alt="" />
        </figure>
      </div>
      <div class="maryland-promo__content-container">
        <h2 id="promo-3" class="maryland-promo__title">Maryland's state parks change with the seasons</h2>
        <div class="maryland-promo__description">
          <p>76 parks, 17,000 miles of waterways, year-round adventure.</p>
        </div>
        <a class="maryland-promo__link" href="/dnr/parks">Plan a visit</a>
      </div>
    </div>
  </div>
</section>
```

The cycling behavior is wired up by `mdwds-core.js` at runtime. Without the script, the first image shows and the rest are hidden via `visibility: hidden`.

## Markup — illustration

```html
<section class="maryland-promo maryland-promo--illustration maryland-promo--illustration-statehouse" aria-labelledby="promo-4">
  <div class="maryland-promo__container">
    <div class="maryland-promo__row">
      <div class="maryland-promo__title-container">
        <h2 id="promo-4" class="maryland-promo__title">Your government, your voice</h2>
      </div>
      <div class="maryland-promo__content-container">
        <div class="maryland-promo__description">
          <p>Find your legislators, attend a public meeting, or testify on a bill.</p>
        </div>
        <a class="maryland-promo__link" href="/government">Get involved</a>
      </div>
    </div>
  </div>
</section>
```

Illustration choices: `flag`, `statehouse`, `dome`, `boat`, `lighthouse`, `dune`, `tractor`, `barn`. The illustration appears as a 10% opacity Maryland-blue mask on the right of the section at desktop+, and centered at the bottom on mobile/tablet.

## What each class does

| Class | Effect |
|---|---|
| `maryland-promo` | Base `<section>`. Provides relative positioning, layout containment, and base body-7 (20px) typography. |
| `maryland-promo--plain` | Maryland blue background, white text, `block-spacing` vertical margins. Padding 48px (mobile), 64px (mobile-lg), 128px (widescreen). |
| `maryland-promo--image` | Cream (`base-lightest`) background. Adds 80px+ vertical margins. The image protrudes above (`margin-top: -80px`) and below the section, with a Maryland-blue diamond pattern `::after` decoration appearing under the section. |
| `maryland-promo--image-multiple` | Near-black background with white text. Same image-protrusion behavior as `--image`. |
| `maryland-promo--illustration` | Maryland blue background with white text and a faint Maryland illustration mask in the background. |
| `maryland-promo--image-left` / `--image-right` | Sets the column order: image left vs right at tablet+. |
| `maryland-promo--illustration-flag` (and similar `-statehouse`, `-dome`, `-boat`, `-lighthouse`, `-dune`, `-tractor`, `-barn`) | Picks the illustration to mask into the background. |
| `maryland-promo__container` | Inner wrapper that applies `grid-container` and 24/56px horizontal padding (mobile / tablet+). z-index 2 to stack above the diamond pattern. |
| `maryland-promo__row` | Flex column on mobile, grid row at tablet. Holds title/content/image columns. |
| `maryland-promo__title-container` | Title column (plain/illustration). 5/12 at tablet, 50% at desktop. |
| `maryland-promo__content-container` | Description + link column. 6/12 with 1-col offset at tablet, 50% at desktop. Font-size scales 16 → 20 → 24px. |
| `maryland-promo__img-container` | Image column. 5/12 at tablet. Adds relative positioning. |
| `maryland-promo__img-container--multiple` | Marker class on the multiple-image variant — its presence is required for the cycling JS to find the element. |
| `maryland-promo__img` | Image `<figure>`. 3:4 aspect ratio, 75% width on mobile, 100% at tablet. Protrudes -80px above and 48px below at mobile (mobile shifts to -40/-72 at tablet). When multiple, non-first images are `visibility: hidden`. |
| `maryland-promo__title` | The `<h2>`. Uses Merriweather light per the `h2` mixin (32 → 40 → 48px depending on breakpoint). Removes default top margin; 32px bottom margin. |
| `maryland-promo__description` | Description block. Has 16px top margin from a preceding element and 16px bottom margin if a link follows. |
| `maryland-promo__link` | Primary link. Inherits color (white on plain/illustration/image-multiple; primary blue on image variant). Uses the typeset-link mixin (underlined, focus outline). |
| `maryland-promo__img-play` | (Internal) Play/pause button overlaid on the image when `image-multiple` cycles. White background with arrow icon. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `title` | string | — | Required. Title text. |
| `description` | string | — | Description text. Renders as inner HTML — pass full `<p>` elements if needed. |
| `linkTitle` | string | — | Required. Link text. |
| `linkUrl` | string | `"#"` | Required. Link URL. |
| `style` | `plain` \| `image` \| `illustration` | `plain` | Visual style. When `image` is set and multiple images are supplied, internally promotes to `image-multiple`. |
| `imagePosition` | `left` \| `right` | `left` | Image side at tablet+ (image style only). |
| `imageOne` … `imageFive` | string (URL) | — | 1–5 image URLs. Only `imageOne` for single-image; provide multiple to enable cycling. |
| `multipleImages` | bool | false | Storybook toggle that reveals image-2..5 fields. Has no rendered effect — the component just looks at whether `imageTwo` etc. are non-empty. |
| `illustration` | one of `flag`, `statehouse`, `dome`, `boat`, `lighthouse`, `dune`, `tractor`, `barn` | `flag` | Background illustration (illustration style only). |

## Heading level adjustment

The promo's title renders as `<h2>` by default — appropriate when the promo is a top-level section of the page (which it almost always is). If you somehow nest it inside another `<h2>`-led section, demote to `<h3>` and remove the `h2` mixin styling via context (or, more practically, don't nest promos under other sections).

## Common mistakes

1. **Wrapping the promo in a `grid-container`** — the promo already applies `grid-container` internally via `maryland-promo__container`. Adding another container introduces double-padding.
2. **Using more than one link inside `maryland-promo__content-container`** — the component is designed for a single CTA. For multi-link promotions, use `maryland-card` or `maryland-link-collection`.
3. **Overriding the title with inline `<style>` for size** — sizes come from the `h2` mixin via breakpoints. If you want a smaller title, you've picked the wrong component.
4. **Forgetting `aria-labelledby` on the `<section>`** — accessibility regression. Pair the `<section>` with the `id` of the `<h2>`.
5. **Setting both `imageOne` and the `image-multiple` class without supplying additional images** — the component auto-promotes to `image-multiple` only when more than one image URL is provided. Don't add `--image-multiple` manually unless you have multiple images.
6. **Mixing illustration + image** — the styles are mutually exclusive; pick one.
