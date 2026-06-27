# maryland-summary-box

Maryland Design System summary box pulls a short, scannable list of key takeaways into a visually framed container near the top of a page. It is the Maryland-themed counterpart to USWDS's `usa-summary-box`, restyled with Maryland's info-color palette.

> **Use `maryland-summary-box` instead of `usa-summary-box` on Maryland-branded pages.** Both render a similar visual; this one uses Maryland's color tokens and spacing. For at-a-glance attention-grabbing notifications (info/warning/error/success), use `maryland-alert`. For a centered single-statement highlight, use `maryland-callout`.

## What it looks like

A summary box is a `<div role="region">` with a light info-tinted background (`info-lighter`), 4px rounded outer corners, and a thin **inner** border colored with `info-dark`. The inner border-radius matches the outer. The whole component sits inset from the page on both axes:

- **Outer** padding: 10px on mobile, 12px on mobile-lg+. Bottom margin: 24px (mobile), 32px (mobile-lg), 40px (tablet+).
- **Inner** wrapper has its own border + padding: 25/20px (mobile), 32/40px (mobile-lg), 32px (tablet+).

Inside the inner wrapper:

- An optional bold heading (`<h2>`). 16px on mobile, 22px at mobile-lg+. 12px bottom margin.
- A `<ul>` of items. List markers are `blue-cool-60v` (Maryland blue). Each item has an 8px bottom margin (except the last). 16/20px padding-left.

Links inside the list use the standard Maryland link typesetting (primary blue, underlined). The list reflows naturally as items wrap; bullets stay aligned.

## When to use

- Topping a long-form page with 3–5 key actions or facts a reader should not miss.
- Recapping a list of preconditions (e.g., "Before you apply, gather these documents").
- A "quick-reference" sidebar block that doesn't need the visual weight of a hero or callout.

Don't use a summary box for time-sensitive notifications (use `maryland-alert`) or for marketing/promotional content (use `maryland-promo` or `maryland-card-group`).

## Default markup

```html
<div class="maryland-summary-box" role="region" aria-labelledby="summary-1">
  <div class="maryland-summary-box__inner">
    <h2 class="maryland-summary-box__heading" id="summary-1">Before you apply for a Maryland fishing license</h2>
    <div class="maryland-summary-box__text">
      <ul class="maryland-summary-box__list">
        <li>Confirm your Maryland residency status — proof required at purchase.</li>
        <li>Decide whether you need a freshwater, tidal, or bay-sport license.</li>
        <li>Have your Social Security number ready (federal requirement).</li>
        <li>If you're 16 or older, you must hold a valid license. <a href="/fishing/exceptions">Review exceptions</a>.</li>
        <li>Renew online through the <a href="/dnr/compass">COMPASS portal</a> or at any DNR Service Center.</li>
      </ul>
    </div>
  </div>
</div>
```

## Markup — no heading

```html
<div class="maryland-summary-box" role="region">
  <div class="maryland-summary-box__inner">
    <div class="maryland-summary-box__text">
      <ul class="maryland-summary-box__list">
        <li>File by April 15 to avoid penalties.</li>
        <li>Use the Comptroller's <a href="/comptroller/efile">free e-file system</a>.</li>
        <li>Income limits apply to most Maryland tax credits.</li>
      </ul>
    </div>
  </div>
</div>
```

Omit `aria-labelledby` when there's no heading.

## What each class does

| Class | Effect |
|---|---|
| `maryland-summary-box` | Outer `<div>`. Info-tinted (`info-lighter`) background. 4px outer radius. Outer padding 10/12px responsive. Bottom margin 24 → 32 → 40px. |
| `maryland-summary-box__inner` | Inner wrapper. 1px solid `info-dark` border, 4px radius. Inner padding 25/20px (mobile), 32/40px (mobile-lg), 32px (tablet+). |
| `maryland-summary-box__heading` | The `<h2>`. Bold. 16px body-5 (mobile) → 22px body-9 (mobile-lg+). Removes default top margin; 12px bottom margin. |
| `maryland-summary-box__text` | Wrapper around the list. Removes vertical margins. Sets body-4 (16px) / body-6 (20px at mobile-lg+) text. |
| `maryland-summary-box__list` | The `<ul>`. Zero margin. Padding-left 16px (mobile/mobile-lg) / 40px (tablet+). List item markers colored `blue-cool-60v`. Each item has 8px bottom spacing (last has 0). Links inside use the Maryland typeset-link styling. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `title` | string | — | Heading text. Optional — if absent and no items are provided, component renders nothing. |
| `items` | string[] | — | Array of HTML strings. Each entry becomes a `<li>` and supports inline HTML (`<a>`, `<strong>`, etc.). |
| `id` | string | auto-generated | Optional id for the heading; used as the target of `aria-labelledby`. |

## Heading level adjustment

The component uses `<h2>` because summary boxes typically sit at the top of a page section. If the box is nested deeper (e.g., inside an already-`<h2>`-led section), demote to `<h3>` and keep the class. The class controls styling, not outline.

## Common mistakes

1. **Skipping the inner wrapper** — the visible border comes from `__inner`. Without it, you get a tinted block but no outline.
2. **Forgetting `role="region"` and `aria-labelledby`** — screen reader users rely on these to identify the box as a landmark when navigating.
3. **Putting paragraphs in `__text` instead of a `<ul>`** — the design assumes a list. For free-form prose, use `usa-prose` or a `maryland-callout`.
4. **More than ~7 items** — the box loses its scannability. Either trim, or split into multiple boxes/sections.
5. **Inline-styling the markers** — colors come from the design system. Use a different component if you need different markers.
6. **Reaching for this when you want an attention-grabbing notice** — `maryland-alert` is the right tool. The summary box is reference content, not a notification.
