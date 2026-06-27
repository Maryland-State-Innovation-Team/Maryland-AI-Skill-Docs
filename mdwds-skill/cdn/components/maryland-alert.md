# maryland-alert

Maryland Design System alerts communicate important, time-sensitive information to users with a left color bar, an icon, an optional heading, and a message body. They are the primary way to surface status/warnings/errors on Maryland.gov pages, and the only acceptable way to render a statewide emergency banner.

> **Use `maryland-alert` instead of `usa-alert` on Maryland-branded pages.** Same five statuses as USWDS plus an extra `emergency` status, with Maryland color tokens. For statewide notifications between the banner and header, use a `maryland-alert` rendered full-width. For inline form validation, use `usa-validation`. For non-urgent reference content, use `maryland-summary-box`.

## What it looks like

An alert is a `<div>` with a left border-bar (`$theme-alert-bar-width`) colored to match the status, a status-tinted background (`*-lighter` for info/warning/success/error, full saturation for emergency), and dark text. The body sits inside a `__container` (which becomes a `grid-container` at tablet-lg+ in MDWDS) and a flex-column `__body` that contains an icon (positioned absolutely on the left), an optional heading, and the message.

- **Icon** — 40×40px Material Symbols glyph. Position is optical-adjusted (offset slightly up and left to align with the heading's baseline). Each status uses its own icon:
  - `info` → `info`
  - `warning` → `warning`
  - `error` → `error`
  - `emergency` → `error` (same glyph as error)
  - `success` → `check_circle`
- **Heading** — Source Sans, large body size (per USWDS `$theme-alert-font-family` and `lg`). Bold. Margin top 0, bottom 8px. Omitted in `slim` mode.
- **Message** — body-4 (16px) on mobile, body-6 (20px) at mobile-lg+. Paragraphs are spaced 8px apart. Allows HTML.

Links inside the alert pick up a status-appropriate color via `get-color-token-from-bg` / `set-link-from-bg` mixins, so text remains accessible at the relevant contrast ratio.

The whole alert behaves as a CSS container (`container-name: alert`), and at tablet-lg+ it adjusts margins outward when its inline size exceeds viewport - 32px.

## Variants

By status:

| Status | Visual | Use for |
|---|---|---|
| `info` | Light info-blue background, info border, info icon | Routine status updates, neutral notices |
| `warning` | Light amber background, warning border, warning icon | Conditions that may cause issues if ignored |
| `error` | Light red background, error border, error icon | Failed operations, blocking problems |
| `success` | Light green background, success border, check icon | Confirmation of successful action |
| `emergency` | Full-saturation emergency-red background, emergency border, error icon | Active statewide emergencies (severe weather, evacuations, AMBER alerts) |

By size:

| Variant | Visual |
|---|---|
| (default) | 40px icon, full padding |
| `slim` | 24px icon, reduced vertical padding, **no heading** (omit it). |
| `no-icon` | Icon hidden, no left-margin offset on content. Can combine with `slim`. |

Accessibility:

- `info` / `warning` / `success` → `role="status"` (polite live region).
- `error` / `emergency` → `role="alert"` (assertive live region).

## Default markup (info)

```html
<div class="maryland-alert maryland-alert--info" role="status" aria-labelledby="alert-1">
  <div class="maryland-alert__container">
    <div class="maryland-alert__body">
      <h2 class="maryland-alert__heading" id="alert-1">Online services available</h2>
      <div class="maryland-alert__text">
        <p>The Motor Vehicle Administration's online renewal system is open 24/7. You can renew a license or registration without visiting a branch.</p>
      </div>
    </div>
  </div>
</div>
```

## Markup — warning

```html
<div class="maryland-alert maryland-alert--warning" role="status" aria-labelledby="alert-2">
  <div class="maryland-alert__container">
    <div class="maryland-alert__body">
      <h2 class="maryland-alert__heading" id="alert-2">Limited service this weekend</h2>
      <div class="maryland-alert__text">
        <p>All DNR Service Centers will close at noon on Saturday, March 14 for system maintenance. Normal hours resume Monday.</p>
      </div>
    </div>
  </div>
</div>
```

## Markup — error

```html
<div class="maryland-alert maryland-alert--error" role="alert" aria-labelledby="alert-3">
  <div class="maryland-alert__container">
    <div class="maryland-alert__body">
      <h2 class="maryland-alert__heading" id="alert-3">Application could not be submitted</h2>
      <div class="maryland-alert__text">
        <p>We couldn't reach the Comptroller's system. Please try again in a few minutes. If the problem continues, <a class="usa-link maryland-link" href="/contact">contact us</a>.</p>
      </div>
    </div>
  </div>
</div>
```

## Markup — success

```html
<div class="maryland-alert maryland-alert--success" role="status" aria-labelledby="alert-4">
  <div class="maryland-alert__container">
    <div class="maryland-alert__body">
      <h2 class="maryland-alert__heading" id="alert-4">Your fishing license is active</h2>
      <div class="maryland-alert__text">
        <p>Confirmation number: <strong>FL-2026-08842331</strong>. Print or save this page for your records.</p>
      </div>
    </div>
  </div>
</div>
```

## Markup — emergency (full-saturation, statewide)

```html
<div class="maryland-alert maryland-alert--emergency" role="alert" aria-labelledby="alert-5">
  <div class="maryland-alert__container">
    <div class="maryland-alert__body">
      <h2 class="maryland-alert__heading" id="alert-5">Severe weather warning — Western Maryland</h2>
      <div class="maryland-alert__text">
        <p>A tornado warning is in effect for Allegany and Garrett Counties until 4:30 p.m. <a href="https://weather.gov" target="_blank" rel="noopener noreferrer">View the National Weather Service alert</a> for shelter instructions.</p>
      </div>
    </div>
  </div>
</div>
```

Emergency alerts are typically placed **above** the `maryland-header` (between the `usa-banner` and the header) so they're the first thing a returning visitor sees. See `cdn/page-shell.md` for the slot.

## Markup — slim

```html
<div class="maryland-alert maryland-alert--warning maryland-alert--slim" role="status">
  <div class="maryland-alert__container">
    <div class="maryland-alert__body">
      <div class="maryland-alert__text">
        <p>Heads up: the renewal form has been updated. <a href="/mva/renew">Use the new form.</a></p>
      </div>
    </div>
  </div>
</div>
```

Slim variant omits the heading. The icon shrinks to 24px and vertical padding is reduced.

## Markup — no icon

```html
<div class="maryland-alert maryland-alert--info maryland-alert--no-icon" role="status">
  <div class="maryland-alert__container">
    <div class="maryland-alert__body">
      <div class="maryland-alert__text">
        <p>Filings submitted today will be processed in the next business cycle.</p>
      </div>
    </div>
  </div>
</div>
```

`no-icon` removes the icon entirely and zeroes the left-margin offset on content. Often combined with `slim` for the lowest-visual-weight notice.

## What each class does

| Class | Effect |
|---|---|
| `maryland-alert` | Base alert. Display block, full-width container. 4px-equivalent left border bar (configurable via `$theme-alert-bar-width`). Becomes a CSS container at `alert` query name. |
| `maryland-alert--info` | Info-blue tinted background (`info-lighter`), info-colored left bar, info icon. |
| `maryland-alert--warning` | Warning-amber tinted background (`warning-lighter`), warning bar, warning icon. |
| `maryland-alert--error` | Error-red tinted background (`error-lighter`), error bar, error icon. |
| `maryland-alert--success` | Success-green tinted background (`success-lighter`), success bar, check icon. |
| `maryland-alert--emergency` | Full-saturation emergency-red background, emergency bar, error icon. White or near-white text. |
| `maryland-alert--slim` | Reduced vertical padding (8px instead of full). Icon shrinks to 24px. Heading is omitted by convention. |
| `maryland-alert--no-icon` | Hides the icon. Content uses zero left-margin offset. |
| `maryland-alert--validation` | (Used by `usa-validation`) Adds top spacing for an embedded checklist. |
| `maryland-alert__container` | Inner wrapper. At tablet-lg+, applies `grid-container($theme-header-max-width)` to align with the page's header max-width. |
| `maryland-alert__body` | Flex column. Holds icon `::before`, heading, text. Vertical padding controlled by `$theme-alert-padding-y`, horizontal by `$theme-alert-padding-x`. Position relative to anchor the icon. |
| `maryland-alert__heading` | The `<h2>`. Source Sans large-body size, bold. 0 top margin, 8px bottom. Hidden in slim mode. |
| `maryland-alert__text` | Message body. body-4 (16px) on mobile, body-6 (20px) at mobile-lg+. Removes default `<p>` margins; adjacent paragraphs get 8px top spacing. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `status` | `info` \| `warning` \| `success` \| `error` \| `emergency` | `info` | Sets the modifier class and the icon. |
| `heading` | string | — | Heading text. Ignored when `slim` is true. |
| `message` | string (HTML) | — | Message body. Rendered as HTML — sanitize first. |
| `slim` | bool | false | Use the slim variant (no heading). |
| `noIcon` | bool | false | Hide the icon. |
| `id` | string | auto-generated | Optional id for the heading; used by `aria-labelledby`. |

## Heading level adjustment

Default `<h2>`. Use `<h3>` when the alert sits inside an already-headed section (e.g., a `usa-step-indicator` step). Don't change to `<h1>` — that role belongs to the hero.

## Common mistakes

1. **Wrong `role` for the status** — error/emergency need `role="alert"` (assertive), the others use `role="status"` (polite). Set the right value when writing the markup by hand.
2. **Heading inside a slim alert** — slim's vertical padding is too small to fit a heading legibly. In hand-written markup, just omit the heading entirely.
3. **Multiple `role="alert"` on a page** — assertive live regions interrupt screen readers. Reserve `error`/`emergency` for genuine page-blocking issues; otherwise use `role="status"`.
4. **Hex colors via inline `<style>`** — colors come from status tokens. If a status doesn't fit, the right answer is to rethink the message, not to recolor.
5. **Emergency alert that isn't actually an emergency** — `emergency` is reserved for severe-weather, AMBER, or evacuation notices. Routine maintenance windows go in `info` or `warning`.
6. **Putting a `maryland-alert` inside a `<form>` to show validation results** — that's a `usa-validation` job. The alert is for global/state messages, not field-level feedback.
7. **Forgetting `aria-labelledby`** — without it, screen readers don't associate the heading with the alert region.
