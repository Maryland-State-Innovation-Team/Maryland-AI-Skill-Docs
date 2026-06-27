# usa-list

USWDS helper class for bulleted, numbered, and unstyled lists. This is the **list typography helper** — different from `usa-collection` (which is the vertical-articles component) and `usa-icon-list` (which adds icon prefixes). Reach for `usa-list` when you need to style plain `<ul>` / `<ol>` markup outside of `usa-prose`, or when you need an unstyled list (no bullets, no left padding).

> Inside a `usa-prose` block, `<ul>` and `<ol>` already get USWDS list styling automatically. You only need to apply `usa-list` to lists **outside** prose contexts (e.g., inside cards, callouts, or component bodies that aren't wrapped in `usa-prose`).

## What it looks like

- **Unordered list** (`<ul class="usa-list">`) — A bulleted list with secondary-colored bullet markers (Maryland gold/orange in the default theme), ~16px body text, `1.6` line-height, ~22px max line measure (USWDS `measure-5`), and ~8px space between items. Nested lists indent one level deeper using a hollow circle marker.
- **Ordered list** (`<ol class="usa-list">`) — A numbered list with decimal markers (`1.`, `2.`, `3.`) in the body text color. Nested ordered lists cycle through `lower-latin` (a, b, c) at level 2 and `lower-roman` (i, ii, iii) at level 3.
- **Unstyled list** (`<ul class="usa-list usa-list--unstyled">` or `<ol class="usa-list usa-list--unstyled">`) — Removes bullets/numbers, left padding, and all marker space. Effectively a `<div>` of items, but preserves the list's semantic meaning for assistive technology.

The list is left-aligned with a maximum measure (~75ch) so lines don't grow too long for comfortable reading.

## Variants

| Variant | Markup | Visual |
|---|---|---|
| Unordered | `<ul class="usa-list">` | Bulleted list, secondary-colored markers |
| Ordered | `<ol class="usa-list">` | Numbered list, decimal markers |
| Unstyled | `<ul class="usa-list usa-list--unstyled">` (or `<ol>`) | No markers, no left padding — semantic list without visual list styling |

## When to use which variant

- **Unordered** → Items where order doesn't matter (features, criteria, options).
- **Ordered** → Sequential steps where order matters. For visually distinct numbered workflows, prefer `usa-process-list`.
- **Unstyled** → A list embedded in component markup (cards, callouts) where bullets would clash with the surrounding design, or for navigation-style lists where you'll style each item independently.

## Default markup — unordered

```html
<ul class="usa-list">
  <li>Maryland driver's license or state ID</li>
  <li>Proof of Maryland residency (utility bill, lease, mortgage statement)</li>
  <li>Social Security number</li>
  <li>Vehicle title and current registration (if transferring a vehicle)</li>
</ul>
```

## Markup — ordered

```html
<ol class="usa-list">
  <li>Schedule your road test at <a class="usa-link" href="/mva/road-test">mva.maryland.gov/road-test</a>.</li>
  <li>Arrive 15 minutes early with your learner's permit and the vehicle you'll test in.</li>
  <li>Complete the test with an MVA-certified examiner.</li>
  <li>Pay the $9 driver's license fee and receive your interim license on-site.</li>
</ol>
```

## Markup — unstyled

```html
<ul class="usa-list usa-list--unstyled">
  <li><a class="usa-link" href="/services/dmv">Driver and vehicle services</a></li>
  <li><a class="usa-link" href="/services/tax">Tax and revenue</a></li>
  <li><a class="usa-link" href="/services/health">Health and human services</a></li>
  <li><a class="usa-link" href="/services/business">Business and licensing</a></li>
</ul>
```

## Markup — nested ordered list

```html
<ol class="usa-list">
  <li>
    Initial application
    <ol>
      <li>Complete Form MD-3001</li>
      <li>Provide proof of insurance</li>
      <li>Submit by mail or in person</li>
    </ol>
  </li>
  <li>Review and approval (typically 5–7 business days)</li>
  <li>License issuance</li>
</ol>
```

Nested `<ol>` cycles through decimal → lower-latin → lower-roman automatically; no extra classes needed.

## What each class does

| Class | Effect |
|---|---|
| `usa-list` | Applies USWDS list styling: ~16px body text, `1.6` line-height, ~22px max measure (USWDS `measure-5`), ~8px space between items, secondary-colored bullets for `<ul>` and decimal numerals for `<ol>`. |
| `usa-list--unstyled` | Removes all list markers, padding-left, and margin-left. Effectively makes the list visually un-list-like while keeping its semantics for screen readers. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `unordered` \| `ordered` \| `unstyled` | `unordered` | Selects the list tag and modifier class |
| `items` | string array | `["List item 1", "List item 2", "List item 3"]` | List item contents (rendered as plain text inside `<li>`) |
| `ariaLabel` | string | `""` | Optional `aria-label` for the list (use when a list has no surrounding heading) |
| `ariaDescribedBy` | string | `""` | Optional `aria-describedby` ID reference |

## Relationship to `usa-prose`

Inside a `<div class="usa-prose">`, plain `<ul>` and `<ol>` elements automatically receive equivalent styling — you do not need to add `usa-list`. The `usa-list` class is for lists **outside** `usa-prose`: in cards, in summary boxes, in component bodies, in headers, anywhere the prose wrapper isn't applied. See `cdn/composition.md` for the prose wrapper.

## Common mistakes

1. **Adding `usa-list` to lists inside `usa-prose`** — redundant; prose already styles them. Harmless but unnecessary.
2. **Confusing `usa-list` with `usa-collection`** — `usa-collection` is a structured vertical list of articles/events/news with metadata, not a typography helper. See `cdn/components/usa-collection.md`.
3. **Using `usa-list--unstyled` and then re-adding bullets via inline `<style>`** — defeats the purpose; just use `usa-list`.
4. **Confusing nested-list marker cycling with manual class control** — the decimal → lower-latin → lower-roman cycle is automatic for nested `<ol>`. Don't add a separate class on the nested list.
5. **Removing the `<ul>` / `<ol>` semantics in favor of `<div>` groups** — even an unstyled list keeps its semantics. Don't replace a list of items with a wall of `<div>`s.
6. **Using `usa-list` for sequential workflows** — a numbered process is more visually distinct as a `usa-process-list` (with circle markers and connector lines). See `cdn/components/usa-process-list.md`.
