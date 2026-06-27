# usa-process-list

A vertical numbered list that guides users through a sequence of steps. Each step has a circled step number on the left and a heading + optional description on the right. Use for multi-step applications, onboarding, "how to apply" pages, and any sequential workflow.

> The MDWDS-original `maryland-step-list` covers similar use cases with a Maryland visual treatment. `usa-process-list` is the plainer USWDS structure: a numbered circle marker with the column of step content beside it. Both are valid on Maryland pages — pick based on visual fit (`maryland-step-list` for marketing-style flows, `usa-process-list` for plainer body-text process descriptions). See `cdn/component-index.md`.

## What it looks like

A `usa-process-list` is an `<ol>` rendered without the default numeric markers. Each `<li class="usa-process-list__item">` is a flex/grid row with:

1. **Numbered marker** (auto-generated) — A circular outline (USWDS `1px solid` primary border) on the left containing the step number, ~32–40px diameter, centered text in the primary color. The numbering is automatic via CSS counter on the `<ol>` — you do not write the numbers in markup.
2. **Step body** — On the right, a heading (`usa-process-list__heading`, default `<h4>`) at the top followed by an optional paragraph description. Headings are weighted bold, slightly larger than body text (~22px). The body is connected to the next step's marker by a **vertical guide line** drawn on the left edge of the content column, anchoring the visual flow.

The vertical guide line is the most distinctive visual cue — it runs from one step's circle down to the next, making the list read as a connected process rather than a series of disconnected blocks.

Steps stack vertically; the marker column has a fixed width and the body fills remaining space.

## Variants

The MDWDS Storybook exposes three documented variants — these aren't true CSS modifiers; they're rendering toggles:

| Variant | Effect |
|---|---|
| `default` | Heading + description paragraph per step. Standard appearance. |
| `no-text` | Step titles only, rendered as `<p class="usa-process-list__heading font-sans-xl line-height-sans-1">` for tight, headline-sized rows. |
| `custom-sizing` | Headings get `font-sans-xl line-height-sans-1` (display-sized) and descriptions use `font-sans-lg` with `text-light`. Use for hero-style process showcases. |

You can also just hand-author the markup with any combination of heading levels and body content.

## When to use it

- **"How to apply" pages** — break the application into 3–6 numbered steps.
- **Eligibility flows** — sequential decision steps users follow.
- **Onboarding** — multi-stage account setup.

Avoid for:
- Lists where order doesn't matter — use `usa-list` or `usa-icon-list`.
- Single-action callouts — use `maryland-callout` or `usa-summary-box`.

## Default markup

```html
<ol class="usa-process-list">
  <li class="usa-process-list__item">
    <h4 class="usa-process-list__heading">Confirm your eligibility</h4>
    <p class="usa-margin-top-05">
      Maryland residents who have worked at least 680 hours in the past 18 months may qualify for unemployment insurance.
    </p>
  </li>
  <li class="usa-process-list__item">
    <h4 class="usa-process-list__heading">Gather your documents</h4>
    <p class="usa-margin-top-05">
      Have your Social Security number, recent pay stubs, employer addresses, and bank account info ready before you start.
    </p>
  </li>
  <li class="usa-process-list__item">
    <h4 class="usa-process-list__heading">Apply in BEACON</h4>
    <p class="usa-margin-top-05">
      Submit your initial claim through the BEACON portal at <a class="usa-link" href="https://beacon.labor.maryland.gov">beacon.labor.maryland.gov</a>. Most users finish in 20 minutes.
    </p>
  </li>
  <li class="usa-process-list__item">
    <h4 class="usa-process-list__heading">File a weekly claim</h4>
    <p class="usa-margin-top-05">
      Within 7 days of approval, log in each week to certify your eligibility and report any earnings. Payments arrive within 2–3 business days of certification.
    </p>
  </li>
</ol>
```

The numbers `1.`, `2.`, `3.`, `4.` are drawn automatically by the component's CSS counter — do not write them.

## Markup — no-text variant (titles only)

```html
<ol class="usa-process-list">
  <li class="usa-process-list__item usa-padding-bottom-4">
    <p class="usa-process-list__heading font-sans-xl line-height-sans-1">
      Confirm eligibility
    </p>
  </li>
  <li class="usa-process-list__item usa-padding-bottom-4">
    <p class="usa-process-list__heading font-sans-xl line-height-sans-1">
      Apply in BEACON
    </p>
  </li>
  <li class="usa-process-list__item usa-padding-bottom-4">
    <p class="usa-process-list__heading font-sans-xl line-height-sans-1">
      File weekly claims
    </p>
  </li>
</ol>
```

