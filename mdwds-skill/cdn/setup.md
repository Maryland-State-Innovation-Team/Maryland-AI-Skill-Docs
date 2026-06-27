# CDN Setup

Every Maryland state page must load the MDWDS CSS and JavaScript from the CDN. There are **three** required tags, plus an optional inline init script for the best FOUC behavior.

## Version pinning

Use the latest stable MDWDS version. Confirm the current version at [designsystem.maryland.gov](https://designsystem.maryland.gov/?path=/docs/getting-started-for-engineers--docs) before shipping. As of this skill's last update, the version is `0.47.4`.

- **Pinned (recommended for production):** `https://cdn.maryland.gov/mdwds/0.47.4-beta.{hash}/...`
- **Floating (always newest, use with caution):** `https://cdn.maryland.gov/mdwds/latest/...`

Pinning to a specific version prevents your site from breaking when MDWDS ships a new release. Use `latest` only in prototypes or environments where automatic upgrades are acceptable.

The version string is `0.47.4`, never `v0.47.4`.

## Required tags

Place these inside `<head>`:

```html
<link
  rel="stylesheet"
  data-mdwds
  href="https://cdn.maryland.gov/mdwds/latest/css/mdwds.min.css"
/>
<script src="https://cdn.maryland.gov/mdwds/latest/js/mdwds-init.js"></script>
<script type="module" src="https://cdn.maryland.gov/mdwds/latest/js/mdwds-core.js"></script>
<script type="module" src="https://cdn.maryland.gov/mdwds/latest/js/mdwds-elements.js"></script>
```

Five things to know:

1. **The `data-mdwds` attribute on the stylesheet `<link>` is REQUIRED.** Lit web components (`<maryland-statewide-banner>`, `<maryland-statewide-footer>`) render into Shadow DOM and look up the CDN stylesheet by `link[rel="stylesheet"][data-mdwds]` to adopt it into their shadow root. **Without `data-mdwds`, the web-component contents render invisibly** (no fonts, no colors, no layout — the shadow root has no styles). Add the attribute exactly as shown.
2. **`mdwds-init.js`** must run synchronously before paint — it adds a `usa-js-loading` class to `<html>` so components (like the USWDS banner accordion) don't flash open then snap closed.
3. **`mdwds-core.js`** is an **ES module** (`type="module"`). It wires up interactive USWDS behaviors (banner accordion expand, modals, date pickers, combo boxes, `maryland-nav` toggle, etc.) and injects GTM. **It does NOT register the Lit custom elements** — that's what `mdwds-elements.js` does. Without `mdwds-core.js`, interactive components are inert.
4. **`mdwds-elements.js`** is a separate **ES module** that registers the Lit custom elements: `<maryland-banner>`, `<maryland-statewide-banner>`, `<maryland-statewide-footer>`, `<maryland-translate>`. **Without it, the statewide banner and statewide footer render as empty unknown HTML elements** — the tags appear in the DOM but produce zero visible output. The MDWDS Storybook's Getting Started page omits this script, which is a documented gap; you need it if your page uses any `<maryland-*>` web component.
5. **GTM is included in CDN builds.** `mdwds-core.js` from the CDN loads Google Tag Manager for statewide analytics. Make sure the site's privacy policy discloses use of Google Analytics / GTM.

### Alternative: per-component standalone scripts

If you only need a single web component (e.g. just the statewide banner inside a non-MDWDS site), skip `mdwds-elements.js` and load the individual component script instead:

```html
<script
  type="module"
  src="https://cdn.maryland.gov/mdwds/latest/components/maryland-statewide-footer.js"
></script>
```

For a full MDWDS page that uses both the statewide banner and statewide footer, `mdwds-elements.js` is simpler — one tag covers all of them.

## Inline init script (more performant alternative to `mdwds-init.js`)

For maximum FOUC prevention, replace the `mdwds-init.js` tag with the same logic inlined in `<head>`. This avoids an extra request and runs immediately:

```html
<script>
  "use strict";

  const loadingClass = "usa-js-loading";

  document.documentElement.classList.add(loadingClass);
  function revertClass() {
    document.documentElement.classList.remove(loadingClass);
  }

  const fallback = setTimeout(revertClass, 8000);

  function verifyLoaded() {
    if (window.uswdsPresent) {
      clearTimeout(fallback);
      revertClass();
      window.removeEventListener("load", verifyLoaded, true);
    }
  }

  window.addEventListener("load", verifyLoaded, true);
</script>
```

`window.uswdsPresent` is set to `true` at the end of `mdwds-core.js` initialization, signaling that all components are ready and the loading class can be removed.

## Minimal HTML skeleton

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Page Title — Agency Name</title>

    <!-- Inline init script for FOUC prevention -->
    <script>
      "use strict";
      const loadingClass = "usa-js-loading";
      document.documentElement.classList.add(loadingClass);
      function revertClass() { document.documentElement.classList.remove(loadingClass); }
      const fallback = setTimeout(revertClass, 8000);
      function verifyLoaded() {
        if (window.uswdsPresent) {
          clearTimeout(fallback);
          revertClass();
          window.removeEventListener("load", verifyLoaded, true);
        }
      }
      window.addEventListener("load", verifyLoaded, true);
    </script>

    <link
      rel="stylesheet"
      data-mdwds
      href="https://cdn.maryland.gov/mdwds/latest/css/mdwds.min.css"
    />
    <script type="module" src="https://cdn.maryland.gov/mdwds/latest/js/mdwds-core.js"></script>
    <script type="module" src="https://cdn.maryland.gov/mdwds/latest/js/mdwds-elements.js"></script>
  </head>
  <body>
    <!-- Page shell starts here. See cdn/page-shell.md. -->
  </body>
</html>
```

## What NOT to do

- **Don't omit `mdwds-elements.js`** if your page uses `<maryland-statewide-banner>`, `<maryland-statewide-footer>`, `<maryland-banner>`, or `<maryland-translate>`. Without it those tags render as empty unknown elements — nothing visible appears. `mdwds-core.js` does not register custom elements.
- **Don't omit `data-mdwds` from the stylesheet link.** Without it, `<maryland-statewide-banner>` and `<maryland-statewide-footer>` register and render but appear invisibly because their shadow DOM can't find the global stylesheet to adopt.
- **Don't write custom CSS to reproduce component styles.** Use the documented class names; the CDN stylesheet does the rest.
- **Don't omit `type="module"` from the `mdwds-core.js` tag.** It's an ESM bundle and will fail without it.
- **Don't load only the CSS.** Interactive components (accordions, modals, banners, date pickers) require the JS bundle.
- **Don't apply `usa-js-loading` to `<body>`.** Apply it to `<html>` — the init script and the stylesheet both target `<html>`.
- **Don't load multiple versions on the same page.** Mixing `0.47.4` CSS with `latest` JS will cause subtle breakage.

## Loading individual web components without the full bundle

Some pages may want a single web component (e.g. just the statewide banner) without the full bundle. Each `<maryland-*>` web component has a standalone build:

```html
<script
  type="module"
  src="https://cdn.maryland.gov/mdwds/latest/components/maryland-statewide-banner.js"
></script>
<maryland-statewide-banner></maryland-statewide-banner>
```

This is useful for embedding the banner in a non-MDWDS site that still needs Maryland.gov branding. For a true MDWDS page, use the full bundle.
