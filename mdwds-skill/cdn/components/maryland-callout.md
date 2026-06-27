# maryland-callout

Maryland Design System callouts highlight a single piece of important information with a centered headline, a short body sentence, and an optional circular image. They are the visually quietest of the promo-style components: no buttons, no link, just a key statement.

> **Use `maryland-callout` to draw attention to one statement or value proposition without a CTA.** If you need a link or button, use `maryland-promo` or `maryland-highlight`. If you need a banner-style status message, use `maryland-alert`.

## What it looks like

A callout is a full-width centered `<section>`. From top to bottom:

1. (Optional) a circular image — 187px diameter on mobile, scales to a `card-lg` size on tablet+. Border-radius 50%, object-fit cover.
2. The headline (`<h2>`). Merriweather light, 24px → 32px → 40px (mobile → mobile-lg → desktop-lg), `ls(1)` letter-spacing. Centered.
3. A thin horizontal divider — `base-light` (light gray) top and bottom borders. 78px wide on mobile, 100px at `mobile`, 200px at mobile-lg+. 4px tall (mobile), 6px at mobile-lg+.
4. The description text. 16px → 22px → 24px responsive. Center-aligned.

Content is constrained to a max-width of 848px (`spacing-multiple(106)`) and centered. The whole component has 24px (mobile) or 64px (tablet+) of perimeter padding.

## When to use

- A mission statement or value-prop block near the top of a homepage ("Your government is committed to serving Marylanders").
- A short quote or testimonial.
- A "what this page is about" centered hero-adjacent intro.

Avoid using callouts for time-sensitive notifications (use `maryland-alert`), for navigational hub content (use `maryland-promo` or `maryland-highlight`), or for any callout that requires a button.

## Default markup

```html
<section class="maryland-callout" aria-labelledby="callout-1">
  <div class="maryland-callout__container">
    <div class="maryland-callout__image">
      <img src="/img/governor-portrait.jpg" alt="" />
    </div>
    <div class="maryland-callout__content">
      <h2 id="callout-1" class="maryland-callout__title">Your government is committed to serving Marylanders</h2>
      <div class="maryland-callout__description">
        The goal of Maryland's state government is to serve the public and represent Marylanders' interests in every county, town, and community.
      </div>
    </div>
  </div>
</section>
```

## Markup — no image

```html
<section class="maryland-callout" aria-labelledby="callout-2">
  <div class="maryland-callout__container">
    <div class="maryland-callout__content">
      <h2 id="callout-2" class="maryland-callout__title">A healthier Chesapeake Bay starts here</h2>
      <div class="maryland-callout__description">
        Maryland leads the nation in oyster restoration, with more than 5 billion oysters planted since 2014.
      </div>
    </div>
  </div>
</section>
```

When `showImage` is false or no `image` is set, the image block is omitted entirely.

## Markup — visually hidden title

Use when the callout is part of a sequence where the surrounding context already names the section:

```html
<h2 id="callout-3" class="maryland-callout__title usa-sr-only">Mission</h2>
```

The divider still appears (it is generated from the description's `::before`), but the headline is screen-reader-only.

## What each class does

| Class | Effect |
|---|---|
| `maryland-callout` | Base `<section>`. Applies `block-spacing` and `grid-container`. Centered text. 24px perimeter padding (mobile), 64px (tablet+). |
| `maryland-callout__container` | Inner content wrapper. Max-width 848px (`spacing-multiple(106)`), horizontally centered. |
| `maryland-callout__image` | Image wrapper. Flex center. Bottom margin 36px (mobile) / 48px (tablet+). |
| `maryland-callout__image img` | The circular image. 100% width up to 187px (mobile) or the USWDS `card-lg` token (tablet+). `border-radius: 50%`, 1:1 aspect ratio, `object-fit: cover`. |
| `maryland-callout__content` | Wraps title and description. No styles on its own — used as a structural anchor for the title's id. |
| `maryland-callout__title` | The `<h2>`. Merriweather light, 24px (mobile) → 32px (mobile-lg) → 40px (desktop-lg). `ls(1)` letter-spacing (about 0.4px). Center-aligned (inherited). 36px → 48px bottom margin. |
| `maryland-callout__description` | Body text. 16px → 22px → 24px responsive. Has a `::before` divider — a 78–200px wide bar with top and bottom 1px `base-light` borders, generating a thin double-line. |
| `usa-sr-only` | (USWDS) Visually hide the title while keeping it readable to screen readers. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `title` | string | sample | Headline text. |
| `hideTitle` | bool | false | Visually hide the title (adds `usa-sr-only`). |
| `showImage` | bool | true | Show or omit the image block. |
| `description` | string | sample | Body text (required). |
| `image` | string (URL) | placeholder | Image src. Image is omitted if missing. |
| `imageAlt` | string | `""` | Alt text. Empty string is correct for decorative images. |

## Heading level adjustment

The title renders as `<h2>` by default. If the callout is a sub-element of an already-`<h2>`-titled section, change the element to `<h3>` and keep the class. The class controls visual style; the element controls the outline.

## Common mistakes

1. **Adding a button or link inside the callout** — the component doesn't support CTAs. Use `maryland-promo` instead.
2. **Using a square or wide image** — the image is forced to a circle. Pick portrait-orientation or 1:1 source images so the cover-fit doesn't crop important details.
3. **Long descriptions** — the design assumes 1–3 sentences. For longer copy, use `usa-prose` paragraphs or a `maryland-summary-box`.
4. **Removing the divider with inline `<style>`** — the divider is a design-system element. If you don't want it, you don't want a callout — pick a different component.
5. **Centering callout text further** — text is already centered via `text-align: center` on the section. Adding alignment utilities is redundant.
6. **Missing `aria-labelledby` with a title** — the section landmark needs the heading's id when a title is present, even if the title is `usa-sr-only`.