## Markup — custom-sizing variant (display-style)

```html
<ol class="usa-process-list">
  <li class="usa-process-list__item usa-padding-bottom-4">
    <h4 class="usa-process-list__heading font-sans-xl line-height-sans-1">
      Reserve your campsite
    </h4>
    <p class="font-sans-lg usa-margin-top-1 text-light">
      Browse availability at any of Maryland's 51 state parks and reserve up to 12 months in advance.
    </p>
  </li>
  <li class="usa-process-list__item usa-padding-bottom-4">
    <h4 class="usa-process-list__heading font-sans-xl line-height-sans-1">
      Pay your fee
    </h4>
    <p class="font-sans-lg usa-margin-top-1 text-light">
      Standard sites start at $25/night. Maryland residents and seniors receive automatic discounts at checkout.
    </p>
  </li>
  <li class="usa-process-list__item usa-padding-bottom-4">
    <h4 class="usa-process-list__heading font-sans-xl line-height-sans-1">
      Receive your confirmation
    </h4>
    <p class="font-sans-lg usa-margin-top-1 text-light">
      A confirmation email arrives within 5 minutes and includes your reservation number, site map, and check-in instructions.
    </p>
  </li>
</ol>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-process-list` | The `<ol>` wrapper. Removes default numeric markers (`list-style: none`), enables a CSS counter that drives the per-item circle number, draws the vertical connecting guide-line on the left side of the content column. |
| `usa-process-list__item` | One step. Increments the CSS counter that produces the circled number. Adds bottom padding to space steps apart, has a left-side padding that leaves room for the circle and the guide line. The circle is generated via a `::before` pseudo-element containing `counter(...)` content. |
| `usa-process-list__heading` | The step title. `<h4>` element by default. Rendered larger and bolder than body type so the step name stands above its description. With `font-sans-xl` and `line-height-sans-1` utilities (used in the `no-text` and `custom-sizing` variants) it becomes a display-sized headline. |
| `usa-padding-bottom-4` | Adds 32px bottom padding to a step (used in the no-text and custom-sizing variants for breathing room when descriptions are absent). |
| `usa-margin-top-05` | Adds 4px top margin to the description paragraph so it sits tight beneath the step heading. |
| `usa-margin-top-1` | Adds 8px top margin (custom-sizing variant) — slightly looser spacing for larger type. |
| `font-sans-xl` | Display-sized type utility (~32px / ~1.41rem). Combined with `line-height-sans-1` for tight headline leading. |
| `font-sans-lg` | Body-large size utility (~22px). |
| `text-light` | Sets `font-weight: 300` for the lighter display weight used in the custom-sizing variant. |

The circle marker and connector line do not have their own dedicated classes — they're generated from the parent `usa-process-list` rules via `::before` pseudo-elements and a sibling-based vertical guide.

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `default` \| `no-text` \| `custom-sizing` | `default` | Toggles between heading+body, heading-only, and display-sized layouts |
| `steps` | `[{ title, text? }]` | sample | Each step object has a `title` (string) and optional `text` (description string) |

## Heading level adjustment

`usa-process-list__heading` is rendered as `<h4>` in the default variant and as a `<p>` in `no-text`. **For accessibility, pick the heading element that matches the page outline**: if the process list is the body of an `<h2>` section, each step heading should be `<h3>`. The `usa-process-list__heading` class can be applied to any heading element (`<h2>`–`<h6>`) or even a `<p>` for the no-text variant — what controls the visual is the class, not the element. See `cdn/composition.md`.

## Common mistakes

1. **Writing the step numbers manually** (`<h4>1. Confirm eligibility</h4>`) — the component generates them. You'll end up with `1. 1.` doubled.
2. **Using `<ul>` instead of `<ol>`** — breaks the CSS counter; markers won't appear.
3. **Wrapping steps in extra `<div>`s** — the connector line and counter depend on `<li>` being a direct child of `<ol class="usa-process-list">`.
4. **Mixing `usa-process-list` with `maryland-step-list` markup** — different components, different DOM. Pick one.
5. **Putting interactive content inside the heading** — accessible heading semantics get muddled. Put buttons/links in the description, not the heading.
6. **Skipping bottom padding on `no-text` items** — without `usa-padding-bottom-4`, rows collapse together because there's no description to add height.
7. **Picking `custom-sizing` on a narrow column** — the display-sized headlines wrap awkwardly. Use the default variant for sidebar widths.
