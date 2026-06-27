# maryland-step-list

Maryland Design System step list displays a vertical sequence of steps with a connecting accent line down the left side. Each step has a heading, body content (rich text allowed), and optional buttons. The list can be presented with numbered markers (large blue circles with the step number) or smaller dot markers (Maryland-gold/secondary circles).

> **Use `maryland-step-list` for "how to do X" multi-step guides on Maryland.gov pages.** For an at-a-glance USWDS-style process indicator, use `usa-process-list`. For a service-hub layout with multiple parallel options, use `maryland-action-items`.

## What it looks like

The step list is a `<section>` with:

- An optional header containing a section title (`<h2>`, Merriweather, `h2` mixin), description paragraph, and a button group with primary/outline action buttons.
- A vertical list of steps below. Steps stack on top of each other; a thin `info-lighter` (light info-blue) vertical bar connects each step's marker to the next.

Each step has:

- A circular marker on the left edge.
  - **Numbered** variant: 48px blue (`secondary`) circle containing the step number in semibold white text (16px on mobile, 22px at tablet).
  - **Bullet** variant: 24px Maryland-gold (`secondary`) dot.
- A step title (`<h3>`) — heading-10 (24px) Merriweather light, `ls(1)` letter-spacing. Sits inline with the marker.
- A body block (`__body` with `usa-prose`) that holds rich text content — paragraphs, lists, links, emphasis.
- Optional button row at the bottom of the body — primary + outline `usa-button--big` buttons.

The vertical accent line continues between steps via a `::before` pseudo on each non-last step. The line color is `info-lighter` and sits at the same x-position as the marker (8px on bullet, 12/20px on numbered).

The list is responsive: the bar's x-offset and the body's left-padding adjust at the `tablet` (640px) breakpoint. Gap between steps is 16px below; the body itself has 16/32px vertical margin.

## Variants

| Variant | Marker | Visual |
|---|---|---|
| `maryland-step-list--number` (`listType: "number"`) | 48px blue circle with the step number | Used when the process is strictly sequential — order matters. |
| `maryland-step-list--bullet` (`listType: "bullet"`) | 24px gold dot | Used when the items are sequential but the count doesn't add information ("Things to check"). |

## When to use

- "How to apply for a Maryland fishing license" — numbered.
- "Before you arrive at the MVA branch" — bullet.
- Onboarding flows, application checklists, multi-page form intros.

Avoid step lists when the content isn't sequential — use `maryland-icon-list`, `maryland-link-collection`, or a `<ul>` inside `usa-prose` instead.

## Default markup — numbered

```html
<section class="maryland-step-list maryland-step-list--number" aria-labelledby="sl-1">
  <div class="maryland-step-list__header">
    <h2 class="maryland-step-list__title" id="sl-1">How to apply for a Maryland fishing license</h2>
    <p class="maryland-step-list__description">
      Four short steps. Have your ID and Social Security number handy.
    </p>
    <div class="maryland-step-list__links">
      <a href="/dnr/apply" class="usa-button usa-button--big">Start an application</a>
      <a href="/dnr/help" class="usa-button usa-button--big usa-button--outline">Get help</a>
    </div>
  </div>
  <ol class="maryland-step-list__steps">
    <li class="maryland-step">
      <h3 class="maryland-step__title">Gather required documents</h3>
      <div class="maryland-step__body usa-prose">
        <p>You'll need a government-issued photo ID and your Social Security number.</p>
        <p><strong>Documents accepted:</strong></p>
        <ul>
          <li>Maryland driver's license</li>
          <li>U.S. passport</li>
          <li>Military ID</li>
        </ul>
      </div>
    </li>
    <li class="maryland-step">
      <h3 class="maryland-step__title">Choose your license type</h3>
      <div class="maryland-step__body usa-prose">
        <p>Freshwater, tidal (saltwater), or bay-sport. <a href="/dnr/licenses/types">Compare options</a>.</p>
      </div>
    </li>
    <li class="maryland-step">
      <h3 class="maryland-step__title">Submit and pay the fee</h3>
      <div class="maryland-step__body usa-prose">
        <p>Payment accepted online via card or e-check.</p>
        <div class="maryland-step__buttons">
          <a href="/dnr/checkout" class="usa-button usa-button--big">Pay now</a>
          <a href="/dnr/fees" class="usa-button usa-button--big usa-button--outline">View fee table</a>
        </div>
      </div>
    </li>
    <li class="maryland-step">
      <h3 class="maryland-step__title">Print or save your license</h3>
      <div class="maryland-step__body usa-prose">
        <p>You'll receive a confirmation email. Print the license PDF or save it to your phone.</p>
      </div>
    </li>
  </ol>
</section>
```

For numbered, the `<ol>` is intentional — semantic order matches visual order.

## Markup — bullet variant

