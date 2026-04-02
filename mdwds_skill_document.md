# Maryland Web Design System (MDWDS) — LLM Skill Document

*Generated 2026-04-02 · 107 components documented*

---

# Maryland Web Design System (MDWDS) — Introduction and Overview

## What MDWDS Is

The Maryland Web Design System (MDWDS) is the official design system for Maryland state government digital services. It exists to help Maryland government teams build consistent, accessible, mobile-friendly web properties that meet state digital service standards.

MDWDS is built on top of the **U.S. Web Design System (USWDS)**. This means the system uses two class namespaces side by side: `usa-*` classes inherited from USWDS, and `maryland-*` classes that are MDWDS-specific. Some components are pure USWDS (buttons, forms, breadcrumbs), some are pure MDWDS extensions (header, footer, hero), and some are hybrids. You must use both class sets correctly — never substitute one for the other.

The system is delivered as a CDN-hosted bundle. The current stable version is **0.44.0**.

---

## CDN Setup

Every Maryland state page must load the MDWDS CSS and JavaScript from the CDN. Place these tags in the `<head>`:

```html
<link rel="stylesheet" href="https://cdn.maryland.gov/mdwds/0.44.0/css/mdwds.min.css">
<script src="https://cdn.maryland.gov/mdwds/0.44.0/js/mdwds.min.js" defer></script>
```

**Important rules:**
- The version string is `0.44.0` — never write `v0.44.0`.
- To always get the latest build (not recommended for production), replace `0.44.0` with `latest`.
- **Never write custom CSS to replicate MDWDS component styles.** All visual styling for every component — colors, spacing, typography, shadows, states — comes from the CDN stylesheet. Your job is to produce correct HTML structure with correct class names. The stylesheet does the rest.
- To prevent a flash of unstyled content (FOUC) while the JavaScript bundle initializes, add `usa-js-loading` to the `<body>` element. USWDS JavaScript removes this class once it is ready, enabling JS-dependent transitions and states.

```html
<body class="usa-js-loading">
```

---

## The Class Naming System

MDWDS uses three distinct naming patterns. Mixing them up is the most common error.

### 1. `maryland-*` — MDWDS Web Components and CSS Classes

Custom HTML elements and their associated CSS classes are all prefixed with `maryland-`. This includes both web components (which require the JS bundle) and regular CSS class names applied to standard HTML elements.

- Web components: `<maryland-statewide-banner>`, `<maryland-statewide-footer>`
- CSS class patterns: `maryland-header`, `maryland-header__util-nav`, `maryland-card`, `maryland-card__container`, `maryland-hero`, `maryland-footer`, `maryland-alert`, `maryland-alert--info`
- CSS custom properties: `--maryland-color-primary`, `--maryland-font-body`

BEM structure applies: `maryland-{block}__element--modifier`.

### 2. `usa-*` — USWDS-Inherited Classes

Components sourced from USWDS use `usa-` prefixed classes. These follow BEM with modifiers separated by double hyphens.

- `usa-button`, `usa-button--secondary`, `usa-button--accent-cool`
- `usa-breadcrumb`, `usa-breadcrumb__list`, `usa-breadcrumb__list-item`, `usa-current`
- `usa-accordion`, `usa-accordion__button`, `usa-accordion__content`
- `usa-banner`, `usa-banner__header`, `usa-banner__inner`
- `usa-form`, `usa-label`, `usa-input`, `usa-select`
- `usa-sr-only` (screen-reader-only utility)
- `usa-prose` (typography wrapper)
- `grid-container`, `grid-row`, `grid-col-*` (layout utilities)

### 3. Real Names Matter

Use the exact class names documented in each component reference. Do not invent plausible-sounding alternatives. The page header is `maryland-header`, not `header` or `site-header`. The utility navigation inside it is `maryland-header__util-nav`, not `nav__utility`. The navigation bar is `maryland-search-form` (wrapping both search and nav links), not `maryland-nav` or `main-nav`. Look up the real names before writing markup.

---

## How Components Compose — The Page Shell

Every Maryland state page follows this top-to-bottom structural order:

```
usa-skipnav link (maryland-link maryland-link--skipnav → #main-content)
  ↓
usa-banner (Statewide Banner — REQUIRED)
  └── usa-accordion (expandable "How you know" section)
  ↓
maryland-header
  └── maryland-header__util-nav (utility links/buttons)
  └── maryland-header__home (logo link)
  ↓
maryland-search-form (navigation + search)
  ↓
<main id="main-content"> (page-specific content)
  └── Hero, Cards, Accordions, Alerts, etc.
  ↓
maryland-footer (agency footer, if present)
  ↓
<maryland-statewide-footer> (web component — zero config required)
```

Templates in the component reference (Maryland Homepage, Agency Homepage, Basic Page, Landing Page, etc.) show the authoritative nesting and class structure for each page type. When composing a full page, follow a template — do not improvise the shell structure.

---

## Key Rules — Get These Right

**(a) Always load the CDN. Never write custom CSS.**
Every visual property of every MDWDS component is defined in the CDN stylesheet. Writing custom CSS to reproduce a button color, card shadow, or alert style is always wrong. Structure the HTML correctly and the styles appear automatically.

**(b) The Statewide Banner is required on every Maryland state page.**
The `usa-banner` section with `aria-label="Official website of the State of Maryland"` must appear at the top of every page before any other content. This is a non-negotiable state requirement, not an optional pattern.

**(c) Use real MDWDS class names from the component reference.**
Every class name in this document is the actual class name used by the CDN stylesheet. Invented class names produce unstyled HTML. When in doubt, consult the per-component reference entry for the exact block, element, and modifier class names.

**(d) `<maryland-*>` web components require the JS bundle.**
`<maryland-statewide-banner>` and `<maryland-statewide-footer>` are Lit-based web components. They render their own shadow DOM and require the JavaScript bundle (`mdwds.min.js`) to function. Without the script tag, they appear blank. The noscript fallback for the statewide banner uses `maryland-alert maryland-alert--warning` classes on standard HTML. All other interactive behaviors — accordions, date pickers, combo boxes, modals — also depend on the JS bundle being loaded.

---

# Component Reference

# Getting Started

## Architecture Decision Records (ADR)

*Getting Started*

Architecture Decision Records (ADRs) are lightweight, version-controlled documents that capture important architectural decisions along with their context and consequences. ADRs help teams document the "why" behind technical decisions so that future team members can understand the rationale. They are used for documenting decisions about tools, system architecture, security/compliance, and tradeoffs in scalability or performance.

### Key Information


**What ADRs Document:**
- Single, important architectural decisions
- Context and background leading to the decision
- The decision itself and reasoning
- Consequences and tradeoffs
- Alternatives considered (optional)

**ADR Status Values:**
- Accepted
- Proposed
- Deprecated
- Superseded by ADR-X

**When to Use ADRs:**
- Selecting new tools, platforms, or approaches
- System architecture or integration design
- Security or compliance-related decisions
- Tradeoffs in scalability, performance, or maintainability

**Benefits of ADRs:**
- Transparency: Everyone understands the "why" behind technical decisions
- History: Trace changes in direction over time
- Consistency: Decisions documented in repeatable format
- Collaboration: Encourages team discussion and review

**ADR Template Format:**
- Title: ADR-N: Title of the Decision
- Status: Accepted | Proposed | Deprecated | Superseded by ADR-X
- Context: Background and situation
- Decision: What was decided and why
- Consequences: Tradeoffs and implications
- Alternatives Considered: Other options and why not chosen


### Implementation


```
# ADR-N: Title of the Decision

## 👀 Status

Accepted | Proposed | Deprecated | Superseded by ADR-X

## 🚀 Context

Explain the situation and background that led to this decision.

## ✅ Decision

State the decision made and the reasoning behind it.

## ⚖️ Consequences

What are the tradeoffs and implications of this decision?

## 👨🏾‍💻 Alternatives Considered

(Optional) Briefly mention other options and why they were not chosen.
```

**Storybook Meta Configuration:**

```html
import { Meta } from "@storybook/addon-docs/blocks";

<Meta title="Developers/Docs/ADR/[Title Goes Here]" />
```


### Context

ADRs are a foundational documentation practice within the MDWDS developer documentation that helps team members understand and review architectural decisions. They work in conjunction with the broader design system governance to maintain consistency and transparency in how the system evolves over time.

---

## Choose Web Component Framework (ADR)

*Getting Started*

This is an Architecture Decision Record (ADR) documenting the decision to use Lit as the web component framework for MDWDS. It explains the context, rationale, consequences, and alternatives for building reusable, accessible web components that work across multiple applications and environments including CMS platforms, static sites, and micro frontends.

### Key Information

**Status:** Accepted  
**Date:** 2025-06-17

**Framework Selected:** Lit

**Key Benefits:**
- Lightweight footprint ideal for performance-sensitive and embedded use cases
- Web Standards First approach building directly on the Web Components spec
- Minimal abstraction layer over native Web Components
- Reactive data-binding support
- Scoped styles via Shadow DOM
- Declarative rendering with simple template syntax
- Reduces boilerplate without introducing unnecessary complexity
- Minimizes lock-in and maximizes browser-native capabilities
- Encourages small, focused, composable components

**Use Cases:**
- Sharing components across micro frontends
- CMS platform integration
- Legacy and static environment compatibility
- Standard-compliant custom element authoring
- Multi-framework and framework-agnostic environments

**Comparison to Alternatives:**
- Chosen over plain JavaScript Web Components (which increase boilerplate and maintenance overhead)
- Preferred over heavier component frameworks for better portability

### Implementation

This is a documentation/decision page with no interactive component implementation. The page contains prose documentation and a table of contents with sections for Context, Decision, Consequences, and Alternatives Considered.

The HTML rendered includes Storybook documentation wrappers and semantic heading structure with anchor links:

```html
<h1 id="choose-web-component-framework">
  <a href="#choose-web-component-framework">Choose Web Component Framework</a>
</h1>

<h2 id="-context">
  <a href="#-context">🚀 Context</a>
</h2>
<p>We need a consistent and scalable way to build web components...</p>

<h2 id="-decision">
  <a href="#-decision">✅ Decision</a>
</h2>
<p>We will use Lit as our framework of choice...</p>

<h2 id="️-consequences">
  <a href="#️-consequences">⚖️ Consequences</a>
</h2>

<h2 id="-alternatives-considered">
  <a href="#-alternatives-considered">👨🏾‍💻 Alternatives Considered</a>
</h2>
```

Navigation structure uses table of contents with links to document sections.

### Context

This ADR documents a foundational architectural decision for MDWDS that guides all web component development across the design system. The choice of Lit framework directly influences how developers build and maintain reusable components that compose together in the MDWDS library.

---

## Getting Started for Engineers

*Getting Started*

This is an onboarding documentation page for engineers implementing the Maryland Web Design System (MDWDS) in their projects. It provides quick-start instructions for both adopters who want to use MDWDS via CDN and developers who want to contribute to the system. The page covers CDN setup, initialization scripts, and local development commands.

### Key Information

## CDN Setup (Current Version 0.44.0)

**Adopter Quick Start:**
- Current stable version: `0.44.0`
- Two CDN URL strategies:
  - **Versioned URL (recommended)**: Pin to a specific release (e.g., `https://cdn.maryland.gov/mdwds/0.44.0/css/mdwds.min.css`) for stable, reproducible deployments
  - **Latest**: Use `https://cdn.maryland.gov/mdwds/latest/css/mdwds.min.css` to always get the newest build

**Required Resources:**
- CSS stylesheet: `https://cdn.maryland.gov/mdwds/0.44.0/css/mdwds.min.css`
- Init script: `https://cdn.maryland.gov/mdwds/0.44.0/js/mdwds-init.js`
- Core module: `https://cdn.maryland.gov/mdwds/0.44.0/js/mdwds-core.js` (loaded as type="module")

**MDWDS Init Script:**
- The `mdwds-init.js` prevents flashes of unstyled content (FOUC) during initial page load
- Adds `usa-js-loading` class to `<html>` element during load
- Removes class once components are initialized (8-second fallback)
- Can be loaded from CDN or inlined in document head for better performance
- Sets `window.uswdsPresent = true` when mdwds-core finishes initializing

**Developer Quickstart:**
- Requires PNPM (enable with `corepack enable`)
- Install: `pnpm install`
- Development: `pnpm dev`
- Storybook runs at `http://localhost:7777/`

### Implementation

## Adopter Implementation

```html
<!-- Add to your <head> -->
<link
  rel="stylesheet"
  href="https://cdn.maryland.gov/mdwds/0.44.0/css/mdwds.min.css"
/>
<script src="https://cdn.maryland.gov/mdwds/0.44.0/js/mdwds-init.js"></script>
<script type="module" src="https://cdn.maryland.gov/mdwds/0.44.0/js/mdwds-core.js"></script>
```

## Alternative: Inline Init Script (Recommended for Performance)

```html
<head>
  <link
    rel="stylesheet"
    href="https://cdn.maryland.gov/mdwds/0.44.0/css/mdwds.min.css"
  />
  <script>
    "use strict";

    const loadingClass = "usa-js-loading";

    document.documentElement.classList.add(loadingClass);
    function revertClass() {
      document.documentElement.classList.remove(loadingClass);
    }

    const fallback = setTimeout(revertClass, 8000);

    function verifyLoaded() {
      // @ts-expect-error uswdsPresent is set to TRUE at the end of mdwds-core initializing components.
      if (window.uswdsPresent) {
        clearTimeout(fallback);
        revertClass();
        window.removeEventListener("load", verifyLoaded, true);
      }
    }

    window.addEventListener("load", verifyLoaded, true);
  </script>
  <script type="module" src="https://cdn.maryland.gov/mdwds/0.44.0/js/mdwds-core.js"></script>
</head>
```

## Developer Setup

```bash
# Enable use of PNPM.
corepack enable

# Install dependencies.
pnpm install

# Start development
pnpm dev
```

Then visit Storybook at http://localhost:7777/

### Context

This is the entry point documentation for the Maryland Web Design System and serves as the primary onboarding resource for both end-users adopting MDWDS and developers contributing to the system. It bridges the gap between discovering MDWDS and implementing it or extending it.

---

## How to Contribute to MDWDS

*Getting Started*

This is a developer-focused documentation page that explains how to contribute to the Maryland Web Design System. It provides guidance on reporting bugs, proposing features, and submitting code contributions, covering the entire contribution workflow and best practices for collaborating with the MDWDS core team. Contributors of any skill level can use this guide to understand the process and standards for improving the Design System.

### Key Information

This documentation page is structured as a guidance document rather than a reusable component. Key sections include:

- **Welcome section**: Introduction encouraging contributions
- **How you can contribute**: Overview with subsections on:
  - Getting Started: Create a GitHub account requirement
  - Reporting bugs and issues: Step-by-step bug reporting process
  - Proposing feature requests or enhancements: Feature proposal workflow
  - Proposing something else: General proposal guidance
- **Code contributions**: Technical guidelines including:
  - Commit Message Guidelines: Standards for commit messages
  - Code Standards: Code quality requirements
  - Code Review Process: How reviews are conducted
  - Development Workflow: Setup and contribution process
  - Testing: Testing requirements and procedures
  - License: Licensing information for contributions
  - Questions or Help: Support resources

The page uses semantic HTML with heading levels (H2, H3) and links to specific sections via anchor IDs for easy navigation. No component-specific CSS classes or ARIA attributes are required for implementation.

### Implementation

This is a documentation/prose page that does not render interactive components. The page structure uses standard HTML heading and paragraph elements:

```html
<h2 id="welcome">Welcome!</h2>
<p>We're glad you're thinking about contributing to the Maryland Web Design System (MDWDS)!</p>
<p>Your contribution helps make the Design System better for the next team that uses it.</p>

<h2 id="how-you-can-contribute">How you can contribute</h2>
<h3 id="getting-started">Getting Started</h3>
<p>Anyone can contribute to MDWDS. Whether it's submitting a bug or proposing a new component, we welcome your ideas on how to improve the Design System.</p>

<h3 id="reporting-bugs-and-issues">Reporting bugs and issues</h3>
<p>If something isn't working the way it's supposed to, here's how you can let us know:</p>

<h2 id="code-contributions">Code contributions</h2>
<h3 id="-commit-message-guidelines">✅ Commit Message Guidelines</h3>
<h3 id="-code-standards">🧹 Code Standards</h3>
<h3 id="-code-review-process">🔍 Code Review Process</h3>
<h3 id="-development-workflow">🛠 Development Workflow</h3>
<h3 id="-testing">🧪 Testing</h3>
<h3 id="-license">📄 License</h3>
<h3 id="-questions-or-help">💬 Questions or Help?</h3>
```

The page includes a table of contents navigation (rendered with `class="toc-list"`) that links to anchor IDs.

### Context

This documentation page serves as the primary entry point for developers wanting to contribute to MDWDS. It complements the foundation and component documentation by providing workflow guidance, standards, and best practices that contributors must follow when proposing changes or improvements to the Design System.

---

## How to Set Up Local Development

*Getting Started*

This is a step-by-step documentation guide for setting up the Maryland Web Design System (MDWDS) on a local development machine. It covers cloning the repository, installing system dependencies, configuring Node.js and package managers, and running Storybook locally. Developers use this guide to establish their initial development environment before working with MDWDS components.

### Key Information

The guide covers six main setup steps:

1. **Clone the Repository** — Uses `git clone git@github.com:maryland-gov/toolkit.git` and navigate to the project directory.

2. **Install System Dependencies** — Run `brew bundle` to install all dependencies listed in the Brewfile.

3. **Set Up Node.js** — Install fnm (Fast Node Manager) via Homebrew, follow shell setup instructions, reload terminal, return to project directory, confirm Node.js version from .node-version file.

4. **Install Dependencies** — Enable pnpm via `corepack enable pnpm` and install packages with `pnpm install`.

5. **VS Code Setup** — Optional step to copy recommended settings from `.vscode/example.settings.json` to `.vscode/settings.json`.

6. **Run Storybook** — Start local dev server with `pnpm dev` and visit `localhost:6006` in browser.

**Success Criteria**: MDWDS component library should run in browser with no build errors.

**Troubleshooting Tips**:
- Re-run `pnpm install` if dependencies fail
- Verify shell is configured for fnm
- Check for typos or shell setup issues
- Verify `node -v` matches `.node-version` file

**Key Prerequisites**: Homebrew, fnm, pnpm, Node.js version manager, and VS Code (optional).

### Implementation

This is a documentation/prose guide page without interactive components. The page structure includes:

```html
<div class="sbdocs sbdocs-wrapper css-3rewwu">
  <aside class="sbdocs sbdocs-toc--custom css-1wizkyk">
    <nav aria-labelledby="_r_0_" class="css-q7khkg">
      <h2 id="_r_0_" class="css-ghy3je">Table of Contents</h2>
      <div class="toc-wrapper">
        <ul class="toc-list">
          <li class="toc-list-item is-active-li">
            <a href="#-success-criteria" class="toc-link node-name--H2 is-active-link">✅ Success Criteria</a>
          </li>
          <li class="toc-list-item">
            <a href="#-troubleshooting" class="toc-link node-name--H2">🛠 Troubleshooting</a>
          </li>
        </ul>
      </div>
    </nav>
  </aside>
  <div class="sbdocs sbdocs-content css-x28zkw">
    <h1 id="-how-to-set-up-local-development" class="css-wzniqs">🚀 How to Set Up Local Development?</h1>
    <p>This guide walks you through setting up MDWDS on your machine.</p>
    <hr>
    <div class="usa-process-list usa-process-list--vertical">
      <div class="usa-process-list__item">
        <h4 class="usa-process-list__heading">1. Clone the Repository</h4>
        <p>Open your terminal and clone the project:</p>
        <pre><code class="language-bash">git clone git@github.com:maryland-gov/toolkit.git
cd toolkit</code></pre>
      </div>
      <div class="usa-process-list__item">
        <h4 class="usa-process-list__heading">2. Install System Dependencies</h4>
        <p>Install everything listed in the <code>Brewfile</code>:</p>
        <pre><code class="language-bash">brew bundle</code></pre>
      </div>
      <div class="usa-process-list__item">
        <h4 class="usa-process-list__heading">3. Set Up Node.js (via fnm)</h4>
        <pre><code class="language-bash">brew install fnm
cd toolkit
node -v</code></pre>
      </div>
      <div class="usa-process-list__item">
        <h4 class="usa-process-list__heading">4. Install Dependencies (via pnpm)</h4>
        <pre><code class="language-bash">corepack enable pnpm
pnpm install</code></pre>
      </div>
      <div class="usa-process-list__item">
        <h4 class="usa-process-list__heading">5. Optional: VS Code Setup</h4>
        <pre><code class="language-bash">cp .vscode/example.settings.json .vscode/settings.json</code></pre>
      </div>
      <div class="usa-process-list__item">
        <h4 class="usa-process-list__heading">6. Run Storybook Locally</h4>
        <pre><code class="language-bash">pnpm dev</code></pre>
        <p>Then visit localhost:6006 in your browser.</p>
      </div>
    </div>
    <h2 id="-success-criteria" class="css-wzniqs">✅ Success Criteria</h2>
    <p>You should see MDWDS component library running in your browser with no build errors.</p>
    <h2 id="-troubleshooting" class="css-wzniqs">🛠 Troubleshooting</h2>
    <ul>
      <li>Run pnpm install again if dependencies fail.</li>
      <li>Confirm your shell is configured for fnm.</li>
      <li>Check for typos or shell setup issues.</li>
      <li>If node -v doesn't match, recheck your .node-version and fnm install.</li>
    </ul>
  </div>
</div>
```

**Key Classes and Elements**:
- `sbdocs sbdocs-wrapper` — Main documentation wrapper
- `sbdocs sbdocs-toc--custom` — Table of contents sidebar
- `sbdocs sbdocs-content` — Main content area
- `toc-link`, `node-name--H2`, `is-active-link` — Navigation link states
- `usa-process-list usa-process-list--vertical` — Vertical process list (USWDS component)
- `usa-process-list__item` — Individual process step
- `usa-process-list__heading` — Step heading

### Context

This Getting Started guide is foundational documentation for the MDWDS system. It provides new developers with the prerequisite steps needed before working with any MDWDS components, establishing the development environment and confirming proper setup through running Storybook locally at localhost:6006.

---

## How-To Guides

*Getting Started*

The How-To Guides section provides practical, step-by-step instructions for common tasks and workflows with the Maryland Web Design System (MDWDS). These task-oriented guides are designed to help developers accomplish specific goals quickly and consistently, complementing reference documentation and design decisions with prescriptive, reusable instructions.

### Key Information

This is a documentation index and guide framework rather than a component. Key characteristics include:

**Purpose**: Task-oriented documentation focused on *doing*, not *deciding*

**Guide Attributes**:
- Task-oriented: Solve specific problems or accomplish goals
- Prescriptive: Provide exact steps and guidance on what to avoid
- Collaborative: Enable teams and future maintainers to move faster with consistent patterns
- Reusable: Can be linked from internal docs, wikis, onboarding checklists, and Storybook

**Suggested Format Structure**:
- Heading: "How to [do a thing]"
- Overview section with context and relevance
- Prerequisites listing requirements
- Steps section with numbered, clear instructions
- Success Criteria for validation
- Troubleshooting section for common gotchas
- Related Resources with links

**Included How-To Guides**:
- how-to-use-toolkit.mdx: Load the design system via CDN or NPM
- how-to-contribute.mdx: Best practices for contributing new components
- how-to-start-locally.mdx: Getting MDWDS running on your machine

### Implementation

This is a documentation organizational section without rendered component HTML. The page content shows Storybook loading states and placeholder elements:

```html
<div class="sbdocs sbdocs-wrapper">
  <aside class="sbdocs sbdocs-toc--custom">
    <nav aria-labelledby="_r_0_" class="css-q7khkg">
      <h2 id="_r_0_" class="css-ghy3je">Table of Contents</h2>
      <div class="toc-wrapper">
        <ul class="toc-list">
          <li class="toc-list-item is-active-li">
            <a href="#-why-we-use-how-to-guides" class="toc-link node-name--H2 is-active-link">
              🫡 Why We Use How-To Guides
            </a>
          </li>
          <li class="toc-list-item">
            <a href="#️-writing-a-good-how-to-guide" class="toc-link node-name--H2">
              ✍️ Writing a Good How-To Guide
            </a>
            <ul class="toc-list is-collapsible is-collapsed">
              <li class="toc-list-item">
                <a href="#-suggested-format" class="toc-link node-name--H3">
                  💡 Suggested Format
                </a>
              </li>
            </ul>
          </li>
          <li class="toc-list-item">
            <a href="#-examples-of-how-to-guides" class="toc-link node-name--H2">
              ✨ Examples of How-To Guides
            </a>
          </li>
          <li class="toc-list-item">
            <a href="#-need-help" class="toc-link node-name--H2">
              💬 Need Help?
            </a>
          </li>
        </ul>
      </div>
    </nav>
  </aside>
  <div class="sbdocs sbdocs-content">
    <h1>📘 How-To Guides</h1>
    <!-- Guide content sections follow -->
  </div>
</div>
```

The page is a Storybook documentation page (MDX) rendered with:
- `.sbdocs` wrapper class for Storybook docs styling
- `.sbdocs-toc--custom` for custom table of contents
- `.toc-list` and `.toc-list-item` for navigation items
- `.toc-link` with modifier classes like `.node-name--H2` and `.is-active-link` for active states

### Context

This documentation index is part of the MDWDS Getting Started / Developers Docs section, serving as an organizational guide for task-oriented how-to guides. It establishes the standard format and philosophy for creating prescriptive documentation that helps developers integrate with and contribute to the Maryland Web Design System consistently.

---

## maryland- Prefix for Web Components and CSS Variables

*Getting Started*

This is an Architectural Decision Record (ADR) documenting the MDWDS decision to use the `maryland-` prefix for all custom elements, CSS variables, and classes. It solves the problem of namespace collisions in consuming applications that may integrate multiple design systems or frameworks. Use this to understand the naming conventions and standards for all MDWDS components.

### Key Information

## Naming Convention Standards

All MDWDS artifacts follow the `maryland-` prefix pattern:

### Web Components
- Pattern: `<maryland-button>`, `<maryland-header>`, etc.
- Examples: `maryland-accordion`, `maryland-card`, `maryland-modal`

### CSS Custom Properties (CSS Variables)
- Pattern: `--maryland-color-primary`, `--maryland-font-body`, etc.
- Examples: `--maryland-color-secondary`, `--maryland-spacing-unit`

### Sass Variables
- Pattern: `$maryland-color-primary`, etc.
- Direct correspondence with CSS custom property names

### CSS Classes
- Pattern: `maryland-[component-name]`, `maryland-[modifier]`
- Example: `class="maryland-link"`, `class="maryland-button maryland-button--primary"`

## Key Facts
- **Status**: Accepted (Date: 2025-01-01)
- **Rationale**: Prevents collisions with other libraries (uswds, bootstrap, material) and improves clarity
- **Community Feedback**: Majority of MDWDS community members polled in late 2024 strongly preferred `maryland-` over alternatives like `md-` or `toolkit-`
- **Applies Globally**: Convention applies across all MDWDS components, utilities, and design tokens

## Alternatives Rejected
- `md-`: Ambiguous (confused with "Markdown" or "Medical Doctor")
- `toolkit-`: Too technical and didn't resonate with users

### Implementation

## Implementation Guidance

All MDWDS components and utilities must follow this pattern:

### Web Component Example
```html
<maryland-button>Click Me</maryland-button>
<maryland-header></maryland-header>
```

### CSS Variable Usage
```css
/* Define custom properties */
--maryland-color-primary: #0066cc;
--maryland-font-body: 'Segoe UI', sans-serif;

/* Use in component styles */
background-color: var(--maryland-color-primary);
font-family: var(--maryland-font-body);
```

### CSS Class Pattern
```html
<a href="#" class="maryland-link">Hello World</a>
<button class="maryland-button maryland-button--primary">Submit</button>
<div class="maryland-card maryland-card--elevated">Content</div>
```

### Sass Variable Pattern
```scss
$maryland-color-primary: #0066cc;
$maryland-spacing-unit: 1rem;

.maryland-component {
  color: $maryland-color-primary;
  padding: $maryland-spacing-unit;
}
```

### Context

This architectural decision establishes the foundational naming standards for the entire MDWDS system. All components, utilities, CSS variables, and design tokens reference this decision to maintain consistency across the design system and prevent namespace collisions when MDWDS is integrated alongside other frameworks or design systems in consuming applications.

---

## Need Help?

*Getting Started*

This is a documentation page that provides guidance and resources for developers and designers using the Maryland Web Design System. It directs users to design assets, CDN resources, and support channels when they need assistance with implementation or have questions about the system.

### Key Information


This page includes:

- **Design Resources**: Links to Maryland Brand Pillars, Design Principles, Digital Services Playbook, and Figma Design Kit
- **Development Resources**: CDN asset links organized by environment:
  - Production Assets: Versioned CDN URLs (current stable version 0.44.0)
  - Development Assets: Assets from the main branch
  - PR Previews: Assets built from pull requests with "preview" label
  - Additional Resources: Links to Storybook, GitHub Repository, and How-To Guides

- **CDN URL patterns**:
  - Production: `https://cdn.maryland.gov/mdwds/{version}/css/mdwds.min.css`
  - Production JS: `https://cdn.maryland.gov/mdwds/{version}/js/mdwds-core.js`
  - Development: `https://designsystem.dev.maryland.dev/css/mdwds.min.css`
  - Development JS: `https://designsystem.dev.maryland.dev/js/mdwds-core.js`
  - PR Preview: `https://pr-XX-maryland-gov-mdwds-core-designsystem.preview.maryland.dev/css/mdwds.min.css`

- **Support Channels**:
  - GitHub issues and discussions
  - MDWDS Contributors Google Chat channel
  - How-To Guides and Architecture Decision Records (ADRs)


### Implementation


```html
<!-- Production Assets (Stable Release v0.44.0) -->
<link
  rel="stylesheet"
  href="https://cdn.maryland.gov/mdwds/0.44.0/css/mdwds.min.css"
/>
<script type="module" src="https://cdn.maryland.gov/mdwds/0.44.0/js/mdwds-core.js"></script>

<!-- Development Assets (Current Main Branch) -->
<link
  rel="stylesheet"
  href="https://designsystem.dev.maryland.dev/css/mdwds.min.css"
/>
<script type="module" src="https://designsystem.dev.maryland.dev/js/mdwds-core.js"></script>

<!-- PR Preview Assets (Replace XX with PR ID) -->
<link
  rel="stylesheet"
  href="https://pr-XX-maryland-gov-mdwds-core-designsystem.preview.maryland.dev/css/mdwds.min.css"
/>
<script type="module" src="https://pr-XX-maryland-gov-mdwds-core-designsystem.preview.maryland.dev/js/mdwds-core.js"></script>
```


### Context

This is the primary Getting Started documentation page for MDWDS, serving as a centralized hub for accessing all system resources including design files, CDN assets, and support information. It bridges the gap between designers (pointing to Figma) and developers (providing CDN URLs and GitHub resources).

---

## Playwright Testing

*Getting Started*

Playwright Testing is an end-to-end visual regression testing setup used by the Maryland Web Design System to ensure components render consistently across different viewports and browsers. It tests components via Storybook stories, captures visual snapshots across mobile, tablet, and desktop sizes, and runs in Docker containers for cross-platform consistency. Use this guide to run tests, update snapshots when components change intentionally, and generate test reports.

### Key Information

## Key Information

### What It Tests
- Components via Storybook stories
- Visual snapshots across multiple viewport sizes (mobile, tablet, desktop)
- Accessibility with @axe-core/playwright
- Cross-browser consistency

### Running Tests

**Run all tests:**
```
pnpm test:e2e
```

**Run specific tests** (use --tests flag with pattern):
```
pnpm test:e2e --tests accordion
pnpm test:e2e --tests hero
```

**Update snapshots** (when component visuals change intentionally):
```
# Update all snapshots
pnpm test:e2e:update-snapshots

# Update specific component snapshots
pnpm test:e2e:update-snapshots --tests accordion
```

### Important Prerequisites
- Prior to running tests, a static Storybook build must exist
- Run `pnpm build` to compile static assets
- Run `pnpm storybook:build` to create static Storybook build

### Test Reports
- **Local runs:** Test report generated in `/playwright-report`
- **CI runs:** Report available as downloadable .zip file on GitHub Actions summary page
- View report by opening the enclosed `index.html` in a browser

### Project Structure
```
e2e/
├── playwright.config.ts        # Playwright configuration
├── src/
│   ├── fixtures/
│   │   └── test.ts            # Custom Storybook fixtures
│   ├── helpers/
│   │   ├── storybook.ts       # Storybook navigation helpers
│   │   ├── images.ts
```

### Testing Features
- Tests executed via bash script running Playwright in Docker container
- Custom fixtures for streamlined Storybook integration
- Ensures consistent results across different development environments

### Implementation

This is a Getting Started documentation page describing testing infrastructure and processes rather than a renderable component. No HTML component implementation is applicable. The page provides configuration instructions and command-line examples for running the Playwright test suite integrated with the MDWDS Storybook environment.

### Context

Playwright Testing is part of the MDWDS development and quality assurance workflow. It integrates with the Storybook component library to provide automated visual regression testing and accessibility checking across all MDWDS components, ensuring consistency and accessibility standards are maintained across viewports and browsers.

---

## Use BEM Convention for CSS

*Getting Started*

This is an Architectural Decision Record (ADR) documenting the adoption of BEM (Block Element Modifier) as the standard CSS class naming convention for the Maryland Design System. BEM provides a consistent, scalable approach to naming that improves code clarity, reduces CSS collisions, and makes the relationship between styles and markup self-evident.

### Key Information

## BEM Structure

The BEM naming convention uses the format: `block-name__element-name--modifier-name`

### Components:

- **Block**: A standalone component representing the highest-level abstraction (e.g., `maryland-card`)
- **Element**: A part or child of the block, denoted with double underscore `__` (e.g., `maryland-card__title`)
- **Modifier**: A variation, state, or flag applied to a block or element, denoted with double hyphens `--` (e.g., `maryland-card--highlighted`)

### Key Facts:

- No class name prefix is shown in the example content; components should use the `maryland-` namespace prefix for consistency across the system
- BEM improves readability by making styles self-descriptive
- Reduces CSS specificity collisions in large-scale applications
- Encourages modular, component-driven development
- Compatible with utility-first frameworks, SCSS modules, and preprocessors
- Class names may be verbose but provide clear semantic meaning

### Implementation

```html
<!-- BEM Naming Convention Example -->
<div class="maryland-card maryland-card--highlighted">
  <h2 class="maryland-card__title">Card Title</h2>
  <p class="maryland-card__content">Description here...</p>
</div>
```

### Structure Breakdown:

- `maryland-card` — Block (standalone component)
- `maryland-card__title` — Element (part of the block, child component)
- `maryland-card__content` — Element (another part of the block)
- `maryland-card--highlighted` — Modifier (variation/state applied to the block)

### Naming Pattern:

```
Block:     block-name
Element:   block-name__element-name
Modifier:  block-name--modifier-name
Combined:  block-name__element-name--modifier-name
```

Each class should clearly indicate its role and hierarchy within the component structure.

### Context

This ADR establishes a foundational naming convention that applies across all components, utilities, and templates in the MDWDS. By standardizing on BEM, all contributors—whether working on Foundation elements, Components, or Templates—can follow the same predictable naming pattern, improving consistency, discoverability, and maintainability throughout the entire design system.

---

## Welcome

*Getting Started*

This is the welcome/introduction page for the Maryland Web Design System (MDWDS). It provides an overview of what MDWDS is and its purpose: to help Maryland government teams design, build, and measure high-performing digital services that are consistent, accessible, well-designed, and mobile-friendly. The page notes that the system is currently under development and will evolve in response to user needs and changing technology.

### Key Information

- This is a documentation/welcome page, not a reusable component
- Contains informational alert using `usa-alert` and `usa-alert--info` classes
- Page structure uses `sbdocs` and `sbdocs-wrapper` classes for Storybook documentation layout
- Alert body uses `usa-alert__body` and `usa-alert__text` classes
- Table of Contents (TOC) navigation with `toc-wrapper`, `toc-list`, and `toc-list-item` classes
- Includes links to external resources (MDWDS Contributors Google Chat channel)
- The MDWDS is in early stages of development
- Future announcements will be made in the Google Chat channel

### Implementation

```html
<div class="sbdocs sbdocs-wrapper">
  <aside class="sbdocs sbdocs-toc--custom">
    <nav aria-labelledby="_r_0_">
      <h2 id="_r_0_">Table of Contents</h2>
      <div class="toc-wrapper">
        <ul class="toc-list">
          <li class="toc-list-item is-active-li">
            <a href="#a-design-system-for-the-state-of-maryland" class="toc-link node-name--H3 is-active-link">
              A design system for the State of Maryland
            </a>
          </li>
        </ul>
      </div>
    </nav>
  </aside>
  <div class="sbdocs sbdocs-content">
    <h1 id="maryland-web-design-system-mdwds">Maryland Web Design System (MDWDS)</h1>
    <h3 id="a-design-system-for-the-state-of-maryland">A design system for the State of Maryland</h3>
    <p>The Maryland Web Design System (MDWDS) provides design, code, and guidance to help Maryland government teams design, build, and measure high-performing digital services that are consistent, accessible, well-designed, and mobile-friendly.</p>
    <div class="usa-alert usa-alert--info">
      <div class="usa-alert__body">
        <p class="usa-alert__text">The MDWDS is currently under development and still in its early stages.</p>
      </div>
    </div>
    <p>The MDWDS will evolve over time in response to the needs of users, as well as to changing technology. As new UI components and patterns are released, we will announce them in the <a href="https://chat.google.com/room/AAAAxp8FY9A?cls=7" target="_top" rel="nofollow">MDWDS Contributors Google Chat channel</a>.</p>
  </div>
</div>
```

### Context

This is the landing/welcome documentation page for MDWDS that introduces the design system to users and establishes its purpose. It serves as the entry point for the Storybook documentation and directs users to other resources for staying updated on new components and patterns as the system evolves.

---

## When to Use Web Components vs. Standard HTML + CSS in MDWDS

*Getting Started*

This is an Architectural Decision Record (ADR) that establishes guidelines for when to use Web Components versus standard HTML + CSS in the Maryland Web Design System. It provides boundary conditions and anti-patterns to help developers make informed decisions about component implementation, emphasizing that standard HTML should be the default approach unless Web Components offer meaningful encapsulation or framework-agnostic behavior.

### Key Information

**Key Decision Principles:**

- **Default to standard HTML markup** — Use native HTML, utility classes, and ARIA attributes as the preferred approach
- **Use Web Components selectively** — Only introduce them when they offer meaningful encapsulation, framework-agnostic behavior, or replace something requiring an iframe, embedded script, or complex JavaScript
- **Avoid wrapping basic native elements** — Do not replace `<a>`, `<button>`, `<input>` with custom components unless significant value is added in behavior, accessibility, or usability
- **Use Web Components for static, reusable elements** — Examples: site-wide banners, footers, alert regions that are centrally managed and reused across Maryland.gov properties
- **Embedded styles** — Web Components should include embedded styles to support fallback display when JavaScript is disabled
- **Anti-pattern** — Do not use Web Components merely to shorten verbose HTML (e.g., replacing multi-div structures with `<alert>` tags)

**Status:** Proposed  
**Date:** 2025-06-01

### Implementation

**Avoid — Web Component for brevity (Anti-Pattern):**

```html
<alert>
  <div slot="heading">Informative status</div>
  <div slot="text">Lorem ipsum dolor sit amet.</div>
</alert>
```

**Prefer — Standard HTML with utility classes and ARIA:**

```html
<div class="alert" role="status" aria-live="polite">
  <h3 class="alert__heading">Informative status</h3>
  <p class="alert__text">Lorem ipsum dolor sit amet.</p>
</div>
```

**When Web Components ARE Appropriate:**

```html
<!-- Site-wide banner (static, reusable, centrally managed) -->
<md-site-banner>
  <!-- embedded styles included for JS-disabled fallback -->
</md-site-banner>

<!-- Footer (static, reusable across Maryland.gov properties) -->
<md-site-footer>
  <!-- embedded styles included for JS-disabled fallback -->
</md-site-footer>
```

### Context

This ADR provides architectural guidance for the entire MDWDS system, establishing standards that all component authors and system consumers should follow. It helps maintain consistency across Maryland.gov properties and ensures that component choices prioritize accessibility, portability, and performance over unnecessary complexity.

---

# Foundation

## Block Spacing

*Foundation*

Block Spacing is a foundational spacing system for components on the page where each component manages its own block-level spacing. The `.block-spacing` class is available to apply consistent vertical spacing between major page sections and components. Use this to maintain visual rhythm and consistent white space throughout your layouts.

### Key Information

- **CSS Class**: `.block-spacing` - Apply to block-level elements (sections, divs) to add consistent spacing
- **Usage**: Wrap component sections with the `.block-spacing` class to automatically apply appropriate margins
- **Scope**: Each component manages its own block-spacing internally; the utility class is also available for manual application
- **Note**: Multiple `.block-spacing` sections can be stacked on a single page and will respect the MDWDS spacing system

### Implementation

```html
<div class="usa-prose">
  <h1>Block Spacing</h1>
  <p>
    The blocks below represent components placed on the page. Each component
    manages its own block-spacing, and a
    <code>.block-spacing</code> class is available.
  </p>
  <section class="block-spacing"></section>
  <section class="block-spacing"></section>
</div>
```

**Styling Context** (for reference):
```css
section {
  min-height: 10rem;
  background-color: lightgray;
  outline: 2px dashed gray;
  outline-offset: -2px;
}
```

### Context

Block Spacing is a foundational spacing utility in MDWDS that works in conjunction with the `usa-prose` wrapper to provide consistent vertical rhythm across page layouts. It is typically applied to container elements alongside prose and component sections to maintain predictable spacing relationships.

---

## Colors

*Foundation*

The Colors foundation provides a standardized color palette for the Maryland Web Design System based on USWDS colors. It includes semantic color names (primary, secondary, accent-cool, accent-warm, info, success, warning, error, emergency, disabled, base) with multiple tints/shades for each. Use colors intentionally and consistently throughout projects to convey meaning, emotion, and information hierarchy while maintaining accessibility.

### Key Information

## Color Families

The MDWDS color system includes 11 semantic color families:
- **base** — neutral grays
- **primary** — Maryland blue (primary brand color)
- **secondary** — Maryland gold/yellow
- **accent-cool** — cyan/teal accents
- **accent-warm** — orange/warm accents
- **info** — information/notice blue
- **success** — success/positive green
- **warning** — warning/caution orange
- **error** — error/critical red
- **emergency** — emergency red
- **disabled** — disabled state gray

## Color Tints & Shades

Each color family includes 8 variants:
- **lightest** — lightest tint
- **lighter** — lighter tint
- **light** — light tint
- **default** — base color
- **vivid** — saturated/vivid variant
- **dark** — dark shade
- **darker** — darker shade
- **darkest** — darkest shade

## Integration Options

1. **Option 1: Limited environments** — Use colors directly from the palette for custom builds
2. **Option 2: Full MDWDS via CDN** — Include `https://cdn.maryland.gov/mdwds/latest/css/mdwds.min.css`
3. **Option 3 (experimental): CSS Variables** — Include `https://cdn.maryland.gov/mdwds/latest/css/colors.css`

## CSS Variables & Utilities

- MDWDS provides CSS variables in the format `var(--maryland-color-*)`
- Utility classes available for text color and background color applications
- Text color utilities apply foreground colors
- Background color utilities apply background colors

## Best Practices

- Use colors intentionally and consistently (same blue throughout as primary)
- Use colors to convey emotion, importance, and information categories
- **Avoid** introducing custom colors outside the palette
- **Never** use color alone to convey meaning (pair with icons/symbols for errors, etc.)

### Implementation

## CSS Variables

```css
.example {
  background-color: var(--maryland-color-primary);
  color: var(--maryland-color-base-darkest);
}

.success-message {
  background-color: var(--maryland-color-success-lighter);
  color: var(--maryland-color-success-darkest);
  border-left: 4px solid var(--maryland-color-success);
}

.error-message {
  background-color: var(--maryland-color-error-lighter);
  color: var(--maryland-color-error-darkest);
  border-left: 4px solid var(--maryland-color-error);
}

.warning-message {
  background-color: var(--maryland-color-warning-lighter);
  color: var(--maryland-color-warning-darkest);
  border-left: 4px solid var(--maryland-color-warning);
}

.info-message {
  background-color: var(--maryland-color-info-lighter);
  color: var(--maryland-color-info-darkest);
  border-left: 4px solid var(--maryland-color-info);
}

.disabled-button {
  background-color: var(--maryland-color-disabled-light);
  color: var(--maryland-color-disabled-darker);
  cursor: not-allowed;
}
```

## CDN Integration

```html
<!-- Option 2: Full MDWDS integration via CDN -->
<link
  rel="stylesheet"
  href="https://cdn.maryland.gov/mdwds/0.44.0/css/mdwds.min.css"
/>

<!-- Option 3 (experimental): CSS Variables only -->
<link
  rel="stylesheet"
  href="https://cdn.maryland.gov/mdwds/0.44.0/css/colors.css"
/>
```

## Color Families Available

- `--maryland-color-base-lightest` through `--maryland-color-base-darkest`
- `--maryland-color-primary-lightest` through `--maryland-color-primary-darkest`
- `--maryland-color-secondary-lightest` through `--maryland-color-secondary-darkest`
- `--maryland-color-accent-cool-lightest` through `--maryland-color-accent-cool-darkest`
- `--maryland-color-accent-warm-lightest` through `--maryland-color-accent-warm-darkest`
- `--maryland-color-info-lightest` through `--maryland-color-info-darkest`
- `--maryland-color-success-lightest` through `--maryland-color-success-darkest`
- `--maryland-color-warning-lightest` through `--maryland-color-warning-darkest`
- `--maryland-color-error-lightest` through `--maryland-color-error-darkest`
- `--maryland-color-emergency-lightest` through `--maryland-color-emergency-darkest`
- `--maryland-color-disabled-lightest` through `--maryland-color-disabled-darkest`

### Context

Colors are a foundational design token in the MDWDS system, derived from the United States Web Design System (USWDS) palette but tailored to reflect Maryland's natural features and state flag. All semantic color usage throughout MDWDS components (buttons, alerts, badges, links, etc.) builds upon this foundation, ensuring visual consistency and accessibility compliance across the entire design system.

---

## Maryland Logo

*Foundation*

The Maryland Logo is the official logo for the State of Maryland, provided in multiple format variants (vertical/horizontal, black/white text). These guidelines ensure proper and accurate logo use to maintain brand consistency across state applications. Use the vertical logo for general applications, and the horizontal variant only when space constraints require it.

### Key Information

## Logo Variants

- **Vertical with Black Text**: Default version for general applications
- **Vertical with White Text**: Use on dark backgrounds
- **Horizontal with Black Text**: Use when vertical space is limited
- **Horizontal with White Text**: Use on dark backgrounds with space constraints

## Logo Colors

The logo employs four primary colors with CSS custom properties:

- **Maryland Red**: `--maryland-color-logo-red` / `var(--maryland-color-logo-red)` / `#c8122c`
- **Maryland Gold**: `--maryland-color-logo-gold` / `var(--maryland-color-logo-gold)` / `#ffc838`
- **Black**: `--maryland-color-logo-black` / `var(--maryland-color-logo-black)` / `#231f20`
- **White**: `--maryland-color-logo-white` / `var(--maryland-color-logo-white)` / `#ffffff`

## Typography

The logo uses **Montserrat Semi Bold** typeface.

## Download Formats

- Vertical with Black Text: SVG, PNG, JPG
- Vertical with White Text: SVG, PNG (1x, 2x, 3x, 4x)
- Horizontal with Black Text: SVG
- Horizontal with White Text: SVG, PNG (1x, 2x, 3x, 4x)

## Usage Guidelines

**Do:**
- Use Vertical Logo for general applications (or as directed)
- Use Horizontal Logo only when space constraints require it

**Do Not:**
- Outline, distort, or manipulate the logo
- Use unapproved color variations or opacity
- Alter logo colors, typefaces, or layout
- Place logo over text, graphics, or patterns
- Apply effects or use unapproved versions

### Implementation

## CSS Custom Properties

Logo colors are accessible via CSS custom properties:

```html
<link
  rel="stylesheet"
  href="https://cdn.maryland.gov/mdwds/0.44.0/css/colors.css"
/>
```

## HTML Usage Example

```html
<p class="maryland-color-logo-red">This text uses the red logo color</p>
```

## Logo Assets

The following SVG logo files are available for use:

- `/img/md_wordmark_vertical.svg` – Vertical logo with black text
- Vertical logo with white text (SVG version)
- Horizontal logo with black text (SVG version)
- Horizontal logo with white text (SVG version)

PNG and JPG variants are also available in multiple resolutions (1x, 2x, 3x, 4x for PNG versions).

## Color Variable Usage

```css
/* Apply logo colors using CSS custom properties */
color: var(--maryland-color-logo-red);
color: var(--maryland-color-logo-gold);
color: var(--maryland-color-logo-black);
color: var(--maryland-color-logo-white);
```

### Context

The Maryland Logo is a foundational branding element within the MDWDS system, establishing the State of Maryland's visual identity. The accompanying color palette (red, gold, black, white) serves as a base for theming and branding across other components and templates in the design system.

---

## Typography

*Foundation*

Typography defines the typeface, sizing, and styling standards for the Maryland Web Design System. It covers font selection, hierarchy, and best practices for readable, accessible text across all components and pages. Use this foundation to maintain visual consistency and legibility throughout MDWDS implementations.

### Key Information

## Typefaces

**Primary Typeface: Source Sans Pro Web**
- Default typeface for all MDWDS components and pages
- Selected for high legibility, platform accessibility, and USWDS standards compliance
- Automatically included and applied via CDN or future NPM packages

**Alternate Typeface: Merriweather**
- Secondary/accent typeface option
- Also selected for high legibility, platform accessibility, and USWDS standards compliance
- Automatically included via CDN or NPM packages

## Typography Best Practices

- Use "Source Sans Pro Web" as the primary font across all components and pages
- Set a base font size of 16px on html or body element
- Scale text using relative units (rem, em) instead of fixed pixel values
- Maintain clear visual hierarchy using defined heading levels (h1–h6)

## Heading Levels

The system supports semantic heading levels h1 through h6 for creating document structure and visual hierarchy.

## Text Elements

- **Paragraph Text**: Standard body copy using base font size
- **Lists**: Unordered, ordered, and description lists for organizing content
- **Grid Container**: Layout mechanism for organizing typographic content

### Implementation

Typography in MDWDS is applied through standard semantic HTML elements and inherited font stack. No special component markup is required.

## Base Font Configuration

```html
<html style="font-size: 16px;">
  <body style="font-family: 'Source Sans Pro Web', sans-serif;">
    <!-- Content -->
  </body>
</html>
```

## Heading Levels (h1–h6)

```html
<h1>Heading Level 1</h1>
<h2>Heading Level 2</h2>
<h3>Heading Level 3</h3>
<h4>Heading Level 4</h4>
<h5>Heading Level 5</h5>
<h6>Heading Level 6</h6>
```

## Paragraph Text

```html
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
```

## Lists

### Unordered List
```html
<ul>
  <li>List item one</li>
  <li>List item two</li>
  <li>List item three</li>
</ul>
```

### Ordered List
```html
<ol>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ol>
```

### Description List
```html
<dl>
  <dt>Term</dt>
  <dd>Definition</dd>
</dl>
```

## Using Alternate Typeface (Merriweather)

Apply the Merriweather font family to specific elements as needed:

```html
<h2 style="font-family: 'Merriweather', serif;">Alternate Typeface Heading</h2>
```

### Context

Typography is a foundational design element in MDWDS that establishes the visual language and reading experience across all components and pages. It works in concert with the color palette and spacing system to create consistent, accessible interfaces. Proper typography scaling using relative units ensures responsive design works correctly across all device sizes.

---

## Typography

*Foundation*

Typography is the foundational system for text styling in MDWDS, providing standardized heading levels, font families, sizes, and line heights from USWDS. It establishes readable, accessible body text at minimum 16px (token 5), lead paragraphs for introductory content, and comprehensive typeface options including Source Sans Pro, Merriweather, Public Sans, and Roboto Mono. Use typography utilities to maintain consistent hierarchy, readability, and accessibility across digital products.

### Key Information

## Typefaces
- **Source Sans Pro**: Primary sans-serif for UI design
- **Merriweather**: Serif for extended reading
- **Public Sans**: Alternative sans-serif
- **Roboto Mono**: Monospaced for code

## Heading Levels
- Supports: display, h1, h2, h3, h4, h5, h6
- Each level represents a different hierarchy in content structure

## Font Sizes
- USWDS token scale: 1, 2, 3, 4, 5, 6
- Minimum body text size: 16px (token 5) for accessibility
- Font family options: sans, serif, mono

## Line Heights
- Line height adjustments available for optimal readability
- Measured in sans-compatible scales

## Measure (Line Length) Variants
- measure-2: Recommended 66 characters for extended reading
- Ensures comfortable reading lengths

## CSS Classes Used
- `usa-intro`: Lead paragraph styling for introductory text
- `font-sans-5`: Font family and size utility (sans-serif, token 5)
- `line-height-sans-5`: Line height utility for sans-serif scale token 5
- `measure-2`: Line length/measure utility for comfortable reading width

## Key Requirements
- Maintain proper heading hierarchy for screen readers
- Use flush-left alignment for consistency
- Minimum body text size: 16px (font-size 5) for running text
- Lead paragraphs use larger text to draw attention and provide context

### Implementation

```html
<!-- Typography Showcase Container -->
<div>
  <h2>Typography Showcase</h2>
  
  <!-- Lead Paragraph (Introductory Text) -->
  <p class="usa-intro">This is a lead paragraph that introduces the content. Lead paragraphs use larger text to draw attention and provide context.</p>
  
  <!-- Body Text with Font, Line Height, and Measure Controls -->
  <p class="font-sans-5 line-height-sans-5 measure-2">This is body text at the default size. Body text should be comfortable to read for extended periods. The USWDS recommends using at least 16px font size (token 5) for running text.</p>
</div>
```

### CSS Class Modifiers

**Lead Paragraph:**
- `usa-intro` — Applies lead paragraph styling with larger text size

**Font & Size Utilities:**
- `font-sans-5` — Sans-serif typeface at token size 5 (16px)
- `font-serif-*` — Serif typeface variants
- `font-mono-*` — Monospaced typeface variants

**Line Height Utilities:**
- `line-height-sans-5` — Line height control for sans-serif at token 5

**Measure (Reading Width) Utilities:**
- `measure-2` — Optimal line length of approximately 66 characters for comfortable reading

### Context

Typography is a foundational element of the MDWDS system that provides the typographic building blocks for all text-based content. It works across all component types—from headings in Headers and Statewide Banners to body text in Cards, Lists, and Content blocks—ensuring consistent, accessible text rendering throughout digital Maryland products.

---

# Components

## Accordion

*Components*

Accordions are collapsible content sections that hide or reveal additional information when selected. They solve the problem of displaying large amounts of content in a limited space by letting users access only the specific information they need. Use accordions when users need only a few specific pieces of content within a page or when space is constrained.

### Key Information

## Variants
- **default**: Standard accordion styling
- **bordered**: Accordion with border styling

## Key CSS Classes
- `maryland-accordion`: Root wrapper for the accordion component
- `maryland-accordion__list`: Container for the accordion header and description
- `maryland-accordion__list--heading`: Heading text for the accordion list
- `maryland-accordion__list--content`: Description text for the accordion list
- `maryland-accordion__items`: Container for all accordion items
- `maryland-accordion__item`: Individual accordion item wrapper
- `maryland-accordion__heading`: Heading container for each item
- `maryland-accordion__button`: Clickable button to expand/collapse items

## Required Attributes
- `aria-labelledby`: Points to the ID of the accordion title
- `aria-expanded`: Boolean indicating if accordion item is open/closed
- `aria-controls`: Points to the ID of the controlled content panel
- `type="button"`: Required on accordion trigger buttons

## Configuration Props
- `accordionListTitle` (string): Title for the accordion list
- `accordionListDescription` (string): Description text for the accordion list
- `variant` (string): Choose between "default" or "bordered"
- `items` (array): Array of accordion items, each with properties for the item content
- `headingLevel` (string): Semantic heading level (h1-h6) for accordion items
- `ariaLabel` (string): Accessible label for the accordion
- `role` (string): ARIA role - "none", "group", or "region"

## Important Facts
- Accordion items use semantic heading elements (h2, h3, etc.) based on the `headingLevel` prop
- Each accordion item requires unique IDs for the button and controlled content panel
- The component requires proper ARIA attributes for screen reader accessibility

### Implementation

```html
<!-- Root accordion section with aria-labelledby reference -->
<section class="maryland-accordion" aria-labelledby="id-oj7o2dygx4">
  
  <!-- Accordion header section -->
  <div class="maryland-accordion__list">
    <h2 class="maryland-accordion__list--heading" id="id-oj7o2dygx4">
      Accordion Title
    </h2>
    <p class="maryland-accordion__list--content">
      Accordion description text.
    </p>
  </div>
  
  <!-- Container for accordion items -->
  <div class="maryland-accordion__items">
    
    <!-- Individual accordion item -->
    <div class="maryland-accordion__item">
      <h3 class="maryland-accordion__heading">
        <button 
          type="button" 
          class="maryland-accordion__button" 
          id="id-4makj0jlhaj" 
          aria-expanded="true" 
          aria-controls="id-jywwykfz2ar"
        >
          First Amendment
        </button>
      </h3>
      <!-- Content panel controlled by the button above -->
      <div id="id-jywwykfz2ar" class="maryland-accordion__panel">
        Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof...
      </div>
    </div>
    
    <!-- Additional accordion items follow the same structure -->
    <div class="maryland-accordion__item">
      <h3 class="maryland-accordion__heading">
        <button 
          type="button" 
          class="maryland-accordion__button" 
          id="id-second" 
          aria-expanded="false" 
          aria-controls="id-second-panel"
        >
          Second Amendment
        </button>
      </h3>
      <div id="id-second-panel" class="maryland-accordion__panel">
        <!-- Content here -->
      </div>
    </div>
    
  </div>
  
</section>
```

## Variant: Bordered
Add a modifier class to the root section:
```html
<section class="maryland-accordion maryland-accordion--bordered" aria-labelledby="id-oj7o2dygx4">
  <!-- Same structure as above -->
</section>
```

### Context

The Accordion component is a foundational UI pattern in MDWDS used to organize and present grouped information while conserving page space. It works in concert with semantic HTML heading elements and ARIA attributes to ensure accessibility, and is typically used within page templates to structure FAQs, help content, or collapsible sections of forms.

---

## Accordion

*Components*

An accordion is a list of headers that hide or reveal additional content when selected. It provides fully accessible keyboard and screen reader support, making it ideal for organizing related content that users can expand or collapse on demand. Use accordions to reduce cognitive load and allow users to focus on relevant sections.

### Key Information

## Variants
- **default**: Standard accordion styling
- **bordered**: Accordion with borders between items

## Key Class Names
- `usa-accordion`: Main container class
- `usa-accordion__heading`: Wraps each accordion header (typically an h4)
- `usa-accordion__button`: Clickable button that toggles content visibility
- `usa-accordion__content`: Content container that shows/hides based on button state

## Required Attributes
- `aria-expanded`: Boolean indicating if content is open or closed (set on button)
- `aria-controls`: ID reference linking button to its content panel (set on button)
- `id`: Unique identifiers required on both button and content elements for aria-controls/aria-labelledby linking
- `type="button"`: Required on accordion buttons

## Options
- **variant**: Choose between "default" or "bordered"
- **items**: Array of accordion items (each with title, content, and optional properties)
- **headingLevel**: Control heading level (h1–h6) for the accordion headers
- **ariaLabel**: Optional string for labeling the accordion container
- **role**: Optional role attribute supporting "none", "group", or "region"

## Accessibility Features
- Full keyboard navigation support (arrow keys, Enter/Space to toggle)
- Screen reader support with aria-expanded and aria-controls
- Supports aria-label, aria-describedby, and semantic roles
- Follows USWDS and WCAG accessibility standards

### Implementation

```html
<div class="usa-accordion">
  <h4 class="usa-accordion__heading">
    <button 
      type="button" 
      class="usa-accordion__button" 
      id="id-gx85lsle3qv" 
      aria-expanded="true" 
      aria-controls="id-z8onz0r06vi">
      First Amendment
    </button>
  </h4>
  <div 
    class="usa-accordion__content" 
    id="id-z8onz0r06vi" 
    aria-labelledby="id-gx85lsle3qv">
    <p>Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof...</p>
  </div>

  <h4 class="usa-accordion__heading">
    <button 
      type="button" 
      class="usa-accordion__button" 
      id="id-198d5p7f6lw" 
      aria-expanded="false" 
      aria-controls="id-content-198d5p7f6lw">
      Second Amendment
    </button>
  </h4>
  <div 
    class="usa-accordion__content" 
    id="id-content-198d5p7f6lw" 
    aria-labelledby="id-198d5p7f6lw">
    <p>A well regulated Militia, being necessary to the security of a free State...</p>
  </div>
</div>
```

## Key Structure Notes
- Wrap accordion in a `div` with class `usa-accordion`
- Each item consists of a heading containing a button and a content panel
- Button must have unique `id` and reference content panel via `aria-controls`
- Content panel must have unique `id` matching button's `aria-controls` value
- Use `aria-labelledby` on content to reference the button ID
- `aria-expanded` toggles between "true" (open) and "false" (closed) as users interact

### Context

The Accordion is a USWDS-based component that follows U.S. web standards for accessible disclosure widgets. It integrates seamlessly with other MDWDS components and can be combined with typography, spacing utilities, and other structural components to create complex content organizations.

---

## Action Items

*Components*

Action Items provide a list of tasks, steps, or featured actions that users need to complete or can choose to engage with. They can be displayed with optional icons, status indicators, and descriptions to guide users through workflows or highlight key actions on a page.

### Key Information

## Variants & Modifiers

- **Featured Actions**: Basic list of action items displayed as links
- **Action Spotlight**: Items with descriptions, nested sub-items, and optional grouping
- **Action Group**: Items grouped with category headers and optional group descriptions

## CSS Classes

- `maryland-featured-actions`: Main container wrapper
- `maryland-featured-actions__list`: Container for list items (uses `<ul>`)
- `maryland-featured-actions__item`: Individual list item wrapper
- `maryland-featured-actions__link`: Anchor element for each action

## Required Attributes

- List items must be semantic `<li>` elements
- Links use standard `<a>` href attribute
- Structure uses valid HTML list semantics

## Important Facts

- Items are organized as an unordered list
- Each item contains a wrapped link element
- Can be nested with sub-items for action spotlights
- Supports optional descriptions and grouping via heading structure
- Flexible for grouping items under categories or sections
- Component data structure uses an `items` array property

### Implementation

```html
<!-- Featured Actions (Basic) -->
<div class="maryland-featured-actions">
  <ul class="maryland-featured-actions__list">
    <li class="maryland-featured-actions__item">
      <div>
        <a class="maryland-featured-actions__link" href="javascript:void(0)">Learn more and make an appointment today</a>
      </div>
    </li>
    <li class="maryland-featured-actions__item">
      <div>
        <a class="maryland-featured-actions__link" href="javascript:void(0)">Find out how to apply for SNAP</a>
      </div>
    </li>
    <li class="maryland-featured-actions__item">
      <div>
        <a class="maryland-featured-actions__link" href="javascript:void(0)">Find a group near you</a>
      </div>
    </li>
  </ul>
</div>
```

```html
<!-- Action Spotlight (With descriptions and nested items) -->
<div class="maryland-featured-actions">
  <ul class="maryland-featured-actions__list">
    <li class="maryland-featured-actions__item">
      <h3>Check eligibility for food and nutrition benefits</h3>
      <p>Learn about the benefits you may qualify for in just five minutes with the benefits screener.</p>
      <a class="maryland-featured-actions__link" href="javascript:void(0)">Check eligibility now</a>
    </li>
    <li class="maryland-featured-actions__item">
      <h3>SNAP guides for participants</h3>
      <ul class="maryland-featured-actions__list">
        <li class="maryland-featured-actions__item">
          <a class="maryland-featured-actions__link" href="javascript:void(0)">Use SNAP for online grocery shopping</a>
        </li>
        <li class="maryland-featured-actions__item">
          <a class="maryland-featured-actions__link" href="javascript:void(0)">Check out the SNAP quality control guide</a>
        </li>
      </ul>
    </li>
  </ul>
</div>
```

### Context

Action Items are a foundational component within the MDWDS for organizing and presenting task-based content to users. They serve as building blocks for templates like action pages and can be composed with headings, descriptions, and nested groupings to create complex action hierarchies and navigation structures.

---

## Alert

*Components*

Alerts communicate important information to users in a clear, timely, and accessible manner. The component supports ARIA roles, live region updates, describedBy links, and labeling for optimal screen reader behavior. Use alerts to notify users of status changes, warnings, errors, or other critical information that requires attention.

### Key Information

## Variants
The Alert component supports the following status variants that determine visual styling:
- `info` — Informational status (default)
- `warning` — Warning status
- `success` — Success status
- `error` — Error status
- `emergency` — Emergency status

## CSS Classes
- `maryland-alert` — Main alert container
- `maryland-alert--info` — Info variant (status modifier)
- `maryland-alert--warning` — Warning variant
- `maryland-alert--success` — Success variant
- `maryland-alert--error` — Error variant
- `maryland-alert--emergency` — Emergency variant
- `maryland-alert__container` — Inner container wrapper
- `maryland-alert__body` — Body content area
- `maryland-alert__heading` — Alert heading element
- `maryland-alert__text` — Alert message text container

## Properties
- **status** (string) — Visual style of the alert (info, warning, success, error, emergency)
- **heading** (string) — Text for the alert heading (ignored in slim mode)
- **message** (string) — Main message text for the alert
- **slim** (boolean) — Use slim variant (no heading by default)
- **noIcon** (boolean) — Hide icon

## ARIA & Accessibility
- `role="status"` — Identifies the alert as a status region for live updates
- `aria-labelledby` — Links to the heading ID for proper labeling
- HTML is allowed in the message content; be sure to escape or sanitize properly

### Implementation

```html
<!-- Basic Informational Alert -->
<div class="maryland-alert maryland-alert--info" role="status" aria-labelledby="maryland-alert-id-93bwol4mcje">
  <div class="maryland-alert__container">
    <div class="maryland-alert__body">
      <h2 class="maryland-alert__heading" id="maryland-alert-id-93bwol4mcje">
        Informational status
      </h2>
      <div class="maryland-alert__text">
        <p>Lorem ipsum dolor sit amet, <a class="usa-link maryland-link" href="#">consectetur adipiscing</a> elit, sed do eiusmod.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
      </div>
    </div>
  </div>
</div>
```

## Alert Status Variants
The status variant is controlled by the `maryland-alert--{status}` modifier class:

- **Info**: `class="maryland-alert maryland-alert--info"`
- **Warning**: `class="maryland-alert maryland-alert--warning"`
- **Success**: `class="maryland-alert maryland-alert--success"`
- **Error**: `class="maryland-alert maryland-alert--error"`
- **Emergency**: `class="maryland-alert maryland-alert--emergency"`

## Key Structure
- Alert container requires `role="status"` for live region announcements
- `aria-labelledby` must reference the heading element's `id` for proper screen reader association
- The heading is wrapped in an `h2` element (or appropriate heading level)
- Message content goes in `maryland-alert__text` and supports HTML with proper sanitization

### Context

The Alert component is a core component in the MDWDS system used to communicate urgent or important information to users. It integrates with the Maryland design system's color and typography standards and can contain inline links using the `usa-link` and `maryland-link` classes for consistency with other MDWDS components.

---

## Alerts

*Components*

Alerts communicate important information to users in a clear, timely, and accessible manner. This component supports ARIA roles, live region updates, describedBy links, and labeling for optimal screen reader behavior. Use alerts to display status messages, warnings, errors, and informational content that requires user attention.

### Key Information

## Variants and Modifiers

**Status variants** (visual styles via `usa-alert--{status}` modifier):
- `info` - Informational status (blue)
- `warning` - Warning status (gold/yellow)
- `success` - Success status (green)
- `error` - Error status (red)
- `emergency` - Emergency status (dark red)

**Display modes:**
- Full alert (default) - includes heading, icon, and message
- Slim variant - compact display without heading by default (use `slim` property)
- No icon variant - hide the status icon (use `noIcon` property)

## CSS Classes

- `usa-alert` - Main alert container
- `usa-alert--info`, `usa-alert--warning`, `usa-alert--success`, `usa-alert--error`, `usa-alert--emergency` - Status modifiers
- `usa-alert__body` - Container for alert content
- `usa-alert__heading` - Alert heading (h4)
- `usa-alert__text` - Alert message text

## Key Properties

- **status** (string): Visual style of the alert (info, warning, success, error, emergency)
- **heading** (string): Text for the alert heading (ignored in slim mode)
- **message** (string): Main message text for the alert
- **slim** (boolean): Use slim variant (no heading by default)
- **noIcon** (boolean): Hide icon

## Important Notes

- HTML is allowed in the message content; ensure content is properly escaped or sanitized
- Component supports inline links via `usa-link` class within message text
- Full screen reader support with ARIA roles and live region capabilities

### Implementation

```html
<!-- Standard Informational Alert -->
<div class="usa-alert usa-alert--info">
  <div class="usa-alert__body">
    <h4 class="usa-alert__heading">Informational status</h4>
    <p class="usa-alert__text">Lorem ipsum dolor sit amet, <a class="usa-link" href="#">consectetur adipiscing</a> elit, sed do eiusmod.</p>
  </div>
</div>
```

## Alert Variants

```html
<!-- Warning Alert -->
<div class="usa-alert usa-alert--warning">
  <div class="usa-alert__body">
    <h4 class="usa-alert__heading">Warning message</h4>
    <p class="usa-alert__text">This is a warning alert message.</p>
  </div>
</div>

<!-- Success Alert -->
<div class="usa-alert usa-alert--success">
  <div class="usa-alert__body">
    <h4 class="usa-alert__heading">Success message</h4>
    <p class="usa-alert__text">This is a success alert message.</p>
  </div>
</div>

<!-- Error Alert -->
<div class="usa-alert usa-alert--error">
  <div class="usa-alert__body">
    <h4 class="usa-alert__heading">Error message</h4>
    <p class="usa-alert__text">This is an error alert message.</p>
  </div>
</div>

<!-- Emergency Alert -->
<div class="usa-alert usa-alert--emergency">
  <div class="usa-alert__body">
    <h4 class="usa-alert__heading">Emergency message</h4>
    <p class="usa-alert__text">This is an emergency alert message.</p>
  </div>
</div>
```

### Context

Alerts are a core USWDS component integrated into the Maryland Design System. They compose with text elements like headings and paragraphs, and support linked content via the `usa-link` class. Alerts work independently or can be combined with other notification patterns to create comprehensive messaging systems.

---

## Automatic List

*Components*

Automatic List displays a grid of linked cards that guide users to different sections or resources. Each card is fully clickable and uses the Linked variant of the Maryland Cards component. It supports multiple content types including Contacts, Documents, Locations, and News.

### Key Information

## Variants
- Default layout with card grid
- With Sidebar variant
- Section menu variant

## Supported Content Types
- Contacts
- Documents
- Locations
- News

## CSS Class Names
- `maryland-automatic-list` — Main wrapper class
- `maryland-card-group__header` — Header section container
- `maryland-card-group__header-content` — Header content wrapper
- `maryland-card-group__title` — Title heading (h2)
- `maryland-card-group__description` — Description text
- `maryland-card-group__more-link` — More link container

## Required Attributes
- `aria-labelledby` on the section element linking to the title ID
- `id` on the title heading for accessibility reference

## Important Facts
- Uses linked Maryland Cards as the base component for each card item
- Supports images and links (placeholder URLs used in examples)
- Includes optional description text below the title
- Includes optional "See more" link for accessing additional items
- Each card is fully clickable

### Implementation

```html
<section class="maryland-automatic-list" aria-labelledby="id-0yoyxpp2gau">
  <div class="maryland-card-group__header">
    <div class="maryland-card-group__header-content">
      <h2 class="maryland-card-group__title" id="id-0yoyxpp2gau">
        Featured News
      </h2>
      <p class="maryland-card-group__description">
        Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt
      </p>
    </div>
    <div class="maryland-card-group__more-link">
      <!-- More link content -->
    </div>
  </div>
  <!-- Card grid items follow -->
</section>
```

## Default Story Structure
The component wraps a section with the `maryland-automatic-list` class and includes:
- A header section with title and optional description
- A more-link container for "See more" navigation
- Grid of linked card items below (not shown in excerpt but referenced in documentation)

### Context

The Automatic List component is a template-level component that composes Maryland Cards in a grid layout with header information. It's used to present collections of related content items (news, contacts, documents, locations) in an organized, scannable format and integrates with the card group styling system.

---

## Banner

*Components*

The Banner component identifies official websites of government organizations in the United States and helps visitors understand whether a website is official and secure. It should be used to identify your site as an official site of the State of Maryland and assure visitors they're connected to a legitimate government domain. The banner should only be used on government domains (.gov) and not on commercial sites (.com, .org, etc.).

### Key Information

## Class Names and Structure
- `usa-banner`: Main container for the banner component
- `usa-banner__header`: Header section of the banner
- `usa-banner__inner`: Inner wrapper for header content
- `usa-banner__header-text`: Text describing the official website
- `usa-banner__button`: Toggle button to reveal additional information
- `usa-accordion`: Accordion wrapper for expandable content

## ARIA Attributes
- `aria-label="Official website of the State of Maryland"`: Identifies the banner purpose
- `aria-controls`: Links the button to the expandable content (e.g., `aria-controls="gov-banner-default"`)
- `aria-expanded`: Indicates collapsed/expanded state (starts as `false`)
- `aria-hidden="true"`: Applied to decorative SVG icons
- `role="img"`: Applied to SVG elements when they convey meaning

## Customization Options
The banner supports three boolean toggles:
- **Include flag**: Display the Maryland state flag (boolean, default: false)
- **Include link to maryland.gov**: Display a link to Maryland.gov (boolean, default: false)
- **Include translation widget**: Display Google Translate integration (boolean, default: false)

## Button Properties
- `type="button"`: Standard button type
- The toggle button uses an SVG icon to indicate expand/collapse functionality
- Button content reads "Here's how you know" followed by an icon

## Important Notes
- The banner should be positioned at the top of the page, before main content
- The translate link href should be formatted as: `https://translate.google.com/translate?u=LOCATION/` where LOCATION is the current page URL
- The banner uses USWDS (U.S. Web Design System) classes and patterns

### Implementation

```html
<section class="usa-banner" aria-label="Official website of the State of Maryland">
  <div class="usa-accordion">
    <div class="usa-banner__header">
      <div class="usa-banner__inner">
        <p class="usa-banner__header-text">
          An official website of the State of Maryland.
        </p>
        <button type="button" class="usa-banner__button" aria-controls="gov-banner-default" aria-expanded="false">
          Here's how you know 
          <svg role="img" aria-hidden="true" aria-label="Toggle button" xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="currentColor">
            <path d="M576-253.85 349.85-480 576-706.15l42.3 42.3L464.62-480l153.68 153.68L576-253.85Z"/>
          </svg>
        </button>
      </div>
    </div>
  </div>
</section>
```

## Variant: With Maryland.gov Link
When "Include link to maryland.gov" toggle is enabled, a link to Maryland.gov is displayed within the banner inner section.

## Variant: With Translation Widget
When "Include translation widget" toggle is enabled, a translation link appears directing users to Google Translate with the current page URL as the translation parameter.

## Variant: With Flag
When "Include flag" toggle is enabled, the Maryland state flag icon is displayed in the banner.

### Context

The Banner is a USWDS-based component that integrates with the MDWDS system to provide consistent government website branding. It composes with the accordion component (usa-accordion) to create an expandable details section and uses standard semantic HTML (section, button) with ARIA attributes for accessibility, following USWDS patterns for official government site identification.

---

## Breadcrumb

*Components*

The MDWDS Breadcrumb component helps users navigate back to previous pages by displaying a hierarchical trail of links. It's based on USWDS Breadcrumb with Maryland-specific styling, supporting both light and dark color variants. Use it to show the current page location within the site hierarchy and enable quick navigation to parent pages.

### Key Information

## Variants
- **Light**: White background with dark gray text (default)
- **Dark**: Blue background (blue-60v) with white text (used in Hero component)

## Key Options
- **pages** (required): Array of breadcrumb pages. Can be strings or objects with `{label, href}` properties. The last item is automatically marked as the current page (not linked).
- **variant**: Breadcrumb color variant (`light` or `dark`)
- **wrapping**: Boolean to allow breadcrumb text to wrap
- **rdfa**: Boolean to enable RDFa metadata for SEO

## Class Names
- `maryland-breadcrumb__wrapper`: Outer wrapper container
- `maryland-breadcrumb__wrapper--light`: Light variant modifier for wrapper
- `maryland-breadcrumb`: Main breadcrumb nav element
- `maryland-breadcrumb--light`: Light variant modifier for breadcrumb
- `maryland-breadcrumb--dark`: Dark variant modifier for breadcrumb
- `maryland-breadcrumb__list`: Ordered list container
- `maryland-breadcrumb__list-item`: Individual breadcrumb item
- `maryland-breadcrumb__link`: Breadcrumb link element
- `usa-breadcrumb*`: USWDS base classes also present

## Important Features
- Accessible with ARIA attributes (`aria-label="Breadcrumbs"`)
- Current page is rendered as plain text, not linked
- Supports wrapping and RDFa metadata for SEO
- Automatically handles the last item in the array as current page

### Implementation

```html
<!-- Light Variant (Default) -->
<div class="maryland-breadcrumb__wrapper maryland-breadcrumb__wrapper--light">
  <nav aria-label="Breadcrumbs" class="usa-breadcrumb maryland-breadcrumb maryland-breadcrumb--light">
    <ol class="usa-breadcrumb__list maryland-breadcrumb__list">
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <a class="usa-breadcrumb__link maryland-breadcrumb__link" href="/">
          <span>Home</span>
        </a>
      </li>
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <a class="usa-breadcrumb__link maryland-breadcrumb__link" href="/level-1">
          <span>Link Level 1</span>
        </a>
      </li>
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <a class="usa-breadcrumb__link maryland-breadcrumb__link" href="/level-2">
          <span>Link Level 2</span>
        </a>
      </li>
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <a class="usa-breadcrumb__link maryland-breadcrumb__link" href="/level-3">
          <span>Link Level 3</span>
        </a>
      </li>
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <a class="usa-breadcrumb__link maryland-breadcrumb__link" href="/level-4">
          <span>Link Level 4</span>
        </a>
      </li>
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <span>Current Page</span>
      </li>
    </ol>
  </nav>
</div>

<!-- Dark Variant -->
<div class="maryland-breadcrumb__wrapper maryland-breadcrumb__wrapper--dark">
  <nav aria-label="Breadcrumbs" class="usa-breadcrumb maryland-breadcrumb maryland-breadcrumb--dark">
    <ol class="usa-breadcrumb__list maryland-breadcrumb__list">
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <a class="usa-breadcrumb__link maryland-breadcrumb__link" href="/">
          <span>Home</span>
        </a>
      </li>
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <a class="usa-breadcrumb__link maryland-breadcrumb__link" href="/level-1">
          <span>Link Level 1</span>
        </a>
      </li>
      <li class="usa-breadcrumb__list-item maryland-breadcrumb__list-item">
        <span>Current Page</span>
      </li>
    </ol>
  </nav>
</div>
```

## Required ARIA Attributes
- `aria-label="Breadcrumbs"` on the `<nav>` element for accessibility

## Component Composition
- **Wrapper**: `maryland-breadcrumb__wrapper` with variant modifier
- **Nav**: `maryland-breadcrumb` (combines USWDS `usa-breadcrumb` class) with variant modifier
- **List**: Ordered list (`<ol>`) with `maryland-breadcrumb__list` class
- **Items**: List items with `maryland-breadcrumb__list-item` class containing either links or text
- **Links**: Anchor elements with `maryland-breadcrumb__link` class; last item is plain text (not linked)

### Context

The Breadcrumb component integrates with the MDWDS system as a navigation aid, extending USWDS Breadcrumb with Maryland-specific styling and color variants. It commonly appears in layouts alongside other navigation components and pairs naturally with the Hero component when using the dark variant for cohesive visual hierarchy.

---

## Breadcrumbs

*Components*

Breadcrumbs help users navigate back to previous pages or higher levels in the site hierarchy. They improve orientation, accessibility, and SEO with optional RDFa metadata support. Use breadcrumbs to show hierarchical page structure and provide quick navigation paths to parent pages.

### Key Information

## Key Class Names
- `usa-breadcrumb`: Main container wrapper
- `usa-breadcrumb__list`: Ordered list of breadcrumb items
- `usa-breadcrumb__list-item`: Individual breadcrumb item (list item)
- `usa-breadcrumb__link`: Breadcrumb link element
- `usa-current`: Modifier class for the current/active page item

## Variants & Options
- **pages**: Array of breadcrumb page labels (including current page). Example: `["Home", "Federal Contracting", "Contracting assistance programs", "Small Business"]`
- **wrapping**: Boolean to allow breadcrumb text to wrap (default: false)
- **rdfa**: Boolean to enable RDFa metadata for SEO enhancements (default: false)

## Required Attributes
- `aria-label="Breadcrumbs"` on the `<nav>` element for accessibility
- `aria-current` attribute on the current page list item (typically the last item)

## HTML Structure Notes
- Uses semantic `<nav>` with proper ARIA labeling
- List items wrapped in `<ol>` for ordered list semantics
- Links use `#` as placeholder URLs (should be replaced with real URLs in implementation)
- Current page indicator uses `usa-current` class modifier


### Implementation

```html
<nav aria-label="Breadcrumbs" class="usa-breadcrumb">
  <ol class="usa-breadcrumb__list">
    <li class="usa-breadcrumb__list-item">
      <a href="#" class="usa-breadcrumb__link">
        Home
      </a>
    </li>
    
    <li class="usa-breadcrumb__list-item">
      <a href="#" class="usa-breadcrumb__link">
        Federal Contracting
      </a>
    </li>
    
    <li class="usa-breadcrumb__list-item">
      <a href="#" class="usa-breadcrumb__link">
        Contracting assistance programs
      </a>
    </li>
    
    <li class="usa-breadcrumb__list-item usa-current" aria-current="page">
      <a href="#" class="usa-breadcrumb__link">
        Small Business
      </a>
    </li>
  </ol>
</nav>
```

## Variant: With Wrapping Enabled
Add the `wrapping` modifier when breadcrumb items need to wrap on smaller screens:

```html
<nav aria-label="Breadcrumbs" class="usa-breadcrumb usa-breadcrumb--wrapping">
  <ol class="usa-breadcrumb__list">
    <!-- list items same as above -->
  </ol>
</nav>
```

## Variant: With RDFa Metadata
Enable RDFa schema markup for SEO by adding data attributes:

```html
<nav aria-label="Breadcrumbs" class="usa-breadcrumb" vocab="https://schema.org/" typeof="BreadcrumbList">
  <ol class="usa-breadcrumb__list">
    <li class="usa-breadcrumb__list-item" property="itemListElement" typeof="ListItem">
      <a href="#" class="usa-breadcrumb__link" property="item" typeof="WebPage">
        <span property="name">Home</span>
      </a>
      <meta property="position" content="1">
    </li>
    
    <li class="usa-breadcrumb__list-item usa-current" property="itemListElement" typeof="ListItem" aria-current="page">
      <a href="#" class="usa-breadcrumb__link" property="item" typeof="WebPage">
        <span property="name">Current Page</span>
      </a>
      <meta property="position" content="2">
    </li>
  </ol>
</nav>
```


### Context

Breadcrumbs are a USWDS component integrated into MDWDS that enhance site navigation and user orientation. They typically appear near the top of content pages and work in concert with main navigation to provide multiple pathways through the site hierarchy, improving both UX and SEO through schema markup support.

---

## Button Group

*Components*

A button group displays 1-3 related action buttons with an optional title. Each button can be styled as Primary or Secondary, and external links display an external link icon. Titles can be visually hidden while remaining accessible to screen readers.

### Key Information

## Variants and Options

- **Primary Button**: Default button style using `.usa-button` class
- **Secondary Button**: Alternative button style (indicated in the visible text)
- **Up to 3 buttons**: Component is designed for 1-3 related action buttons
- **Title Display**: Title can be visually shown or hidden (still accessible to screen readers) via the `hide title` boolean property
- **External Link Support**: External links display an external link icon
- **Title Character Limit**: 75 character maximum for button group title

## CSS Classes

- `.maryland-button-group`: Main container wrapper
- `.maryland-button-group__title`: Title element (h2)
- `.maryland-button-group__list`: Button list container (uses `.usa-button-group`)
- `.maryland-button-group__item`: Individual button list item (also uses `.usa-button-group__item`)
- `.maryland-button-group__button`: Individual button/link element (also uses `.usa-button`)
- `.usa-button-group`: USWDS button group list wrapper
- `.usa-button-group__item`: USWDS button item
- `.usa-button`: USWDS button base class

## Required Attributes

- Title element should have an `id` attribute for accessible labeling
- List element should have `aria-labelledby` attribute pointing to the title's id
- Buttons can use `href` attribute for links

## Properties

- **Title**: String for button group title (75 character limit)
- **Hide title**: Boolean to visually hide title (default: false)
- **Buttons**: Array of button objects with text, url, and style properties

### Implementation

```html
<div class="maryland-button-group">
  <h2 id="id-f97jkhskbe" class="maryland-button-group__title">
    Button group title goes here (can be hidden)
  </h2>
  <ul class="usa-button-group maryland-button-group__list" aria-labelledby="id-f97jkhskbe">
    <li class="usa-button-group__item maryland-button-group__item">
      <a href="#!" class="usa-button maryland-button-group__button">
        Primary button
      </a>
    </li>
    <li class="usa-button-group__item maryland-button-group__item">
      <a href="#!" class="usa-button maryland-button-group__button">
        Secondary button
      </a>
    </li>
    <li class="usa-button-group__item maryland-button-group__item">
      <a href="#!" class="usa-button maryland-button-group__button">
        3rd Button
      </a>
    </li>
  </ul>
</div>
```

**Hidden Title Variant** (title still accessible to screen readers):

```html
<div class="maryland-button-group">
  <h2 id="id-f97jkhskbe" class="maryland-button-group__title" style="display: none;">
    Button group title goes here (can be hidden)
  </h2>
  <ul class="usa-button-group maryland-button-group__list" aria-labelledby="id-f97jkhskbe">
    <!-- buttons same as above -->
  </ul>
</div>
```

### Context

The Button Group component is built on top of USWDS button group patterns (.usa-button-group) and extends them with Maryland Design System styling through maryland-prefixed classes. It composes with individual buttons (.usa-button) and integrates accessible labeling patterns through ARIA attributes and semantic HTML structure.

---

## Button Group

*Components*

The Button Group component presents a set of related buttons as a unified element. It supports default (spaced) or segmented (cohesive row) layouts, with customizable variants, disabled states, and optional Google Analytics tracking. Use it when you need to group related actions with a unified visual presentation.

### Key Information

## Variants

- **Default**: Buttons displayed with spacing between them; stack vertically on mobile devices.
- **Segmented**: Buttons displayed as a unified row element, ideal for view toggles or mutually exclusive options.

## CSS Classes

- `usa-button-group`: Main container class for the button group
- `usa-button-group__item`: Wrapper class for each button in the group
- `usa-button`: Standard button class (used for buttons within the group)
- `usa-button--outline`: Outline variant modifier for secondary-style buttons
- `usa-button--secondary`: Secondary button variant
- `usa-button--accent-cool`: Cool accent button variant
- `usa-button--accent-warm`: Warm accent button variant
- `usa-button--base`: Base button variant

## Required Attributes

- `aria-label`: Required ARIA label for the button group providing context to screen readers
- `id`: Unique identifier for the button group element

## Key Configuration Options

- **variant**: Choose between "default" (separated buttons) or "segmented" (cohesive row)
- **buttons**: Array of button configurations with `label`, `variant`, and `disabled` properties
- **disabled**: Boolean to disable all buttons in the group
- **enableAnalytics**: Boolean to enable Google Analytics tracking
- **gaCategory**: GA event category string
- **gaAction**: GA event action string
- **gaLabel**: GA event label string

## Important Facts

- Buttons are wrapped in `<li>` elements with the `usa-button-group__item` class
- The button group uses an unordered list (`<ul>`) as the container
- Each button is a `<button>` element with `type="button"`
- Button variants control visual hierarchy and styling
- Keyboard accessibility and ARIA labels are supported and recommended

### Implementation

## Default Button Group

```html
<ul class="usa-button-group" id="button-group-id-h3pn5aaf6q" aria-label="Navigation buttons">
  <li class="usa-button-group__item">
    <button type="button" class="usa-button usa-button--outline">
      Back
    </button>
  </li>
  <li class="usa-button-group__item">
    <button type="button" class="usa-button">
      Continue
    </button>
  </li>
</ul>
```

## Segmented Button Group (Mutually Exclusive Options)

```html
<ul class="usa-button-group usa-button-group--segmented" id="button-group-id-segmented" aria-label="View options">
  <li class="usa-button-group__item">
    <button type="button" class="usa-button usa-button--outline">
      Map
    </button>
  </li>
  <li class="usa-button-group__item">
    <button type="button" class="usa-button usa-button--outline">
      Hybrid
    </button>
  </li>
  <li class="usa-button-group__item">
    <button type="button" class="usa-button">
      Satellite
    </button>
  </li>
</ul>
```

## Multiple Actions with Different Variants

```html
<ul class="usa-button-group" id="button-group-id-actions" aria-label="Form actions">
  <li class="usa-button-group__item">
    <button type="button" class="usa-button usa-button--secondary">
      Cancel
    </button>
  </li>
  <li class="usa-button-group__item">
    <button type="button" class="usa-button usa-button--outline">
      Save Draft
    </button>
  </li>
  <li class="usa-button-group__item">
    <button type="button" class="usa-button">
      Publish
    </button>
  </li>
</ul>
```

## Button Group with Disabled State

```html
<ul class="usa-button-group" id="button-group-id-disabled" aria-label="Navigation buttons" disabled>
  <li class="usa-button-group__item">
    <button type="button" class="usa-button usa-button--outline" disabled>
      Back
    </button>
  </li>
  <li class="usa-button-group__item">
    <button type="button" class="usa-button" disabled>
      Continue
    </button>
  </li>
</ul>
```

## Button Group with Google Analytics Attributes

```html
<ul class="usa-button-group" id="button-group-id-analytics" aria-label="Navigation buttons" data-ga-category="engagement" data-ga-action="button-group-click" data-ga-label="navigation">
  <li class="usa-button-group__item">
    <button type="button" class="usa-button usa-button--outline" data-ga-category="engagement" data-ga-action="back-click" data-ga-label="navigation">
      Back
    </button>
  </li>
  <li class="usa-button-group__item">
    <button type="button" class="usa-button" data-ga-category="engagement" data-ga-action="continue-click" data-ga-label="navigation">
      Continue
    </button>
  </li>
</ul>
```

### Context

The Button Group component is built on USWDS standards and is part of the MDWDS component library. It composes with the Button component and follows the same variant pattern system (default, secondary, accent-cool, accent-warm, base, outline), making it consistent with other interactive elements in the design system.

---

## Buttons

*Components*

The USWDS Button component provides multiple style variants to support various UI use cases, including primary actions, secondary options, and accent styles. It allows customization of button style, label, type, and state, with optional Google Analytics tracking and accessibility attributes. Use buttons to trigger actions, submit forms, or navigate within your application.

### Key Information

## Variants
- **Primary** (default): Standard primary action button
- **Secondary**: Secondary action variant
- **Accent Cool**: Cool accent style variant
- **Accent Warm**: Warm accent style variant
- **Base**: Base button style
- **Outline**: Outline button variant

## Sizes
- **default**: Standard button size
- **big**: Larger button size

## Properties
- **variant**: Button style variant (string) — options: default, secondary, accent-cool, accent-warm, base, outline
- **size**: Button size (string) — options: default, big
- **label**: Text displayed on the button (string)
- **type**: Button type attribute (string) — options: button, submit, reset
- **disabled**: Boolean to disable the button
- **enableAnalytics**: Enable or disable GA tracking attributes (boolean)
- **gaCategory**: Google Analytics event category (string)
- **gaAction**: Google Analytics event action (string)
- **gaLabel**: Google Analytics event label (string)

## CSS Classes
- `usa-button`: Base button class

## Accessibility
ARIA attributes and screen reader support are configurable through the component's accessibility properties.

### Implementation

```html
<!-- Primary Button (default variant) -->
<button type="button" class="usa-button">
  Primary Button
</button>

<!-- Secondary Button -->
<button type="button" class="usa-button usa-button--secondary">
  Secondary Button
</button>

<!-- Accent Cool Button -->
<button type="button" class="usa-button usa-button--accent-cool">
  Accent Cool Button
</button>

<!-- Accent Warm Button -->
<button type="button" class="usa-button usa-button--accent-warm">
  Accent Warm Button
</button>

<!-- Base Button -->
<button type="button" class="usa-button usa-button--base">
  Base Button
</button>

<!-- Outline Button -->
<button type="button" class="usa-button usa-button--outline">
  Outline Button
</button>

<!-- Big/Large Button -->
<button type="button" class="usa-button usa-button--big">
  Big Button
</button>

<!-- Disabled Button -->
<button type="button" class="usa-button" disabled>
  Disabled Button
</button>

<!-- Button with Submit Type -->
<button type="submit" class="usa-button">
  Submit
</button>

<!-- Button with Reset Type -->
<button type="reset" class="usa-button">
  Reset
</button>

<!-- Button with Google Analytics Tracking -->
<button type="button" class="usa-button" data-ga-category="engagement" data-ga-action="click" data-ga-label="primary-action">
  Tracked Button
</button>
```

### Context

The Button component is a core UI element in the MDWDS system based on USWDS standards. It composes with forms, navigation patterns, and action workflows throughout the design system, providing consistent styling and interaction patterns across Maryland digital services.

---

## Callout

*Components*

The Callout component highlights important information with a description and optional title and/or image. It's used to draw attention to key messages, government information, or announcements in a visually distinct container. Use this when you need to emphasize critical information that stands out from regular body content.

### Key Information

## Key Classes and Structure
- **Root container**: `maryland-callout` — semantic `<section>` element
- **Inner wrapper**: `maryland-callout__container` — holds all callout content
- **Image area**: `maryland-callout__image` — optional image container with `<img>` element
- **Content wrapper**: `maryland-callout__content` — groups title and description
- **Title**: `maryland-callout__title` — optional `<h2>` element with auto-generated ID
- **Description**: `maryland-callout__description` — required text content area

## Properties (Configurable via Attributes)
- **Title** (optional): Display text for the callout heading
- **Visually hide title** (boolean): Hides title from display while keeping it available to screen readers
- **Description** (required): The main descriptive text content
- **Show image** (boolean): Toggle image display on/off
- **Image** (optional): URL for the callout image
- **Image alt text** (optional): Alt text for accessibility; leave empty for decorative images

## ARIA Requirements
- `aria-labelledby` attribute on `<section>` element that references the title's ID for accessible labeling
- Auto-generated unique IDs on title elements for proper association

## Required Attributes
- `<section>` must include `aria-labelledby` attribute pointing to the title's ID
- Title `<h2>` must have an `id` attribute for the `aria-labelledby` reference
- Image `<img>` must have an `alt` attribute (can be empty for decorative images)

### Implementation

```html
<!-- Basic Callout with Title, Image, and Description -->
<section class=" maryland-callout " aria-labelledby="id-oti3dembu68">
  <div class="maryland-callout__container">
    
    <div class="maryland-callout__image">
      <img src="https://placehold.co/400x400/1976d2/white/webp" alt="">
    </div>
    
    <div class="maryland-callout__content">
      <h2 id="id-oti3dembu68" class=" maryland-callout__title ">
        Your government is committed to serving Marylanders
      </h2>
      
      <div class="maryland-callout__description">
        The goal of Maryland's state government is to serve the public and represent Marylanders' interests.
      </div>
    </div>
  </div>
</section>
```

**Variant: Title with Alt Text on Image**
```html
<section class=" maryland-callout " aria-labelledby="id-example-title">
  <div class="maryland-callout__container">
    
    <div class="maryland-callout__image">
      <img src="image-url.webp" alt="Descriptive alt text for the image">
    </div>
    
    <div class="maryland-callout__content">
      <h2 id="id-example-title" class=" maryland-callout__title ">
        Title Text
      </h2>
      
      <div class="maryland-callout__description">
        Description text goes here.
      </div>
    </div>
  </div>
</section>
```

**Variant: Without Image**
```html
<section class=" maryland-callout " aria-labelledby="id-no-image-example">
  <div class="maryland-callout__container">
    
    <div class="maryland-callout__content">
      <h2 id="id-no-image-example" class=" maryland-callout__title ">
        Important Title
      </h2>
      
      <div class="maryland-callout__description">
        Description content only, no image display.
      </div>
    </div>
  </div>
</section>
```

### Context

The Callout component is a foundational MDWDS component used throughout the design system to highlight critical information, government announcements, and important notices. It combines with typography and image utilities to create flexible, accessible information containers that adapt across the system's various page templates and layouts.

---

## Cards

*Components*

Maryland Design System cards are modular containers that group related information in a visually distinct format. They support multiple variants (simple, media, full, flag, linked) and can display images, headings, subheadings, text, links, and link buttons. Cards are ideal for highlighting articles, events, news, or services in a grid layout.

### Key Information

## Variants
- **simple**: Basic card layout with title and body text
- **media**: Card with image support
- **full**: Full-featured card with all content options
- **flag**: Card with flag-style layout
- **linked**: Card formatted as an interactive link

## CSS Classes
- `.maryland-card`: Base card component class
- `.maryland-card--simple`: Modifier for simple variant
- `.maryland-card__container`: Main card container
- `.maryland-card__header`: Card heading section
- `.maryland-card__heading`: Card title (h3 element)
- `.maryland-card__body`: Main content area
- `.maryland-card__footer`: Footer section
- `.maryland-card__footer--left`: Left-aligned footer modifier
- `.maryland-card-group`: Wrapper list for card collections
- `.tablet-lg:grid-col-6`: Responsive grid class for tablet large screens (6 columns)
- `.desktop-lg:grid-col-4`: Responsive grid class for desktop large screens (4 columns)

## Content Options
- **title** (string): Card heading text
- **body** (string): Main content text of the card
- **variant** (string): Choose card style - options: simple, media, full, flag, linked

## Structure
Cards are displayed within a `.maryland-card-group` (ul element) with individual cards as `.maryland-card` list items.

### Implementation

```html
<ul class="maryland-card-group">
  <li class="maryland-card maryland-card--simple tablet-lg:grid-col-6 desktop-lg:grid-col-4">
    <div class="maryland-card__container">
      <div class="maryland-card__header">
        <h3 class="maryland-card__heading">Maryland Card Title</h3>
      </div>
      
      <div class="maryland-card__body">
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
      </div>

      <div class="maryland-card__footer maryland-card__footer--left">
        <!-- footer content -->
      </div>
    </div>
  </li>
</ul>
```

## Responsive Grid Modifiers
The card list items use responsive utility classes to control column span:
- `.tablet-lg:grid-col-6`: 6-column layout on tablet large breakpoint
- `.desktop-lg:grid-col-4`: 4-column layout on desktop large breakpoint

### Context

Cards are a foundational container component in the Maryland Design System used to organize and display grouped content. They compose with grid utilities and responsive breakpoint classes to create flexible layouts, and integrate with the system's typography and link patterns.

---

## Cards

*Components*

Cards are modular containers that group related information in a visually distinct format. They are ideal for highlighting articles, events, services, or tasks, and support images, headings, links, buttons, and metadata. Cards help organize content in a scannable, self-contained manner for better user engagement.

### Key Information

## Variants

- **Simple**: Basic card with heading, body text, and optional button
- **Media**: Card with image support (media can be placed first or after header)
- **Flag**: Alternative card style variant

## CSS Class Names

- `usa-card-group`: Container for multiple cards (applied to `<ul>`)
- `usa-card`: Individual card item wrapper (applied to `<li>`)
- `usa-card__container`: Inner wrapper for card content
- `usa-card__header`: Card header section
- `usa-card__heading`: Card title/heading element
- `usa-card__body`: Main content section
- `usa-card__footer`: Footer section (typically contains buttons/links)

## Grid Modifiers

- `tablet-lg:grid-col-6`: 50% width on tablet-lg breakpoint (2 columns)
- `desktop-lg:grid-col-4`: 33.33% width on desktop-lg breakpoint (3 columns)

## Media Placement Options

- **Media First**: Image appears before heading
- **Header First**: Heading appears before image

## Media Style Options

- **Default**: Standard image sizing
- **Inset**: Image inset within card
- **Exdent**: Image extends beyond card bounds

## Component Properties

- `variant`: Card style (simple, media, flag)
- `title`: Card heading text
- `body`: Main content text
- `buttonText`: CTA button/link label
- `buttonUrl`: Button destination URL
- `cardCount`: Number of cards to display
- `imageUrl`: Image URL for media cards
- `imageAlt`: Alt text for images
- `mediaPlacement`: Order of card contents (Media First or Header First)
- `mediaStyle`: Media sizing (Default, Inset, Exdent)
- `enableAnalytics`: Enable GA tracking
- `gaCategory`: GA event category
- `gaAction`: GA event action
- `gaLabel`: GA event label

### Implementation

```html
<!-- Card Group Container -->
<ul class="usa-card-group">
  <!-- Individual Card Item -->
  <li class="usa-card tablet-lg:grid-col-6 desktop-lg:grid-col-4">
    <div class="usa-card__container">
      
      <!-- Card Header Section -->
      <div class="usa-card__header">
        <h4 class="usa-card__heading">Card Title</h4>
      </div>

      <!-- Card Body Section -->
      <div class="usa-card__body">
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
      </div>

      <!-- Card Footer Section (typically with button/link) -->
      <div class="usa-card__footer">
        <a class="usa-button" href="#">Learn More</a>
      </div>

    </div>
  </li>

  <!-- Additional cards follow same structure -->
  <li class="usa-card tablet-lg:grid-col-6 desktop-lg:grid-col-4">
    <div class="usa-card__container">
      <div class="usa-card__header">
        <h4 class="usa-card__heading">Card Title</h4>
      </div>
      <div class="usa-card__body">
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
      </div>
      <div class="usa-card__footer">
        <a class="usa-button" href="#">Learn More</a>
      </div>
    </div>
  </li>
</ul>
```

### Context

Cards are a core MDWDS component based on USWDS card patterns, providing a flexible, reusable container for content organization. They compose well with grid systems (using responsive grid column classes) and button components, making them essential for service listings, event highlights, and content discovery in Maryland digital properties.

---

## Character Count

*Components*

The Character Count component provides real-time character counting feedback for text inputs and textareas. It displays the remaining or used character count with visual feedback and automatically shows error states when limits are exceeded. Use it to help users stay within specified character limits for form fields.

### Key Information

## Variants
- **Input**: Uses `<input>` element for single-line character counting
- **Textarea**: Uses `<textarea>` element for multi-line character counting

## CSS Classes
- `usa-form`: Form wrapper class
- `usa-label`: Label element styling
- `usa-hint`: Hint text styling (displayed below label)
- `usa-character-count`: Main wrapper container for the component
- `usa-character-count__field`: Applied to the textarea or input element
- `usa-character-count__message`: Container for character count message text
- `usa-sr-only`: Screen reader only text (hides message visually but keeps it accessible)
- `usa-textarea`: Textarea field styling

## Required Attributes
- `data-maxlength`: Set on `.usa-character-count` container to define maximum character limit (number value)
- `id`: Unique identifier for the input/textarea element
- `aria-describedby`: Links the field to both the hint and message via their IDs
- `name`: Name attribute for form submission

## Configuration Options
- **label**: Label text for the input field
- **inputType**: Choose between "input" or "textarea"
- **maxLength**: Maximum character limit (numeric)
- **hint**: Optional hint text displayed below the label
- **defaultValue**: Default text value in the field
- **required**: Mark field as required (boolean)
- **enableAnalytics**: Enable Google Analytics tracking (boolean)
- **gaCategory**: GA event category (string)
- **gaAction**: GA event action (string)
- **gaLabel**: GA event label (string)

## Important Facts
- Requires USWDS JavaScript to be loaded for live counting functionality
- The message element uses `usa-sr-only` for screen reader announcement
- Character count message is dynamically updated as user types
- Works with both input validation and form submission

### Implementation

```html
<form class="usa-form usa-form--large">
  <label class="usa-label" for="character-count-id-lfeaaigyv5o">
    Message
  </label>
  <span class="usa-hint" id="hint-id-lfeaaigyv5o">Enter your message</span>
  <div class="usa-character-count" data-maxlength="200">
    <textarea 
      class="usa-textarea usa-character-count__field" 
      id="character-count-id-lfeaaigyv5o" 
      name="character-count-id-lfeaaigyv5o" 
      aria-describedby="hint-id-lfeaaigyv5o message-id-lfeaaigyv5o">
    </textarea>
    <span 
      class="usa-character-count__message usa-sr-only" 
      id="message-id-lfeaaigyv5o">
      200 characters allowed
    </span>
  </div>
</form>
```

## Variant: Input Element
```html
<form class="usa-form usa-form--large">
  <label class="usa-label" for="character-count-input">
    Short Description
  </label>
  <div class="usa-character-count" data-maxlength="50">
    <input 
      class="usa-input usa-character-count__field" 
      id="character-count-input" 
      name="character-count-input" 
      aria-describedby="message-count-input"
      type="text">
    <span 
      class="usa-character-count__message usa-sr-only" 
      id="message-count-input">
      50 characters allowed
    </span>
  </div>
</form>
```

## Variant: With Hint and Required Field
```html
<form class="usa-form usa-form--large">
  <label class="usa-label" for="character-count-required">
    Required Message
    <span class="usa-label__required">*</span>
  </label>
  <span class="usa-hint" id="hint-required">Provide detailed information (required)</span>
  <div class="usa-character-count" data-maxlength="200">
    <textarea 
      class="usa-textarea usa-character-count__field" 
      id="character-count-required" 
      name="character-count-required" 
      aria-describedby="hint-required message-required"
      required>
    </textarea>
    <span 
      class="usa-character-count__message usa-sr-only" 
      id="message-required">
      200 characters allowed
    </span>
  </div>
</form>
```

### Context

Character Count is a USWDS component that enhances form field accessibility and user experience by providing real-time feedback. It integrates with form fields (input/textarea) and works alongside label, hint, and ARIA attributes to ensure proper form structure and screen reader support within the MDWDS system.

---

## Checkboxes

*Components*

Checkboxes allow users to select one or more options from a list, making them ideal for forms where multiple selections are permitted. This component supports both default and tile styles with configurable checked and disabled states per option, plus optional Google Analytics tracking and ARIA accessibility attributes.

### Key Information

## Variants
- **default**: Standard checkbox style
- **tile**: Tile-based checkbox style

## CSS Classes
- `usa-fieldset`: Container for checkbox fieldset
- `usa-legend`: Legend text for screen readers and visual display
- `usa-checkbox`: Wrapper div for each checkbox option
- `usa-checkbox__input`: The actual checkbox input element
- `usa-checkbox__label`: Label associated with checkbox input

## Key Attributes & Options
- **variant**: Choose between "default" or "tile" styles (default: not specified)
- **legend**: Group legend text displayed to users and screen readers
- **fieldName**: Form field element name attribute (applies to all inputs in group)
- **options**: Array of checkbox option objects with structure:
  - `label` (required): Display text for the checkbox
  - `value` (required): Value attribute for the input
  - `description` (optional): Additional descriptive text
  - `checked` (optional): Boolean to set default checked state
  - `disabled` (optional): Boolean to disable the option
- **enableAnalytics**: Boolean to enable/disable Google Analytics tracking attributes
- **gaCategory**: GA event category string
- **gaAction**: GA event action string
- **gaLabel**: GA event label string

## Required Structure
- Checkboxes must be wrapped in a `<form>` element
- Use `<fieldset>` with `<legend>` for semantic grouping and accessibility
- Each checkbox requires a unique `id` attribute
- Each checkbox should have an associated `<label>` with matching `for` attribute

### Implementation

```html
<form class="usa-form">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">Select any historical figure</legend>

    <div class="usa-checkbox">
      <input 
        type="checkbox" 
        class="usa-checkbox__input" 
        id="id-w8ycf11mzgt" 
        name="historical-figures" 
        value="sojourner-truth" 
        checked="">
      <label class="usa-checkbox__label" for="id-w8ycf11mzgt">
        Sojourner Truth
      </label>
    </div>

    <div class="usa-checkbox">
      <input 
        type="checkbox" 
        class="usa-checkbox__input" 
        id="id-52gymqv0c4e" 
        name="historical-figures" 
        value="frederick-douglass">
      <label class="usa-checkbox__label" for="id-52gymqv0c4e">
        Frederick Douglass
      </label>
    </div>

    <div class="usa-checkbox">
      <input 
        type="checkbox" 
        class="usa-checkbox__input" 
        id="id-another-id" 
        name="historical-figures" 
        value="booker-t-washington" 
        disabled="">
      <label class="usa-checkbox__label" for="id-another-id">
        Disabled option
      </label>
    </div>
  </fieldset>
</form>
```

## Key Implementation Notes
- Each checkbox in a group shares the same `name` attribute but must have unique `id` values
- The `<label>` element's `for` attribute must match the checkbox `id` for proper accessibility
- Use `checked=""` attribute to set default checked state
- Use `disabled=""` attribute to disable an option
- The `usa-form` wrapper provides form styling context
- The `usa-fieldset` and `usa-legend` provide semantic structure and screen reader support

### Context

Checkboxes are a fundamental USWDS form component used in conjunction with fieldsets and legends to create accessible grouped form controls. They compose with the `usa-form` container and support optional Google Analytics tracking for user interaction monitoring across the MDWDS system.

---

## Collection

*Components*

The Collection component displays a compact list of multiple related items (such as articles, events, or news items) that link to original sources. It supports various display options including images, descriptions, metadata, dates, and tags to help users browse and discover related content efficiently.

### Key Information

## Variants
- **Default**: Standard collection display with headings, descriptions, and metadata
- **Media Thumbnail**: Includes optional images or icons for each item
- **Calendar Display**: Shows date information in calendar format
- **Headings Only**: Simplified variant displaying only item titles
- **Condensed**: Compact variant with reduced spacing

## Core CSS Classes
- `usa-collection`: Main container for the collection list
- `usa-collection__item`: Individual list item wrapper
- `usa-collection__body`: Container for item content
- `usa-collection__heading`: Item title heading (typically `<h4>`)
- `usa-collection__description`: Item description text
- `usa-link`: Link styling for item titles
- `usa-icon`: Icon element (e.g., external link launch icon)

## Key Features
- Display items with headings, descriptions, and metadata
- Optional images or icon support for each item
- Date information (standard or calendar format)
- Tag support for categorization
- Google Analytics tracking attributes support (optional)

## HTML Structure
- Collection is rendered as an unordered list (`<ul>`)
- Each item is a list item (`<li class="usa-collection__item">`)
- Items contain a body div with heading, description, and optional metadata
- Links use standard `usa-link` class styling

### Implementation

```html
<ul class="usa-collection" id="collection-id-example">
  <li class="usa-collection__item">
    <div class="usa-collection__body">
      <h4 class="usa-collection__heading">
        <a class="usa-link" href="https://example.com/item">
          Item Title
          <svg class="usa-icon" aria-hidden="true" focusable="false" role="img">
            <use xlink:href="/assets/img/sprite.svg#launch"></use>
          </svg>
        </a>
      </h4>
      <p class="usa-collection__description">
        Item description text goes here.
      </p>
    </div>
  </li>
</ul>
```

## Accessibility Requirements
- Use unique, descriptive headings (avoid generic "read more" links)
- Maintain logical heading level hierarchy
- Ensure images have descriptive alt text
- Include external link indicators (e.g., launch icon) when linking to outside sources

### Context

The Collection component is part of the USWDS component library and integrates with the Maryland Web Design System for displaying lists of related content items. It composes standard elements like headings, links, descriptions, and optional media, following USWDS patterns and accessibility guidelines for creating scannable, organized content displays.

---

## Combo Box

*Components*

The Combo Box is an enhanced select dropdown that combines a text input with a filterable option list, providing type-ahead functionality ideal for long lists of options. It solves the UX problem of scrolling through lengthy option lists by allowing users to quickly filter and find their choice. Use it when you need to present many selectable options while maintaining accessibility and keyboard navigation support.

### Key Information

## Variants & Features

- **Type-ahead filtering** — Real-time filtering as users type
- **Keyboard navigation** — Arrow keys, Enter, Escape support
- **Clear button** — Reset selection capability
- **Required field support** — For mandatory selections
- **Disabled state** — Disable the entire combo box
- **Default selected value** — Pre-populate with a selection
- **Google Analytics tracking** — Built-in analytics attributes
- **WCAG 2.1 AA compliant** — Full accessibility support

## CSS Classes

- `usa-combo-box` — Main wrapper container
- `usa-combo-box__select` — Hidden select element (requires `usa-sr-only`, `usa-select` classes)
- `usa-form` — Form container
- `usa-label` — Label element
- `usa-select` — Select styling
- `usa-sr-only` — Screen reader only visibility

## Required Attributes & Structure

- `<label class="usa-label">` with `for` attribute tied to select `id`
- `<div class="usa-combo-box">` wrapper with `data-enhanced="true"` attribute
- `<select>` element with class `usa-select usa-sr-only usa-combo-box__select`
- `aria-hidden="true"` on the select element
- `tabindex="-1"` on the select element
- `name` attribute for form submission
- Option elements with `value` and label text
- First option typically serves as placeholder ("Select a fruit")

## Configuration Properties

- **label** — Display label text for the combo box
- **id** — Identifier for the select element (required for label association)
- **name** — Name attribute for form submission
- **placeholder** — Placeholder text for the first option
- **options** — Array of option objects with structure: `{ label, value, selected?, disabled? }`

## JavaScript

The component automatically loads USWDS JavaScript for keyboard navigation and filtering functionality upon rendering.

### Implementation

```html
<form class="usa-form">
  <label class="usa-label" for="fruit" id="fruit-label">Select a fruit</label>
  <div class="usa-combo-box" data-enhanced="true">
    <select id="fruit" name="fruit" class="usa-select usa-sr-only usa-combo-box__select" aria-hidden="true" tabindex="-1">
      <option value="">Select a fruit</option>
      <option value="apple">Apple</option>
      <option value="apricot">Apricot</option>
      <option value="avocado">Avocado</option>
      <option value="banana">Banana</option>
      <option value="blackberry">Blackberry</option>
      <option value="blueberry">Blueberry</option>
      <option value="cantaloupe">Cantaloupe</option>
      <option value="cherry">Cherry</option>
      <option value="cranberry">Cranberry</option>
      <option value="date">Date</option>
      <option value="dragonfruit">Dragonfruit</option>
      <option value="elderberry">Elderberry</option>
      <option value="fig">Fig</option>
      <option value="grape">Grape</option>
      <option value="grapefruit">Grapefruit</option>
      <option value="guava">Guava</option>
      <option value="kiwifruit">Kiwifruit</option>
      <option value="lemon">Lemon</option>
      <option value="lime">Lime</option>
      <option value="mango">Mango</option>
      <option value="orange">Orange</option>
      <option value="papaya">Papaya</option>
      <option value="peach">Peach</option>
      <option value="pear">Pear</option>
      <option value="pineapple">Pineapple</option>
      <option value="plum">Plum</option>
      <option value="pomegranate">Pomegranate</option>
      <option value="raspberry">Raspberry</option>
      <option value="strawberry">Strawberry</option>
      <option value="tangerine">Tangerine</option>
      <option value="watermelon">Watermelon</option>
    </select>
  </div>
</form>
```

## Key Structure Notes

1. The select element is visually hidden using `usa-sr-only` class while remaining available to screen readers
2. The `data-enhanced="true"` attribute indicates USWDS JavaScript enhancement is active
3. The label's `for` attribute must match the select's `id` for proper accessibility
4. The first option typically acts as a placeholder prompt
5. USWDS JavaScript transforms this hidden select into an interactive combo box with filtering and keyboard navigation
6. All interactive elements (input, dropdown, filtering) are generated by the USWDS JavaScript library

### Context

The Combo Box is a USWDS component that integrates with MDWDS as an enhanced form control. It composes with the standard form layout (usa-form, usa-label) and leverages USWDS's JavaScript system for progressive enhancement. This component follows the same accessibility and styling patterns as other MDWDS form inputs.

---

## Data Visualizations

*Components*

The USWDS Data Visualizations component provides guidance and accessible patterns for implementing charts, graphs, and data visualizations in compliance with WCAG 2.1 AA. It addresses the critical need for equitable data presentation by ensuring visual information is never embedded in images alone and is always accessible to screen readers. Use this component when displaying charts, graphs, or other data-driven visualizations that must serve all users regardless of ability.

### Key Information

## Core CSS Classes

- `.usa-data-visualization` — Main container wrapper for the visualization component
- `.chart-title` — Semantic heading for the chart (typically `<h3>`)
- `.chart-description` — Narrative summary providing context and intent
- `.visualization-container` — Wrapper for the actual SVG/visual chart element

## Required HTML Attributes & ARIA

- `role="img"` — Applied to `.visualization-container` to indicate decorative chart content
- `aria-labelledby` — Links visualization to the chart title ID (e.g., `aria-labelledby="chart-title-id-..."`)
- `id` attributes — Required on `.chart-title` and `.chart-description` for proper labeling
- `aria-hidden="true"` — Applied to decorative SVG graphics to hide from screen readers

## Key Variants & Patterns

1. **Default** — Basic chart with title, description, and SVG visualization
2. **With Pattern Fills** — Uses pattern fills instead of solid colors for colorblind accessibility
3. **High Contrast** — Enhanced contrast ratio for visibility in varied lighting conditions
4. **With Data Table** — Includes `.usa-sr-only` data table as screen reader alternative
5. **Screen Reader Only** — Data table marked with `.usa-sr-only` for non-visual access
6. **Accessible Color Palette** — USWDS-compliant color scheme that meets WCAG AA standards
7. **Container Pattern** — Reusable container structure for consistent visualization layout
8. **With Analytics** — Optional Google Analytics tracking for chart interactions

## Core Principles

- **Simplicity** — Limit to 1-2 central themes; prefer common chart types (line, bar)
- **Lossless Representation** — Provide textual axis labels and data tables; minimize required interactions
- **Clarity of Intent** — State the intended message explicitly in text; include statistical trends
- **Equivalent Access** — Hide decorative graphics; provide screen-reader-only alternatives and narrative context

### Implementation

```html
<!-- Basic Data Visualization Container -->
<div class="usa-data-visualization">
  <!-- Chart Title (Semantic Heading) -->
  <h3 class="chart-title" id="chart-title-id-kksq0s9p81m">
    Maryland State Agency Budgets (FY 2025)
  </h3>

  <!-- Narrative Summary (Accessible Context) -->
  <p class="chart-description" id="chart-description-id-kksq0s9p81m">
    Transportation receives the largest budget allocation at $4.2B, followed by Education at $3.8B. Health spending increased 15% year-over-year.
  </p>

  <!-- Visualization Container (Decorative SVG, Hidden from Screen Readers) -->
  <div 
    class="visualization-container" 
    role="img" 
    id="chart-id-kksq0s9p81m" 
    aria-labelledby="chart-title-id-kksq0s9p81m"
  >
    <!-- SVG Chart Content Goes Here (marked aria-hidden if nested SVG) -->
    <svg aria-hidden="true">
      <!-- Chart elements -->
    </svg>
  </div>
</div>
```

### With Screen Reader Data Table Alternative

```html
<div class="usa-data-visualization">
  <h3 class="chart-title" id="chart-title-id-example">
    Budget Allocation Summary
  </h3>

  <p class="chart-description" id="chart-description-id-example">
    Key budget trends for FY 2025 across major state agencies.
  </p>

  <!-- Visual Chart -->
  <div 
    class="visualization-container" 
    role="img" 
    id="chart-id-example" 
    aria-labelledby="chart-title-id-example"
  >
    <svg aria-hidden="true">
      <!-- SVG chart -->
    </svg>
  </div>

  <!-- Screen Reader Only Data Table -->
  <table class="usa-sr-only">
    <caption>Maryland State Agency Budgets (FY 2025) - Data Table</caption>
    <thead>
      <tr>
        <th>Agency</th>
        <th>Budget Amount (Billions)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Transportation</td>
        <td>$4.2B</td>
      </tr>
      <tr>
        <td>Education</td>
        <td>$3.8B</td>
      </tr>
    </tbody>
  </table>
</div>
```

### With Pattern Fills (Colorblind Accessible)

```html
<div class="usa-data-visualization">
  <h3 class="chart-title" id="chart-title-id-patterns">
    Budget Distribution with Pattern Fills
  </h3>

  <p class="chart-description" id="chart-description-id-patterns">
    Uses distinct pattern fills in addition to colors for accessibility.
  </p>

  <div 
    class="visualization-container" 
    role="img" 
    id="chart-id-patterns" 
    aria-labelledby="chart-title-id-patterns"
  >
    <svg aria-hidden="true">
      <!-- SVG with pattern fills and defs -->
    </svg>
  </div>
</div>
```

### High Contrast Variant

```html
<div class="usa-data-visualization">
  <h3 class="chart-title" id="chart-title-id-hc">
    High Contrast Visualization
  </h3>

  <p class="chart-description" id="chart-description-id-hc">
    Enhanced contrast ratios meeting WCAG AAA standards.
  </p>

  <div 
    class="visualization-container" 
    role="img" 
    id="chart-id-hc" 
    aria-labelledby="chart-title-id-hc"
  >
    <svg aria-hidden="true">
      <!-- High-contrast SVG -->
    </svg>
  </div>
</div>
```

### Context

Data Visualizations is a guidance component within the MDWDS system that demonstrates best practices for accessible chart and graph implementation across Maryland digital services. It extends USWDS accessibility patterns by combining semantic HTML, ARIA attributes, narrative descriptions, and alternative data representations to ensure all users can access and understand data-driven content, regardless of ability.

---

## Date Picker

*Components*

The Date Picker is an accessible calendar popup widget for date selection powered by USWDS JavaScript. It provides users with an interactive calendar interface for selecting dates while supporting keyboard navigation, date range constraints, and required field validation. Use this component when you need a user-friendly way to collect date input in forms.

### Key Information

## Variants
- **Default**: Basic date picker with calendar popup widget
- **With Default Value**: Pre-filled default value (format: YYYY-MM-DD)
- **With Min Max Dates**: Constrained date selection with minimum and maximum dates
- **With Range Highlight**: Highlights date range from a specified date
- **Required**: Marks the date field as required
- **Disabled**: Disables the date picker input
- **With Analytics**: Includes Google Analytics tracking attributes

## CSS Classes
- `usa-form-group`: Container wrapper
- `usa-label`: Label element
- `usa-hint`: Hint text for date format
- `usa-date-picker`: Main date picker container
- `usa-date-picker--initialized`: Applied when date picker JavaScript is initialized
- `usa-input`: Input field styling
- `usa-date-picker__internal-input`: Hidden internal input for accessibility
- `usa-date-picker__external-input`: Visible user-facing input
- `usa-date-picker__wrapper`: Wraps the external input

## Key Attributes
- `data-min-date`: Minimum selectable date (format: YYYY-MM-DD)
- `aria-labelledby`: Associates input with label ID
- `aria-describedby`: Associates input with hint text ID
- `aria-hidden="true"`: Hides internal input from screen readers
- `tabindex="-1"`: Removes internal input from tab order

## Configuration Properties
- **label**: Label text for the date picker input (string)
- **hintText**: Optional hint text for date format (string)
- **name**: Input name attribute for form submission (string)
- **required**: Whether the date field is required (boolean)
- **disabled**: Disable the date picker input (boolean)
- **defaultValue**: Default date value (format: YYYY-MM-DD)
- **minDate**: Minimum selectable date (format: YYYY-MM-DD)
- **maxDate**: Maximum selectable date (format: YYYY-MM-DD)
- **rangeDate**: Highlight range from this date (format: YYYY-MM-DD)
- **enableAnalytics**: Enable or disable GA tracking (boolean)
- **gaCategory**: Google Analytics event category (string)
- **gaAction**: Google Analytics event action (string)
- **gaLabel**: Google Analytics event label (string)

## Important Facts
- Requires USWDS JavaScript to be loaded for functionality
- Calendar widget initializes automatically on page load
- Supports keyboard navigation: arrow keys, Page Up/Down, Home/End
- Follows WCAG 2.1 AA accessibility requirements
- Two-input pattern: internal hidden input + external visible input for accessibility

### Implementation

```html
<div class="usa-form-group">
  <label class="usa-label" id="date-picker-label-id-q3gi6d6crmn" for="date-picker-id-q3gi6d6crmn">
    Appointment date
  </label>
  <div class="usa-hint" id="date-picker-hint-id-q3gi6d6crmn">mm/dd/yyyy</div>
  
  <div class="usa-date-picker usa-date-picker--initialized" data-min-date="0000-01-01">
    <!-- Internal hidden input for accessibility -->
    <input 
      class="usa-input usa-date-picker__internal-input" 
      aria-labelledby="date-picker-label-id-q3gi6d6crmn" 
      aria-describedby="date-picker-hint-id-q3gi6d6crmn" 
      aria-hidden="true" 
      tabindex="-1" 
      style="display: none;">
    
    <!-- Wrapper for external input -->
    <div class="usa-date-picker__wrapper">
      <!-- External visible input for user interaction -->
      <input 
        class="usa-input usa-date-picker__external-input" 
        id="date-picker-id-q3gi6d6crmn"
        aria-labelledby="date-picker-label-id-q3gi6d6crmn" 
        aria-describedby="date-picker-hint-id-q3gi6d6crmn" 
        placeholder="mm/dd/yyyy"
        type="text">
    </div>
  </div>
</div>
```

## With Min/Max Dates Example
```html
<div class="usa-form-group">
  <label class="usa-label" id="date-picker-min-max-label" for="date-picker-min-max">
    Select Date
  </label>
  <div class="usa-hint" id="date-picker-min-max-hint">mm/dd/yyyy</div>
  
  <div class="usa-date-picker usa-date-picker--initialized" 
       data-min-date="2024-01-01" 
       data-max-date="2024-12-31">
    <input 
      class="usa-input usa-date-picker__internal-input" 
      aria-labelledby="date-picker-min-max-label" 
      aria-describedby="date-picker-min-max-hint" 
      aria-hidden="true" 
      tabindex="-1" 
      style="display: none;">
    
    <div class="usa-date-picker__wrapper">
      <input 
        class="usa-input usa-date-picker__external-input" 
        id="date-picker-min-max"
        aria-labelledby="date-picker-min-max-label" 
        aria-describedby="date-picker-min-max-hint" 
        placeholder="mm/dd/yyyy"
        type="text">
    </div>
  </div>
</div>
```

## Required Date Picker Example
```html
<div class="usa-form-group">
  <label class="usa-label" id="date-picker-req-label" for="date-picker-req">
    Required Date <span class="usa-label__required">*</span>
  </label>
  
  <div class="usa-date-picker usa-date-picker--initialized" data-min-date="0000-01-01">
    <input 
      class="usa-input usa-date-picker__internal-input" 
      aria-labelledby="date-picker-req-label" 
      aria-hidden="true" 
      tabindex="-1" 
      required
      style="display: none;">
    
    <div class="usa-date-picker__wrapper">
      <input 
        class="usa-input usa-date-picker__external-input" 
        id="date-picker-req"
        aria-labelledby="date-picker-req-label" 
        placeholder="mm/dd/yyyy"
        type="text"
        required>
    </div>
  </div>
</div>
```

### Context

The Date Picker is a USWDS-based component that integrates into the MDWDS form system, composing with the form group, label, and hint text components. It provides an accessible alternative to native date inputs and enables consistent date entry across Maryland digital properties.

---

## Date Range Picker

*Components*

The Date Range Picker component enables users to select a date range using two synchronized date picker widgets (start date and end date). It validates that the end date is after the start date and supports constraining the range with minimum and maximum dates. Use this when users need to specify a date interval, such as for booking, event planning, or filtering by date range.

### Key Information

## Key Features

- **Dual Date Pickers**: Two connected date picker components that work together to enforce valid date ranges
- **Date Constraints**: Support for minimum (`minDate`) and maximum (`maxDate`) dates in YYYY-MM-DD format
- **Default Values**: Can be pre-populated with `startDefaultValue` and `endDefaultValue` (YYYY-MM-DD format)
- **Required State**: Boolean `required` property to make both date fields mandatory
- **Disabled State**: Boolean `disabled` property to disable both date picker inputs
- **Labels and Hints**: Configurable `startLabel` and `endLabel` properties; optional `hintText` for date format guidance
- **Form Integration**: `startName` and `endName` properties for input name attributes
- **Analytics Support**: Optional Google Analytics tracking with `enableAnalytics`, `gaCategory`, `gaAction`, and `gaLabel` properties
- **Keyboard Navigation**: Full keyboard support across both pickers
- **Accessibility**: Follows WCAG 2.1 AA requirements with proper ARIA labels and labelledby attributes

## CSS Classes

- `.usa-date-range-picker`: Main container wrapper
- `.usa-date-range-picker__range-start`: Applied to the start date picker's date-picker container
- `.usa-date-range-picker__range-end`: Applied to the end date picker's date-picker container (implied from pattern)
- `.usa-form-group`: Standard form group wrapper for each date picker
- `.usa-label`: Label element styling
- `.usa-hint`: Hint text styling
- `.usa-date-picker`: Individual date picker component
- `.usa-date-picker--initialized`: Applied when date picker is fully initialized
- `.usa-date-picker__internal-input`: Internal input field class
- `.usa-input`: Standard input styling

## Data Attributes

- `data-min-date`: Minimum selectable date (format: YYYY-MM-DD)
- `data-max-date`: Maximum selectable date (format: YYYY-MM-DD)
- `data-range-date`: Tracks the date range state
- `data-default-date`: Stores default date value

## Required Attributes

- `id` on input elements (unique identifiers)
- `for` on label elements (links labels to inputs)
- `aria-labelledby` on inputs (connects to label by ID)
- `aria-describedby` on inputs (connects to hint text by ID)

## JavaScript Requirement

This component requires USWDS JavaScript to be loaded and initialized. The component uses the `.usa-date-picker--initialized` class to indicate successful initialization.

### Implementation

```html
<div class="usa-date-range-picker" data-min-date="0000-01-01">
  <!-- Start Date Picker -->
  <div class="usa-form-group">
    <label class="usa-label" id="date-range-start-label-id-zfxqi06s7v8" for="date-range-start-id-zfxqi06s7v8">
      Event start date
    </label>
    <div class="usa-hint" id="date-range-start-hint-id-zfxqi06s7v8">mm/dd/yyyy</div>
    <div class="usa-date-picker usa-date-picker--initialized usa-date-range-picker__range-start" data-min-date="0000-01-01" data-max-date="" data-range-date="" data-default-date="">
      <input class="usa-input usa-date-picker__internal-input" aria-labelledby="date-range-start-label-id-zfxqi06s7v8" aria-describedby="date-range-start-hint-id-zfxqi06s7v8" id="date-range-start-id-zfxqi06s7v8" type="text" inputmode="numeric" placeholder="mm/dd/yyyy" />
    </div>
  </div>

  <!-- End Date Picker -->
  <div class="usa-form-group">
    <label class="usa-label" id="date-range-end-label-id-zfxqi06s7v8" for="date-range-end-id-zfxqi06s7v8">
      Event end date
    </label>
    <div class="usa-hint" id="date-range-end-hint-id-zfxqi06s7v8">mm/dd/yyyy</div>
    <div class="usa-date-picker usa-date-picker--initialized usa-date-range-picker__range-end" data-min-date="0000-01-01" data-max-date="" data-range-date="" data-default-date="">
      <input class="usa-input usa-date-picker__internal-input" aria-labelledby="date-range-end-label-id-zfxqi06s7v8" aria-describedby="date-range-end-hint-id-zfxqi06s7v8" id="date-range-end-id-zfxqi06s7v8" type="text" inputmode="numeric" placeholder="mm/dd/yyyy" />
    </div>
  </div>
</div>
```

## With Min/Max Dates Example

```html
<div class="usa-date-range-picker" data-min-date="2024-01-01" data-max-date="2024-12-31">
  <div class="usa-form-group">
    <label class="usa-label" id="start-label" for="start-input">
      Start Date
    </label>
    <div class="usa-hint" id="start-hint">mm/dd/yyyy</div>
    <div class="usa-date-picker usa-date-picker--initialized usa-date-range-picker__range-start" data-min-date="2024-01-01" data-max-date="2024-12-31" data-default-date="2024-01-15">
      <input class="usa-input usa-date-picker__internal-input" aria-labelledby="start-label" aria-describedby="start-hint" id="start-input" type="text" inputmode="numeric" placeholder="mm/dd/yyyy" />
    </div>
  </div>

  <div class="usa-form-group">
    <label class="usa-label" id="end-label" for="end-input">
      End Date
    </label>
    <div class="usa-hint" id="end-hint">mm/dd/yyyy</div>
    <div class="usa-date-picker usa-date-picker--initialized usa-date-range-picker__range-end" data-min-date="2024-01-01" data-max-date="2024-12-31" data-default-date="2024-12-15">
      <input class="usa-input usa-date-picker__internal-input" aria-labelledby="end-label" aria-describedby="end-hint" id="end-input" type="text" inputmode="numeric" placeholder="mm/dd/yyyy" />
    </div>
  </div>
</div>
```

## Required State

```html
<div class="usa-date-range-picker" data-min-date="0000-01-01">
  <div class="usa-form-group">
    <label class="usa-label" id="req-start-label" for="req-start-input">
      Start Date <span class="usa-label__required-mark">*</span>
    </label>
    <div class="usa-hint" id="req-start-hint">mm/dd/yyyy</div>
    <div class="usa-date-picker usa-date-picker--initialized usa-date-range-picker__range-start" data-min-date="0000-01-01">
      <input class="usa-input usa-date-picker__internal-input" required aria-labelledby="req-start-label" aria-describedby="req-start-hint" id="req-start-input" type="text" inputmode="numeric" placeholder="mm/dd/yyyy" />
    </div>
  </div>

  <div class="usa-form-group">
    <label class="usa-label" id="req-end-label" for="req-end-input">
      End Date <span class="usa-label__required-mark">*</span>
    </label>
    <div class="usa-hint" id="req-end-hint">mm/dd/yyyy</div>
    <div class="usa-date-picker usa-date-picker--initialized usa-date-range-picker__range-end" data-min-date="0000-01-01">
      <input class="usa-input usa-date-picker__internal-input" required aria-labelledby="req-end-label" aria-describedby="req-end-hint" id="req-end-input" type="text" inputmode="numeric" placeholder="mm/dd/yyyy" />
    </div>
  </div>
</div>
```

## Disabled State

```html
<div class="usa-date-range-picker" data-min-date="0000-01-01">
  <div class="usa-form-group">
    <label class="usa-label" id="dis-start-label" for="dis-start-input">
      Start Date
    </label>
    <div class="usa-hint" id="dis-start-hint">mm/dd/yyyy</div>
    <div class="usa-date-picker usa-date-picker--initialized usa-date-range-picker__range-start" data-min-date="0000-01-01">
      <input class="usa-input usa-date-picker__internal-input" disabled aria-labelledby="dis-start-label" aria-describedby="dis-start-hint" id="dis-start-input" type="text" inputmode="numeric" placeholder="mm/dd/yyyy" />
    </div>
  </div>

  <div class="usa-form-group">
    <label class="usa-label" id="dis-end-label" for="dis-end-input">
      End Date
    </label>
    <div class="usa-hint" id="dis-end-hint">mm/dd/yyyy</div>
    <div class="usa-date-picker usa-date-picker--initialized usa-date-range-picker__range-end" data-min-date="0000-01-01">
      <input class="usa-input usa-date-picker__internal-input" disabled aria-labelledby="dis-end-label" aria-describedby="dis-end-hint" id="dis-end-input" type="text" inputmode="numeric" placeholder="mm/dd/yyyy" />
    </div>
  </div>
</div>
```

## With Google Analytics Attributes

```html
<div class="usa-date-range-picker" data-min-date="0000-01-01">
  <div class="usa-form-group">
    <label class="usa-label" id="ga-start-label" for="ga-start-input">
      Start Date
    </label>
    <div class="usa-hint" id="ga-start-hint">mm/dd/yyyy</div>
    <div class="usa-date-picker usa-date-picker--initialized usa-date-range-picker__range-start" data-min-date="0000-01-01">
      <input class="usa-input usa-date-picker__internal-input" data-ga-event-category="booking" data-ga-event-action="start_date_selected" data-ga-event-label="date-range-picker" aria-labelledby="ga-start-label" aria-describedby="ga-start-hint" id="ga-start-input" type="text" inputmode="numeric" placeholder="mm/dd/yyyy" />
    </div>
  </div>

  <div class="usa-form-group">
    <label class="usa-label" id="ga-end-label" for="ga-end-input">
      End Date
    </label>
    <div class="usa-hint" id="ga-end-hint">mm/dd/yyyy</div>
    <div class="usa-date-picker usa-date-picker--initialized usa-date-range-picker__range-end" data-min-date="0000-01-01">
      <input class="usa-input usa-date-picker__internal-input" data-ga-event-category="booking" data-ga-event-action="end_date_selected" data-ga-event-label="date-range-picker" aria-labelledby="ga-end-label" aria-describedby="ga-end-hint" id="ga-end-input" type="text" inputmode="numeric" placeholder="mm/dd/yyyy" />
    </div>
  </div>
</div>
```

## JavaScript Initialization

```javascript
// USWDS Date Range Picker requires USWDS JavaScript library
// Include the USWDS JS bundle from CDN:
<script src="https://cdn.jsdelivr.net/npm/uswds@3.x.x/dist/js/uswds.min.js"></script>

// The component auto-initializes when USWDS JS loads and finds elements with the usa-date-range-picker class
// No additional initialization code is required if using the USWDS JS bundle
```

### Context

The Date Range Picker is a USWDS component integrated into MDWDS that combines two synchronized Date Picker components to enable range selection with validation. It extends the single Date Picker component by adding cross-field validation and coordinated min/max constraints, allowing complex date-range workflows while maintaining accessibility and keyboard navigation consistency across the system.

---

## File Input

*Components*

The File Input component provides an accessible and user-friendly way to upload single or multiple files. It supports drag-and-drop functionality, file type restrictions, error states, and optional Google Analytics tracking. Use this component whenever users need to upload documents or other file types to a form.

### Key Information

## Variants & Modifiers
- **Default**: Single file upload with drag-and-drop
- **Multiple Files**: Enable multiple file selection
- **Image Only**: Restrict to image file types
- **Error State**: Display validation error messages
- **Disabled**: Prevent file input interaction

## Key CSS Classes
- `usa-form-group` - Form group wrapper
- `usa-label` - Label element
- `usa-hint` - Hint/helper text
- `usa-file-input` - Main file input container
- `usa-sr-only` - Screen reader only text
- `usa-file-input__target` - Drag-and-drop target area
- `usa-file-input__box` - Visual container for drop zone
- `usa-file-input__instructions` - Instructions text wrapper
- `usa-file-input__drag-text` - Drag instruction text
- `usa-file-input__choose` - "Choose from folder" text

## Component Properties
- `label` (string, required) - Label text for the file input
- `hint` (string, optional) - Helper text describing file requirements
- `multiple` (boolean) - Allow multiple file selection
- `accept` (string) - Comma-separated file types (e.g., '.pdf,.doc,.docx' or 'image/*')
- `disabled` (boolean) - Disable the input
- `error` (boolean) - Show error state
- `errorMessage` (string) - Error message to display

## Analytics Properties
- `enableAnalytics` (boolean) - Enable GA tracking
- `gaCategory` (string) - GA event category
- `gaAction` (string) - GA event action
- `gaLabel` (string) - GA event label

## Required Attributes
- `for` attribute on label linked to input `id`
- `aria-live="polite"` on status message div
- `aria-hidden="true"` on visual instructions

## Important Facts
- Implements USWDS File Input component
- Supports native HTML5 file input with USWDS styling
- Drag-and-drop functionality requires USWDS JavaScript initialization
- Status updates announced to screen readers via aria-live region
- Built on usa-form base styling

### Implementation

```html
<form class="usa-form">
  <div class="usa-form-group">
    <label class="usa-label" for="id-8zrdopf1b9i">
      Upload a file
    </label>
    <div class="usa-hint" id="id-4t7m3jodzqb">
      Select PDF, Word, or text files smaller than 20MB
    </div>
    
    <div class="usa-file-input">
      <div class="usa-sr-only" aria-live="polite">
        No file selected.
      </div>
      <div class="usa-file-input__target">
        <div class="usa-file-input__box"></div>
        <div class="usa-file-input__instructions" aria-hidden="true">
          <span class="usa-file-input__drag-text">Drag file here or</span>
          <span class="usa-file-input__choose">choose from folder</span>
        </div>
        <input 
          class="usa-file-input__input" 
          id="id-8zrdopf1b9i"
          type="file"
          accept=".pdf,.doc,.docx,.txt"
          aria-describedby="id-4t7m3jodzqb"
        />
      </div>
    </div>
  </div>
</form>
```

### Multiple Files Variant
```html
<input 
  class="usa-file-input__input" 
  id="id-multiple"
  type="file"
  multiple
  accept=".pdf,.doc,.docx,.txt"
  aria-describedby="id-hint"
/>
```

### Error State Variant
```html
<div class="usa-form-group usa-form-group--error">
  <label class="usa-label" for="id-error">
    Upload a file
  </label>
  <div class="usa-error-message" role="alert">
    Please select a valid file
  </div>
  <div class="usa-file-input">
    <div class="usa-sr-only" aria-live="polite">
      No file selected.
    </div>
    <div class="usa-file-input__target">
      <div class="usa-file-input__box"></div>
      <div class="usa-file-input__instructions" aria-hidden="true">
        <span class="usa-file-input__drag-text">Drag file here or</span>
        <span class="usa-file-input__choose">choose from folder</span>
      </div>
      <input 
        class="usa-file-input__input" 
        id="id-error"
        type="file"
        aria-invalid="true"
      />
    </div>
  </div>
</div>
```

### Disabled State Variant
```html
<input 
  class="usa-file-input__input" 
  id="id-disabled"
  type="file"
  disabled
/>
```

### Context

The File Input component is part of the USWDS-based form components system in MDWDS. It integrates with the `usa-form-group` and `usa-label` components to provide complete accessible form field functionality. Pairs with hint text (usa-hint) and error messaging (usa-error-message) for comprehensive user feedback.

---

## Footer

*Components*

The Footer component is a comprehensive page footer that displays navigate links for Maryland.gov, including top services, government information, policies, connect options, and alerts. It serves as a persistent navigation and information access point at the bottom of pages and provides users with quick links to critical state services and resources.

### Key Information

## Class Names and Structure

### Root Container
- `maryland-footer` — main footer wrapper
- `maryland-footer__container` — inner container for footer content

### Sections
- `maryland-footer__section` — wraps each major section (e.g., Top services, Government)
- Use `aria-labelledby` attribute to associate section with its heading

### Section Headers
- `maryland-footer__title` — main section heading (H2 level)
- Use `id` attribute to match with section's `aria-labelledby`

### Link Groups
- `maryland-footer__link-group` — navigation container for related links
- `maryland-footer__link-group-heading` — subheading for link group (H3 level)
- `maryland-footer__link-group-list` — unordered list `<ul>` containing link items

### Content Area
- `maryland-footer__content` — wraps multiple link groups within a section

## Key Attributes
- Sections require `aria-labelledby` pointing to the heading `id`
- Headings (`h2`, `h3`) must have `id` attributes that match the associated `aria-labelledby` values
- Links are standard `<a>` elements with `href` attributes

## Content Structure
The footer typically organizes links into sections like:
- Top services (Vehicle services, Food assistance, Unemployment, Taxes, etc.)
- Government (Governor, Cabinet agencies, State agencies, etc.)
- Policies (Accessibility, Privacy & security, Terms of use)
- Connect (Maryland Relay, Employee directory, News, etc.)
- Alerts (Emergency alerts, Travel alerts, Cybersecurity, etc.)

## Copyright Notice
Footer includes a copyright statement (© 2026 State of Maryland. All rights reserved.)

### Implementation

```html
<footer class="maryland-footer">
  <div class="maryland-footer__container">
    <section aria-labelledby="global-footer" class="maryland-footer__section">
      <h2 class="maryland-footer__title" id="global-footer">
        Explore Maryland.gov
      </h2>
      <div class="maryland-footer__content">
        <nav class="maryland-footer__link-group" aria-labelledby="top-services">
          <h3 class="maryland-footer__link-group-heading" id="top-services">
            Top services
          </h3>
          <ul class="maryland-footer__link-group-list">
            <li>
              <a href="https://mva.maryland.gov/vehicles">Vehicle services</a>
            </li>
            <li>
              <a href="https://dhs.maryland.gov/supplemental-nutrition-assistance-program/">Food assistance / SNAP</a>
            </li>
            <li>
              <a href="https://www.labor.maryland.gov/employment/unemployment.shtml">Unemployment services</a>
            </li>
            <li>
              <a href="https://www.marylandtaxes.gov/individual/index.php">Taxes</a>
            </li>
            <li>
              <a href="https://elections.maryland.gov/voter_registration/index.html">Register to vote</a>
            </li>
            <li>
              <a href="https://www.maryland.gov/pages/residents.aspx">Resident resources</a>
            </li>
            <li>
              <a href="https://www.visitmaryland.org/">Visit Maryland</a>
            </li>
          </ul>
        </nav>
        <!-- Additional link groups follow the same pattern -->
      </div>
    </section>
  </div>
</footer>
```

## Full Component Structure
Multiple `maryland-footer__link-group` elements can be placed within a single `maryland-footer__content` container. Each section can contain one or more link groups. The entire footer is wrapped in `maryland-footer` and `maryland-footer__container`.

### Context

The Footer component is a foundational layout component in the MDWDS system that provides consistent bottom-of-page navigation and information architecture across all Maryland.gov properties. It works in conjunction with the Header component to frame page content and uses semantic HTML (section, nav, heading hierarchy) with ARIA attributes to ensure accessibility and proper semantic structure.

---

## Form

*Components*

The USWDS Form component provides a consistent container and semantic markup for organizing form elements. It supports standard and large variants, fieldset grouping with legends, and optional Google Analytics tracking. Use it to create accessible, properly-structured forms with organized field groups.

### Key Information

## Variants and Modifiers

- **Standard Form**: `usa-form` class applied to `<form>` element
- **Large Form**: `usa-form--large` modifier class for emphasis
- **With Fieldset**: Use `<fieldset>` with `<legend>` to group related fields

## Required HTML Structure

- Form element with `usa-form` class
- Labels use `usa-label` class and `for` attribute linking to input `id`
- Inputs use `usa-input` class
- Buttons use `usa-button` class with `type="submit"`
- Fieldsets use standard HTML5 `<fieldset>` and `<legend>` elements

## Configuration Options

- **large**: Boolean to enable large variant styling (usa-form--large)
- **includeFieldset**: Boolean to include fieldset with legend
- **legend**: String for fieldset legend text
- **enableAnalytics**: Boolean to enable Google Analytics tracking attributes
- **gaCategory**: GA event category string
- **gaAction**: GA event action string
- **gaLabel**: GA event label string

## Key Features

- Supports text inputs, email inputs, radio buttons, checkboxes, and textareas
- Hint text support for field guidance
- Nested fieldsets for complex forms
- Autocomplete attributes (e.g., `autocomplete="given-name"`, `autocomplete="email"`)
- `required` attribute for validation
- Unique ID generation for all form inputs and labels

### Implementation

## Basic Form

```html
<form class="usa-form" id="form-id">
  <label class="usa-label" for="first-name-id">First name</label>
  <input class="usa-input" name="first-name" type="text" autocomplete="given-name" required="" id="first-name-id">

  <label class="usa-label" for="last-name-id">Last name</label>
  <input class="usa-input" name="last-name" type="text" autocomplete="family-name" required="" id="last-name-id">

  <label class="usa-label" for="email-id">Email address</label>
  <input class="usa-input" name="email" type="email" autocomplete="email" required="" id="email-id">

  <button type="submit" class="usa-button">Submit</button>
</form>
```

## Large Form Variant

```html
<form class="usa-form usa-form--large" id="form-id">
  <label class="usa-label" for="first-name-id">First name</label>
  <input class="usa-input" name="first-name" type="text" autocomplete="given-name" required="" id="first-name-id">

  <label class="usa-label" for="last-name-id">Last name</label>
  <input class="usa-input" name="last-name" type="text" autocomplete="family-name" required="" id="last-name-id">

  <label class="usa-label" for="email-id">Email address</label>
  <input class="usa-input" name="email" type="email" autocomplete="email" required="" id="email-id">

  <button type="submit" class="usa-button">Submit</button>
</form>
```

## Form with Fieldset

```html
<form class="usa-form" id="form-id">
  <fieldset>
    <legend>Personal Information</legend>

    <label class="usa-label" for="first-name-id">First name</label>
    <input class="usa-input" name="first-name" type="text" autocomplete="given-name" required="" id="first-name-id">

    <label class="usa-label" for="last-name-id">Last name</label>
    <input class="usa-input" name="last-name" type="text" autocomplete="family-name" required="" id="last-name-id">

    <label class="usa-label" for="email-id">Email address</label>
    <input class="usa-input" name="email" type="email" autocomplete="email" required="" id="email-id">
  </fieldset>

  <button type="submit" class="usa-button">Submit</button>
</form>
```

### Context

The Form component is a foundational USWDS component in MDWDS that provides semantic, accessible containers for organizing form inputs. It combines with other form elements (labels, inputs, buttons, fieldsets) to create properly-structured, compliant forms and typically composes with input fields, fieldsets, and action buttons throughout MDWDS applications.

---

## Header

*Components*

The Header component helps users identify where they are and provides a quick, organized way to reach the main sections of a website. It includes a utility navigation area, logo/home link, and optional primary navigation menu. Use it as the top-level navigation structure for Maryland government websites.

### Key Information

## Key Class Names
- `maryland-header`: Main header container
- `maryland-header__util-nav-container`: Container for utility navigation
- `maryland-header__util-nav`: Utility navigation list (horizontal links/buttons)
- `maryland-header__home`: Home/logo link element
- `maryland-header__logo`: Logo image element

## Key Properties/Options
- **Agency Title**: Name of the agency for the site (string)
- **Enable Utility Menu**: Adds the utility nav to header layout (boolean, default: false)
- **Utility Menu**: JSON array representation of utility menu structure with link objects
- **Enable Primary Menu**: Adds the primary nav to header layout (boolean, default: false)
- **Show Maryland.gov Link**: Shows Maryland.gov link at bottom of mobile navigation (boolean, default: false)
- **Navigation Items**: JSON array representation of nav menu structure

## Variants
- Utility navigation with links and buttons (uses `usa-button usa-button--small` for styled buttons)
- Optional primary navigation menu
- Responsive behavior with mobile navigation considerations

## Structure Notes
- Utility navigation items are rendered as `<li>` elements inside a `<ul class="maryland-header__util-nav">`
- Links within utility nav are plain `<a>` tags or `<a class="usa-button usa-button--small">` for button-styled items
- Logo is an `<img>` with src pointing to Maryland wordmark SVG and descriptive alt text

### Implementation

```html
<header class="maryland-header">
  <div class="maryland-header__util-nav-container">
    <ul class="maryland-header__util-nav">
      <li>
        <a href="#!">Link One</a>
      </li>
      <li>
        <a href="#!">Link Two</a>
      </li>
      <li>
        <a class="usa-button usa-button--small" href="#!">Button</a>
      </li>
    </ul>
  </div>

  <a class="maryland-header__home" href="/">
    <img class="maryland-header__logo" src="https://designsystem.maryland.gov/assets/md_wordmark_horizontal-D9RJzvGS.svg" alt="Maryland.gov home">
  </a>
</header>
```

## Utility Navigation Variant
The utility menu renders as a list of `<li>` elements with `<a>` tags. Button-styled items use the `usa-button usa-button--small` classes applied to the anchor tag itself.

### Context

The Header is a foundational component in the MDWDS system that serves as the primary site navigation and branding area. It composes with utility navigation controls and integrates with the USA Design System button component for styled call-to-action items in the utility menu.

---

## Hero

*Components*

The Hero component is a full-width banner section that displays prominent content at the top of pages, with variants supporting landing pages, agency pages, regular pages, news articles, and location pages. It solves the problem of creating visually distinctive page headers with flexible layouts supporting background images, text overlays, logos, and call-to-action buttons. Use it to establish page context and draw attention to key messaging.

### Key Information

## Variants

The Hero component supports six main variants:
- **Landing Main**: Full-width landscape background image with text overlay for landing pages. Title starting with "Welcome to " auto-displays the prefix as styled eyebrow text.
- **Landing Agency**: White background variant for agency landing pages with optional agency logo support and no breadcrumbs.
- **Landing Regular**: Standard landing page hero variant.
- **Basic**: Basic hero variant.
- **News**: Hero variant for news/article pages.
- **Location**: Hero variant for location-specific pages.

## Key Class Names

- `maryland-hero` - Base hero section container
- `maryland-hero--landing-main` - Modifier for landing main variant
- `maryland-hero__background-image` - Background image element
- `maryland-hero__container` - Inner container wrapper
- `maryland-hero__content` - Content wrapper
- `maryland-hero__title` - Main heading
- `maryland-hero__title-text` - Title text span
- `maryland-hero__eyebrow` - Eyebrow/prefix text (auto-styled for "Welcome to " titles)

## Required Elements

- **title** (required): Main heading text for the hero section. For Landing Main variant, titles starting with "Welcome to " will auto-style the prefix as an eyebrow.
- **backgroundImage** (optional): Landscape background image selection (available options: forest, farmland, bridge). Only used for Landing Main Hero variant.
- **description** (optional): Subtitle or descriptive text.

## Important Notes

- Background images must include the gradient overlay baked into the image itself; the component does not apply a CSS gradient overlay.
- Background images should be exported from Figma with both the Photo and Rectangle gradient layers merged.
- Features full-width background image positioning for scenic display.
- Supports optional agency logo (displays above title or on right side depending on layout).
- Some variants include no breadcrumb navigation.

### Implementation

```html
<!-- Landing Main Hero with Auto-Detected Eyebrow -->
<section class="maryland-hero maryland-hero--landing-main" aria-labelledby="id-nnxvk2y0ooj">
  <img alt="" class="maryland-hero__background-image" src="https://designsystem.maryland.gov/assets/md_forest-DB-269v5.png">
  <div class="maryland-hero__container">
    <div class="grid-container">
      <div class="grid-row">
        <div class="grid-col-12">
          <div class="maryland-hero__content">
            <h1 class="maryland-hero__title" id="id-nnxvk2y0ooj">
              <span class="maryland-hero__eyebrow">Welcome to</span>
              <span class="maryland-hero__title-text">Maryland</span>
            </h1>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

### Variant: Landing Main with Description
```html
<section class="maryland-hero maryland-hero--landing-main" aria-labelledby="hero-title">
  <img alt="" class="maryland-hero__background-image" src="image-url.png">
  <div class="maryland-hero__container">
    <div class="grid-container">
      <div class="grid-row">
        <div class="grid-col-12">
          <div class="maryland-hero__content">
            <h1 class="maryland-hero__title" id="hero-title">
              <span class="maryland-hero__eyebrow">Welcome to</span>
              <span class="maryland-hero__title-text">Maryland</span>
            </h1>
            <p class="maryland-hero__description">Optional description text</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

### Key ARIA Attributes
- `aria-labelledby`: References the title element `id` for accessibility; required for semantic structure

### Context

The Hero component is a foundational layout component in the MDWDS system that serves as the primary visual entry point for pages. It composes with the grid system (using `grid-container`, `grid-row`, `grid-col-12`) and integrates with optional child components like agency logos, buttons, and descriptions to create flexible, responsive page headers.

---

## Highlight

*Components*

The Highlight component displays up to 3 columns of featured links with an optional section header and description. Each column can contain a title, description, up to 5 links, and an optional "more" link. Use this component to feature key content areas and help users navigate to important services or information.

### Key Information

## CSS Classes

- `maryland-highlight` — Main wrapper section element
- `maryland-highlight__section-title` — Section heading (optional)
- `maryland-highlight__section-description` — Section description (optional)
- `maryland-highlight__grid` — Grid container holding columns
- `maryland-highlight__item` — Individual column container
- `maryland-highlight__title` — Column title
- `maryland-highlight__links` — Unordered list of links within a column
- `maryland-highlight__link` — Individual link item (inferred from visible structure)

## Key Attributes & Features

- **Section Header**: Optional heading and description via `title` and `description` properties
- **Column Count**: Configurable via `columnCount` property (1, 2, or 3 columns)
- **Links per Column**: Up to 5 links per column with optional icons
- **Icon Support**: Each link can have an optional icon type specified via `colXLinkYIconType` properties
- **ARIA Labeling**: Section uses `aria-labelledby` to associate with the section title
- **Responsive Grid**: Uses `maryland-highlight__grid` to manage column layout

## Properties

- `title` — Section heading (optional, string)
- `description` — Section description (optional, string)
- `columnCount` — Number of columns to display (number: 1, 2, or 3)
- `col1Title`, `col2Title`, `col3Title` — Column titles (string)
- `col1Description`, `col2Description`, `col3Description` — Column descriptions (string)
- `colXLinkYText` — Link text (up to 5 links per column, string)
- `colXLinkYUrl` — Link URL (up to 5 links per column, string)
- `colXLinkYIconType` — Icon type for each link (string, optional)

### Implementation

```html
<section class="maryland-highlight" aria-labelledby="id-xn8b4gqzvy">
  <h2 class="maryland-highlight__section-title" id="id-xn8b4gqzvy">
    Benefits, services and business
  </h2>
  <p class="maryland-highlight__section-description">
    Find the right information you need today in these featured areas.
  </p>
  <div class="maryland-highlight__grid">
    
    <div class="maryland-highlight__item">
      <h3 class="maryland-highlight__title">Benefits</h3>
      <ul class="maryland-highlight__links">
        <li>
          <a href="[link-url]" class="maryland-highlight__link">Health and medical</a>
        </li>
        <li>
          <a href="[link-url]" class="maryland-highlight__link">Unemployment and jobs</a>
        </li>
        <li>
          <a href="[link-url]" class="maryland-highlight__link">Download benefits guide (PDF)</a>
        </li>
      </ul>
    </div>

    <div class="maryland-highlight__item">
      <h3 class="maryland-highlight__title">Services</h3>
      <ul class="maryland-highlight__links">
        <li>
          <a href="[link-url]" class="maryland-highlight__link">Driving and transportation</a>
        </li>
        <li>
          <a href="[link-url]" class="maryland-highlight__link">Recreation licenses and permits</a>
        </li>
        <li>
          <a href="[link-url]" class="maryland-highlight__link">Federal education resources</a>
        </li>
      </ul>
    </div>

    <div class="maryland-highlight__item">
      <h3 class="maryland-highlight__title">Business and work</h3>
      <ul class="maryland-highlight__links">
        <li>
          <a href="[link-url]" class="maryland-highlight__link">Licenses and permits for professionals</a>
        </li>
        <li>
          <a href="[link-url]" class="maryland-highlight__link">Doing business in Maryland</a>
        </li>
      </ul>
    </div>

  </div>
</section>
```

## Notes

- The section element uses `aria-labelledby` to reference the section title for accessibility
- The grid container (`maryland-highlight__grid`) holds all column items and handles responsive column layout
- Each column is wrapped in `maryland-highlight__item`
- Column titles use `maryland-highlight__title` heading level (h3)
- Links are organized in an unordered list (`maryland-highlight__links`) with individual list items containing anchor tags
- The component supports optional section-level header and description
- Icon support is available through component properties but rendering depends on implementation details

### Context

The Highlight component is a featured content display pattern in the MDWDS system used to organize and showcase key information areas on pages. It composes with other navigation and link components to create scannable, organized sections of related content that guide users to important services, benefits, or resources.

---

## Icon

*Components*

The USWDS Icon component provides inline SVG icons following USWDS design patterns. It allows developers to select from a library of icon names, configure sizes (3–9), customize colors, and add accessibility attributes. Use this component to display semantic or decorative icons throughout your application with proper ARIA support.

### Key Information

## Icon Variants & Properties

### Icon Names
Available USWDS icon names: `check`, `close`, `search`, `arrow_forward`, `arrow_back`, `arrow_upward`, `arrow_downward`, `add`, `remove`, `delete`, `edit`, `check_circle`, `error`, `warning`, `info`, `calendar_today`, `mail`, `phone`, `file_download`, `settings`, `menu`, `more_vert`, `more_horiz`

### Sizing
- Size tokens: `3` (smallest) through `9` (largest)
- Controlled via `size` property
- Applied to CSS class: `usa-icon--size-{3|4|5|6|7|8|9}`

### Color
- Custom color values supported: semantic names like `primary`, `error`, `success`, or hex values
- Controlled via `color` property

### Accessibility
- `ariaLabel`: Accessible label for meaningful icons (leave empty for decorative icons)
- `ariaHidden`: Set to `true` for decorative icons (default); `false` for meaningful icons with `aria-label`
- Decorative icons should use `aria-hidden="true"` and `role="img"`
- Meaningful icons should have `aria-label` attribute

### Analytics Tracking (Optional)
- `enableAnalytics`: Enable/disable GA tracking
- `gaCategory`: Google Analytics event category
- `gaAction`: Google Analytics event action
- `gaLabel`: Google Analytics event label

### CSS Classes
- `usa-icon`: Base icon class
- `usa-icon--size-5`: Standard size variant (and size-3 through size-9)

### Rendered SVG Structure
Icons render as inline `<svg>` elements with:
- `focusable="false"` attribute (prevents tab focus on decorative icons)
- `role="img"` for semantic icons
- `viewBox="0 0 24 24"` coordinate system
- `class="usa-icon usa-icon--size-{N}"` where N is the size token
- Unique `id` attribute for multiple icon instances
- `aria-hidden="true"` for decorative use or `aria-label="..."` for semantic use
- `<path>` child elements with SVG path data

### Implementation

```html
<!-- Default Icon (Standard size-5) -->
<svg focusable="false" role="img" viewBox="0 0 24 24" class="usa-icon usa-icon--size-5" id="icon-id-unique" aria-hidden="true">
  <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path>
</svg>

<!-- Small Icon (size-3) -->
<svg focusable="false" role="img" viewBox="0 0 24 24" class="usa-icon usa-icon--size-3" id="icon-id-small" aria-hidden="true">
  <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path>
</svg>

<!-- Large Icon (size-9) -->
<svg focusable="false" role="img" viewBox="0 0 24 24" class="usa-icon usa-icon--size-9" id="icon-id-large" aria-hidden="true">
  <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path>
</svg>

<!-- Icon with Custom Color -->
<svg focusable="false" role="img" viewBox="0 0 24 24" class="usa-icon usa-icon--size-5" style="color: success;" id="icon-id-colored" aria-hidden="true">
  <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path>
</svg>

<!-- Meaningful Icon with Accessibility -->
<svg focusable="false" role="img" viewBox="0 0 24 24" class="usa-icon usa-icon--size-5" id="icon-id-accessible" aria-label="Success: Action completed">
  <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path>
</svg>

<!-- Icon with Google Analytics Tracking (attributes would be added by component) -->
<svg focusable="false" role="img" viewBox="0 0 24 24" class="usa-icon usa-icon--size-5" id="icon-id-tracked" aria-hidden="true" data-ga-category="navigation" data-ga-action="click" data-ga-label="search-icon">
  <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path>
</svg>
```

### Context

The Icon component is a USWDS-based utility that integrates into the MDWDS system for consistent iconography across applications. It composes seamlessly with navigation, buttons, form fields, and other UI elements that need visual indicators, while maintaining accessibility standards through ARIA attributes and proper semantic markup.

---

## Icon List

*Components*

The Icon List component presents a collection of items with Material icons, titles, optional descriptions, and optional links. Each item features a circular icon, making it ideal for highlighting services, features, or categories in a visually organized layout.

### Key Information

## Key Class Names

- `maryland-icon-list` — Container wrapper for the entire icon list
- `maryland-icon-list__header` — Header section containing title, description, and optional link
- `maryland-icon-list__title` — Title/heading text element
- `maryland-icon-list__description` — Description text for the entire list
- `maryland-icon-list__list` — Unordered list (`<ul>`) containing icon list items
- `maryland-link` — Optional link modifier for "view more" or similar navigation

## Variants & Modifiers

- **With Header**: Icon list can include an optional header with title, description text, and a link
- **With Sidebar**: Icon list items can be displayed in a layout that includes a sidebar
- **Default**: Standard icon list display

## Required Structure

- Main container uses `class="maryland-icon-list"`
- Header section requires semantic headings (`<h2>`, `<h3>`) with unique `id` attributes (used in `aria-labelledby`)
- List must be an unordered list (`<ul>`) with class `maryland-icon-list__list`
- Each list item is an `<li>` element within the list

## Accessibility

- Section elements use `aria-labelledby` to associate with the heading `id`
- Semantic HTML structure with proper heading hierarchy
- Headings must have unique IDs that match the `aria-labelledby` references

### Implementation

```html
<section class="maryland-icon-list" aria-labelledby="id-u2mote4xumc">
  <div class="maryland-icon-list__header">
    <h2 id="id-u2mote4xumc" class="maryland-icon-list__title">Lorem ipsum dolor sit amet</h2>
    <div class="maryland-icon-list__description">Mollit labore anim duis sunt qui aliquip sit qui fugiat elit.</div>
    <a class="maryland-link" href="#">
      Nisi proident ex
    </a>
  </div>

  <ul class="maryland-icon-list__list">
    <li>
      <!-- Icon list item content -->
    </li>
  </ul>
</section>
```

## Variant: With Sidebar

```html
<section class="maryland-icon-list" aria-labelledby="id-example-heading">
  <div class="maryland-icon-list__header">
    <h2 id="id-example-heading" class="maryland-icon-list__title">Section Title</h2>
    <div class="maryland-icon-list__description">Optional description text</div>
  </div>

  <ul class="maryland-icon-list__list">
    <!-- Icon list items with sidebar layout -->
  </ul>
</section>
```

### Context

The Icon List component integrates with MDWDS's layout grid system (grid-container, grid-row, grid-col-12) and uses standard Maryland Design System link styling. It serves as a reusable component for organizing and presenting collections of featured items, services, or categories within page templates.

---

## Icon List

*Components*

The Icon List component displays a list of items with accompanying icons, following USWDS design patterns. It supports multiple color variants, configurable sizes, and optional Google Analytics tracking. Use it when you need to present related items with visual indicators in a list format.

### Key Information

## Variants & Modifiers

- **Color Variants**: `default`, `primary`, `secondary`, `accent-warm`, `accent-cool` — controls icon color theme
- **Sizes**: `default` (standard), `lg` (large) — configurable via the component settings
- **Content Types**: Simple text content or rich content with HTML markup

## CSS Classes

- `usa-icon-list` — main list container
- `usa-icon-list__item` — individual list item wrapper
- `usa-icon-list__icon` — icon container within each item
- `usa-icon-list__content` — text/content container within each item

## Required Attributes & Properties

- `items` (array, required) — array of item objects, each containing:
  - `icon` — icon identifier or SVG
  - `content` — text or rich HTML content
  - `title` (optional) — item title
- `variant` (string, optional) — color variant for icons (default, primary, secondary, accent-warm, accent-cool)
- `size` (string, optional) — list size: `default` or `lg`
- `enableAnalytics` (boolean, optional) — enables Google Analytics tracking
- `gaCategory`, `gaAction`, `gaLabel` (strings, optional) — GA tracking parameters when analytics enabled

## Important Facts

- Component is built on USWDS patterns (link: https://designsystem.digital.gov/components/icon-list/)
- Supports multiple icon color theme options
- Integrates with Google Analytics for event tracking
- Can display both simple and rich content variants

### Implementation

```html
<ul class="usa-icon-list" id="icon-list-id-7tly3z5cv1t">
  <li class="usa-icon-list__item">
    <div class="usa-icon-list__icon">
      <svg class="usa-icon" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"></path>
      </svg>
    </div>
    <div class="usa-icon-list__content" id="content-id-vfuqsgby2qc">
      Direct access to interagency teams with insight into the TBM process
    </div>
  </li>
  <li class="usa-icon-list__item">
    <div class="usa-icon-list__icon">
      <svg class="usa-icon" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
        <path d="..."></path>
      </svg>
    </div>
    <div class="usa-icon-list__content">
      Unparalleled transparency into agency staffing and projects
    </div>
  </li>
  <li class="usa-icon-list__item">
    <div class="usa-icon-list__icon">
      <svg class="usa-icon" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24">
        <path d="..."></path>
      </svg>
    </div>
    <div class="usa-icon-list__content">
      Opportunities for collaboration and technology sharing
    </div>
  </li>
</ul>
```

## Notes on SVG Icons

- Each icon uses the `usa-icon` class
- Icons have `aria-hidden="true"` for screen readers (content is in the adjacent text div)
- `focusable="false"` prevents SVG from being tab-focused
- `role="img"` provides semantic meaning
- `viewBox` attribute scales icon appropriately

### Context

The Icon List component is a USWDS-based component that integrates into the MDWDS system for displaying structured, icon-annotated lists. It composes with the USWDS icon set and follows accessibility patterns with proper ARIA attributes, making it suitable for presenting related items, benefits, or features in a visually organized manner.

---

## Identifier

*Components*

The Identifier component signals trust and authority at the bottom of every government website. It displays agency branding, domain, legal disclaimer, and required policy links in a footer-like section. Use this to provide mandatory legal and accessibility information along with a link to the maryland.gov state portal.

### Key Information

## Structure
The Identifier is a USWDS component from the U.S. Web Design System that is implemented in MDWDS.

## Key Classes
- `usa-identifier` - Root container for the entire identifier component
- `usa-identifier__section` - Wrapper for identifier sections
- `usa-identifier__section--masthead` - Masthead section variant
- `usa-identifier__container` - Inner container for section content
- `usa-identifier__logos` - Container for agency logos
- `usa-identifier__logo` - Logo link element
- `usa-identifier__logo-img` - Logo image element
- `usa-identifier__identity` - Section for agency description/identity
- `usa-identifier__identity-domain` - Domain/URL display
- `usa-identifier__identity-disclaimer` - Legal disclaimer text

## Required Attributes
- `aria-label` - Required on sections to describe their purpose (e.g., "Agency identifier", "Agency description")
- `role="img"` - Should be added to logo images for proper semantic identification
- `aria-hidden="true"` - Used on decorative text spans (e.g., "An ")

## Component Properties
The component accepts the following configuration properties:

### Settings
- `agencyName` (string) - Parent agency name for branding and legal link labels
- `domain` (string) - Displayed domain in the identifier
- `logoSrc` (string) - Logo image URL (accessible via alt text)

### Accessibility
- `logoAlt` (string) - Alt text for screen readers describing the logo

### Analytics
- `enableAnalytics` (boolean) - Enable Google Analytics tracking attributes
- `gaCategory` (string) - GA category for link tracking
- `gaAction` (string) - GA action for link tracking
- `gaLabel` (string) - GA label for link tracking

## Content Sections
The identifier typically includes:
- Agency logo with alt text
- Agency name and domain
- Legal disclaimer
- Links to required pages (Accessibility statement, FOIA requests, No FEAR Act data, Office of the Inspector General, Performance reports, Privacy policy)
- Link to maryland.gov state portal

### Implementation

```html
<div class="usa-identifier">
  <section class="usa-identifier__section usa-identifier__section--masthead" aria-label="Agency identifier">
    <div class="usa-identifier__container">
      <div class="usa-identifier__logos">
        <a href="#" class="usa-identifier__logo">
          <img class="usa-identifier__logo-img" src="/assets/img/mdds-logo-wings.png" alt="Parent agency logo" role="img">
        </a>
      </div>
      <section class="usa-identifier__identity" aria-label="Agency description">
        <p class="usa-identifier__identity-domain">maryland.gov</p>
        <p class="usa-identifier__identity-disclaimer">
          <span aria-hidden="true">An </span>official website of the Parent agency
        </p>
      </section>
    </div>
  </section>
  <!-- Additional sections for links, navigation, and footer content follow the same structural pattern -->
</div>
```

## Key Structural Notes
- The root `usa-identifier` wrapper contains all identifier content
- The masthead section (`usa-identifier__section--masthead`) contains logo and agency identity
- The `usa-identifier__container` provides layout structure within each section
- Logo and identity information are grouped in the masthead section
- ARIA labels are required on all `<section>` elements for accessibility
- Images use both `alt` attribute and `role="img"` for proper semantics
- Decorative text spans use `aria-hidden="true"`

### Context

The Identifier is a footer component from the U.S. Web Design System (USWDS) that MDWDS includes to ensure every Maryland government website meets federal branding and accessibility requirements. It composes as a standalone footer section that wraps around agency branding, required legal links, and the state portal reference.

---

## In-Page Navigation

*Components*

The USWDS In-Page Navigation component provides automatic navigation for long content pages with multiple sections. It auto-generates a navigation menu from page headings, tracks the active section as the user scrolls, and supports sticky positioning and smooth scrolling. This component helps users navigate complex documents and understand their current position within the content.

### Key Information

## CSS Classes
- `usa-in-page-nav-container` — Wrapper container for the component
- `usa-in-page-nav` — Main navigation aside element
- `usa-prose` — Prose styling for main content area

## Required Attributes
- `data-heading-elements` — Comma-separated list of heading selectors to include in navigation (e.g., "h2, h3")
- `data-threshold` — Intersection Observer threshold for active section detection (e.g., "0.2")
- `data-scroll-offset` — Scroll offset in pixels to adjust active section tracking (e.g., "0")
- `aria-label="In-page navigation"` — Required for the nav element to identify its purpose
- `id` — Unique identifier for the main content container

## Key Features
- **Automatic Generation** — Navigation is auto-generated from page headings (h2, h3)
- **Sticky Positioning** — Navigation can remain visible while scrolling
- **Active Tracking** — Uses Intersection Observer API to highlight the current section
- **Keyboard Navigation** — Fully keyboard accessible with Tab and Enter keys
- **Focus States** — Links have distinct hover and focus states
- **WCAG 2.1 AA Compliant** — Tested for accessibility standards

## Configuration Options
- Heading elements are configurable via `data-heading-elements`
- Threshold for active detection is adjustable
- Scroll offset can be customized
- Optional Google Analytics tracking support
- Optional smooth scrolling behavior

### Implementation

```html
<div class="usa-in-page-nav-container">
  <aside class="usa-in-page-nav" 
         data-heading-elements="h2, h3" 
         data-threshold="0.2" 
         data-scroll-offset="0">
    <nav aria-label="In-page navigation">
      <!-- Navigation will be auto-generated by USWDS JavaScript -->
    </nav>
  </aside>
  
  <main class="usa-prose" id="main-content-id-y09fa749mol">
    <h2 id="section-id-y09fa749mol-0">Introduction</h2>
    <p>This is the introduction section. In-page navigation helps users navigate long documents by providing quick access to different sections. The navigation automatically updates to show which section is currently being viewed.</p>
  </main>
</div>
```

## Notes
- The `<nav>` element starts empty; USWDS JavaScript auto-generates navigation links from headings
- Each heading should have a unique `id` attribute for linking
- The component uses the Intersection Observer API to track scroll position
- Navigation items become active based on which section is currently in the viewport
- Keyboard users can Tab through navigation links and use Enter to jump to sections
- Focus is moved to the target section when activated via keyboard

### Context

The In-Page Navigation component is part of the USWDS (U.S. Web Design System) component library integrated into MDWDS. It typically accompanies long-form content pages and works alongside the prose typography component to create accessible, navigable documents. The component enhances user experience by providing overview and quick access to page structure without requiring custom JavaScript implementation.

---

## Input

*Components*

The USWDS Input component is a single-line text field used for collecting user data such as names, addresses, or short identifiers. It provides accessible form input with support for labels, placeholders, and ARIA attributes to ensure compliance with accessibility standards. Use this component whenever you need users to enter basic text information in a form.

### Key Information

**Key Class Names:**
- `usa-form`: Container for form elements
- `usa-label`: Label element associated with the input
- `usa-input`: The input field itself

**Required Attributes:**
- `id`: Unique identifier for the input (required for label association)
- `for` attribute on label: Must match the input's `id`
- `name`: Input name attribute used in form submissions

**Optional Attributes:**
- `placeholder`: Optional placeholder text displayed inside the input
- `aria-label`: ARIA label when visual label is hidden (Optional)
- `aria-describedby`: ID of an element providing additional description (Optional)

**Properties:**
- `label`: Text label associated with the input field
- `id`: Unique ID for input and label association
- `name`: Input name attribute (used in form submissions)
- `placeholder`: Optional placeholder text inside the input
- `ariaLabel`: ARIA label (used when label is visually hidden)
- `ariaDescribedBy`: ID of an element describing this input

### Implementation

```html
<form class="usa-form">
  <label class="usa-label" for="input-type-text">Text input label</label>
  <input class="usa-input" id="input-type-text" name="input-type-text">
</form>
```

**With Placeholder:**
```html
<form class="usa-form">
  <label class="usa-label" for="input-with-placeholder">Label text</label>
  <input class="usa-input" id="input-with-placeholder" name="input-with-placeholder" placeholder="Optional placeholder text">
</form>
```

**With ARIA Attributes:**
```html
<form class="usa-form">
  <label class="usa-label" for="input-accessible">Accessible input</label>
  <input class="usa-input" id="input-accessible" name="input-accessible" aria-label="Screen reader label" aria-describedby="input-helper-text">
  <span id="input-helper-text">Additional description</span>
</form>
```

### Context

The Input component is a core MDWDS form element built on USWDS standards, providing consistent styling and accessibility across Maryland web properties. It composes with form containers and validation components to create complete, accessible form experiences.

---

## Input Mask

*Components*

The Input Mask component provides formatted input fields for common data patterns like phone numbers, SSN, and ZIP codes. It automatically formats user input as they type and displays hint text showing the expected format. Use this when you need to enforce structured data entry with real-time formatting and validation.

### Key Information

## Variants & Mask Types

- **Phone**: `###-###-####` (10-digit phone number)
- **SSN**: `###-##-####` (Social Security Number)
- **ZIP Code**: `#####` or `#####-####` (5-digit or ZIP+4)
- **Custom**: User-defined mask pattern

## Required Attributes & Properties

- `data-input-mask=""` - Enables mask functionality on the input element
- `data-mask-type=""` - Specifies which mask to apply: `phone`, `ssn`, `zip`, or `custom`
- `type="text"` - Input type must be text
- `pattern=""` - Validation pattern (e.g., `[0-9]{3}-[0-9]{3}-[0-9]{4}` for phone)
- `placeholder=""` - Shows expected format with underscores (e.g., `___-___-____`)
- `aria-describedby=""` - Links to hint text for accessibility

## CSS Classes

- `usa-form` - Main form container
- `usa-form--large` - Large form variant
- `usa-label` - Label styling
- `usa-input` - Input field styling
- `usa-hint` - Hint text styling for format instructions

## Optional Properties

- `required` (boolean) - Marks field as required
- `disabled` (boolean) - Disables the input field
- `enableAnalytics` (boolean) - Enables Google Analytics tracking
- `gaCategory`, `gaAction`, `gaLabel` - GA tracking attributes when analytics enabled

## Important Notes

- Requires USWDS JavaScript to be loaded for live masking functionality
- Component relies on USWDS base classes from the `usa-` namespace
- Hint text should clearly indicate the expected format

### Implementation

```html
<!-- Phone Number Input Mask (Default) -->
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <label class="usa-label" for="input-mask-id-k4bemcxqq">
    Phone number
  </label>
  <span class="usa-hint" id="hint-id-k4bemcxqq">###-###-####</span>
  <input 
    type="text" 
    data-input-mask="" 
    class="usa-input" 
    id="input-mask-id-k4bemcxqq" 
    name="input-mask-id-k4bemcxqq" 
    data-mask-type="phone" 
    pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" 
    placeholder="___-___-____" 
    aria-describedby="hint-id-k4bemcxqq"
  >
</form>
```

```html
<!-- Social Security Number Input Mask -->
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <label class="usa-label" for="input-mask-ssn">
    Social Security Number
    <span aria-label="required">*</span>
  </label>
  <span class="usa-hint" id="hint-ssn">###-##-####</span>
  <input 
    type="text" 
    data-input-mask="" 
    class="usa-input" 
    id="input-mask-ssn" 
    name="ssn" 
    data-mask-type="ssn" 
    pattern="[0-9]{3}-[0-9]{2}-[0-9]{4}" 
    placeholder="___-__-____" 
    aria-describedby="hint-ssn"
    required
  >
</form>
```

```html
<!-- ZIP Code Input Mask -->
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <label class="usa-label" for="input-mask-zip">
    ZIP code
  </label>
  <span class="usa-hint" id="hint-zip">##### or #####-####</span>
  <input 
    type="text" 
    data-input-mask="" 
    class="usa-input" 
    id="input-mask-zip" 
    name="zip" 
    data-mask-type="zip" 
    placeholder="_____" 
    aria-describedby="hint-zip"
  >
</form>
```

```html
<!-- Required Field Variant -->
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <label class="usa-label" for="input-mask-required">
    Phone number
    <span aria-label="required">*</span>
  </label>
  <span class="usa-hint" id="hint-required">###-###-####</span>
  <input 
    type="text" 
    data-input-mask="" 
    class="usa-input" 
    id="input-mask-required" 
    name="phone-required" 
    data-mask-type="phone" 
    pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" 
    placeholder="___-___-____" 
    aria-describedby="hint-required"
    required
  >
</form>
```

```html
<!-- Disabled Variant -->
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <label class="usa-label" for="input-mask-disabled">
    Phone number
  </label>
  <span class="usa-hint" id="hint-disabled">###-###-####</span>
  <input 
    type="text" 
    data-input-mask="" 
    class="usa-input" 
    id="input-mask-disabled" 
    name="phone-disabled" 
    data-mask-type="phone" 
    pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" 
    placeholder="___-___-____" 
    aria-describedby="hint-disabled"
    disabled
  >
</form>
```

```html
<!-- With Google Analytics Tracking -->
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <label class="usa-label" for="input-mask-analytics">
    Phone number
  </label>
  <span class="usa-hint" id="hint-analytics">###-###-####</span>
  <input 
    type="text" 
    data-input-mask="" 
    class="usa-input" 
    id="input-mask-analytics" 
    name="phone-analytics" 
    data-mask-type="phone" 
    pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" 
    placeholder="___-___-____" 
    aria-describedby="hint-analytics"
    data-ga-category="Contact Form"
    data-ga-action="Phone Input"
    data-ga-label="Phone Number Entry"
  >
</form>
```

### Context

The Input Mask component is a USWDS-based utility for structured data capture in forms. It integrates with the Maryland Web Design System by inheriting standard form styling (usa-form, usa-label, usa-input, usa-hint) and works alongside other form components to ensure consistent, accessible data input across state applications.

---

## Input Prefix Suffix

*Components*

The Input Prefix Suffix component adds contextual information before or after an input field, such as currency symbols, units of measurement, or domain extensions. It solves the problem of providing clear input context and validation in a single visual unit. Use this when users need to understand the expected input format or unit type.

### Key Information

## Variants
- **Default**: Input with a single prefix indicator (e.g., "$" for currency)
- **With Suffix**: Input with a suffix indicator (e.g., "lbs" for weight)
- **Prefix and Suffix Combined**: Input with both prefix and suffix (e.g., "https://" prefix and ".gov" suffix for URLs)
- **Error State**: Input with prefix displaying error styling and error message
- **Disabled State**: Input with prefix that is disabled

## Key Class Names
- `usa-form`: Form container
- `usa-form-group`: Form group wrapper
- `usa-label`: Label element
- `usa-input`: The input field itself
- `usa-input-group`: Wrapper container for input with prefix/suffix
- `usa-input-prefix`: Container for prefix text (use `aria-hidden="true"`)

## Properties
- **label**: Label text for the input field (string)
- **prefix**: Text to display before the input, e.g., "$", "https://" (string)
- **suffix**: Text to display after the input, e.g., "lbs", ".gov" (string)
- **hint**: Optional hint text to help users (string)
- **placeholder**: Placeholder text inside the input (string)
- **disabled**: Disable the input if true (boolean)
- **error**: Show error state (boolean)
- **errorMessage**: Error message to display when error state is active (string)
- **enableAnalytics**: Enable or disable GA tracking attributes (boolean)
- **gaCategory**: Google Analytics event category (string)
- **gaAction**: Google Analytics event action (string)
- **gaLabel**: Google Analytics event label (string)

## Important Details
- The prefix element must have `aria-hidden="true"` to prevent screen reader repetition
- Input ID is auto-generated (e.g., "id-6otjads46ny")
- Input name follows pattern "input-id-{generatedId}"
- Supports Google Analytics tracking via optional GA attributes
- Supports ARIA attributes for accessibility

### Implementation

## Default: Currency Input with Prefix

```html
<form class="usa-form">
  <div class="usa-form-group">
    <label class="usa-label" for="id-6otjads46ny">
      Price
    </label>
    <div class="usa-input-group">
      <div class="usa-input-prefix" aria-hidden="true">
        $
      </div>
      <input class="usa-input" type="text" id="id-6otjads46ny" name="input-id-6otjads46ny" placeholder="0.00">
    </div>
  </div>
</form>
```

## With Suffix: Weight Input

```html
<form class="usa-form">
  <div class="usa-form-group">
    <label class="usa-label" for="id-weight">
      Weight
    </label>
    <div class="usa-input-group">
      <input class="usa-input" type="text" id="id-weight" name="input-weight" placeholder="">
      <div class="usa-input-suffix" aria-hidden="true">
        lbs
      </div>
    </div>
  </div>
</form>
```

## Combined Prefix and Suffix: URL Input

```html
<form class="usa-form">
  <div class="usa-form-group">
    <label class="usa-label" for="id-url">
      Website
    </label>
    <div class="usa-form-hint" id="hint-url">Enter your government website domain</div>
    <div class="usa-input-group">
      <div class="usa-input-prefix" aria-hidden="true">
        https://
      </div>
      <input class="usa-input" type="text" id="id-url" name="input-url" placeholder="" aria-describedby="hint-url">
      <div class="usa-input-suffix" aria-hidden="true">
        .gov
      </div>
    </div>
  </div>
</form>
```

## Error State

```html
<form class="usa-form">
  <div class="usa-form-group usa-form-group--error">
    <label class="usa-label" for="id-price-error">
      Price
    </label>
    <span class="usa-error-message" id="error-price" role="alert">
      Please enter a valid price
    </span>
    <div class="usa-input-group">
      <div class="usa-input-prefix" aria-hidden="true">
        $
      </div>
      <input class="usa-input usa-input--error" type="text" id="id-price-error" name="input-price-error" placeholder="" aria-describedby="error-price">
    </div>
  </div>
</form>
```

## Disabled State

```html
<form class="usa-form">
  <div class="usa-form-group">
    <label class="usa-label" for="id-price-disabled">
      Price
    </label>
    <div class="usa-input-group">
      <div class="usa-input-prefix" aria-hidden="true">
        $
      </div>
      <input class="usa-input" type="text" id="id-price-disabled" name="input-price-disabled" placeholder="0.00" disabled>
    </div>
  </div>
</form>
```

### Context

The Input Prefix Suffix component is part of the USWDS (U.S. Web Design System) component library and is implemented in MDWDS. It builds on the standard form input component by wrapping it with optional prefix/suffix containers, extending input functionality without requiring additional HTML form controls. This component is commonly used alongside other form elements like text inputs, selects, and checkboxes in multi-field forms.

---

## Language Selector

*Components*

The Language Selector provides a dropdown interface for users to select content in different languages. It supports both dropdown (for headers) and menu variants, with proper accessibility attributes and optional Google Analytics tracking. This component helps serve multilingual audiences by offering an intuitive language choice mechanism with native language names.

### Key Information

## Variants & Modifiers

- **Dropdown variant**: Primary variant for use in site headers
- **Small variant**: Compact size modifier via `size` property set to "small"
- **Menu variant**: Alternative for footers
- **With Additional Link**: Optional link for additional language resources (controlled via `includeAdditionalLink` boolean)
- **Custom Languages**: Supports custom language arrays with `{ native, english, lang, url }` structure
- **Maryland State Languages**: Preconfigured language set for Maryland

## CSS Class Names

- `usa-language-container`: Main container wrapper
- `usa-language__primary`: Primary language list
- `usa-language__primary-item`: Individual primary item
- `usa-button`: Button element styling
- `usa-language__link`: Language selector trigger button
- `usa-language__submenu`: Dropdown menu container
- `usa-language__submenu-item`: Individual submenu item
- `usa-accordion`: USWDS accordion class for functionality

## Required Attributes

- `aria-expanded`: Boolean attribute on trigger button (false when closed, true when open)
- `aria-controls`: Points to the ID of the submenu element it controls
- `lang` and `xml:lang`: Language code attributes on language name spans (e.g., `lang="ar"` for Arabic)
- `title`: Descriptive title on language links (e.g., "عربى | Arabic")

## Key Properties

- **triggerLabel**: Text displayed on the language selector button (default: "Languages")
- **languages**: Array of language objects with native name, English name, language code, and URL
- **size**: Controls variant size ("default" or "small")
- **includeAdditionalLink**: Boolean to show/hide additional resources link
- **additionalLinkText**: Custom text for additional resources link
- **additionalLinkUrl**: URL for additional resources link
- **ariaLabel**: ARIA label for accessibility
- **enableAnalytics**: Toggle Google Analytics tracking
- **gaCategory**, **gaAction**, **gaLabel**: Analytics event parameters

## Important Notes

- Requires USWDS JavaScript for accordion/dropdown functionality
- Provides full WCAG 2.1 AA accessibility compliance
- Language names should display in their native script/language (e.g., "عربى", "中文", "Español")
- Supports keyboard navigation when JS is loaded

### Implementation

```html
<div class="usa-language-container" id="id-3qpn7xnds3n">
  <ul class="usa-language__primary usa-accordion">
    <li class="usa-language__primary-item">
      <button 
        class="usa-button usa-language__link" 
        aria-expanded="false" 
        aria-controls="id-1uh9m8vxtmy">
        Languages
      </button>
      <ul 
        class="usa-language__submenu" 
        hidden 
        id="id-1uh9m8vxtmy">
        <li class="usa-language__submenu-item">
          <a 
            href="javascript:void(0)" 
            title="عربى | Arabic">
            <span lang="ar" xml:lang="ar">
              <strong>عربى</strong>
            </span>
          </a>
        </li>
        <!-- Additional language items follow same pattern -->
        <li class="usa-language__submenu-item">
          <a 
            href="javascript:void(0)" 
            title="[Language Name] | [English Name]">
            <span lang="[language-code]" xml:lang="[language-code]">
              <strong>[Native Language Name]</strong>
            </span>
          </a>
        </li>
      </ul>
    </li>
  </ul>
</div>
```

**Small Variant Structure** (same HTML structure, controlled via `size="small"` property that applies appropriate CSS)

**With Additional Link Variant** (adds footer link when `includeAdditionalLink` is true):
```html
<div class="usa-language-container">
  <!-- Primary selector as above -->
  <div class="usa-language__additional">
    <a href="[additionalLinkUrl]">[additionalLinkText]</a>
  </div>
</div>
```

**Key Structural Details:**
- Container element has unique ID for identification
- Primary list uses `usa-accordion` class for USWDS JavaScript integration
- Trigger button must have `aria-expanded` and `aria-controls` for accessibility
- Submenu must have `hidden` attribute and matching ID referenced in `aria-controls`
- Each language link includes `lang` and `xml:lang` attributes matching the language code
- Language names wrapped in `<strong>` tags for emphasis
- Title attribute provides fallback with format: "[Native Name] | [English Name]"

### Context

The Language Selector is a USWDS-based component that integrates into the Maryland Design System for multilingual site support. It typically appears in site headers or footers and works in conjunction with site navigation and regional settings to provide comprehensive accessibility for non-English speakers.

---

## Link

*Components*

The USWDS Link component provides multiple visual styles for various use cases including inline links, decorative links, and button-styled links. It solves the problem of creating consistent, accessible link experiences across different contexts. Use it for standard text navigation, emphasis, or strong calls-to-action.

### Key Information

**Link Types/Variants:**
- Inline Links: Standard text links used within paragraph content
- Decorative Links: Enhanced links for emphasis or external navigation
- Button Links: Links styled as buttons for strong call-to-action behavior

**Key CSS Classes:**
- `usa-link`: Base class for all link components

**Key Properties:**
- `label`: Text displayed for the link (string, required)
- `href`: Destination URL for the link (string, required)
- `external`: Boolean indicating if the link leaves the current site (optional)
- `target`: Controls link target behavior - supports "Current Tab" or "New Tab" (optional)

**ARIA & Accessibility:**
- Optional ARIA label can be added for improved screen reader context
- External links should be indicated via the `external` property
- Use appropriate `target` attributes when needed

### Implementation

```html
<!-- Inline Link (default variant) -->
<a class="usa-link" href="#">Inline link</a>
```

**Variants with modifiers:**
- Inline link with external indicator
- Decorative/enhanced link styling
- Button-styled link variant

**Props/Attributes:**
- `href`: URL destination (required)
- `label`: Link text content (required)
- `external`: Boolean to mark external links
- `target`: Set to indicate new tab behavior (e.g., "_blank")

### Context

The Link component is part of the USWDS component library and provides foundational navigation elements used throughout the MDWDS system. It composes with other content components and serves as the basis for navigation patterns, breadcrumbs, and call-to-action elements.

---

## LinkCollection

*Components*

The LinkCollection component presents a curated list of related links with an optional description and call-to-action. It helps organize and promote related content in a structured, scannable format. Use it when you need to group related links together with additional context and a "learn more" option.

### Key Information

## Variants
- **Default**: Basic link collection with title, description, and multiple links
- **With Item Descriptions**: Links include optional descriptions beneath each title
- **Without More Link**: Link collection without the optional "learn more" call-to-action link
- **Mixed Descriptions**: Some links have descriptions, others do not
- **Stacked**: Layout variation (appears to be for vertical stacking of items)

## CSS Class Names
- `maryland-link-collection`: Main container wrapper
- `maryland-link-collection__container`: Inner container for content
- `maryland-link-collection__header`: Header section containing title and description
- `maryland-link-collection__title`: Heading for the collection (required, should be H2)
- `maryland-link-collection__header-bottom`: Bottom section of header
- `maryland-link-collection__description`: Optional description text

## Props/Attributes
- **Title** (required): Clear, concise, descriptive heading text for the collection
- **Description** (optional): Brief message providing context for the links
- **More Link Text** (optional): Text for the optional "Learn more" link
- **More Link URL** (optional): URL for the optional "Learn more" link
- **Links** (required): Array of link objects with `title`, `url`, and optional `description` properties

## Important Facts
- The section uses `aria-labelledby` to reference the title ID for accessibility
- Each link collection should have a unique ID for the title element
- The component supports both simple links and links with descriptions

### Implementation

```html
<section class="maryland-link-collection" aria-labelledby="id-eqnz93yq2ah">
  <div class="maryland-link-collection__container">
    <div class="maryland-link-collection__header">
      <h2 class="maryland-link-collection__title" id="id-eqnz93yq2ah">
        Grow your career in Maryland
      </h2>
      
      <div class="maryland-link-collection__header-bottom">
        <div class="maryland-link-collection__description">
          Discover how Maryland works for you. Find a job, volunteer, or start your own business.
        </div>
      </div>
    </div>
    <!-- Links follow in list structure -->
    <!-- Optional "More/Learn more" link can be included -->
  </div>
</section>
```

### With Item Descriptions
```html
<section class="maryland-link-collection" aria-labelledby="collection-title">
  <div class="maryland-link-collection__container">
    <div class="maryland-link-collection__header">
      <h2 class="maryland-link-collection__title" id="collection-title">
        Collection Title
      </h2>
      <div class="maryland-link-collection__header-bottom">
        <div class="maryland-link-collection__description">
          Optional description providing context for the links.
        </div>
      </div>
    </div>
    <!-- Each link item can include a description beneath the title -->
  </div>
</section>
```

### Context

LinkCollection is a presentational component that helps organize related links with context. It integrates with the broader MDWDS system by providing a consistent way to highlight curated link sets across pages, often used alongside other content components to guide users through related topics or actions.

---

## Links

*Components*

Maryland Design System links provide enhanced styling and accessibility features for various link types, including standard links, document links, labelled links, external links, and skip links. Links solve the problem of providing consistent, accessible navigation throughout the design system with support for different contexts and use cases. Use links for navigation, file downloads, external site references, and keyboard-accessible skip navigation.

### Key Information

## Variants

- **default**: Standard links with Maryland styling
- **document**: Links for downloadable files with file type and size indicators
- **document-heading**: Document links within heading elements for listings and cards
- **document-card**: Document links in card context without hover underline
- **labelled**: Links with descriptive labels displayed above the link
- **skipnav**: Accessibility skip links for keyboard users to bypass navigation

## Modifiers & Controls

- **external**: Boolean flag to indicate the link navigates away from current site (adds external icon)
- **fileType**: File type indicator for document variants (PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, ZIP)
- **fileSize**: File size display for document variants
- **description**: Label text displayed above the link (labelled variant only)
- **target**: Where to open the link (current tab or new tab)
- **skipTo**: Navigation target for skip links ("main" or "sidebar")

## CSS Class Names

- `maryland-link`: Base link class applied to anchor elements

## Required Attributes

- `href`: Destination URL for the link (required)
- `label`: Text displayed for the link (required)

### Implementation

## Default Link
```html
<a class="maryland-link" href="#">
  Maryland Link
</a>
```

## Document Link
```html
<a class="maryland-link" href="#" data-file-type="PDF" data-file-size="2MB">
  FY2025 Annual Report - PDF 2MB
</a>
```

## Labelled Link
```html
<div>
  <label>Download</label>
  <a class="maryland-link" href="#">
    Maryland Link
  </a>
</div>
```

## External Link
```html
<a class="maryland-link" href="#" rel="external">
  Visit Maryland.gov 
  <svg aria-hidden="true"><!-- external icon --></svg>
</a>
```

## Skip Navigation Link
```html
<a class="maryland-link" href="#main">
  Skip to main content
</a>
```

### Context

Links are a fundamental navigation component in the Maryland Design System that compose with other components like navigation bars, cards, and lists. They provide consistent styling and accessibility features across the design system and support various use cases from standard navigation to document downloads and keyboard accessibility.

---

## Lists

*Components*

The USWDS List component provides consistent styling for ordered, unordered, and unstyled lists. It allows you to dynamically define list items and configure accessibility attributes (ARIA) for improved screen reader support. Use this component to create semantically correct, accessible lists with predefined USWDS styling.

### Key Information

## Variants
- **Unordered list**: Standard bulleted list (default)
- **Ordered list**: Numbered list
- **Unstyled list**: List without visual markers

## CSS Classes
- `usa-list`: Base class for styled lists (unordered and ordered variants)

## HTML Elements
- `<ul>`: For unordered lists
- `<ol>`: For ordered lists
- `<li>`: For list items (required children)

## Configurable Properties
- **variant**: Choose between "unordered", "ordered", or "unstyled" list types
- **items**: Array of strings representing list item content
- **ariaLabel**: Optional accessible name for the list
- **ariaDescribedBy**: Optional ID of element that describes the list

## Accessibility
- Lists support ARIA attributes (`aria-label`, `aria-describedby`) for improved screen reader support
- Semantic HTML elements (`<ul>`, `<ol>`, `<li>`) provide native accessibility

### Implementation

## Unordered List
```html
<ul class="usa-list">
  <li>List item 1</li>
  <li>List item 2</li>
  <li>List item 3</li>
</ul>
```

## Ordered List
```html
<ol class="usa-list">
  <li>List item 1</li>
  <li>List item 2</li>
  <li>List item 3</li>
</ol>
```

## Unstyled List
```html
<ul>
  <li>List item 1</li>
  <li>List item 2</li>
  <li>List item 3</li>
</ul>
```

## With Accessibility Attributes
```html
<ul class="usa-list" aria-label="Main navigation">
  <li>List item 1</li>
  <li>List item 2</li>
  <li>List item 3</li>
</ul>
```

```html
<ul class="usa-list" aria-describedby="list-description">
  <li>List item 1</li>
  <li>List item 2</li>
  <li>List item 3</li>
</ul>
```

### Context

The Lists component is a foundational USWDS element that provides consistent, accessible styling for list content throughout the MDWDS system. It integrates with the broader design system's typography and spacing utilities, and serves as a building block for navigation menus, step lists, and other list-based components.

---

## Memorable Date

*Components*

The Memorable Date component provides an accessible way to collect dates from users using three separate inputs: a month dropdown, day text field, and year text field. It solves the problem of date entry by breaking the input into semantic parts, reducing user errors and improving accessibility. Use this when you need users to enter dates like birth dates, application dates, or other specific calendar dates in a structured format.

### Key Information

## Variants and Configuration

- **Basic memorable date**: Month dropdown with day and year text inputs
- **With hint text**: Displays helper text (e.g., "For example: 4 28 1986")
- **With required field marking**: Indicates required status on the fieldset
- **Error states**: Shows error messages when validation fails
- **Disabled state**: All date input fields can be disabled
- **Analytics-enabled**: Supports Google Analytics tracking attributes (gaCategory, gaAction, gaLabel)

## CSS Class Names

- `usa-form`: Main form wrapper
- `usa-form--large`: Large form variant
- `usa-fieldset`: Fieldset container for the date group
- `usa-legend`: Legend text for the fieldset
- `usa-hint`: Hint text styling
- `usa-memorable-date`: Wrapper for the date input group
- `usa-form-group`: Individual form group wrapper
- `usa-form-group--month`: Month field-specific wrapper
- `usa-form-group--select`: Select dropdown wrapper
- `usa-label`: Label styling for each field (month, day, year)
- `usa-select`: Select dropdown element for month

## Key Attributes and Requirements

- **fieldset** with **legend**: Required for semantic grouping of date inputs
- **aria-describedby**: Links hint text to the fieldset (e.g., `aria-describedby="hint-id-..."`)
- **id** and **name** attributes**: Each input (month, day, year) requires unique id and name
- **label** elements: Each input field must have an associated label with `for` attribute
- **select** for month**: Month is a dropdown (select) element with options 1-12
- **type="text"** for day and year**: Day and year use text inputs (assumed from component description)

## Configuration Properties

- `label` (string): Legend text for the memorable date fieldset
- `hintText` (string): Optional hint text to help users format the date
- `required` (boolean): Whether the date fields are required
- `disabled` (boolean): Disable all date input fields
- `errorMessage` (string): Error message to display when validation fails
- `monthValue` (string): Default value for month (1-12)
- `dayValue` (string): Default value for day (1-31)
- `yearValue` (string): Default value for year (4 digits)
- `enableAnalytics` (boolean): Enable or disable GA tracking
- `gaCategory` (string): Google Analytics event category
- `gaAction` (string): Google Analytics event action
- `gaLabel` (string): Google Analytics event label

### Implementation

```html
<form class="usa-form usa-form--large">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">Date of birth</legend>
    <span class="usa-hint" id="hint-id-l4nmqjb4n7b">For example: 4 28 1986</span>
    
    <div class="usa-memorable-date">
      <div class="usa-form-group usa-form-group--month usa-form-group--select">
        <label class="usa-label" for="month-id-l4nmqjb4n7b">Month</label>
        <select class="usa-select" id="month-id-l4nmqjb4n7b" name="date-of-birth-month" aria-describedby="hint-id-l4nmqjb4n7b">
          <option value="">-Select-</option>
          <option value="1">01 - January</option>
          <option value="2">02 - February</option>
          <option value="3">03 - March</option>
          <option value="4">04 - April</option>
          <option value="5">05 - May</option>
          <option value="6">06 - June</option>
          <option value="7">07 - July</option>
          <option value="8">08 - August</option>
          <option value="9">09 - September</option>
          <option value="10">10 - October</option>
          <option value="11">11 - November</option>
          <option value="12">12 - December</option>
        </select>
      </div>

      <div class="usa-form-group usa-form-group--day">
        <label class="usa-label" for="day-id-l4nmqjb4n7b">Day</label>
        <input class="usa-input" id="day-id-l4nmqjb4n7b" type="text" name="date-of-birth-day" aria-describedby="hint-id-l4nmqjb4n7b" />
      </div>

      <div class="usa-form-group usa-form-group--year">
        <label class="usa-label" for="year-id-l4nmqjb4n7b">Year</label>
        <input class="usa-input" id="year-id-l4nmqjb4n7b" type="text" name="date-of-birth-year" aria-describedby="hint-id-l4nmqjb4n7b" />
      </div>
    </div>
  </fieldset>
</form>
```

## With Error State

```html
<form class="usa-form usa-form--large">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">Date of birth</legend>
    <span class="usa-hint" id="hint-id-error">For example: 4 28 1986</span>
    <span class="usa-error-message">Please enter a valid date</span>
    
    <div class="usa-memorable-date">
      <div class="usa-form-group usa-form-group--month usa-form-group--select">
        <label class="usa-label" for="month-id-error">Month</label>
        <select class="usa-select" id="month-id-error" name="date-of-birth-month" aria-describedby="hint-id-error">
          <option value="">-Select-</option>
          <!-- month options -->
        </select>
      </div>
      <!-- day and year inputs -->
    </div>
  </fieldset>
</form>
```

## With Required Marking

```html
<form class="usa-form usa-form--large">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">
      Date of birth
      <abbr title="required">*</abbr>
    </legend>
    <span class="usa-hint" id="hint-id-required">For example: 4 28 1986</span>
    
    <div class="usa-memorable-date">
      <!-- form groups with required attribute on inputs -->
    </div>
  </fieldset>
</form>
```

### Context

The Memorable Date component is part of the USWDS (U.S. Web Design System) component library adopted by MDWDS. It works in conjunction with form validation utilities and error messaging patterns. It composes with fieldsets, labels, and hints to create accessible date input forms that meet WCAG 2.1 AA standards.

---

## Modal

*Components*

The USWDS Modal is a fully accessible modal dialog component that works with or without JavaScript. It uses the native `<dialog>` element with focus trap, ESC close support, and keyboard accessibility. Use it to display important messages, confirmations, or user interactions that require focused attention.

### Key Information

## Key Information

**Core Features:**
- Works with or without JavaScript (CSS `:target` fallback for non-JS environments)
- Uses native `<dialog>` HTML element
- Full keyboard accessibility and screen reader support
- Focus trap and ESC key close functionality

**CSS Classes:**
- `usa-button` - Trigger button class
- `usa-modal` - Main modal container class
- `usa-modal--undefined` - Size variant (other options: `usa-modal--large`, default)

**HTML Attributes:**
- `data-open-modal=""` - Trigger button attribute to open modal
- `href="#id"` - Links trigger to modal by ID
- `aria-controls="id"` - Associates button with modal it controls
- `role="button"` - Semantic role on trigger link
- `aria-labelledby="id"` - Associates modal with its heading
- `aria-describedby="id"` - Associates modal with descriptive text
- `data-placeholder-for="id"` - Placeholder wrapper for modal

**Component Properties:**
- `heading` - Heading text shown in the modal (string)
- `description` - Descriptive body text inside modal (string)
- `triggerLabel` - Label text for modal trigger button (string)
- `confirmLabel` - Text for confirm/primary action button (string)
- `cancelLabel` - Text for cancel/secondary action button (string)
- `size` - Modal size options: Default or Large
- `forcedAction` - Boolean to force an action (prevents closing without interaction)

**JavaScript Requirement:**
Include `<script src="modal.js"></script>` once globally to enable enhanced JS behavior and full interactivity.

### Implementation

```html
<!-- Basic Modal Trigger Button -->
<a class="usa-button" data-open-modal="" href="#id-9292bhk5xrn" aria-controls="id-9292bhk5xrn" role="button">
  Open Modal
</a>

<!-- Modal Placeholder Container -->
<div 
  data-placeholder-for="id-9292bhk5xrn" 
  aria-hidden="true" 
  data-original-class="usa-modal usa-modal--undefined" 
  data-original-id="id-9292bhk5xrn" 
  data-original-aria-labelledby="id-9cjl94j5cr" 
  data-original-aria-describedby="id-ir1x8z396ph" 
  style="display: none;">
</div>

<!-- Full Modal Structure (for reference) -->
<div class="usa-modal" id="id-9292bhk5xrn" aria-labelledby="id-9cjl94j5cr" aria-describedby="id-ir1x8z396ph">
  <h2 id="id-9cjl94j5cr">Modal Heading</h2>
  <p id="id-ir1x8z396ph">Modal description text</p>
  <button>Confirm</button>
  <button>Cancel</button>
</div>

<!-- Large Modal Variant -->
<div class="usa-modal usa-modal--large" id="modal-id" aria-labelledby="modal-heading" aria-describedby="modal-description">
  <h2 id="modal-heading">Large Modal Heading</h2>
  <p id="modal-description">Large modal description text</p>
  <button>Confirm</button>
  <button>Cancel</button>
</div>
```

**JavaScript Initialization:**
```html
<script src="modal.js"></script>
```

This enables:
- Automatic focus trap on modal open
- ESC key to close modal
- Automatic focus return to trigger element on close
- Click outside to close (when not forced action)

### Context

The Modal component is part of the USWDS foundation and integrates with MDWDS for displaying critical information and user interactions. It composes with the Button component (`usa-button`) for triggers and works seamlessly with other layout components while maintaining accessibility standards across the design system.

---

## Navigation

*Components*

Navigation is a component that provides search functionality and navigation links for Maryland government websites. It includes a statewide search form and displays navigation items with optional Maryland.gov link integration in mobile view. This component serves as a primary navigation interface for state websites.

### Key Information

## Key Classes and Structure

- **Root container**: `maryland-search-form` — wraps the entire navigation component
- **Form element**: `maryland-search-form__form` — semantic search form with `role="search"`
- **Label**: `maryland-search-form__label` — hidden from view using `usa-sr-only` class
- **Widget container**: `maryland-search-form__widget` — wraps input and submit button
- **Input field**: `maryland-search-form__input` — search input with `type="text"` and `autocomplete="on"`
- **Submit button**: `maryland-search-form__submit` — search action button

## Properties

- **items**: Array property (default empty) — defines navigation menu items
- **showMarylandGovLink**: Boolean property (default False) — controls visibility of Maryland.gov link in mobile navigation

## Required Attributes

- Form requires `role="search"` for semantic HTML and accessibility
- Input requires `type="text"` and `autocomplete="on"`
- Labels should use `usa-sr-only` class for screen reader visibility when hidden
- Input should have a `placeholder` attribute (e.g., "How do I...")
- Input and label must be connected via `for` and `id` attributes

### Implementation

```html
<div class="maryland-search-form">
  <form role="search" class="maryland-search-form__form" action="/search" id="search-form-id">
    <label class="maryland-search-form__label usa-sr-only" for="search-input-id">Search</label>
    <div class="maryland-search-form__widget">
      <input 
        class="maryland-search-form__input" 
        type="text" 
        autocomplete="on" 
        name="q" 
        placeholder="How do I..." 
        id="search-input-id">
      <button type="submit" class="maryland-search-form__submit">
        Search
      </button>
    </div>
  </form>
</div>
```

## Navigation with Items and Maryland.gov Link

The component accepts an `items` array to populate navigation links and can display a Maryland.gov link in mobile view when `showMarylandGovLink` is set to true.

**Example with properties:**
- `items`: Array of navigation item objects
- `showMarylandGovLink`: Boolean (True to show Maryland.gov link on mobile)

### Context

The Navigation component provides essential site-wide search and navigation functionality within the MDWDS system. It typically appears at the top of pages and integrates with other header/banner components to create a cohesive statewide navigation experience for Maryland government websites.

---

## Pagination

*Components*

The Pagination component provides semantic, accessible, and responsive navigation for long datasets or multi-page content. It displays numbered page links with previous/next navigation arrows and optional ellipses to indicate non-visible pages. Use it when you need to help users navigate through multi-page datasets or paginated content.

### Key Information

## CSS Classes

- `.usa-pagination` - Main pagination container (requires `aria-label="Pagination"`)
- `.usa-pagination__list` - Unordered list wrapper
- `.usa-pagination__item` - Individual pagination item
- `.usa-pagination__arrow` - Modifier for previous/next arrow buttons
- `.usa-pagination__page-no` - Modifier for numbered page items
- `.usa-pagination__overflow` - Modifier for ellipsis items
- `.usa-pagination__link` - Link element within pagination
- `.usa-pagination__link-text` - Text wrapper for link text
- `.usa-pagination__previous-page` - Modifier for previous page link
- `.usa-pagination__button` - Button-style page number link

## Attributes & Properties

- `aria-label="Pagination"` - Required on the `<nav>` container
- `aria-label="Previous page"` - Required on previous navigation link
- `aria-label="Page N"` - Required on numbered page links (where N is the page number)
- `aria-label="ellipsis indicating non-visible pages"` - Required on ellipsis container items

## Variants

- **default** - Standard pagination with numbered pages
- **unbounded** - Alternative pagination style variant

## Properties

- `variant` - Choose pagination style variant (default or unbounded)
- `currentPage` - Current active page number (number)
- `totalPages` - Total number of available pages (number)
- `showEllipses` - Display ellipses between distant page numbers (boolean, default: false)
- `ariaLabelPagination` - Overrides the ARIA label for the pagination container (string)

### Implementation

```html
<nav class="usa-pagination" aria-label="Pagination">
  <ul class="usa-pagination__list">
    <!-- Previous page button -->
    <li class="usa-pagination__item usa-pagination__arrow">
      <a href="#" class="usa-pagination__link usa-pagination__previous-page" aria-label="Previous page">
        <span class="usa-pagination__link-text">Previous</span>
      </a>
    </li>
    
    <!-- Numbered page links -->
    <li class="usa-pagination__item usa-pagination__page-no">
      <a href="#" class="usa-pagination__button" aria-label="Page 1">1</a>
    </li>
    
    <!-- Ellipsis for non-visible pages -->
    <li class="usa-pagination__item usa-pagination__overflow" aria-label="ellipsis indicating non-visible pages">
      <span>…</span>
    </li>
    
    <!-- Additional page numbers (example showing pages 9, 10, 11) -->
    <li class="usa-pagination__item usa-pagination__page-no">
      <a href="#" class="usa-pagination__button" aria-label="Page 9">9</a>
    </li>
    <li class="usa-pagination__item usa-pagination__page-no">
      <a href="#" class="usa-pagination__button" aria-label="Page 10">10</a>
    </li>
    <li class="usa-pagination__item usa-pagination__page-no">
      <a href="#" class="usa-pagination__button" aria-label="Page 11">11</a>
    </li>
    
    <!-- Ellipsis for more non-visible pages -->
    <li class="usa-pagination__item usa-pagination__overflow" aria-label="ellipsis indicating non-visible pages">
      <span>…</span>
    </li>
    
    <!-- Final page number -->
    <li class="usa-pagination__item usa-pagination__page-no">
      <a href="#" class="usa-pagination__button" aria-label="Page 24">24</a>
    </li>
    
    <!-- Next page button -->
    <li class="usa-pagination__item usa-pagination__arrow">
      <a href="#" class="usa-pagination__link" aria-label="Next page">
        <span class="usa-pagination__link-text">Next</span>
      </a>
    </li>
  </ul>
</nav>
```

### Context

Pagination is a foundational USWDS component within the MDWDS system used to break up large datasets into manageable page views. It works alongside data tables and search results to provide users with clear navigation options when content spans multiple pages.

---

## Process List

*Components*

The Process List component visually guides users through a sequence of steps in a process. It is ideal for workflows such as multi-step forms, onboarding instructions, and application processes. Use this component when you need to display a linear progression of steps with titles and descriptions.

### Key Information

## Variants
- **Default**: Standard process list layout
- **No-text**: Process list without descriptive text
- **Custom-sizing**: Process list with customizable sizing

## CSS Classes
- `usa-process-list`: Container wrapper (ordered list)
- `usa-process-list__item`: Individual step item (list item)
- `usa-process-list__heading`: Step title/heading (h4 element)
- `usa-margin-top-05`: Utility class for top margin spacing on description text

## Structure
Each step is a list item containing:
- A heading using `usa-process-list__heading`
- Optional descriptive text with `usa-margin-top-05` utility class

## Properties
- **variant**: Allows selection between default, no-text, and custom-sizing styles
- **steps**: Array of step objects, each containing a title and optional text

### Implementation

```html
<ol class="usa-process-list">
  <li class="usa-process-list__item">
    <h4 class="usa-process-list__heading">Start a process</h4>
    <p class="usa-margin-top-05">Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi commodo, ipsum sed pharetra gravida, orci magna rhoncus neque.</p>
  </li>
  <li class="usa-process-list__item">
    <h4 class="usa-process-list__heading">Proceed to the second step</h4>
    <p class="usa-margin-top-05">Suspendisse id velit vitae ligula volutpat condimentum. Aliquam erat volutpat. Sed quis velit. Nulla facilisi.</p>
  </li>
  <li class="usa-process-list__item">
    <h4 class="usa-process-list__heading">Complete the step-by-step process</h4>
    <p class="usa-margin-top-05">Vivamus pharetra posuere sapien. Nulla libero. Nulla facilisi.</p>
  </li>
</ol>
```

**Notes:**
- Use semantic `<ol>` (ordered list) for the container
- Each step is wrapped in `<li>` with `usa-process-list__item` class
- Headings should use `<h4>` with `usa-process-list__heading` class
- Description text uses utility class `usa-margin-top-05` for consistent spacing
- Steps are displayed in a linear, numbered progression

### Context

The Process List component is part of the USWDS component library and fits into the MDWDS as a foundational component for guiding users through workflows. It composes with heading and utility spacing classes to create clear, accessible multi-step processes.

---

## Promo

*Components*

The Promo component visually highlights a single call-to-action link with a title, optional description, and link action. It's used to draw attention to important messages or feedback opportunities and comes in multiple style variants including plain, image-based, and illustration-based options.

### Key Information

## Variants & Modifiers

- **Plain Promo** (default): No image or background illustration, text-focused layout
- **Contained**: A bordered or contained variant of the plain promo style
- **Stacked**: Vertical stacking layout for the promo elements
- **Image Promo**: Includes an image alongside the content
- **Multiple Image Promo**: Multiple images can be included in the promo
- **Illustration Promo**: Uses a background illustration instead of a photograph

## Key CSS Classes

- `maryland-promo`: Base container class for the promo component
- `maryland-promo--plain`: Modifier class for plain promo style (no image)
- `maryland-promo__container`: Inner wrapper that contains the promo content
- `maryland-promo__row`: Row wrapper for layout
- `maryland-promo__title-container`: Container for the title element
- `maryland-promo__title`: The heading element (h2) with the promo title
- `maryland-promo__content-container`: Container for description and link content
- `maryland-promo__description`: Wrapper for the optional description text
- `maryland-promo_`: Link element class (prefix visible, full class name cut off in HTML)

## Required & Optional Attributes

- **Title** (required): Clear, concise, descriptive title relevant to the content
- **Description** (optional): Brief message providing context for the link
- **Link Title** (required): Call-to-action link text using active verbs
- **Link URL** (required): URL destination for the promo link
- **Promo style** (required selector): Choose between "No image", "With image", or "With background illustration"
- `aria-labelledby`: Links the section to the title element for accessibility
- `id`: Unique identifier on the title element for aria-labelledby reference

### Implementation

```html
<!-- Plain Promo (Default) -->
<section class="maryland-promo maryland-promo--plain" aria-labelledby="id-5fqrogjwoa3">
  <div class="maryland-promo__container">
    <div class="maryland-promo__row">
      <div class="maryland-promo__title-container">
        <h2 class="maryland-promo__title" id="id-5fqrogjwoa3">Your voice, your state: building a better tomorrow</h2>
      </div>
      <div class="maryland-promo__content-container">
        <div class="maryland-promo__description">
          <p>We're committed to serving you. Whether you're looking for help, have a suggestion, or want to share your thoughts, we want to hear from you.</p>
        </div>
        <a class="maryland-promo__link" href="/feedback">Share your feedback</a>
      </div>
    </div>
  </div>
</section>
```

**Key Structure Notes:**
- The `<section>` element uses `aria-labelledby` to reference the h2 title by its `id`
- Title must be wrapped in `maryland-promo__title-container` with the h2 having the class `maryland-promo__title`
- Content (description and link) must be in `maryland-promo__content-container`
- Description text is wrapped in `maryland-promo__description`
- Link element receives the promo-specific link styling class
- All content flows within `maryland-promo__row` and `maryland-promo__container`

### Context

The Promo component is a featured callout component within the MDWDS that emphasizes important messages or user actions. It integrates with the overall content hierarchy and typically appears as a prominent section on pages where user feedback or engagement is needed. The component supports multiple visual treatments (plain, image, illustration) to fit different content and design contexts.

---

## Prose

*Components*

The USWDS Prose component wraps blocks of running text and automatically applies USWDS typography styles to child elements. It is particularly useful for content from markdown or CMS systems where adding custom classes to individual elements is impractical, as well as for blog posts, articles, documentation, and user-generated content that require consistent automatic formatting.

### Key Information

## Key Class Names
- `usa-prose`: Main wrapper class that applies typography styling to direct-child elements

## Measure Tokens (Line Length Control)
The component supports measure tokens to control line length for optimal readability:
- `measure-1` to `measure-5`: 45-90 characters
- `measure-2` (66 characters): **Recommended** for extended reading
- `measure-6`: Shorter text blocks like captions

## Styled Child Elements
The `usa-prose` class automatically applies styling to:
- **Headings**: h1 through h6
- **Paragraphs**: p
- **Lists**: ul, ol, and child li elements
- **Blockquotes**: blockquote with cite
- **Tables**: table with thead, th, td, and caption
- **Figures**: figure with figcaption

## Accessibility Features
- Proper heading hierarchy maintained
- Focus indicators on interactive elements
- Semantic HTML structure preserved
- WCAG 2.1 AA compliance support

### Implementation

```html
<section class="usa-prose measure-2" id="prose-id-[unique-id]">
  <h2>Heading Level 2</h2>
  <p>Paragraph text content goes here.</p>
  
  <h3>Key Points</h3>
  <ul>
    <li>List item one</li>
    <li>List item two</li>
    <li>List item three</li>
  </ul>
  
  <blockquote>
    <p>Blockquote content</p>
    <cite>Source attribution</cite>
  </blockquote>
  
  <figure>
    <img src="image.jpg" alt="description" />
    <figcaption>Figure caption text</figcaption>
  </figure>
  
  <table>
    <thead>
      <tr>
        <th>Header 1</th>
        <th>Header 2</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Data 1</td>
        <td>Data 2</td>
      </tr>
    </tbody>
    <caption>Table caption</caption>
  </table>
</section>
```

## Measure Variants
The section wrapper can use any of the measure classes:
- `class="usa-prose measure-1"` (narrow)
- `class="usa-prose measure-2"` (recommended, ~66 characters)
- `class="usa-prose measure-3"`
- `class="usa-prose measure-4"`
- `class="usa-prose measure-5"` (wide)
- `class="usa-prose measure-6"` (short)

### Context

The Prose component is part of the USWDS component library integrated into MDWDS. It provides automatic typography styling for content blocks, making it especially useful when composing with content management systems or markdown-based content where applying individual styling classes is impractical.

---

## Radios

*Components*

Radio buttons allow users to select only one option from a list. The Maryland Design System offers both default and tile-style radio button variants. Use radio groups when you need mutually exclusive selections with clear accessibility attributes for screen reader compatibility.

### Key Information

## Variants
- **Default**: Standard radio button style
- **Tile**: Tile-style radio button presentation

## CSS Classes
- `usa-form`: Form wrapper
- `usa-fieldset`: Groups related radio inputs
- `usa-legend`: Legend text for the fieldset
- `usa-radio`: Container for each radio option
- `usa-radio__input`: The actual radio input element
- `usa-radio__label`: Label associated with the radio input

## Options Array Structure
Each radio option object supports:
- `label` (string): Display text for the radio option
- `value` (string): The value submitted when selected
- `description` (string, optional): Additional context text
- `checked` (boolean, optional): Pre-selected state
- `disabled` (boolean, optional): Disabled state

## Required Attributes
- `name`: Shared by all radio inputs in the group (required)
- `id`: Unique identifier for each radio input (auto-generated: `{name}-{label}-{index}`)
- `type="radio"`: HTML input type
- `for` attribute on labels: Links label to input via id

## Accessibility Attributes
- `aria-describedby` (optional but recommended): ID of element describing the group
- `aria-label` (optional): Screen reader override for the label

## Properties
- `variant`: "default" or "tile"
- `legend`: Fieldset legend text
- `name`: Shared name attribute for the radio group
- `options`: Array of radio option objects
- `ariaDescribedBy`: ID for aria-describedby attribute
- `ariaLabel`: Screen reader label override
- `enableAnalytics`: Enable/disable GA tracking (boolean)
- `gaCategory`: Google Analytics event category
- `gaAction`: Google Analytics event action
- `gaLabel`: Google Analytics event label

### Implementation

```html
<!-- Default Radio Button Group -->
<form class="usa-form">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">Select one historical figure</legend>
    
    <div class="usa-radio">
      <input 
        class="usa-radio__input" 
        id="historical-figures-sojourner-truth-0" 
        type="radio" 
        name="historical-figures" 
        value="sojourner-truth" 
        checked="">
      <label class="usa-radio__label" for="historical-figures-sojourner-truth-0">
        Sojourner Truth
      </label>
    </div>
    
    <div class="usa-radio">
      <input 
        class="usa-radio__input" 
        id="historical-figures-frederick-douglass-1" 
        type="radio" 
        name="historical-figures" 
        value="frederick-douglass">
      <label class="usa-radio__label" for="historical-figures-frederick-douglass-1">
        Frederick Douglass
      </label>
    </div>
    
    <div class="usa-radio">
      <input 
        class="usa-radio__input" 
        id="historical-figures-booker-t-washington-2" 
        type="radio" 
        name="historical-figures" 
        value="booker-t-washington">
      <label class="usa-radio__label" for="historical-figures-booker-t-washington-2">
        Booker T. Washington
      </label>
    </div>
    
    <div class="usa-radio">
      <input 
        class="usa-radio__input" 
        id="historical-figures-george-washington-carver-3" 
        type="radio" 
        name="historical-figures" 
        value="george-washington-carver">
      <label class="usa-radio__label" for="historical-figures-george-washington-carver-3">
        George Washington Carver
      </label>
    </div>
  </fieldset>
</form>
```

## Structure Notes
- Each radio input and its label are wrapped in a `div` with class `usa-radio`
- The `id` attribute on the input must match the `for` attribute on the label
- All inputs in a group share the same `name` attribute
- The `checked` attribute (empty string or present) marks the selected option
- The `usa-fieldset` and `usa-legend` structure the group semantically

### Context

Radio buttons are core form components in the MDWDS system, built on USWDS patterns. They compose with fieldsets and legends to create accessible, mutually-exclusive option groups and integrate with form layouts and validation patterns across the design system.

---

## Range Slider

*Components*

Range Slider allows users to select a numeric value by dragging a handle along a horizontal track. This component is ideal for choosing a value from a continuous or stepped numeric range, such as volume, brightness, or price. It supports customizable ranges (min, max), step values, accessibility attributes, and optional Google Analytics tracking.

### Key Information

## Variants & Options

The Range Slider component supports the following configuration options:

### Settings
- **label** (string): Visible label for the slider input
- **id** (string): Unique ID used to link label and input
- **name** (string): The name attribute of the slider input
- **min** (number): Minimum selectable value
- **max** (number): Maximum selectable value
- **step** (number): Step increment between values
- **value** (number): Default selected value

### Accessibility
- **ariaLabel** (string): Label for screen readers (optional if visible label is sufficient)
- **ariaDescribedBy** (string): ID of an element that provides additional descriptive context

### Analytics
- **enableAnalytics** (boolean): Enable Google Analytics tracking on this component
- **gaCategory** (string): GA event category (e.g., 'Slider')
- **gaAction** (string): GA event action (e.g., 'Adjust')
- **gaLabel** (string): GA event label (e.g., 'Price Range')

## CSS Class Names
- **usa-form**: Wrapper form class
- **usa-label**: Label styling
- **usa-range**: Primary class for the range input element

## Required Attributes
- `type="range"`: HTML5 range input type
- `min`: Minimum value attribute
- `max`: Maximum value attribute
- `step`: Step increment attribute
- `value`: Default value attribute

### Implementation

```html
<form class="usa-form">
  <label class="usa-label" for="usa-range">Range slider</label>
  <input id="usa-range" name="usa-range" class="usa-range" type="range" min="0" max="100" step="5" value="20">
</form>
```

## Component Structure

- **Form wrapper** (`.usa-form`): Contains the entire range slider component
- **Label** (`.usa-label`): Associated with input via `for` attribute matching the input `id`
- **Input** (`.usa-range`): The actual range control with required HTML5 attributes:
  - `type="range"`: Specifies this as a range input
  - `min="0"`: Minimum selectable value
  - `max="100"`: Maximum selectable value
  - `step="5"`: Increment between values
  - `value="20"`: Default selected value
  - `id`: Must match the label's `for` attribute
  - `name`: Form field name for submission

### Context

The Range Slider is a USWDS component that provides an accessible, HTML5-native input control for numeric value selection. It integrates with the Maryland Web Design System form styling through the usa-form and usa-label classes, and supports optional Google Analytics event tracking for monitoring user interactions.

---

## Search

*Components*

The Search component provides a reusable form interface for site-wide search functionality. It supports multiple display variants (pop-out, static, hero, and results) and can be configured with keywords and scope parameters. Use this component to enable users to search across Maryland government sites or specific subdomains.

### Key Information

## Variants
- **Pop Out**: Hidden form that toggles open via a button (aria-expanded controls visibility)
- **Static**: Permanently visible search form
- **Hero**: Large search form with scope selection dropdown
- **Results**: Search results display with sorting and result items

## CSS Class Names
- `maryland-search-form`: Main container
- `maryland-search-form--toggleable`: Modifier for pop-out/toggle behavior
- `maryland-search-form__form`: Form element with `role="search"`
- `maryland-search-form__widget`: Input wrapper
- `maryland-search-form__input`: Text input field
- `maryland-search-form__submit`: Submit button
- `maryland-search-form__toggle`: Toggle button for pop-out variant

## Required Attributes
- `role="search"` on form element
- `aria-label` on submit and toggle buttons
- `aria-expanded` on toggle button (indicates open/closed state)
- `aria-controls` on toggle button (references form ID)
- `autocomplete="on"` on input for browser-supported suggestions
- Unique `id` attributes on form and input for accessibility linking

## Important Facts
- Component uses a hidden attribute to toggle visibility in pop-out mode
- Input has `type="text"` and `name="q"` for search queries
- Toggle button uses `aria-expanded="false"` when form is hidden
- Form action can be customized (currently set to "#")
- Supports `keywords` and `scope` properties for filtering searches
- Results variant shows result count, timestamp, and individual result items

### Implementation

```html
<!-- Pop Out / Toggleable Variant -->
<div class="maryland-search-form maryland-search-form--toggleable">
  <form class="maryland-search-form__form" role="search" action="#" hidden="" id="id-e7h34o2celc">
    <label class="usa-sr-only" for="id-axg80xk8sko">Search</label>
    <div class="maryland-search-form__widget">
      <input class="maryland-search-form__input" type="text" name="q" autocomplete="on" id="id-axg80xk8sko">
      <button type="submit" aria-label="Submit Search" class="maryland-search-form__submit"></button>
    </div>
  </form>
  <button class="maryland-search-form__toggle" aria-label="Open header search" aria-expanded="false" aria-controls="id-e7h34o2celc"></button>
</div>
```

```html
<!-- Static Variant (form always visible, no toggle button) -->
<div class="maryland-search-form">
  <form class="maryland-search-form__form" role="search" action="#" id="search-form-static">
    <label class="usa-sr-only" for="search-input-static">Search</label>
    <div class="maryland-search-form__widget">
      <input class="maryland-search-form__input" type="text" name="q" autocomplete="on" id="search-input-static">
      <button type="submit" aria-label="Submit Search" class="maryland-search-form__submit"></button>
    </div>
  </form>
</div>
```

```html
<!-- Hero Variant (with scope dropdown) -->
<div class="maryland-search-form">
  <form class="maryland-search-form__form" role="search" action="#">
    <label class="usa-sr-only" for="search-input-hero">Search</label>
    <div class="maryland-search-form__widget">
      <input class="maryland-search-form__input" type="text" name="q" autocomplete="on" id="search-input-hero" placeholder="Search">
      <select class="maryland-search-form__scope">
        <option>Select a search scope</option>
        <option>subdomain.maryland.gov</option>
        <option>All Maryland.gov sites</option>
      </select>
      <button type="submit" aria-label="Submit Search" class="maryland-search-form__submit"></button>
    </div>
  </form>
</div>
```

### Context

The Search component is a foundational UI element in the MDWDS that integrates with Maryland government sites to enable site-wide and cross-domain search functionality. It can be embedded in headers (as a toggleable pop-out), used as a persistent search interface, or displayed prominently as a hero element on search landing pages.

---

## Search

*Components*

The Maryland Design System Search component allows users to perform queries across site content or datasets. It provides multiple size variants (default, big, small), Spanish localization support, optional Google Analytics tracking, and custom icon support. Use this component when you need a search input interface with accessibility compliance and optional analytics capabilities.

### Key Information

## Variants
- **Size variants**: `default`, `big`, `small`
- **Language support**: `english`, `spanish`

## Key Properties
- **variant**: Select the size of the search bar (string) — options: default, big, small
- **language**: Language for screen reader text and button label (string) — options: english, spanish
- **placeholder**: Placeholder text inside the search input field (string)
- **buttonText**: Visible text on the submit button; ignored in Spanish mode (string)
- **id**: ID for the search input, used with the label (string)
- **name**: The name attribute of the search input (string)
- **iconUrl**: Custom icon URL for the search button (string)

## Accessibility
- **ariaDescribedBy**: ID of an element describing the input field (optional, string)

## Analytics (Optional)
- **enableAnalytics**: Enable or disable GA tracking attributes on the input (boolean; default: False)
- **gaCategory**: Google Analytics event category (string)
- **gaAction**: Google Analytics event action (string)
- **gaLabel**: Google Analytics event label (string)

## CSS Classes
- `usa-search`: Main search form container
- `usa-sr-only`: Screen reader only label
- `usa-search__input`: Input field class
- `usa-input`: General input styling
- `usa-button`: Submit button class
- `usa-search__submit-text`: Text label inside submit button
- `usa-search__submit-icon`: Icon image element inside submit button

### Implementation

```html
<section aria-label="Search component">
  <form class="usa-search" role="search">
    <label class="usa-sr-only" for="search-field">Search</label>
    <input 
      class="usa-search__input usa-input" 
      id="search-field" 
      type="search" 
      name="search" 
      placeholder="Search"
    >
    <button class="usa-button" type="submit">
      <span class="usa-search__submit-text">Search</span>
      <img 
        src="https://cdn.maryland.gov/mdwds/latest/img/search--white.svg" 
        class="usa-search__submit-icon" 
        alt="Search"
      >
    </button>
  </form>
</section>
```

## Structure Notes
- The form element uses `role="search"` for semantic HTML and accessibility
- The label is marked with `usa-sr-only` to hide it visually while keeping it available to screen readers
- The input field combines both `usa-search__input` and `usa-input` classes
- The submit button contains both text (`usa-search__submit-text`) and an icon (`usa-search__submit-icon`)
- The form wrapper has `aria-label="Search component"` for screen reader context

### Context

The Search component is a USWDS-based component that integrates into the Maryland Design System for site-wide search functionality. It composes with standard form elements and button components while adding search-specific styling, accessibility labels, and optional analytics tracking attributes.

---

## Select

*Components*

The Select component is a native HTML `<select>` element enhanced with consistent Maryland Design System visual styling. It allows users to choose a single option from a predefined list and supports accessibility, mobile responsiveness, and optional Google Analytics tracking out-of-the-box.

### Key Information

## Variants
- Standard dropdown select with placeholder option

## CSS Classes
- `usa-form` — wrapper form element
- `usa-label` — label styling for form inputs
- `usa-select` — main select element styling

## Required Attributes
- `id` — associates the select element with its label via `for` attribute
- `name` — name attribute for form submission
- `for` (on label) — must match the select's `id`

## Options Structure
- Options configured as array of objects with:
  - `label` — displayed option text
  - `value` — submitted form value
  - `selected?` — optional, marks option as pre-selected
  - `disabled?` — optional, disables individual options

## Accessibility
- Screen reader-friendly labeling via label-select association
- `ariaDescribedBy` prop supports optional element ID for additional descriptions

## Analytics
- `enableAnalytics` — boolean to enable/disable GA tracking
- `gaCategory` — GA event category string
- `gaAction` — GA event action string
- `gaLabel` — GA event label string

## Props Summary
- `label` (string) — visible label text
- `id` (string) — select element ID
- `name` (string) — form submission name
- `placeholder` (string) — first option prompt text
- `options` (array) — list of option objects
- `ariaDescribedBy` (string) — ID of describing element
- `enableAnalytics` (boolean) — GA tracking toggle
- `gaCategory` (string) — analytics category
- `gaAction` (string) — analytics action
- `gaLabel` (string) — analytics label

### Implementation

```html
<form class="usa-form">
  <label class="usa-label" for="options">Dropdown label</label>
  <select class="usa-select" name="options" id="options">
    <option value="">- Select -</option>
    <option value="value1">Option A</option>
    <option value="value2">Option B</option>
    <option value="value3">Option C</option>
  </select>
</form>
```

## Structure Notes
- Label must precede the select element
- Label's `for` attribute must match select's `id`
- First option can serve as placeholder with empty value
- All options rendered as standard HTML `<option>` elements
- Select wrapped in `usa-form` class container

### Context

The Select component extends native HTML form elements with MDWDS styling and follows U.S. Web Design System (USWDS) patterns. It composes with form labels and integrates with optional accessibility descriptors and analytics tracking, making it suitable for use within larger form layouts and templates across the Maryland Design System.

---

## Side Navigation

*Components*

Side Navigation is a hierarchical, vertical navigation component designed to be placed at the side of a page. It provides a structured menu for organizing and displaying page sections and content hierarchy. Use it to help users navigate through nested content levels and understand the current page context within a site structure.

### Key Information

**Core Class Names:**
- `maryland-sidenav` - Main container element
- `maryland-sidenav__toggle` - Toggle button for collapsing/expanding (mobile)
- `maryland-sidenav__title` - Navigation section title
- `maryland-sidenav__list` - List container for menu items
- `maryland-sidenav__list--level-1` - Level modifier for nested lists
- `maryland-sidenav__item` - Individual menu item
- `maryland-sidenav__item--level-1` - Level modifier for items
- `maryland-sidenav__link` - Menu link/text
- `maryland-sidenav__link--level-1` - Level modifier for links
- `is-open` - State class indicating expanded/open state
- `usa-sr-only` - Screen reader only text class

**ARIA Attributes:**
- `aria-labelledby` - Links nav to its title element ID
- `aria-controls` - Button controls which list to expand/collapse
- `aria-current="page"` - Marks the current page link

**Variants:**
- Default: Full sidenav display with hierarchy
- In Sidebar: Sidenav rendered within a sidebar context alongside page content
- Show as top-level page: Boolean toggle to display navigation as if current page is top-level (no menu parent)

### Implementation

```html
<nav class="maryland-sidenav" aria-labelledby="id-i7hfxybfk6">
  <button class="maryland-sidenav__toggle" aria-controls="id-jrxhk5esar">
    <span class="usa-sr-only"></span>
    <h2 class="maryland-sidenav__title" id="id-i7hfxybfk6">Section menu</h2>
  </button>
  <ul class="maryland-sidenav__list maryland-sidenav__list--level-1 is-open" id="id-jrxhk5esar">
    <li class="maryland-sidenav__item maryland-sidenav__item--level-1">
      <span class="maryland-sidenav__link maryland-sidenav__link--level-1" aria-current="page">Your Government</span>
      <ul class="maryland-sidenav__list">
        <li class="maryland-sidenav__item">
          <a href="#" class="maryland-sidenav__link">State government</a>
        </li>
        <li class="maryland-sidenav__item">
          <a href="#" class="maryland-sidenav__link">Elections and voting</a>
        </li>
        <li class="maryland-sidenav__item">
          <a href="#" class="maryland-sidenav__link">State agencies and departments</a>
        </li>
      </ul>
    </li>
  </ul>
</nav>
```

**Structure Notes:**
- Root `<nav>` element with `maryland-sidenav` class
- Toggle button controls visibility of the list via `aria-controls` attribute
- Main `<ul>` list with level modifier classes for styling nested levels
- List items use `<li>` with `maryland-sidenav__item` class
- Links can be `<a>` or `<span>` elements with `maryland-sidenav__link` class
- Current page uses `aria-current="page"` attribute
- `is-open` state class indicates expanded state
- Nested lists follow the same structure with appropriate level modifiers

### Context

Side Navigation is a core navigation component in MDWDS that provides hierarchical organization of site content. It typically pairs with page layouts and header components to create complete page navigation patterns, allowing users to understand site structure and move between related content sections.

---

## Side Navigation

*Components*

The Side Navigation component provides a hierarchical, accessible way to guide users through complex website sections. It supports 1–3 levels of navigation hierarchy with current page highlighting and semantic nested list structure. Use this component to organize multi-level site navigation with clear visual hierarchy and accessibility support.

### Key Information

## Variants
- **Single-level**: Basic flat list of navigation items
- **Two-level**: Parent items with nested children
- **Three-level**: Parent items with nested children and grandchildren

## CSS Class Names
- `usa-sidenav` — Main navigation container
- `usa-sidenav__item` — Individual navigation list item
- `usa-sidenav__sublist` — Nested child/grandchild list container
- `usa-current` — Applied to links representing the current active page

## Required Attributes
- `aria-label` — Custom label for the nav element (defaults to 'Side navigation')
- `aria-describedby` — Optional ID of element that describes the navigation region

## Key Properties
- **currentLabel** — Label for the current active page
- **parentLabels** — Array of parent link labels (optional)
- **childLabels** — Array of child links (used for two- or three-level variants)
- **grandchildLabels** — Array of grandchild links (used only for three-level variant)
- **ariaLabel** — Customizable aria-label for the nav element
- **ariaDescribedBy** — Optional aria-describedby attribute for additional description

## Important Facts
- Supports semantic structure using properly nested `<ul>` and `<li>` elements
- The `usa-current` class marks the page the user is currently viewing
- Supports up to 3 levels of hierarchy
- Fully accessible with ARIA labels and semantic HTML

### Implementation

```html
<!-- Three-level Side Navigation Example -->
<nav aria-label="Side navigation">
  <ul class="usa-sidenav">
    <li class="usa-sidenav__item">
      <a href="#" class="usa-current">Current page</a>
      <ul class="usa-sidenav__sublist">
        <li class="usa-sidenav__item">
          <a href="#">Child link A</a>
          <ul class="usa-sidenav__sublist">
            <li class="usa-sidenav__item">
              <a href="#">Grandchild link A</a>
            </li>
            <li class="usa-sidenav__item">
              <a href="#" class="usa-current">Grandchild link B</a>
            </li>
            <li class="usa-sidenav__item">
              <a href="#">Grandchild link C</a>
            </li>
          </ul>
        </li>
        <li class="usa-sidenav__item">
          <a href="#">Child link B</a>
        </li>
        <li class="usa-sidenav__item">
          <a href="#">Child link C</a>
        </li>
      </ul>
    </li>
  </ul>
</nav>
```

## Two-level Variant
```html
<nav aria-label="Side navigation">
  <ul class="usa-sidenav">
    <li class="usa-sidenav__item">
      <a href="#" class="usa-current">Current page</a>
      <ul class="usa-sidenav__sublist">
        <li class="usa-sidenav__item">
          <a href="#">Child link A</a>
        </li>
        <li class="usa-sidenav__item">
          <a href="#">Child link B</a>
        </li>
      </ul>
    </li>
  </ul>
</nav>
```

## Single-level Variant
```html
<nav aria-label="Side navigation">
  <ul class="usa-sidenav">
    <li class="usa-sidenav__item">
      <a href="#" class="usa-current">Current page</a>
    </li>
    <li class="usa-sidenav__item">
      <a href="#">Other page</a>
    </li>
  </ul>
</nav>
```

## With Custom aria-label and aria-describedby
```html
<nav aria-label="Main site sections" aria-describedby="nav-description">
  <ul class="usa-sidenav">
    <li class="usa-sidenav__item">
      <a href="#" class="usa-current">Current page</a>
    </li>
  </ul>
</nav>
<p id="nav-description">Use this navigation to explore main sections of the website.</p>
```

### Context

Side Navigation is a USWDS component integrated into MDWDS for organizing hierarchical site navigation. It composes well with page layouts and header components to provide users with a clear navigation path through complex content areas. The component follows USWDS standards for accessibility and semantic structure.

---

## Site Alert

*Components*

The Site Alert component provides a consistent way to inform users of critical site-wide information. It supports multiple variants (info, warning, emergency, success) that reflect the importance and urgency of the message. Use it to communicate important site-wide notices, emergencies, or status updates with full accessibility customization.

### Key Information

## Variants
- **info** (default): General messages and updates
- **warning**: Important non-emergency warnings
- **emergency**: Emergency alerts requiring immediate attention
- **success**: Confirmation or success notifications

## CSS Classes
- `usa-site-alert`: Main wrapper element
- `usa-site-alert--info`: Modifier for info variant (default)
- `usa-site-alert--warning`: Modifier for warning variant
- `usa-site-alert--emergency`: Modifier for emergency variant
- `usa-site-alert--success`: Modifier for success variant
- `usa-alert`: Container for alert content
- `usa-alert__body`: Wrapper for alert heading and text
- `usa-alert__heading`: The alert heading element (h3)
- `usa-alert__text`: The alert message content

## Customization Options
- **variant**: Style variant of the alert box (info, warning, emergency, success)
- **heading**: The heading text inside the alert
- **content**: The main message content of the alert
- **role**: ARIA role for screen readers (can be left blank for default, or set to `status` or `alert`)
- **ariaLive**: ARIA live region behavior (polite, assertive, off)
- **ariaLabel**: Label for the entire alert region, read by screen readers

## Key Attributes
- Supports full accessibility customization including ARIA roles and live regions
- Based on USWDS Site Alert component

### Implementation

```html
<!-- Info variant (default) -->
<section class="usa-site-alert usa-site-alert--info">
  <div class="usa-alert">
    <div class="usa-alert__body">
      <h3 class="usa-alert__heading">This is a site alert</h3>
      <p class="usa-alert__text">
        Here is some helpful information for your users.
      </p>
    </div>
  </div>
</section>
```

## Variants with ARIA Attributes

```html
<!-- With status role and polite live region -->
<section class="usa-site-alert usa-site-alert--info" role="status" aria-live="polite" aria-label="Alert">
  <div class="usa-alert">
    <div class="usa-alert__body">
      <h3 class="usa-alert__heading">This is a site alert</h3>
      <p class="usa-alert__text">
        Here is some helpful information for your users.
      </p>
    </div>
  </div>
</section>
```

```html
<!-- Warning variant -->
<section class="usa-site-alert usa-site-alert--warning">
  <div class="usa-alert">
    <div class="usa-alert__body">
      <h3 class="usa-alert__heading">Warning Alert</h3>
      <p class="usa-alert__text">
        This is an important non-emergency warning message.
      </p>
    </div>
  </div>
</section>
```

```html
<!-- Emergency variant with alert role -->
<section class="usa-site-alert usa-site-alert--emergency" role="alert" aria-live="assertive">
  <div class="usa-alert">
    <div class="usa-alert__body">
      <h3 class="usa-alert__heading">Emergency Alert</h3>
      <p class="usa-alert__text">
        Emergency alert requiring immediate attention.
      </p>
    </div>
  </div>
</section>
```

```html
<!-- Success variant -->
<section class="usa-site-alert usa-site-alert--success">
  <div class="usa-alert">
    <div class="usa-alert__body">
      <h3 class="usa-alert__heading">Success</h3>
      <p class="usa-alert__text">
        Confirmation or success notification message.
      </p>
    </div>
  </div>
</section>
```

### Context

The Site Alert component is a USWDS-based component that integrates into the Maryland Web Design System for communicating critical site-wide information. It composes with standard semantic HTML elements and ARIA attributes to ensure accessibility compliance, and can be paired with other alert components or messaging systems depending on the scope of the notification.

---

## Social Media

*Components*

A list of linked social media icons that provides quick access to an agency or entity's social media profiles. This component displays icon links for common platforms like Facebook, X (formerly Twitter), YouTube, Instagram, LinkedIn, and Flickr with screen reader-friendly text. Use this component in footers, sidebars, or contact sections to direct users to official social media channels.

### Key Information

## Variants & Modifiers

The Social Media component uses a modifier class system to display different platform icons:

- `maryland-social__link--facebook` - Facebook icon link
- `maryland-social__link--x` - X (Twitter) icon link
- `maryland-social__link--youtube` - YouTube icon link
- `maryland-social__link--instagram` - Instagram icon link
- `maryland-social__link--linkedin` - LinkedIn icon link
- `maryland-social__link--flickr` - Flickr icon link

## CSS Class Names

- `maryland-social` - Main container list element (unordered list)
- `maryland-social__link` - Individual social media link element (applies base link styling)
- `maryland-social__link--[platform]` - Platform-specific modifier that applies the corresponding icon

## Required Attributes

- Screen reader text wrapper: `<span class="usa-sr-only">` containing descriptive text in format "Connect with [Agency Name] on [platform].com (external link)"
- Link href attribute pointing to the social media profile URL

## Important Facts

- The component uses BEM (Block Element Modifier) naming convention
- Each link should have associated screen reader text to describe the link destination
- Icons are typically applied via CSS background-image or pseudo-elements
- Links should be accessible with proper ARIA labels via screen reader text

### Implementation

```html
<ul class="maryland-social">
  <li>
    <a href="#!" class="maryland-social__link maryland-social__link--facebook">
      <span class="usa-sr-only">Connect with Agency Title on facebook.com (external link)</span>
    </a>
  </li>
  <li>
    <a href="#!" class="maryland-social__link maryland-social__link--x">
      <span class="usa-sr-only">Connect with Agency Title on x.com (external link)</span>
    </a>
  </li>
  <li>
    <a href="#!" class="maryland-social__link maryland-social__link--youtube">
      <span class="usa-sr-only">Connect with Agency Title on youtube.com (external link)</span>
    </a>
  </li>
  <li>
    <a href="#!" class="maryland-social__link maryland-social__link--instagram">
      <span class="usa-sr-only">Connect with Agency Title on instagram.com (external link)</span>
    </a>
  </li>
  <li>
    <a href="#!" class="maryland-social__link maryland-social__link--linkedin">
      <span class="usa-sr-only">Connect with Agency Title on linkedin.com (external link)</span>
    </a>
  </li>
  <li>
    <a href="#!" class="maryland-social__link maryland-social__link--flickr">
      <span class="usa-sr-only">Connect with Agency Title on flickr.com (external link)</span>
    </a>
  </li>
</ul>
```

### Context

The Social Media component is a utility component that integrates into the MDWDS system to provide consistent styling for social media links across Maryland government websites. It complements the usa-sr-only class from USWDS for accessibility and follows the Maryland design system's BEM naming conventions.

---

## Statewide Banner

*Components*

The Statewide Banner is a required component that communicates to users that a website or application is a secure and official Maryland government site. It displays key information prominently without being visually distracting. The banner must be positioned at the top of all pages in any Maryland government website or application.

### Key Information

## Key Information

- **Component Tag**: `maryland-statewide-banner` (web component)
- **Required**: Yes — must appear on all pages of Maryland government sites and applications
- **Positioning**: Must be placed at the top of all pages
- **CDN Version**: 0.44.0

## CSS Classes
- `maryland-alert` — Alert container class (used in noscript fallback)
- `maryland-alert--warning` — Warning alert variant
- `maryland-alert__body` — Alert body container
- `maryland-alert__heading` — Alert heading
- `maryland-alert__text` — Alert text content

## Important Features
- The component is a custom web component (`<maryland-statewide-banner>`)
- Includes a noscript fallback that displays a warning alert when JavaScript is disabled
- The fallback uses the Maryland Alert component styling classes
- Communicates official government status and security information
- JavaScript is required for full functionality

## No-Script Fallback
When JavaScript is disabled, a fallback alert appears with the message "JavaScript is required to use content on this page. Please enable JavaScript in your browser." This uses the `maryland-alert--warning` variant.

### Implementation

```html
<maryland-statewide-banner>
  <noscript>
    <link rel="stylesheet" href="https://cdn.maryland.gov/mdwds/latest/css/mdwds.min.css">
    <div class="maryland-alert maryland-alert--warning">
      <div class="maryland-alert__body">
        <h4 class="maryland-alert__heading">JavaScript Required</h4>
        <p class="maryland-alert__text">
          JavaScript is required to use content on this page. Please enable
          JavaScript in your browser.
        </p>
      </div>
    </div>
  </noscript>
</maryland-statewide-banner>
```

## Usage Notes
- Place this component at the very top of your page, before other page content
- The component is self-contained and does not require additional initialization beyond including the MDWDS CSS and JavaScript files
- The noscript fallback provides a degraded but functional experience for users without JavaScript enabled
- Link the MDWDS stylesheet in the noscript block to ensure the fallback alert displays correctly

### Context

The Statewide Banner is a foundational component in the Maryland Web Design System that serves as a standardized header element for all Maryland government digital properties. It works in conjunction with other MDWDS components and uses the same Alert component styling (`maryland-alert` classes) for its JavaScript-disabled fallback, ensuring visual and behavioral consistency across the design system.

---

## Statewide Footer

*Components*

The Statewide Footer is a standardized, accessible footer component that provides consistent navigation and information across all Maryland.gov websites and applications. It reinforces public trust, improves navigation, and aligns with Maryland's digital service standards and the U.S. Web Design System (USWDS). This is a zero-configuration, plug-and-play component best used as a site-wide footer element.

### Key Information

## Key Features
- **Zero Configuration**: No configuration or data bindings required — fully self-contained
- **Responsive Design**: Mobile-first responsive layout that adapts to all screen sizes
- **Structured Content**: Includes grouped links to:
  - Maryland state services
  - Government portals
  - Privacy policies
  - Emergency alerts and notifications
- **Accessibility**: Built-in accessibility features and ARIA support
- **Built-in Styling**: Styled using MDWDS design tokens and CSS; no additional stylesheet required
- **Web Component**: Implemented as a custom HTML element (`<maryland-statewide-footer>`)

## Usage Notes
- This component is **non-editable** in most use cases
- Intended to be used as-is without modification
- If customization is needed, MDDS recommends using scoped CSS or submitting a feature request
- Best delivered via CDN to ensure all downstream applications stay up-to-date with latest layout, links, and accessibility improvements
- No manual deployments required when using CDN version

## CSS Class Names
While the component itself uses the custom element `maryland-statewide-footer`, all internal styling is encapsulated within the web component using MDWDS design tokens.

### Implementation

```html
<!-- Recommended: CDN-hosted version (always up-to-date) -->
<script type="module" src="https://cdn.maryland.gov/mdwds/0.44.0/components/maryland-statewide-footer.js"></script>
<maryland-statewide-footer></maryland-statewide-footer>
```

## Component Markup Structure

```html
<maryland-statewide-footer></maryland-statewide-footer>
```

The `maryland-statewide-footer` is a self-contained web component. It renders its own internal footer structure with:
- Grouped navigation links to Maryland state services
- Government portals
- Privacy and legal policies
- Emergency alert sections
- Responsive layout with mobile-first design

All styling is encapsulated within the shadow DOM of the web component — no external CSS classes need to be applied.

### Context

The Statewide Footer is a foundational component in the MDWDS system designed to provide a consistent, accessible footer across all Maryland government digital services. It aligns with the U.S. Web Design System (USWDS) standards and is delivered as a web component for easy integration with minimal configuration, ensuring all Maryland.gov applications maintain visual and functional consistency at the footer level.

---

## Statistic List

*Components*

The Statistic List component displays key rankings, counts, or percentages in a highlighted format. It supports 1 to 4 statistic items with optional title, description, and "more" link. Use this component to showcase important statistics or achievements in a visually organized layout.

### Key Information

### Variants
- **1 Statistic**: Single item layout
- **2 Statistics**: Two-item layout
- **3 Statistics**: Three-item layout
- **4 Statistics**: Four-item layout

### CSS Class Names
- `.maryland-statistic-list`: Main container element
- `.maryland-statistic-list--one`: Modifier for single statistic (shown: `maryland-statistic-list--one`)
- `.maryland-statistic-list__container`: Inner wrapper for content
- `.maryland-statistic-list__header`: Header section containing title and description
- `.maryland-statistic-list__title`: Heading for the statistic list
- `.maryland-statistic-list__description`: Description text container

### Required Attributes
- `aria-labelledby`: Links section to heading ID for accessibility
- `id`: Unique identifier on the title element (e.g., `id-36z1g7cxq4f`)

### Important Facts
- Supports flexible layout with 1-4 items
- Each statistic item displays: number/statistic, title, description, and optional "more" link
- The component scales responsively from single column to multi-column grid layouts
- Built to work with grid container system (`grid-container`, `grid-row`, `grid-gap`, `grid-col-12`)

### Implementation

```html
<section class="maryland-statistic-list maryland-statistic-list--one" aria-labelledby="id-36z1g7cxq4f">
  <div class="maryland-statistic-list__container">
    <div class="maryland-statistic-list__header">
      <h2 id="id-36z1g7cxq4f" class="maryland-statistic-list__title">
        Maryland rankings by the numbers
      </h2>
      <div class="maryland-statistic-list__description">
        <p>US News rates Maryland in the top 20 states overall in its Best States 2025 rankings.</p>
      </div>
    </div>
    <!-- Statistic items follow -->
  </div>
</section>
```

### Multiple Statistics Layout
Use variant modifiers for different quantities:
- `.maryland-statistic-list--one` for single item
- `.maryland-statistic-list--two` for two items (expected)
- `.maryland-statistic-list--three` for three items (expected)
- `.maryland-statistic-list--four` for four items (expected)

### Context

The Statistic List component integrates with MDWDS grid system (grid-container, grid-row, grid-col-12) for responsive layouts. It commonly appears in hero sections or content areas to highlight key state metrics, achievements, or rankings. The component is self-contained and typically doesn't nest other MDWDS components inside its statistics.

---

## Step Indicator

*Components*

The Step Indicator is a USWDS component that helps users track their progress through multi-step processes, such as forms, wizards, or onboarding flows. It visually communicates completed steps, highlights the current step, and shows remaining steps. Use it when you need to guide users through a defined sequence of tasks or workflow stages.

### Key Information

**Core Classes:**
- `usa-step-indicator` — Main container for the step indicator
- `usa-step-indicator__segments` — Ordered list wrapper for all steps
- `usa-step-indicator__segment` — Individual step item (list item)
- `usa-step-indicator__segment--complete` — Modifier for completed steps
- `usa-step-indicator__segment-label` — Label text for each step
- `usa-sr-only` — Screen reader only text for status (e.g., " - completed")

**Key Props/Options:**
- `steps` (array, required) — Array of step labels in display order
- `currentStep` (number, required) — Currently active step (1-based index)
- `showLabels` (boolean) — Toggle to show or hide step labels
- `centerAlign` (boolean) — Toggle to center-align the steps
- `counters` (boolean) — Toggle numeric counters (1, 2, 3...)
- `smallCounters` (boolean) — Toggle small numeric counters variant

**Accessibility Attributes:**
- `aria-label` (optional) — Provides an accessible label for the step indicator container
- `aria-described-by` (optional) — Reference ID for element that describes the component
- `aria-labelled-by` (optional) — Reference ID for label element (overrides aria-label)

**Step States:**
- Completed: `.usa-step-indicator__segment--complete` class applied
- Current: Active/current step (no specific class shown in documentation)
- Not yet completed: Default state with no modifier class

### Implementation

```html
<div class="usa-step-indicator" aria-label="Step indicator showing current step in application process">
  <ol class="usa-step-indicator__segments">
    <li class="usa-step-indicator__segment usa-step-indicator__segment--complete">
      <span class="usa-step-indicator__segment-label">
        Personal information
        <span class="usa-sr-only"> - completed</span>
      </span>
    </li>
    <li class="usa-step-indicator__segment usa-step-indicator__segment--complete">
      <span class="usa-step-indicator__segment-label">
        Household status
        <span class="usa-sr-only"> - completed</span>
      </span>
    </li>
    <li class="usa-step-indicator__segment">
      <span class="usa-step-indicator__segment-label">
        Supporting documents
        <span class="usa-sr-only"> - current step</span>
      </span>
    </li>
    <li class="usa-step-indicator__segment">
      <span class="usa-step-indicator__segment-label">
        Signature
        <span class="usa-sr-only"> - not completed</span>
      </span>
    </li>
    <li class="usa-step-indicator__segment">
      <span class="usa-step-indicator__segment-label">
        Review and submit
        <span class="usa-sr-only"> - not completed</span>
      </span>
    </li>
  </ol>
</div>
```

**Notes:**
- Container uses `aria-label` to describe the step indicator
- Use an `<ol>` (ordered list) to wrap all steps in `.usa-step-indicator__segments`
- Each step is an `<li>` with class `.usa-step-indicator__segment`
- Apply `.usa-step-indicator__segment--complete` to mark completed steps
- Use `.usa-sr-only` spans to provide screen-reader-only status text (e.g., " - completed", " - current step", " - not completed")
- Step label text goes inside `.usa-step-indicator__segment-label` span

### Context

The Step Indicator is part of the USWDS component library integrated into MDWDS and provides a standardized way to communicate multi-step workflow progress. It works alongside form components and page layouts to create guided user experiences for complex processes.

---

## Step List

*Components*

The Step List component displays a vertical list of steps that guide users through multi-step processes like applications, onboarding flows, and tutorials. It provides visual structure through a vertical accent bar connecting steps and supports both ordered (numbered) and unordered (bullet) variants. Use it whenever you need to guide users through sequential instructions or complex processes.

### Key Information

## Variants
- **Ordered (Numbered)**: Displays numbered steps with a larger circular badge
- **Unordered (Bullet)**: Displays steps with a smaller bullet indicator (class: `maryland-step-list--bullet`)

## Key CSS Classes
- `maryland-step-list`: Main container for the step list component
- `maryland-step-list--bullet`: Modifier for bullet/unordered variant
- `maryland-step-list__header`: Optional header section containing title, description, and actions
- `maryland-step-list__title`: Title heading for the step list (wrapped in `<h2>`)
- `maryland-step-list__description`: Description text for the step list
- `maryland-step-list__links`: Container for action buttons/links

## Features
- Vertical accent bar connects steps visually
- Supports rich text content including links, lists, and emphasis
- Optional header with title, description, and action buttons
- Optional action buttons within individual steps
- Responsive design adapts to container width
- Uses semantic HTML with proper heading hierarchy
- ARIA attributes for accessibility (e.g., `aria-labelledby` linking header to title)

### Implementation

```html
<!-- Bullet/Unordered Variant -->
<section class="maryland-step-list maryland-step-list--bullet" aria-labelledby="id-vy4ay58x9hd">
  <div class="maryland-step-list__header">
    <h2 class="maryland-step-list__title" id="id-vy4ay58x9hd">
      Steps to complete
    </h2>
    <p class="maryland-step-list__description">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    </p>
    <div class="maryland-step-list__links">
      <a href="javascript:void(0)" class="usa-button usa-button--big">Primary action</a>
      <a href="javascript:void(0)" class="usa-button usa-button--big">Secondary action</a>
    </div>
  </div>
  <!-- Individual step items follow the header -->
</section>

<!-- Ordered/Numbered Variant (structure is same, remove the maryland-step-list--bullet modifier) -->
<section class="maryland-step-list" aria-labelledby="id-vy4ay58x9hd">
  <div class="maryland-step-list__header">
    <h2 class="maryland-step-list__title" id="id-vy4ay58x9hd">
      Steps to complete
    </h2>
    <p class="maryland-step-list__description">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    </p>
  </div>
</section>
```

### Context

The Step List component is a core MDWDS component for presenting sequential workflows and processes. It composes with MDWDS buttons (using `usa-button` classes) for actions and follows Maryland's design system patterns for accessibility, responsive behavior, and semantic HTML structure.

---

## Summary Box

*Components*

The Maryland Summary Box component highlights important information in a visually prominent container. It is ideal for surfacing key takeaways, action items, or warnings that users should not miss. Use this component when you need to draw attention to critical information that requires user awareness or action.

### Key Information

## Properties

- **title** (string, required): Heading text for the summary box.
- **items** (array, required): Array of list items. Each item is an HTML string, allowing for embedded links and other inline markup.

## CSS Classes

- `maryland-summary-box`: Main container with `role="region"` and `aria-labelledby` attribute pointing to the heading ID.
- `maryland-summary-box__inner`: Inner wrapper containing the heading and content.
- `maryland-summary-box__heading`: The h2 heading element for the summary box title.
- `maryland-summary-box__text`: Container for the list content.
- `maryland-summary-box__list`: Unordered list (`<ul>`) containing individual list items.

## Required Attributes

- `role="region"`: Applied to the main container to define it as a landmark region.
- `aria-labelledby`: References the ID of the heading element for accessible labeling.
- Heading ID: A unique ID on the `maryland-summary-box__heading` element for `aria-labelledby` reference.

## Variants

- Single default variant with title and bulleted list of HTML string items.

### Implementation

```html
<div role="region" class="maryland-summary-box" aria-labelledby="maryland-summary-box-id-unique">
  <div class="maryland-summary-box__inner">
    <h2 class="maryland-summary-box__heading" id="maryland-summary-box-id-unique">
      Key information
    </h2>
    <div class="maryland-summary-box__text">
      <ul class="maryland-summary-box__list">
        <li>If you are under a winter storm warning, <a href="#">find shelter</a> right away.</li>
        <li>Sign up for <a href="#">your community's warning system</a>.</li>
        <li>Learn the signs of, and basic treatments for, <a href="#">frostbite</a> and <a href="#">hypothermia</a>.</li>
        <li>Gather emergency supplies for your <a href="#">home</a> and your <a href="#">car</a>.</li>
        <li>Review and update your <a href="#">emergency plan</a> annually.</li>
      </ul>
    </div>
  </div>
</div>
```

### Context

The Summary Box is a specialized Components section within MDWDS that provides visual emphasis for critical information. It works as a standalone container and complements other content components by highlighting key messages without requiring integration with other elements.

---

## Summary Box

*Components*

The Summary Box component highlights important information in a visually prominent container. It is ideal for surfacing key takeaways, action items, or warnings that users should not miss. This USWDS-based component is fully customizable via controls and supports accessibility labels.

### Key Information

## Key CSS Classes
- `usa-summary-box`: Main container element
- `usa-summary-box__body`: Wrapper for the summary box content
- `usa-summary-box__heading`: Heading text (typically an h4)
- `usa-summary-box__text`: Container for the summary box text content
- `usa-summary-box__link`: Link styling within the summary box
- `usa-list`: List container class for list items

## Key Properties
- **heading** (string): Heading text for the summary box
- **listItems** (array): Array of objects defining list items, each with `{ text, link }` properties
- **regionLabel** (string): ARIA label for the region; required for screen readers to describe the purpose of the summary box

## Required ARIA Attributes
- `role="region"`: Identifies the summary box as a landmark region
- `aria-label`: Must be set to provide an accessible description (e.g., "Summary of important information")

## Structure
The component wraps a list of linked items inside a prominent container with a heading. Links within the box use the `usa-summary-box__link` class for consistent styling.

### Implementation

```html
<div class="usa-summary-box" role="region" aria-label="Summary of important information">
  <div class="usa-summary-box__body">
    <h4 class="usa-summary-box__heading">Key information</h4>
    <div class="usa-summary-box__text">
      <ul class="usa-list">
        <li><a class="usa-summary-box__link" href="#">Find shelter</a></li>
        <li><a class="usa-summary-box__link" href="#">Sign up for alerts</a></li>
        <li><a class="usa-summary-box__link" href="#">Learn about frostbite and hypothermia</a></li>
        <li><a class="usa-summary-box__link" href="#">Gather emergency supplies</a></li>
      </ul>
    </div>
  </div>
</div>
```

## Notes
- The `role="region"` and `aria-label` are critical for accessibility and screen reader users
- The heading is typically an `<h4>` element
- List items are wrapped in a `<ul class="usa-list">` for semantic structure
- Links within the summary box receive the `usa-summary-box__link` class for proper styling and visual distinction

### Context

The Summary Box is a USWDS component adapted for MDWDS that serves as a prominent container for highlighting critical information. It composes with the standard `usa-list` utility and link styling, fitting into the broader USWDS component ecosystem for organizing and emphasizing content that users should not miss.

---

## Table

*Components*

The Maryland Table component displays data in rows and columns with responsive horizontal scrolling on narrow screens. It provides borderless and striped variants by default, with an italic caption above the table. In Drupal environments, Tabled.js enhances the table with navigation arrows and scroll indicators for horizontal column navigation.

### Key Information

## Variants & Modifiers

- **Striped**: Enable alternating row striping via the `striped` boolean property (default behavior enabled)
- **Borderless**: Enable/disable borders via the `borderless` boolean property
- **Caption**: Display italic caption text above the table (max 200 characters) via the `caption` string property

## CSS Classes

- `maryland-table`: Main container wrapper
- `tabled`: Wrapper for table with scrolling support
- `tabled--fade-right`: Modifier class indicating fade effect on right edge during horizontal scroll
- `tabled__header`: Container for caption and navigation controls
- `tabled__caption`: Caption text display (aria-hidden for accessibility)
- `tabled__navigation`: Container for scroll navigation buttons
- `tabled__previous`: Previous column button (disabled when at start)
- `tabled__next`: Next column button

## Required Attributes

- Table headers: Standard semantic `<thead>`, `<th>` elements
- Navigation buttons: `aria-label` and `aria-controls` attributes for accessibility
- Caption container: `aria-hidden="true"` attribute
- Button states: `disabled` attribute when navigation is not applicable

## Important Notes

- Max caption length: 200 characters
- Horizontal scrolling navigation provided by Tabled.js in Drupal environments
- Table structure uses semantic HTML with proper heading hierarchy
- Striped and borderless variants are enabled by default

### Implementation

```html
<div class="maryland-table" id="maryland-table-0">
  <div class="tabled tabled--fade-right">
    <div class="tabled__header">
      <div class="tabled__caption" aria-hidden="true">
        Table caption goes here with max 200 characters consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, qui.
      </div>
      <div class="tabled__navigation">
        <button class="tabled__previous" aria-label="previous table column" aria-controls="tabled-n1" disabled="disabled" type="button"></button>
        <button class="tabled__next" aria-label="next table column" aria-controls="tabled-n1" type="button"></button>
      </div>
    </div>
    <!-- Table content with semantic HTML -->
    <table>
      <caption>Table caption goes here with max 200 characters consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, qui.</caption>
      <thead>
        <tr>
          <th>Table(s) title goes here</th>
          <th>Long title can go like this in double lines Long title can go like this in double lines</th>
          <th>Column 3 header</th>
          <th>Column 4 header</th>
          <th>Column 5 header</th>
          <th>Column 6 header</th>
          <th>Column 7 header</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Column 1, Row 1</td>
          <td>Column 2, Row 1</td>
          <td>Column 3, Row 1</td>
          <td>Column 4, Row 1</td>
          <td>Column 5, Row 1</td>
          <td>Column 6, Row 1</td>
          <td>Column 7, Row 1</td>
        </tr>
        <tr>
          <td>Column 1, Row 2</td>
          <td>Column 2, Row 2</td>
          <td>Column 3, Row 2</td>
          <td>Column 4, Row 2</td>
          <td>Column 5, Row 2</td>
          <td>Column 6, Row 2</td>
          <td>Column 7, Row 2</td>
        </tr>
        <!-- Additional rows follow same pattern -->
      </tbody>
    </table>
  </div>
</div>
```

### Context

The Maryland Table component is a core data presentation component that integrates with the MDWDS system for consistent tabular data display. It composes with Tabled.js in Drupal environments for enhanced horizontal scrolling navigation and works alongside standard semantic HTML table elements to provide accessible, responsive data presentation.

---

## Table

*Components*

The USWDS Table component organizes data in rows and columns with multiple style variants and responsive behavior. It supports various configurations including striped, borderless, stacked layouts, and optional features like sortable columns and sticky headers. Use this component to display structured tabular data with proper accessibility semantics and responsive design.

### Key Information

## Variants & Modifiers
- **Variant options:** `default`, `borderless`, `striped`, `stacked`, `stacked-header`, `compact`
- Stacked variants collapse to single-column on mobile devices
- **Scrollable:** Wraps table in a scrollable container for horizontal scrolling of wide datasets
- **Sortable:** Enable sortable columns requiring USWDS JavaScript integration; individual columns must have `sortable: true`
- **Sticky Header:** Keep column headers visible during vertical scrolling with `stickyHeader` option
- **Compact:** Reduced padding variant for dense data display

## CSS Class Names
- Base table class: `usa-table`
- Variant modifiers applied as classes on the table element (e.g., `usa-table usa-table--striped`)

## Key HTML Attributes
- **`<table>`**: Unique `id` attribute for scripting and identification
- **`<caption>`**: Required for accessibility; describes table content
- **`<th scope="col">`**: Column headers with `scope="col"` attribute and `role="columnheader"`
- **`<th scope="row">`**: Row header cells with `scope="row"` attribute
- **`<td>`**: Standard data cells

## Configuration Properties
- **variant:** Table style variant (string, default varies by design)
- **caption:** Descriptive caption for the table (string)
- **columns:** Array of column definition objects with properties: `header` (display text), `accessor` (data key), `sortable` (boolean)
- **rows:** Array of data objects where keys match column accessors
- **scrollable:** Boolean to enable horizontal scrolling wrapper
- **sortable:** Boolean to enable column sorting; requires USWDS JavaScript
- **stickyHeader:** Boolean to keep headers visible during scrolling
- **enableAnalytics:** Optional boolean for Google Analytics tracking attributes

## Accessibility Requirements
- Proper semantic markup with `<table>`, `<thead>`, `<tbody>`
- Column headers require `scope="col"` and `role="columnheader"`
- Row headers require `scope="row"`
- All tables must have a `<caption>` element describing the table purpose
- WCAG 2.1 AA compliant

### Implementation

```html
<!-- Basic Table with Caption -->
<table class="usa-table" id="table-id-example">
  <caption>Agency contact information</caption>
  <thead>
    <tr>
      <th scope="col" role="columnheader">Agency</th>
      <th scope="col" role="columnheader">Contact</th>
      <th scope="col" role="columnheader">Email</th>
      <th scope="col" role="columnheader">Phone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Department of Information Technology</th>
      <td>John Smith</td>
      <td>john.smith@maryland.gov</td>
      <td>(410) 555-1234</td>
    </tr>
    <tr>
      <th scope="row">Department of Health</th>
      <td>Jane Doe</td>
      <td>jane.doe@maryland.gov</td>
      <td>(410) 555-5678</td>
    </tr>
    <tr>
      <th scope="row">Department of Transportation</th>
      <td>Bob Johnson</td>
      <td>bob.johnson@maryland.gov</td>
      <td>(410) 555-9012</td>
    </tr>
  </tbody>
</table>
```

```html
<!-- Striped Variant -->
<table class="usa-table usa-table--striped" id="table-id-example">
  <caption>Table caption describing content</caption>
  <thead>
    <tr>
      <th scope="col" role="columnheader">Column 1</th>
      <th scope="col" role="columnheader">Column 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Row Header</th>
      <td>Data</td>
    </tr>
  </tbody>
</table>
```

```html
<!-- Borderless Variant -->
<table class="usa-table usa-table--borderless" id="table-id-example">
  <caption>Table caption describing content</caption>
  <thead>
    <tr>
      <th scope="col" role="columnheader">Column 1</th>
      <th scope="col" role="columnheader">Column 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Row Header</th>
      <td>Data</td>
    </tr>
  </tbody>
</table>
```

```html
<!-- Compact Variant -->
<table class="usa-table usa-table--compact" id="table-id-example">
  <caption>Table caption describing content</caption>
  <thead>
    <tr>
      <th scope="col" role="columnheader">Column 1</th>
      <th scope="col" role="columnheader">Column 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Row Header</th>
      <td>Data</td>
    </tr>
  </tbody>
</table>
```

```html
<!-- Stacked Variant (Responsive) -->
<table class="usa-table usa-table--stacked" id="table-id-example">
  <caption>Table caption describing content</caption>
  <thead>
    <tr>
      <th scope="col" role="columnheader">Column 1</th>
      <th scope="col" role="columnheader">Column 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Row Header</th>
      <td>Data</td>
    </tr>
  </tbody>
</table>
```

```html
<!-- Stacked Header Variant -->
<table class="usa-table usa-table--stacked-header" id="table-id-example">
  <caption>Table caption describing content</caption>
  <thead>
    <tr>
      <th scope="col" role="columnheader">Column 1</th>
      <th scope="col" role="columnheader">Column 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Row Header</th>
      <td>Data</td>
    </tr>
  </tbody>
</table>
```

```html
<!-- Scrollable Table (Horizontally Scrollable) -->
<div class="usa-table-container--scrollable">
  <table class="usa-table" id="table-id-example">
    <caption>Wide table with horizontal scrolling</caption>
    <thead>
      <tr>
        <th scope="col" role="columnheader">Column 1</th>
        <th scope="col" role="columnheader">Column 2</th>
        <th scope="col" role="columnheader">Column 3</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Row Header</th>
        <td>Data</td>
        <td>Data</td>
      </tr>
    </tbody>
  </table>
</div>
```

```html
<!-- Sortable Columns with USWDS JS -->
<table class="usa-table" id="table-id-example" data-sortable="">
  <caption>Table with sortable columns</caption>
  <thead>
    <tr>
      <th scope="col" role="columnheader" data-sortable="">Column 1</th>
      <th scope="col" role="columnheader" data-sortable="">Column 2</th>
      <th scope="col" role="columnheader">Column 3 (Not sortable)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Row Header</th>
      <td>Data</td>
      <td>Data</td>
    </tr>
  </tbody>
</table>

<!-- Initialize USWDS Table JavaScript -->
<script src="https://cdn.designsystem.maryland.gov/js/uswds.min.js?v=0.44.0"></script>
<script>
  USWDS.Table.on(document.getElementById("table-id-example"));
</script>
```

```html
<!-- Sticky Header Table -->
<div class="usa-table-container--sticky-header">
  <table class="usa-table" id="table-id-example">
    <caption>Table with sticky headers</caption>
    <thead>
      <tr>
        <th scope="col" role="columnheader">Column 1</th>
        <th scope="col" role="columnheader">Column 2</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Row Header 1</th>
        <td>Data</td>
      </tr>
      <tr>
        <th scope="row">Row Header 2</th>
        <td>Data</td>
      </tr>
      <!-- Additional rows... -->
    </tbody>
  </table>
</div>
```

### Context

The Table component is a core USWDS element adapted into MDWDS for displaying structured data across Maryland government applications. It integrates with USWDS JavaScript utilities for sortable columns and responsive behaviors, composing with other data display patterns while maintaining consistent accessibility and visual standards.

---

## Table of Contents

*Components*

A table of contents component provides in-page navigation links to various sections of a page, allowing users to quickly jump to relevant content. It improves page usability by offering an overview of page structure and enabling faster navigation for longer documents.

### Key Information

## Key Information

### Class Names
- `maryland-sidenav`: Main navigation container for the table of contents
- `maryland-sidenav__toggle`: Button to toggle the visibility of the navigation list
- `maryland-sidenav__title`: Heading for the navigation section
- `maryland-sidenav__list`: Container for navigation items
- `maryland-sidenav__list--level-1`: Modifier indicating first-level navigation items
- `maryland-sidenav__item`: Individual navigation item
- `maryland-sidenav__item--level-1`: Modifier for first-level items
- `maryland-sidenav__link`: Clickable link within a navigation item

### ARIA Attributes
- `aria-labelledby`: Links the nav to the title via ID
- `aria-controls`: Connects toggle button to the list it controls

### States
- `is-open`: Applied to the list to indicate expanded state

### HTML Structure
- Uses semantic `<nav>` and `<ul>`/`<li>` elements
- Requires toggle button for mobile/responsive behavior
- Links are typically `<a>` or `<span>` elements styled as links

### Implementation

```html
<nav class="maryland-sidenav" aria-labelledby="id-gdapyyf7w7f">
  <button class="maryland-sidenav__toggle" aria-controls="id-k459osmcu6">
    <span class="usa-sr-only"></span>
    <h2 class="maryland-sidenav__title" id="id-gdapyyf7w7f">Section menu</h2>
  </button>
  <ul class="maryland-sidenav__list maryland-sidenav__list--level-1 is-open" id="id-k459osmcu6">
    <li class="maryland-sidenav__item maryland-sidenav__item--level-1">
      <span class="maryland-sidenav__link">Navigation Link</span>
    </li>
  </ul>
</nav>
```

### Expanded State
Apply `is-open` class to `maryland-sidenav__list` to show the navigation list:

```html
<ul class="maryland-sidenav__list maryland-sidenav__list--level-1 is-open" id="id-k459osmcu6">
```

### Collapsed State
Remove or do not apply the `is-open` class to hide the navigation list:

```html
<ul class="maryland-sidenav__list maryland-sidenav__list--level-1" id="id-k459osmcu6">
```

### Context

The Table of Contents component is part of the Maryland Web Design System's navigation components. It typically works alongside page layout utilities (such as grid-container, grid-row, grid-col classes) to provide a responsive side navigation that enhances discoverability of page sections.

---

## Tag

*Components*

The Tag component is a USWDS-based element used to visually emphasize statuses, categories, or other metadata. It provides a flexible way to display labeled information with optional ARIA attributes for accessibility. Use tags to highlight important information, status indicators, or categorical labels within your interface.

### Key Information

**Variants:**
- `default` - Standard tag size
- `big` - Larger tag size

**Key CSS Classes:**
- `usa-tag` - Base tag component class

**Properties/Attributes:**
- `size` - Controls tag size (options: "default" or "big")
- `label` - Text displayed inside the tag
- `ariaLabel` (optional) - Override visible text for screen readers
- `ariaDescribedBy` (optional) - ID of another element providing additional context
- `role` (optional) - ARIA role such as 'status' or 'note'

**Important Facts:**
- The component accepts customizable label text
- ARIA attributes are optional and can be used to enhance accessibility
- Supports both default and big sizing options

### Implementation

```html
<span class="usa-tag">Info</span>
```

**Default Tag:**
```html
<span class="usa-tag">Info</span>
```

**Big Tag Variant (when size="big"):**
```html
<span class="usa-tag usa-tag--big">Info</span>
```

**With ARIA Attributes:**
```html
<span class="usa-tag" aria-label="Status: Active" role="status">Active</span>
```

**With aria-describedBy:**
```html
<span class="usa-tag" aria-describedby="tag-description">Info</span>
```

### Context

The Tag component is part of the USWDS component library integrated into MDWDS. It serves as a lightweight, accessible labeling component that can be combined with other components to provide status indicators, category labels, or metadata emphasis throughout the design system.

---

## Textarea

*Components*

The USWDS Textarea component is used for collecting longer free-form input like comments, descriptions, or multiline data. It supports custom labels, placeholders, optional ARIA attributes, and MDWDS styling with focus visibility. Use this when you need to gather multiple lines of text input from users.

### Key Information

## Properties

- **label** (string): Text label associated with the textarea
- **id** (string): Unique ID for textarea and label association
- **name** (string): Textarea name attribute (used in form submissions)
- **placeholder** (string, optional): Optional placeholder text inside the textarea
- **rows** (number, optional): Number of visible rows

## Accessibility Attributes

- **ariaLabel** (string, optional): ARIA label used when label is visually hidden
- **ariaDescribedBy** (string, optional): ID of an element describing this textarea

## CSS Classes

- `usa-form`: Form wrapper class
- `usa-label`: Applied to the label element for proper styling
- `usa-textarea`: Main class applied to the textarea element

## Notes

- The component uses standard HTML form elements with USWDS styling applied
- Supports optional ARIA attributes for enhanced accessibility
- Label should be associated with textarea via `for` attribute on label and matching `id` on textarea element

### Implementation

```html
<form class="usa-form">
  <label class="usa-label" for="input-type-textarea">Text area label</label>
  <textarea class="usa-textarea" id="input-type-textarea" name="input-type-textarea" rows="5"></textarea>
</form>
```

### With Placeholder

```html
<form class="usa-form">
  <label class="usa-label" for="textarea-id">Label Text</label>
  <textarea class="usa-textarea" id="textarea-id" name="textarea-name" rows="5" placeholder="Enter your text here"></textarea>
</form>
```

### With ARIA Attributes

```html
<form class="usa-form">
  <label class="usa-label" for="textarea-id">Label Text</label>
  <textarea class="usa-textarea" id="textarea-id" name="textarea-name" rows="5" aria-label="Description" aria-describedby="help-text"></textarea>
  <div id="help-text">Provide additional details</div>
</form>
```

### Context

The Textarea component extends USWDS form elements within the MDWDS system, providing consistent styling and accessibility patterns for multi-line text input. It composes with the usa-form wrapper and usa-label components to create accessible, properly-associated form fields.

---

## Time Picker

*Components*

The Time Picker is an accessible dropdown time selection widget that provides filterable time options with customizable intervals. It solves the problem of allowing users to quickly select a time from a pre-defined list with keyboard filtering capabilities. Use it in forms where time input is required, such as appointment scheduling or time-based event registration.

### Key Information

## Variants & Features
- **Default intervals**: 30-minute increments (configurable to 15, 60 minutes, or custom)
- **Filtering**: Keyboard filtering enabled by default (can be disabled with `data-disable-filtering="true"`)
- **Min/Max constraints**: Support for minimum and maximum time boundaries
- **Default values**: Can set a pre-selected time with `data-default-value`
- **Required state**: Boolean attribute to mark field as required
- **Disabled state**: Boolean attribute to disable the input
- **Analytics support**: Google Analytics tracking attributes configurable

## CSS Class Names
- `usa-form-group` — wrapper container
- `usa-label` — label element
- `usa-hint` — hint text container
- `usa-time-picker` — main time picker container
- `usa-combo-box` — combobox functionality class (used alongside `usa-time-picker`)

## Required Attributes & Data Attributes
- `id` — unique identifier for the input
- `name` — form submission name
- `for` (on label) — links label to input via id
- `data-step` — time interval in minutes (e.g., 30, 15, 60)
- `data-filter` — regex pattern for filtering (e.g., `0?{{ hourQueryFilter }}:{{minuteQueryFilter}}.*{{ apQueryFilter }}m?`)
- `data-ap-query-filter` — regex for AM/PM filtering
- `data-hour-query-filter` — regex for hour filtering
- `data-minute-query-filter` — regex for minute filtering
- `data-disable-filtering` — boolean to disable keyboard filtering
- `data-default-value` — default selected time value
- `data-enhanced` — boolean indicating USWDS JS has been applied

## Important Facts
- Requires USWDS JavaScript to initialize and function
- Automatically initializes on page load with combobox-like functionality
- Supports WCAG 2.1 AA accessibility requirements
- Hint text provided via `usa-hint` div with matching id attribute
- Component generates 48 time options (30-minute intervals over 24 hours) by default

### Implementation

```html
<div class="usa-form-group">
  <label class="usa-label" id="time-picker-label-id" for="time-picker-id">
    Appointment time
  </label>
  <div class="usa-hint" id="time-picker-hint-id">
    Select a time from the dropdown. Type to filter options.
  </div>
  <div class="usa-time-picker usa-combo-box" 
       data-step="30" 
       data-filter="0?{{ hourQueryFilter }}:{{minuteQueryFilter}}.*{{ apQueryFilter }}m?"
       data-ap-query-filter="([ap])"
       data-hour-query-filter="([1-9][0-2]?)"
       data-minute-query-filter="[\d]+:([0-9]{0,2})"
       data-disable-filtering="true"
       data-default-value="undefined"
       data-enhanced="true">
    <select id="time-picker-id" name="appointment_time"></select>
  </div>
</div>
```

### With 15-Minute Intervals
```html
<div class="usa-form-group">
  <label class="usa-label" id="time-picker-label" for="time-picker-id">
    Select Time
  </label>
  <div class="usa-time-picker usa-combo-box" 
       data-step="15"
       data-filter="0?{{ hourQueryFilter }}:{{minuteQueryFilter}}.*{{ apQueryFilter }}m?"
       data-ap-query-filter="([ap])"
       data-hour-query-filter="([1-9][0-2]?)"
       data-minute-query-filter="[\d]+:([0-9]{0,2})"
       data-disable-filtering="false"
       data-enhanced="true">
    <select id="time-picker-id" name="time"></select>
  </div>
</div>
```

### With Min/Max Times
```html
<div class="usa-form-group">
  <label class="usa-label" id="business-hours-label" for="time-picker-business">
    Business Hours (9 AM - 5 PM)
  </label>
  <div class="usa-time-picker usa-combo-box" 
       data-step="30"
       data-min-time="9:00am"
       data-max-time="5:00pm"
       data-filter="0?{{ hourQueryFilter }}:{{minuteQueryFilter}}.*{{ apQueryFilter }}m?"
       data-ap-query-filter="([ap])"
       data-hour-query-filter="([1-9][0-2]?)"
       data-minute-query-filter="[\d]+:([0-9]{0,2})"
       data-enhanced="true">
    <select id="time-picker-business" name="business_time"></select>
  </div>
</div>
```

### Required & Disabled States
```html
<!-- Required -->
<div class="usa-form-group">
  <label class="usa-label" for="time-required">
    Appointment Time <span class="usa-required">*</span>
  </label>
  <div class="usa-time-picker usa-combo-box" data-step="30" data-enhanced="true">
    <select id="time-required" name="time" required></select>
  </div>
</div>

<!-- Disabled -->
<div class="usa-form-group">
  <label class="usa-label" for="time-disabled">
    Time (Disabled)
  </label>
  <div class="usa-time-picker usa-combo-box" data-step="30" data-enhanced="true">
    <select id="time-disabled" name="time" disabled></select>
  </div>
</div>
```

### Context

The Time Picker is a USWDS component integrated into MDWDS that provides accessible time selection for forms. It composes with the form group system (usa-form-group, usa-label, usa-hint) and shares combobox functionality with other select-like components. It requires USWDS JavaScript initialization and follows WCAG accessibility standards for enhanced user experience.

---

## Tooltip

*Components*

The USWDS Tooltip component provides contextual help text that appears on hover or focus. It solves the problem of delivering brief, contextual information without cluttering the interface. Use tooltips to clarify form fields, button purposes, or provide additional context for UI elements.

### Key Information

## Variants
- **Position options**: top (default), bottom, left, right
- **Trigger types**: button or link element
- **Analytics**: Optional Google Analytics tracking attributes (gaCategory, gaAction, gaLabel)

## CSS Classes
- `usa-tooltip`: Container wrapper
- `usa-tooltip__trigger`: Applied to the trigger element (button or link)
- `usa-tooltip__body`: The tooltip content container

## Required Attributes
- `data-position`: Specifies tooltip placement (top, bottom, left, right)
- `aria-describedby`: Links trigger to tooltip body by ID
- `id`: Unique identifier for tooltip trigger element
- `role="tooltip"`: Applied to the tooltip content container
- `aria-hidden="true"`: Applied to tooltip body to hide from assistive tech when not visible

## Key Facts
- Tooltips are keyboard accessible via Tab and focus states
- ESC key dismisses the tooltip
- Tested against WCAG 2.1 AA standards
- Progressive enhancement of native title attribute
- Supports custom content via `tooltipText` property
- Configurable trigger labels via `triggerLabel` property

### Implementation

```html
<!-- Basic Tooltip with Button Trigger -->
<span class="usa-tooltip">
  <button 
    type="button" 
    class="usa-button usa-tooltip__trigger" 
    id="tooltip-trigger-id-5tgd9bb68uw" 
    data-position="top" 
    aria-describedby="tooltip-313835" 
    tabindex="0">
    Hover or focus me
  </button>
  <span 
    class="usa-tooltip__body" 
    id="tooltip-313835" 
    role="tooltip" 
    aria-hidden="true">
    This is helpful information
  </span>
</span>
```

## Key Implementation Details
- The trigger element must have a unique `id` attribute
- The `aria-describedby` attribute on the trigger must match the `id` of the tooltip body
- The `data-position` attribute controls placement: `top`, `bottom`, `left`, or `right`
- The tooltip body uses `role="tooltip"` and `aria-hidden="true"` for accessibility
- Multiple variants exist for different positions (top, bottom, left, right) and trigger types (button, link)
- Link trigger variant uses similar structure with `<a>` instead of `<button>`

### Context

The Tooltip component is a USWDS component that enhances user experience by providing on-demand contextual information. It integrates with standard form controls and buttons, and can be combined with other components that need additional help or explanation.

---

## Utility Nav

*Components*

The utility navigation provides quick access to secondary actions and account-related links in the header. It supports both standard links and button-styled CTAs. The utility nav appears at the top of the header on desktop viewports and in the mobile menu on smaller screens.

### Key Information

## Item Types

The utility nav supports three types of items:

- **Plain link**: `{ label: "Text", url: "#" }` — renders as a standard `<a>` tag
- **Button-styled link**: `{ label: "Text", url: "#", isButton: true }` — renders as an anchor with button classes
- **Button (no link)**: `{ label: "Text", isButton: true }` — renders as a button element without a URL property

## CSS Class Names

- `maryland-header__util-nav-container` — wrapper container for the utility nav
- `maryland-header__util-nav` — the unordered list containing nav items
- `usa-button` — standard button class for button-styled items
- `usa-button--small` — modifier for small button variant

## Properties

- `enableUtil` (boolean, default: false) — Enable/disable the utility navigation
- `util` (array) — Array of navigation items with label, url, and optional isButton properties

## Structure

The component renders as an unordered list of navigation items that can be either plain links or button-styled links. Each item is a list item (`<li>`) containing either an `<a>` tag or button element.

### Implementation

```html
<!-- Utility Nav Container -->
<div class="maryland-header__util-nav-container">
  <ul class="maryland-header__util-nav">
    <!-- Plain Link Item -->
    <li>
      <a href="#!">Link One</a>
    </li>
    
    <!-- Plain Link Item -->
    <li>
      <a href="#!">Link Two</a>
    </li>
    
    <!-- Button-Styled Link Item -->
    <li>
      <a class="usa-button usa-button--small" href="#!">Button</a>
    </li>
  </ul>
</div>
```

**Variants:**

1. **Plain Link** — Standard anchor tag with no button classes
2. **Button-Styled Link** — Anchor tag with `usa-button` and `usa-button--small` classes

### Context

The utility navigation is a header component that composes within the Maryland header system. It provides a flexible list-based structure for secondary navigation and account-related actions, supporting both text links and button-styled CTAs within the header region.

---

## Validation

*Components*

The USWDS Validation component provides inline validation feedback for form fields with error and success states. It displays error messages, success indicators, and required field markers while maintaining accessibility through ARIA attributes. Use this component to provide users with real-time form field validation feedback.

### Key Information

**Variants/States:**
- Default: Standard styling with optional hints
- Error: Red border, error message, error icon
- Success: Green border, success icon
- Disabled with error: Disabled input with error state
- Required field: Field marked with asterisk indicator

**CSS Classes:**
- `usa-form`: Form wrapper (may use `usa-form--large` modifier for larger spacing)
- `usa-form-group`: Container for each form field
- `usa-label`: Label element
- `usa-hint`: Hint text displayed below label
- `usa-input`: Input field element (appears without color modifiers in HTML; error/success states managed via parent form-group or input attributes)

**Input Types Supported:**
- `text`
- `email`
- `tel`
- `password`
- `number`

**Component Properties:**
- `label` (string): Label text for the input field
- `inputType` (string): Type of input field (text, email, tel, password, number)
- `validationState` (string): Current state — default, error, or success
- `errorMessage` (string): Error message displayed only when validationState is 'error'
- `hint` (string): Optional hint text displayed below label
- `required` (boolean): Mark field as required (false by default)
- `disabled` (boolean): Disable the input field (false by default)
- `enableAnalytics` (boolean): Enable/disable GA tracking attributes
- `gaCategory`, `gaAction`, `gaLabel` (strings): Google Analytics tracking parameters

**Required Attributes:**
- `id` on input (for aria-describedby linking)
- `aria-describedby` on input (links to hint text id)
- `for` attribute on label (matches input id)

**Note:** This component requires USWDS JavaScript to be loaded for dynamic validation functionality.

### Implementation

```html
<!-- Default State with Hint -->
<form class="usa-form usa-form--large" style="max-width: 30rem;">
  <div class="usa-form-group">
    <label class="usa-label" for="validation-id-example">
      Email address
    </label>
    <span class="usa-hint" id="hint-id-example">For example, name@example.com</span>
    <input class="usa-input" id="validation-id-example" name="validation-id-example" type="email" aria-describedby="hint-id-example">
  </div>
</form>
```

**Error State Variant:**
```html
<form class="usa-form usa-form--large">
  <div class="usa-form-group usa-form-group--error">
    <label class="usa-label" for="validation-error">
      Email address
    </label>
    <span class="usa-hint" id="hint-error">For example, name@example.com</span>
    <span class="usa-error-message" id="error-message-error">Please enter a valid email address</span>
    <input class="usa-input usa-input--error" id="validation-error" name="validation-error" type="email" aria-describedby="hint-error error-message-error">
  </div>
</form>
```

**Required Field Variant:**
```html
<form class="usa-form usa-form--large">
  <div class="usa-form-group">
    <label class="usa-label" for="validation-required">
      Full Name
      <abbr title="required">*</abbr>
    </label>
    <input class="usa-input" id="validation-required" name="validation-required" type="text" required aria-required="true">
  </div>
</form>
```

**Success State Variant:**
```html
<form class="usa-form usa-form--large">
  <div class="usa-form-group">
    <label class="usa-label" for="validation-success">
      Email address
    </label>
    <input class="usa-input usa-input--success" id="validation-success" name="validation-success" type="email">
  </div>
</form>
```

### Context

This component extends USWDS form validation patterns for the Maryland Web Design System. It integrates with the standard form components (form-group, label, input) and enhances them with state-specific styling and error messaging. Validation states compose with other form elements and support optional Google Analytics tracking for user interaction monitoring.

---

## Video Promo

*Components*

The Video Promo component is a visually prominent content section that combines video media with accompanying text and a call-to-action link. It highlights a single message or offer by presenting video and descriptive content in a structured, flexible layout to drive user engagement.

### Key Information


**Variants:**
- Layout option: Side-by-side (default: `maryland-video-promo--side-by-side`)
- Layout options available: Full-width, Video first, Text first

**CSS Classes:**
- `.maryland-video-promo` – Main container
- `.maryland-video-promo--side-by-side` – Layout modifier for side-by-side display
- `.maryland-video-promo__container` – Inner wrapper
- `.maryland-video-promo__content` – Content section wrapper
- `.maryland-video-promo__title` – Title heading
- `.maryland-video-promo__description` – Description text
- `.maryland-video-promo__link` – Call-to-action link

**Required Props:**
- `title` (string, required) – Clear, concise, descriptive title relevant to the content
- `video` (string, required) – iFrame embed code for YouTube/Vimeo video player

**Optional Props:**
- `description` (string) – Brief message providing information or context for the link
- `visually_hide_title` (boolean, default: false) – Hides title from display but not screen readers
- `link_text` (string) – Text for optional call-to-action link
- `link_url` (string) – URL for optional call-to-action link
- `caption` (string) – Adds a caption to the video player
- `layout` (string) – Supports Full-width, Video first, Text first options

**Accessibility:**
- Uses `aria-labelledby` to associate the section with its title ID
- Title is an `<h2>` heading with auto-generated ID


### Implementation


```html
<section class="maryland-video-promo maryland-video-promo--side-by-side" aria-labelledby="id-r34vb9wdqlj">
  <div class="maryland-video-promo__container">
    <div class="maryland-video-promo__content">
      <h2 id="id-r34vb9wdqlj" class="maryland-video-promo__title">Video Promo</h2>
      <p class="maryland-video-promo__description">Culpa esse excepteur commodo velit mollit amet amet mollit consequat irure ipsum sint sint.</p>
      <a class="maryland-video-promo__link" href="https://example.com">Call to action</a>
    </div>
  </div>
</section>
```

**Notes:**
- The video player iframe embed would be inserted in the appropriate layout position alongside the content
- The title receives an auto-generated ID (e.g., `id-r34vb9wdqlj`) that is referenced in the `aria-labelledby` attribute
- Layout modifiers control positioning of video and text (side-by-side, full-width, video-first, text-first)


### Context

The Video Promo component is part of the MDWDS component library for composing rich media sections. It combines semantic HTML with BEM-style class naming and integrates with the grid system for layout control, allowing flexible positioning of multimedia content with supporting text and calls-to-action.

---

## Visual Link Collection

*Components*

Visual Link Collection displays a grid of linked cards that guide users to different sections or resources. Each card is fully clickable and uses the Linked variant of the Maryland Cards component. It is ideal for service directories, topic landing pages, resource collections, and navigation hubs.

### Key Information

## Key Class Names
- `maryland-visual-link-collection` — Main container/wrapper for the component
- `maryland-card-group__header` — Header section containing title and description
- `maryland-card-group__header-content` — Content wrapper within the header
- `maryland-card-group__title` — Section title heading (h2 element)
- `maryland-card-group__description` — Description text below the title

## Structure & Usage
- The component uses a section element with the `maryland-visual-link-collection` class
- Includes a header with title and optional description
- Cards within the collection use the Maryland Cards component with the Linked variant
- Each card is fully clickable for navigation
- Supports custom section aria labels via `aria-labelledby` attribute

## Important Attributes
- `aria-labelledby` — Links the section to its title ID for proper accessibility
- Section-level semantic HTML for proper document structure

### Implementation

```html
<section class="maryland-visual-link-collection" aria-labelledby="id-iw3e8mw6os8">
  <div class="maryland-card-group__header">
    <div class="maryland-card-group__header-content">
      <h2 class="maryland-card-group__title" id="id-iw3e8mw6os8">
        Latest updates
      </h2>
      <p class="maryland-card-group__description">
        Maryland is the perfect place to start your business. Learn about doing business in the state and find grants, and loans for qualified businesses.
      </p>
    </div>
  </div>
  <!-- Card items using Maryland Cards component with Linked variant -->
</section>
```

### Context

Visual Link Collection is a layout template component in MDWDS that combines a section header with the Maryland Cards component in Linked variant. It provides a reusable pattern for organizing related resources or topics into grouped, clickable card collections across topic landing pages and resource directories.

---

# Templates

## Action Page

*Templates*

The Action Page is a template for full-page layouts in the Maryland Web Design System that combines a statewide banner and main navigation. It serves as a base page structure for state of Maryland web properties and demonstrates how foundational components like the banner and navigation compose together.

### Key Information

## Key Structure
- Uses `usa-banner` for the statewide banner section with `aria-label="Official website of the State of Maryland"`
- Includes `usa-accordion` within the banner header for the "Here's how you know" toggle
- Uses `maryland-link` and `maryland-link--skipnav` classes for skip navigation link
- Skip navigation link should target `#main-content` for proper accessibility
- Banner button uses `usa-banner__button` with `aria-controls` and `aria-expanded` attributes
- SVG icons are included with `role="img"` and `aria-hidden="true"` for button labels

## Class Names
- `.usa-skipnav`: Skip navigation link
- `.maryland-link`: Base link styling
- `.maryland-link--skipnav`: Skip navigation link modifier
- `.usa-banner`: Banner section container
- `.usa-accordion`: Accordion component within banner
- `.usa-banner__header`: Banner header inner container
- `.usa-banner__inner`: Inner wrapper for banner content
- `.usa-banner__header-text`: Text content in banner header
- `.usa-banner__button`: Toggle button for banner details

## Required Attributes
- Skip link: `href="#main-content"`
- Banner: `aria-label="Official website of the State of Maryland"`
- Banner button: `aria-controls`, `aria-expanded`, `type="button"`
- SVG icons: `role="img"`, `aria-hidden="true"`, `aria-label` for descriptive text

### Implementation

```html
<a class="usa-skipnav maryland-link maryland-link--skipnav" href="#main-content">
  Skip to main content
</a>

<section class="usa-banner" aria-label="Official website of the State of Maryland">
  <div class="usa-accordion">
    <div class="usa-banner__header">
      <div class="usa-banner__inner">
        <p class="usa-banner__header-text">
          An official website of the State of Maryland.
        </p>
        <button type="button" class="usa-banner__button" aria-controls="gov-banner-default" aria-expanded="false">
          Here's how you know 
          <svg role="img" aria-hidden="true" aria-label="Toggle button">
            <!-- SVG icon content -->
          </svg>
        </button>
      </div>
    </div>
  </div>
</section>
```

### Context

The Action Page template demonstrates the foundational composition of MDWDS pages, combining the Statewide Banner and skip navigation patterns that should be present at the top of most Maryland government websites. It serves as the template wrapper within which other components and content are nested.

---

## Agency Homepage

*Templates*

The Agency Homepage is a template that demonstrates the full-page layout for a Maryland state agency website. It serves as a starting point for building agency web properties following MDWDS standards. This template includes the statewide banner, header, navigation, and main content area structure.

### Key Information

## Key Components Included:
- **Statewide Banner**: Uses `usa-banner` class with `usa-accordion` for the expandable section
- **Skip Navigation Link**: Implements accessibility best practice with `usa-skipnav` and `maryland-link maryland-link--skipnav` classes, linking to `#main-content`
- **Banner Text**: Uses `usa-banner__header-text` class for the "An official website of the State of Maryland" text
- **Banner Button**: Uses `usa-banner__button` with `aria-controls="gov-banner-default"` and `aria-expanded="false"` attributes
- **Banner Inner Container**: `usa-banner__inner` wraps header content
- **SVG Icons**: Used with `role="img"` and `aria-hidden="true"` attributes for decorative purposes

## Required ARIA Attributes:
- `aria-label` on the banner section for "Official website of the State of Maryland"
- `aria-controls` on the banner toggle button
- `aria-expanded` state on the banner button
- `role="img"` and `aria-hidden="true"` on decorative SVG elements

## Main Content Reference:
- The skip navigation link targets `#main-content` which should exist on the page

### Implementation

```html
<!-- Skip Navigation Link -->
<a class="usa-skipnav maryland-link maryland-link--skipnav" href="#main-content">
  Skip to main content
</a>

<!-- Statewide Banner -->
<section class="usa-banner" aria-label="Official website of the State of Maryland">
  <div class="usa-accordion">
    <div class="usa-banner__header">
      <div class="usa-banner__inner">
        <p class="usa-banner__header-text">
          An official website of the State of Maryland.
        </p>
        <button type="button" class="usa-banner__button" aria-controls="gov-banner-default" aria-expanded="false">
          Here's how you know
          <svg role="img" aria-hidden="true" aria-label="Toggle button" class="usa-icon">
            <!-- SVG content -->
          </svg>
        </button>
      </div>
    </div>
  </div>
</section>
```

**Notes:**
- The banner serves as the top-level statewide identifier for all Maryland government websites
- The accordion structure allows the banner content to expand/collapse
- The skip navigation link should be the first focusable element on the page
- Maryland-specific styling is applied via `maryland-link` and `maryland-link--skipnav` classes

### Context

The Agency Homepage template establishes the foundational page structure for Maryland state agencies using MDWDS. It composes the Statewide Banner component with header, navigation, and content area layouts to create a consistent, accessible template that agencies can build upon for their specific needs.

---

## Basic Page

*Templates*

The Basic Page template provides the foundational structure for Maryland government web pages, including the required Statewide Banner, Skip to Main Content link, and standard header/navigation framework. This template establishes consistent layout and accessibility patterns across all MDWDS-based pages.

### Key Information


### Key Class Names
- `usa-skipnav` - Skip to main content link class
- `maryland-link` - Maryland-specific link styling
- `maryland-link--skipnav` - Skip nav link modifier
- `usa-banner` - Statewide banner section with `aria-label="Official website of the State of Maryland"`
- `usa-accordion` - Accordion container for banner content
- `usa-banner__header` - Banner header section
- `usa-banner__inner` - Banner inner wrapper
- `usa-banner__header-text` - Text label ("An official website of the State of Maryland.")
- `usa-banner__button` - Toggle button for banner details

### Required ARIA Attributes
- `aria-label` on section (for banner context)
- `aria-controls` on banner toggle button (links to banner accordion ID)
- `aria-expanded` on banner button (initial state: false)
- `role="img"` on SVG icons with `aria-hidden="true"` and `aria-label`

### Structure Requirements
- Skip to main content link must appear first in the page structure
- Statewide banner must be a `<section>` element with appropriate aria-label
- Banner includes an accordion mechanism for expandable content details


### Implementation


```html
<!-- Skip to Main Content Link -->
<a class="usa-skipnav maryland-link maryland-link--skipnav" href="#main-content">
  Skip to main content
</a>

<!-- Statewide Banner Section -->
<section class="usa-banner" aria-label="Official website of the State of Maryland">
  <div class="usa-accordion">
    <div class="usa-banner__header">
      <div class="usa-banner__inner">
        <p class="usa-banner__header-text">
          An official website of the State of Maryland.
        </p>
        <button 
          type="button" 
          class="usa-banner__button" 
          aria-controls="gov-banner-default" 
          aria-expanded="false">
          Here's how you know
          <svg role="img" aria-hidden="true" aria-label="Toggle button">
            <!-- SVG icon content -->
          </svg>
        </button>
      </div>
    </div>
  </div>
</section>
```


### Context

The Basic Page template serves as the starting point for all MDWDS page implementations, establishing required accessibility landmarks and government-mandated elements like the Statewide Banner. It composes with navigation, header, and content components to create complete page layouts.

---

## Landing Page

*Templates*

The Landing Page is a complete page template that serves as the entry point for Maryland state websites. It establishes the visual hierarchy and layout patterns for state government digital properties, combining the Statewide Banner, navigation, hero sections, and content areas into a cohesive full-page design.

### Key Information

### Key Classes and Structure
- `usa-skipnav`: Skip navigation link for accessibility (class: `maryland-link maryland-link--skipnav`)
- `usa-banner`: Statewide Banner section wrapping the official Maryland government message
- `usa-accordion`: Accordion component container within banner
- `usa-banner__header`: Banner header container
- `usa-banner__inner`: Inner wrapper for banner content
- `usa-banner__header-text`: Text content styling for the banner message
- `usa-banner__button`: Button to toggle banner details with aria-controls and aria-expanded attributes

### Required ARIA Attributes
- Skip link: `href="#main-content"` (target ID for keyboard navigation)
- Banner button: `aria-controls="gov-banner-default"`, `aria-expanded="false"` (toggle state management)
- Section: `aria-label="Official website of the State of Maryland"` (descriptive label)

### Important Notes
- The Landing Page template integrates the USWDS (U.S. Web Design System) components with Maryland customizations
- Rendered HTML shows the initial page structure with Storybook loader states
- The actual rendered preview appears to be loading or not fully displayed in the captured HTML

### Implementation

```html
<a class="usa-skipnav maryland-link maryland-link--skipnav" href="#main-content">
  Skip to main content
</a>

<section class="usa-banner" aria-label="Official website of the State of Maryland">
  <div class="usa-accordion">
    <div class="usa-banner__header">
      <div class="usa-banner__inner">
        <p class="usa-banner__header-text">
          An official website of the State of Maryland.
        </p>
        <button 
          type="button" 
          class="usa-banner__button" 
          aria-controls="gov-banner-default" 
          aria-expanded="false">
          Here's how you know
        </button>
      </div>
    </div>
  </div>
</section>
```

### Context

The Landing Page template is the foundational page structure for Maryland state websites, integrating USWDS patterns with Maryland-specific customizations. It combines the Statewide Banner, skip navigation link, and accordion components to provide accessible and recognizable navigation patterns for state government digital properties.

---

## Listing Page

*Templates*

The Listing Page is a template component for displaying searchable, filterable collections of items such as news articles or listings on Maryland.gov. It provides a form-based interface with text and select filters, combined with a prose introduction section. Use this template when you need to present multiple items with user-controlled filtering capabilities.

### Key Information


**Key Classes:**
- `maryland-listing__body` – Main body section containing introductory prose
- `maryland-listing__form` – Form wrapper containing all filter controls
- `maryland-listing__filter` – Individual filter field wrapper
- `maryland-listing__filter--input` – Modifier for text input filter section
- `maryland-listing__filter--select` – Modifier for select dropdown filter section
- `usa-prose` – USWDS class for prose styling on the body section
- `usa-label` – USWDS label component
- `usa-input` – USWDS text input component
- `usa-select` – USWDS select dropdown component

**Structure:**
- The component contains two main sections: a body section with descriptive prose and a form section with filters
- Filters use modifier classes (`--input`, `--select`) to distinguish between filter types
- Form controls utilize USWDS base components (usa-input, usa-select, usa-label)
- Text input filter includes standard input attributes (type="text", id, name, size)
- Select filter includes option elements (markup appears incomplete in source)


### Implementation


```html
<div class="maryland-listing__body usa-prose">
  <p>Search through news items for Maryland.gov.</p>
</div>

<form class="maryland-listing__form">
  <div class="maryland-listing__filter maryland-listing__filter--input">
    <label class="usa-label" for="input-type-text">Filter text</label>
    <input class="usa-input" id="input-type-text" name="input-type-text" size="35" type="text">
  </div>

  <div class="maryland-listing__filter maryland-listing__filter--select">
    <label class="usa-label" for="options">Filter select</label>
    <select class="usa-select" name="options" id="options">
      <option>Select an option</option>
    </select>
  </div>
</form>
```


### Context

The Listing Page template integrates with USWDS form components (usa-label, usa-input, usa-select) and combines them with Maryland-specific layout and filtering patterns. It serves as a container for implementing searchable, filtered content listings across Maryland.gov applications.

---

## Listing Page

*Templates*

The Listing Page is a template component for displaying collections of items in a structured list format. It provides the foundational layout and structure for pages that need to present multiple records or entries. This template is used when you need a standardized way to display filterable, paginated, or organized item listings on Maryland state websites.

### Key Information

The Listing Page template is a container template that composes with other MDWDS components to create a full page layout. Key classes visible in the Storybook wrapper:

- `.usa-skipnav` - Skip navigation link for accessibility
- `.maryland-link` - Maryland-specific link styling
- `.maryland-link--skipnav` - Skip navigation link variant
- `.usa-banner` - Statewide banner wrapper (USWDS)
- `.usa-accordion` - Accordion functionality for banner expansion
- `.usa-banner__header` - Banner header container
- `.usa-banner__inner` - Banner inner wrapper
- `.usa-banner__header-text` - Banner header text
- `.usa-banner__button` - Banner toggle button

Required ARIA attributes:
- `aria-label` on the banner section for semantic identification
- `aria-controls` on banner button pointing to accordion ID
- `aria-expanded` on banner button for state management
- `role="img"` on SVG elements
- `aria-hidden="true"` on decorative SVGs

The template utilizes USWDS components (banner, accordion) as foundational elements and Maryland-specific link styling for skip navigation.

### Implementation

```html
<a class="usa-skipnav maryland-link maryland-link--skipnav" href="#main-content">
  Skip to main content
</a>

<section class="usa-banner" aria-label="Official website of the State of Maryland">
  <div class="usa-accordion">
    <div class="usa-banner__header">
      <div class="usa-banner__inner">
        <p class="usa-banner__header-text">
          An official website of the State of Maryland.
        </p>
        <button type="button" class="usa-banner__button" aria-controls="gov-banner-default" aria-expanded="false">
          Here's how you know
          <svg role="img" aria-hidden="true" aria-label="Toggle button">
            <!-- SVG content -->
          </svg>
        </button>
      </div>
    </div>
  </div>
</section>

<main id="main-content">
  <!-- Listing page content goes here -->
</main>
```

### Context

The Listing Page template serves as the primary template for displaying collections within the MDWDS system. It integrates the USWDS banner and accordion components at the top of the page and provides the structural foundation that other content components (cards, tables, filters) can be composed into to create complete listing experiences.

---

## Location Page

*Templates*

The Location Page is a template that provides a standardized layout for displaying location or facility information within Maryland government websites. It serves as a reusable template pattern that integrates core MDWDS components like the statewide banner and skip navigation link. This template ensures consistency and accessibility across location-based pages in the Maryland Web Design System.

### Key Information


**Key Components:**
- Statewide banner section with `usa-banner` class
- Skip navigation link with `maryland-link maryland-link--skipnav` classes
- Accordion component within banner (`usa-accordion`)
- Banner header with `usa-banner__header`, `usa-banner__inner`, and `usa-banner__header-text` classes
- Banner button with `usa-banner__button` class
- Proper ARIA attributes for accessibility: `aria-label`, `aria-controls`, `aria-expanded`

**CSS Class Names:**
- `.usa-skipnav` - Skip navigation link
- `.maryland-link` - Maryland-specific link styling
- `.maryland-link--skipnav` - Skip nav link modifier
- `.usa-banner` - Main banner section wrapper
- `.usa-accordion` - Accordion container
- `.usa-banner__header` - Banner header block
- `.usa-banner__inner` - Inner banner container
- `.usa-banner__header-text` - Header text styling
- `.usa-banner__button` - Banner toggle button

**Required Attributes:**
- `aria-label` on section for semantic description
- `type="button"` on banner button
- `aria-controls` linking button to accordion ID
- `aria-expanded` for toggle state management
- `role="img"` on SVG icons with `aria-hidden="true"` when decorative


### Implementation


```html
<a class="usa-skipnav maryland-link maryland-link--skipnav" href="#main-content">
  Skip to main content
</a>

<section class="usa-banner" aria-label="Official website of the State of Maryland">
  <div class="usa-accordion">
    <div class="usa-banner__header">
      <div class="usa-banner__inner">
        <p class="usa-banner__header-text">
          An official website of the State of Maryland.
        </p>
        <button type="button" class="usa-banner__button" aria-controls="gov-banner-default" aria-expanded="false">
          Here's how you know
          <svg role="img" aria-hidden="true" aria-label="Toggle button">
            <!-- Icon SVG content -->
          </svg>
        </button>
      </div>
    </div>
  </div>
</section>
```


### Context

The Location Page template is part of the MDWDS Templates category and provides a standardized page structure that incorporates foundational components like the Statewide Banner and accessibility features such as skip navigation. It serves as a starting point for building location-specific pages that maintain consistency with Maryland government web standards.

---

## Maryland Homepage

*Templates*

The Maryland Homepage is a full-page template that demonstrates the complete layout and structure of Maryland's official state website. It serves as the primary entry point for citizens and includes the state banner, navigation, and main content areas. Use this template as the foundation for all Maryland-branded web pages requiring consistent state identity and accessibility.

### Key Information

**Key Classes:**
- `usa-skipnav` - Skip navigation link for accessibility
- `maryland-link` - Maryland-specific link styling
- `maryland-link--skipnav` - Modifier for skip navigation link styling
- `usa-banner` - Statewide banner container
- `usa-accordion` - Accordion component within banner
- `usa-banner__header` - Banner header section
- `usa-banner__inner` - Inner container for banner content
- `usa-banner__header-text` - Banner text content
- `usa-banner__button` - Banner toggle button

**Required ARIA Attributes:**
- `aria-label` on banner section (describes purpose)
- `aria-controls` on banner button (references controlled element ID)
- `aria-expanded` on banner button (indicates expanded state, starts as "false")
- `role="img"` on SVG icons
- `aria-hidden="true"` on decorative SVG elements
- `aria-label` on SVG for descriptive purposes when needed

**HTML Structure:**
- Skip navigation link placed at top for keyboard accessibility
- Statewide banner with accordion pattern for "Here's how you know" section
- Banner includes SVG toggle button with proper ARIA attributes

### Implementation

```html
<a class="usa-skipnav maryland-link maryland-link--skipnav" href="#main-content">
  Skip to main content
</a>

<section class="usa-banner" aria-label="Official website of the State of Maryland">
  <div class="usa-accordion">
    <div class="usa-banner__header">
      <div class="usa-banner__inner">
        <p class="usa-banner__header-text">
          An official website of the State of Maryland.
        </p>
        <button 
          type="button" 
          class="usa-banner__button" 
          aria-controls="gov-banner-default" 
          aria-expanded="false"
        >
          Here's how you know 
          <svg role="img" aria-hidden="true" aria-label="Toggle button">
            <!-- SVG content -->
          </svg>
        </button>
      </div>
    </div>
  </div>
</section>
```

**Accessibility Features:**
- Skip navigation link at the top allows keyboard users to jump to main content
- Banner section clearly labeled with `aria-label`
- Button state controlled via `aria-expanded` attribute
- SVG icons properly marked as decorative with `aria-hidden="true"` or labeled appropriately

### Context

The Maryland Homepage template establishes the foundational page structure for all Maryland state websites. It begins with the statewide banner—a required component that clearly identifies the site as an official government resource—followed by navigation and main content areas. This template ensures consistent branding, accessibility compliance, and proper information hierarchy across all Maryland web properties.

---

## News Page

*Templates*

The News Page is a template component that demonstrates how to structure a news or article-focused page within the MDWDS. It combines the Statewide Banner, skip navigation link, and page layout patterns to create a consistent news article presentation. Use this template as a starting point for creating news, blog, or article pages that follow Maryland Design System standards.

### Key Information

### Key Classes and Attributes

- **Skip Navigation Link**: `usa-skipnav`, `maryland-link`, `maryland-link--skipnav` — provides accessible skip-to-content functionality
- **Statewide Banner**: Uses `usa-banner` section with `usa-accordion` for the collapsible "Official website of Maryland" section
- **Banner Header**: `usa-banner__header`, `usa-banner__inner`, `usa-banner__header-text` — contains the official state website text
- **Banner Button**: `usa-banner__button` with `aria-controls="gov-banner-default"` and `aria-expanded="false"` for toggling the banner details

### ARIA Attributes
- `aria-label="Official website of the State of Maryland"` on the banner section
- `aria-controls` and `aria-expanded` on the toggle button for accessible state management
- `role="img"` and `aria-hidden="true"` on SVG icons within the button

### Important Facts
- The News Page template starts with the standard Maryland header/banner pattern
- Skip navigation link uses the ID anchor `#main-content` as the target
- The banner follows USA Design System (USWDS) conventions with `usa-*` class naming
- The template is designed to be extended with additional main content sections below the banner

### Implementation

```html
<a class="usa-skipnav maryland-link maryland-link--skipnav" href="#main-content">
  Skip to main content
</a>

<section class="usa-banner" aria-label="Official website of the State of Maryland">
  <div class="usa-accordion">
    <div class="usa-banner__header">
      <div class="usa-banner__inner">
        <p class="usa-banner__header-text">
          An official website of the State of Maryland.
        </p>
        <button 
          type="button" 
          class="usa-banner__button" 
          aria-controls="gov-banner-default" 
          aria-expanded="false">
          Here's how you know 
          <svg role="img" aria-hidden="true" aria-label="Toggle button">
            <!-- SVG icon content -->
          </svg>
        </button>
      </div>
    </div>
  </div>
</section>

<!-- Main content follows with id="main-content" -->
```

### Variant Notes
The template renders the standard Statewide Banner at the top. Additional page content (hero section, news article content, sidebar) would follow the banner structure, anchored by `id="main-content"` for the skip navigation target.

### Context

The News Page template provides the foundational structure for news and article pages in the MDWDS, combining the Statewide Banner component with skip navigation accessibility patterns. It demonstrates proper composition of header elements and accessibility features (ARIA labels, skip links) that should be present on all Maryland web pages.

---

## Search Page

*Templates*

The Search Page is a template that provides a full-page search interface for Maryland Web Design System implementations. It solves the problem of allowing users to discover and filter content across an entire website. Use this template when you need a dedicated, accessible search experience that follows MDWDS patterns.

### Key Information

This is a page template that includes standard MDWDS page structure components:

**Key Components Included:**
- `usa-skipnav` - Skip navigation link with class `maryland-link maryland-link--skipnav`
- `usa-banner` - Statewide banner section with aria-label for accessibility
- `usa-accordion` - Accordion component within the banner for expandable content
- `usa-banner__header` - Banner header container
- `usa-banner__inner` - Inner wrapper for banner content
- `usa-banner__header-text` - Text element within banner header
- `usa-banner__button` - Interactive button with aria-controls and aria-expanded attributes

**Required Attributes:**
- The banner button requires `aria-controls`, `aria-expanded`, and `type="button"`
- The banner section requires `aria-label` for semantic meaning
- SVG elements should have `role="img"`, `aria-hidden="true"`, and `aria-label` attributes

**Accessibility:**
This template prioritizes accessibility with skip navigation links, ARIA labels, and proper button semantics.

### Implementation

```html
<a class="usa-skipnav maryland-link maryland-link--skipnav" href="#main-content">
  Skip to main content
</a>

<section class="usa-banner" aria-label="Official website of the State of Maryland">
  <div class="usa-accordion">
    <div class="usa-banner__header">
      <div class="usa-banner__inner">
        <p class="usa-banner__header-text">
          An official website of the State of Maryland.
        </p>
        <button type="button" class="usa-banner__button" aria-controls="gov-banner-default" aria-expanded="false">
          Here's how you know <svg role="img" aria-hidden="true" aria-label="Toggle button"></svg>
        </button>
      </div>
    </div>
  </div>
</section>
```

### Context

The Search Page template establishes a standardized page structure that integrates the MDWDS header components (skip navigation, statewide banner, and accordion) with search functionality. It provides a foundation for implementing state government search patterns while maintaining consistency with other MDWDS templates.

---

# Utilities

## Layout Grid

*Utilities*

The Layout Grid is a responsive 12-column layout system designed to build flexible, consistent page structures that adapt to various screen sizes. It supports fixed-width, auto-layout, fill, and offset column behaviors using Flexbox principles. Use it whenever you need responsive content layouts with consistent spacing and alignment without custom CSS.

### Key Information

## Variants

- **ThreeColumns**: 3 equal-width columns at tablet and above
- **NumericWidth**: Fixed-width columns using 12-column scale
- **AutoFill**: Flexible columns using auto-sizing and fill
- **ResponsiveMix**: Responsive columns with different widths per breakpoint
- **Offset**: Shifted content using column offsets
- **Gutters**: Demonstrates grid gutter spacing—default, small, and large

## CSS Class Names

### Container & Row
- `grid-container` – Constrains grid within page margins
- `grid-row` – Wraps columns in a flex row

### Column Classes
- `grid-col` – Base column class
- `grid-col-auto` – Flexible, content-driven columns
- `grid-col-fill` – Fill available space equally
- `grid-col-6` – Fixed-width 6-column (50% of 12-column grid)
- `tablet:grid-col` – Responsive column width at tablet breakpoint and above
- `tablet:grid-col-4` – Fixed 4-column width at tablet breakpoint
- Numeric modifiers: `grid-col-1` through `grid-col-12`
- Responsive prefixes: `tablet:`, `desktop:`, `widescreen:` before column classes

### Offset Classes
- `grid-col-offset-*` – Shift columns; e.g., `grid-col-offset-3` offsets by 3 columns

### Gutter Variants
- Default gutter spacing
- Small gutters
- Large gutters

### Utility Combinations
Often combined with presentation utilities:
- `padding-2`, `margin-top-2` – Spacing
- `text-center` – Text alignment
- `bg-base-lightest` – Background color
- `border` – Border styling
- `font-mono` – Font styling

## Required Attributes
- No ARIA attributes required; grids are visual constructs only
- Use semantic heading levels and landmarks inside the grid for accessibility

## Important Facts
- Grid system is based on Flexbox
- Mirrors U.S. Web Design System (USWDS) principles with usa-specific class names
- Responsive breakpoints support mobile-first design patterns
- Should not affect semantic structure of content

### Implementation

```html
<!-- Basic Three-Column Layout (Responsive at Tablet) -->
<div class="grid-container">
  <div class="grid-row">
    <div class="tablet:grid-col bg-base-lightest padding-2 border text-center font-mono">
      tablet:grid-col
    </div>
    <div class="tablet:grid-col bg-base-lightest padding-2 border text-center font-mono">
      tablet:grid-col
    </div>
    <div class="tablet:grid-col bg-base-lightest padding-2 border text-center font-mono">
      tablet:grid-col
    </div>
  </div>
</div>
```

```html
<!-- Fixed-Width Columns (Numeric Width) -->
<div class="grid-container">
  <div class="grid-row">
    <div class="grid-col-6">
      <!-- 50% width content -->
    </div>
    <div class="grid-col-6">
      <!-- 50% width content -->
    </div>
  </div>
</div>
```

```html
<!-- Auto-Fill Layout -->
<div class="grid-container">
  <div class="grid-row">
    <div class="grid-col-auto">
      <!-- Auto-sized content -->
    </div>
    <div class="grid-col-fill">
      <!-- Fills remaining space -->
    </div>
  </div>
</div>
```

```html
<!-- Responsive Mix with Multiple Breakpoints -->
<div class="grid-container">
  <div class="grid-row">
    <div class="grid-col-12 tablet:grid-col-6 desktop:grid-col-4">
      <!-- Full width mobile, half at tablet, third at desktop -->
    </div>
    <div class="grid-col-12 tablet:grid-col-6 desktop:grid-col-4">
      <!-- Same responsive behavior -->
    </div>
    <div class="grid-col-12 tablet:grid-col-12 desktop:grid-col-4">
      <!-- Full width until desktop -->
    </div>
  </div>
</div>
```

```html
<!-- Offset Columns -->
<div class="grid-container">
  <div class="grid-row">
    <div class="grid-col-6 grid-col-offset-3">
      <!-- Offset by 3 columns, 50% width -->
    </div>
  </div>
</div>
```

### Context

The Layout Grid is a foundational utility in the MDWDS that provides responsive column-based layouts. It composes with other utility classes (spacing, colors, typography) and serves as the backbone for page structure and content organization across the design system, following USWDS conventions.

---

# Other

## Adopt Conventional Comments for Code Reviews (ADR)

*Other*

This is an Architecture Decision Record (ADR) documenting the team's adoption of Conventional Comments as a structured framework for code review feedback. Conventional Comments categorizes review feedback (nitpick, suggestion, issue, question, praise) to improve clarity, reduce ambiguity, and foster a collaborative review culture. Use this ADR as a reference for understanding and implementing the code review standards across MDWDS repositories.

### Key Information

**Conventional Comments Labels:**
- `nitpick`: for small changes that are optional but improve code style or readability
- `suggestion`: for recommended changes that are non-blocking
- `issue`: for problems that must be addressed before merging
- `question`: for clarifications or understanding
- `praise`: for positive reinforcement or acknowledgment of good work

**Comment Structure:**
All reviewers must use the format: `[label]: [comment]`

Example: `suggestion: Consider renaming this variable to better reflect its purpose.`

**Status:** Accepted  
**Date:** 2025-06-18

**Key Benefits:**
- Improves clarity and actionability of code review feedback
- Reduces ambiguity and fosters respect and collaboration
- Helps new contributors understand what is required
- Makes review process more consistent across team

**Implementation Notes:**
- All code review feedback across repositories must follow this convention
- Team onboarding and contribution guidelines should reference this ADR
- Small learning curve expected during adoption phase

### Implementation

This is a documentation/guidance page with no interactive components or structured markup examples to extract. The page consists primarily of prose content rendered via Storybook's documentation view, using standard semantic HTML headings, paragraphs, and links. There are no MDWDS-specific component implementations, class patterns, or ARIA structures to document.

The page contains:
- Standard heading hierarchy (`<h1>`, `<h2>`)
- Paragraph text (`<p>`) with inline links
- Horizontal rule separator (`<hr>`)
- Status metadata (Accepted, Date: 2025-06-18)
- Structured sections with emoji prefixes (🚀, ✅, ⚖️, 👨🏾‍💻)

No component code blocks or implementation examples are provided.

### Context

This ADR document is part of the MDWDS developer documentation and governance structure, establishing standardized practices for code reviews across the design system. It serves as a reference guide for all contributors and maintainers working within the MDWDS ecosystem.

---

## Adopt Conventional Commits for Versioning and Clarity (ADR)

*Other*

This is an Architecture Decision Record (ADR) documenting the adoption of Conventional Commits specification across all MDWDS projects. It standardizes commit message formats to enable semantic versioning, automatic changelog generation, and improved code history clarity. This decision supports long-term project sustainability and better collaboration across contributors.

### Key Information

**Commit Message Structure:**
- Format: `<type>[optional scope]: <description>`
- Optional body and footer sections for additional context

**Supported Commit Types:**
- `feat` – A new feature
- `fix` – A bug fix
- `docs` – Documentation changes only
- `style` – Formatting, whitespace, etc. (no code changes)
- `refactor` – Code change that neither fixes nor adds a feature
- `test` – Adding or fixing tests
- `chore` – Maintenance tasks (e.g., bumping deps)
- `ci` – CI/CD configuration or scripts
- `perf` – Performance improvements
- `build` – Changes that affect the build system or deps

**Key Benefits:**
- Enables semantic versioning and automatic changelog generation
- Provides consistent, meaningful history across all projects
- Makes it easier for new contributors to understand changes
- Supports tools like semantic-release and release-please

**Consequences:**
- Requires learning curve and upfront discipline from contributors
- Teams need to lint and enforce commit message standards

### Implementation

```html
<!-- Example conventional commits (text format): -->

feat(auth): add login redirect after signup
fix(forms): handle null values in required fields
docs(readme): update contributing guidelines
chore(deps): bump astro from 3.5 to 3.6

<!-- Full commit message structure: -->
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Context

This ADR establishes a development standard for the MDWDS project that affects all contributors and CI/CD workflows. By standardizing commit messages, the system enables automated versioning, changelog generation, and integration with modern development tools across the design system ecosystem.

---

## Changelog

*Other*

The Changelog is a documentation page that tracks version history and release notes for the Maryland Web Design System. It documents features, bug fixes, documentation updates, and other changes across multiple versions. This page serves as a reference for developers to understand what has changed between releases and plan updates to their projects.

### Key Information

This is a documentation-only page with no interactive components or variants. The page displays a table of contents with collapsible sections for each version, organized by release date in reverse chronological order. Key information includes:

- Version numbers following semantic versioning (e.g., v0.43.0-rc.4576727)
- Release dates
- Categories of changes: Features, Bug Fixes, Documentation, Code Refactoring, Build System, CI/CD, Housekeeping (Chores), and Tests
- No CSS class modifiers or interactive elements to configure

The page uses standard Storybook documentation styling with `sbdocs` wrapper classes and navigation elements.

### Implementation

The Changelog page renders as a documentation-only page using Storybook's default documentation layout. No custom component implementation is needed. The page structure consists of:

```html
<div id="storybook-docs">
  <div class="sbdocs sbdocs-wrapper css-3rewwu">
    <aside class="sbdocs sbdocs-toc--custom css-1wizkyk">
      <nav aria-labelledby="_r_0_" class="css-q7khkg">
        <h2 id="_r_0_" class="css-ghy3je">Table of Contents</h2>
        <div class="toc-wrapper">
          <ul class="toc-list">
            <li class="toc-list-item is-active-li">
              <a href="#v0430-rc4576727-2026-03-24" class="toc-link node-name--H2 is-active-link">
                v0.43.0-rc.4576727 (2026-03-24)
              </a>
              <ul class="toc-list is-collapsible">
                <li class="toc-list-item">
                  <a href="#features" class="toc-link node-name--H3">Features</a>
                </li>
              </ul>
            </li>
            <!-- Additional version entries follow same pattern -->
          </ul>
        </div>
      </nav>
    </aside>
  </div>
</div>
```

The navigation uses `toc-list` and `toc-list-item` classes with `is-active-li` and `is-active-link` modifiers for the currently selected version. Collapsible sections use `is-collapsible` and `is-collapsed` classes.

### Context

The Changelog is a reference documentation page within the MDWDS Storybook that helps developers track system updates and changes. It integrates with the Storybook navigation system to provide historical context for the design system's evolution and helps teams stay informed about new features, fixes, and breaking changes across versions.

---

## Exclude USWDS Styles from Core Web Components

*Other*

This is an Architectural Decision Record (ADR) documenting the decision to exclude U.S. Web Design System (USWDS) stylesheets as direct dependencies from core MDWDS Web Components. The decision prevents style conflicts, reduces bundle bloat, and maintains component encapsulation while still adhering to USWDS and MDWDS design principles. This ensures flexibility for consuming applications and improves long-term maintainability of the design system.

### Key Information

**Status:** Accepted  
**Date:** 2025-06-18

**Key Points:**

- Core MDWDS Web Components will not include USWDS stylesheets as direct dependencies
- Components are built using custom design tokens, custom properties, and internal styles without relying on USWDS core, global, or component styles
- Non-core components may reuse USWDS class names or behavior where practical
- All components continue to follow USWDS and MDWDS design standards for look, feel, and accessibility

**Pros:**
- Reduces bundle size by eliminating redundant USWDS styles
- Prevents style conflicts between app-wide USWDS usage and Shadow DOM encapsulation
- Maintains flexibility for applying MDWDS styles to both design system components and consuming applications
- Decouples MDWDS from USWDS Sass architecture for improved maintainability

**Cons:**
- Core components will not automatically receive USWDS updates
- Developers must manually maintain consistency with USWDS design patterns

### Implementation

No rendered component implementation is present on this documentation page. This is an Architectural Decision Record (ADR) containing prose documentation, not a component with HTML structure or code examples.

### Context

This ADR establishes architectural guidance for how MDWDS Web Components relate to and integrate (or do not integrate) with the U.S. Web Design System. It clarifies the design philosophy for the core component library and provides developers with understanding of dependency boundaries between MDWDS and USWDS.

---
