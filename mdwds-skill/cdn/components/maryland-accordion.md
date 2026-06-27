# maryland-accordion

Maryland Design System accordion is a collapsible content component for FAQs, supplementary details, and any "lots of related sections, only one or two interesting at a time" pattern. Built on the USWDS accordion behavior with Maryland-namespaced classes and styling.

> **Use `maryland-accordion` instead of `usa-accordion` on Maryland-branded pages.** Same accessibility behavior; Maryland-themed colors and typography. For a single dismissable detail row, use a native `<details>` element inside `usa-prose` instead.

## What it looks like

An accordion is a `<section>` with a Maryland-themed header (`<h2>` Merriweather, body paragraph) above a stack of accordion items. Each item is:

- A heading (`<h2>`–`<h6>`, configurable via `headingLevel`; defaults to `<h4>`) containing a full-width `<button>` (the accordion trigger).
- A panel `<div role="region">` immediately below, holding the content (HTML content inside `usa-prose`).

The trigger has:

- 24px vertical padding, no left padding, no border. body-`lg` font size (~20–22px) with 4px line-height ratio.
- A 1px `base-light` bottom border (and on the first item, a matching top border).
- A `+` icon on the right (Material Symbols `add`) when collapsed, `-` (Material Symbols `remove`) when expanded.
- On hover (collapsed): a 3px `blue-60v` bottom border replaces the 1px line, and the `+` icon turns Maryland blue.
- When expanded: a 3px `gray-90` (near-black) top border replaces the 1px line, marking the active section clearly.
- Focus outline: 4px `blue-40v` outline on `focus-visible`.

There's a `bordered` variant that wraps the whole accordion in an additional `gray-cool-20` border with rounded corners — used when the accordion sits in a less-structured page area and needs more visual containment.

The component requires `mdwds-core.js` to be loaded — the open/close behavior is wired up by the MDWDS JS bundle. Without the script, only the initial `open: true` items are visible.

## Variants

| Variant | Visual |
|---|---|
| `default` | The canonical MDWDS accordion — no outer border, items separated by 1px `base-light` rules, flush-left button text (no inner padding inset from container edge), `+` / `–` glyph at far right. This is what the Storybook "Accordion" page shows by default and what most Maryland.gov pages use. |
| `bordered` | Adds left/right/bottom borders to the **content panel only** (the button row keeps its rule treatment). Same overall shape, slight extra chrome around the expanded body. Use when the surrounding context makes the default rule-only look ambiguous (e.g., a dense page with many adjacent rule lines from other components). |

**Use `default` for almost all FAQ-style accordions** — it matches the Storybook visual exactly. Reach for `--bordered` only when the surrounding page makes the standalone rules visually ambiguous.

## When to use

- FAQs on a service page.
- Long-form policy/regulation text broken into navigable subsections.
- "More about this program" panels at the bottom of a hero page.
- Multi-step instructions where each step has expandable detail.

