# Composition — Spacing, Heading Hierarchy, Grid, and Prose

This file covers how components fit together on a page: vertical rhythm, heading levels, layout grid, and the prose wrapper. **Read this before placing any component inside `<main>` for the first time.**

## Heading hierarchy — the most common bug

Per-component reference files often show `<h2>` or `<h3>` inside example markup. **Do not copy those levels blindly.** Adjust them to match the page's heading outline.

### The rule

- The page has exactly one `<h1>` — almost always the hero title (`maryland-hero__title`).
- Each major section (`<section>` or component group) starts with `<h2>`.
- Sub-sections inside a section use `<h3>`, then `<h4>`, etc. — sequential, no skipping levels.
- The component reference files default to `<h3>` for component-level headings because they're usually nested inside an `<h2>`-led section. Adjust if not.

### Example outline

```
<h1> Department of Natural Resources                    ← hero title
  <h2> Featured services                                ← cards section
    <h3> Apply for a fishing license                    ← card title
    <h3> Find a state park                              ← card title
    <h3> Boating safety classes                         ← card title
  <h2> Latest news                                      ← listing section
    <h3> {article title}                                ← collection item
  <h2> Contact us                                       ← footer-like section
```

### When in doubt

- `maryland-card__heading` → defaults to `<h3>` in markup; adjust to `<h2>` if the card group **is** the section.
- `maryland-hero__title` → always `<h1>`.
- `usa-collection__heading` → defaults to `<h3>`; adjust based on context. The Collection component has a `headingLevel` arg in its story (h2–h6).
- `usa-accordion__heading` → defaults to `<h2>` (USWDS convention). Adjust if the accordion is nested.

## Vertical rhythm — `block-spacing` and `margin-y-*`

**Don't write `margin-top: 24px`-style attributes.** MDWDS provides spacing utilities that match the design system's vertical rhythm.

### `.block-spacing` — the default for component sections

Applied to a section wrapper, this gives MDWDS-correct vertical spacing between major page components.

| Viewport | Vertical margin (top + bottom) |
|---|---|
| Mobile | `units(6)` = **48px** |
| Mobile-lg (480px+) | `units(8)` = **64px** |
| Desktop (1024px+) | `units(15)` = **120px** |
| Inside a sidebar column | `units(4)` / `units(6)` / `units(8)` = 32/48/64px (via container queries) |

First child has `margin-block-start: 0` so the first section sits flush against the hero.

```html
<section class="block-spacing">
  <h2>Featured services</h2>
  <!-- cards -->
</section>

<section class="block-spacing">
  <h2>Latest news</h2>
  <!-- collection -->
</section>
```

### USWDS spacing utility classes

The full USWDS spacing scale is available. Each `units(N)` = `N * 8px`.

| Class | Effect |
|---|---|
| `margin-y-0` to `margin-y-15` | Vertical margin (top + bottom) at scale 0–15 (0px to 120px) |
| `margin-top-0` to `margin-top-15` | Top only |
| `margin-bottom-0` to `margin-bottom-15` | Bottom only |
| `margin-x-auto` | Horizontal center |
| `padding-y-*`, `padding-top-*`, etc. | Same scale for padding |
| `desktop:margin-top-10` | Responsive prefix — applies at the `desktop` breakpoint (1024px+) |
| `tablet:margin-y-8` | Applies at `tablet` (640px+) |
| `mobile-lg:margin-y-6` | Applies at `mobile-lg` (480px+) |

Scale reference: 1=8px, 2=16px, 3=24px, 4=32px, 5=40px, 6=48px, 7=56px, 8=64px, 9=72px, 10=80px, 11=88px, 12=96px, 13=104px, 14=112px, 15=120px.

### When to use which

- **Between major page sections in `<main>`** → `.block-spacing` (handles responsive)
- **Inside a section** → `margin-top-*` / `margin-bottom-*` on the individual element
- **Specific responsive override** → `margin-y-6 desktop:margin-y-10`
- **Never** → custom `margin` in a `style=""` attribute

## Layout grid

MDWDS uses the USWDS 12-column grid. Three utilities do almost everything:

