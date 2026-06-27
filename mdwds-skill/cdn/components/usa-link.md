# usa-link

A helper class for styling inline `<a>` elements — typically used inside `usa-prose` body content for external links, alternate-color links on dark backgrounds, and any link that needs the explicit USWDS treatment. The default link styling (Maryland blue, underlined) is already applied to `<a>` elements inside `usa-prose`, so `usa-link` is mainly needed for modifiers (`--external`, `--alt`) or for `<a>` outside `usa-prose`.

> **Disambiguation:** there is also a Maryland-specific `maryland-link` (see `cdn/components/maryland-link.md`) used internally by other Maryland components (cards, link lists, sidenav). For author-written body links, prefer `usa-link`. The `maryland-link` class supports MDWDS-specific variants (`skipnav`, "labelled" link with description text) and is the right choice when you're hand-building those patterns. See `cdn/component-index.md`.

## What it looks like

A `usa-link` is an inline `<a>` rendered in **Maryland blue** (`primary` = `blue-60v`, approximately `#1A4480`) with an **underline** (USWDS default link style). On hover, the color deepens to `primary-dark` and the underline thickens slightly. On focus, the global 2px focus ring appears. Visited links use `primary-vivid` (a slightly different shade of Maryland blue).

Variants:

- **Default** — Maryland blue, underlined. Inherit font and size from surrounding text.
- **`usa-link--external`** — Adds an inline **"open in new" icon** (Material Symbols `open_in_new`, an arrow leaving a box) immediately after the link text, separated by a tiny space. The icon sits at the link's baseline and uses the same color as the text. Use this only when the link genuinely opens a new tab (or leaves the maryland.gov domain) — the icon is a promise to the user.
- **`usa-link--alt`** — Alternate color treatment for use on tinted or dark backgrounds. On a dark hero, the default Maryland blue is hard to see; `--alt` switches to white (or a lighter blue) underlined.

The link text itself is **not** styled (font-weight, family, size) by `usa-link` — it inherits from its parent. Inside `usa-prose`, that's Source Sans Pro 19.2px / 1.6 line-height.

## Variants

| Variant | Class | Visual |
|---|---|---|
| Default | `usa-link` (or bare `<a>` inside `usa-prose`) | Maryland blue, underlined |
| External | `usa-link usa-link--external` | Maryland blue + open-in-new icon after text |
| Alt | `usa-link usa-link--alt` | Lighter / white underlined, for dark backgrounds |

## When to use which variant

- **Default** — Most inline links. Inside `usa-prose` you can omit the class — `<a>` already gets the right styling.
- **External** — When the link points to a non-`maryland.gov` site or otherwise leaves the current site. Pair with `target="_blank"` and `rel="noreferrer"` (or `rel="noopener"`). The icon signals "this opens elsewhere".
- **Alt** — Inside a dark-background section (e.g., agency footer, dark hero). The default Maryland blue link fails contrast against navy; `--alt` flips to a light color.

## Default markup

Bare link inside body content (works inside `usa-prose` without the helper class):

```html
<div class="usa-prose">
  <p>
    Visit the
    <a href="/parks">Maryland State Parks directory</a>
    to find a park near you.
  </p>
</div>
```

Outside `usa-prose`, add the class explicitly:

```html
<p>
  Read the
  <a class="usa-link" href="/about">DNR mission statement</a>.
</p>
```

## Markup — external

```html
<p>
  For federal fishing regulations, see the
  <a
    class="usa-link usa-link--external"
    href="https://www.fisheries.noaa.gov/"
    target="_blank"
    rel="noreferrer"
  >NOAA Fisheries site</a>.
</p>
```

The `target="_blank"` opens the link in a new tab; `rel="noreferrer"` prevents the new page from accessing `window.opener` and from leaking the referer header. The `--external` icon does **not** auto-open in a new tab — the modifier is purely visual. Set `target` and `rel` yourself.

## Markup — alt (on dark background)

```html
<section class="bg-primary-darker padding-y-6 text-white">
  <p>
    Read the
    <a class="usa-link usa-link--alt" href="/strategic-plan">
      department strategic plan
    </a>
    for fiscal year 2026.
  </p>
</section>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-link` | Applies the USWDS link style: color `primary` (Maryland blue), underline-on-rest (not just on hover), hover deepens to `primary-dark`, focus shows the 2px focus ring. Inherits all typography from parent. |
| `usa-link--external` | Adds an open-in-new icon (Material Symbols `open_in_new`) after the text via `::after` pseudo. Icon color matches link text. **Purely visual** — does not change link behavior; set `target="_blank"` and `rel` yourself. |
| `usa-link--alt` | Alternative color treatment for dark backgrounds. Switches link color to a lighter shade (USWDS uses `base-lightest` / white) while keeping the underline. Hover deepens slightly. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `label` | string | `"Inline link"` | The text content of the `<a>`. |
| `href` | string | `"#"` | Destination URL. |
| `external` | boolean | `false` | When true, adds `usa-link--external` class and `rel="noreferrer"`. |
| `target` | `_self` \| `_blank` | `_self` | `_blank` opens in a new tab. Pair with `external: true` for the right visual + behavior combo. |

## Accessibility

- **Underline matters.** Don't remove the underline — color alone is not sufficient to mark a link (WCAG 1.4.1). The CDN already underlines `usa-link`; don't add `text-no-underline`.
- **External link warning** — When opening in a new tab, screen reader users should know. Either:
  - Use `usa-link--external` (the icon is announced as decoration but the visual cue is there for sighted users), and add a screen-reader-only suffix like `<span class="usa-sr-only">(opens in new tab)</span>` to the link text; **or**
  - Add `aria-label` to the link that includes "opens in new tab".
- **`rel` attribute** — Always pair `target="_blank"` with `rel="noreferrer"` or `rel="noopener"`. Without it, the new page can manipulate `window.opener`.
- **Meaningful link text** — Don't use "click here" or "read more". The link text should make sense out of context (screen readers can list all links on a page). Prefer "Read the strategic plan" over "click here to read".
- **Focus visible** — The global 2px Maryland blue focus ring is applied automatically. Don't override `outline: none`.

## JS requirements

None. `usa-link` is pure CSS applied to an `<a>` element. The `--external` icon is rendered via a `::after` pseudo-element — no JS, no markup change.

## Common mistakes

1. **`text-no-underline` on a link** — Removes the underline → fails WCAG 1.4.1. The only acceptable case is when the link sits in a navigation list (header nav, footer nav) where alternative styling (bold, separator) makes the linkness obvious; for body text, always keep the underline.
2. **`usa-link--external` without `target="_blank"`** — The icon promises "opens in new tab"; if it opens in the current tab, the icon lies. Either set `target="_blank"` or drop the `--external` class.
3. **`target="_blank"` without `rel="noreferrer"`** — Security vulnerability. Always pair them.
4. **Using `usa-link` on a `<button>`** — `usa-link` is for `<a>` elements. If you need a link-styled button, use `usa-button usa-button--unstyled` instead.
5. **`href="#"` placeholders** — A link with `href="#"` jumps the page to the top. Use `href="javascript:void(0)"` for prototypes if needed, but in production code, either give it a real URL or convert to a `<button>`.
6. **Forgetting `usa-link` outside `usa-prose`** — A bare `<a>` outside a `usa-prose` wrapper renders with browser-default styling (often purple visited, blue unvisited, no Maryland color). Add the `usa-link` class.
7. **Using `usa-link--alt` on a light background** — The lighter color disappears. Only use it on `bg-primary-darker`, `bg-base-darkest`, or other dark sections.
