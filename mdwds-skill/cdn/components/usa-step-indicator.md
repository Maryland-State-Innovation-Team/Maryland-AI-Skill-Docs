# usa-step-indicator

The USWDS Step Indicator visualizes a user's progress through a multi-step process — a license application, a registration form, a wizard. It shows which step is current, which steps are complete, and what's still ahead. MDWDS uses the upstream USWDS component as-is, restyled by the MDWDS color tokens.

> There is no `maryland-step-indicator`. The `usa-step-indicator` is the canonical implementation for multi-step progress on Maryland.gov pages.

## What it looks like

A horizontal row of numbered segments sitting above the step content. Each segment is one step of the process and renders as a small circle (or number, depending on variant) connected to its neighbors by a thin horizontal line that runs through the row.

State by step:

- **Completed steps** — circle filled with primary blue (Maryland blue), white checkmark inside; the connector line to the next step is also primary blue.
- **Current step** — circle filled with primary blue with a slightly larger ring; the segment label below sits in `base-darkest` semibold, prefixed by a small "current step" sr-only token. The connector line going *into* this step is primary blue; the line going *out* is light gray.
- **Future / not-completed steps** — circle filled with light gray (`base-lighter`), no checkmark; connector line is light gray; label is in base color, regular weight.

Below the segments row, a heading line reads e.g. **"Step 3 of 5: Vehicle details"** — large semibold text combining a step counter and the current step label. On mobile, the segment row collapses to a compact bar (just the dots and connector lines, no labels by default below mobile-lg) and the "Step N of M" heading does the heavy lifting.

The whole component is a `<div class="usa-step-indicator">` wrapping an `<ol class="usa-step-indicator__segments">` (the dots) plus a `<div class="usa-step-indicator__header">` (the heading line). The list is ordered because step order is meaningful.

## Variants

Set modifier classes on the `.usa-step-indicator` element. They are additive.

| Variant | Class | Visual |
|---|---|---|
| Default (labels only) | `usa-step-indicator` | Circle dots + step labels below each circle. No numbers in the circles. |
| With counters | `usa-step-indicator--counters` | Numbers (1, 2, 3...) shown inside each circle. Circles become larger to fit. |
| Small counters | `usa-step-indicator--counters-sm` | Same as counters, but smaller circle size — denser. |
| No labels | `usa-step-indicator--no-labels` | Hide the per-step labels below the row. The "Step N of M: {label}" heading still appears below. |
| Center aligned | `usa-step-indicator--center` | Center-align the segment row inside its container instead of left-aligning. |

## When to use which variant

- **Default** → Most multi-step forms. Labels under each step make the path scannable without reading the heading.
- **`--counters`** → When step numbers carry meaning ("Step 3 of 5: Documents") and the form's audience benefits from explicit numbering. Useful for long, formal applications.
- **`--counters-sm`** → 6+ steps where a full-size counter row would wrap or feel crowded.
- **`--no-labels`** → Short, tight layouts where the heading line below the row is enough context. Common in sidebars or compact form shells.
- **`--center`** → Centered hero-style form layouts where the indicator should align with a centered form body.

## Default markup

A 5-step MVA vehicle registration form, currently on step 3 (Payment):

```html
<div class="usa-step-indicator" aria-label="progress">
  <ol class="usa-step-indicator__segments">
    <li class="usa-step-indicator__segment usa-step-indicator__segment--complete">
      <span class="usa-step-indicator__segment-label">
        Personal information
        <span class="usa-sr-only"> - completed</span>
      </span>
    </li>
    <li class="usa-step-indicator__segment usa-step-indicator__segment--complete">
      <span class="usa-step-indicator__segment-label">
        Vehicle details
        <span class="usa-sr-only"> - completed</span>
      </span>
    </li>
    <li class="usa-step-indicator__segment usa-step-indicator__segment--current" aria-current="step">
      <span class="usa-step-indicator__segment-label">
        Payment
        <span class="usa-sr-only"> - current step</span>
      </span>
    </li>
    <li class="usa-step-indicator__segment">
      <span class="usa-step-indicator__segment-label">
        Review
        <span class="usa-sr-only"> - not completed</span>
      </span>
    </li>
    <li class="usa-step-indicator__segment">
      <span class="usa-step-indicator__segment-label">
        Confirmation
        <span class="usa-sr-only"> - not completed</span>
      </span>
    </li>
  </ol>
  <div class="usa-step-indicator__header">
    <h4 class="usa-step-indicator__heading">
      <span class="usa-step-indicator__heading-counter">
        <span class="usa-sr-only">Step</span>
        <span class="usa-step-indicator__current-step">3</span>
        <span class="usa-step-indicator__total-steps">of 5</span>
      </span>
      <span class="usa-step-indicator__heading-text">Payment</span>
    </h4>
  </div>
</div>
```

