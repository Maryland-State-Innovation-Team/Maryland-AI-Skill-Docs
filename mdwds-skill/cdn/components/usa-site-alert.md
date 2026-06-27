# usa-site-alert

A **full-width statewide notice strip** that sits between the `usa-banner` and the `maryland-header`. Use it to surface site-wide notices: emergency alerts, statewide announcements, scheduled outages affecting all services. Unlike `usa-alert`, which lives inline inside `<main>`, `usa-site-alert` is a page-shell element.

> Different component from `usa-alert`. `usa-alert` is an inline panel inside content; `usa-site-alert` is a full-bleed strip at the top of the page. They share inner markup (`usa-alert`, `usa-alert__body`, etc.) but the outer wrapper and intent differ. See `cdn/components/usa-alert.md` for the inline variant.

## What it looks like

A `usa-site-alert` is a `<section>` that spans the full viewport width. Inside it, a `usa-alert` block (the same inner construct as the inline alert) carries the heading and message. The strip has a solid fill rather than a side-bar accent — the entire band is colored by status.

Two USWDS variants are documented in the MDWDS Storybook: `info` and `emergency`. MDWDS uses the same USWDS theme underneath, so the visual treatment matches the standard color tokens.

- **`info`** — Pale cyan background, dark teal heading text, info icon on the left. Used for routine site-wide messages.
- **`emergency`** — Solid red background (`emergency` color), white heading + body text, alert/warning icon. Used for genuinely urgent statewide alerts (boil-water advisories, weather emergencies, AMBER alerts).

Inside the strip, content is constrained to the standard `grid-container` width on wider viewports so the message lines up with the header and main content below.

Heading is rendered as `<h3 class="usa-alert__heading">` — this places the site alert above the page `<h1>` in the source order but **does not** become the page's primary heading because it lives outside `<main>`. Body text is `<p class="usa-alert__text">`.

## Variants

| Variant | Use for |
|---|---|
| `info` (default) | Routine statewide announcements — service updates, ongoing programs |
| `emergency` | Critical, time-sensitive notices — public safety, weather, infrastructure failures |

A `success`/`warning`/`error` style is not part of the documented MDWDS site-alert variants; if you need those tones, use an inline `usa-alert` inside `<main>` or the page-shell-level `maryland-alert` (which sits in the same slot — see `cdn/page-shell.md`).

## When to use it

- **Statewide emergencies** that every agency site must surface (boil-water, severe weather, AMBER alerts) → `emergency`.
- **Scheduled statewide IT outages** affecting login, payments, or other shared services → `info` or `emergency` depending on severity.
- **Time-bounded announcements** that should appear on every page until they expire → `info`.

Do **not** use this for per-page alerts (use inline `usa-alert` or `maryland-alert`), or for permanent site banners (those belong in the header or hero).

## Position in the page shell

`usa-site-alert` sits **after** the `usa-banner` and **before** the `maryland-header`:

```
usa-skipnav
usa-banner               ← official-website strip (always present)
usa-site-alert           ← this component, when present
maryland-header          ← agency / Maryland header
<main>                   ← page content
maryland-footer
<maryland-statewide-footer>
```

See `cdn/page-shell.md` for the full shell.

## Default markup (info)

```html
<section class="usa-site-alert usa-site-alert--info"
         aria-label="Site alert"
         role="status">
  <div class="usa-alert">
    <div class="usa-alert__body">
      <h3 class="usa-alert__heading">Maryland Census 2030 outreach launches statewide</h3>
      <p class="usa-alert__text">
        Public meetings begin June 1 in every county. Find a session near you at
        <a class="usa-link" href="/census-2030">maryland.gov/census-2030</a>.
      </p>
    </div>
  </div>
</section>
```

## Markup — emergency

```html
<section class="usa-site-alert usa-site-alert--emergency"
         aria-label="Emergency site alert"
         role="alert"
         aria-live="assertive">
  <div class="usa-alert">
    <div class="usa-alert__body">
      <h3 class="usa-alert__heading">Severe weather alert — Western Maryland</h3>
      <p class="usa-alert__text">
        Tornado warning in effect for Garrett and Allegany Counties until 9:00 PM EDT. Seek shelter immediately.
        Updates at <a class="usa-link" href="https://mema.maryland.gov">mema.maryland.gov</a>.
      </p>
    </div>
  </div>
</section>
```

`role="alert"` plus `aria-live="assertive"` ensures screen readers interrupt and announce the message immediately on appearance.

## What each class does

| Class | Effect |
|---|---|
| `usa-site-alert` | Outer `<section>`. Full-bleed (`width: 100%`) banner-style wrapper. Contains and constrains the inner `usa-alert`. |
| `usa-site-alert--info` | Pale cyan background, dark teal text, info icon. Friendly informational treatment. |
| `usa-site-alert--emergency` | Solid red background (`color-emergency`), white text, alert/warning icon. Highest-urgency treatment, reserved for genuine emergencies. |
| `usa-alert` | Inner alert frame (shared with `usa-alert`). Inside `usa-site-alert`, it loses its own side-bar styling and inherits the strip's full-width fill. |
| `usa-alert__body` | Inner content wrapper. Holds heading + text. Constrained to grid container width on wider viewports. |
| `usa-alert__heading` | The alert title. `<h3>` element styled at ~22px semibold. Color tuned per variant (dark on light backgrounds, white on emergency red). |
| `usa-alert__text` | Body paragraph. ~16px. Inline `<a class="usa-link">` inherits high-contrast link color. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `info` \| `emergency` | `info` | Visual style of the strip |
| `heading` | string | `"This is a site alert"` | Heading text |
| `content` | string | sample | Body paragraph (raw text — escape if user-supplied) |
| `role` | `status` \| `alert` \| `""` | `""` | ARIA role on the outer section. Use `alert` for emergencies. |
| `ariaLive` | `polite` \| `assertive` \| `off` \| `""` | `""` | ARIA live-region politeness. Use `assertive` for emergencies. |
| `ariaLabel` | string | `""` | Accessible region label (recommended: `"Site alert"`). |

## Heading level adjustment

Use `<h3>` for the site alert heading because it sits in the global page-shell region above `<main>` — it's a peer of other shell sections (banner, header) rather than a section inside the page content. **Do not** make this `<h1>` even when it's the loudest message on the page; the page `<h1>` lives inside `maryland-hero` in `<main>`. See `cdn/composition.md`.

## Common mistakes

1. **Confusing this with `usa-alert`** — `usa-alert` is inline inside `<main>`; `usa-site-alert` is a full-width strip in the page shell. Different placement, different intent.
2. **Placing the strip below the `maryland-header`** — it belongs between the banner and header. Putting it after the header buries the message.
3. **Omitting `role="alert"` + `aria-live="assertive"` on emergencies** — screen reader users won't be interrupted to hear the notice.
4. **Wrapping the `<section>` in a `<div class="grid-container">`** — the strip needs to span the full viewport. Let the inner `usa-alert__body` handle width constraints.
5. **Using `usa-site-alert--emergency` for a routine announcement** — the bright red treatment is reserved for genuine emergencies. For routine notices use `info`, or `maryland-alert--warning` in the global-alert slot.
6. **Forgetting to remove the strip after the event ends** — site alerts are time-bounded. Plan for removal/expiration when authoring.
