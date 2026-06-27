# maryland-utility-nav

The small top-strip of secondary links above the main `maryland-header` content (sign-in, language, "Make a payment", etc.). On desktop it sits right-aligned across the top of the header; on mobile it moves inside the hamburger menu panel.

> **Composed inside `maryland-header`.** You normally don't render this standalone. See `cdn/components/maryland-header.md`. The standalone component is available for unusual layouts where the header is built piece-by-piece.

## What it looks like

**Desktop (≥1024px):**
A right-justified horizontal flex row of small (13px / `font-size("ui", 3)`) semibold links. The container (`maryland-header__util-nav-container`) becomes a full-width block at the top of the header. The list itself has `units(3)` (24px) top margin and `spacing-multiple(5.5)` (~44px) bottom margin so it sits just above the logo row.

- **Plain links** are 13px semibold, color `base-dark`, with 16px (`units(2)`) horizontal padding. Adjacent plain links are separated by a 1px `base-light` vertical divider (`border-left` on the next sibling). Hover/focus: color shifts to Maryland blue (`primary`) and the text underlines.
- **Button-styled items** (`isButton: true`) render as small `usa-button--small` pills with 13px font, vertically centered, 8px horizontal margin. The first/last button gets edge margin removed.

**Mobile (<1024px):**
The desktop container hides. The same `<ul class="maryland-header__util-nav">` is re-rendered inside a `maryland-nav__mobile-slot` at the bottom of the hamburger panel. Items become a vertical flex column with 16px (`units(2)`) gaps. Plain links are 14px (`ui-7`), full-width. Buttons are 16px (`ui-5`) with `units(2)` × `units(3)` padding. A 1px `base-light` bottom border separates the utility group from the next slot.

## Item types

| Item shape | Renders as | Use for |
|---|---|---|
| `{ label: "Text", url: "/path" }` | Plain link | Secondary navigation (sign-in, language) |
| `{ label: "Text", url: "/path", isButton: true }` | Button-styled link | A primary call-to-action ("Make a payment", "Apply now") |
| `{ label: "Text", isButton: true }` | Real `<button>` element | Triggers a JS handler (open modal, etc.) |

## Default markup — desktop wrapper

```html
<div class="maryland-header__util-nav-container">
  <ul class="maryland-header__util-nav">
    <li><a href="/sign-in">Sign in</a></li>
    <li><a href="/language">Language</a></li>
    <li>
      <a href="/pay" class="usa-button usa-button--small">Make a payment</a>
    </li>
  </ul>
</div>
```

## Markup — mobile wrapper

```html
<div class="maryland-nav__mobile-slot">
  <ul class="maryland-header__util-nav">
    <li><a href="/sign-in">Sign in</a></li>
    <li><a href="/language">Language</a></li>
    <li>
      <a href="/pay" class="usa-button usa-button--small">Make a payment</a>
    </li>
  </ul>
</div>
```

Both wrappers render the **same `<ul>`** — the wrapper class drives the responsive presentation. In a real `maryland-header`, both wrappers are present in the DOM (one is hidden by media query); the component emits both.

## Markup — item shapes

```html
<!-- Plain link: { label, url } -->
<li><a href="/sign-in">Sign in</a></li>

<!-- Button-styled link: { label, url, isButton: true } -->
<li>
  <a href="/pay" class="usa-button usa-button--small">Make a payment</a>
</li>

<!-- Real <button> element: { label, isButton: true } with NO url -->
<li>
  <button type="button" class="usa-button usa-button--small">
    Open chat
  </button>
</li>
```

Use the `<button>` variant only for items that fire a JS handler without navigation (modals, language switchers, chat widgets). Items with a destination URL should always be `<a>` elements, even when `isButton: true`.

## What each class does

| Class | Effect |
|---|---|
| `maryland-header__util-nav-container` | Desktop wrapper. Hidden by default (`display: none`); shown as a full-width block at `desktop` (1024px+). Also hidden when the header's primary nav is in `maryland-nav--hamburgered` mode (rare). |
| `maryland-header__util-nav` | The `<ul>`. No bullets, zero margin-block. Inside `__util-nav-container`: flex row, right-justified, 13px font. Inside `maryland-nav__mobile-slot`: flex column, 14–16px font, 16px gap, 1px bottom border. |
| `maryland-header__util-nav a:not(.usa-button)` | Plain links — 13px (desktop) / 14px (mobile) semibold, color `base-dark` (gray-90-ish), no underline. Hover: Maryland blue + underline. Adjacent plain links separated by 1px `base-light` vertical divider at desktop. |
| `maryland-header__util-nav a.usa-button` | Button-styled link — uses the small USWDS button (Maryland blue pill). 13px font at desktop, 16px on mobile. |
| `maryland-nav__mobile-slot` | Mobile wrapper that places the `<ul>` inside the hamburger panel. Adds vertical padding (`spacing-multiple(4.5)` / 36px top, `units(4)` / 32px bottom) and a 1px `base-light` bottom border to separate from the next mobile slot. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `enableUtil` | bool | `true` | Whether to render the utility nav at all. If `false` or `util` is empty, the component renders nothing. |
| `util` | array of `{label, url?, isButton?}` | 3 sample items | The items. `url` is the href (defaults to `#` if absent). `isButton: true` switches the item to button-styled. If `isButton: true` and `url` is omitted, a real `<button>` is rendered. |

## Heading level adjustment

The utility nav contains no headings — it's a list of small action links. Don't add `<h2>`/`<h3>` for "Utility" or "Account."

## Common mistakes

1. **Rendering only the desktop wrapper** — if you skip the mobile-slot copy, the utility nav vanishes on mobile. Render both (or use `maryland-header`, which handles this).
2. **Mixing button-styled items with plain links arbitrarily** — the published CSS adds dividers only between adjacent **plain** links, and margin only around buttons. Interleaving the two styles produces uneven spacing. Keep button items at the end of the list (the convention is plain links left, CTA right).
3. **Forgetting `usa-button--small`** — a button-styled item without `--small` becomes full-size and breaks the header height.
4. **Using `<button>` instead of `<a>` for a navigation link** — items with a destination URL should be anchors, even if `isButton: true`. Use a `<button>` element only for items that trigger JS without navigation.
5. **Loading `<a class="usa-button">` without the USWDS button styles** — the button visual relies on the USWDS button CSS, which the MDWDS CDN stylesheet pulls in. If you copy the markup standalone, ensure the CDN stylesheet is loaded.
6. **Putting headings or paragraphs inside `<li>` items** — utility-nav items are single links/buttons. Anything more belongs in the primary nav.
