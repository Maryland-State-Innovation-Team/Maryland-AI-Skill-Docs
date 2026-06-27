# usa-summary-box

The USWDS summary box highlights key information in a visually prominent container at the top of a page or section: a list of action items, key takeaways, or the most important links a user needs.

> **Prefer `maryland-summary-box` on Maryland.gov pages.** `usa-summary-box` and `maryland-summary-box` share the same general idea but use different class namespaces and different visual tuning. The MDWDS-original `maryland-summary-box` is the canonical "what you need to know" box on Maryland-branded pages. Use `usa-summary-box` only in internal tools or USWDS-style microsites where Maryland theming is intentionally absent.

## What it looks like

A `usa-summary-box` is a `<div>` panel with a pale primary-tinted background (USWDS `primary-lighter`, a soft blue ~`#d9e8f6`), a thin left or full border in primary blue, generous internal padding (~24px), and a clear heading at the top. Below the heading sits a body region — typically a `<ul class="usa-list">` of action items or links, each link rendered in the USWDS primary blue with an underline.

The heading (`usa-summary-box__heading`, default `<h4>`) is sized larger than body text (~22px) and weighted semibold so the box reads as a callout. List items inside use the standard USWDS list styling — bullet markers in the secondary color, ~16px text. Links use the `usa-summary-box__link` class which underlines and colors them the same as `usa-link`.

The component is a `role="region"` with an `aria-label` so screen readers announce it as a distinct landmark.

## When to use it

- **Top of a long page** to surface a quick "do this now" list before the prose body.
- **After a hero** to give the user a list of the most common tasks (apply, renew, contact).
- **Inside a service page** to summarize eligibility or required documents.

If you have free-form prose with no list, use a `maryland-callout` or `maryland-highlight` instead.

## Default markup

```html
<div class="usa-summary-box" role="region" aria-label="Summary of important information">
  <div class="usa-summary-box__body">
    <h3 class="usa-summary-box__heading">What you need to apply for unemployment insurance</h3>
    <div class="usa-summary-box__text">
      <ul class="usa-list">
        <li><a class="usa-summary-box__link" href="/services/ui/eligibility">Confirm you're eligible</a></li>
        <li><a class="usa-summary-box__link" href="/services/ui/documents">Gather your Social Security number, pay stubs, and direct-deposit info</a></li>
        <li><a class="usa-summary-box__link" href="/services/ui/apply">Start your application in BEACON</a></li>
        <li><a class="usa-summary-box__link" href="/services/ui/weekly-claim">File a weekly claim within 7 days of approval</a></li>
      </ul>
    </div>
  </div>
</div>
```

The `aria-label` value is exposed to assistive technology — make it specific to the box's content ("Summary of unemployment-insurance steps") rather than the literal placeholder text shown above.

## Markup — with paragraph body (no list)

The text region accepts arbitrary markup. For a non-list summary, drop a paragraph in:

```html
<div class="usa-summary-box" role="region" aria-label="Storm preparedness summary">
  <div class="usa-summary-box__body">
    <h3 class="usa-summary-box__heading">Storm preparedness in Maryland</h3>
    <div class="usa-summary-box__text">
      <p>
        Sign up for <a class="usa-summary-box__link" href="/alerts">Maryland Emergency Alerts</a>,
        stock 72 hours of food and water, and review your evacuation route. Updates from MEMA are posted at
        <a class="usa-summary-box__link" href="https://mema.maryland.gov">mema.maryland.gov</a>.
      </p>
    </div>
  </div>
</div>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-summary-box` | Outer `<div>` panel. Sets pale primary-tint background (~`#d9e8f6`), primary-blue border, generous padding (~24px), and rounded corners per USWDS theme. Pairs with `role="region"` + `aria-label` for landmark navigation. |
| `usa-summary-box__body` | Inner wrapper holding heading + text. Provides the inner padding layout. |
| `usa-summary-box__heading` | Box title. `<h4>` element styled at ~22px semibold, color base-darkest. Sits at the top of the body with a small bottom margin separating it from the text region. |
| `usa-summary-box__text` | Body region. Wraps the list or paragraphs. Contains link styling overrides so descendant `<a>` tags align with the box's typography. |
| `usa-summary-box__link` | Link inside the summary box. Color primary, underlined, with hover/focus states tuned to the tinted background for sufficient contrast. |
| `usa-list` | Standard USWDS bulleted list used inside `__text`. Inherits secondary-color bullet markers and ~16px body text. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `heading` | string | `"Key information"` | Title text |
| `listItems` | array of `{ text, link }` | sample | Each item becomes `<li><a class="usa-summary-box__link" href="{link}">{text}</a></li>` |
| `regionLabel` | string | `"Summary of important information"` | Applied as `aria-label` on the outer div. Required for screen readers to announce the region. |

## Heading level adjustment

The default heading renders as `<h4>`. **Pick the level that matches the page outline** — when a summary box opens a page directly after the hero (so the box is the first major section), use `<h2 class="usa-summary-box__heading">`. When it's nested inside an `<h2>` section, use `<h3>`. See `cdn/composition.md`.

## Common mistakes

1. **Using `usa-summary-box` on a Maryland page** — switch to `maryland-summary-box` for the Maryland visual treatment.
2. **Omitting `role="region"` or `aria-label`** — the box is a landmark; without the label, screen reader users can't navigate to it semantically.
3. **Plain `<a>` (no `usa-summary-box__link`) inside the body** — links lose the box-tuned color and lose hover/focus contrast against the tinted background.
4. **Wrapping the box in `<aside>`** — that adds another landmark on top of the existing `role="region"` and confuses screen reader nav. Either use the role attribute (default) or switch to `<aside>` and drop the role — not both.
5. **Stuffing more than 5–6 list items inside** — the box is meant to be scannable. If the list is long, switch to a `usa-collection` or a `maryland-action-items`.
6. **Inline `<style>` to change the background color** — breaks the design system's contrast guarantees. The pale primary tint is intentional and paired with the link styling.