```html
<section class="maryland-step-list maryland-step-list--bullet" aria-labelledby="sl-2">
  <div class="maryland-step-list__header">
    <h2 class="maryland-step-list__title" id="sl-2">Before you visit an MVA branch</h2>
  </div>
  <ul class="maryland-step-list__steps">
    <li class="maryland-step">
      <h3 class="maryland-step__title">Make an appointment</h3>
      <div class="maryland-step__body usa-prose">
        <p>Walk-ins are accepted but appointment holders are served first.</p>
      </div>
    </li>
    <li class="maryland-step">
      <h3 class="maryland-step__title">Bring two proofs of address</h3>
      <div class="maryland-step__body usa-prose">
        <p>Examples: a utility bill, bank statement, or lease.</p>
      </div>
    </li>
    <li class="maryland-step">
      <h3 class="maryland-step__title">Allow 60–90 minutes</h3>
      <div class="maryland-step__body usa-prose">
        <p>Most appointments take less, but plan for some buffer.</p>
      </div>
    </li>
  </ul>
</section>
```

Use a `<ul>` for the bullet variant.

## Markup — no header

```html
<section class="maryland-step-list maryland-step-list--bullet">
  <ol class="maryland-step-list__steps">
    <!-- maryland-step items -->
  </ol>
</section>
```

Omit `<div class="maryland-step-list__header">` when the surrounding page already provides context.

## What each class does

| Class | Effect |
|---|---|
| `maryland-step-list` | Base `<section>`. Applies `block-spacing` vertical rhythm. Display flex column with 48/64px gap between header and step list. Sets a `counter-reset: steps` so the numbered marker can count items. |
| `maryland-step-list--number` | Numbered variant. Step markers display the step counter (48px filled circle with white number). Adjusts left-padding and bar position. |
| `maryland-step-list--bullet` | Bullet variant. Step markers are 24px gold dots. |
| `maryland-step-list__header` | Optional header block. No styling on its own — used as a structural container. |
| `maryland-step-list__title` | Header `<h2>`. Uses the `h2` mixin (Merriweather, 32–48px). Zero margin. |
| `maryland-step-list__description` | Header paragraph. body-6 (20px), `base-darkest`. 16px top margin. |
| `maryland-step-list__links` | Header button group. Flex row with 16px gap, wraps. 32px top margin. |
| `maryland-step-list__steps` | The step container (`<ol>` or `<ul>`). List-style none, no margin/padding, display flex column. |
| `maryland-step` | Each step. Counter-increments `steps`. Position relative. Flex column with 16px gap. Adjacent steps get 16px top margin. Each non-last step has a `::before` vertical bar (`info-lighter`, 8px wide, full height minus the marker) that connects to the next step. |
| `maryland-step__title` | Step heading (`<h3>`). Heading-10 (24px) Merriweather light, `ls(1)`. Pseudo-element `::before` is the circular marker (gold for bullet, blue for number). Adds 40/48px left padding to make room for the marker. |
| `maryland-step__body` | Step body. Combines with `usa-prose` so paragraphs, lists, links, etc. pick up Maryland prose styling. Adds 40/48px left padding (aligned under the title) and 16/32px vertical margin. |
| `maryland-step__buttons` | Optional button row inside the body. Flex row with 16px gap, wraps. 32px top margin. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `listType` | `bullet` \| `number` | `bullet` | Variant. |
| `title` | string | sample | Section heading. Show/hide via `showTitle`. |
| `showTitle` | bool | true | Storybook toggle. |
| `description` | string | sample | Header description. Show/hide via `showDescription`. |
| `showDescription` | bool | true | Storybook toggle. |
| `links` | `Array<{text, url, variant?: "primary" \| "outline"}>` | — | Header buttons. Show/hide via `showButtons`. |
| `showButtons` | bool | true | Storybook toggle. |
| `steps` | `Array<{title, content: HTML, buttons?: Array<{text, url, variant}>}>` | sample | Steps. `content` is rendered via `unsafeHTML`. |

## Heading level adjustment

- `maryland-step-list__title` defaults to `<h2>`.
- `maryland-step__title` defaults to `<h3>`.

If the step list is nested inside another `<h2>`-headed section, demote the list title to `<h3>` and step titles to `<h4>`. Keep classes — they control styling.

## Common mistakes

1. **Using `<ul>` for the numbered variant** — for semantic correctness, the numbered variant should be `<ol>`. The CSS still works on either, but `<ol>` matches the meaning.
2. **Skipping `usa-prose` on `__body`** — the body relies on `usa-prose` styling for paragraph + list rendering. Without it, body text looks unstyled.
3. **More than ~6 steps** — gets visually overwhelming. Break into multiple sections or summarize.
4. **Step content longer than 2-3 short paragraphs** — the design assumes a scannable flow. For deep content, use `maryland-accordion` or a multi-page layout.
5. **Putting buttons in `__body` directly** — they need the `__buttons` wrapper for spacing and flex layout.
6. **Inline-styling the marker color** — comes from the variant class. Choose the right variant rather than recoloring.
7. **Forgetting `aria-labelledby` on the section** — pair it with the title id when a title is present.
