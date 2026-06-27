# usa-alert

The USWDS alert is an inline notification block — a colored panel with an icon, heading, and message — for surfacing information, warnings, errors, success states, and emergencies inside page content (not at the top of the site).

> **Prefer `maryland-alert` on Maryland.gov pages.** `usa-alert` and `maryland-alert` are different components (different class namespaces, different visual treatments tuned to the Maryland palette). The MDWDS-original `maryland-alert` is the canonical inline alert on Maryland-branded surfaces. Use `usa-alert` only inside internal tools or USWDS-style microsites. See `cdn/component-index.md` for the disambiguation.
>
> **Also: this is not `usa-site-alert`.** `usa-alert` is an inline message inside `<main>`; `usa-site-alert` is the full-width strip that sits between the banner and the header to convey site-wide notices. See `cdn/components/usa-site-alert.md`.

## What it looks like

A `usa-alert` is a horizontal panel with a thick left border in the alert's status color, a same-tinted background fill (very light), an icon on the left (USWDS sprite icon ~24px), and the message body on the right containing a heading (`<h4 class="usa-alert__heading">`, semibold, ~22px) above one or more paragraphs of body text.

Color treatments per status (from USWDS theme):

| Status | Left border / icon | Background |
|---|---|---|
| `info` | Cyan blue (~`#00bde3`) | Pale cyan |
| `warning` | Amber gold (~`#ffbe2e`) | Pale yellow |
| `success` | Green (~`#00a91c`) | Pale green |
| `error` | Red (~`#d54309`) | Pale red |
| `emergency` | Bright red (~`#9c1d22`) | Solid red with white text |

On the desktop breakpoint (1024px+), MDWDS adds `margin-block-start: units(3)` (24px) to the alert so it has consistent breathing room from preceding content.

The **slim** variant (`usa-alert--slim`) hides the heading and reduces padding to a single horizontal line — useful for tight inline notices.

The **no-icon** variant (`usa-alert--no-icon`) suppresses the status icon, leaving just the colored border and text. Use when the icon would be redundant with surrounding context.

Body text supports inline HTML — anchor tags inside `usa-alert__text` should be marked with `class="usa-link"` so they inherit the alert's link styling.

## Variants

| Status | Use for |
|---|---|
| `info` (default) | General-information messages, helpful tips, neutral context |
| `warning` | Important non-emergency cautions (e.g., scheduled maintenance) |
| `success` | Confirmations after a successful action |
| `error` | Validation failures, form errors |
| `emergency` | Critical alerts that demand immediate attention |

Combine with `slim` or `noIcon` modifiers as needed.

## Default markup

```html
<div class="usa-alert usa-alert--info">
  <div class="usa-alert__body">
    <h4 class="usa-alert__heading">Office closed for the Memorial Day holiday</h4>
    <p class="usa-alert__text">
      The Department of Labor will be closed Monday, May 25, 2026. Online services remain available at
      <a class="usa-link" href="/services">maryland.gov/services</a>.
    </p>
  </div>
</div>
```

## Markup — warning

```html
<div class="usa-alert usa-alert--warning">
  <div class="usa-alert__body">
    <h4 class="usa-alert__heading">Scheduled maintenance: May 18</h4>
    <p class="usa-alert__text">
      The eGovernment portal will be unavailable from 11:00 PM Saturday to 3:00 AM Sunday for system upgrades.
    </p>
  </div>
</div>
```

## Markup — success

```html
<div class="usa-alert usa-alert--success">
  <div class="usa-alert__body">
    <h4 class="usa-alert__heading">Application submitted</h4>
    <p class="usa-alert__text">
      Your Maryland fishing license application has been received. Confirmation number: <strong>FL-2026-0084231</strong>.
    </p>
  </div>
</div>
```

## Markup — error

```html
<div class="usa-alert usa-alert--error" role="alert">
  <div class="usa-alert__body">
    <h4 class="usa-alert__heading">We couldn't process your renewal</h4>
    <p class="usa-alert__text">
      The driver's license number you entered does not match our records. Double-check the number or
      <a class="usa-link" href="/help/license-lookup">look it up here</a>.
    </p>
  </div>
</div>
```

