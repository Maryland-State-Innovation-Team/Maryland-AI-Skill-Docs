# maryland-social-media

Maryland Design System social-media component renders a horizontal row of circular icon links to the agency's social profiles. Each icon is a 40px ink-colored disc with the platform glyph in white. On hover, the disc turns Maryland gold (`secondary`). Used inside `maryland-footer` and "Connect with us" sections.

> **Use `maryland-social-media` to display agency social profile links.** Combine with `maryland-footer` for the standard "Connect with [Agency]" pattern. There is no smaller-size variant — these are footer-scale icons. For inline social-share buttons, you'd need a separate component.

## What it looks like

An unstyled `<ul>` rendered as a flex row with 16px gaps. Each `<li>` contains a single `<a>` that has:

- 40×40px (`units(5)`) ink-colored disc, `border-radius: 999px` (pill / circle).
- A 20×20px (`units(2.5)`) white platform glyph centered via CSS mask.
- A visually-hidden `<span class="usa-sr-only">` containing "Connect with [agency] on [platform].com (external link)".

On hover, the disc background changes from `ink` (near-black) to `secondary` (Maryland gold).

Supported platforms (each maps to a `--{name}` modifier):

| Modifier | Platform | Glyph |
|---|---|---|
| `maryland-social__link--facebook` | Facebook | Facebook glyph |
| `maryland-social__link--x` (or `--twitter`) | X / Twitter | X glyph |
| `maryland-social__link--youtube` | YouTube | YouTube glyph |
| `maryland-social__link--instagram` | Instagram | Instagram glyph |
| `maryland-social__link--linkedin` | LinkedIn | LinkedIn glyph |
| `maryland-social__link--flickr` | Flickr | Flickr glyph |
| `maryland-social__link--threads` | Threads | Threads glyph |
| `maryland-social__link--email` | Email | Material Symbols `mail` |

## When to use

- Inside `maryland-footer` as the social block.
- Below a "Connect with us" heading on a contact page.
- In an agency homepage's footer or hero "stay in touch" block.

Only include platforms the agency actively maintains — don't ship empty/never-updated profiles.

## Default markup

```html
<ul class="maryland-social">
  <li>
    <a href="https://www.facebook.com/MDDNR" class="maryland-social__link maryland-social__link--facebook">
      <span class="usa-sr-only">Connect with Department of Natural Resources on facebook.com (external link)</span>
    </a>
  </li>
  <li>
    <a href="https://x.com/MDDNR" class="maryland-social__link maryland-social__link--x">
      <span class="usa-sr-only">Connect with Department of Natural Resources on x.com (external link)</span>
    </a>
  </li>
  <li>
    <a href="https://youtube.com/@MDDNR" class="maryland-social__link maryland-social__link--youtube">
      <span class="usa-sr-only">Connect with Department of Natural Resources on youtube.com (external link)</span>
    </a>
  </li>
  <li>
    <a href="https://www.instagram.com/mddnr" class="maryland-social__link maryland-social__link--instagram">
      <span class="usa-sr-only">Connect with Department of Natural Resources on instagram.com (external link)</span>
    </a>
  </li>
  <li>
    <a href="https://www.linkedin.com/company/mddnr" class="maryland-social__link maryland-social__link--linkedin">
      <span class="usa-sr-only">Connect with Department of Natural Resources on linkedin.com (external link)</span>
    </a>
  </li>
  <li>
    <a href="https://www.flickr.com/photos/mddnr" class="maryland-social__link maryland-social__link--flickr">
      <span class="usa-sr-only">Connect with Department of Natural Resources on flickr.com (external link)</span>
    </a>
  </li>
</ul>
```

## What each class does

| Class | Effect |
|---|---|
| `maryland-social` | The `<ul>`. Zero margin/padding, list-style none, flex row with 16px gap. |
| `maryland-social__link` | Base link disc. Inline-flex center, 40×40px, ink background, white text, `border-radius: 999px`. The `::after` pseudo holds the platform glyph (20×20px). On hover, background becomes `secondary` (Maryland gold). |
| `maryland-social__link--facebook` | Sets the `::after` mask to the Facebook glyph. |
| `maryland-social__link--flickr` | Sets the `::after` mask to the Flickr glyph. |
| `maryland-social__link--instagram` | Sets the `::after` mask to the Instagram glyph. |
| `maryland-social__link--linkedin` | Sets the `::after` mask to the LinkedIn glyph. |
| `maryland-social__link--threads` | Sets the `::after` mask to the Threads glyph. |
| `maryland-social__link--x` / `--twitter` | Sets the `::after` mask to the X glyph. (Both modifiers point at the same glyph.) |
| `maryland-social__link--youtube` | Sets the `::after` mask to the YouTube glyph. |
| `maryland-social__link--email` | Sets the `::after` mask to Material Symbols `mail`. |
| `usa-sr-only` | (USWDS) Visually hides the accessible-name span while keeping it announceable. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `name` | string | `"Agency Title"` | Agency name. Used in the `usa-sr-only` text for each link. |

In the documented variants, the URL list is hard-coded to `#!` placeholders. In hand-written markup, supply real URLs.

## Heading level adjustment

The component has no heading of its own — it sits inside another section (e.g., `maryland-footer`'s "Connect with us" block). The surrounding heading is the responsibility of the parent.

## Common mistakes

1. **Empty `href="#!"` in production** — the documented variants default to `#!`. Replace with the actual social URLs before shipping.
2. **Including platforms the agency doesn't use** — fewer active links is better than more broken/dead links.
3. **Custom backgrounds via inline `<style>`** — the ink/gold colors are part of the design system. Don't recolor for a "brand match" — Maryland brand wins.
4. **Skipping the `usa-sr-only` text** — without it, screen-reader users hear "link" with no destination. Each link needs an accessible name.
5. **Wrapping the list in a non-`<ul>` element** — the flex layout, list-style reset, and gap all rely on `.maryland-social` being a `<ul>`.
6. **Mixing `--x` and `--twitter`** — pick one. They render identically; use `--x` for new sites to match the current platform name.