Place this immediately above the current step's form section inside `<main>`, after the hero.

## Markup — with counters

Add `usa-step-indicator--counters`:

```html
<div class="usa-step-indicator usa-step-indicator--counters" aria-label="progress">
  <ol class="usa-step-indicator__segments">
    <li class="usa-step-indicator__segment usa-step-indicator__segment--complete">
      <span class="usa-step-indicator__segment-label">Personal information<span class="usa-sr-only"> - completed</span></span>
    </li>
    <!-- ...remaining steps... -->
  </ol>
  <div class="usa-step-indicator__header">
    <h4 class="usa-step-indicator__heading">
      <span class="usa-step-indicator__heading-counter">
        <span class="usa-sr-only">Step</span>
        <span class="usa-step-indicator__current-step">3</span>
        <span class="usa-step-indicator__total-steps">of 5</span>
      </span>
      <span class="usa-step-indicator__heading-text">Payment</span>
    </h4>
  </div>
</div>
```

For small counters, swap in `usa-step-indicator--counters-sm` instead.

## Markup — no labels

```html
<div class="usa-step-indicator usa-step-indicator--no-labels" aria-label="progress">
  <ol class="usa-step-indicator__segments">
    <li class="usa-step-indicator__segment usa-step-indicator__segment--complete">
      <span class="usa-step-indicator__segment-label">Personal information<span class="usa-sr-only"> - completed</span></span>
    </li>
    <!-- ...remaining steps... -->
  </ol>
  <div class="usa-step-indicator__header">
    <h4 class="usa-step-indicator__heading">
      <span class="usa-step-indicator__heading-counter">
        <span class="usa-sr-only">Step</span>
        <span class="usa-step-indicator__current-step">3</span>
        <span class="usa-step-indicator__total-steps">of 5</span>
      </span>
      <span class="usa-step-indicator__heading-text">Payment</span>
    </h4>
  </div>
</div>
```

The labels under the dots are visually hidden, but they remain in the DOM as `__segment-label` for screen readers.

## Markup — centered

```html
<div class="usa-step-indicator usa-step-indicator--center usa-step-indicator--counters" aria-label="progress">
  <ol class="usa-step-indicator__segments">
    <!-- segments -->
  </ol>
  <div class="usa-step-indicator__header">
    <!-- heading -->
  </div>
</div>
```

Center alignment applies to the segments row only; the heading below still left-aligns with the row.

## What each class does