`role="alert"` on the outer div is recommended for error states so assistive technology announces the message immediately.

## Markup — emergency

```html
<div class="usa-alert usa-alert--emergency" role="alert">
  <div class="usa-alert__body">
    <h4 class="usa-alert__heading">Boil water advisory — Anne Arundel County</h4>
    <p class="usa-alert__text">
      Residents in the Severn River service area must boil tap water for at least 1 minute before consumption.
      Updates: <a class="usa-link" href="/emergency/water-advisory">maryland.gov/emergency</a>.
    </p>
  </div>
</div>
```

## Markup — slim

```html
<div class="usa-alert usa-alert--info usa-alert--slim">
  <div class="usa-alert__body">
    <p class="usa-alert__text">
      Heads up — applications submitted after 5:00 PM are processed the next business day.
    </p>
  </div>
</div>
```

## Markup — no icon

```html
<div class="usa-alert usa-alert--warning usa-alert--no-icon">
  <div class="usa-alert__body">
    <h4 class="usa-alert__heading">Limited service today</h4>
    <p class="usa-alert__text">Walk-in service is paused for staff training until 12:00 PM.</p>
  </div>
</div>
```

## What each class does

| Class | Effect |
|---|---|
| `usa-alert` | Base alert wrapper. Sets the panel layout (icon column + body column) and a heavy left border. Adds `margin-block-start: 24px` at the desktop breakpoint (MDWDS override). |
| `usa-alert--info` | Cyan left border, pale cyan background, info icon. |
| `usa-alert--warning` | Amber left border, pale yellow background, warning icon. |
| `usa-alert--success` | Green left border, pale green background, success icon. |
| `usa-alert--error` | Red left border, pale red background, error icon. |
| `usa-alert--emergency` | Bright red solid background with white text and white icon. Heaviest treatment. |
| `usa-alert--slim` | Removes the heading slot, tightens vertical padding to a single line. |
| `usa-alert--no-icon` | Suppresses the status icon (icon column collapses). |
| `usa-alert__body` | Inner content wrapper. Holds heading + text. Has horizontal padding so the body doesn't touch the icon column. |
| `usa-alert__heading` | Alert title. `<h4>` element styled at ~22px semibold. Sits at the top of the body. |
| `usa-alert__text` | Body paragraph. ~16px. Supports inline `<a class="usa-link">` for links — links inherit the alert's contrast-appropriate color. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `status` | `info` \| `warning` \| `success` \| `error` \| `emergency` | `info` | Determines `usa-alert--{status}` |
| `heading` | string | `"Informational status"` | Heading text. Ignored visually when `slim` is true. |
| `message` | string (HTML allowed) | sample | Body paragraph. Inline HTML is rendered raw — sanitize user-supplied content. |
| `slim` | bool | `false` | Adds `usa-alert--slim`. |
| `noIcon` | bool | `false` | Adds `usa-alert--no-icon`. |

## Heading level adjustment

Alerts use `<h4>` because they are usually nested below the page's `<h2>`/`<h3>` section heading. If your alert is the page-level lead notice (rare), bump to `<h3>` or `<h2>` to fit the outline. See `cdn/composition.md`.

## Common mistakes

1. **Using `usa-alert` for the statewide notice strip at the top of the page** — that's `usa-site-alert`. `usa-alert` lives inside `<main>`.
2. **Using `usa-alert` on a Maryland-branded page** — prefer `maryland-alert`.
3. **Forgetting `role="alert"` on dynamic error/emergency alerts** — screen readers won't announce the message when it appears.
4. **Using `slim` together with a heading you want to show** — slim hides the heading visually. Either pick non-slim, or accept that the heading won't render.
5. **Plain `<a>` links inside `usa-alert__text`** — they don't inherit the alert link color. Always use `class="usa-link"`.
6. **Inline `style="background: red"`** — overrides the careful USWDS tinting and breaks contrast guarantees. Use the right `--status` modifier.
