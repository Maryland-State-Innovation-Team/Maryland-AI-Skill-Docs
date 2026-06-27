# usa-tooltip

A USWDS Tooltip is a small floating label that appears on hover or focus of a trigger element to provide a short, contextual hint. Use it for inline help — explaining a form field abbreviation, clarifying an icon-only button, or attaching a hint to a link. MDWDS uses the upstream USWDS tooltip as-is.

> There is no `maryland-tooltip`. `usa-tooltip` is the canonical tooltip implementation on Maryland.gov pages.

## What it looks like

The trigger is any focusable element — typically a `<button>` or `<a>` — with the `usa-tooltip` class and a `title` attribute holding the tooltip text. The trigger renders normally; nothing extra appears next to it.

On hover or keyboard focus of the trigger:

- A small dark-gray pill (`base-darkest` background, ~70 90% opacity, white text) fades in next to the trigger. The pill has fully rounded corners (~3px), padding of about ~8px horizontal × 4px vertical, and Source Sans Pro ~14px text.
- A small triangle (the "arrow" or "callout caret") points from the pill toward the trigger, attached to the side facing the trigger.
- The pill sits ~6–8px offset from the trigger edge in the direction specified by `data-position` (top by default).

The USWDS JS replaces the trigger's `title` attribute with a generated `<span class="usa-tooltip__body">` element. This is what's actually shown — browsers' native `title` tooltips would otherwise duplicate the same text in a system-rendered bubble, so the JS strips `title` once it has read it.

Behavior:

- Mouse hover **on** the trigger shows the tooltip; moving the mouse away hides it.
- Keyboard focus on the trigger (via Tab) shows the tooltip; blurring hides it.
- Pressing ESC while the tooltip is visible dismisses it without removing focus from the trigger.

## Variants

The tooltip "variants" are positions — where the floating pill appears relative to the trigger. Set via the `data-position` attribute on the trigger.

| Position | `data-position` | Visual |
|---|---|---|
| Top (default) | `top` | Pill above the trigger, arrow points down. |
| Bottom | `bottom` | Pill below the trigger, arrow points up. |
| Left | `left` | Pill to the left of the trigger, arrow points right. |
| Right | `right` | Pill to the right of the trigger, arrow points left. |

The USWDS JS may auto-flip the position to keep the tooltip on-screen when the requested side is too close to the viewport edge — e.g., a `data-position="top"` tooltip near the top of the page may render below the trigger instead.

## When to use which position

- **`top`** → Default for most cases. Floats above the trigger without overlapping content below (which is often body text).
- **`bottom`** → Triggers near the very top of the viewport (top of the page hero, sticky headers).
- **`left`** → Triggers in the right edge of a sidebar or right-aligned form column where there isn't horizontal room to the right.
- **`right`** → Triggers in the left edge of the layout where there's open space to the right, e.g., field labels in a left-aligned form column.

## Default markup

A "What is a VIN?" hint attached to a vehicle-identification field on an MVA vehicle registration form:

```html
<label class="usa-label" for="vin-input">
  Vehicle Identification Number (VIN)
  <button
    type="button"
    class="usa-button usa-button--unstyled usa-tooltip"
    data-position="top"
    title="A VIN is the unique 17-character code stamped on your vehicle's dashboard and door jamb. It identifies the make, model, year, and serial number of the vehicle."
    aria-label="What is a VIN? Show explanation."
  >
    <svg class="usa-icon" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
      <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 .88-.36 1.68-.93 2.25z"/>
    </svg>
  </button>
</label>
<input class="usa-input" id="vin-input" name="vin" type="text" maxlength="17" />
```

Notes:

- The trigger is a `<button type="button">` (not an `<a>`), because the tooltip is supplemental help, not navigation.
- `usa-tooltip` is added alongside `usa-button usa-button--unstyled` so the help icon renders cleanly without button styling.
- The `title` attribute holds the tooltip text. The USWDS JS reads this and moves it into a `<span class="usa-tooltip__body">` so the browser's native title-bubble doesn't double up.
- The `aria-label` on the button names the icon for screen readers (icons alone aren't accessible). Do not rely on the tooltip itself to label the button — the tooltip is *supplemental*; the button must still be self-descriptive.

## Markup — bottom position

```html
<button
  type="button"
  class="usa-button usa-tooltip"
  data-position="bottom"
  title="Saves your application without submitting it. You can return to it later."
>
  Save draft
</button>
```

## Markup — left position

```html
<button
  type="button"
  class="usa-button usa-tooltip"
  data-position="left"
  title="Required field."
  aria-label="Required field information"
>
  <svg class="usa-icon" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2z"/>
  </svg>
</button>
```

## Markup — right position

```html
<button
  type="button"
  class="usa-button usa-tooltip"
  data-position="right"
  title="Open this section in a new tab."
>
  Vehicle types
</button>
```

## What each class does

| Class / attribute | Effect |
|---|---|
| `usa-tooltip` | Marks the element as a tooltip trigger. The USWDS JS scans for this class on load and instruments each match: it reads the `title` attribute, removes it (to suppress the browser's native title bubble), and injects a sibling `<span class="usa-tooltip__body">` holding the same text. |
| `data-position="top\|bottom\|left\|right"` | Tells the USWDS JS which side of the trigger the floating pill should appear on. The JS may flip the position dynamically if the chosen side would overflow the viewport. Defaults to `top` when omitted. |
| `title="..."` | The tooltip text source. Read once by the USWDS JS during initialization and removed from the element afterward. **Required** — the JS treats elements with `usa-tooltip` but no `title` as having empty content. |
| `usa-tooltip__body` (generated) | The visible pill: dark background, white text, rounded corners. Created by the JS as a sibling of the trigger; you do not author this in your HTML. |
| `aria-label` (on the trigger) | Required when the trigger is icon-only or otherwise lacks a textual label. Names the trigger for screen readers independently of the tooltip text. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `position` | `top` \| `bottom` \| `left` \| `right` | `top` | Tooltip placement relative to trigger. |
| `tooltipText` | string | `"This is helpful information"` | Goes into the trigger's `title` attribute. |
| `triggerType` | `button` \| `link` | `button` | Type of trigger element. The documented `link` variant still renders a `<button>` — both variants render a button. |
| `triggerLabel` | string | `"Hover or focus me"` | Text displayed on the trigger. |
| `enableAnalytics` | bool | `false` | When true, attaches `data-ga-*` attributes to the trigger. |
| `gaCategory` | string | `"Tooltip"` | GA event category. |
| `gaAction` | string | `"Show"` | GA event action. |
| `gaLabel` | string | `"Help Text"` | GA event label. |

## Accessibility

- The tooltip is supplemental, not load-bearing. **Never put critical information in a tooltip-only location** — sighted users may not hover, touch users have no hover, and the tooltip vanishes when the trigger blurs. If the user *must* know it, place the text in the visible page.
- Icon-only triggers must carry their own `aria-label`. The tooltip's text labels the *help*, not the *control*; without `aria-label`, screen readers announce the control as unlabeled.
- USWDS adds `aria-describedby` on the trigger pointing to the generated `usa-tooltip__body` once the JS initializes. This is the connection that lets screen readers announce the tooltip text. Do not set `aria-describedby` yourself in the HTML — the JS owns this attribute.
- ESC dismisses the tooltip while keeping focus on the trigger, allowing keyboard users to clear a distracting tooltip without losing their place.
- The tooltip is keyboard accessible: tabbing to the trigger shows it; tabbing away hides it. Hover alone is not sufficient.
- Tooltip text should be brief — one sentence, ideally under 12 words. Long content belongs in a popover or modal, not a tooltip.

## JS requirements

`usa-tooltip` **requires `mdwds-core.js` to function.** Without it:

- The element keeps its raw `title` attribute, so on long-hover the browser shows a generic OS-native tooltip — but with no styling, no positioning control, and no keyboard support.
- No `usa-tooltip__body` span is generated, so the styled dark pill never appears.
- The `data-position` attribute has no effect — there is no JS to read it.
- `aria-describedby` is never added to the trigger, so screen readers have no programmatic link between the trigger and the tooltip text.
- ESC does not dismiss the OS-native title tooltip.

In short: without `mdwds-core.js`, the styled tooltip is never shown. Users fall back to the browser's native `title` bubble, which is far inferior in styling, accessibility, and timing.

## Common mistakes

1. **Forgetting `mdwds-core.js`** — the styled tooltip is never shown; only the browser's native `title` bubble appears on long hover.
2. **Putting critical information in a tooltip** — touch users have no hover, and the tooltip disappears when focus leaves. Information users *must* know belongs in the visible page.
3. **Omitting `title=""` from the trigger** — the USWDS JS reads tooltip text from `title`. No `title`, no tooltip text. Some authors mistakenly set `aria-label` instead and find the tooltip empty.
4. **Using `usa-tooltip` on an icon-only button without also setting `aria-label`** — the tooltip names the help but not the control. Screen readers announce the button as "button" with no description.
5. **Setting `aria-describedby` manually on the trigger** — the USWDS JS adds this on init. A manually-set value will be overwritten or conflict, depending on order.
6. **Triggering the tooltip from a non-focusable element** (e.g., `<span>` or `<div>`) — keyboard users can't focus it, so the tooltip is effectively mouse-only. Use a `<button>` or `<a>` (or add `tabindex="0"` if you genuinely need a focusable non-interactive element).
7. **Writing a long paragraph in `title=""`** — the pill is sized for short hints, not body content. Long content overflows or wraps awkwardly. Use a popover or modal instead.