| Class | Effect |
|---|---|
| `grid-container` | Max-width centered wrapper. Default max is `desktop-lg` (1400px). Use `grid-container="widescreen"` (1600px) where applicable. |
| `grid-row` | Direct flex/grid row. Add `grid-gap` for 16px gutters, `grid-gap-lg` for 32px. |
| `grid-col-N` | Span N of 12 columns. `grid-col-12` = full width, `grid-col-6` = half. Use responsive prefix to change span at breakpoint: `grid-col-12 desktop:grid-col-8`. |

### Sidebar + content layout

```html
<div class="grid-container">
  <div class="grid-row grid-gap">
    <aside class="grid-col-12 desktop:grid-col-3">
      <!-- maryland-sidenav -->
    </aside>
    <div class="grid-col-12 desktop:grid-col-8">
      <!-- main content -->
    </div>
  </div>
</div>
```

On mobile (<1024px), the sidebar and content stack full-width. At desktop, they sit side-by-side with the sidebar at 3/12 and content at 8/12 (a one-column gap is left for breathing room).

### Three-up cards

```html
<div class="grid-container">
  <div class="grid-row grid-gap">
    <div class="grid-col-12 tablet:grid-col-4">
      <!-- card 1 -->
    </div>
    <div class="grid-col-12 tablet:grid-col-4">
      <!-- card 2 -->
    </div>
    <div class="grid-col-12 tablet:grid-col-4">
      <!-- card 3 -->
    </div>
  </div>
</div>
```

**Note:** `maryland-card` components are usually wrapped in a `<ul class="maryland-card-group">` which handles its own grid layout. Don't manually wrap individual cards in `grid-col-*` — use the card-group wrapper.

## The `usa-prose` wrapper

When you have free-form body text (paragraphs, lists, links, headings together), wrap them in `<div class="usa-prose">`. This applies MDWDS typography defaults to everything inside:

- Source Sans Pro Web body font
- 19.2px body / 1.6 line-height (base), 22px at desktop
- Merriweather headings (h1–h3) with letter-spacing tuned for headings
- Bullet and ordered-list styling with secondary-color markers
- Link color = primary, with underline

```html
<div class="usa-prose">
  <h2>About this service</h2>
  <p>The Department of Natural Resources offers...</p>
  <ul>
    <li>First item</li>
    <li>Second item</li>
  </ul>
  <p>Contact us at <a href="#">info@dnr.maryland.gov</a>.</p>
</div>
```

Without `usa-prose`, browser default styles apply — text will look unstyled and links will be the wrong color.

**Use `usa-prose` for free-form text only.** Don't wrap entire component-driven pages in it; components handle their own typography.

## Common composition mistakes

1. **Skipping heading levels** — e.g. `<h1>` straight to `<h4>` because the card markup says `<h4>`. Always sequential.
2. **Multiple `<h1>` elements** — only one per page. Hero gets it.
3. **Custom margins on sections** — use `.block-spacing` or `margin-y-*` utilities. Inline `style="margin-top: 24px"` always wrong.
4. **Forgetting `grid-container` around `grid-row`** — without the container, content runs edge-to-edge of the viewport.
5. **Wrapping cards in `grid-col-*`** — use `<ul class="maryland-card-group">` instead; it handles columns.
6. **Putting `usa-prose` on a page-level wrapper** — it applies to free text only; let components style themselves.
7. **Inline `<style>` blocks to "fix spacing"** — almost always means a utility class would have worked. Re-read this file.

## Breakpoints

| Name | Min width | Use as prefix |
|---|---|---|
| (none) | 0 | bare class (`grid-col-12`) |
| `mobile-lg` | 480px | `mobile-lg:grid-col-6` |
| `tablet` | 640px | `tablet:grid-col-6` |
| `tablet-lg` | 880px | `tablet-lg:grid-col-6` |
| `desktop` | 1024px | `desktop:grid-col-8` |
| `desktop-lg` | 1200px | `desktop-lg:grid-col-8` |
| `widescreen` | 1400px | `widescreen:grid-col-8` |