Avoid accordions for content that should be visible by default (most users won't expand collapsed content). Don't use for primary navigation.

## Default markup

The canonical MDWDS accordion is intentionally minimal: each item is a button row separated by 1px `base-light` rules, with flush-left text and no inner padding around the expanded content. This matches the Storybook reference exactly. Don't reach for `--bordered` unless the surrounding context demands more visual containment.

```html
<section class="maryland-accordion" aria-labelledby="acc-1">
  <div class="maryland-accordion__list">
    <h2 id="acc-1" class="maryland-accordion__list--heading">Frequently asked questions</h2>
    <p class="maryland-accordion__list--content">Common questions about applying for a Maryland fishing license.</p>
  </div>
  <div class="maryland-accordion__items">
    <div class="maryland-accordion__item">
      <h3 class="maryland-accordion__heading">
        <button id="btn-1" type="button" class="maryland-accordion__button" aria-expanded="true" aria-controls="panel-1">
          Who needs a Maryland fishing license?
        </button>
      </h3>
      <div id="panel-1" class="maryland-accordion__content" role="region" aria-labelledby="btn-1">
        <div class="usa-prose">
          <p>Anyone 16 or older fishing in Maryland's tidal or non-tidal waters needs a fishing license. Special exemptions apply for residents 65+ on Free Fishing Days.</p>
        </div>
      </div>
    </div>
    <div class="maryland-accordion__item">
      <h3 class="maryland-accordion__heading">
        <button id="btn-2" type="button" class="maryland-accordion__button" aria-expanded="false" aria-controls="panel-2">
          How much does a license cost?
        </button>
      </h3>
      <div id="panel-2" class="maryland-accordion__content" role="region" aria-labelledby="btn-2" hidden>
        <div class="usa-prose">
          <p>Resident annual licenses are $20.50. Non-resident annual is $30.50. Multi-year and short-term options are also available — see the <a href="/dnr/fees">fee table</a>.</p>
        </div>
      </div>
    </div>
    <div class="maryland-accordion__item">
      <h3 class="maryland-accordion__heading">
        <button id="btn-3" type="button" class="maryland-accordion__button" aria-expanded="false" aria-controls="panel-3">
          What documents do I need?
        </button>
      </h3>
      <div id="panel-3" class="maryland-accordion__content" role="region" aria-labelledby="btn-3" hidden>
        <div class="usa-prose">
          <p>A government-issued photo ID and your Social Security number. Maryland residency proof is required for resident rates.</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

## Markup — bordered variant

Add `maryland-accordion--bordered` to the section. The button rows stay the same; only the **expanded content panel** picks up left/right/bottom borders. The overall layout doesn't change much — this is a subtle option, not a full card-style restyle.

```html
<section class="maryland-accordion maryland-accordion--bordered" aria-labelledby="acc-2">
  <!-- same inner structure as default -->
</section>
```

## Heading level adjustment

Each accordion trigger is wrapped in a heading element. MDWDS defaults to `<h4>` per USWDS convention (accordions usually sit beneath an `<h2>` section + `<h3>` sub-heading). Configure via the `headingLevel` arg (`h1`–`h6`).

The section's own heading (`maryland-accordion__list--heading`) defaults to `<h2>`. If the accordion sits inside an existing `<h2>` section, demote that to `<h3>` and bump the trigger headings to `<h5>` to preserve a sequential outline.

## What each class does

| Class | Effect |
|---|---|
| `maryland-accordion` | Base `<section>`. Applies `block-spacing` and `grid-container('tablet-lg')` so the accordion stays inside a 1024px container. |
| `maryland-accordion--bordered` | Adds an outer `gray-cool-20` border and rounded corners around the whole component. |
| `maryland-accordion__list` | The header wrapper for title + description. |
| `maryland-accordion__list--heading` | The header `<h2>`. Uses the `h2` mixin (Merriweather, 32–48px). 32px bottom margin. |
| `maryland-accordion__list--content` | Header description paragraph. Uses `paragraph-text` mixin (16–22px responsive). 48/64px bottom margin. |
| `maryland-accordion__items` | Container for the accordion items. |
| `maryland-accordion__item` | Each item wrapper. Holds the heading + panel. |
| `maryland-accordion__heading` | The heading element wrapping the trigger (h1–h6). No visual override; the inner button does the styling. |
| `maryland-accordion__button` | The trigger `<button>`. Full-width, transparent background, no border. body-`lg` font, 24px vertical padding. 1px `base-light` bottom border (top border on first item). Has a `+` icon (collapsed) / `-` icon (expanded) on the right. Hover/active state changes the bottom border to 3px Maryland blue (collapsed) or top border to 3px `gray-90` (expanded). Focus-visible: 4px `blue-40v` outline. |
| `maryland-accordion__content` | The panel `<div>`. Hidden when collapsed (via `hidden` attribute toggled by JS). When visible, the inner `.usa-prose` provides paragraph + list typography. Has `role="region"` and `aria-labelledby` pointing at the trigger so screen readers identify the panel. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `default` \| `bordered` | `default` | Outer border style. |
| `accordionListTitle` | string | sample | Header title. |
| `accordionListDescription` | string | sample | Header description. |
| `items` | `Array<{title, content, open}>` | sample | Accordion items. `content` is rendered as HTML. `open: true` marks the item expanded on initial render. |
| `headingLevel` | `h1` \| `h2` \| `h3` \| `h4` \| `h5` \| `h6` | `h4` | Heading level for each trigger. |
| `ariaLabel` | string | — | Optional `aria-label` on the section landmark. |
| `role` | `none` \| `group` \| `region` | `none` | Optional `role` on the section. Use `group` if items are logically related sub-controls; otherwise omit. |

## Common mistakes

1. **Forgetting to load `mdwds-core.js`** — without the script, the expand/collapse JS doesn't fire. Only the items with `aria-expanded="true"` (and unhidden panels) are visible.
2. **Mismatching `aria-controls` and panel `id`** — the trigger's `aria-controls` must equal the panel's `id`. Same for `aria-labelledby` on the panel pointing at the trigger's `id`.
3. **Default-expanded *every* item** — defeats the purpose of an accordion. Pick zero or one to expand by default.
4. **Heading inside the trigger button** — the heading wraps the button, not the other way around. The button is what's interactive.
5. **Using `usa-accordion` markup with `maryland-accordion` classes** — different DOM. Pick one component family.
6. **Trigger labels longer than ~80 characters** — long button text reads as wall-of-text in screen readers. Keep questions short and scannable.
7. **Skipping the `<div class="usa-prose">` inside the panel** — without `usa-prose`, body text inside the panel loses paragraph/list styling.
