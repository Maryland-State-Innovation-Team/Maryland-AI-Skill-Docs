# maryland-placeholder

Maryland Design System placeholder is a **wireframe/template-only utility** that exists in the public Storybook to demonstrate the file structure of an MDWDS component. It is **not a production component** — it does not appear on real Maryland.gov pages, and the CDN does not ship usable styles for it.

> **Do not use `maryland-placeholder` in production pages.** It exists in Storybook for design-system development purposes only. If you want a "we're still figuring this out" indicator on a real page, use a `maryland-alert--info` ("This page is under development") or simply leave the section out.

## What it looks like

The Storybook story renders an `<h1>Hello, world!</h1>` and a `<pre>` block showing the current Storybook args as JSON. It applies three example classes via Lit's `classMap`:

- `class-always-on` — present on every render
- `class-optional` — toggled by a Storybook boolean control
- `class-constructable-{value}` — dynamically named based on a "select" control

None of these classes have actual CSS rules — they're scaffolding to teach contributors how to set up dynamic class binding in MDWDS templates. The component has no component-specific stylesheet shipped on the CDN.

## When to use

**Don't.** Use it only when:

- Contributing to MDWDS itself and you want a scaffold to copy when starting a new component.
- Demonstrating Storybook control patterns to other contributors.

For any user-facing scenario, pick a real component from `cdn/component-index.md`.

## Default markup (Storybook rendering, not for production)

```html
<div class="class-always-on class-optional class-constructable-opt-one">
  <h1>Hello, world!</h1>
  <pre>
    <code>
      args = {
        textField: Default value,
        optionsField: opt-one,
        trueFalseField: true,
      }
    </code>
  </pre>
</div>
```

## What each class does

None of these classes have CSS rules in the published CSS. The component is a template stub.

| Class | Effect |
|---|---|
| `class-always-on` | No styling. Demonstrates a static class. |
| `class-optional` | No styling. Demonstrates a boolean-toggled class. |
| `class-constructable-{opt-one\|opt-two\|opt-three}` | No styling. Demonstrates dynamic class-name construction from a "select" arg. |

## Prop schema

| Prop | Type | Default | Notes |
|---|---|---|---|
| `textField` | string | `"Default value"` | Demo text control. |
| `optionsField` | `opt-one` \| `opt-two` \| `opt-three` | `opt-one` | Demo select control. |
| `trueFalseField` | bool | true | Demo boolean control. |

## Common mistakes

1. **Using `maryland-placeholder` on production pages** — it's not a real component. The CDN ships no styles for it.
2. **Copying the `class-always-on` / `class-optional` class names into other components** — they're examples, not a shared utility. Use BEM-style component-prefixed class names like `maryland-component-name__element--modifier`.
3. **Building a wireframe placeholder for in-progress content with this** — use a Maryland alert ("Under construction") or just omit the section until it's ready. Inline `<style>` placeholders or this component will both render unstyled in production.