| Class | Effect |
|---|---|
| `usa-step-indicator` | Base container. Sets the row layout, default left alignment, and the responsive collapse to mobile bar. |
| `usa-step-indicator--counters` | Replaces dots with numbered circles (1, 2, 3...) sized to fit the digit. Slightly larger than default dots. |
| `usa-step-indicator--counters-sm` | Like `--counters` but with a smaller circle, used for dense or many-step indicators. |
| `usa-step-indicator--no-labels` | Visually hides each segment's label text while keeping it in the DOM for screen readers. The "Step N of M: Label" heading below the row remains visible. |
| `usa-step-indicator--center` | Centers the segments row horizontally within the parent container. |
| `usa-step-indicator__segments` | The `<ol>` holding each step. Renders as a flex row with the connector line drawn behind the circles. Removes default list bullets and margins. |
| `usa-step-indicator__segment` | A single step `<li>`. Default appearance: light-gray circle, light-gray connector line, label in base text color. |
| `usa-step-indicator__segment--complete` | Marks the step as completed: circle filled primary blue, white checkmark inside, connector line going *to* the next segment turns primary blue. |
| `usa-step-indicator__segment--current` | Marks the step as currently active: circle filled primary blue (no checkmark), label rendered semibold. |
| `usa-step-indicator__segment-label` | The text label below each circle. In `--no-labels` it becomes visually hidden. Holds the `usa-sr-only` "current step / completed / not completed" tag. |
| `usa-step-indicator__header` | Wrapper for the "Step N of M: Label" heading row below the segments. Adds top margin. |
| `usa-step-indicator__heading` | `<h4>` styled with semibold weight and step heading sizing — combines the counter and the current step name on one line. |
| `usa-step-indicator__heading-counter` | The "Step 3 of 5" segment of the heading. Slightly smaller than the step text. |
| `usa-step-indicator__current-step` | The active step number. Rendered with semibold weight inside the counter. |
| `usa-step-indicator__total-steps` | The "of N" portion. Renders in a lighter weight. |
| `usa-step-indicator__heading-text` | The current step's label text inside the heading. Bold weight, larger than the counter. |
| `usa-sr-only` | Visually hidden but readable by screen readers. Used inside each segment to announce state ("- completed", "- current step", "- not completed"). |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `steps` | `string[]` | 5-item sample array | Step labels in display order. The array length determines total steps. |
| `currentStep` | number (1-based) | `3` | Which step is current. Steps before this index get `--complete`; the matching step gets `--current`; later steps get neither. |
| `showLabels` | bool | `true` | When `false`, applies `usa-step-indicator--no-labels`. |
| `centerAlign` | bool | `false` | When `true`, applies `usa-step-indicator--center`. |
| `counters` | bool | `false` | When `true`, applies `usa-step-indicator--counters`. |
| `smallCounters` | bool | `false` | When `true`, applies `usa-step-indicator--counters-sm`. Wins over `counters` if both are set. |
| `ariaLabel` | string | `"Step indicator showing current step in application process"` | Container `aria-label`. The recommended convention is the literal string `"progress"`, per USWDS. |
| `ariaDescribedBy` | string | `""` | Optional ID of a descriptive element. |
| `ariaLabelledBy` | string | `""` | Optional ID of a labelling element. Overrides `aria-label`. |

## Accessibility

- The container takes `aria-label="progress"` (or another describing label). USWDS specifies "progress" as the canonical label.
- The current segment carries `aria-current="step"`. Only one step at a time should have this attribute.
- Each segment's state ("completed", "current step", "not completed") is encoded for screen readers inside a `usa-sr-only` span under `__segment-label`. Don't omit those — without them, a screen-reader user can't tell completed from upcoming steps.
- Don't use color alone to convey state. The combination of primary-blue circle + sr-only "completed" text + checkmark inside the circle is required; removing any one of them breaks WCAG.
- The component is a static visual; it does **not** receive focus. Focus should remain on the form's current field, not on the indicator.

## JS requirements

`usa-step-indicator` is **purely presentational** — no JavaScript is required for it to render correctly. Loading `mdwds-core.js` is still recommended for the rest of the page (banner, header, modals, etc.), but the step indicator itself does not depend on JS to display state.

To advance the indicator between steps, your server (or your single-page application) must re-render the markup with a new `currentStep`, updating which `<li>` has `--complete`, `--current`, or neither, and updating the `aria-current="step"` placement plus the heading counter and text.

## Common mistakes

1. **Forgetting `aria-current="step"`** on the current segment — screen readers won't know which step is active even though it visually appears highlighted.
2. **Omitting the `usa-sr-only` state tags** ("- completed", "- not completed") — leaves screen readers with no way to perceive step state since color alone is the visual cue.
3. **Using `<ul>` instead of `<ol>`** for the segments — step order is meaningful; the list must be ordered for assistive tech and semantics.
4. **Forgetting the `__header` heading block** — the "Step N of M: Label" line is the primary affordance on mobile (where labels are hidden by default). Without it, users on small screens lose orientation.
5. **Marking two segments as `--current` simultaneously** — only one step is current. Future steps get no state class; past steps get `--complete`.
6. **Trying to make the indicator clickable** — the USWDS pattern is non-interactive. Navigation between steps is handled by the form's prev/next buttons, not by clicking the indicator dots.
7. **Skipping `usa-step-indicator__heading-counter` and writing the counter as plain text** — the counter is composed of three nested spans (sr-only "Step", current step, total steps) so screen readers announce "Step 3 of 5" correctly.
