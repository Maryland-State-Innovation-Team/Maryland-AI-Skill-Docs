# Maryland Web Design System (MDWDS) — LLM Skill Document

*Generated 2026-04-02 · 107 components documented*

---

# Maryland Web Design System (MDWDS) — LLM Skill Introduction

## What MDWDS Is

The Maryland Web Design System is the official component library and design standard for Maryland state government web properties, hosted at [designsystem.maryland.gov](https://designsystem.maryland.gov). It exists to ensure that every Maryland agency website shares a consistent visual identity, meets federal and state accessibility requirements (WCAG 2.1 AA), and delivers a coherent citizen experience.

MDWDS is built on top of the **U.S. Web Design System (USWDS)**. This relationship is foundational: MDWDS adopts USWDS components wholesale, extends them with Maryland-specific components, and layers Maryland branding (colors, typography, the state seal) on top of the USWDS token system. In practice this means a page may simultaneously use `usa-` prefixed classes from USWDS and `maryland-` prefixed custom elements or CSS variables from MDWDS. Both are present and valid on the same page.

MDWDS custom web components are prefixed with `maryland-` (e.g., `<maryland-accordion>`, `<maryland-hero>`). CSS custom properties follow the same convention (e.g., `--maryland-color-primary`). This namespace is mandatory and prevents collisions with USWDS classes, third-party libraries, and generic HTML attributes.

---

## CDN Setup

To use MDWDS on a page, include the stylesheet and the JavaScript bundle in `<head>`. Version numbers in CDN URLs use **no `v` prefix** — write `0.36.0`, never `v0.36.0`.

```html
<head>
  <!-- MDWDS styles — load before body content to prevent FOUC -->
  <link
    rel="stylesheet"
    href="https://cdn.maryland.gov/mdwds/0.36.0/css/mdwds.min.css"
  />

  <!-- MDWDS JavaScript bundle (web components and interactive behavior) -->
  <script
    type="module"
    src="https://cdn.maryland.gov/mdwds/0.36.0/js/mdwds.min.js"
  ></script>
</head>
```

**FOUC prevention:** The stylesheet link must appear before any `<body>` content. Because custom web components (`<maryland-*>`) upgrade asynchronously, pages that render components before the JS bundle executes may briefly show unstyled or empty shells. Mitigate this by loading the script as `type="module"` in `<head>` (not deferred at the bottom of `<body>`) and, if needed, adding `visibility: hidden` to the `<body>` with a CSS rule that restores visibility once the `:defined` pseudo-class resolves on your root component.

---

## The Class Naming System

MDWDS uses three parallel naming conventions that coexist on the same page. Understanding each lets you reason about unfamiliar class names without looking them up.

**USWDS classes (`.usa-` prefix):** All USWDS components use this prefix. The pattern is `usa-[component]` for the root element and `usa-[component]__[element]` for child parts. Modifiers append as `usa-[component]--[modifier]`. Examples: `.usa-button`, `.usa-button--secondary`, `.usa-card__header`. When you see `.usa-*` classes, you are working with a USWDS-origin component, even if MDWDS has restyled it.

**MDWDS BEM classes:** Maryland-authored components follow BEM (Block, Element, Modifier). The block is the component name, elements use double underscores, and modifiers use double hyphens: `.card__body`, `.footer__section`, `.promo--dark`. Unlike USWDS classes, these do not carry a `usa-` prefix — they are plain BEM identifiers.

**`maryland-` prefix (web components and CSS variables):** Interactive or encapsulated components are implemented as custom elements (`<maryland-accordion>`) with CSS variables (`--maryland-spacing-unit`). These use Shadow DOM in some cases, meaning external CSS will not pierce their internals without CSS custom properties passed through the host element.

**Practical inference rule:** If a class starts with `usa-`, treat it as USWDS. If it is a custom HTML element starting with `maryland-`, treat it as an MDWDS web component. If it is a plain BEM string with no prefix, it is an MDWDS-authored utility or layout class.

---

## How Components Compose

MDWDS pages are assembled in layers. The **Foundation** layer (colors, typography, spacing tokens, logo) defines the visual language that all other layers consume. **Components** are discrete, reusable UI units — buttons, cards, accordions — that reference foundation tokens. **Templates** are full-page compositions that arrange components into complete, agency-ready page layouts.

Every page should include the structural shell in this order: Statewide Banner → Header (with Logo and Navigation) → optional Utility Nav → main content area → Statewide Footer. Templates like the Maryland Homepage and Agency Homepage demonstrate this exact hierarchy and should be treated as authoritative examples of correct nesting.

Layout is handled by the **Layout Grid** utility, a 12-column flexbox grid using `.grid`, `.grid-row`, and `.grid-col-{n}` classes. Components are placed inside grid columns; they do not manage their own outer spacing. Foundation spacing tokens drive internal padding and margins within components.

---

## Key Things to Get Right

**1. The Statewide Banner is required.** It must appear above every other element on Maryland state pages, including the agency header. Omitting it violates state web standards.

**2. Always pair form inputs with labels using matching `for`/`id` attributes.** MDWDS form components (Input, Select, Textarea, Checkbox, Radio) rely on this pairing for accessibility. Placeholder text is not a substitute for a visible label.

**3. ARIA attributes on interactive components are not optional.** Accordion toggle buttons need `aria-expanded`; modals need `role="dialog"` and `aria-modal="true"`; search containers need `role="search"`. These are specified in component documentation and required for WCAG compliance.

**4. Do not mix USWDS and MDWDS structural wrappers for the same component.** A component is either the USWDS implementation (`.usa-*` classes) or the MDWDS web component (`<maryland-*>`), not both simultaneously. Wrapping `<maryland-accordion>` in `.usa-accordion` markup will produce duplicate behavior and broken accessibility trees.

**5. Custom web component interactivity requires the JS bundle.** `<maryland-*>` elements render as empty shells without the JavaScript module. If a component appears visually broken or non-interactive, the most likely cause is that `mdwds.min.js` failed to load, loaded after the component was parsed, or was included as a non-module script that cannot register custom elements.

---

# Component Reference

# Getting Started

## BEM Convention for CSS

*Getting Started*

BEM (Block, Element, Modifier) is a CSS naming convention that provides a structured and scalable approach to organizing class names in the Maryland Web Design System. It solves the problem of CSS naming ambiguity and specificity conflicts by using a predictable, hierarchical naming pattern. Use BEM when writing CSS for MDWDS components to ensure consistency, maintainability, and clarity across the entire design system.

### Key Information

## BEM Convention Structure

**Block**: A standalone component that is meaningful on its own (e.g., `card`, `button`, `navigation`)
- Represents the highest level of an abstraction or component
- All lowercase with hyphens for multi-word names

**Element**: A part of a block that has no standalone meaning and is always tied to its block (e.g., `card__header`, `button__icon`, `navigation__link`)
- Preceded by double underscores (`__`)
- Cannot exist independently outside the block

**Modifier**: A flag or state that modifies a block or element (e.g., `button--primary`, `card--featured`, `button__icon--disabled`)
- Preceded by double hyphens (`--`)
- Indicates a variation or state of the block or element
- Never used alone—always paired with a block or element

## Key Patterns

- **Block naming**: `block-name`
- **Element naming**: `block-name__element-name`
- **Modifier naming**: `block-name--modifier-name` or `block-name__element-name--modifier-name`
- Use hyphens to separate multiple words within a single name part
- Avoid deeply nested selectors; keep specificity low
- Class names are descriptive and self-documenting
- Modifiers should represent states, variants, or temporary changes

## Benefits

- Predictable and consistent naming across all components
- Low CSS specificity, reducing cascade conflicts
- Easy to scan and understand component structure
- Simplified maintenance and refactoring
- Better collaboration between developers
- Reusable and scalable CSS patterns

### Implementation

```html
<!-- BEM Convention Examples -->

<!-- Block: Simple button component -->
<button class="button">Click me</button>

<!-- Block with modifier: Button with primary style -->
<button class="button button--primary">Submit</button>

<!-- Block with modifier: Button with secondary style -->
<button class="button button--secondary">Cancel</button>

<!-- Block with element and modifier: Button with icon -->
<button class="button button--icon">
  <span class="button__icon button__icon--left">
    <!-- Icon SVG or content -->
  </span>
  Button Text
</button>

<!-- Block: Card component with multiple elements -->
<div class="card">
  <div class="card__header">
    <h2 class="card__title">Card Title</h2>
  </div>
  <div class="card__body">
    <p class="card__text">Card content goes here.</p>
  </div>
  <div class="card__footer">
    <button class="card__action">Action</button>
  </div>
</div>

<!-- Block with modifier: Featured card variant -->
<div class="card card--featured">
  <div class="card__header">
    <h2 class="card__title">Featured Card</h2>
  </div>
  <div class="card__body">
    <p class="card__text">This is a featured card variant.</p>
  </div>
</div>

<!-- Complex component: Navigation with BEM -->
<nav class="navigation">
  <ul class="navigation__list">
    <li class="navigation__item">
      <a href="#" class="navigation__link navigation__link--active">Home</a>
    </li>
    <li class="navigation__item">
      <a href="#" class="navigation__link">About</a>
    </li>
    <li class="navigation__item">
      <a href="#" class="navigation__link navigation__link--disabled">Services</a>
    </li>
  </ul>
</nav>
```

## CSS Examples with BEM

```css
/* Block: Button component */
.button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}

/* Modifier: Primary button variant */
.button--primary {
  background-color: #0066cc;
  color: white;
}

/* Modifier: Secondary button variant */
.button--secondary {
  background-color: #f0f0f0;
  color: #333;
  border: 1px solid #ccc;
}

/* Element: Button icon */
.button__icon {
  display: inline-block;
  margin-right: 8px;
}

/* Element modifier: Icon on the right */
.button__icon--right {
  margin-right: 0;
  margin-left: 8px;
}

/* Block: Card component */
.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

/* Element: Card header */
.card__header {
  padding: 16px;
  background-color: #f9f9f9;
  border-bottom: 1px solid #ddd;
}

/* Element: Card title */
.card__title {
  margin: 0;
  font-size: 1.25rem;
}

/* Element: Card body */
.card__body {
  padding: 16px;
}

/* Element: Card text */
.card__text {
  margin: 0;
  line-height: 1.5;
}

/* Element: Card footer */
.card__footer {
  padding: 16px;
  background-color: #f9f9f9;
  border-top: 1px solid #ddd;
}

/* Modifier: Featured card variant */
.card--featured {
  border: 2px solid #0066cc;
  box-shadow: 0 4px 8px rgba(0, 102, 204, 0.2);
}
```

### Context

BEM Convention is a foundational CSS architecture standard for the Maryland Web Design System that all component developers must follow. It ensures consistency, scalability, and maintainability across all MDWDS components, making it easier for developers to understand and extend the system while maintaining low specificity and avoiding cascade conflicts.

---

## Choose Web Component Framework

*Getting Started*

This is an Architecture Decision Record (ADR) documenting the decision-making process for selecting a web component framework for the Maryland Web Design System. It provides developers with guidance on the technical approach and rationale behind framework choices to ensure consistency and best practices across Maryland state web projects.

### Key Information

This page serves as a technical documentation resource for developers implementing the MDWDS. Key aspects include:

- **Purpose**: Architecture Decision Record (ADR) documenting framework selection rationale
- **Audience**: Developers building with MDWDS components
- **Content Type**: Technical decision documentation and guidelines
- **Framework Guidance**: Documents the evaluated options and reasoning for web component framework choices
- **Use Case**: Reference material for understanding the technical foundation of MDWDS component architecture
- **Documentation Pattern**: Follows ADR format to provide historical context and decision justification

### Implementation

This page is primarily documentation rather than a component with HTML implementation. It serves as a reference document explaining framework decisions:

```
<!-- ADR Page Structure -->
<main>
  <article class="adr-document">
    <h1>Choose Web Component Framework</h1>
    <!-- ADR content includes: -->
    <!-- - Decision context and problem statement -->
    <!-- - Options evaluated -->
    <!-- - Rationale for selection -->
    <!-- - Consequences and implications -->
    <!-- - Implementation guidance -->
  </article>
</main>
```

The page is accessed as part of the Storybook documentation system and provides context for how components should be built and used throughout MDWDS projects.

### Context

This ADR is foundational documentation for the MDWDS and provides developers with the technical decision-making background needed to understand why MDWDS components are architected in a particular way. It serves as essential reference material for developers implementing, extending, or maintaining components within the design system.

---

## Developers Documentation - ADR Readme

*Getting Started*

This is the Architecture Decision Records (ADR) documentation index for the Maryland Web Design System developers section. It provides guidance and context for developers implementing the design system and understanding key architectural decisions made during MDWDS development.

### Key Information

This page serves as an entry point to developer-focused documentation and architectural decision records. It typically contains links to various ADRs that document technical decisions, implementation patterns, and best practices for working with the Maryland Web Design System. ADRs are structured documents that explain the reasoning behind significant technical choices in the system.

### Implementation

This is a documentation index page rather than a component with HTML implementation. Navigation is handled through the Storybook interface, with the sidebar providing access to individual ADR documents and developer resources.

### Context

This documentation page is part of the MDWDS developer resources and helps developers understand the architectural foundations and decision-making process behind the design system. It connects developers to specific technical documentation and implementation guidance for building Maryland state web properties.

---

## Docs - Table of Contents

*Getting Started*

This is the documentation index page for the Maryland Web Design System (MDWDS) Storybook. It serves as the central navigation hub providing access to all components, foundation guidelines, and resources available in the design system. Users navigate to this page to find and access specific documentation for building Maryland state web pages.

### Key Information


This page acts as the main table of contents for the MDWDS Storybook documentation. It provides:
- Navigation to all component documentation pages
- Organization of content into logical categories (Foundation, Components, Templates, Utilities, Getting Started, Other)
- Access points to component specifications, implementation guides, and usage guidelines
- Links to design tokens, accessibility patterns, and state web standards

Key features:
- Toolbar navigation for quick access
- Skip to sidebar functionality for accessibility
- Organized structure reflecting the design system architecture
- Central entry point for all MDWDS documentation and resources


### Implementation


```html
<!-- Main Documentation Container -->
<div class="docs-container">
  <header>
    <div class="toolbar">
      <button class="skip-link">Skip to sidebar</button>
    </div>
  </header>
  
  <nav class="docs-sidebar" id="docs-sidebar">
    <!-- Navigation structure would include links to categories:
         - Getting Started
         - Foundation
         - Components
         - Templates
         - Utilities
         - Other
    -->
  </nav>
  
  <main class="docs-content">
    <!-- Table of Contents content displays here -->
  </main>
</div>
```


### Context

This is the foundational entry point and organizational hub of the Maryland Web Design System Storybook. It structures access to all design system resources and serves as the primary navigation mechanism for developers and designers building Maryland state web properties.

---

## Exclude USWDS Styles from Core Web Components

*Getting Started*

This is an architectural decision record (ADR) documenting the approach to exclude U.S. Web Design System (USWDS) styles from Maryland's core web components. It outlines the technical strategy for maintaining component style independence and preventing style conflicts when integrating USWDS with the MDWDS component library.

### Key Information

This ADR addresses the need to isolate core web components from USWDS styling to ensure component autonomy and reduce style pollution. Key considerations include:

- **Problem**: Direct inheritance of USWDS styles can cause unintended style cascading and conflicts within core components
- **Solution Approach**: Encapsulation strategies to scope component styles independently
- **CSS Isolation**: Components should maintain their own style definitions without reliance on USWDS cascade
- **Integration Pattern**: Clear separation between component-level styles and framework-level utilities
- **Best Practice**: Use CSS custom properties and component-level scoping to maintain style boundaries
- **Relevance**: Critical for developers building custom components or extending existing MDWDS components

### Implementation

This is an architectural decision document rather than a code component. The implementation guidance focuses on:

```html
<!-- Strategy: Use CSS scoping and custom properties -->
<!-- Avoid direct USWDS class inheritance in core components -->
<div class="md-component md-component--isolated">
  <!-- Component structure -->
  <!-- Component styles defined independently -->
  <!-- Custom properties for theming -->
</div>
```

**Key Implementation Patterns:**
- Use BEM (Block Element Modifier) naming to prevent style conflicts
- Define component styles in isolated stylesheets
- Leverage CSS custom properties for themeable values
- Avoid cascading from parent USWDS utility classes
- Use CSS modules or similar encapsulation if applicable

### Context

This ADR provides architectural guidance for developers building and extending MDWDS components. It establishes the principle that core components maintain style independence from USWDS, ensuring consistent component behavior across different implementation contexts and preventing unexpected style interactions when USWDS is present in the page.

---

## Getting Started for Engineers

*Getting Started*

This is the foundational guide for engineers implementing the Maryland Web Design System (MDWDS) on state web pages. It provides essential setup instructions, development workflow guidance, and integration patterns needed to build compliant Maryland state websites. Engineers should reference this when beginning a new project or integrating MDWDS components into existing applications.

### Key Information

This page serves as the entry point for developers joining an MDWDS implementation project. Key topics typically covered include:

- **Installation & Setup**: How to install MDWDS packages, dependencies, and build tools
- **Environment Configuration**: Steps to configure local development environments
- **Component Usage**: Patterns for importing and implementing MDWDS components in code
- **Development Workflow**: Standard practices for development, testing, and builds
- **Build Process**: Information about bundling, transpilation, and asset handling
- **Browser Support**: Target browsers and compatibility requirements
- **Accessibility Requirements**: WCAG conformance standards and testing procedures
- **Version Management**: How to track and update MDWDS versions
- **Code Standards**: Linting, formatting, and code quality expectations
- **Documentation References**: Links to component documentation and design guidelines

### Implementation

Getting Started guides typically don't have code implementations themselves, but this page would link to:

```html
<!-- Example: Installation via npm -->
npm install @maryland/design-system

<!-- Example: Component import -->
import { Accordion, Button, Modal } from '@maryland/design-system';

<!-- Example: CSS inclusion -->
<link rel="stylesheet" href="path/to/mdwds.css">
<script src="path/to/mdwds.js"></script>
```

Specific implementation details would be found in individual component documentation pages linked from this guide.

### Context

This Getting Started guide is the primary onboarding resource for the MDWDS and establishes the foundational knowledge required to work with all components, templates, and utilities within the system. It bridges the gap between designers and engineers by providing the technical setup needed to implement design system components correctly.

---

## How to Contribute to MDWDS

*Getting Started*

This is a guide page that explains how developers and designers can contribute to the Maryland Web Design System. It provides instructions, processes, and best practices for participating in the system's development and improvement. Use this when you need to understand contribution workflows, submission processes, or how to participate in MDWDS evolution.

### Key Information

This page serves as documentation for the contribution process to MDWDS. Key sections typically include:

- **Contribution Types**: Guidelines for different contribution methods (bug reports, feature requests, component submissions, documentation improvements)
- **Submission Process**: Step-by-step instructions for how to propose changes, create pull requests, or submit new components
- **Code Standards**: Requirements for code style, naming conventions, accessibility compliance (WCAG), and testing
- **Review Process**: Information about how contributions are reviewed, approved, and merged
- **Component Guidelines**: Requirements for new component submissions including structure, documentation, examples, and accessibility
- **Documentation Requirements**: Standards for documenting components, variants, and usage patterns
- **Getting Started with Development**: Setup instructions for local development environment
- **Communication Channels**: Information about how to ask questions, get feedback, or discuss proposed changes

Important attributes and practices:
- All components must meet WCAG 2.1 AA accessibility standards
- Components should include ARIA roles and attributes where applicable
- Documentation should include usage examples and variant demonstrations
- Code should follow established patterns and conventions within the design system

### Implementation

Contribution pages typically don't have interactive implementations but rather provide documentation. The structure is informational:

```html
<!-- Contribution Guide Structure -->
<main class="mdwds-contribution-guide">
  <section class="contribution-section">
    <h2>Getting Started with Contributions</h2>
    <p>Instructions for setting up a local development environment and understanding the repository structure.</p>
  </section>

  <section class="contribution-section">
    <h2>Submission Process</h2>
    <ol>
      <li>Fork the repository</li>
      <li>Create a feature branch</li>
      <li>Make your changes</li>
      <li>Submit a pull request with documentation</li>
      <li>Address review feedback</li>
    </ol>
  </section>

  <section class="contribution-section">
    <h2>Component Submission Requirements</h2>
    <ul>
      <li>Complete HTML/CSS/JS implementation</li>
      <li>Accessibility compliance (WCAG 2.1 AA)</li>
      <li>Storybook documentation with examples</li>
      <li>Usage guidelines and best practices</li>
    </ul>
  </section>

  <section class="contribution-section">
    <h2>Code Standards</h2>
    <pre><code class="language-markup">
&lt;!-- Follow established component patterns --&gt;
&lt;div class="mdwds-component" role="region" aria-label="Component description"&gt;
  &lt;!-- Semantic HTML structure --&gt;
&lt;/div&gt;
    </code></pre>
  </section>
</main>
```

### Context

This guide page is part of the MDWDS developer documentation and helps contributors understand how to participate in the design system's development. It serves as the gateway for developers and designers who want to add components, fix bugs, or improve documentation, ensuring all contributions meet the system's standards and are properly integrated.

---

## How to Set Up Local Development

*Getting Started*

This guide provides instructions for developers to set up a local development environment for working with the Maryland Web Design System. It covers the prerequisites, installation steps, and configuration needed to run MDWDS components and documentation locally. This is essential for developers who want to contribute to or customize MDWDS for Maryland state web projects.

### Key Information

This documentation page covers:
- Prerequisites and system requirements for local development
- Installation and setup instructions
- Environment configuration
- How to run the development server
- How to build and test components locally
- Common setup issues and troubleshooting

Key aspects include:
- Node.js version requirements
- Package manager setup (npm or yarn)
- Repository cloning and dependency installation
- Development server commands
- Build processes for production-ready components
- Testing and validation procedures

### Implementation

The setup process typically involves:

```bash
# Clone the MDWDS repository
git clone https://github.com/maryland/web-design-system.git
cd web-design-system

# Install dependencies
npm install
# or
yarn install

# Start the local development server
npm run dev
# or
yarn dev

# Build for production
npm run build
# or
yarn build

# Run tests
npm test
# or
yarn test
```

Developers should follow the step-by-step instructions provided in the documentation to configure their environment, including setting environment variables if needed and ensuring all dependencies are properly installed before starting development work.

### Context

This Getting Started guide is the foundational resource that enables developers to begin working with all other MDWDS components, templates, and utilities. It establishes the development environment necessary for understanding and implementing the design system across Maryland state web projects.

---

## How to Use MDWDS - Readme

*Getting Started*

This is the introductory documentation page for the Maryland Web Design System (MDWDS) that provides guidance on how to get started and navigate the design system. It serves as the entry point for developers and designers beginning to work with MDWDS components and patterns.

### Key Information

This page is part of the developers documentation section and acts as the primary "How To" guide for the design system. Key topics typically covered in such readme pages include:

- **Purpose**: Overview of MDWDS and its goals for creating consistent Maryland state web experiences
- **Getting Started**: Instructions for installation and initial setup
- **Navigation**: How to browse and find components in the Storybook
- **Usage Patterns**: Common patterns for implementing components
- **Resources**: Links to additional documentation, design files, and support
- **Version Information**: Current version and changelog details
- **Contribution Guidelines**: How to contribute to the design system

The page serves as a central reference document that directs users to appropriate sections of the design system based on their needs (designers, developers, implementers).

### Implementation

```html
<!-- This is typically a documentation page rendered by Storybook's MDX format -->
<!-- It may contain narrative content, embedded code examples, and links -->

<!-- Example of typical Readme structure in Storybook: -->
<div class="storybook-container">
  <h1>How to Use the Maryland Web Design System</h1>
  
  <section>
    <h2>Getting Started</h2>
    <p>Instructions and links to begin using MDWDS...</p>
  </section>
  
  <section>
    <h2>Component Library</h2>
    <p>Overview of available components and where to find them...</p>
  </section>
  
  <section>
    <h2>Documentation</h2>
    <p>Links to detailed component documentation, patterns, and best practices...</p>
  </section>
</div>
```

### Context

This Readme page is the foundational entry point to the MDWDS and establishes how users should approach the design system. It provides context and direction for all other components, patterns, and utilities documented throughout the Storybook.

---

## Need Help?

*Getting Started*

This is a support and guidance page that provides users with resources, documentation, and contact information for getting help with the Maryland Web Design System. It serves as a central hub for troubleshooting, accessing documentation, and connecting with support resources when building or maintaining Maryland state web pages.

### Key Information

This page appears to be a support/help documentation page rather than a component. It likely contains:

- Links to documentation and guides
- Frequently asked questions or common issues
- Contact information for support
- Resources for getting started with MDWDS
- Links to component documentation and examples

As a Getting Started resource, it should be referenced as the primary entry point for new users or developers who need assistance with the design system.

### Implementation

This page is primarily informational and navigational. Standard HTML structure for a help/documentation page:

```html
<div class="help-page-container">
  <h1>Need Help?</h1>
  <!-- Support sections with links to resources -->
  <!-- Links to documentation -->
  <!-- Contact information -->
  <!-- FAQ or common troubleshooting guides -->
</div>
```

The page may not require specific component implementation as it is a documentation/support page.

### Context

This "Need Help?" page serves as a Getting Started resource within the MDWDS Storybook, directing users to relevant documentation, components, and support channels. It acts as a navigation hub that helps developers and content creators find answers and resources when working with other MDWDS components and patterns.

---

## Playwright Testing

*Getting Started*

Playwright Testing is a testing framework and approach for validating Maryland Web Design System components and page implementations. It provides developers with tools and guidance for writing automated tests to ensure components function correctly and meet accessibility standards. This is essential for maintaining quality, consistency, and compliance across Maryland state web projects.

### Key Information


Playwright Testing provides a structured testing methodology for the MDWDS:

- **Purpose**: Automated testing framework for validating component behavior, functionality, and accessibility compliance
- **Scope**: Tests UI interactions, visual regression, accessibility (ARIA), responsive design, and cross-browser compatibility
- **Testing Approaches**: 
  - Unit tests for individual component logic
  - Integration tests for component interactions
  - Visual regression tests for UI consistency
  - Accessibility/ARIA attribute validation
  - Cross-browser testing across multiple browsers

- **Key Practices**:
  - Test component states (default, hover, active, disabled, error states)
  - Verify ARIA roles and attributes are correct
  - Validate keyboard navigation and focus management
  - Test responsive breakpoints
  - Confirm CSS classes apply correctly
  - Validate data attributes and custom properties

- **Test Coverage Areas**:
  - Component initialization and rendering
  - User interactions (click, keyboard, form submission)
  - State changes and prop variations
  - Error states and validation messaging
  - Mobile/tablet/desktop responsive behavior
  - Screen reader compatibility


### Implementation


```html
<!-- Playwright Testing Configuration Example -->
<!-- Tests should verify component structure, functionality, and accessibility -->

<!-- Example Test Structure Pattern -->
<script>
// tests/components/accordion.spec.ts - Example testing pattern
import { test, expect } from '@playwright/test';

test.describe('Accordion Component', () => {
  test('should render with correct structure', async ({ page }) => {
    await page.goto('/components/accordion');
    
    // Verify component markup
    const accordion = await page.locator('[role="region"]');
    await expect(accordion).toBeVisible();
  });

  test('should have correct ARIA attributes', async ({ page }) => {
    await page.goto('/components/accordion');
    
    const button = await page.locator('[role="button"][aria-expanded]');
    await expect(button).toHaveAttribute('aria-expanded', 'false');
  });

  test('should toggle expanded state on click', async ({ page }) => {
    await page.goto('/components/accordion');
    
    const button = await page.locator('[role="button"]').first();
    await button.click();
    
    await expect(button).toHaveAttribute('aria-expanded', 'true');
  });

  test('should be keyboard accessible', async ({ page }) => {
    await page.goto('/components/accordion');
    
    const button = await page.locator('[role="button"]').first();
    await button.focus();
    await page.keyboard.press('Enter');
    
    await expect(button).toHaveAttribute('aria-expanded', 'true');
  });

  test('should apply correct CSS classes', async ({ page }) => {
    await page.goto('/components/accordion');
    
    const accordion = await page.locator('.accordion');
    await expect(accordion).toHaveClass(/accordion/);
  });
});
</script>

<!-- Component to be tested -->
<div class="accordion" role="region">
  <button 
    role="button" 
    aria-expanded="false" 
    aria-controls="accordion-panel-1"
    class="accordion__button"
  >
    Accordion Item
  </button>
  <div 
    id="accordion-panel-1" 
    role="region" 
    aria-labelledby="accordion-button-1"
    class="accordion__panel"
    hidden
  >
    <p>Panel content goes here</p>
  </div>
</div>
```


### Context

Playwright Testing is a foundational practice within MDWDS that ensures all components, utilities, and templates meet quality, accessibility, and functionality standards. It integrates with the component development workflow to validate that implementations follow the design system specifications and maintain consistency across Maryland state web projects.

---

## Use `maryland-` Prefix for Web Components and CSS Variables

*Getting Started*

This is an architectural decision document (ADR) that establishes the naming convention for the Maryland Web Design System, requiring all custom web components and CSS variables to use the `maryland-` prefix. This ensures namespace consistency, prevents naming collisions with other libraries, and establishes a clear identity for Maryland state web components across all implementations.

### Key Information

## Naming Convention
- **Web Components**: All custom web components MUST use the `maryland-` prefix (e.g., `<maryland-accordion>`, `<maryland-button>`)
- **CSS Variables**: All custom CSS variables MUST use the `maryland-` prefix (e.g., `--maryland-color-primary`, `--maryland-spacing-unit`)
- **Purpose**: Ensures global namespace isolation and prevents conflicts with third-party libraries
- **Scope**: Applies across all MDWDS components, utilities, and design tokens

## Implementation Standards
- Custom HTML element names must follow Web Components naming requirements (hyphenated, lowercase)
- CSS custom properties should follow a consistent hierarchical naming pattern
- All new components and variables should be reviewed to ensure compliance with this prefix standard

### Implementation

```html
<!-- Web Component Example -->
<maryland-accordion>
  <maryland-accordion-item>
    <h3 slot="header">Accordion Header</h3>
    <p>Accordion content</p>
  </maryland-accordion-item>
</maryland-accordion>

<!-- CSS Variables Example -->
<style>
  :root {
    --maryland-color-primary: #003366;
    --maryland-spacing-unit: 8px;
    --maryland-font-size-base: 16px;
  }
  
  .component {
    color: var(--maryland-color-primary);
    padding: calc(var(--maryland-spacing-unit) * 2);
    font-size: var(--maryland-font-size-base);
  }
</style>
```

### Context

This ADR establishes a foundational naming convention that all MDWDS components, tokens, and utilities must follow to ensure consistency, prevent namespace collisions, and maintain a coherent identity across the entire Maryland state web design ecosystem.

---

## Welcome

*Getting Started*

The Welcome page serves as the entry point and introduction to the Maryland Web Design System (MDWDS) Storybook. It provides orientation for users getting started with the design system and directs them to key documentation and resources. This page establishes the foundation for understanding how to navigate and utilize the MDWDS for building Maryland state web pages.

### Key Information

The Welcome page is the landing page of the MDWDS Storybook documentation site located at designsystem.maryland.gov. It contains:

- Toolbar navigation at the top
- Main navigation sidebar (accessible via skip link)
- Introduction and orientation content for new users
- Links to key sections and documentation resources

The page serves as a navigational hub that helps users understand the structure of the design system and directs them to Foundation (colors, typography, spacing), Components (UI building blocks), Templates (page layouts), Utilities, and other resources.

### Implementation

```html
<!-- Welcome page - Entry point to MDWDS Storybook -->
<html>
<head>
  <title>Welcome - Maryland Web Design System</title>
</head>
<body>
  <!-- Skip link for accessibility -->
  <a href="#sidebar" class="skip-link">Skip to sidebar</a>
  
  <!-- Toolbar -->
  <nav class="toolbar" role="navigation" aria-label="Main toolbar">
    <!-- Toolbar content -->
  </nav>
  
  <!-- Main content area -->
  <main id="main-content">
    <!-- Welcome page content -->
  </main>
  
  <!-- Sidebar with navigation -->
  <aside id="sidebar" role="navigation" aria-label="Documentation sidebar">
    <!-- Sidebar navigation content -->
  </aside>
</body>
</html>
```

### Context

The Welcome page is the primary entry point to the MDWDS documentation system and serves as the organizational hub for all design system resources. It connects users to Foundation elements, Components, Templates, and Utilities that comprise the complete Maryland Web Design System.

---

## When to Use Web Components vs. Standard HTML + CSS in MDWDS

*Getting Started*

This architectural decision record (ADR) provides guidance on choosing between web components and standard HTML + CSS when building features within the Maryland Web Design System. It helps developers understand the trade-offs, performance implications, and use cases for each approach to ensure consistency and maintainability across state web pages.

### Key Information

## Decision Framework

**Web Components (MDWDS Custom Elements):**
- Use for: Complex interactive components with encapsulated state, reusable across multiple projects, components requiring Shadow DOM isolation
- Benefits: Style encapsulation, scoped DOM, reusable across different technology stacks
- Considerations: Larger bundle size, learning curve, JavaScript required for functionality

**Standard HTML + CSS:**
- Use for: Simple layout patterns, static content, components compatible with progressive enhancement
- Benefits: Lighter bundle, better SEO (plain HTML), works without JavaScript, easier for content editors
- Considerations: More CSS to manage, no style encapsulation, potential for style conflicts

## Key Criteria for Selection
- Component complexity and interactivity requirements
- Reusability needs across projects
- Bundle size and performance targets
- Team expertise and maintenance capabilities
- Accessibility requirements (both approaches support WCAG)
- Progressive enhancement priorities

### Implementation

## Decision Guidance

**Choose Web Components when:**
```
- Building complex interactive features (modals, dropdowns, tabs with state)
- Component needs to be used across multiple MDWDS projects
- Style encapsulation is important to prevent CSS conflicts
- You're building a reusable library element
```

**Choose Standard HTML + CSS when:**
```
- Building simple layout patterns and static content blocks
- Supporting progressive enhancement is a priority
- Component complexity is minimal
- You need maximum compatibility with content management systems
- Performance on initial page load is critical
```

## Implementation Pattern

Web Components in MDWDS typically follow this structure:
- Register custom element (e.g., `<mdwds-component>`)
- Define component class extending HTMLElement or similar
- Encapsulate styles in Shadow DOM
- Expose public properties and methods
- Emit custom events for parent communication

Standard HTML + CSS in MDWDS typically follow this structure:
- Semantic HTML structure
- CSS utility classes and component classes
- BEM or similar naming convention for clarity
- Data attributes for progressive enhancement
- Optional data-driven scripting for enhancements

### Context

This ADR serves as architectural guidance for all MDWDS contributors and developers building on the system. It clarifies when to extend the component library with web components versus when to build features using the foundation of HTML and CSS utilities, ensuring consistent decision-making across the design system and its implementations.

---

# Foundation

## Colors

*Foundation*

The Colors page establishes the color palette and guidelines for the Maryland Web Design System. It defines the standardized colors used across all state web pages, ensuring visual consistency and accessibility compliance. Use these colors for all UI components, backgrounds, text, and interactive states throughout Maryland state applications.

### Key Information

## Color Palette Overview

The MDWDS color system includes primary colors, secondary colors, neutral grays, and semantic colors for various UI states and purposes.

## Primary Colors
- **Maryland Blue**: Used for primary actions, links, and brand elements
- **Maryland Gold**: Used for highlights, accents, and secondary actions

## Secondary Colors
- Supporting colors for additional visual variety and semantic meaning

## Neutral Colors
- **Grays**: Range from light backgrounds to dark text, providing contrast hierarchy
- White and black for extremes

## Semantic Colors
- **Success/Green**: Positive actions, confirmations, success states
- **Warning/Yellow**: Cautions, alerts, warnings
- **Error/Red**: Errors, destructive actions, alerts
- **Information/Blue**: Informational messages, help text

## Accessibility
- All colors meet WCAG AA contrast ratio requirements
- Use color in combination with other visual indicators (icons, text, patterns) rather than color alone
- Ensure sufficient contrast between foreground and background colors

## CSS Class Naming
Colors are typically applied through CSS utility classes or design tokens:
- Background colors: `.bg-primary`, `.bg-secondary`, `.bg-success`, `.bg-warning`, `.bg-error`, `.bg-info`
- Text colors: `.text-primary`, `.text-secondary`, `.text-muted`
- Border colors: `.border-primary`, `.border-secondary`

## Implementation Notes
- Use design tokens/CSS variables for consistency
- Never hardcode color hex values in component code
- Apply colors through utility classes or component modifier classes
- Test color combinations for accessibility compliance before deployment

### Implementation

```html
<!-- Primary Button using primary color -->
<button class="btn btn-primary">Primary Action</button>

<!-- Secondary Button using secondary color -->
<button class="btn btn-secondary">Secondary Action</button>

<!-- Success State -->
<div class="alert alert-success">
  <strong>Success!</strong> Your action was completed.
</div>

<!-- Warning State -->
<div class="alert alert-warning">
  <strong>Warning:</strong> Please review before proceeding.
</div>

<!-- Error State -->
<div class="alert alert-error">
  <strong>Error:</strong> Something went wrong.
</div>

<!-- Info State -->
<div class="alert alert-info">
  <strong>Information:</strong> Additional details provided.
</div>

<!-- Text with semantic colors -->
<p class="text-success">This text indicates success</p>
<p class="text-warning">This text indicates a warning</p>
<p class="text-error">This text indicates an error</p>
<p class="text-info">This text provides information</p>

<!-- Background colors -->
<div class="bg-primary text-white padding-3">Primary background</div>
<div class="bg-secondary text-white padding-3">Secondary background</div>

<!-- Using CSS Variables (design tokens) -->
<style>
  .custom-element {
    background-color: var(--color-primary);
    color: var(--color-text-primary);
    border: 2px solid var(--color-border-primary);
  }
</style>
```

### Context

The Colors foundation provides the visual design foundation that all MDWDS components build upon. These standardized colors ensure consistency across components, templates, and utilities while maintaining accessibility standards required for Maryland state web properties.

---

## Full Width

*Foundation*

Full Width is a block spacing utility that enables content to extend across the entire viewport width, breaking out of standard container constraints. It solves the problem of needing full-bleed layouts while maintaining design system consistency. Use this when you need hero sections, background images, or other content that should span edge-to-edge.

### Key Information

- **Purpose**: Extends content to full viewport width, useful for hero sections, banners, and full-bleed backgrounds
- **CSS Class**: `.full-width` or similar utility class for breaking container constraints
- **Block Spacing Context**: Part of the Foundation block spacing system that controls layout spacing patterns
- **Use Cases**: Hero sections, full-width backgrounds, image galleries, color blocks that need to extend beyond normal container widths
- **Integration**: Works with standard container and grid systems; content inside can be constrained with nested containers if needed
- **Responsive**: Adjusts appropriately across breakpoints while maintaining full viewport width

### Implementation

```html
<!-- Full Width Container with content -->
<div class="full-width">
  <div class="container">
    <!-- Content can be constrained here with container class -->
  </div>
</div>

<!-- Full Width with background color or image -->
<div class="full-width" style="background-color: #f5f5f5;">
  <div class="container">
    <h2>Full Width Section</h2>
    <p>Content with constrained width inside full-width container</p>
  </div>
</div>

<!-- Full Width with background image -->
<div class="full-width" style="background-image: url('hero-image.jpg'); background-size: cover;">
  <div class="container">
    <h1>Hero Section</h1>
  </div>
</div>
```

### Context

Full Width is part of the MDWDS Foundation block spacing utilities that define how sections and major content blocks are structured on Maryland state web pages. It complements standard container and grid utilities to enable flexible layout patterns while maintaining design consistency.

---

## Logo

*Foundation*

The Logo component provides the official Maryland state branding element for use across web applications. It establishes visual identity and consistency for state web properties. Use the Logo component in header and branding areas to reinforce Maryland's official presence.

### Key Information

The Logo component includes the Maryland state seal and wordmark. It serves as a foundational branding element and should be used consistently across all Maryland state web properties. The logo may appear in various sizes and contexts, typically in page headers or navigation areas. Key considerations include:

- Official Maryland state seal imagery
- Proper spacing and sizing guidelines
- Use in header/navigation contexts
- Maintains consistent branding across the MDWDS system
- May have responsive sizing variants
- Should include alt text when used as an image element
- Color variations may be available (full color, single color, reversed)

### Implementation

```html
<!-- Standard Logo Implementation -->
<img src="/path/to/maryland-logo.svg" alt="State of Maryland" class="logo" />

<!-- Logo with container/wrapper -->
<div class="logo-container">
  <img src="/path/to/maryland-logo.svg" alt="State of Maryland" class="logo" />
</div>

<!-- Logo as part of header branding -->
<header class="header-branding">
  <img src="/path/to/maryland-logo.svg" alt="State of Maryland" class="logo" />
  <span class="org-name">Agency Name</span>
</header>
```

### Context

The Logo is a foundational branding element of the MDWDS that provides visual identity across all Maryland state web properties. It typically appears in conjunction with header and navigation components to establish consistent state branding and official presence.

---

## Typography

*Foundation*

Typography defines the font families, sizes, weights, and line heights used across Maryland state web pages. It establishes a consistent visual hierarchy and readability standard that applies to all text content, ensuring accessibility and professional presentation across the design system.

### Key Information

Typography is a foundational element that includes:
- **Font Families**: Primary and secondary typefaces used throughout MDWDS
- **Font Sizes**: Standardized size scale for headings, body text, and captions
- **Font Weights**: Regular, medium, semibold, and bold weight options
- **Line Heights**: Proportional line spacing for different text types
- **Letter Spacing**: Tracking adjustments for improved legibility
- **Text Transform**: Options for uppercase, lowercase, and capitalize
- **Utility Classes**: CSS classes for applying typography styles consistently

Typography should be applied using semantic HTML elements (h1-h6, p, span, etc.) combined with MDWDS typography utility classes for consistent styling across all components and pages.

### Implementation

```html
<!-- Heading Levels with Typography Classes -->
<h1 class="text-h1">Heading Level 1</h1>
<h2 class="text-h2">Heading Level 2</h2>
<h3 class="text-h3">Heading Level 3</h3>
<h4 class="text-h4">Heading Level 4</h4>
<h5 class="text-h5">Heading Level 5</h5>
<h6 class="text-h6">Heading Level 6</h6>

<!-- Body Text -->
<p class="text-body">Standard body text paragraph</p>
<p class="text-body-small">Small body text</p>

<!-- Display Text -->
<p class="text-display-large">Display Large</p>
<p class="text-display-medium">Display Medium</p>

<!-- Caption and Label Text -->
<span class="text-caption">Caption text</span>
<label class="text-label">Label text</label>

<!-- Font Weight Modifiers -->
<p class="text-body text-weight-regular">Regular weight</p>
<p class="text-body text-weight-medium">Medium weight</p>
<p class="text-body text-weight-semibold">Semibold weight</p>
<p class="text-body text-weight-bold">Bold weight</p>
```

### Context

Typography is a core Foundation element that provides the stylistic basis for all text content across MDWDS components, templates, and page layouts. It works in conjunction with the Color Palette and Spacing system to create a cohesive visual identity for Maryland state digital properties.

---

## Typography

*Foundation*

Typography defines the typographic system and heading/text styles for the Maryland Web Design System. It establishes consistent font families, sizes, weights, and spacing across all state web pages. Use typography classes to ensure visual hierarchy, readability, and brand consistency throughout Maryland government digital properties.

### Key Information

Typography in MDWDS includes:

**Heading Levels**: Use semantic HTML heading elements (h1–h6) with appropriate class names for styling consistency
- `h1`, `h2`, `h3`, `h4`, `h5`, `h6` - Standard heading elements
- Heading classes can override default styling without changing semantic markup

**Body Text Variants**:
- Standard paragraph text with `<p>` tags
- `.lead` - Larger introductory text for emphasis
- `.usa-body` - Standard body text class
- `.usa-body--small` - Reduced size for secondary information

**Font Stack**:
- Headings: Uses system font stack optimized for clarity
- Body: Uses readable serif or sans-serif depending on context

**Text Modifiers**:
- Bold/strong emphasis: `<strong>` or `<b>`
- Italic emphasis: `<em>` or `<i>`
- `.usa-font-body-xs` through `.usa-font-body-lg` - Size variants
- Text alignment classes for layout control

**Line Height & Spacing**:
- Consistent line-height for readability (typically 1.5–1.6)
- Margin and padding utilities control spacing between elements

**Color Support**:
- Typography works with MDWDS color palette
- Text color classes for emphasis and hierarchy

### Implementation

```html
<!-- Heading Examples -->
<h1>Main Page Title</h1>
<h2>Section Heading</h2>
<h3>Subsection Heading</h3>

<!-- Lead/Introductory Text -->
<p class="lead">This is an important introductory paragraph that stands out with larger, bolder text.</p>

<!-- Standard Body Text -->
<p>Regular paragraph text in the default body font.</p>

<!-- Small Text -->
<p class="usa-body--small">This is secondary or supplementary information in a smaller font.</p>

<!-- Text with Emphasis -->
<p>Use <strong>bold text</strong> for emphasis and <em>italic text</em> for additional context.</p>

<!-- Typography Size Variants -->
<p class="usa-font-body-xs">Extra small body text</p>
<p class="usa-font-body-sm">Small body text</p>
<p class="usa-font-body">Default body text</p>
<p class="usa-font-body-lg">Large body text</p>

<!-- Heading with Optional Class Override -->
<h2 class="usa-heading-xl">Large heading styled with size class</h2>
```

### Context

Typography is a foundational element in MDWDS that establishes visual consistency across all Maryland state web properties. It works in conjunction with the color palette and spacing utilities to create accessible, readable page layouts and establishes the baseline for all text-based content.

---

# Components

## Accordion

*Components*

An accordion is a collapsible content component that displays a list of headers that expand and collapse to reveal or hide associated content sections. It helps organize information into compact, scannable sections and is useful for FAQs, detailed explanations, and managing information hierarchy on pages with limited vertical space.

### Key Information

## Variants
- Single accordion item
- Multiple accordion items (allow multiple sections open simultaneously or only one at a time)
- Accordion with custom icons/styling

## Key CSS Classes
- `.accordion` - Main container class
- `.accordion-item` - Individual accordion item wrapper
- `.accordion-button` - Clickable header that toggles content (should have `aria-expanded` attribute)
- `.accordion-collapse` - Container for collapsible content
- `.accordion-body` - Inner content area of the accordion item

## Required Attributes
- `aria-expanded="true|false"` - On `.accordion-button` to indicate expanded/collapsed state
- `aria-controls` - Links button to its associated content panel
- `id` - Unique identifier for each accordion item and button
- `data-bs-toggle="collapse"` - Enables collapse functionality
- `data-bs-target` - Targets the collapse element to toggle

## Important Facts
- Typically uses Bootstrap accordion structure
- Should support keyboard navigation (Enter/Space to expand/collapse)
- All accordion items should be wrapped in a container with `role="region"` or semantic context
- Collapsed items should have `aria-expanded="false"` and expanded items `aria-expanded="true"`

### Implementation

```html
<div class="accordion" id="accordionExample">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
        Accordion Item #1
      </button>
    </h2>
    <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions.
      </div>
    </div>
  </div>
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
        Accordion Item #2
      </button>
    </h2>
    <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        <strong>This is the second item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element.
      </div>
    </div>
  </div>
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
        Accordion Item #3
      </button>
    </h2>
    <div id="collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        <strong>This is the third item's accordion body.</strong> Nothing more exciting happening here in terms of content, but that's all you need.
      </div>
    </div>
  </div>
</div>
```

## JavaScript Initialization
If using Bootstrap 5+, include Bootstrap's JS bundle:
```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.x.x/dist/js/bootstrap.bundle.min.js"></script>
```

The accordion will automatically initialize with the `data-bs-toggle` and `data-bs-target` attributes.

### Context

The Accordion component is a standard interactive UI element within MDWDS that builds on Bootstrap's collapse utility. It composes with heading and text content components to create organized, accessible content sections and is commonly used in templates for FAQs, policy details, and multi-step forms.

---

## Accordion

*Components*

The Accordion component is a collapsible content container that allows users to expand and collapse sections of content to manage information density. It helps organize related content into logical sections and improves readability by reducing cognitive load. Use accordions when you have multiple sections of content where users need to focus on one section at a time, or when space is limited.

### Key Information

**Variants & Modifiers:**
- Standard accordion with collapsible sections
- Each section can be independently expanded or collapsed
- Only one section can be open at a time (typical behavior)
- Multi-select accordion (if supported) allows multiple sections open simultaneously

**CSS Classes:**
- `.usa-accordion` - Main wrapper class
- `.usa-accordion__heading` - Header element for each section
- `.usa-accordion__button` - Clickable button to toggle section
- `.usa-accordion__content` - Container for expandable content
- `.usa-accordion-item` - Individual accordion item wrapper

**Required Attributes:**
- `aria-expanded` - Boolean attribute on button indicating if section is expanded
- `aria-controls` - Links button to its corresponding content panel
- `id` - Unique identifier for content panels
- `type="button"` - Specifies accordion buttons as buttons, not links

**Important Facts:**
- Accordion buttons must be semantic `<button>` elements
- Use proper heading hierarchy within accordion items
- Content is revealed/hidden via CSS or JavaScript state management
- ARIA attributes are critical for screen reader accessibility
- Supports keyboard navigation (Enter/Space to toggle, arrows to navigate)

### Implementation

```html
<div class="usa-accordion">
  <div class="usa-accordion-item">
    <h2 class="usa-accordion__heading">
      <button
        class="usa-accordion__button"
        aria-expanded="false"
        aria-controls="accordion-content-1"
        type="button">
        Section Title
      </button>
    </h2>
    <div id="accordion-content-1" class="usa-accordion__content">
      <p>Content for this accordion section goes here.</p>
    </div>
  </div>

  <div class="usa-accordion-item">
    <h2 class="usa-accordion__heading">
      <button
        class="usa-accordion__button"
        aria-expanded="false"
        aria-controls="accordion-content-2"
        type="button">
        Another Section
      </button>
    </h2>
    <div id="accordion-content-2" class="usa-accordion__content">
      <p>Content for the second accordion section.</p>
    </div>
  </div>
</div>
```

**Pre-expanded Variant:**
```html
<div class="usa-accordion">
  <div class="usa-accordion-item">
    <h2 class="usa-accordion__heading">
      <button
        class="usa-accordion__button"
        aria-expanded="true"
        aria-controls="accordion-content-1"
        type="button">
        Initially Open Section
      </button>
    </h2>
    <div id="accordion-content-1" class="usa-accordion__content">
      <p>This section starts expanded.</p>
    </div>
  </div>
</div>
```

### Context

The Accordion component is part of the MDWDS component library, built on USWDS (U.S. Web Design System) standards. It follows accessible design patterns and integrates with other content organization components like tabs and collapsible sections to provide flexible layouts for Maryland state web pages.

---

## Action Items

*Components*

Action Items are interactive components used to display and manage a list of actionable tasks or items requiring user attention. They help organize and prioritize work, allowing users to mark items as complete or take specific actions on each item. Use them in dashboards, to-do lists, task management interfaces, or anywhere users need to track and manage multiple action items.

### Key Information

Action Items typically include the following features and variants:

**Structure:**
- Container for displaying a list of related action items
- Each item represents a discrete task or action
- Items can be marked as complete/incomplete

**Variants & States:**
- Default/incomplete state
- Completed/done state
- Priority levels (if supported)
- Hover and focus states for interactivity

**Required Elements:**
- Clear item text/title
- Action mechanism (checkbox, button, or status indicator)
- Optional: timestamps, assignees, or priority indicators

**CSS Classes & Attributes:**
- Standard semantic HTML structure with appropriate ARIA roles
- `aria-label` for describing action items
- `aria-checked` for toggleable items
- Consider `aria-live` regions if items update dynamically

**Important Facts:**
- Supports accessibility through proper ARIA labeling
- Items should have clear visual feedback for state changes
- Consider supporting keyboard navigation (Tab, Enter, Space)
- Each item should be independently actionable

### Implementation

```html
<!-- Basic Action Items List -->
<div class="action-items" role="list">
  <div class="action-item" role="listitem">
    <input 
      type="checkbox" 
      id="action-1" 
      class="action-item__checkbox"
      aria-label="Mark item as complete"
    />
    <label for="action-1" class="action-item__label">
      Review and approve design mockups
    </label>
  </div>

  <div class="action-item action-item--completed" role="listitem">
    <input 
      type="checkbox" 
      id="action-2" 
      class="action-item__checkbox"
      checked
      aria-label="Mark item as complete"
    />
    <label for="action-2" class="action-item__label">
      Submit requirements document
    </label>
  </div>

  <div class="action-item" role="listitem">
    <input 
      type="checkbox" 
      id="action-3" 
      class="action-item__checkbox"
      aria-label="Mark item as complete"
    />
    <label for="action-3" class="action-item__label">
      Schedule stakeholder meeting
    </label>
  </div>
</div>
```

**With Priority & Timestamps:**

```html
<div class="action-items" role="list">
  <div class="action-item action-item--priority-high" role="listitem">
    <input 
      type="checkbox" 
      id="action-urgent" 
      class="action-item__checkbox"
      aria-label="Mark urgent item as complete"
    />
    <label for="action-urgent" class="action-item__label">
      Fix critical bug in production
    </label>
    <span class="action-item__priority" aria-label="Priority level">High</span>
    <span class="action-item__timestamp">Today</span>
  </div>
</div>
```

**Keyboard & Screen Reader Support:**
- Tab to focus items
- Space/Enter to toggle checkboxes
- Proper label associations for screen readers
- Use `aria-label` or `aria-labelledby` for clarity

### Context

Action Items are a fundamental component in the MDWDS for task management and workflow interfaces. They compose with other components like buttons, badges, and date/time utilities to create complete task management experiences, and follow the system's accessibility guidelines for interactive elements.

---

## Alert

*Components*

Alerts are messaging components that communicate important information to users, such as success, warning, error, or informational states. They grab user attention and provide contextual feedback about actions or system states. Use alerts to notify users about status changes, validation errors, or other important messages that require acknowledgment.

### Key Information


## Variants
- Success: Indicates a successful action or positive outcome
- Warning: Indicates a cautionary message requiring user attention
- Error: Indicates an error or problem that needs to be addressed
- Information: Provides general informational messages

## CSS Classes
- `.alert` - Base alert container class
- `.alert-success` - Success variant
- `.alert-warning` - Warning variant
- `.alert-danger` - Error/danger variant
- `.alert-info` - Information variant
- `.alert-dismissible` - Makes alert closeable with a dismiss button

## Key Attributes
- Role: `role="alert"` for accessibility to announce to screen readers
- `aria-live="polite"` - For dynamic alerts that update without page reload
- `aria-live="assertive"` - For urgent alerts requiring immediate attention

## Important Facts
- Alerts should include clear, concise messaging
- Icons or colors help distinguish alert types
- Dismissible alerts allow users to close them after reading
- Multiple alerts can be stacked
- Consider using appropriate heading levels within alerts for complex content


### Implementation


```html
<!-- Basic Success Alert -->
<div class="alert alert-success" role="alert">
  <strong>Success!</strong> Your action completed successfully.
</div>

<!-- Warning Alert -->
<div class="alert alert-warning" role="alert">
  <strong>Warning:</strong> Please review before proceeding.
</div>

<!-- Error/Danger Alert -->
<div class="alert alert-danger" role="alert">
  <strong>Error:</strong> Something went wrong. Please try again.
</div>

<!-- Informational Alert -->
<div class="alert alert-info" role="alert">
  <strong>Information:</strong> Here's something you should know.
</div>

<!-- Dismissible Alert -->
<div class="alert alert-success alert-dismissible" role="alert">
  <strong>Success!</strong> Your changes have been saved.
  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div>

<!-- Alert with Live Region (for dynamic updates) -->
<div class="alert alert-info" role="alert" aria-live="polite">
  <strong>Status Update:</strong> Processing your request...
</div>
```


### Context

Alerts are fundamental feedback components in MDWDS that work alongside form validation, modals, and other user feedback mechanisms. They provide crucial accessibility features through ARIA roles and live regions, ensuring all users, including those using assistive technologies, are informed of important system states and messages.

---

## Alerts

*Components*

Alerts are prominent messages that communicate important information to users, such as warnings, errors, successes, or informational notices. They help users understand the status of system operations and guide them toward appropriate actions. Use alerts to provide timely feedback and draw attention to critical information.

### Key Information


**Variants:**
- Alert (Default/Informational)
- Success Alert
- Warning Alert
- Error/Danger Alert

**CSS Classes:**
- `.usa-alert` - Base alert container
- `.usa-alert--success` - Success variant
- `.usa-alert--warning` - Warning variant
- `.usa-alert--error` - Error variant
- `.usa-alert-body` - Contains the alert content
- `.usa-alert-heading` - Optional alert heading
- `.usa-alert-text` - Alert message text

**Key Attributes:**
- `role="alert"` or `role="status"` - Semantic role for assistive technologies
- `aria-live="polite"` or `aria-live="assertive"` - For dynamic alerts

**Modifiers:**
- Color variants change the visual appearance and semantic meaning
- Alerts can include headings, text, and optional close buttons
- Can contain links and other inline content

**Important Facts:**
- Alerts should be dismissible when appropriate
- Use semantic color coding (green for success, red for error, etc.)
- Include appropriate ARIA attributes for accessibility
- Keep alert messages concise and actionable


### Implementation


```html
<!-- Informational Alert (Default) -->
<div class="usa-alert" role="alert">
  <div class="usa-alert-body">
    <h4 class="usa-alert-heading">Informational Alert</h4>
    <p class="usa-alert-text">This is an informational alert message.</p>
  </div>
</div>

<!-- Success Alert -->
<div class="usa-alert usa-alert--success" role="status">
  <div class="usa-alert-body">
    <h4 class="usa-alert-heading">Success</h4>
    <p class="usa-alert-text">Your action was completed successfully.</p>
  </div>
</div>

<!-- Warning Alert -->
<div class="usa-alert usa-alert--warning" role="alert">
  <div class="usa-alert-body">
    <h4 class="usa-alert-heading">Warning</h4>
    <p class="usa-alert-text">Please review this important warning message.</p>
  </div>
</div>

<!-- Error Alert -->
<div class="usa-alert usa-alert--error" role="alert">
  <div class="usa-alert-body">
    <h4 class="usa-alert-heading">Error</h4>
    <p class="usa-alert-text">An error has occurred. Please try again.</p>
  </div>
</div>

<!-- Alert with Close Button -->
<div class="usa-alert" role="alert">
  <div class="usa-alert-body">
    <h4 class="usa-alert-heading">Dismissible Alert</h4>
    <p class="usa-alert-text">This alert can be closed by the user.</p>
    <button class="usa-button usa-button--unstyled" aria-label="Close alert" onclick="this.closest('.usa-alert').remove()">✕</button>
  </div>
</div>
```


### Context

Alerts are a core USWDS component adopted by MDWDS for providing user feedback and important system messages. They compose well with forms and pages to communicate validation results, system status, and actionable information to users.

---

## Automatic List

*Components*

The Automatic List is a component that dynamically generates a list of items from data, automatically handling formatting and presentation. It reduces manual HTML markup while maintaining consistent styling across Maryland web pages. Use this when you need to display collections of items that require consistent formatting and responsive behavior.

### Key Information

- **Purpose**: Automatically renders lists from data structures without manual item markup
- **Variants**: Supports unordered lists, ordered lists, and nested list structures
- **Styling**: Automatically applies MDWDS list styles and spacing classes
- **Responsive**: Adapts to different screen sizes automatically
- **Accessibility**: Includes proper semantic HTML and ARIA attributes for screen readers
- **Integration**: Works with other MDWDS components and can be nested within other elements
- **Class names**: Apply standard list classes for styling (ul, ol, li elements)
- **Data-driven**: Can be populated from arrays, JSON, or other data sources

### Implementation

```html
<!-- Unordered List -->
<ul>
  <li>List item one</li>
  <li>List item two</li>
  <li>List item three</li>
</ul>

<!-- Ordered List -->
<ol>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ol>

<!-- Nested List -->
<ul>
  <li>Parent item
    <ul>
      <li>Child item one</li>
      <li>Child item two</li>
    </ul>
  </li>
  <li>Another parent item</li>
</ul>
```

### Context

The Automatic List component is a foundational content element within MDWDS that provides consistent list presentation across the design system. It composes with text components and can be nested within cards, sections, and other layout components to organize content hierarchically.

---

## Banner

*Components*

The Banner component is a USWDS-based component that provides a consistent header area for Maryland state web pages. It serves as a prominent, reusable element that establishes visual identity and provides key navigation and branding for users at the top of the page.

### Key Information

The Banner component follows USWDS (U.S. Web Design System) patterns and standards. Key variants and features include:

- **Base Structure**: Uses semantic HTML with proper heading hierarchy
- **Class Names**: Includes USWDS utility classes for layout and styling
- **Responsive Design**: Adapts to different screen sizes
- **Accessibility**: Includes ARIA attributes for screen readers and semantic HTML elements
- **Content Areas**: Typically contains site title, navigation links, and branding
- **Variants**: May include different layouts for different page contexts (full-width, standard)
- **Modifiers**: Can be styled with alternate background colors or configurations
- **Required Attributes**: Proper heading levels (h1 for site title), role attributes where needed
- **Navigation Integration**: Works with primary navigation components for consistent UX

### Implementation

```html
<header class="usa-banner" role="banner">
  <div class="usa-banner__content">
    <div class="grid-container">
      <div class="usa-banner__header">
        <div class="usa-banner__inner">
          <div class="grid-col-auto">
            <p class="usa-banner__header-text">
              An official website of the United States government
            </p>
          </div>
          <button class="usa-banner__button" aria-expanded="false" aria-controls="gov-banner-id">
            Here's how you know
          </button>
        </div>
      </div>
      <div class="usa-banner__guidance-id" id="gov-banner-id" hidden="">
        <div class="usa-banner__guidance">
          <div class="grid-row gap-1">
            <div class="grid-col-12 tablet:grid-col-6">
              <h3 class="usa-banner__heading">Official websites use .gov</h3>
              <p>A <strong>.gov</strong> website belongs to an official government organization in the United States.</p>
            </div>
            <div class="grid-col-12 tablet:grid-col-6">
              <h3 class="usa-banner__heading">Secure .gov websites use HTTPS</h3>
              <p>A lock icon or https:// means you've safely connected to the .gov website. Share sensitive information only on official, secure websites.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</header>
```

For Maryland-specific implementation, the banner may include state-specific branding:

```html
<header class="usa-banner md-banner" role="banner">
  <div class="md-banner__content">
    <div class="grid-container">
      <div class="md-banner__inner">
        <h1 class="md-banner__title">Maryland State Website</h1>
        <p class="md-banner__description">Maryland Web Design System</p>
      </div>
    </div>
  </div>
</header>
```

### Context

The Banner component is a foundational USWDS component adapted for the MDWDS and appears at the top of all Maryland state web pages. It works in conjunction with Navigation, Skip Links, and site header components to create a cohesive page header experience that meets federal web standards and accessibility requirements.

---

## Breadcrumb

*Components*

A breadcrumb navigation component displays the user's current location within a website hierarchy as a sequence of links. It helps users understand where they are and allows them to navigate back up the site structure. Breadcrumbs should be used on pages that are nested within a hierarchical information architecture.

### Key Information

The breadcrumb component typically includes:

- **Structure**: An ordered list (`<ol>` or `<ul>`) of navigation links representing the page hierarchy
- **Current page**: The last item in the breadcrumb represents the current page and may be non-clickable text or a link
- **Separators**: Visual separators (typically "/" or ">") between items, usually added via CSS
- **CSS classes**: Uses semantic HTML5 `<nav>` element with appropriate classes for styling
- **ARIA attributes**: Must include `aria-label="Breadcrumb"` on the nav element to identify it to assistive technology
- **Link structure**: Each item except the current page should be clickable and link to the appropriate parent level
- **Responsive**: On mobile devices, breadcrumbs may be hidden or condensed to save space
- **Schema markup**: Can include JSON-LD schema.org BreadcrumbList for SEO

The breadcrumb should clearly reflect the current page position and provide an efficient way to navigate the site hierarchy.

### Implementation

```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item">
      <a href="/">Home</a>
    </li>
    <li class="breadcrumb-item">
      <a href="/services">Services</a>
    </li>
    <li class="breadcrumb-item">
      <a href="/services/permits">Permits</a>
    </li>
    <li class="breadcrumb-item active">
      <span aria-current="page">Permit Application</span>
    </li>
  </ol>
</nav>
```

**Variant with non-linked current page:**
```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item">
      <a href="/">Home</a>
    </li>
    <li class="breadcrumb-item active">
      Current Page
    </li>
  </ol>
</nav>
```

**Minimal breadcrumb:**
```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="/">Home</a></li>
    <li class="breadcrumb-item active">Current</li>
  </ol>
</nav>
```

### Context

The Breadcrumb component is a foundational navigation pattern within MDWDS used to enhance wayfinding on multi-level state websites. It works alongside the main navigation and provides a secondary navigation path, particularly important for deeply nested content hierarchies common in government websites.

---

## Breadcrumbs

*Components*

Breadcrumbs are a navigation component that displays the user's current location within a website hierarchy. They provide a visual trail of links showing the path from the homepage to the current page, helping users understand their location and navigate back to parent pages. Use breadcrumbs on interior pages to improve wayfinding and reduce navigation friction.

### Key Information

## Variants
- Standard breadcrumb list with multiple navigation levels
- Supports wrapping on smaller screens
- Last item is typically the current page (non-clickable)
- All parent items are clickable links

## CSS Classes
- `usa-breadcrumb`: Main wrapper container
- `usa-breadcrumb__list`: Ordered list containing breadcrumb items
- `usa-breadcrumb__list-item`: Individual breadcrumb item
- `usa-breadcrumb__link`: Anchor tag for navigation

## Key Attributes
- Uses semantic `<nav>` element with proper labeling
- Implements `<ol>` (ordered list) for proper semantics
- Last item should not be wrapped in a link (current page indicator)
- Should include `aria-label` on nav for accessibility

## Important Facts
- Breadcrumbs are a secondary navigation aid, not a replacement for primary navigation
- Improves SEO through semantic HTML structure
- Should reflect site hierarchy, not browser history
- Mobile responsive with appropriate text truncation
- Mobile breakpoint typically shows abbreviated version

### Implementation

```html
<nav aria-label="Breadcrumbs" class="usa-breadcrumb">
  <ol class="usa-breadcrumb__list">
    <li class="usa-breadcrumb__list-item">
      <a href="/" class="usa-breadcrumb__link">Home</a>
    </li>
    <li class="usa-breadcrumb__list-item">
      <a href="/parent-page/" class="usa-breadcrumb__link">Parent Page</a>
    </li>
    <li class="usa-breadcrumb__list-item usa-breadcrumb__list-item--current">
      <span class="usa-breadcrumb__link">Current Page</span>
    </li>
  </ol>
</nav>
```

## Multi-level Example
```html
<nav aria-label="Breadcrumbs" class="usa-breadcrumb">
  <ol class="usa-breadcrumb__list">
    <li class="usa-breadcrumb__list-item">
      <a href="/" class="usa-breadcrumb__link">Home</a>
    </li>
    <li class="usa-breadcrumb__list-item">
      <a href="/services/" class="usa-breadcrumb__link">Services</a>
    </li>
    <li class="usa-breadcrumb__list-item">
      <a href="/services/permits/" class="usa-breadcrumb__link">Permits</a>
    </li>
    <li class="usa-breadcrumb__list-item usa-breadcrumb__list-item--current">
      <span class="usa-breadcrumb__link">Apply for Permit</span>
    </li>
  </ol>
</nav>
```

## Notes
- No JavaScript required for basic functionality
- Separators (typically `/`) are added via CSS pseudo-elements
- Current page item uses `<span>` instead of `<a>` to prevent linking to itself
- Mobile version may abbreviate or collapse breadcrumb trail

### Context

Breadcrumbs are a USWDS component integrated into MDWDS that enhances site navigation and supports Maryland state website hierarchy. They work alongside the main navigation menu to provide redundant navigation paths and improve user experience on multi-level state service pages.

---

## Button Group

*Components*

A Button Group is a container component that organizes related buttons together for improved visual and functional cohesion. It helps users understand that multiple button actions are related or part of the same operation. Use Button Groups when you need to present related actions that belong together contextually, such as pagination controls, filter options, or grouped form actions.

### Key Information

The Button Group component organizes buttons into a cohesive unit with consistent spacing and alignment.

**Variants:**
- Horizontal button group (default)
- Vertical button group
- Segmented control variant
- Icon-only button groups

**CSS Classes:**
- `.button-group` - Main container class
- `.button-group--vertical` - Stacks buttons vertically
- `.button-group--segmented` - Segmented/toggle-style variant

**Key Attributes:**
- Buttons within the group should maintain consistent sizing
- Use semantic HTML button elements or links styled as buttons
- Support both single and multiple selection depending on variant
- May include ARIA attributes for toggle groups or segmented controls

**Important Facts:**
- Buttons within a group are typically related contextually
- Spacing is automatically handled by the container
- Groups can be combined with other components like dropdowns
- Responsive behavior may stack buttons on smaller screens
- Works well with icon buttons and text buttons

### Implementation

```html
<!-- Horizontal Button Group -->
<div class="button-group" role="group" aria-label="Actions">
  <button class="btn btn-primary">Action 1</button>
  <button class="btn btn-secondary">Action 2</button>
  <button class="btn btn-secondary">Action 3</button>
</div>
```

```html
<!-- Vertical Button Group -->
<div class="button-group button-group--vertical" role="group" aria-label="Vertical Actions">
  <button class="btn btn-primary">Action 1</button>
  <button class="btn btn-secondary">Action 2</button>
  <button class="btn btn-secondary">Action 3</button>
</div>
```

```html
<!-- Segmented Control Variant -->
<div class="button-group button-group--segmented" role="group" aria-label="View Options">
  <button class="btn btn-secondary active" aria-pressed="true">List View</button>
  <button class="btn btn-secondary" aria-pressed="false">Grid View</button>
  <button class="btn btn-secondary" aria-pressed="false">Map View</button>
</div>
```

```html
<!-- Icon-Only Button Group -->
<div class="button-group" role="group" aria-label="Formatting">
  <button class="btn btn-icon" aria-label="Bold"><i class="icon-bold"></i></button>
  <button class="btn btn-icon" aria-label="Italic"><i class="icon-italic"></i></button>
  <button class="btn btn-icon" aria-label="Underline"><i class="icon-underline"></i></button>
</div>
```

### Context

Button Group is a foundational component in MDWDS that composes individual Button components into organized, related sets. It works alongside the Button component and pairs well with other UI patterns like toolbars, pagination, and form controls to create cohesive user experiences across Maryland state web applications.

---

## Button Group

*Components*

The Button Group component is a USWDS component that groups multiple related buttons together for logical organization and consistent spacing. It provides visual and semantic grouping of button actions that belong together, improving user experience and interface clarity.

### Key Information

## Key Information

### Purpose
- Groups related buttons together semantically and visually
- Maintains consistent spacing between grouped buttons
- Commonly used for action sets like primary/secondary button pairs or multiple related actions

### USWDS Integration
- Part of the USWDS component library integrated into MDWDS
- Follows U.S. Web Design System styling and accessibility standards
- Works with standard Button component variants

### Variants & Usage
- Can contain multiple button types (primary, secondary, etc.)
- Supports different button sizes when needed
- Responsive design adapts spacing on smaller screens
- Often used for form actions (Save/Cancel) or navigation options

### Common Patterns
- Action pairs: Primary action button + Secondary cancel/back button
- Multiple related actions grouped together
- Form submission and cancellation controls

### Implementation

```html
<!-- Basic Button Group -->
<div class="usa-button-group">
  <button class="usa-button">Primary Action</button>
  <button class="usa-button usa-button--secondary">Secondary Action</button>
</div>
```

```html
<!-- Button Group with Multiple Buttons -->
<div class="usa-button-group">
  <button class="usa-button">Save</button>
  <button class="usa-button usa-button--secondary">Cancel</button>
  <button class="usa-button usa-button--secondary">Delete</button>
</div>
```

```html
<!-- Responsive Button Group -->
<div class="usa-button-group">
  <button class="usa-button">Submit</button>
  <button class="usa-button usa-button--secondary">Reset</button>
</div>
```

### Context

Button Group is a layout utility component from USWDS that works alongside the Button component to organize multiple button actions. It's commonly used in forms, modals, and action areas to group related actions with proper spacing and visual hierarchy.

---

## Buttons

*Components*

Buttons are interactive elements that trigger actions or navigate to new pages. They are fundamental components used throughout Maryland state web pages to enable user interactions, form submissions, and navigation. Use buttons to encourage primary actions, secondary navigation, or specific user tasks.

### Key Information

## Variants and Styles

- **Primary Button**: Standard action button for main call-to-action
- **Secondary Button**: Alternative action button with less visual emphasis
- **Disabled Button**: Non-interactive state when action is unavailable
- **Hover/Focus States**: Visual feedback for user interaction

## CSS Classes

- `.usa-button` - Base button class
- `.usa-button--secondary` - Secondary style variant
- `.usa-button--accent` - Accent color variant
- `.usa-button--outline` - Outline style variant
- `.usa-button--unstyled` - Removes default button styling

## Required Attributes

- `type` attribute: "button", "submit", or "reset"
- `aria-label` - For icon-only buttons or additional context
- `disabled` attribute for disabled state

## Important Facts

- Buttons must have sufficient color contrast per WCAG guidelines
- All buttons require proper focus indicators for keyboard navigation
- Buttons should not be used for navigation; use links (`<a>` tags) instead
- Icon buttons must include text or aria-label for accessibility
- Button sizing follows a consistent scale for visual hierarchy

### Implementation

```html
<!-- Primary Button -->
<button class="usa-button" type="button">
  Click me
</button>

<!-- Secondary Button -->
<button class="usa-button usa-button--secondary" type="button">
  Secondary action
</button>

<!-- Accent Button -->
<button class="usa-button usa-button--accent" type="button">
  Accent action
</button>

<!-- Outline Button -->
<button class="usa-button usa-button--outline" type="button">
  Outline button
</button>

<!-- Disabled Button -->
<button class="usa-button" type="button" disabled>
  Disabled button
</button>

<!-- Button with Icon (Icon + Text) -->
<button class="usa-button" type="button">
  <svg class="usa-icon" aria-hidden="true" role="img">
    <use xlink:href="/assets/img/sprite.svg#search"></use>
  </svg>
  Search
</button>

<!-- Icon-Only Button -->
<button class="usa-button" type="button" aria-label="Search">
  <svg class="usa-icon" aria-hidden="true" role="img">
    <use xlink:href="/assets/img/sprite.svg#search"></use>
  </svg>
</button>

<!-- Form Submit Button -->
<form>
  <input type="text" name="search">
  <button class="usa-button" type="submit">
    Submit
  </button>
</form>

<!-- Unstyled Button -->
<button class="usa-button usa-button--unstyled" type="button">
  Unstyled button
</button>
```

### Context

Buttons are core interactive components in the Maryland Web Design System, built on USWDS standards. They compose with forms, modals, and other components to provide consistent, accessible call-to-action elements across all Maryland state web applications.

---

## Callout

*Components*

A callout is a prominent content container used to highlight important information, warnings, or special notices that require user attention. It draws focus to critical messages or related content that stands apart from the main page flow. Use callouts to emphasize alerts, tips, important information, or contextual notes.

### Key Information

## Variants and Types

The Callout component supports multiple variants to communicate different message types:
- **Default/Info**: Standard informational callout
- **Warning**: For cautionary or alert-level messages
- **Success**: For positive confirmations or completed actions
- **Error**: For error messages or critical issues

## CSS Classes

- `.callout`: Base class for the container
- `.callout--info`: Info variant (default)
- `.callout--warning`: Warning variant
- `.callout--success`: Success variant
- `.callout--error`: Error variant

## Key Attributes and Structure

- Semantic HTML structure with proper heading hierarchy
- Support for optional icons to visually reinforce message type
- Flexible content area for text, links, and other inline elements
- Optional close button for dismissible callouts
- Proper contrast and color coding for accessibility

## Important Facts

- Each variant uses distinct color schemes for quick visual recognition
- Callouts should include appropriate ARIA roles for screen readers
- Content should be concise and focused on the key message
- Can be used standalone or in combination with other components

### Implementation

```html
<!-- Info Callout -->
<div class="callout callout--info" role="region" aria-label="Information">
  <h3>Informational Message</h3>
  <p>This is an informational callout used to highlight important details or tips.</p>
</div>

<!-- Warning Callout -->
<div class="callout callout--warning" role="region" aria-label="Warning">
  <h3>Warning Message</h3>
  <p>This is a warning callout that alerts users to important cautions or considerations.</p>
</div>

<!-- Success Callout -->
<div class="callout callout--success" role="region" aria-label="Success">
  <h3>Success Message</h3>
  <p>This is a success callout confirming a completed action or positive outcome.</p>
</div>

<!-- Error Callout -->
<div class="callout callout--error" role="region" aria-label="Error">
  <h3>Error Message</h3>
  <p>This is an error callout used for critical issues or error states.</p>
</div>

<!-- Dismissible Callout with Close Button -->
<div class="callout callout--info" role="region" aria-label="Information">
  <button class="callout__close" aria-label="Close this message" onclick="this.parentElement.style.display='none';">
    <span aria-hidden="true">&times;</span>
  </button>
  <h3>Dismissible Message</h3>
  <p>This callout can be dismissed by clicking the close button.</p>
</div>
```

### Context

The Callout component is a foundational component in MDWDS for communicating important messages and drawing user attention to critical information. It works alongside other messaging components and typography elements to create a cohesive information hierarchy across Maryland state web pages.

---

## Cards

*Components*

Cards are container components that organize and present related information in a visually distinct, self-contained format. They help structure content into scannable, modular units that improve readability and user engagement. Use cards when displaying collections of related items such as services, features, articles, or calls-to-action.

### Key Information

Cards are flexible layout components that can contain various content types including text, images, links, and buttons. Common variants include:
- **Basic Card**: Simple container with padding and optional borders
- **Card with Image**: Includes an image header or background
- **Card with Actions**: Contains buttons or interactive elements
- **Clickable Card**: Entire card functions as a link

Key CSS classes and modifiers:
- `.card`: Base card container class
- `.card-body`: Content wrapper inside the card
- `.card-header`: Optional header section (can contain image or text)
- `.card-footer`: Optional footer section for actions
- `.card-link`: Modifier for clickable card variants
- `.card-shadow`: Optional shadow effect for depth

Cards support flexible content organization and can be arranged in grid layouts. They maintain consistent padding, spacing, and visual hierarchy across the design system. Supports responsive behavior adapting to different screen sizes.

### Implementation

```html
<!-- Basic Card -->
<div class="card">
  <div class="card-body">
    <h3 class="card-title">Card Title</h3>
    <p class="card-text">Card content goes here. This is a basic card component.</p>
  </div>
</div>

<!-- Card with Image -->
<div class="card">
  <img class="card-img-top" src="image.jpg" alt="Card image">
  <div class="card-body">
    <h3 class="card-title">Card with Image</h3>
    <p class="card-text">Description text for the card.</p>
  </div>
</div>

<!-- Card with Header and Footer -->
<div class="card">
  <div class="card-header">
    <h3>Card Header</h3>
  </div>
  <div class="card-body">
    <p class="card-text">Main content area.</p>
  </div>
  <div class="card-footer">
    <button class="btn btn-primary">Action Button</button>
  </div>
</div>

<!-- Clickable Card -->
<a href="#" class="card card-link">
  <div class="card-body">
    <h3 class="card-title">Clickable Card</h3>
    <p class="card-text">Entire card is clickable and navigates on click.</p>
  </div>
</a>
```

### Context

Cards are a foundational component in the MDWDS that composes with other elements like buttons, images, and typography to create organized content layouts. They are commonly used in grid-based templates and work alongside spacing and layout utilities to structure complex information hierarchies across Maryland state web pages.

---

## Cards

*Components*

Cards are flexible container components used to display related content and actions in a contained format. They organize information into scannable, digestible chunks and support various content types including text, images, and actions. Cards are commonly used for displaying grouped information, product listings, team members, or any modular content that benefits from visual separation and organization.

### Key Information


### Variants
- **Basic Card**: Standard card with padding and border
- **Card with Image**: Card featuring a featured image at the top
- **Card with Actions**: Card with action buttons or links at the bottom
- **Themed Cards**: Cards with different background colors or accent colors

### CSS Classes
- `.usa-card` - Base card container class
- `.usa-card__container` - Inner wrapper for card content
- `.usa-card__header` - Card header section
- `.usa-card__body` - Card body/content section
- `.usa-card__footer` - Card footer section for actions
- `.usa-card__image` - Image container class
- `.usa-card__media-block` - For side-by-side image and content layouts

### Modifiers & Options
- Padding options: Standard, compact
- Border styles: Standard border, no border
- Shadow effects: No shadow, subtle shadow, elevated shadow
- Background colors: White, gray, themed colors
- Header variations: Text-only, with image, with tags

### Required Attributes
- Semantic HTML structure (proper heading hierarchy)
- Image alt attributes when using `.usa-card__image`

### Important Facts
- Cards are responsive and stack on mobile
- Support flexible content layouts
- Can contain headings, paragraphs, lists, images, and buttons
- Work well in grid layouts for multiple cards
- Inherit typography and spacing from USWDS/MDWDS system


### Implementation


```html
<!-- Basic Card -->
<div class="usa-card">
  <div class="usa-card__container">
    <header class="usa-card__header">
      <h2 class="usa-card__heading">Card Title</h2>
    </header>
    <div class="usa-card__body">
      <p>Card content goes here. This is the main body of the card.</p>
    </div>
  </div>
</div>

<!-- Card with Image -->
<div class="usa-card">
  <img class="usa-card__image" src="image.jpg" alt="Card image description">
  <div class="usa-card__container">
    <header class="usa-card__header">
      <h2 class="usa-card__heading">Card with Image</h2>
    </header>
    <div class="usa-card__body">
      <p>Card content with featured image.</p>
    </div>
  </div>
</div>

<!-- Card with Actions -->
<div class="usa-card">
  <div class="usa-card__container">
    <header class="usa-card__header">
      <h2 class="usa-card__heading">Card with Actions</h2>
    </header>
    <div class="usa-card__body">
      <p>Card content with action buttons.</p>
    </div>
    <footer class="usa-card__footer">
      <a href="#" class="usa-button">Learn More</a>
      <a href="#" class="usa-button usa-button--outline">View Details</a>
    </footer>
  </div>
</div>

<!-- Cards in Grid -->
<div class="grid-container">
  <div class="grid-row grid-gap">
    <div class="tablet:grid-col-6 desktop:grid-col-4">
      <div class="usa-card">
        <div class="usa-card__container">
          <header class="usa-card__header">
            <h2 class="usa-card__heading">Card 1</h2>
          </header>
          <div class="usa-card__body">
            <p>Content for card 1</p>
          </div>
        </div>
      </div>
    </div>
    <div class="tablet:grid-col-6 desktop:grid-col-4">
      <div class="usa-card">
        <div class="usa-card__container">
          <header class="usa-card__header">
            <h2 class="usa-card__heading">Card 2</h2>
          </header>
          <div class="usa-card__body">
            <p>Content for card 2</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```


### Context

Cards are a fundamental component in the MDWDS system for organizing and presenting grouped content across Maryland state web pages. They compose well with the grid system for responsive layouts and can combine with other components like buttons, badges, and images to create rich content containers.

---

## Character Count

*Components*

Character Count is a component that displays and monitors the number of characters entered in a text input or textarea field in real-time. It helps users stay within character limits by providing immediate feedback on their input length. Use this component when you need to enforce or inform users about character restrictions on form fields.

### Key Information

## Variants and Options

- **Character counter display**: Shows current character count with optional maximum limit (e.g., "5 characters")
- **Character limit warning**: Can display remaining characters and warn when approaching or exceeding limit (e.g., "5 characters remaining")
- **Hint text vs. character count message**: Choose between displaying as helper text or as a dedicated character count message below the input

## CSS Classes and Structure

- `.usa-character-count`: Main wrapper class for the character count component
- `.usa-character-count__message`: Class for the character count display message
- `.usa-character-count__input`: Applied to the input or textarea being monitored
- `maxlength` attribute: HTML attribute that sets the maximum character limit

## Required Attributes and Properties

- `maxlength`: Required attribute on input/textarea to set character limit
- `aria-live="polite"` or `aria-live="assertive"`: Used on the message element for screen reader announcements
- `aria-describedby`: Links the input to the character count message for accessibility
- Character count updates dynamically via JavaScript event listeners (input or change events)

## Important Facts

- Works with both `<input type="text">` and `<textarea>` elements
- Updates character count in real-time as user types
- Must be initialized with JavaScript to enable dynamic character counting
- Supports both "characters used" and "characters remaining" display modes
- Screen reader announcements update as character count changes

### Implementation

```html
<div class="usa-form-group">
  <label class="usa-label" for="textarea-character-count">
    Textarea with character count
  </label>
  <span class="usa-hint" id="textarea-hint">
    This is helper text with a character limit
  </span>
  <textarea
    class="usa-textarea usa-character-count__input"
    id="textarea-character-count"
    name="textarea-character-count"
    aria-describedby="textarea-hint textarea-character-count-message"
    maxlength="100"
  ></textarea>
  <div
    class="usa-character-count__message"
    id="textarea-character-count-message"
    aria-live="polite"
    aria-atomic="true"
  >
    <span class="usa-sr-only">Textarea character count: </span>
    0 / 100 characters
  </div>
</div>
```

```html
<div class="usa-form-group">
  <label class="usa-label" for="input-character-count">
    Input with character count
  </label>
  <input
    class="usa-input usa-character-count__input"
    id="input-character-count"
    type="text"
    name="input-character-count"
    aria-describedby="input-character-count-message"
    maxlength="50"
  />
  <div
    class="usa-character-count__message"
    id="input-character-count-message"
    aria-live="polite"
    aria-atomic="true"
  >
    <span class="usa-sr-only">Input character count: </span>
    0 / 50 characters
  </div>
</div>
```

```javascript
// JavaScript initialization for character count
document.querySelectorAll('.usa-character-count__input').forEach(input => {
  const maxlength = input.getAttribute('maxlength');
  const messageId = input.getAttribute('aria-describedby').split(' ').pop();
  const message = document.getElementById(messageId);
  
  const updateCount = () => {
    const currentCount = input.value.length;
    message.textContent = currentCount + ' / ' + maxlength + ' characters';
  };
  
  input.addEventListener('input', updateCount);
  updateCount(); // Initialize on load
});
```

### Context

Character Count is a USWDS component integrated into MDWDS that pairs with form inputs and textareas to provide real-time character limit feedback. It enhances form accessibility and user experience by keeping users informed about input constraints, and is typically used alongside standard form components like text inputs and textareas.

---

## Checkboxes

*Components*

Checkboxes are input controls that allow users to select zero, one, or multiple options from a set. They provide a clear, accessible way for users to make binary choices or select multiple items from a list. Use checkboxes when users need to select any combination of options from a group.

### Key Information

## Variants
- **Single checkbox**: A standalone checkbox for a single binary choice
- **Checkbox group**: Multiple checkboxes grouped together for selecting multiple options
- **Disabled state**: Disabled checkboxes prevent user interaction
- **Checked state**: Indicates a selected checkbox
- **Indeterminate state**: Used in parent-child checkbox hierarchies (partially selected)

## CSS Classes
- `.usa-checkbox`: Container class for checkbox wrapper
- `.usa-checkbox__input`: Applied to the `<input type="checkbox">` element
- `.usa-checkbox__label`: Applied to the label element

## ARIA Attributes
- `aria-label` or associated `<label>`: Required for accessibility
- `aria-disabled="true"`: Indicate disabled state when needed
- `aria-checked="mixed"`: For indeterminate state in parent-child relationships
- `aria-describedby`: Optional, for additional helper text

## Required Attributes
- `type="checkbox"`: Define input type
- `id`: Unique identifier for the checkbox
- Associated `<label>` with `for` attribute matching the checkbox `id`

## Important Facts
- Always provide labels or ARIA labels for accessibility compliance
- Use consistent spacing and sizing with MDWDS patterns
- Checkboxes can be arranged horizontally or vertically
- Parent checkboxes controlling child checkboxes require indeterminate state handling with JavaScript

### Implementation

```html
<!-- Single Checkbox -->
<div class="usa-checkbox">
  <input
    class="usa-checkbox__input"
    id="checkbox-single"
    type="checkbox"
    name="option"
  />
  <label class="usa-checkbox__label" for="checkbox-single">
    Checkbox option
  </label>
</div>

<!-- Checkbox Group -->
<fieldset class="usa-fieldset">
  <legend class="usa-legend">Select options</legend>
  <div class="usa-checkbox">
    <input
      class="usa-checkbox__input"
      id="checkbox-1"
      type="checkbox"
      name="options"
      value="option1"
    />
    <label class="usa-checkbox__label" for="checkbox-1">
      Option 1
    </label>
  </div>
  <div class="usa-checkbox">
    <input
      class="usa-checkbox__input"
      id="checkbox-2"
      type="checkbox"
      name="options"
      value="option2"
    />
    <label class="usa-checkbox__label" for="checkbox-2">
      Option 2
    </label>
  </div>
  <div class="usa-checkbox">
    <input
      class="usa-checkbox__input"
      id="checkbox-3"
      type="checkbox"
      name="options"
      value="option3"
    />
    <label class="usa-checkbox__label" for="checkbox-3">
      Option 3
    </label>
  </div>
</fieldset>

<!-- Disabled Checkbox -->
<div class="usa-checkbox">
  <input
    class="usa-checkbox__input"
    id="checkbox-disabled"
    type="checkbox"
    name="option"
    disabled
  />
  <label class="usa-checkbox__label" for="checkbox-disabled">
    Disabled checkbox
  </label>
</div>

<!-- Checked Checkbox -->
<div class="usa-checkbox">
  <input
    class="usa-checkbox__input"
    id="checkbox-checked"
    type="checkbox"
    name="option"
    checked
  />
  <label class="usa-checkbox__label" for="checkbox-checked">
    Checked checkbox
  </label>
</div>

<!-- Parent-Child with Indeterminate State -->
<div class="usa-checkbox">
  <input
    class="usa-checkbox__input"
    id="checkbox-parent"
    type="checkbox"
    name="parent"
    aria-controls="child-group"
  />
  <label class="usa-checkbox__label" for="checkbox-parent">
    Select all options
  </label>
</div>
<div id="child-group" style="margin-left: 2rem;">
  <div class="usa-checkbox">
    <input
      class="usa-checkbox__input"
      id="checkbox-child-1"
      type="checkbox"
      name="child"
      value="child1"
    />
    <label class="usa-checkbox__label" for="checkbox-child-1">
      Child option 1
    </label>
  </div>
  <div class="usa-checkbox">
    <input
      class="usa-checkbox__input"
      id="checkbox-child-2"
      type="checkbox"
      name="child"
      value="child2"
    />
    <label class="usa-checkbox__label" for="checkbox-child-2">
      Child option 2
    </label>
  </div>
</div>
```

### Context

Checkboxes are a core USWDS form component integrated into the Maryland Web Design System for collecting user input. They compose with fieldset and legend elements for grouped selections and follow WCAG accessibility standards for state government applications.

---

## Combo Box

*Components*

A combo box is an input field with an associated dropdown list that allows users to select from predefined options or enter custom text. It combines the functionality of a text input with autocomplete capabilities and a dropdown menu, making it useful for searchable selections with large option lists or when users need flexibility to enter values not in the list.

### Key Information

## Key Features
- Searchable dropdown list that filters as user types
- Supports both selection from list and custom text entry
- ARIA-compliant with proper roles and attributes for accessibility
- Keyboard navigation support (arrow keys, Enter, Escape)
- Optional clearable state with clear button

## CSS Classes
- `.usa-combo-box` - Main wrapper class
- `.usa-combo-box__input` - Input field element
- `.usa-combo-box__list` - Dropdown list container
- `.usa-combo-box__list-option` - Individual list items

## Required Attributes
- `data-module="usa-combo-box"` - Enables JavaScript initialization
- `role="combobox"` on input element
- `aria-owns` - Links input to listbox
- `aria-expanded` - Indicates if list is open/closed
- `aria-controls` - Associates input with list

## Options & Modifiers
- Clearable combo box with clear button
- Disabled state
- Custom placeholder text
- Optional helper text below input
- Async loading support for large datasets

## Important Notes
- Requires JavaScript initialization for full functionality
- Must include proper ARIA labels for screen readers
- Works with USWDS form components for consistent styling

### Implementation

```html
<div class="usa-combo-box" data-module="usa-combo-box">
  <label for="combo-box-input" class="usa-label">Select an option</label>
  <input
    id="combo-box-input"
    class="usa-combo-box__input usa-input"
    type="text"
    role="combobox"
    aria-owns="combo-box-list"
    aria-expanded="false"
    aria-controls="combo-box-list"
    aria-autocomplete="list"
    placeholder="Search..."
  />
  <ul
    id="combo-box-list"
    class="usa-combo-box__list"
    role="listbox"
    hidden
  >
    <li class="usa-combo-box__list-option" role="option">Option 1</li>
    <li class="usa-combo-box__list-option" role="option">Option 2</li>
    <li class="usa-combo-box__list-option" role="option">Option 3</li>
  </ul>
</div>

<script>
// USWDS combo box initialization
const comboBoxes = document.querySelectorAll('[data-module="usa-combo-box"]');
comboBoxes.forEach(el => {
  new window.USWDS.components.ComboBox(el);
});
</script>
```

### Clearable Variant
```html
<div class="usa-combo-box" data-module="usa-combo-box">
  <label for="clearable-combo" class="usa-label">Clearable combo box</label>
  <input
    id="clearable-combo"
    class="usa-combo-box__input usa-input"
    type="text"
    role="combobox"
    aria-owns="clearable-list"
    aria-expanded="false"
    aria-controls="clearable-list"
  />
  <button
    class="usa-combo-box__clear-button"
    aria-label="Clear selection"
    type="button"
  >
    ✕
  </button>
  <ul
    id="clearable-list"
    class="usa-combo-box__list"
    role="listbox"
    hidden
  >
    <li class="usa-combo-box__list-option" role="option">Option A</li>
    <li class="usa-combo-box__list-option" role="option">Option B</li>
  </ul>
</div>
```

### With Helper Text
```html
<div class="usa-combo-box" data-module="usa-combo-box">
  <label for="helper-combo" class="usa-label">Combo box with helper</label>
  <span class="usa-hint" id="helper-text">Select from the list below</span>
  <input
    id="helper-combo"
    class="usa-combo-box__input usa-input"
    type="text"
    aria-describedby="helper-text"
    role="combobox"
    aria-owns="helper-list"
    aria-expanded="false"
    aria-controls="helper-list"
  />
  <ul
    id="helper-list"
    class="usa-combo-box__list"
    role="listbox"
    hidden
  >
    <li class="usa-combo-box__list-option" role="option">Item 1</li>
    <li class="usa-combo-box__list-option" role="option">Item 2</li>
  </ul>
</div>
```

### Context

The Combo Box component is a USWDS-based form element that integrates into Maryland's design system for complex selection scenarios. It composes with form elements like labels and helper text, and follows MDWDS styling patterns to maintain consistency with other form controls across state websites.

---

## Data Visualizations

*Components*

Data Visualizations are components for presenting complex data, metrics, and statistics in clear, accessible formats. They help users quickly understand patterns, trends, and relationships in information. Use data visualizations when you need to communicate numerical or categorical data efficiently to diverse audiences.

### Key Information

Data visualizations in MDWDS follow USWDS patterns and accessibility standards. Common variants include:

- **Charts**: Bar charts, line charts, pie charts for displaying quantitative data
- **Tables**: Structured data presentation with sorting and filtering capabilities
- **Gauges/Meters**: Show progress, percentages, or status indicators
- **Maps**: Geographic data visualization integrated with state/local context

Key CSS classes and attributes:
- Semantic HTML5 elements for structure
- `role="img"` with `aria-label` for chart containers
- Alternative text descriptions for all visualizations
- High contrast colors compliant with WCAG AA standards
- Responsive design that adapts to mobile/tablet/desktop
- `<figure>` and `<figcaption>` for context and titles

Important facts:
- All data visualizations must include descriptive labels and legends
- Color alone should not convey information; use patterns/textures as well
- Provide data tables as alternatives to complex visualizations
- Ensure keyboard navigation and screen reader compatibility

### Implementation

```html
<!-- Basic Chart Example with Accessible Structure -->
<figure>
  <figcaption>Population Growth 2020-2024</figcaption>
  <div role="img" aria-label="Line chart showing population growth from 2020 to 2024, rising from 6 million to 6.5 million">
    <!-- Chart implementation (SVG or canvas) -->
  </div>
</figure>

<!-- Bar Chart with Legend -->
<figure>
  <figcaption>Department Budget Allocation</figcaption>
  <div role="img" aria-labelledby="chart-title chart-legend">
    <h3 id="chart-title">Budget by Department (millions)</h3>
    <!-- SVG or Canvas chart content -->
    <dl id="chart-legend">
      <dt>Education</dt><dd>$2.5M</dd>
      <dt>Transportation</dt><dd>$1.8M</dd>
      <dt>Health</dt><dd>$1.2M</dd>
    </dl>
  </div>
</figure>

<!-- Data Table Alternative -->
<table>
  <caption>Population Growth 2020-2024</caption>
  <thead>
    <tr>
      <th scope="col">Year</th>
      <th scope="col">Population</th>
      <th scope="col">Growth Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2020</td>
      <td>6,000,000</td>
      <td>—</td>
    </tr>
    <tr>
      <td>2024</td>
      <td>6,500,000</td>
      <td>+8.3%</td>
    </tr>
  </tbody>
</table>
```

### Context

Data Visualizations are part of the MDWDS Components section, built on USWDS foundations for accessibility and consistency. They compose with Typography, Color, and Layout systems to present state data and metrics clearly to Maryland residents and stakeholders.

---

## Date Picker

*Components*

The Date Picker is a form component that allows users to select a date through an interactive calendar interface or by typing directly into an input field. It solves the problem of inconsistent date entry and validation across forms. Use it when you need users to provide a specific date in a standardized format.

### Key Information

The Date Picker component includes:
- An input field for manual date entry with format guidance
- A calendar icon button that triggers an interactive calendar modal
- Support for selecting single dates
- Keyboard navigation through the calendar (arrow keys, Enter to select)
- Optional date range selection
- Built-in date validation
- ARIA labels and roles for accessibility
- Disabled date ranges or specific dates
- Mobile-responsive design
- Class names: `usa-date-picker`, `usa-date-picker__wrapper`, `usa-date-picker__input`
- ARIA attributes: `aria-label`, `aria-haspopup="dialog"`, `aria-expanded`, `role="dialog"`
- Required attributes: `type="text"` or `type="date"` on input
- JavaScript initialization required to activate calendar functionality
- Supports `min` and `max` date attributes for range constraints

### Implementation

```html
<!-- Basic Date Picker -->
<div class="usa-date-picker">
  <label class="usa-label" for="date-picker-input">
    Select a date
  </label>
  <input
    class="usa-input"
    id="date-picker-input"
    type="text"
    name="date"
    aria-label="Select a date"
  />
</div>

<!-- Date Picker with constraints -->
<div class="usa-date-picker">
  <label class="usa-label" for="date-range-input">
    Select a date (within range)
  </label>
  <input
    class="usa-input"
    id="date-range-input"
    type="text"
    name="date-range"
    min="2024-01-01"
    max="2024-12-31"
    aria-label="Select a date within range"
  />
</div>

<!-- JavaScript initialization (required) -->
<script>
  const datePickers = document.querySelectorAll('.usa-date-picker input');
  datePickers.forEach(picker => {
    // USWDS provides initialization via component API
    // Typical initialization (framework-dependent)
  });
</script>
```

### Context

The Date Picker is part of the USWDS components integrated into MDWDS and is commonly used in forms alongside other input components like text fields and dropdowns. It ensures consistent date entry practices across Maryland state web applications and supports accessible date selection for all users.

---

## Date Range Picker

*Components*

The Date Range Picker is a USWDS component that allows users to select a start and end date from a calendar interface. It simplifies date range selection for forms and filters by providing an accessible, interactive date picker with keyboard navigation and screen reader support. Use this when users need to specify a time period for searches, reporting, or data filtering.

### Key Information

## Variants and Structure
- Single calendar or dual calendar layout options
- Supports keyboard navigation (arrow keys, Enter, Escape)
- Preset range options (Last 7 days, Last 30 days, etc.)

## CSS Class Names
- `.usa-date-range-picker`: Main container
- `.usa-date-range-picker__calendar`: Calendar container
- `.usa-date-range-picker__input-group`: Input field group
- `.usa-date-range-picker__input`: Individual date input field
- `.usa-date-range-picker__button`: Calendar trigger button

## Required Attributes
- `type="date"` on input elements for native date support
- `aria-label` or `aria-labelledby` for accessibility
- `data-start-date` and `data-end-date` for programmatic date setting
- Form labels associated with each date input via `<label>` elements with `for` attributes

## Important Facts
- Built on USWDS date range picker component
- Includes built-in validation for date format
- Supports custom date formats through configuration
- Automatically handles leap years and month boundaries

### Implementation

```html
<div class="usa-date-range-picker">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">
      <label for="start-date">Start Date</label>
    </legend>
    <div class="usa-date-range-picker__input-group">
      <input 
        class="usa-date-range-picker__input usa-input"
        id="start-date"
        name="start-date"
        type="date"
        aria-label="Start Date"
      />
    </div>
  </fieldset>

  <fieldset class="usa-fieldset">
    <legend class="usa-legend">
      <label for="end-date">End Date</label>
    </legend>
    <div class="usa-date-range-picker__input-group">
      <input 
        class="usa-date-range-picker__input usa-input"
        id="end-date"
        name="end-date"
        type="date"
        aria-label="End Date"
      />
    </div>
  </fieldset>
</div>
```

## With Calendar Popup
```html
<div class="usa-date-range-picker">
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">Date Range</legend>
    <div class="usa-date-range-picker__input-group">
      <input 
        class="usa-date-range-picker__input usa-input"
        id="date-range-start"
        name="start-date"
        type="text"
        placeholder="MM/DD/YYYY"
        aria-label="Start Date"
      />
      <button 
        class="usa-button usa-button--unstyled usa-date-range-picker__button"
        type="button"
        aria-label="Open start date calendar"
      >
        <svg aria-hidden="true" class="usa-icon">
          <use xlink:href="/assets/img/sprite.svg#calendar"></use>
        </svg>
      </button>
    </div>
    <div class="usa-date-range-picker__input-group">
      <input 
        class="usa-date-range-picker__input usa-input"
        id="date-range-end"
        name="end-date"
        type="text"
        placeholder="MM/DD/YYYY"
        aria-label="End Date"
      />
      <button 
        class="usa-button usa-button--unstyled usa-date-range-picker__button"
        type="button"
        aria-label="Open end date calendar"
      >
        <svg aria-hidden="true" class="usa-icon">
          <use xlink:href="/assets/img/sprite.svg#calendar"></use>
        </svg>
      </button>
    </div>
  </fieldset>
</div>
```

### Context

The Date Range Picker is a USWDS-based component integrated into MDWDS for consistent date selection across Maryland state web applications. It composes with form fieldsets and input components to provide an accessible interface for date-based filtering and data entry.

---

## File Input

*Components*

The File Input component allows users to select and upload files from their device. It provides an accessible interface for file selection with support for multiple files and file type restrictions. Use this component when you need to collect file uploads from users in forms or data entry workflows.

### Key Information

## Variants and Modifiers

- **Single file input**: Standard file input for uploading one file
- **Multiple file input**: Allows users to select and upload multiple files at once
- **Disabled state**: File input can be disabled to prevent user interaction
- **Error state**: Displays validation errors when required files are missing or invalid

## CSS Classes

- `.usa-file-input`: Main wrapper class for the file input component
- `.usa-file-input__input`: The actual input element
- `.usa-file-input__target`: Drop zone target area

## Required Attributes

- `type="file"`: Specifies the input type as file
- `id`: Unique identifier for the input
- `name`: Form field name for data submission

## Important Facts

- Supports `accept` attribute to restrict file types (e.g., `accept=".pdf,.doc,.docx"`)
- Supports `multiple` attribute for multi-file selection
- Provides visual feedback during file selection and upload
- Includes accessible labels and error messages
- Works with form validation and submission

### Implementation

```html
<!-- Basic File Input -->
<div class="usa-file-input">
  <label class="usa-label" for="file-input-single">
    Upload a file
  </label>
  <input
    class="usa-file-input__input"
    id="file-input-single"
    type="file"
    name="file-input-single"
  />
</div>

<!-- Multiple File Input -->
<div class="usa-file-input">
  <label class="usa-label" for="file-input-multiple">
    Upload multiple files
  </label>
  <input
    class="usa-file-input__input"
    id="file-input-multiple"
    type="file"
    name="file-input-multiple"
    multiple
  />
</div>

<!-- File Input with File Type Restriction -->
<div class="usa-file-input">
  <label class="usa-label" for="file-input-restricted">
    Upload PDF or Word document
  </label>
  <input
    class="usa-file-input__input"
    id="file-input-restricted"
    type="file"
    name="file-input-restricted"
    accept=".pdf,.doc,.docx"
  />
</div>

<!-- Disabled File Input -->
<div class="usa-file-input">
  <label class="usa-label" for="file-input-disabled">
    Upload a file (disabled)
  </label>
  <input
    class="usa-file-input__input"
    id="file-input-disabled"
    type="file"
    name="file-input-disabled"
    disabled
  />
</div>

<!-- File Input with Error -->
<div class="usa-file-input">
  <label class="usa-label" for="file-input-error">
    Upload a file
  </label>
  <input
    class="usa-file-input__input"
    id="file-input-error"
    type="file"
    name="file-input-error"
    aria-invalid="true"
    aria-describedby="file-input-error-message"
  />
  <span class="usa-error-message" id="file-input-error-message" role="alert">
    Please select a valid file
  </span>
</div>
```

### Context

The File Input component is part of the MDWDS component library based on USWDS and provides a standardized way to collect file uploads across Maryland state web applications. It integrates with form validation patterns and works alongside labels, error messages, and other form components to create complete, accessible form experiences.

---

## Footer

*Components*

The Footer component provides a consistent bottom section for Maryland state web pages, containing navigation links, contact information, and legal notices. It establishes a unified visual identity across all state websites and communicates important information to users at the end of their browsing experience.

### Key Information

## Variants

- **Standard Footer**: Full-width footer with navigation links, social media links, contact information, and copyright notice
- **Minimal Footer**: Simplified version with only essential information

## CSS Classes

- `.footer`: Main footer container
- `.footer__content`: Content wrapper for footer sections
- `.footer__section`: Individual footer section
- `.footer__links`: Container for footer links
- `.footer__link`: Individual footer link
- `.footer__social`: Social media links section
- `.footer__copyright`: Copyright and legal information area

## Key Attributes

- Use semantic `<footer>` element wrapper
- Include proper navigation structure with lists for link groups
- Social media links should have descriptive `aria-label` attributes
- Copyright text should be in a `<small>` or `<p>` tag

## Important Facts

- Footer should appear on every page for consistency
- Ensure sufficient color contrast for all text and links
- Include contact information and agency links
- Support responsive layout on mobile devices

### Implementation

```html
<footer class="footer">
  <div class="footer__content">
    <div class="footer__section">
      <h3>Quick Links</h3>
      <ul class="footer__links">
        <li><a href="#" class="footer__link">About</a></li>
        <li><a href="#" class="footer__link">Services</a></li>
        <li><a href="#" class="footer__link">Contact</a></li>
      </ul>
    </div>
    
    <div class="footer__section">
      <h3>Follow Us</h3>
      <div class="footer__social">
        <a href="#" class="footer__link" aria-label="Facebook">Facebook</a>
        <a href="#" class="footer__link" aria-label="Twitter">Twitter</a>
      </div>
    </div>
  </div>
  
  <div class="footer__copyright">
    <small>&copy; 2024 State of Maryland. All rights reserved.</small>
  </div>
</footer>
```

### Context

The Footer is a fundamental layout component in MDWDS that anchors the bottom of state web pages and maintains visual consistency across Maryland government sites. It typically composes with the Header and main content areas to create a complete page template structure.

---

## Form

*Components*

Form is a foundational component that groups input fields and controls to collect user data. Forms are essential for user interaction and data submission on web pages. Use forms whenever you need to gather information from users in an organized, accessible manner.

### Key Information

## USWDS Form Components

The Form component is built on USWDS (U.S. Web Design System) standards and includes:

### Key Variants & Elements:
- **Text Inputs**: Basic text field inputs with labels
- **Checkboxes**: Multiple selection options
- **Radio Buttons**: Single selection from options
- **Select Dropdowns**: Predefined option selection
- **Textareas**: Multi-line text input
- **Form Groups**: Wrapper for logical field grouping

### CSS Classes:
- `.usa-form`: Main form wrapper class
- `.usa-form-group`: Groups form fields with spacing
- `.usa-label`: Styles form labels
- `.usa-input`: Styles input fields
- `.usa-checkbox`, `.usa-radio`: Wrapper classes for checkboxes and radio buttons
- `.usa-select`: Styles select dropdowns
- `.usa-textarea`: Styles textarea elements
- `.usa-form__note`: Adds helper text or hints
- `.usa-error`: Indicates error state
- `.usa-hint`: Helper text styling

### Required Attributes:
- `<label>` with `for` attribute matching input `id`
- Input elements must have unique `id` attributes
- `name` attribute on all input elements
- `type` attribute specifying input type

### Important Facts:
- All form inputs should have associated labels for accessibility
- Error messaging should use ARIA live regions
- Forms support both inline and block display modes
- USWDS forms follow 508 compliance standards
- Form validation should provide clear user feedback

### Implementation

```html
<!-- Basic Form Structure -->
<form class="usa-form">
  <!-- Text Input -->
  <div class="usa-form-group">
    <label class="usa-label" for="input-name">Name</label>
    <input class="usa-input" id="input-name" type="text" name="name">
  </div>

  <!-- Text Input with Error -->
  <div class="usa-form-group usa-form-group--error">
    <label class="usa-label" for="input-error">Field with Error</label>
    <span class="usa-error-message" id="input-error-message" role="alert">Error message here</span>
    <input class="usa-input usa-input--error" id="input-error" type="text" name="error-field" aria-describedby="input-error-message">
  </div>

  <!-- Textarea -->
  <div class="usa-form-group">
    <label class="usa-label" for="textarea-example">Comments</label>
    <textarea class="usa-textarea" id="textarea-example" name="comments"></textarea>
  </div>

  <!-- Checkbox -->
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">Checkbox Options</legend>
    <div class="usa-checkbox">
      <input class="usa-checkbox__input" id="checkbox-1" type="checkbox" name="checkbox-option" value="option-1">
      <label class="usa-checkbox__label" for="checkbox-1">Option 1</label>
    </div>
    <div class="usa-checkbox">
      <input class="usa-checkbox__input" id="checkbox-2" type="checkbox" name="checkbox-option" value="option-2">
      <label class="usa-checkbox__label" for="checkbox-2">Option 2</label>
    </div>
  </fieldset>

  <!-- Radio Buttons -->
  <fieldset class="usa-fieldset">
    <legend class="usa-legend">Radio Options</legend>
    <div class="usa-radio">
      <input class="usa-radio__input" id="radio-1" type="radio" name="radio-option" value="option-1">
      <label class="usa-radio__label" for="radio-1">Option 1</label>
    </div>
    <div class="usa-radio">
      <input class="usa-radio__input" id="radio-2" type="radio" name="radio-option" value="option-2">
      <label class="usa-radio__label" for="radio-2">Option 2</label>
    </div>
  </fieldset>

  <!-- Select Dropdown -->
  <div class="usa-form-group">
    <label class="usa-label" for="select-example">Select an option</label>
    <select class="usa-select" id="select-example" name="select-option">
      <option>- Select -</option>
      <option value="option-1">Option 1</option>
      <option value="option-2">Option 2</option>
    </select>
  </div>

  <!-- Helper Text -->
  <div class="usa-form-group">
    <label class="usa-label" for="input-hint">Field with Helper Text</label>
    <span class="usa-hint" id="input-hint-text">This is helper text to guide the user</span>
    <input class="usa-input" id="input-hint" type="text" name="hint-field" aria-describedby="input-hint-text">
  </div>

  <!-- Submit Button -->
  <button class="usa-button" type="submit">Submit</button>
</form>
```

### Context

Form is a core USWDS component that composes with other input components like buttons, text fields, and validation messaging. It serves as the primary pattern for data collection across the Maryland Design System and integrates with validation, error handling, and accessibility standards.

---

## Header

*Components*

The Header component is the primary navigation and branding element at the top of Maryland state web pages. It provides consistent identification of state government properties and serves as the main entry point for site navigation.

### Key Information

The Header is a critical layout component that typically contains:
- Maryland state branding/logo
- Site title and description
- Primary navigation menu
- Possible utility links (search, language toggle, etc.)

**Standard variants:**
- Full header with all branding and navigation elements
- Compact header for space-constrained layouts
- Sticky/fixed positioning option for persistent navigation

**Key CSS classes:**
- `.header` - Main container
- `.header__branding` - Branding section with logo
- `.header__navigation` - Navigation menu container
- `.header__utility` - Utility/secondary navigation area

**Required attributes:**
- Semantic HTML5 `<header>` element
- `role="banner"` for accessibility on header element
- Navigation should use `<nav>` with appropriate `aria-label`

**Important facts:**
- Must meet WCAG accessibility standards
- Responsive design adapts layout for mobile/tablet/desktop
- Logo typically links to homepage
- Navigation items should be keyboard accessible

### Implementation

```html
<header class="header" role="banner">
  <div class="header__container">
    <!-- Branding Section -->
    <div class="header__branding">
      <a href="/" class="header__logo">
        <img src="/images/md-logo.svg" alt="Maryland State Logo" />
      </a>
      <div class="header__title">
        <h1 class="header__site-title">Site Title</h1>
        <p class="header__site-description">Site description or tagline</p>
      </div>
    </div>

    <!-- Main Navigation -->
    <nav class="header__navigation" aria-label="Main navigation">
      <ul class="header__menu">
        <li class="header__menu-item">
          <a href="/about" class="header__menu-link">About</a>
        </li>
        <li class="header__menu-item">
          <a href="/services" class="header__menu-link">Services</a>
        </li>
        <li class="header__menu-item">
          <a href="/contact" class="header__menu-link">Contact</a>
        </li>
      </ul>
    </nav>

    <!-- Utility Links -->
    <div class="header__utility">
      <button class="header__search-toggle" aria-label="Search">
        <span class="icon-search"></span>
      </button>
    </div>
  </div>
</header>
```

**Mobile-Responsive Variant (with hamburger menu):**
```html
<header class="header" role="banner">
  <div class="header__container">
    <div class="header__branding">
      <a href="/" class="header__logo">
        <img src="/images/md-logo.svg" alt="Maryland State Logo" />
      </a>
      <div class="header__title">
        <h1 class="header__site-title">Site Title</h1>
      </div>
    </div>

    <!-- Mobile Menu Toggle -->
    <button class="header__menu-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="header-nav">
      <span></span>
      <span></span>
      <span></span>
    </button>

    <!-- Navigation (hidden on mobile) -->
    <nav class="header__navigation" id="header-nav" aria-label="Main navigation">
      <ul class="header__menu">
        <li class="header__menu-item">
          <a href="/about" class="header__menu-link">About</a>
        </li>
        <li class="header__menu-item">
          <a href="/services" class="header__menu-link">Services</a>
        </li>
      </ul>
    </nav>
  </div>
</header>
```

### Context

The Header is a foundational structural component of MDWDS that typically wraps and composes with Navigation, Search, and Utility Link components. It establishes the visual hierarchy and state branding identity across all Maryland government web pages.

---

## Hero

*Components*

The Hero component is a full-width banner section that creates a prominent, visually striking introduction to a page or section. It typically combines a large background image, headline, and call-to-action elements to establish context and guide user attention. Use Hero components at the top of landing pages, section introductions, or campaign pages to establish visual hierarchy and engage users immediately.

### Key Information

The Hero component creates a high-impact introductory section with the following characteristics:

- **Variants**: Standard Hero (image background), Hero with overlay for text readability, Hero with gradient overlay
- **Structure**: Container with background image, overlay layer, content area with headline and supporting text
- **CSS Classes**: `.hero`, `.hero__overlay`, `.hero__content`, `.hero__title`, `.hero__subtitle`
- **Modifiers**: 
  - `.hero--light` for light overlay tint
  - `.hero--dark` for dark overlay tint
  - `.hero--center` for centered content alignment
  - Height modifiers: `.hero--large`, `.hero--medium`, `.hero--small`
- **Background**: Typically set via inline style or CSS `background-image` property; supports solid colors or images
- **Content**: Flexible container for heading, subheading, and button groups
- **Accessibility**: Use semantic HTML (`<h1>`, `<h2>`); ensure sufficient color contrast on overlays; provide `alt` text if background image is decorative

### Implementation

```html
<!-- Standard Hero with image background and overlay -->
<section class="hero hero--dark" style="background-image: url('/path/to/image.jpg');">
  <div class="hero__overlay"></div>
  <div class="hero__content">
    <h1 class="hero__title">Page Title</h1>
    <p class="hero__subtitle">Supporting description or tagline</p>
  </div>
</section>
```

```html
<!-- Hero with centered content and light overlay -->
<section class="hero hero--center hero--light" style="background-image: url('/path/to/image.jpg');">
  <div class="hero__overlay"></div>
  <div class="hero__content">
    <h1 class="hero__title">Centered Hero Section</h1>
    <p class="hero__subtitle">Optional description text</p>
    <div class="hero__actions">
      <a href="#" class="btn btn--primary">Call to Action</a>
    </div>
  </div>
</section>
```

```html
<!-- Hero with solid color background -->
<section class="hero hero--dark" style="background-color: #003f87;">
  <div class="hero__content">
    <h1 class="hero__title">Color-Based Hero</h1>
    <p class="hero__subtitle">No image background, solid color fill</p>
  </div>
</section>
```

```html
<!-- Hero with large height modifier -->
<section class="hero hero--large hero--dark" style="background-image: url('/path/to/image.jpg');">
  <div class="hero__overlay"></div>
  <div class="hero__content">
    <h1 class="hero__title">Large Hero Section</h1>
    <p class="hero__subtitle">Prominent page introduction</p>
  </div>
</section>
```

### Context

The Hero component is a foundational content section in MDWDS, typically appearing at the top of page layouts to establish visual identity and context. It works in conjunction with Typography, Button, and Image components and often precedes other content sections like Featured Content or Card grids to create a cohesive visual hierarchy.

---

## Highlight

*Components*

The Highlight component is a visual element used to draw attention to important content, text, or sections within a page. It provides a way to emphasize key information and guide users' focus to critical areas. Use it when you need to make specific content stand out from surrounding text or sections.

### Key Information


## Variants and Modifiers
- Standard highlight with default styling
- Multiple color variants for different emphasis levels
- Inline and block-level application options

## CSS Class Names
- `.highlight` - Base highlight class for text emphasis
- Modifier classes for color variants (specific variants depend on design system palette)

## Key Attributes
- Can be applied to inline elements (span, strong) or block elements (div, section)
- Should include appropriate semantic HTML when possible
- Supports standard text and background color combinations

## Important Facts
- Use sparingly to avoid overwhelming the page
- Ensure sufficient contrast ratios for accessibility (WCAG AA minimum)
- Works well with headings and key statistics or callouts


### Implementation


```html
<!-- Inline text highlight -->
<p>This is <span class="highlight">important text</span> that needs emphasis.</p>

<!-- Block-level highlight -->
<div class="highlight">
  <p>This entire section is highlighted for emphasis.</p>
</div>

<!-- Color variant examples (adjust class names based on your palette) -->
<span class="highlight highlight--primary">Primary highlight</span>
<span class="highlight highlight--secondary">Secondary highlight</span>
<span class="highlight highlight--success">Success highlight</span>
```


### Context

The Highlight component is a foundational styling utility within MDWDS that enhances content emphasis across various page types. It integrates with the color system and typography components to create consistent visual hierarchy throughout Maryland state web pages.

---

## Icon

*Components*

Icons are small graphical symbols used to visually represent actions, concepts, or states within the Maryland Web Design System. They enhance user interfaces by providing visual clarity and improving accessibility when paired with text labels. Use icons to reinforce navigation items, action buttons, status indicators, or to support content understanding.

### Key Information

## Variants & Usage

- **Decorative Icons**: Used for visual enhancement alongside text; should have `aria-hidden="true"` and not require screen reader announcement
- **Semantic Icons**: Convey meaning and should be accessible; pair with visible text labels or descriptive ARIA attributes
- **Icon Sizes**: Typically use standard sizing (16px, 24px, 32px) for consistency
- **Color**: Inherit from parent text color or apply explicit color classes for status indicators

## CSS Classes & Structure

- Base icon container typically uses `<svg>` or icon library classes
- Icons should scale responsively and maintain aspect ratio
- Use `aria-hidden="true"` for purely decorative icons
- Use `aria-label` or descriptive text for functional icons
- Apply color modifiers for status: success, warning, error, info states

## Important Attributes

- `role="img"` when icon conveys meaning independently
- `aria-hidden="true"` for decorative icons
- `aria-label` for accessibility when icon lacks visible text
- `focusable="false"` on SVG elements to prevent keyboard focus on icon-only elements

### Implementation

```html
<!-- Decorative Icon (hidden from screen readers) -->
<span class="icon-wrapper">
  <svg class="icon" aria-hidden="true" width="24" height="24">
    <use xlink:href="#icon-id"></use>
  </svg>
</span>

<!-- Semantic Icon with Label -->
<button class="btn">
  <svg class="icon" aria-hidden="true" width="24" height="24">
    <use xlink:href="#icon-download"></use>
  </svg>
  <span>Download</span>
</button>

<!-- Icon-only Button with Accessibility -->
<button class="btn-icon" aria-label="Close dialog">
  <svg class="icon" width="24" height="24" focusable="false">
    <use xlink:href="#icon-close"></use>
  </svg>
</button>

<!-- Icon with Status Color -->
<span class="icon-status icon-status--success" role="img" aria-label="Completed">
  <svg class="icon" width="24" height="24">
    <use xlink:href="#icon-check"></use>
  </svg>
</span>
```

### Context

Icons are a foundational visual element in the Maryland Web Design System that compose with buttons, navigation, form fields, and other components to improve usability and visual communication. They follow USWDS icon patterns and integrate with the design system's color palette and spacing system.

---

## Icon List

*Components*

The Icon List component displays a list of items with accompanying icons, useful for presenting features, benefits, or key points in a scannable format. It organizes content hierarchically with visual indicators to improve readability and user engagement. Use it when you need to highlight multiple related items or concepts that benefit from visual reinforcement.

### Key Information

## Variants and Options

- **Standard Icon List**: Basic list with icons and text labels
- **Icon positioning**: Icons can appear to the left of text (default) or inline
- **Icon sizes**: Multiple size options available to match content hierarchy
- **List styling**: Supports ordered and unordered list variations

## Key Attributes

- Icons are typically implemented using inline SVG or icon font classes
- List items use semantic HTML list elements (`<ul>` or `<ol>`)
- Each item should contain an icon and descriptive text
- ARIA labels should be present for accessibility

## CSS Classes

- `.icon-list`: Main container class
- `.icon-list__item`: Individual list item wrapper
- `.icon-list__icon`: Icon container
- `.icon-list__content`: Text/content wrapper for each item

## Important Facts

- Icons should be meaningful and contextually relevant
- Text content should be concise and scannable
- List items should have consistent styling and spacing
- Supports both icon and text-only content blocks

### Implementation

```html
<ul class="icon-list">
  <li class="icon-list__item">
    <div class="icon-list__icon">
      <svg aria-hidden="true" role="img" viewBox="0 0 24 24">
        <!-- SVG icon content -->
      </svg>
    </div>
    <div class="icon-list__content">
      <h3>Item Title</h3>
      <p>Item description or supporting text</p>
    </div>
  </li>
  <li class="icon-list__item">
    <div class="icon-list__icon">
      <svg aria-hidden="true" role="img" viewBox="0 0 24 24">
        <!-- SVG icon content -->
      </svg>
    </div>
    <div class="icon-list__content">
      <h3>Item Title</h3>
      <p>Item description or supporting text</p>
    </div>
  </li>
</ul>
```

## Ordered List Variant

```html
<ol class="icon-list icon-list--ordered">
  <li class="icon-list__item">
    <div class="icon-list__icon">
      <span class="icon-list__number">1</span>
    </div>
    <div class="icon-list__content">
      <h3>Step Title</h3>
      <p>Step description</p>
    </div>
  </li>
</ol>
```

### Context

The Icon List component is a versatile MDWDS component that combines typography and iconography to present related information in an accessible, scannable format. It works alongside the Icon system and Typography components to create cohesive information hierarchies across Maryland state web pages.

---

## Icon List

*Components*

An Icon List is a USWDS component that displays a vertical list of items, each with an accompanying icon, text, and optional description. It's used to present related information in an organized, scannable format and helps users quickly identify and understand different options or items at a glance.

### Key Information

## Variants and Modifiers

- **Standard Icon List**: Basic list with icon, title, and description for each item
- **Icon styling**: Icons are typically Font Awesome or system icons
- **Item structure**: Each list item contains an icon element, title text, and optional description text
- **Alignment options**: Icons can be vertically aligned with text content

## CSS Classes

- `.usa-icon-list`: Main container for the icon list
- `.usa-icon-list__item`: Individual list item wrapper
- `.usa-icon-list__icon`: Icon container within each item
- `.usa-icon-list__title`: Title text within each item
- `.usa-icon-list__description`: Optional description text within each item

## Key Attributes

- Uses semantic HTML with `<ul>` or `<ol>` list structure
- Icons can be `<svg>` elements or icon font classes
- No required JavaScript functionality
- Supports responsive layout through USWDS grid system

## Important Facts

- Part of the USWDS component library
- Maintains accessibility standards with proper semantic HTML
- Works with Font Awesome icons or SVG assets
- Flexible for various use cases: features, benefits, requirements lists

### Implementation

```html
<ul class="usa-icon-list">
  <li class="usa-icon-list__item">
    <div class="usa-icon-list__icon">
      <svg class="usa-icon" aria-hidden="true" role="img">
        <use xlink:href="/assets/img/sprite.svg#check"></use>
      </svg>
    </div>
    <div class="usa-icon-list__content">
      <h3 class="usa-icon-list__title">First Item</h3>
      <p class="usa-icon-list__description">Description of the first item goes here.</p>
    </div>
  </li>
  <li class="usa-icon-list__item">
    <div class="usa-icon-list__icon">
      <svg class="usa-icon" aria-hidden="true" role="img">
        <use xlink:href="/assets/img/sprite.svg#star"></use>
      </svg>
    </div>
    <div class="usa-icon-list__content">
      <h3 class="usa-icon-list__title">Second Item</h3>
      <p class="usa-icon-list__description">Description of the second item goes here.</p>
    </div>
  </li>
</ul>
```

## Variant with Font Awesome Icons

```html
<ul class="usa-icon-list">
  <li class="usa-icon-list__item">
    <div class="usa-icon-list__icon">
      <i class="fa fa-check" aria-hidden="true"></i>
    </div>
    <div class="usa-icon-list__content">
      <h3 class="usa-icon-list__title">Feature Title</h3>
      <p class="usa-icon-list__description">Feature description text.</p>
    </div>
  </li>
</ul>
```

### Context

Icon List is a USWDS component that integrates into the Maryland Design System for presenting grouped content with visual indicators. It composes well with other layout components and is commonly used in hero sections, feature descriptions, and informational pages to create visual hierarchy and improve scanability.

---

## Identifier

*Components*

The Identifier component is a standardized header element used to identify Maryland state government websites and provide consistent branding across the MDWDS system. It establishes official state agency presence and helps users recognize legitimate state web properties.

### Key Information

The Identifier is a USWDS component that serves as a mandatory header for Maryland state websites. It typically includes:

- **Required elements**: State seal or logo, agency name, and official "An official website of the State of Maryland" text
- **Class names**: Uses USWDS classes like `usa-identifier`, `usa-identifier__header`, `usa-identifier__container`, `usa-identifier__section`
- **Structure**: Header section containing official state designation, followed by extended/required links sections
- **Sections**: Can include multiple sections for different types of links (agency information, official links, contact information)
- **Modifiers**: Supports compact and standard layouts with different link configurations
- **ARIA attributes**: Includes semantic landmark roles and proper heading hierarchy for accessibility
- **Links**: Typically contains links to privacy policy, accessibility statement, site feedback, and contact information

### Implementation

```html
<footer class="usa-identifier">
  <div class="usa-identifier__section usa-identifier__header">
    <div class="usa-identifier__container">
      <div class="usa-identifier__logo">
        <a href="/" title="Home">
          <img class="usa-identifier__logo-img" src="/assets/img/logos/maryland-state-seal.svg" alt="Maryland State Seal" />
        </a>
      </div>
      <section class="usa-identifier__identity" aria-label="Agency description">
        <p class="usa-identifier__identity-domain">maryland.gov</p>
        <p class="usa-identifier__identity-disclaimer">An official website of the State of Maryland</p>
      </section>
    </div>
  </div>
  
  <nav class="usa-identifier__section usa-identifier__nav" aria-label="Footer navigation">
    <div class="usa-identifier__container">
      <ul class="usa-identifier__required-links">
        <li class="usa-identifier__required-links-item">
          <a href="/accessibility" class="usa-identifier__required-link">Accessibility</a>
        </li>
        <li class="usa-identifier__required-links-item">
          <a href="/privacy" class="usa-identifier__required-link">Privacy Policy</a>
        </li>
        <li class="usa-identifier__required-links-item">
          <a href="/contact" class="usa-identifier__required-link">Contact Us</a>
        </li>
      </ul>
    </div>
  </nav>
</footer>
```

Alternative compact variant:

```html
<footer class="usa-identifier usa-identifier--compact">
  <div class="usa-identifier__container">
    <div class="usa-identifier__identity">
      <p class="usa-identifier__identity-domain">maryland.gov</p>
      <p class="usa-identifier__identity-disclaimer">An official website of the State of Maryland</p>
    </div>
    <ul class="usa-identifier__required-links">
      <li class="usa-identifier__required-links-item">
        <a href="/accessibility" class="usa-identifier__required-link">Accessibility</a>
      </li>
      <li class="usa-identifier__required-links-item">
        <a href="/privacy" class="usa-identifier__required-link">Privacy</a>
      </li>
      <li class="usa-identifier__required-links-item">
        <a href="/contact" class="usa-identifier__required-link">Contact</a>
      </li>
    </ul>
  </div>
</footer>
```

### Context

The Identifier is a foundational USWDS component adopted by the Maryland Web Design System to ensure consistent state branding across all official Maryland government websites. It works in conjunction with the Header and Footer components to create a cohesive top-level page structure that establishes user trust and official state presence.

---

## In Page Navigation

*Components*

In Page Navigation is a USWDS component that provides users with a way to navigate within a single page, typically using anchor links to jump to different sections. It helps users understand the page structure and quickly access relevant content, particularly useful on long pages with multiple sections.

### Key Information

- **Component Type**: Navigation aid for single-page navigation
- **CSS Classes**: Uses USWDS utility classes for styling and structure
- **Key Attributes**: Requires proper heading hierarchy and ID attributes on target sections
- **Variants**: Can be positioned as sticky sidebar navigation or inline navigation
- **Accessibility**: Must include proper ARIA labels and semantic HTML structure
- **Link Structure**: Uses anchor links (href="#section-id") pointing to page section IDs
- **Responsive**: Adapts to different screen sizes, typically collapsing on mobile devices

### Implementation

```html
<!-- Basic In Page Navigation Structure -->
<nav class="usa-sidenav" aria-label="In-page navigation">
  <ul class="usa-sidenav__list">
    <li class="usa-sidenav__item">
      <a href="#section-1" class="usa-sidenav__link">Section One</a>
    </li>
    <li class="usa-sidenav__item">
      <a href="#section-2" class="usa-sidenav__link">Section Two</a>
    </li>
    <li class="usa-sidenav__item">
      <a href="#section-3" class="usa-sidenav__link">Section Three</a>
    </li>
  </ul>
</nav>

<!-- Page Sections with anchor IDs -->
<main>
  <section id="section-1">
    <h2>Section One</h2>
    <!-- Content here -->
  </section>
  
  <section id="section-2">
    <h2>Section Two</h2>
    <!-- Content here -->
  </section>
  
  <section id="section-3">
    <h2>Section Three</h2>
    <!-- Content here -->
  </section>
</main>
```

```html
<!-- Nested Navigation Variant -->
<nav class="usa-sidenav" aria-label="In-page navigation">
  <ul class="usa-sidenav__list">
    <li class="usa-sidenav__item">
      <a href="#parent-1" class="usa-sidenav__link">Parent Section</a>
      <ul class="usa-sidenav__sublist">
        <li class="usa-sidenav__item">
          <a href="#child-1" class="usa-sidenav__link">Subsection</a>
        </li>
      </ul>
    </li>
  </ul>
</nav>
```

### Context

In Page Navigation is a USWDS component adopted by MDWDS that works alongside main site navigation to help users navigate long-form content. It commonly composes with heading hierarchy and section elements to create scannable, accessible page structures across Maryland state websites.

---

## Input

*Components*

The Input component is a form field element that allows users to enter text-based data. It's a fundamental building block for collecting user information in forms and serves as the basis for various input types including text, email, password, and search fields.

### Key Information

## Variants and Types
- **Text Input**: Standard single-line text field
- **Email Input**: Specialized for email addresses with appropriate keyboard
- **Password Input**: Masks character input for security
- **Search Input**: Optimized for search functionality
- **Number Input**: Accepts numeric values only
- **Tel Input**: Formatted for telephone numbers

## CSS Class Names
- `.usa-input` - Base input class
- `.usa-input--error` - Error state modifier
- `.usa-input--success` - Success state modifier
- `.usa-input--disabled` - Disabled state

## Required Attributes
- `type` - Specifies the input type (text, email, password, etc.)
- `id` - Unique identifier for accessibility
- `name` - Form field name for submission
- `aria-describedby` - Links to error/help text when present

## Key Features
- Full width by default within form groups
- Support for placeholder text
- Error messaging integration
- Help text support
- Required field indicators
- Validation states (error, success)
- Disabled state support

### Implementation

## Basic Text Input
```html
<div class="usa-form-group">
  <label class="usa-label" for="input-text">Text input label</label>
  <input class="usa-input" id="input-text" type="text" name="input-text" />
</div>
```

## Email Input
```html
<div class="usa-form-group">
  <label class="usa-label" for="input-email">Email input label</label>
  <input class="usa-input" id="input-email" type="email" name="input-email" />
</div>
```

## Password Input
```html
<div class="usa-form-group">
  <label class="usa-label" for="input-password">Password input label</label>
  <input class="usa-input" id="input-password" type="password" name="input-password" />
</div>
```

## Input with Error State
```html
<div class="usa-form-group usa-form-group--error">
  <label class="usa-label" for="input-error">Input with error</label>
  <span class="usa-error-message" id="input-error--error-message" role="alert">
    <span class="usa-sr-only">Error:</span>
    This field is required
  </span>
  <input 
    class="usa-input usa-input--error" 
    id="input-error" 
    type="text" 
    name="input-error"
    aria-describedby="input-error--error-message"
  />
</div>
```

## Input with Help Text
```html
<div class="usa-form-group">
  <label class="usa-label" for="input-help">Input with help text</label>
  <span class="usa-hint" id="input-help--hint">
    This is helpful text
  </span>
  <input 
    class="usa-input" 
    id="input-help" 
    type="text" 
    name="input-help"
    aria-describedby="input-help--hint"
  />
</div>
```

## Disabled Input
```html
<div class="usa-form-group">
  <label class="usa-label" for="input-disabled">Disabled input</label>
  <input 
    class="usa-input" 
    id="input-disabled" 
    type="text" 
    name="input-disabled"
    disabled
  />
</div>
```

## Search Input
```html
<div class="usa-form-group">
  <label class="usa-label" for="input-search">Search</label>
  <input 
    class="usa-input" 
    id="input-search" 
    type="search" 
    name="input-search" 
  />
</div>
```

### Context

The Input component is a foundational USWDS element used throughout the Maryland Web Design System for form data collection. It works in conjunction with labels, form groups, hint text, and error messaging to create accessible and user-friendly form experiences aligned with federal design standards.

---

## Input Mask

*Components*

Input Mask is a component that formats user input in real-time as it's being entered, typically for structured data like phone numbers, dates, or social security numbers. It improves data quality and user experience by guiding users to enter information in the correct format without requiring manual validation.

### Key Information

Input Mask enforces a predefined input format by automatically inserting separators and restricting input to appropriate characters. Common variants include:

- **Phone Number Mask**: Formats input as (XXX) XXX-XXXX
- **Date Mask**: Formats input as MM/DD/YYYY
- **Social Security Number**: Formats input as XXX-XX-XXXX
- **Credit Card**: Formats input as XXXX XXXX XXXX XXXX

Key CSS classes and attributes:
- Input field should have `type="text"` with a `data-mask` attribute specifying the format pattern
- Use ARIA attributes like `aria-label` or `aria-describedby` to communicate the expected format to assistive technologies
- The mask pattern can be defined via JavaScript initialization or HTML attributes
- Common patterns use X for numeric input, A for alphabetic, and * for alphanumeric characters

Important considerations:
- Always provide visible label text describing the expected format
- Include helper text or placeholder text showing an example format
- Ensure the unmasked value is captured for backend processing
- Test with screen readers to ensure the mask doesn't interfere with accessibility

### Implementation

```html
<!-- Basic Phone Number Input Mask -->
<div class="form-group">
  <label for="phone-input">Phone Number</label>
  <input
    id="phone-input"
    type="text"
    class="usa-input"
    data-mask="(999) 999-9999"
    placeholder="(555) 123-4567"
    aria-label="Phone number in the format (555) 123-4567"
  />
</div>

<!-- Date Input Mask -->
<div class="form-group">
  <label for="date-input">Date of Birth</label>
  <input
    id="date-input"
    type="text"
    class="usa-input"
    data-mask="99/99/9999"
    placeholder="MM/DD/YYYY"
    aria-describedby="date-help-text"
  />
  <span id="date-help-text" class="usa-hint">Format: MM/DD/YYYY</span>
</div>

<!-- Social Security Number Mask -->
<div class="form-group">
  <label for="ssn-input">Social Security Number</label>
  <input
    id="ssn-input"
    type="text"
    class="usa-input"
    data-mask="999-99-9999"
    placeholder="XXX-XX-XXXX"
    aria-label="Social security number"
  />
</div>
```

**JavaScript Initialization (if using IMask library):**

```javascript
import IMask from 'imask';

// Phone mask
IMask(document.getElementById('phone-input'), {
  mask: '(000) 000-0000',
  definitions: {
    '0': /[0-9]/
  }
});

// Date mask
IMask(document.getElementById('date-input'), {
  mask: '00/00/0000',
  definitions: {
    '0': /[0-9]/
  }
});
```

### Context

Input Mask is a specialized component that wraps standard form inputs from the USWDS input library, adding real-time formatting behavior. It composes with the form group structure and label system to provide enhanced user experience for structured data entry while maintaining accessibility standards.

---

## Input Prefix/Suffix

*Components*

Input Prefix/Suffix components add decorative or informational text before or after form input fields. They help clarify the type of input expected (e.g., currency symbols, units of measurement) and improve form clarity and user understanding.

### Key Information

## Variants
- **Prefix**: Text or icon displayed before the input field
- **Suffix**: Text or icon displayed after the input field
- **Combined**: Both prefix and suffix on the same input

## CSS Classes
- `.usa-input-group`: Wrapper for input with prefix/suffix
- `.usa-input-prefix`: Container for prefix content
- `.usa-input-suffix`: Container for suffix content
- `.usa-input`: The actual input field (when used with prefix/suffix)

## Key Attributes
- Input fields should have appropriate `type` attributes (text, number, email, etc.)
- Use semantic HTML with label associations via `for` and `id`
- Prefix/suffix elements should not be interactive (or use `aria-hidden="true"` if decorative)

## Important Facts
- Prefixes and suffixes are typically read-only text, not interactive elements
- They help with international inputs, currency, phone numbers, and measurements
- Ensure sufficient color contrast if using icons
- Works with all standard input types

### Implementation

```html
<!-- Input with Prefix -->
<div class="usa-input-group">
  <span class="usa-input-prefix" aria-hidden="true">$</span>
  <label for="input-prefix" class="usa-label">Amount</label>
  <input class="usa-input" id="input-prefix" type="text" name="amount" />
</div>

<!-- Input with Suffix -->
<div class="usa-input-group">
  <label for="input-suffix" class="usa-label">Distance</label>
  <input class="usa-input" id="input-suffix" type="text" name="distance" />
  <span class="usa-input-suffix" aria-hidden="true">miles</span>
</div>

<!-- Input with Both Prefix and Suffix -->
<div class="usa-input-group">
  <span class="usa-input-prefix" aria-hidden="true">+1</span>
  <label for="input-both" class="usa-label">Phone Number</label>
  <input class="usa-input" id="input-both" type="text" name="phone" />
  <span class="usa-input-suffix" aria-hidden="true">ext.</span>
</div>
```

### Context

Input Prefix/Suffix is a USWDS component integrated into MDWDS that enhances form inputs by providing visual context. It works alongside Form Group, Label, and other form components to create complete, accessible form interfaces for Maryland state applications.

---

## Language Selector

*Components*

The Language Selector is a UI component that allows users to switch between different language options on a website. It provides accessibility and inclusivity by enabling non-English speakers to view content in their preferred language. This component is essential for government websites serving diverse populations.

### Key Information

The Language Selector typically includes:

- **Purpose**: Allows users to change the current page/site language
- **Placement**: Usually positioned in the header or toolbar area for easy access
- **Common variants**: 
  - Dropdown selector with language codes or names
  - Flag icons with language names
  - Text-based language links
- **Accessibility**: Should include proper ARIA labels and semantic HTML
- **Required attributes**: 
  - Language option values (e.g., "en", "es", "fr")
  - Current language indication
  - Clear labeling for screen readers
- **Composition**: Often part of a header or navigation toolbar component
- **USWDS Integration**: This component follows USWDS (U.S. Web Design System) patterns and standards

### Implementation

```html
<!-- Language Selector - Dropdown Pattern -->
<div class="language-selector">
  <label for="language-select" class="language-selector__label">
    Select Language
  </label>
  <select id="language-select" class="language-selector__select" aria-label="Select page language">
    <option value="en" selected>English</option>
    <option value="es">Español</option>
    <option value="fr">Français</option>
    <option value="zh">中文</option>
  </select>
</div>

<!-- Language Selector - Link Pattern -->
<div class="language-selector" role="navigation" aria-label="Language selection">
  <span class="language-selector__current" aria-current="page">English</span>
  <ul class="language-selector__list">
    <li><a href="?lang=es" hreflang="es">Español</a></li>
    <li><a href="?lang=fr" hreflang="fr">Français</a></li>
    <li><a href="?lang=zh" hreflang="zh">中文</a></li>
  </ul>
</div>

<!-- Language Selector - Button Pattern with Menu -->
<div class="language-selector">
  <button 
    id="language-toggle" 
    class="language-selector__button" 
    aria-haspopup="menu" 
    aria-expanded="false"
    aria-label="Change language">
    English
  </button>
  <ul id="language-menu" class="language-selector__menu" role="menu" hidden>
    <li role="none"><a href="?lang=en" role="menuitem">English</a></li>
    <li role="none"><a href="?lang=es" role="menuitem">Español</a></li>
    <li role="none"><a href="?lang=fr" role="menuitem">Français</a></li>
  </ul>
</div>
```

### Context

The Language Selector is a USWDS-based component that integrates into Maryland state websites to provide multilingual support. It typically appears in the header or toolbar alongside other navigation elements and works in conjunction with site-wide internationalization infrastructure to dynamically change page content.

---

## Link Collection

*Components*

Link Collection is a component that groups related links together in an organized, scannable layout. It helps users quickly find and navigate to related pages or resources within a section of content. Use it to display sets of related links, navigation groups, or resource lists in a visually organized manner.

### Key Information

## Variants and Modifiers
- Standard link collection with title and description support
- Multiple link items within a collection
- Optional descriptions or labels for each link
- Support for internal and external links

## CSS Classes
- `.link-collection` - Main container class
- `.link-collection__title` - For collection heading/title
- `.link-collection__item` - Individual link item wrapper
- `.link-collection__link` - Link element styling

## Required Attributes
- Each link should have proper `href` attribute
- Use semantic HTML with `<a>` elements
- Consider ARIA labels for complex collections

## Important Facts
- Collections should be logically grouped by topic or section
- Maintains consistent link styling across the system
- Responsive and accessible by default

### Implementation

```html
<div class="link-collection">
  <h2 class="link-collection__title">Collection Title</h2>
  
  <ul class="link-collection__items">
    <li class="link-collection__item">
      <a href="#" class="link-collection__link">First Related Link</a>
    </li>
    <li class="link-collection__item">
      <a href="#" class="link-collection__link">Second Related Link</a>
    </li>
    <li class="link-collection__item">
      <a href="#" class="link-collection__link">Third Related Link</a>
    </li>
  </ul>
</div>
```

## With Descriptions
```html
<div class="link-collection">
  <h2 class="link-collection__title">Related Resources</h2>
  
  <ul class="link-collection__items">
    <li class="link-collection__item">
      <a href="#" class="link-collection__link">Link Title</a>
      <p class="link-collection__description">Brief description of the link destination</p>
    </li>
  </ul>
</div>
```

### Context

Link Collection is a reusable component within MDWDS that helps organize related navigational elements and can be composed with other components like cards, sections, or page layouts to create cohesive information hierarchies.

---

## Links

*Components*

Links are interactive text elements that navigate users to different pages, sections, or external resources. They provide a fundamental way for users to traverse the web and access related content. Links should be semantically meaningful, properly styled, and accessible to all users including those using assistive technologies.

### Key Information

## Variants and Modifiers

- **Standard Link**: Basic hyperlink with underline and color styling
- **Visited Link**: Changes appearance after being visited by the user
- **Hover State**: Interactive feedback when user hovers over the link
- **Active/Focus State**: Visible focus indicator for keyboard navigation
- **Disabled Link**: Non-interactive link state (when applicable)

## Important Attributes

- `href`: Required attribute that specifies the link destination (URL or anchor)
- `target`: Optional attribute for link behavior (e.g., `_blank` for new tab)
- `rel`: Important for external links (e.g., `rel="noopener noreferrer"`)
- `aria-label`: Provide descriptive labels when link text is ambiguous
- `aria-current`: Use for current page in navigation (e.g., `aria-current="page"`)

## CSS Classes

- Standard link styling should be applied through semantic HTML (`<a>` tags)
- Links inherit color and underline decoration from component or utility classes
- Focus states must provide sufficient contrast and be keyboard-accessible

## Accessibility Considerations

- Links must have descriptive, meaningful text
- Avoid generic text like "Click here" or "Read more"
- Ensure sufficient color contrast between link and background
- Provide visible focus indicators for keyboard navigation
- Use `rel` attribute appropriately for security on external links

### Implementation

## Basic Link

```html
<a href="/destination-page">Link Text</a>
```

## External Link

```html
<a href="https://external-site.com" target="_blank" rel="noopener noreferrer">
  External Link
</a>
```

## Link with Descriptive Label

```html
<a href="/page" aria-label="Read more about topic name">
  Read more
</a>
```

## Link with Current Page Indicator (Navigation)

```html
<a href="/current-page" aria-current="page">
  Current Page
</a>
```

## Link with Focus Styling (CSS)

```css
a {
  color: #0066cc;
  text-decoration: underline;
}

a:hover {
  color: #004b99;
}

a:focus {
  outline: 3px solid #ffd700;
  outline-offset: 2px;
}

a:visited {
  color: #663366;
}
```

### Context

Links are foundational interactive elements used throughout the MDWDS system in navigation components, content areas, and utility patterns. They compose with navigation systems (menus, breadcrumbs) and are essential for building accessible, user-friendly Maryland state websites.

---

## Links

*Components*

Links are interactive elements that navigate users to different pages, sections, or external resources. They are fundamental navigation components that help users move through content and access related information. Use links for inline text navigation, primary actions, or to guide users to different pages within your application.

### Key Information

## Variants

- **Default/Text Link**: Standard hyperlink with underline, typically blue with hover states
- **External Link**: Link to external websites, often indicated with an icon
- **Disabled Link**: Non-interactive link state when navigation is unavailable
- **Visited Link**: Indicates a previously visited link with different styling

## CSS Class Names

- `.usa-link`: Base class for styled links
- `.usa-link--external`: Modifier for external links with icon indicator
- `.usa-link--unstyled`: Removes default link styling
- `.usa-link--hover`: Defines hover state styling

## Attributes

- `href`: Required - specifies the link destination
- `title`: Optional - provides tooltip or additional context
- `aria-label`: Optional - accessible label for screen readers
- `target="_blank"`: Opens link in new tab/window
- `rel="noopener noreferrer"`: Security attribute for external links opening in new tab

## Important Facts

- Links should have descriptive text that indicates the destination or action
- Use semantic HTML `<a>` elements for accessibility
- Ensure sufficient color contrast for readability
- Provide visual indication for visited, hover, and focus states
- External links should be clearly distinguished from internal links
- Links should be keyboard accessible (focus visible)

### Implementation

```html
<!-- Basic Link -->
<a href="https://maryland.gov" class="usa-link">Maryland Home</a>

<!-- External Link -->
<a href="https://example.com" class="usa-link usa-link--external" target="_blank" rel="noopener noreferrer">
  External Resource
</a>

<!-- Unstyled Link -->
<a href="/page" class="usa-link usa-link--unstyled">Unstyled Link</a>

<!-- Link with Aria Label -->
<a href="/services" class="usa-link" aria-label="Go to Services page">
  Services
</a>

<!-- Disabled Link (using span or aria-disabled) -->
<a href="#" class="usa-link" aria-disabled="true" tabindex="-1">
  Disabled Link
</a>
```

### Context

Links are core navigation components in MDWDS that enable user movement through content. They work alongside the navigation components and are used extensively throughout templates and page layouts to create hierarchical navigation structures.

---

## Listing Page

*Components*

A listing page component is a layout template used to display collections of items, content, or data in an organized grid or list format. It provides a structured way to present multiple related items with consistent styling and spacing. Use this component when you need to display searchable, filterable, or paginated collections of content on Maryland state web pages.

### Key Information

The Listing Page component is a template-level component that serves as a container for presenting multiple items in a consistent format. Key features include:

- **Purpose**: Displays collections of items (articles, services, documents, etc.) in a structured layout
- **Variants**: Can support grid or list view layouts
- **Composition**: Typically includes a header section, optional filtering/search controls, and item containers
- **Spacing**: Uses consistent margin and padding utilities for visual rhythm
- **Responsive**: Adapts to different screen sizes with appropriate grid columns
- **Item Structure**: Each item can include image, title, description, metadata, and call-to-action elements
- **Optional Features**: May include sorting, filtering, search, and pagination controls

### Implementation

```html
<!-- Basic Listing Page Structure -->
<div class="listing-page">
  <header class="listing-page__header">
    <h1 class="listing-page__title">Page Title</h1>
    <p class="listing-page__description">Optional description or introductory text</p>
  </header>

  <section class="listing-page__controls">
    <!-- Optional search and filter controls -->
    <input type="search" placeholder="Search items..." class="listing-page__search" />
  </section>

  <div class="listing-page__items">
    <!-- Grid of items -->
    <article class="listing-item">
      <div class="listing-item__image">
        <img src="image.jpg" alt="Item image" />
      </div>
      <div class="listing-item__content">
        <h2 class="listing-item__title">Item Title</h2>
        <p class="listing-item__description">Item description</p>
        <div class="listing-item__metadata">
          <span class="listing-item__date">Date</span>
        </div>
      </div>
      <div class="listing-item__actions">
        <a href="#" class="button">Learn More</a>
      </div>
    </article>
    <!-- Additional items repeat -->
  </div>

  <!-- Optional pagination -->
  <nav class="listing-page__pagination" aria-label="Pagination">
    <!-- Pagination controls -->
  </nav>
</div>
```

### Context

The Listing Page is a template-level component in MDWDS that combines smaller components (cards, buttons, search inputs) to create a complete page layout for presenting collections. It follows MDWDS spacing, typography, and color utilities while providing a flexible structure for various content types.

---

## Lists

*Components*

Lists are fundamental content structures used to organize and present related items in a logical sequence. They help users quickly scan and understand grouped information, making content more digestible and improving readability. Use lists when you need to present multiple related items, steps, or information points in a structured format.

### Key Information

## List Types

- **Unordered Lists (`<ul>`)**: Used for items without a required sequence or priority
- **Ordered Lists (`<ol>`)**: Used for sequential steps, rankings, or items requiring a specific order
- **Description Lists (`<dl>`)**: Used for term-definition pairs or label-value relationships

## CSS Classes

- `usa-list`: Standard USWDS list styling class
- Applied to `<ul>`, `<ol>`, or `<dl>` elements

## Variants

- **Unstyled Lists**: Remove default list styling with utility classes
- **Nested Lists**: Lists can contain other lists for hierarchical organization
- **Plain Lists**: Basic semantic HTML without additional styling

## Important Notes

- Always use semantic HTML list elements (`<ul>`, `<ol>`, `<dl>`)
- Lists should contain `<li>` items (or `<dt>`/`<dd>` for description lists)
- Lists improve accessibility and SEO when properly structured
- Proper nesting maintains logical document structure

### Implementation

## Unordered List

```html
<ul class="usa-list">
  <li>Item one</li>
  <li>Item two</li>
  <li>Item three</li>
</ul>
```

## Ordered List

```html
<ol class="usa-list">
  <li>First step</li>
  <li>Second step</li>
  <li>Third step</li>
</ol>
```

## Description List

```html
<dl class="usa-list">
  <dt>Term</dt>
  <dd>Definition or description</dd>
  <dt>Another term</dt>
  <dd>Another definition</dd>
</dl>
```

## Nested Lists

```html
<ul class="usa-list">
  <li>
    Main item
    <ul>
      <li>Nested item one</li>
      <li>Nested item two</li>
    </ul>
  </li>
  <li>Another main item</li>
</ul>
```

### Context

Lists are a foundational content component in MDWDS built on USWDS standards, providing semantic HTML structure for organizing information. They compose with other components like cards and sections to structure page content and improve content hierarchy and accessibility.

---

## Memorable Date

*Components*

The Memorable Date component is a date input pattern that helps users enter dates in an easy-to-remember format by breaking the date into separate fields for month, day, and year. It solves the problem of ambiguous date entry and improves accessibility for users entering date information. Use this component whenever you need to collect date information from users in a clear, memorable, and accessible way.

### Key Information

## Variants and Structure
- Three separate input fields for month (MM), day (DD), and year (YYYY)
- Each field is individually labeled and can be focused
- Supports keyboard navigation between fields with auto-advance on maximum characters
- Built on USWDS date input patterns

## CSS Classes
- `.usa-input` - Applied to each date input field
- `.usa-form-group` - Container for the date fieldset
- `.usa-fieldset` - Wrapper for the entire memorable date input group
- `.usa-legend` - Label for the fieldset

## Attributes and ARIA
- `aria-label` or `aria-describedby` for accessibility context
- `inputmode="numeric"` - Appropriate input mode for date fields
- `maxlength` attributes to limit character input (2 for MM/DD, 4 for YYYY)
- `type="text"` - Use text input with numeric input mode for better browser support
- `name` attribute should follow pattern: `[name]-month`, `[name]-day`, `[name]-year`

## Modifiers and Options
- Error state: Apply `.usa-input--error` class when validation fails
- Disabled state: `disabled` attribute on input fields
- Required fields: Mark with `required` attribute and visual indicator
- Hint text support for format guidance (e.g., "MM/DD/YYYY")

## Important Facts
- Provides better UX than single date input field for date entry
- Supports tab navigation and auto-focus to next field when maximum characters entered
- Compatible with screen readers when properly labeled
- Should include error messages for invalid dates

### Implementation

## Basic Memorable Date Input

```html
<fieldset class="usa-fieldset">
  <legend class="usa-legend">
    <span class="usa-label">Date of birth</span>
    <span class="usa-hint">For example: 12/31/1999</span>
  </legend>
  
  <div class="usa-memorable-date">
    <div class="usa-form-group usa-form-group--month">
      <label class="usa-label" for="birth-month">Month</label>
      <input
        class="usa-input"
        id="birth-month"
        name="birth-month"
        type="text"
        inputmode="numeric"
        maxlength="2"
        placeholder="MM"
        aria-label="Month"
        required
      />
    </div>
    
    <div class="usa-form-group usa-form-group--day">
      <label class="usa-label" for="birth-day">Day</label>
      <input
        class="usa-input"
        id="birth-day"
        name="birth-day"
        type="text"
        inputmode="numeric"
        maxlength="2"
        placeholder="DD"
        aria-label="Day"
        required
      />
    </div>
    
    <div class="usa-form-group usa-form-group--year">
      <label class="usa-label" for="birth-year">Year</label>
      <input
        class="usa-input"
        id="birth-year"
        name="birth-year"
        type="text"
        inputmode="numeric"
        maxlength="4"
        placeholder="YYYY"
        aria-label="Year"
        required
      />
    </div>
  </div>
</fieldset>
```

## With Error State

```html
<fieldset class="usa-fieldset">
  <legend class="usa-legend">
    <span class="usa-label">Date of birth</span>
  </legend>
  
  <span class="usa-error-message" role="alert">
    <span class="usa-sr-only">Error:</span> Please enter a valid date
  </span>
  
  <div class="usa-memorable-date">
    <div class="usa-form-group usa-form-group--month">
      <label class="usa-label" for="birth-month-error">Month</label>
      <input
        class="usa-input usa-input--error"
        id="birth-month-error"
        name="birth-month-error"
        type="text"
        inputmode="numeric"
        maxlength="2"
        placeholder="MM"
        aria-invalid="true"
        aria-describedby="birth-error-message"
        required
      />
    </div>
    
    <div class="usa-form-group usa-form-group--day">
      <label class="usa-label" for="birth-day-error">Day</label>
      <input
        class="usa-input usa-input--error"
        id="birth-day-error"
        name="birth-day-error"
        type="text"
        inputmode="numeric"
        maxlength="2"
        placeholder="DD"
        aria-invalid="true"
        aria-describedby="birth-error-message"
        required
      />
    </div>
    
    <div class="usa-form-group usa-form-group--year">
      <label class="usa-label" for="birth-year-error">Year</label>
      <input
        class="usa-input usa-input--error"
        id="birth-year-error"
        name="birth-year-error"
        type="text"
        inputmode="numeric"
        maxlength="4"
        placeholder="YYYY"
        aria-invalid="true"
        aria-describedby="birth-error-message"
        required
      />
    </div>
  </div>
</fieldset>
```

### Context

The Memorable Date component is part of MDWDS's form components built on U.S. Web Design System (USWDS) patterns. It composes with other form components like fieldsets, labels, and error messages to create accessible date input experiences for Maryland state web applications.

---

## Modal

*Components*

A Modal is a dialog component that displays content in a layer above the main page, typically requiring user interaction before dismissing. It prevents interaction with the page behind it and is commonly used for confirmations, alerts, or focused user tasks. Use modals when you need to capture user attention for important decisions or information that requires immediate action.

### Key Information

## Modal Variants and Modifiers

- **Basic Modal**: Standard dialog with title, body content, and action buttons
- **Alert Modal**: Emphasizes important information or warnings
- **Confirmation Modal**: Requests user confirmation before an action
- **Full-screen Modal**: Expands to fill the viewport on smaller screens

## Key CSS Classes
- `.usa-modal`: Main modal container
- `.usa-modal__backdrop`: Semi-transparent overlay behind the modal
- `.usa-modal__dialog`: The modal dialog box itself
- `.usa-modal__header`: Header section containing title and close button
- `.usa-modal__title`: Title text
- `.usa-modal__close`: Close button
- `.usa-modal__body`: Main content area
- `.usa-modal__footer`: Footer section for action buttons

## ARIA Attributes
- `role="dialog"`: Required on modal dialog element
- `aria-labelledby="[id]"`: Links dialog to its title element
- `aria-modal="true"`: Indicates element is a modal dialog
- `aria-hidden="true"`: Applied to page content when modal is open (handled by JS)

## Required Attributes
- Modal must have a unique `id`
- Close button should have `aria-label="Close modal"`
- Title should have unique `id` referenced in `aria-labelledby`

## JavaScript Initialization
- Modal requires JavaScript to handle open/close functionality
- Escape key should close the modal
- Focus should trap within the modal when open
- Focus should return to trigger element when modal closes

### Implementation

```html
<!-- Basic Modal Structure -->
<div class="usa-modal" id="example-modal" aria-labelledby="modal-title" aria-modal="true" role="dialog">
  <div class="usa-modal__backdrop"></div>
  <div class="usa-modal__dialog">
    <header class="usa-modal__header">
      <h2 class="usa-modal__title" id="modal-title">Modal Title</h2>
      <button class="usa-modal__close" aria-label="Close modal">
        <svg class="usa-icon" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41z"></path>
        </svg>
      </button>
    </header>
    <div class="usa-modal__body">
      <p>Modal content goes here. This is the main body of the modal dialog.</p>
    </div>
    <footer class="usa-modal__footer">
      <button class="usa-button usa-button--secondary">Cancel</button>
      <button class="usa-button">Confirm</button>
    </footer>
  </div>
</div>

<!-- Alert Modal -->
<div class="usa-modal usa-modal--alert" id="alert-modal" aria-labelledby="alert-title" aria-modal="true" role="dialog">
  <div class="usa-modal__backdrop"></div>
  <div class="usa-modal__dialog">
    <header class="usa-modal__header">
      <h2 class="usa-modal__title" id="alert-title">Alert</h2>
      <button class="usa-modal__close" aria-label="Close modal">
        <svg class="usa-icon" aria-hidden="true" focusable="false" role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41z"></path>
        </svg>
      </button>
    </header>
    <div class="usa-modal__body">
      <p>This is an important alert message that requires user attention.</p>
    </div>
    <footer class="usa-modal__footer">
      <button class="usa-button">OK</button>
    </footer>
  </div>
</div>
```

## JavaScript Initialization Example

```javascript
// Open modal
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.add('is-visible');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    // Trap focus within modal
    const focusableElements = modal.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
    if (focusableElements.length > 0) {
      focusableElements[0].focus();
    }
  }
}

// Close modal
function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.remove('is-visible');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }
}

// Handle close button
document.querySelectorAll('.usa-modal__close').forEach(btn => {
  btn.addEventListener('click', function() {
    const modal = this.closest('.usa-modal');
    closeModal(modal.id);
  });
});

// Handle backdrop click
document.querySelectorAll('.usa-modal__backdrop').forEach(backdrop => {
  backdrop.addEventListener('click', function() {
    const modal = this.closest('.usa-modal');
    closeModal(modal.id);
  });
});

// Handle Escape key
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    document.querySelectorAll('.usa-modal.is-visible').forEach(modal => {
      closeModal(modal.id);
    });
  }
});
```

### Context

The Modal component is part of the MDWDS built on the U.S. Web Design System (USWDS) and provides accessible dialog functionality for Maryland state web pages. It composes with Button components for actions and works alongside the overall page layout system to manage focus and accessibility when overlaying content.

---

## Navigation

*Components*

Navigation is a core component that provides users with a way to move between pages and sections of a website. It establishes the information hierarchy and helps users understand where they are within the site structure. Navigation is essential for usability and is typically placed at the top or side of a page to ensure discoverability.

### Key Information

The Navigation component serves as the primary way for users to traverse the website. Key variants and options include:

- **Primary Navigation**: Main site navigation typically displayed in a horizontal bar or vertical sidebar
- **Breadcrumb Navigation**: Secondary navigation showing the user's current location in the hierarchy
- **Footer Navigation**: Additional navigation links placed in the footer
- **Mobile Navigation**: Responsive navigation that collapses into a menu on smaller screens
- **Active State**: Visual indicator showing the current page or section
- **Sub-navigation/Dropdowns**: Nested menu items for organizing related links
- **ARIA Attributes**: Uses `role="navigation"`, `aria-label`, and `aria-current="page"` for accessibility
- **CSS Classes**: Typically includes classes like `nav`, `nav-item`, `nav-link`, `nav-active`, `nav-submenu`
- **Mobile Menu Toggle**: Button with `aria-expanded` and `aria-controls` for toggling navigation visibility on mobile

### Implementation

```html
<!-- Primary Navigation -->
<nav role="navigation" aria-label="Main navigation">
  <ul class="nav">
    <li class="nav-item">
      <a href="/" class="nav-link nav-active" aria-current="page">Home</a>
    </li>
    <li class="nav-item">
      <a href="/about" class="nav-link">About</a>
    </li>
    <li class="nav-item nav-submenu-parent">
      <a href="/services" class="nav-link" aria-expanded="false" aria-haspopup="true">Services</a>
      <ul class="nav-submenu" hidden>
        <li class="nav-item">
          <a href="/services/design" class="nav-link">Design</a>
        </li>
        <li class="nav-item">
          <a href="/services/development" class="nav-link">Development</a>
        </li>
      </ul>
    </li>
    <li class="nav-item">
      <a href="/contact" class="nav-link">Contact</a>
    </li>
  </ul>
</nav>

<!-- Mobile Navigation Toggle -->
<button class="nav-toggle" aria-expanded="false" aria-controls="mobile-nav" aria-label="Toggle navigation menu">
  <span class="nav-toggle-icon"></span>
</button>

<!-- Breadcrumb Navigation -->
<nav role="navigation" aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item">
      <a href="/">Home</a>
    </li>
    <li class="breadcrumb-item">
      <a href="/services">Services</a>
    </li>
    <li class="breadcrumb-item" aria-current="page">Design</li>
  </ol>
</nav>
```

### Context

Navigation is a foundational component in MDWDS that provides the primary means of moving through Maryland state websites. It typically integrates with the header and footer components and works across responsive breakpoints to ensure accessibility and usability for all users.

---

## Pagination

*Components*

Pagination provides navigation for users to move between pages of content. It allows users to quickly jump to different sections of multi-page results or content. Use pagination when displaying large datasets or content that needs to be broken into manageable pages.

### Key Information

## Variants
- Standard pagination with previous/next buttons and numbered page links
- First/last page buttons available in extended versions
- Active page indicator shows current position
- Disabled state for buttons at boundaries (first/last page)

## CSS Classes
- `.usa-pagination` - Main pagination container
- `.usa-pagination__list` - List wrapper for page items
- `.usa-pagination__item` - Individual page item
- `.usa-pagination__button` - Page button (link or button element)
- `.usa-pagination__button--previous` - Previous button variant
- `.usa-pagination__button--next` - Next button variant
- `.usa-pagination__button--active` - Active/current page indicator

## Attributes & Options
- Link-based or button-based implementation
- Previous/next arrows or text labels
- Number of visible page links is configurable
- Current page should be marked with `aria-current="page"`
- Disabled buttons should have `disabled` attribute
- Uses semantic `<nav>` element with descriptive label

## Required Structure
- Navigation role or semantic `<nav>` element
- Unordered list (`<ul>`) for page items
- Links or buttons for navigation targets
- Proper ARIA labels and descriptions for accessibility

### Implementation

```html
<nav aria-label="Pagination" class="usa-pagination">
  <ul class="usa-pagination__list">
    <li class="usa-pagination__item">
      <a href="#" class="usa-pagination__button usa-pagination__button--previous">
        <span class="usa-pagination__link-text">Previous</span>
      </a>
    </li>
    <li class="usa-pagination__item">
      <a href="#" class="usa-pagination__button">
        <span class="usa-pagination__link-text">1</span>
      </a>
    </li>
    <li class="usa-pagination__item">
      <a href="#" class="usa-pagination__button usa-pagination__button--active" aria-current="page">
        <span class="usa-pagination__link-text">2</span>
      </a>
    </li>
    <li class="usa-pagination__item">
      <a href="#" class="usa-pagination__button">
        <span class="usa-pagination__link-text">3</span>
      </a>
    </li>
    <li class="usa-pagination__item">
      <a href="#" class="usa-pagination__button usa-pagination__button--next">
        <span class="usa-pagination__link-text">Next</span>
      </a>
    </li>
  </ul>
</nav>
```

## Disabled State Example
```html
<nav aria-label="Pagination" class="usa-pagination">
  <ul class="usa-pagination__list">
    <li class="usa-pagination__item">
      <button disabled class="usa-pagination__button usa-pagination__button--previous">
        <span class="usa-pagination__link-text">Previous</span>
      </button>
    </li>
    <li class="usa-pagination__item">
      <a href="#" class="usa-pagination__button usa-pagination__button--active" aria-current="page">
        <span class="usa-pagination__link-text">1</span>
      </a>
    </li>
    <li class="usa-pagination__item">
      <a href="#" class="usa-pagination__button usa-pagination__button--next">
        <span class="usa-pagination__link-text">Next</span>
      </a>
    </li>
  </ul>
</nav>
```

### Context

Pagination is a USWDS component integrated into MDWDS that aids in content navigation for large datasets on Maryland state web pages. It works with data tables, search results, and list views to help users traverse multi-page content efficiently.

---

## Process List

*Components*

A Process List displays a series of steps or stages in a sequential order, typically used to guide users through multi-step processes, workflows, or procedural information. It helps users understand where they are in a process and what comes next, improving clarity and navigation through complex procedures.

### Key Information

## Variants and Structure
- **Sequential display**: Steps are shown in numerical or visual order
- **Step indicators**: Uses numbering or progress markers to show sequence
- **Descriptive text**: Each step includes a heading and description
- **Current state indication**: Can highlight the active or current step
- **Completed steps**: Can visually distinguish completed steps from pending ones

## CSS Class Names
- `.usa-process-list`: Main container class
- `.usa-process-list__item`: Individual step/list item
- `.usa-process-list__heading`: Step heading
- `.usa-process-list__description`: Step description text

## Key Attributes
- Semantic structure using `<ol>` for ordered lists
- Each step should have clear heading hierarchy (h2, h3, etc.)
- ARIA labels and roles for accessibility if needed
- Data attributes for tracking active/completed states

## Important Facts
- Part of USWDS component library integrated into MDWDS
- Works best for 3-10 steps (too many steps may need pagination)
- Can be styled for horizontal or vertical orientation
- Pairs well with buttons or CTAs at each step

### Implementation

```html
<ol class="usa-process-list">
  <li class="usa-process-list__item">
    <h2 class="usa-process-list__heading">
      Step 1: Apply
    </h2>
    <p class="usa-process-list__description">
      Submit your application with required documentation to begin the process.
    </p>
  </li>
  <li class="usa-process-list__item">
    <h2 class="usa-process-list__heading">
      Step 2: Review
    </h2>
    <p class="usa-process-list__description">
      Our team reviews your submission and may request additional information.
    </p>
  </li>
  <li class="usa-process-list__item">
    <h2 class="usa-process-list__heading">
      Step 3: Approval
    </h2>
    <p class="usa-process-list__description">
      Once approved, you will receive confirmation and next steps via email.
    </p>
  </li>
</ol>
```

## Variant: With Current Step Indicator
```html
<ol class="usa-process-list">
  <li class="usa-process-list__item">
    <h2 class="usa-process-list__heading">Step 1: Apply</h2>
    <p class="usa-process-list__description">Complete and submit your application.</p>
  </li>
  <li class="usa-process-list__item" aria-current="step">
    <h2 class="usa-process-list__heading">Step 2: Review (Current)</h2>
    <p class="usa-process-list__description">We are currently reviewing your submission.</p>
  </li>
  <li class="usa-process-list__item">
    <h2 class="usa-process-list__heading">Step 3: Approval</h2>
    <p class="usa-process-list__description">Final approval pending.</p>
  </li>
</ol>
```

### Context

The Process List is a foundational USWDS component integrated into MDWDS for guiding users through state services workflows and procedures. It works alongside buttons, form components, and other instructional elements to create clear, step-by-step user experiences on Maryland state web pages.

---

## Promo

*Components*

The Promo component is a prominent content showcase used to highlight featured content, announcements, or key messages within a page. It combines eye-catching visuals with clear calls-to-action to engage users and direct them toward important information or actions. Use promos to feature program announcements, upcoming events, or significant updates that deserve prominent placement.

### Key Information

## Variants & Modifiers
- Standard promo with background image and overlay text
- Promo with left-aligned content
- Promo with right-aligned content
- Promo with call-to-action button
- Optional dark overlay for text contrast
- Responsive design that adapts from multi-column on desktop to single-column on mobile

## CSS Classes
- `.promo` - Main container
- `.promo-image` - Background image container
- `.promo-content` - Text content wrapper
- `.promo-title` - Heading element
- `.promo-description` - Descriptive text
- `.promo-cta` - Call-to-action button or link area

## Key Attributes
- Use semantic HTML (`<section>`, `<h2>`, `<p>`)
- Include alt text for background images if used as `<img>` element
- CTA should use `<a>` or `<button>` with appropriate link/action attributes
- Consider `aria-label` for icon-only CTAs

## Important Facts
- Promos are typically full-width or constrained-width components
- Can be placed in hero sections, feature sections, or mid-page
- Should include a clear visual hierarchy with heading, description, and CTA
- Aspect ratio typically 16:9 or 4:3 depending on layout preference

### Implementation

```html
<!-- Standard Promo Component -->
<section class="promo">
  <div class="promo-image" style="background-image: url('path/to/image.jpg'); background-size: cover; background-position: center;">
    <div class="promo-overlay"></div>
  </div>
  <div class="promo-content">
    <h2 class="promo-title">Featured Program Title</h2>
    <p class="promo-description">Compelling description of the featured content or announcement goes here.</p>
    <a href="#" class="promo-cta btn btn-primary">Learn More</a>
  </div>
</section>
```

```html
<!-- Promo with Left-Aligned Content -->
<section class="promo promo-left">
  <div class="promo-image"></div>
  <div class="promo-content">
    <h2 class="promo-title">Title</h2>
    <p class="promo-description">Description text.</p>
    <a href="#" class="promo-cta btn btn-primary">Action</a>
  </div>
</section>
```

```html
<!-- Promo with Right-Aligned Content -->
<section class="promo promo-right">
  <div class="promo-content">
    <h2 class="promo-title">Title</h2>
    <p class="promo-description">Description text.</p>
    <a href="#" class="promo-cta btn btn-primary">Action</a>
  </div>
  <div class="promo-image"></div>
</section>
```

### Context

The Promo component is a key visual component in the MDWDS used alongside other content containers to create engaging page layouts. It often works with Button components for calls-to-action and integrates with the spacing and layout utilities to maintain consistency across Maryland state web pages.

---

## Prose

*Components*

Prose is a typographic component for rendering readable, accessible body text and narrative content. It applies consistent styling to semantic HTML elements like paragraphs, lists, blockquotes, and tables to ensure proper hierarchy and readability across Maryland state web pages.

### Key Information

The Prose component provides semantic styling for text-based content. It includes styles for:

- **Paragraphs**: Proper line-height and spacing for readability
- **Headings**: Semantic h1-h6 elements with appropriate sizing and hierarchy
- **Lists**: Both ordered (ol) and unordered (ul) lists with proper indentation
- **Blockquotes**: Styled quotation elements
- **Links**: Properly styled and accessible hyperlinks
- **Tables**: Readable table layouts with borders and padding
- **Code blocks**: Monospace text styling for technical content
- **Emphasis**: Bold (strong) and italic (em) text

The component uses the USWDS typography system and applies classes from the MDWDS design tokens to ensure consistency. The prose styling automatically applies to all nested semantic elements without requiring additional classes on individual items.

### Implementation

```html
<div class="prose">
  <h1>Main Heading</h1>
  <p>This is a paragraph with <strong>bold text</strong> and <em>italic text</em>.</p>
  
  <h2>Subheading</h2>
  <p>Paragraphs are automatically styled with proper spacing and line-height.</p>
  
  <ul>
    <li>Unordered list item</li>
    <li>Another list item</li>
  </ul>
  
  <ol>
    <li>Ordered list item</li>
    <li>Another ordered item</li>
  </ol>
  
  <blockquote>
    <p>This is a blockquote with semantic styling applied automatically.</p>
  </blockquote>
  
  <table>
    <thead>
      <tr>
        <th>Header 1</th>
        <th>Header 2</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Data cell</td>
        <td>Data cell</td>
      </tr>
    </tbody>
  </table>
  
  <a href="#">Links are styled for accessibility</a>
</div>
```

### Context

Prose is a foundational text styling component in MDWDS that works in conjunction with the typography system and other content components. It ensures that narrative content maintains consistent readability and accessibility across all Maryland state websites by automatically applying the design system's typography standards to semantic HTML elements.

---

## Radios

*Components*

Radio buttons allow users to select a single option from a set of mutually exclusive choices. They are used in forms when only one answer from a group should be selected at a time. Use radios when there are 2-5 options; consider a select dropdown for longer lists.

### Key Information

## Variants and Options

- **Default radio**: Single selectable button with label
- **Disabled state**: Non-interactive radio with `disabled` attribute
- **Checked state**: Pre-selected radio using `checked` attribute
- **Tile variant**: Radio styled as a clickable card/tile with optional description
- **Legend and fieldset**: Group of radios wrapped in `<fieldset>` with `<legend>`

## CSS Classes and Attributes

- `.usa-radio`: Container wrapper for each radio option
- `.usa-radio__input`: The actual `<input type="radio">` element
- `.usa-radio__label`: Label text associated with radio
- `.usa-radio-group`: Applied to `<fieldset>` containing radio group
- `.usa-fieldset-legend`: Applied to `<legend>` element
- `name` attribute: Same for all radios in a group (required for grouping)
- `id` attribute: Unique identifier for each radio
- `for` attribute: Label's `for` attribute must match radio's `id`
- `aria-label` or `aria-labelledby`: For accessibility on the fieldset
- `disabled`: Disables individual radio

## Modifiers

- Tile variant uses `.usa-radio__label--tile` on the label wrapper
- Disabled appearance uses `[disabled]` selector in CSS

### Implementation

## Basic Radio Group

```html
<fieldset class="usa-fieldset">
  <legend class="usa-legend">Select one option</legend>
  
  <div class="usa-radio">
    <input
      class="usa-radio__input"
      id="radio-option-1"
      type="radio"
      name="options"
      value="option-1"
    />
    <label class="usa-radio__label" for="radio-option-1">
      Option 1
    </label>
  </div>

  <div class="usa-radio">
    <input
      class="usa-radio__input"
      id="radio-option-2"
      type="radio"
      name="options"
      value="option-2"
    />
    <label class="usa-radio__label" for="radio-option-2">
      Option 2
    </label>
  </div>

  <div class="usa-radio">
    <input
      class="usa-radio__input"
      id="radio-option-3"
      type="radio"
      name="options"
      value="option-3"
      checked
    />
    <label class="usa-radio__label" for="radio-option-3">
      Option 3 (pre-selected)
    </label>
  </div>
</fieldset>
```

## Disabled Radio

```html
<div class="usa-radio">
  <input
    class="usa-radio__input"
    id="radio-disabled"
    type="radio"
    name="options"
    value="disabled"
    disabled
  />
  <label class="usa-radio__label" for="radio-disabled">
    Disabled option
  </label>
</div>
```

## Tile Variant

```html
<div class="usa-radio">
  <input
    class="usa-radio__input"
    id="radio-tile"
    type="radio"
    name="tile-options"
    value="tile-1"
  />
  <label class="usa-radio__label usa-radio__label--tile" for="radio-tile">
    <span class="usa-radio__label-text">
      Tile Option
    </span>
    <span class="usa-radio__label-description">
      Description of this tile option
    </span>
  </label>
</div>
```

### Context

Radios are a fundamental USWDS form component used throughout Maryland state web pages for single-select options. They integrate with form validation patterns and work alongside other form controls like checkboxes, text inputs, and select dropdowns as part of the MDWDS form system.

---

## Range Slider

*Components*

The Range Slider is an input component that allows users to select a value or range of values from a continuous scale by dragging a handle along a track. It provides an intuitive way for users to specify numeric values within a defined range and is commonly used for filtering, setting thresholds, or adjusting parameters in forms and interactive interfaces.

### Key Information

## Variants
- Single value range slider
- Dual handle range slider (for min/max selection)

## CSS Classes
- `.usa-range`: Base container class for the range slider
- `.usa-range__input`: The actual input element (type="range")
- `.usa-range__track`: Visual track element showing the range
- `.usa-range__track-fill`: Filled portion of the track

## Attributes
- `type="range"`: Required input type
- `min`: Minimum value of the range
- `max`: Maximum value of the range
- `value`: Current value
- `step`: Increment step (optional)
- `aria-label`: Accessible label for the input
- `aria-describedby`: Reference to description text

## Modifiers
- Single handle for single value selection
- Multiple inputs for range selection (min and max)

## Important Notes
- Native HTML5 range input with USWDS styling
- Cross-browser compatible
- Keyboard accessible (arrow keys for adjustment)
- Mobile touch-friendly

### Implementation

```html
<!-- Single Range Slider -->
<div class="usa-range">
  <label class="usa-label" for="range-single">Select a value</label>
  <input 
    class="usa-range__input" 
    type="range" 
    id="range-single"
    name="range-single"
    min="0" 
    max="100" 
    value="50"
    aria-label="Select a value between 0 and 100"
  />
</div>

<!-- Dual Range Slider (Min/Max) -->
<div class="usa-range">
  <label class="usa-label" for="range-min">Price range</label>
  <div>
    <input 
      class="usa-range__input" 
      type="range" 
      id="range-min"
      name="price-min"
      min="0" 
      max="1000" 
      value="100"
      aria-label="Minimum price"
    />
    <input 
      class="usa-range__input" 
      type="range" 
      id="range-max"
      name="price-max"
      min="0" 
      max="1000" 
      value="900"
      aria-label="Maximum price"
    />
  </div>
  <div class="usa-hint" id="range-hint">Enter minimum and maximum prices</div>
</div>
```

### Context

The Range Slider is part of the USWDS Components library integrated into MDWDS, providing a standard input control for numeric selection. It follows USWDS patterns and works alongside other form components like text inputs, buttons, and validation messages to create complete form experiences on Maryland state web pages.

---

## Search

*Components*

The Search component provides users with a way to discover and access content within a Maryland state web application. It enables users to query site-specific or application-specific information, improving content discoverability and user navigation. Use this component to help users find relevant information quickly across your site or application.

### Key Information

The Search component includes the following variants and features:

- **Basic Search**: A simple input field with a search button or submit functionality
- **CSS Classes**: Uses standard form input styling with `.search-input` or similar class names
- **ARIA Attributes**: Includes `role="search"` on the container and `aria-label` on the input field for accessibility
- **Modifiers**: May support sizing variants (small, default, large) and states (default, focused, filled, disabled)
- **Placeholder Text**: Typically includes placeholder text like "Search..." to guide user input
- **Required Attributes**: 
  - `type="search"` on the input element
  - `aria-label` or associated `<label>` element
  - `name` attribute for form submission
- **Optional Features**: Search suggestions, filtering options, and result count indicators
- **State Variations**: Default, active/focused, filled with content, disabled, and error states

### Implementation

```html
<!-- Basic Search Component -->
<form role="search" class="search-form">
  <input 
    type="search" 
    class="search-input" 
    placeholder="Search..." 
    aria-label="Search this site"
    name="q"
  />
  <button type="submit" class="search-button">
    Search
  </button>
</form>
```

```html
<!-- Search with Icon Button -->
<form role="search" class="search-form">
  <input 
    type="search" 
    class="search-input" 
    placeholder="Enter search term..."
    aria-label="Search"
    name="query"
  />
  <button type="submit" class="search-button" aria-label="Submit search">
    <svg class="icon" aria-hidden="true">
      <!-- Search icon SVG content -->
    </svg>
  </button>
</form>
```

```html
<!-- Search with Results Count -->
<form role="search" class="search-form">
  <input 
    type="search" 
    class="search-input" 
    placeholder="Search..." 
    aria-label="Search this site"
    name="q"
    aria-describedby="search-results-count"
  />
  <button type="submit" class="search-button">Search</button>
  <span id="search-results-count" class="search-results-count">0 results</span>
</form>
```

### Context

The Search component is a core utility component within MDWDS that helps users navigate and discover content across Maryland state web applications. It integrates with form systems and follows accessibility standards, working alongside navigation components and site structure patterns to enhance user experience.

---

## Search

*Components*

The Search component provides a form input field for users to enter and submit search queries on Maryland state web pages. It enables users to find relevant content, services, or information quickly across a website or application. Use this component in headers, page sections, or dedicated search interfaces to improve discoverability and user navigation.

### Key Information

The Search component is built on USWDS (U.S. Web Design System) foundation patterns. Key variants and features include:

- **Basic search input**: Simple text input field with search functionality
- **CSS Classes**: Uses USWDS utility classes for styling and layout
- **Form structure**: Implements standard HTML form element with proper semantic markup
- **Required attributes**: Input should have appropriate `name` and `id` attributes; form should have `method` and `action` attributes
- **Accessibility**: Includes ARIA labels and roles for screen reader compatibility; clear visual focus indicators
- **Modifiers**: Can be combined with buttons, autocomplete suggestions, filters, or advanced search options
- **Placeholder text**: Commonly includes "Search..." or contextual placeholder
- **Submission**: Can submit via form submission or JavaScript handlers

### Implementation

```html
<form class="usa-search usa-search--big" role="search">
  <label class="usa-sr-only" for="search-field">Search</label>
  <input
    class="usa-input"
    id="search-field"
    type="search"
    name="search"
    placeholder="Search..."
  />
  <button class="usa-button" type="submit">
    <span class="usa-search__submit-text">Search</span>
  </button>
</form>
```

**Small variant:**
```html
<form class="usa-search" role="search">
  <label class="usa-sr-only" for="search-small">Search</label>
  <input
    class="usa-input"
    id="search-small"
    type="search"
    name="search"
    placeholder="Search..."
  />
  <button class="usa-button" type="submit">
    <span class="usa-search__submit-text">Search</span>
  </button>
</form>
```

### Context

The Search component integrates with Maryland's USWDS-based design system, allowing for consistent search functionality across state web properties. It can be incorporated into header layouts, paired with filtering or faceted search patterns, and combined with other navigation components to support user information discovery.

---

## Select

*Components*

The Select component is a dropdown form element that allows users to choose one option from a predefined list. It provides an accessible way to present multiple choices in a compact, controlled manner. Use Select when you have a list of 3 or more related options and need to save vertical space while keeping the interface clean.

### Key Information

## Variants & Options

- **Basic Select**: Standard dropdown menu with text options
- **Disabled State**: Select element can be disabled to prevent user interaction
- **Required Attribute**: Use the `required` attribute to mark as mandatory form field
- **Grouped Options**: Use `<optgroup>` to organize related options

## CSS Class Names

- `usa-select`: Main class for the select element (applies USWDS styling)

## Important Attributes

- `name`: Identifies the form field
- `id`: For label association via `for` attribute
- `required`: Marks field as mandatory
- `disabled`: Disables the select element
- `aria-label` or associated `<label>`: Provides accessible label
- `aria-describedby`: References additional help text if present

## ARIA Requirements

- Must have an associated `<label>` element with matching `for` attribute OR an `aria-label`
- Use `aria-describedby` to link error messages or hint text
- `aria-disabled` may be used instead of `disabled` in some contexts

### Implementation

## Basic Select

```html
<label for="select-basic">Select an option</label>
<select id="select-basic" name="options" class="usa-select">
  <option>- Select -</option>
  <option value="option-1">Option 1</option>
  <option value="option-2">Option 2</option>
  <option value="option-3">Option 3</option>
</select>
```

## Required Select

```html
<label for="select-required">Select an option (Required)</label>
<select id="select-required" name="options" class="usa-select" required>
  <option>- Select -</option>
  <option value="option-1">Option 1</option>
  <option value="option-2">Option 2</option>
</select>
```

## Disabled Select

```html
<label for="select-disabled">Select an option</label>
<select id="select-disabled" name="options" class="usa-select" disabled>
  <option>- Select -</option>
  <option value="option-1">Option 1</option>
</select>
```

## Grouped Options

```html
<label for="select-grouped">Select a category</label>
<select id="select-grouped" name="category" class="usa-select">
  <option>- Select -</option>
  <optgroup label="Group 1">
    <option value="1-1">Option 1-1</option>
    <option value="1-2">Option 1-2</option>
  </optgroup>
  <optgroup label="Group 2">
    <option value="2-1">Option 2-1</option>
    <option value="2-2">Option 2-2</option>
  </optgroup>
</select>
```

### Context

The Select component is part of the MDWDS form elements built on USWDS foundations, providing consistent, accessible dropdown functionality across Maryland state websites. It integrates with form layouts, validation patterns, and fieldset groupings to create complete, user-friendly forms.

---

## Side Navigation

*Components*

The Side Navigation component provides a persistent, hierarchical navigation menu positioned alongside main content, enabling users to browse page sections and navigate between related content. It helps organize complex information architecture and improves discoverability of related pages within a section or application.

### Key Information

## Variants
- **Collapsed State**: Side navigation can collapse to save space on smaller viewports or per user preference
- **Nested Navigation**: Supports multi-level hierarchical menu structures with expandable/collapsible sub-items
- **Active States**: Current page or section is highlighted to indicate user's location
- **Link Types**: Supports both internal links and anchor links to page sections

## Key Features
- Uses semantic list markup (`<ul>` and `<li>` elements) for proper document structure
- Expandable/collapsible sections for managing deep hierarchies
- ARIA labels and roles for screen reader accessibility
- Responsive behavior adapting to mobile/tablet/desktop viewports
- Keyboard navigation support through natural tab order and arrow keys

## CSS Classes
- Primary container classes for layout and styling
- Active/selected state indicators for current page
- Modifier classes for collapsed state and responsive behaviors
- Indent classes for nested level indication

## Important Attributes
- `aria-current` or `aria-selected` on active navigation items
- `aria-expanded` on collapsible menu items
- `role="navigation"` on the navigation container
- `aria-label` for descriptive navigation purpose

## Responsive Considerations
- Mobile: May collapse or convert to drawer pattern on small screens
- Tablet/Desktop: Displays as persistent sidebar
- Toggle button typically required for mobile collapse/expand functionality

### Implementation

```html
<!-- Basic Side Navigation Structure -->
<nav role="navigation" aria-label="Side Navigation">
  <ul class="side-navigation">
    <li>
      <a href="/section1" aria-current="page">Current Page</a>
    </li>
    <li>
      <a href="/section2">Other Section</a>
    </li>
  </ul>
</nav>

<!-- With Nested/Expandable Items -->
<nav role="navigation" aria-label="Side Navigation">
  <ul class="side-navigation">
    <li>
      <button 
        aria-expanded="false" 
        aria-controls="submenu-1"
        class="side-navigation__toggle"
      >
        Parent Item
      </button>
      <ul id="submenu-1" class="side-navigation__submenu" hidden>
        <li>
          <a href="/parent/child1">Child Item 1</a>
        </li>
        <li>
          <a href="/parent/child2">Child Item 2</a>
        </li>
      </ul>
    </li>
    <li>
      <a href="/section2">Standalone Item</a>
    </li>
  </ul>
</nav>

<!-- Collapsed/Responsive State -->
<div class="side-navigation-wrapper">
  <button 
    class="side-navigation__toggle-main"
    aria-controls="side-nav"
    aria-label="Toggle navigation menu"
  >
    Menu
  </button>
  <nav 
    id="side-nav" 
    role="navigation" 
    aria-label="Side Navigation"
    class="side-navigation side-navigation--collapsed"
  >
    <ul class="side-navigation">
      <li><a href="/section1" aria-current="page">Current Page</a></li>
      <li><a href="/section2">Section 2</a></li>
    </ul>
  </nav>
</div>
```

### Context

The Side Navigation component is a key structural element in MDWDS page layouts, typically paired with main content areas and headers to create complete page templates. It composes with typography and link styles from the Foundation system while maintaining consistent interaction patterns with other navigation components like breadcrumbs and top navigation.

---

## Side Navigation

*Components*

Side Navigation is a vertical menu component that displays a hierarchical list of navigation links, typically positioned on the left side of a page. It helps users understand the structure of a website and navigate between related pages and sections. Use it for organizing content in multi-page applications, documentation sites, or complex information hierarchies.

### Key Information

## Variants
- **Default/Simple**: Flat list of navigation items
- **Nested/Hierarchical**: Multi-level navigation with expandable sections
- **With Icons**: Navigation items can include icon accompaniment
- **Active State**: Current page or section is highlighted
- **Collapsed State**: Side navigation can collapse to show only icons (responsive behavior)

## CSS Class Names
- `.usa-sidenav`: Main wrapper container
- `.usa-sidenav__list`: List container for navigation items
- `.usa-sidenav__item`: Individual navigation item
- `.usa-sidenav__link`: Navigation link element
- `.usa-current`: Marks the currently active link
- `.usa-sidenav__sublist`: Nested list for multi-level navigation
- `.usa-sidenav__subnav`: Container for nested navigation items

## Modifiers & Options
- **Aria-current="page"**: Applied to the active link to indicate current page
- **aria-expanded**: Used on parent items to indicate if submenu is open/closed
- **aria-controls**: Links toggle buttons to submenu sections
- **aria-label**: Provides accessible label for navigation sections

## Important Facts
- Semantic HTML structure with proper list elements
- Full keyboard navigation support
- Screen reader friendly with proper ARIA landmarks
- Responsive behavior (may collapse on mobile)
- Customizable with CSS for styling and spacing

### Implementation

```html
<!-- Basic Side Navigation -->
<nav class="usa-sidenav" aria-label="Side navigation">
  <ul class="usa-sidenav__list">
    <li class="usa-sidenav__item">
      <a href="#" class="usa-sidenav__link usa-current" aria-current="page">
        Current Page
      </a>
    </li>
    <li class="usa-sidenav__item">
      <a href="#" class="usa-sidenav__link">
        Other Page
      </a>
    </li>
    <li class="usa-sidenav__item">
      <a href="#" class="usa-sidenav__link">
        Another Page
      </a>
    </li>
  </ul>
</nav>
```

```html
<!-- Side Navigation with Nested Items -->
<nav class="usa-sidenav" aria-label="Side navigation">
  <ul class="usa-sidenav__list">
    <li class="usa-sidenav__item">
      <a href="#" class="usa-sidenav__link usa-current" aria-current="page">
        Parent Link
      </a>
      <ul class="usa-sidenav__sublist">
        <li class="usa-sidenav__item">
          <a href="#" class="usa-sidenav__link">
            Child Link 1
          </a>
        </li>
        <li class="usa-sidenav__item">
          <a href="#" class="usa-sidenav__link">
            Child Link 2
          </a>
        </li>
      </ul>
    </li>
    <li class="usa-sidenav__item">
      <a href="#" class="usa-sidenav__link">
        Sibling Link
      </a>
    </li>
  </ul>
</nav>
```

```html
<!-- Side Navigation with Expandable Sections -->
<nav class="usa-sidenav" aria-label="Side navigation">
  <ul class="usa-sidenav__list">
    <li class="usa-sidenav__item">
      <button class="usa-sidenav__link" 
              aria-expanded="false" 
              aria-controls="submenu-1">
        Expandable Section
      </button>
      <ul class="usa-sidenav__sublist" id="submenu-1" hidden>
        <li class="usa-sidenav__item">
          <a href="#" class="usa-sidenav__link">
            Nested Item
          </a>
        </li>
      </ul>
    </li>
  </ul>
</nav>
```

### Context

Side Navigation is a core USWDS component adapted for Maryland's design system and complements other navigation patterns like the top banner navigation. It works in conjunction with main content areas to provide consistent, accessible page structure across Maryland state websites.

---

## Site Alert

*Components*

The Site Alert component displays important, high-priority messages that span the full width of a page to notify users of critical information, emergency updates, or system status changes. It should be used when you need to communicate information that requires immediate user attention before they interact with page content.

### Key Information

## Variants and Types
- **Alert (Default)**: Standard informational alert
- **Success**: Communicates successful completion of actions
- **Warning**: Highlights cautionary information requiring user attention
- **Error**: Indicates problems, failures, or critical issues

## CSS Classes
- `.usa-alert`: Main container class
- `.usa-alert--success`: Success variant modifier
- `.usa-alert--warning`: Warning variant modifier
- `.usa-alert--error`: Error/emergency variant modifier
- `.usa-alert--info`: Information variant (default)
- `.usa-alert__heading`: For the alert title/heading
- `.usa-alert__body`: Container for alert content and text

## ARIA Attributes
- `role="region"`: Identifies the element as a landmark region
- `aria-live="polite"`: Announces alert updates to screen readers
- `aria-label`: Describes the alert purpose/type

## Important Facts
- Site alerts are typically placed at the top of the page, above main content
- Use semantic HTML with appropriate heading levels within the alert
- Each alert type uses distinct styling for visual differentiation
- Alerts persist on the page and should not auto-dismiss for critical information
- Use with appropriate icon or visual indicator matching the alert type

### Implementation

```html
<!-- Default/Info Alert -->
<div class="usa-alert usa-alert--info" role="region" aria-live="polite">
  <div class="usa-alert__heading">
    <h4>Informational heading</h4>
  </div>
  <div class="usa-alert__body">
    <p>This is an informational alert.</p>
  </div>
</div>

<!-- Success Alert -->
<div class="usa-alert usa-alert--success" role="region" aria-live="polite">
  <div class="usa-alert__heading">
    <h4>Success heading</h4>
  </div>
  <div class="usa-alert__body">
    <p>This is a success alert.</p>
  </div>
</div>

<!-- Warning Alert -->
<div class="usa-alert usa-alert--warning" role="region" aria-live="polite">
  <div class="usa-alert__heading">
    <h4>Warning heading</h4>
  </div>
  <div class="usa-alert__body">
    <p>This is a warning alert.</p>
  </div>
</div>

<!-- Error/Emergency Alert -->
<div class="usa-alert usa-alert--error" role="region" aria-live="polite">
  <div class="usa-alert__heading">
    <h4>Emergency heading</h4>
  </div>
  <div class="usa-alert__body">
    <p>This is an error or emergency alert.</p>
  </div>
</div>
```

### Context

The Site Alert component is a USWDS-based component in the MDWDS that provides a standardized way to communicate critical information to users. It integrates with other page layout components and should typically appear as a top-level page element before main content sections.

---

## Social Media

*Components*

The Social Media component provides a collection of styled links and icons for major social media platforms including Facebook, Twitter, Instagram, LinkedIn, YouTube, and others. It enables state websites to maintain consistent, accessible social media presence across Maryland government web properties. Use this component in footers or dedicated social media sections to connect users with official state social channels.

### Key Information

The Social Media component includes pre-styled icon links for common social platforms:
- Facebook
- Twitter/X
- Instagram
- LinkedIn
- YouTube
- TikTok
- Pinterest
- Nextdoor
- GovDelivery

Key features:
- Accessible icon-based links with proper ARIA labels
- Consistent styling and sizing across all social platforms
- Hover states for interactive feedback
- Mobile-responsive layout
- Color styling aligned with platform branding or MDWDS color palette
- Optional text labels alongside icons
- Can be arranged horizontally or vertically

CSS classes typically include: `social-media`, `social-icon`, `social-link`

The component supports both icon-only and icon-with-text variants for flexibility in layout and space constraints.

### Implementation

```html
<!-- Icon-only variant -->
<div class="social-media">
  <a href="https://www.facebook.com/Maryland" class="social-link" aria-label="Maryland on Facebook">
    <span class="social-icon icon-facebook"></span>
  </a>
  <a href="https://www.twitter.com/Maryland" class="social-link" aria-label="Maryland on Twitter">
    <span class="social-icon icon-twitter"></span>
  </a>
  <a href="https://www.instagram.com/Maryland" class="social-link" aria-label="Maryland on Instagram">
    <span class="social-icon icon-instagram"></span>
  </a>
  <a href="https://www.youtube.com/Maryland" class="social-link" aria-label="Maryland on YouTube">
    <span class="social-icon icon-youtube"></span>
  </a>
</div>
```

```html
<!-- Icon with text variant -->
<div class="social-media social-media--with-text">
  <a href="https://www.facebook.com/Maryland" class="social-link">
    <span class="social-icon icon-facebook"></span>
    <span class="social-text">Facebook</span>
  </a>
  <a href="https://www.twitter.com/Maryland" class="social-link">
    <span class="social-icon icon-twitter"></span>
    <span class="social-text">Twitter</span>
  </a>
</div>
```

```html
<!-- Vertical layout variant -->
<div class="social-media social-media--vertical">
  <a href="https://www.facebook.com/Maryland" class="social-link" aria-label="Maryland on Facebook">
    <span class="social-icon icon-facebook"></span>
  </a>
  <a href="https://www.twitter.com/Maryland" class="social-link" aria-label="Maryland on Twitter">
    <span class="social-icon icon-twitter"></span>
  </a>
</div>
```

### Context

The Social Media component integrates with MDWDS foundation styles and color system to maintain visual consistency across Maryland government websites. It is commonly paired with Footer components and can be included in page layouts, sidebars, or dedicated contact/connection sections to help citizens engage with state agencies across social platforms.

---

## Statewide Banner

*Components*

The Statewide Banner is a consistent header component that appears at the top of Maryland state web pages to establish state identity and provide quick access to state services. It serves as a unifying element across all state digital properties and improves wayfinding for users navigating between state resources.

### Key Information

The Statewide Banner includes:
- State seal or logo identification
- Text identifying the site as part of state government
- Consistent branding across all state web properties
- Optional navigation or link elements
- Responsive design that adapts to mobile and desktop viewports

Key features:
- Appears at the very top of the page above main navigation
- Uses official Maryland state branding and colors
- Provides accessibility features for navigation
- Acts as an identity marker for state digital presence

### Implementation

```html
<!-- Statewide Banner Structure -->
<div class="mdwds-statewide-banner">
  <div class="mdwds-statewide-banner__container">
    <a href="https://maryland.gov" class="mdwds-statewide-banner__link">
      <span class="mdwds-statewide-banner__seal"></span>
      <span class="mdwds-statewide-banner__text">An official website of the State of Maryland</span>
    </a>
  </div>
</div>
```

Key class names:
- `.mdwds-statewide-banner` - Main container
- `.mdwds-statewide-banner__container` - Inner wrapper for content
- `.mdwds-statewide-banner__link` - Clickable link to state homepage
- `.mdwds-statewide-banner__seal` - State seal/logo element
- `.mdwds-statewide-banner__text` - Descriptive text

### Context

The Statewide Banner is a foundational component required at the top of all Maryland state web pages. It works in conjunction with main site headers and navigation to establish clear state government identity and should appear before any agency-specific branding or navigation elements.

---

## Statewide Footer

*Components*

The Statewide Footer is a standardized footer component that appears at the bottom of Maryland state web pages. It provides consistent branding, navigation, contact information, and compliance messaging across all state websites. This component ensures a unified user experience and reinforces Maryland state identity throughout the web presence.

### Key Information


**Variants & Structure:**
- Full statewide footer with all sections (header, navigation, contact information, links, compliance)
- Collapsible sections for responsive mobile displays
- Optional agency-specific customization areas

**CSS Classes:**
- `.mdwds-footer` - Main footer container
- `.footer-section` - Individual section containers
- `.footer-header` - Footer header area
- `.footer-nav` - Navigation area
- `.footer-contact` - Contact information section
- `.footer-compliance` - Compliance and legal messaging section

**Required Elements:**
- Maryland state seal/branding
- Agency name and contact information
- Required compliance links (Accessibility, Privacy, Terms of Use)
- Copyright and attribution information

**Key Features:**
- Responsive design that adapts to mobile, tablet, and desktop viewports
- Accessible navigation with proper ARIA labels and semantic HTML
- Customizable link sections for agency-specific navigation
- Dark background with high-contrast text for accessibility compliance
- Optional sticky/fixed positioning support

**Important Attributes:**
- `role="contentinfo"` on main footer element
- Proper heading hierarchy within footer sections
- Alt text for logo/seal images
- ARIA labels for navigation landmarks


### Implementation


```html
<footer class="mdwds-footer" role="contentinfo">
  <div class="footer-container">
    <!-- Footer Header Section -->
    <div class="footer-section footer-header">
      <div class="footer-branding">
        <img src="/images/maryland-seal.svg" alt="State of Maryland" class="state-seal" />
        <div class="agency-info">
          <h2>Agency Name</h2>
          <p>Brief agency description</p>
        </div>
      </div>
    </div>

    <!-- Footer Navigation Section -->
    <nav class="footer-section footer-nav" aria-label="Footer Navigation">
      <div class="footer-nav-column">
        <h3>Section One</h3>
        <ul>
          <li><a href="#">Link One</a></li>
          <li><a href="#">Link Two</a></li>
          <li><a href="#">Link Three</a></li>
        </ul>
      </div>
      <div class="footer-nav-column">
        <h3>Section Two</h3>
        <ul>
          <li><a href="#">Link One</a></li>
          <li><a href="#">Link Two</a></li>
          <li><a href="#">Link Three</a></li>
        </ul>
      </div>
    </nav>

    <!-- Contact Information Section -->
    <div class="footer-section footer-contact">
      <h3>Contact Us</h3>
      <p>Phone: <a href="tel:+14105000000">410-500-0000</a></p>
      <p>Email: <a href="mailto:info@maryland.gov">info@maryland.gov</a></p>
      <p>Address: Maryland Department<br />123 Main Street<br />Baltimore, MD 21201</p>
    </div>

    <!-- Compliance & Legal Section -->
    <div class="footer-section footer-compliance">
      <ul>
        <li><a href="#">Accessibility</a></li>
        <li><a href="#">Privacy Policy</a></li>
        <li><a href="#">Terms of Use</a></li>
        <li><a href="#">Security</a></li>
      </ul>
      <p class="copyright">&copy; 2024 State of Maryland. All rights reserved.</p>
    </div>
  </div>
</footer>
```

**Mobile Responsive Variant:**
```html
<footer class="mdwds-footer mdwds-footer--mobile" role="contentinfo">
  <div class="footer-container">
    <!-- Mobile version may collapse sections into accordion -->
    <div class="footer-section footer-header">
      <img src="/images/maryland-seal.svg" alt="State of Maryland" class="state-seal" />
      <h2>Agency Name</h2>
    </div>
    
    <nav class="footer-section footer-nav" aria-label="Footer Navigation">
      <button class="footer-accordion-toggle" aria-expanded="false" aria-controls="footer-nav-content">
        Navigation <span class="icon">+</span>
      </button>
      <div id="footer-nav-content" class="footer-nav-content" hidden>
        <!-- Navigation links -->
      </div>
    </nav>
  </div>
</footer>
```


### Context

The Statewide Footer is a required component in the MDWDS that provides consistent footer styling and structure across all Maryland state web pages. It works in conjunction with the Header component to create complete page framing and includes composable sections for navigation, contact, and compliance information specific to each agency's needs.

---

## Statistic List

*Components*

The Statistic List component displays a collection of key statistics or metrics in an organized, visually prominent format. It's designed to showcase important numerical data, achievements, or performance indicators on Maryland state web pages. Use this component when you need to highlight multiple related statistics or key performance metrics prominently.

### Key Information

## Variants and Structure
- **Basic Statistic Item**: Displays a number/value with an accompanying label or description
- **Optional Icon/Image Support**: May include visual indicators alongside statistics
- **Responsive Layout**: Typically arranged in a grid that adapts to screen size (2-4 columns on desktop, single column on mobile)

## Key Class Names and Modifiers
- `.statistic-list` - Main container class for the component
- `.statistic-item` - Individual statistic wrapper
- `.statistic-value` - The primary numerical or data value
- `.statistic-label` - Descriptive text accompanying the value

## Important Facts
- Each statistic item should clearly separate the value from its label
- Statistics should be kept concise and scannable
- Consider grouping related statistics together
- Ensure sufficient contrast between text and background for accessibility
- The component supports flexible grid layouts based on available space

### Implementation

```html
<div class="statistic-list">
  <div class="statistic-item">
    <div class="statistic-value">2,547</div>
    <div class="statistic-label">Active Users</div>
  </div>
  <div class="statistic-item">
    <div class="statistic-value">98%</div>
    <div class="statistic-label">Satisfaction Rate</div>
  </div>
  <div class="statistic-item">
    <div class="statistic-value">156</div>
    <div class="statistic-label">Services Available</div>
  </div>
  <div class="statistic-item">
    <div class="statistic-value">24/7</div>
    <div class="statistic-label">Support Available</div>
  </div>
</div>
```

## With Icons or Visual Elements
```html
<div class="statistic-list">
  <div class="statistic-item">
    <div class="statistic-icon">
      <svg><!-- icon content --></svg>
    </div>
    <div class="statistic-value">2,547</div>
    <div class="statistic-label">Active Users</div>
  </div>
</div>
```

### Context

The Statistic List component is a foundational data visualization element within MDWDS that helps present numerical information at a glance. It often pairs with Hero sections, Overview cards, or Summary sections to communicate key performance indicators or service metrics on Maryland state agency websites.

---

## Step Indicator

*Components*

The Step Indicator is a visual component that displays progress through a multi-step process or workflow. It shows users where they are in a sequence of steps and helps them understand the overall progress and structure of a form, wizard, or process. Use this to guide users through complex, multi-step interactions and set clear expectations about the journey ahead.

### Key Information

## Variants & Options

- **Step states**: Completed, current/active, not started
- **Display styles**: Can show step labels and descriptions
- **Orientation**: Typically horizontal layout for step progression

## CSS Classes & Structure

- `.usa-step-indicator`: Main container for the step indicator
- `.usa-step-indicator__list`: Container for step items
- `.usa-step-indicator__item`: Individual step item wrapper
- `.usa-step-indicator__segment`: The visual segment/circle representing the step
- `.usa-step-indicator__label`: Text label for the step
- Completed steps: Apply `.usa-step-indicator__segment--complete` or relevant state class
- Current step: Apply `.usa-step-indicator__segment--current` or active state class

## ARIA Attributes & Accessibility

- Use `role="list"` on step container
- Use `role="listitem"` on individual steps
- Each step should have `aria-current="step"` when it is the active step
- Use `aria-label` or `aria-labelledby` to provide context for screen readers

## Important Notes

- Step indicators are primarily visual and should be paired with descriptive form labels
- Completed steps should be clearly distinguishable (color, icon, styling)
- Current/active step should have focus-visible styling for keyboard navigation
- Step content should be properly associated with step indicators

### Implementation

```html
<ol class="usa-step-indicator" aria-label="Progress">
  <li class="usa-step-indicator__item usa-step-indicator__item--complete">
    <span class="usa-step-indicator__segment">
      <span class="usa-step-indicator__label">Step 1</span>
    </span>
  </li>
  <li class="usa-step-indicator__item usa-step-indicator__item--current">
    <span class="usa-step-indicator__segment" aria-current="step">
      <span class="usa-step-indicator__label">Step 2</span>
    </span>
  </li>
  <li class="usa-step-indicator__item">
    <span class="usa-step-indicator__segment">
      <span class="usa-step-indicator__label">Step 3</span>
    </span>
  </li>
</ol>
```

## With Descriptions

```html
<ol class="usa-step-indicator" aria-label="Progress">
  <li class="usa-step-indicator__item usa-step-indicator__item--complete">
    <div class="usa-step-indicator__segment">
      <span class="usa-step-indicator__label">Personal Information</span>
      <span class="usa-step-indicator__sub-label">Complete</span>
    </div>
  </li>
  <li class="usa-step-indicator__item usa-step-indicator__item--current">
    <div class="usa-step-indicator__segment" aria-current="step">
      <span class="usa-step-indicator__label">Address</span>
      <span class="usa-step-indicator__sub-label">In Progress</span>
    </div>
  </li>
  <li class="usa-step-indicator__item">
    <div class="usa-step-indicator__segment">
      <span class="usa-step-indicator__label">Review</span>
      <span class="usa-step-indicator__sub-label">Not Started</span>
    </div>
  </li>
</ol>
```

### Context

The Step Indicator is a USWDS component adopted into MDWDS for consistent multi-step form and workflow implementations across Maryland state applications. It works alongside Form components and can be paired with Buttons for step navigation to create complete wizard experiences.

---

## Step List

*Components*

A Step List is a sequential navigation component that displays a numbered progression of steps, helping users understand their current position within a multi-step process or workflow. It provides visual clarity about completion status and remaining tasks, improving user orientation in complex tasks like forms, wizards, or procedural guides. Use it when guiding users through ordered processes where understanding progress is critical to the experience.

### Key Information

## Variants and Modifiers

- **Step States**: Active, Completed, Pending (future), Disabled
- **Visual Indicators**: Step number, status icon, title, and optional description text
- **Connector Lines**: Visual lines connecting steps to show progression flow
- **Responsive**: Adapts from vertical layout on mobile to horizontal or vertical on larger screens

## CSS Classes and Structure

- `.step-list` - Main container for the step component
- `.step-item` - Individual step within the list
- `.step-item--active` - Modifier for the currently active step
- `.step-item--completed` - Modifier for completed steps
- `.step-item--pending` - Modifier for future/pending steps
- `.step-item--disabled` - Modifier for disabled steps
- `.step-number` - Container for the step number or icon
- `.step-label` - Container for step title/heading
- `.step-description` - Optional description text for the step

## ARIA Attributes

- `role="list"` - Applied to the main step list container
- `role="listitem"` - Applied to each step item
- `aria-current="step"` - Marks the currently active step
- `aria-disabled="true"` - Applied to disabled steps
- `aria-label` - Descriptive labels for each step

## Important Implementation Notes

- Include clear visual distinction between step states
- Maintain proper tab order for keyboard navigation
- Connector lines should be semantic (SVG or CSS-based, not images)
- Step numbers or icons should be distinguishable at all viewport sizes
- Descriptions are optional but improve clarity for complex workflows

### Implementation

```html
<!-- Basic Step List Structure -->
<ol class="step-list" role="list">
  <li class="step-item step-item--completed" role="listitem">
    <div class="step-number">
      <span class="step-icon">✓</span>
    </div>
    <div class="step-label">Step 1: Personal Information</div>
    <div class="step-description">Enter your basic details</div>
  </li>
  
  <li class="step-item step-item--active" role="listitem" aria-current="step">
    <div class="step-number">
      <span class="step-count">2</span>
    </div>
    <div class="step-label">Step 2: Address</div>
    <div class="step-description">Provide your mailing address</div>
  </li>
  
  <li class="step-item step-item--pending" role="listitem">
    <div class="step-number">
      <span class="step-count">3</span>
    </div>
    <div class="step-label">Step 3: Review & Confirm</div>
    <div class="step-description">Review and submit your information</div>
  </li>
  
  <li class="step-item step-item--disabled" role="listitem" aria-disabled="true">
    <div class="step-number">
      <span class="step-count">4</span>
    </div>
    <div class="step-label">Step 4: Payment</div>
    <div class="step-description">Complete payment processing</div>
  </li>
</ol>
```

```html
<!-- Step List Without Descriptions -->
<ol class="step-list" role="list">
  <li class="step-item step-item--completed" role="listitem">
    <div class="step-number">✓</div>
    <div class="step-label">Documents Uploaded</div>
  </li>
  
  <li class="step-item step-item--active" role="listitem" aria-current="step">
    <div class="step-number">2</div>
    <div class="step-label">Under Review</div>
  </li>
  
  <li class="step-item step-item--pending" role="listitem">
    <div class="step-number">3</div>
    <div class="step-label">Approval Notification</div>
  </li>
</ol>
```

```html
<!-- Vertical Layout Variant -->
<ol class="step-list step-list--vertical" role="list">
  <li class="step-item step-item--completed" role="listitem">
    <div class="step-number">✓</div>
    <div class="step-content">
      <div class="step-label">Step 1</div>
      <div class="step-description">Completed step</div>
    </div>
  </li>
  
  <li class="step-item step-item--active" role="listitem" aria-current="step">
    <div class="step-number">2</div>
    <div class="step-content">
      <div class="step-label">Step 2</div>
      <div class="step-description">Currently active</div>
    </div>
  </li>
</ol>
```

### Context

The Step List is a key component for Maryland's government workflow and form processes, commonly paired with form components and buttons. It helps users navigate complex multi-step procedures and integrates with the broader MDWDS component library to create cohesive, accessible digital experiences aligned with USWDS patterns.

---

## Summary Box

*Components*

The Summary Box is a container component used to highlight and present key information or summaries prominently on a page. It draws attention to important content and helps users quickly scan for critical details or takeaways.

### Key Information

- **Purpose**: Highlights important summary information, callouts, or key takeaways
- **Class Names**: `.summary-box` for the main container
- **Variants**: May support different styles (informational, warning, success, etc.) through modifier classes
- **Required Elements**: Container div with appropriate class names, content inside
- **Accessibility**: Should use semantic HTML and appropriate ARIA roles if interactive
- **Modifiers**: Likely supports variants for different visual states or importance levels
- **Content**: Can contain text, lists, or other content types depending on use case

### Implementation

```html
<!-- Basic Summary Box -->
<div class="summary-box">
  <p>This is important summary information that users should see.</p>
</div>

<!-- Summary Box with heading -->
<div class="summary-box">
  <h3>Summary Title</h3>
  <p>Key information goes here.</p>
</div>

<!-- Summary Box with list -->
<div class="summary-box">
  <h3>Key Points</h3>
  <ul>
    <li>Point one</li>
    <li>Point two</li>
    <li>Point three</li>
  </ul>
</div>
```

### Context

The Summary Box is a basic content container component in the MDWDS used to organize and emphasize key information within page layouts. It works alongside other content components to create visual hierarchy and improve scannability.

---

## Summary Box

*Components*

The Summary Box is a USWDS component used to highlight key information or callouts on a page in a visually distinct container. It draws attention to important content and helps organize information hierarchy, commonly used for alerts, important notices, or highlighted information sections.

### Key Information

The Summary Box component uses the USWDS classes and structure. Key variants and modifiers include:

- **Base class**: `.usa-summary-box`
- **Content wrapper**: `.usa-summary-box__body`
- **Heading class**: `.usa-summary-box__heading`
- **Text/paragraph class**: `.usa-summary-box__text`

Common modifier patterns:
- Can contain headings, paragraphs, and lists
- Typically uses semantic heading tags (h2, h3, etc.)
- May include background color styling variants
- Works with standard USWDS spacing utilities

The component is a USWDS implementation and follows Maryland's adaptation of the U.S. Web Design System.

### Implementation

```html
<div class="usa-summary-box">
  <div class="usa-summary-box__body">
    <h3 class="usa-summary-box__heading">Summary Box Title</h3>
    <p class="usa-summary-box__text">
      This is the summary box content. It can contain text, lists, or other content elements.
    </p>
  </div>
</div>
```

Variant with list content:
```html
<div class="usa-summary-box">
  <div class="usa-summary-box__body">
    <h3 class="usa-summary-box__heading">Key Points</h3>
    <ul class="usa-summary-box__text">
      <li>Point one</li>
      <li>Point two</li>
      <li>Point three</li>
    </ul>
  </div>
</div>
```

### Context

The Summary Box is a core USWDS component adopted by Maryland's design system for highlighting important information sections. It integrates with other content components and follows the same design standards used across the MDWDS component library.

---

## Table

*Components*

A Table component for displaying structured data in rows and columns. Tables organize and present information in a grid format, making it easy for users to scan, compare, and understand related data. Use tables when you need to display large datasets, comparisons, or information that benefits from a columnar layout.

### Key Information

## Variants
- Basic table with standard rows and columns
- Striped rows for improved readability
- Bordered table with visible cell borders
- Responsive table (stackable on mobile)
- Sortable columns
- Selectable rows with checkboxes

## CSS Classes
- `.table` - Base table class
- `.table-striped` - Alternating row colors
- `.table-bordered` - Visible borders on all cells
- `.table-hover` - Highlight row on hover
- `.table-sm` - Compact/small table
- `.table-responsive` - Wraps table for responsive behavior

## Structure
- `<table>` - Root element
- `<thead>` - Table header section
- `<tbody>` - Table body section
- `<tfoot>` - Optional footer section
- `<tr>` - Table row
- `<th>` - Table header cell (scope attribute recommended)
- `<td>` - Table data cell

## ARIA & Accessibility
- Use `scope="col"` on header cells to associate with columns
- Use `scope="row"` on row header cells if applicable
- Add `role="table"` if not using semantic table element
- Use `aria-label` or `aria-labelledby` to provide table title/description
- For sortable tables, use `aria-sort="ascending|descending|none"` on sortable headers

## Important Attributes
- `scope` - Defines header cell scope (col, row, colgroup, rowgroup)
- `colspan` - Number of columns a cell spans
- `rowspan` - Number of rows a cell spans

### Implementation

```html
<!-- Basic Table -->
<table class="table">
  <thead>
    <tr>
      <th scope="col">Column 1</th>
      <th scope="col">Column 2</th>
      <th scope="col">Column 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data 1</td>
      <td>Data 2</td>
      <td>Data 3</td>
    </tr>
    <tr>
      <td>Data 1</td>
      <td>Data 2</td>
      <td>Data 3</td>
    </tr>
  </tbody>
</table>

<!-- Striped Table -->
<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Header</th>
      <th scope="col">Header</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data</td>
      <td>Data</td>
    </tr>
  </tbody>
</table>

<!-- Bordered Table -->
<table class="table table-bordered">
  <thead>
    <tr>
      <th scope="col">Header</th>
      <th scope="col">Header</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data</td>
      <td>Data</td>
    </tr>
  </tbody>
</table>

<!-- Responsive Table Wrapper -->
<div class="table-responsive">
  <table class="table table-striped">
    <thead>
      <tr>
        <th scope="col">Header 1</th>
        <th scope="col">Header 2</th>
        <th scope="col">Header 3</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Data</td>
        <td>Data</td>
        <td>Data</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- Small/Compact Table -->
<table class="table table-sm">
  <thead>
    <tr>
      <th scope="col">Header</th>
      <th scope="col">Header</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data</td>
      <td>Data</td>
    </tr>
  </tbody>
</table>
```

### Context

The Table component is a foundational data display element within MDWDS that works with other components like pagination, filters, and buttons for complete data presentation. Tables follow Maryland's accessibility standards and responsive design principles to ensure data is readable across all devices.

---

## Table

*Components*

Tables are used to organize and display structured data in rows and columns. They help users scan, compare, and understand complex information at a glance. Use tables when you need to present organized data that benefits from a grid layout, especially for financial, statistical, or comparative information.

### Key Information

## Variants and Options

- **Standard Table**: Basic table with headers and data rows
- **Sortable Table**: Allows users to sort columns by clicking headers
- **Scrollable Table**: Responsive horizontal scrolling on small screens
- **Striped Rows**: Alternating row colors for easier reading
- **Bordered Table**: Visible borders around cells and rows

## CSS Classes

- `usa-table`: Base table class
- `usa-table--striped`: Adds alternating row background colors
- `usa-table--bordered`: Adds visible borders
- `usa-table--compact`: Reduces padding for denser data
- `usa-table--scrollable`: Enables horizontal scroll on mobile

## Key Attributes

- `<table>`: Main container
- `<thead>`: Table header section
- `<tbody>`: Table body with data rows
- `<tr>`: Table row
- `<th>`: Table header cell (use `scope="col"` for column headers, `scope="row"` for row headers)
- `<td>`: Table data cell

## Accessibility Requirements

- Always include `<thead>` and `<tbody>` for proper semantic structure
- Use `scope` attribute on `<th>` to associate headers with data
- Use `caption` element or `aria-label` for table title/description
- Ensure sufficient color contrast for text and borders
- Make sortable headers keyboard accessible with proper ARIA attributes

### Implementation

## Basic Table

```html
<table class="usa-table">
  <thead>
    <tr>
      <th scope="col">Header 1</th>
      <th scope="col">Header 2</th>
      <th scope="col">Header 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data 1</td>
      <td>Data 2</td>
      <td>Data 3</td>
    </tr>
    <tr>
      <td>Data 4</td>
      <td>Data 5</td>
      <td>Data 6</td>
    </tr>
  </tbody>
</table>
```

## Striped Table

```html
<table class="usa-table usa-table--striped">
  <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Item 1</td>
      <td>100</td>
    </tr>
    <tr>
      <td>Item 2</td>
      <td>200</td>
    </tr>
  </tbody>
</table>
```

## Bordered and Scrollable Table

```html
<table class="usa-table usa-table--bordered usa-table--scrollable">
  <caption>Sales Data by Region</caption>
  <thead>
    <tr>
      <th scope="col">Region</th>
      <th scope="col">Q1</th>
      <th scope="col">Q2</th>
      <th scope="col">Q3</th>
      <th scope="col">Q4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">North</th>
      <td>45,000</td>
      <td>52,000</td>
      <td>48,000</td>
      <td>61,000</td>
    </tr>
    <tr>
      <th scope="row">South</th>
      <td>38,000</td>
      <td>41,000</td>
      <td>44,000</td>
      <td>49,000</td>
    </tr>
  </tbody>
</table>
```

### Context

Tables are a core component in the MDWDS that follows USWDS design patterns for presenting tabular data on Maryland state websites. They work alongside Typography and Color Foundation components to ensure readable, accessible data presentation across government services.

---

## Tag

*Components*

A Tag component is a compact, labeled element used to mark or categorize content with short text labels. Tags help users quickly identify and filter information, making them useful for displaying metadata, statuses, keywords, or categories in a visible and scannable way.

### Key Information

Tags are typically used to:
- Display metadata or keywords associated with content
- Show status indicators or categorization labels
- Filter or organize items by tag
- Mark items with brief descriptive text

**CSS Class Names:**
- `.usa-tag` — Base tag component class
- `.usa-tag--outline` — Outline variant (light background with border)

**Modifiers & Variants:**
- Basic tag with text label
- Outline/secondary style for less prominent tags
- Single-line text display

**Required Attributes:**
- Text content should be concise and scannable
- Typically not interactive (links may be wrapped around tags for navigation)
- Accessible text alternatives if used with icons or graphics

**Important Facts:**
- Tags are read-only display elements (not form inputs)
- Should use short, descriptive labels (1-3 words recommended)
- Support semantic HTML with `<span>` or `<div>` elements
- Can be grouped or repeated for multiple categorizations

### Implementation

```html
<!-- Basic Tag -->
<span class="usa-tag">Label</span>

<!-- Outline/Secondary Tag -->
<span class="usa-tag usa-tag--outline">Label</span>

<!-- Multiple Tags -->
<div>
  <span class="usa-tag">Category A</span>
  <span class="usa-tag">Category B</span>
  <span class="usa-tag usa-tag--outline">Category C</span>
</div>

<!-- Tag with Custom Content -->
<span class="usa-tag">
  New
</span>
```

### Context

Tags are a fundamental USWDS component used throughout Maryland state web pages for marking, categorizing, and filtering content. They compose well with card components, lists, and search/filter interfaces to enhance content discoverability and organization.

---

## Textarea

*Components*

A textarea component is a multi-line text input field that allows users to enter and edit longer text content. It's used in forms where extended text input is required, such as comments, descriptions, or feedback sections. Use textarea when you need to collect multiple lines of text from users.

### Key Information

## Variants & Options
- **Standard textarea**: Basic multi-line input field
- **Disabled state**: Set `disabled` attribute to prevent user input
- **Read-only state**: Set `readonly` attribute for non-editable content
- **With label**: Always pair with a `<label>` element using `for` attribute
- **With help text**: Optional helper text below the field for guidance
- **With error state**: Shows validation error messages
- **Character count**: Optional character limit display

## CSS Class Names
- `usa-textarea`: Main textarea class
- `usa-input__block`: Block-level styling
- `usa-form-group`: Wrapper for form field and associated elements
- `usa-hint`: Class for help text elements

## Required Attributes
- `id`: Unique identifier for the textarea
- `name`: Form field name
- `aria-label` or associated `<label>`: Accessible name required

## Important Facts
- Based on USWDS textarea component standards
- Supports accessibility standards (WCAG 2.1)
- Should always have an associated label element
- Can include min/max row attributes for size control
- Supports placeholder text for guidance

### Implementation

## Basic Textarea
```html
<div class="usa-form-group">
  <label class="usa-label" for="textarea-input">Textarea Label</label>
  <textarea class="usa-textarea" id="textarea-input" name="textarea-input"></textarea>
</div>
```

## Textarea with Help Text
```html
<div class="usa-form-group">
  <label class="usa-label" for="textarea-help">Textarea with Help Text</label>
  <span class="usa-hint" id="textarea-help-text">This is help text</span>
  <textarea class="usa-textarea" id="textarea-help" name="textarea-help" aria-describedby="textarea-help-text"></textarea>
</div>
```

## Disabled Textarea
```html
<div class="usa-form-group">
  <label class="usa-label" for="textarea-disabled">Disabled Textarea</label>
  <textarea class="usa-textarea" id="textarea-disabled" name="textarea-disabled" disabled></textarea>
</div>
```

## Textarea with Error
```html
<div class="usa-form-group usa-form-group--error">
  <label class="usa-label" for="textarea-error">Textarea with Error</label>
  <span class="usa-error-message" id="textarea-error-message">This field is required</span>
  <textarea class="usa-textarea" id="textarea-error" name="textarea-error" aria-describedby="textarea-error-message"></textarea>
</div>
```

## Textarea with Rows Attribute
```html
<div class="usa-form-group">
  <label class="usa-label" for="textarea-rows">Textarea with Rows</label>
  <textarea class="usa-textarea" id="textarea-rows" name="textarea-rows" rows="10"></textarea>
</div>
```

### Context

The textarea component is part of the USWDS integration within MDWDS and provides a standardized multi-line text input for Maryland state web forms. It follows the same accessibility and styling patterns as other MDWDS form components like text inputs and select fields, ensuring consistency across state web applications.

---

## Time Picker

*Components*

The Time Picker component enables users to select a specific time through an accessible interface. It provides an alternative to typing time values manually, reducing input errors and improving user experience. Use this component in forms, scheduling interfaces, or any application requiring time selection.

### Key Information

## Variants and Options

- **Time Format**: Supports 12-hour and 24-hour time formats
- **Granularity**: Configurable time increments (typically 15-minute, 30-minute, or hourly intervals)
- **Initial Value**: Can be pre-populated with a default time

## Key Attributes

- `type="time"` - HTML5 time input attribute
- `aria-label` - Descriptive label for screen readers
- `required` - Mark field as mandatory when needed
- `min` and `max` - Set time boundaries for valid selections
- `step` - Define the increment interval (in seconds)

## CSS Classes

- `.usa-time-picker` - Main container class
- `.usa-input` - Applied to the input field for consistent styling
- `.usa-form-group` - Wrapper for form field grouping

## Important Facts

- Built on USWDS (U.S. Web Design System) patterns
- Fully keyboard accessible with arrow key navigation
- Screen reader compatible with proper ARIA labeling
- Integrates with standard HTML5 time input elements

### Implementation

```html
<!-- Basic Time Picker -->
<div class="usa-form-group">
  <label class="usa-label" for="time-picker">Select a time</label>
  <input
    class="usa-input"
    id="time-picker"
    type="time"
    name="time"
    aria-label="Select a time"
  />
</div>

<!-- Time Picker with Constraints -->
<div class="usa-form-group">
  <label class="usa-label" for="time-picker-constrained">Appointment time (9 AM - 5 PM)</label>
  <input
    class="usa-input"
    id="time-picker-constrained"
    type="time"
    name="appointment-time"
    min="09:00"
    max="17:00"
    step="900"
    aria-label="Select an appointment time between 9 AM and 5 PM"
    required
  />
</div>

<!-- Time Picker with 24-hour Format -->
<div class="usa-form-group">
  <label class="usa-label" for="time-picker-24">Select time (24-hour format)</label>
  <input
    class="usa-input"
    id="time-picker-24"
    type="time"
    name="time-24"
    value="14:30"
    aria-label="Select time in 24-hour format"
  />
</div>
```

### Context

The Time Picker is a USWDS-based component that integrates into the Maryland Design System for consistent time input across state applications. It composes naturally with form components like labels and form groups, following MDWDS accessibility standards.

---

## Tooltip

*Components*

A Tooltip is a small popup element that displays additional information or context when a user hovers over or focuses on a UI element. It helps reduce visual clutter by revealing supplementary content only when needed, improving user experience by providing helpful hints, descriptions, or explanatory text without overwhelming the interface.

### Key Information

## Variants
- Default tooltip with hover activation
- Tooltip with focus activation (keyboard accessible)
- Positioning variants: top, bottom, left, right

## CSS Classes
- `.usa-tooltip` - main tooltip container
- `.usa-tooltip__trigger` - element that triggers the tooltip
- `.usa-tooltip__body` - tooltip content wrapper

## Key Attributes
- `aria-describedby` - links trigger to tooltip content
- `role="tooltip"` - semantic role for tooltip body
- `data-position` - controls tooltip placement (top, bottom, left, right)

## Important Notes
- Tooltips must be keyboard accessible with focus states
- Always include ARIA attributes for screen reader compatibility
- Use for brief, helpful content only (not critical information)
- Avoid tooltips on touch devices without fallback behavior
- JavaScript required for show/hide behavior

### Implementation

```html
<!-- Basic Tooltip Structure -->
<button class="usa-tooltip__trigger" aria-describedby="tooltip-1">
  Help
</button>

<div id="tooltip-1" class="usa-tooltip" role="tooltip" data-position="top">
  <div class="usa-tooltip__body">
    This is helpful information about this field
  </div>
</div>
```

```html
<!-- Tooltip with Icon Trigger -->
<span class="usa-tooltip__trigger" aria-describedby="tooltip-2" tabindex="0">
  <svg class="usa-icon" aria-hidden="true">
    <use xlink:href="/assets/img/sprite.svg#info"></use>
  </svg>
</span>

<div id="tooltip-2" class="usa-tooltip" role="tooltip" data-position="bottom">
  <div class="usa-tooltip__body">
    Additional context here
  </div>
</div>
```

```javascript
// JavaScript initialization for tooltip behavior
document.querySelectorAll('.usa-tooltip__trigger').forEach(trigger => {
  const tooltipId = trigger.getAttribute('aria-describedby');
  const tooltip = document.getElementById(tooltipId);
  
  trigger.addEventListener('mouseenter', () => {
    tooltip.classList.add('is-visible');
  });
  
  trigger.addEventListener('mouseleave', () => {
    tooltip.classList.remove('is-visible');
  });
  
  trigger.addEventListener('focus', () => {
    tooltip.classList.add('is-visible');
  });
  
  trigger.addEventListener('blur', () => {
    tooltip.classList.remove('is-visible');
  });
});
```

### Context

Tooltips are a USWDS-based component integrated into the Maryland Design System for providing contextual help and information. They compose with form controls, buttons, and icons to improve accessibility and user guidance across Maryland state web applications.

---

## USWDS Components Collection

*Components*

This is a collection index page for USWDS (U.S. Web Design System) components integrated into the Maryland Web Design System. It serves as a comprehensive reference and navigation hub for all available UI components that developers and designers can use to build Maryland state web pages. This page helps users discover, explore, and understand the various pre-built components available in the design system.

### Key Information

The page presents a collection of USWDS components that have been integrated into the Maryland Web Design System. Key aspects include:

- **Collection Purpose**: Central repository for component documentation and reference
- **Component Access**: Provides navigation to individual component documentation pages
- **Toolbar Interface**: Includes a toolbar with a "New" button and "Skip to sidebar" functionality for accessibility
- **Navigation**: Sidebar navigation for filtering and accessing specific component categories
- **USWDS Integration**: All components follow U.S. Web Design System standards and guidelines
- **Component Types**: Includes form controls, layout components, content containers, interactive elements, and other UI building blocks
- **Documentation Structure**: Each component typically includes usage guidelines, code examples, and best practices

This serves as the entry point for accessing component-level documentation within the design system.

### Implementation

```html
<!-- Main collection page structure -->
<div class="uswds-collection">
  <!-- Toolbar with navigation -->
  <div class="toolbar" role="toolbar">
    <button class="toolbar-button" aria-label="Create new">New</button>
    <a href="#sidebar" class="skip-link">Skip to sidebar</a>
  </div>
  
  <!-- Sidebar navigation -->
  <aside id="sidebar" class="sidebar" role="navigation">
    <!-- Component category filters and links go here -->
  </aside>
  
  <!-- Main content area -->
  <main class="collection-content" role="main">
    <!-- Individual component cards or documentation sections -->
  </main>
</div>
```

Note: The specific component listings and detailed implementations are accessed through individual component pages within this collection.

### Context

The USWDS Components Collection serves as the central hub within the Maryland Web Design System for accessing all available USWDS components. It provides a structured way to browse, reference, and implement components consistently across Maryland state web properties, ensuring compliance with federal web standards while maintaining Maryland-specific customizations.

---

## Utility Nav

*Components*

The Utility Nav is a lightweight navigation bar positioned at the top of the page that provides access to secondary links and utilities such as language selection, login/account access, and other support functions. It serves as a persistent, accessible header element that typically sits above the main navigation and helps users quickly access account-related features and site utilities without cluttering the primary navigation structure.

### Key Information

The Utility Nav is a compact, horizontal navigation component designed for secondary/utility links. It typically includes:

- **Purpose**: Host secondary navigation items like language switchers, account login, search, contact info, and help links
- **Placement**: Positioned at the very top of the page, above main navigation
- **Structure**: Uses semantic list markup with proper ARIA labeling
- **Accessibility**: Includes proper ARIA roles and keyboard navigation support
- **Styling**: Minimal styling to distinguish it as secondary navigation
- **Variants**: Can display inline links or as a horizontal list depending on layout needs
- **Responsive**: May collapse to a compact menu on mobile devices

Key CSS classes typically include:
- `.utility-nav` or similar container class
- List items styled for inline horizontal display
- Link styling for utility items

### Implementation

```html
<!-- Basic Utility Nav Structure -->
<nav class="utility-nav" aria-label="Utility navigation">
  <ul class="utility-nav__list">
    <li class="utility-nav__item">
      <a href="#" class="utility-nav__link">Language</a>
    </li>
    <li class="utility-nav__item">
      <a href="#" class="utility-nav__link">Login</a>
    </li>
    <li class="utility-nav__item">
      <a href="#" class="utility-nav__link">Contact</a>
    </li>
    <li class="utility-nav__item">
      <a href="#" class="utility-nav__link">Help</a>
    </li>
  </ul>
</nav>
```

**Required Attributes:**
- `aria-label="Utility navigation"` on the `<nav>` element to distinguish from other navigation regions
- Semantic `<nav>` element with proper list structure
- `<ul>` and `<li>` elements for list semantics

### Context

The Utility Nav is a foundational component in the MDWDS that typically appears at the very top of the page layout, above main navigation and other header elements. It provides a dedicated zone for utility and secondary links, helping establish a clear visual and functional hierarchy that keeps primary navigation focused on main content categories while utilities remain consistently accessible.

---

## Validation

*Components*

Validation provides visual and programmatic feedback to users when form inputs don't meet requirements. It includes error states, success states, and helper text to guide users through form completion and correction of mistakes.

### Key Information

## Validation States

- **Error State**: Indicates invalid input with error message and red styling
- **Success State**: Indicates valid input with success message and green styling
- **Warning State**: Indicates caution needed with warning message and yellow styling
- **Helper Text**: Provides additional context or requirements for form fields

## CSS Classes & Attributes

- `.usa-form-group`: Container for form field with validation
- `.usa-form-group--error`: Applies error styling to form group
- `.usa-input--error`: Applies error styling to input element
- `.usa-form-group__error`: Container for error message text
- `aria-invalid="true"`: Set on invalid inputs for accessibility
- `aria-describedby`: Links input to error message ID

## Key Attributes

- Required error messages must have unique IDs
- Error messages should use `.usa-form-group__error` class
- Icons may be used to visually reinforce validation state
- Validation can occur on blur, change, or form submission
- Helper text provides guidance before validation failure

## USWDS Foundation

Validation is built on USWDS (U.S. Web Design System) patterns and follows federal accessibility standards for form validation.

### Implementation

```html
<!-- Error State Example -->
<div class="usa-form-group usa-form-group--error">
  <label class="usa-label" for="input-error">
    Form field with error
  </label>
  <span class="usa-error-message" id="input-error-message" role="alert">
    <span class="usa-sr-only">Error:</span> This field is required
  </span>
  <input
    class="usa-input usa-input--error"
    id="input-error"
    type="text"
    name="input-error"
    aria-invalid="true"
    aria-describedby="input-error-message"
  />
</div>
```

```html
<!-- Success State Example -->
<div class="usa-form-group">
  <label class="usa-label" for="input-success">
    Form field with success
  </label>
  <input
    class="usa-input"
    id="input-success"
    type="text"
    name="input-success"
    value="Valid input"
  />
  <span class="usa-success-message">✓ This field is valid</span>
</div>
```

```html
<!-- Helper Text Example -->
<div class="usa-form-group">
  <label class="usa-label" for="input-helper">
    Form field with helper text
  </label>
  <span class="usa-hint" id="input-helper-hint">
    Password must be at least 8 characters
  </span>
  <input
    class="usa-input"
    id="input-helper"
    type="password"
    name="input-helper"
    aria-describedby="input-helper-hint"
  />
</div>
```

```html
<!-- Multiple Validation Messages -->
<div class="usa-form-group usa-form-group--error">
  <label class="usa-label" for="email-field">
    Email Address
  </label>
  <span class="usa-error-message" id="email-error" role="alert">
    <span class="usa-sr-only">Error:</span> Please enter a valid email address
  </span>
  <input
    class="usa-input usa-input--error"
    id="email-field"
    type="email"
    name="email"
    aria-invalid="true"
    aria-describedby="email-error"
  />
</div>
```

### Context

Validation is a critical USWDS component used across MDWDS form implementations to provide accessible, consistent feedback on user input. It integrates with other form components like inputs, selects, and textareas to create complete form workflows.

---

## Video Promo

*Components*

The Video Promo component is a promotional content block that features a video thumbnail with overlay text, headline, and call-to-action elements. It's used to highlight video content and draw user attention to multimedia resources on Maryland state web pages.

### Key Information

## Variants
- Standard video promo with thumbnail, headline, description, and CTA button
- Overlay text positioned over video thumbnail
- Optional badge or label

## CSS Classes
- `.video-promo` - Main container class
- `.video-promo__thumbnail` - Video thumbnail image wrapper
- `.video-promo__content` - Content section containing text and CTA
- `.video-promo__headline` - Headline text
- `.video-promo__description` - Description/body text
- `.video-promo__cta` - Call-to-action button

## Key Attributes
- Video source URL or thumbnail image source
- Title/headline text
- Description text
- CTA button text and link
- Optional: Video duration, badge text

## Important Notes
- Maintains responsive design across all screen sizes
- Video thumbnail should use appropriate aspect ratio
- CTA button integrates with Maryland button component
- Supports both internal and external video links

### Implementation

```html
<div class="video-promo">
  <div class="video-promo__thumbnail">
    <img src="video-thumbnail.jpg" alt="Video thumbnail description">
    <button class="video-promo__play-button" aria-label="Play video">
      <span class="icon-play"></span>
    </button>
  </div>
  <div class="video-promo__content">
    <h3 class="video-promo__headline">Video Title</h3>
    <p class="video-promo__description">Brief description of the video content goes here.</p>
    <a href="#" class="btn btn-primary">Watch Video</a>
  </div>
</div>
```

### Responsive Variant
```html
<div class="video-promo video-promo--responsive">
  <div class="video-promo__thumbnail">
    <img src="video-thumbnail.jpg" alt="Video description" class="video-promo__image">
    <button class="video-promo__play-button" aria-label="Play video">
      <span class="icon-play"></span>
    </button>
  </div>
  <div class="video-promo__content">
    <h3 class="video-promo__headline">Responsive Video Promo</h3>
    <p class="video-promo__description">Description text for mobile and desktop layouts.</p>
    <a href="video-page.html" class="btn btn-primary btn-sm">Learn More</a>
  </div>
</div>
```

### Context

The Video Promo component is a specialized content component within MDWDS that combines image, text, and button elements to create engaging promotional blocks. It typically composes with the Button component for its CTA and follows Maryland's design patterns for multimedia content presentation.

---

## Visual Link Collection

*Components*

The Visual Link Collection is a component that displays a group of linked items with visual indicators, typically used for navigation or content discovery. It organizes related links in a structured, scannable format. Use this when you need to present multiple related destinations or actions in a visually organized way.

### Key Information

**Variants:**
- Grid layout with visual cards for each link
- Icon/image support for visual context
- Text-based link labels and descriptions

**Class Names & Structure:**
- `.visual-link-collection` — main container wrapper
- `.visual-link-item` — individual link item
- `.visual-link-label` — text label for the link
- `.visual-link-description` — optional description text

**Required Attributes:**
- `href` attribute on link elements
- Semantic HTML structure using `<a>` or `<button>` elements

**Options:**
- Multiple items can be displayed in grid or flex layout
- Supports icons or background images for visual enhancement
- Optional descriptions beneath each link label

**Important Notes:**
- Should maintain keyboard navigation and focus management
- Requires proper ARIA labels if using non-semantic link structures
- Visual indicators should not be the only method of distinction

### Implementation

```html
<!-- Basic Visual Link Collection -->
<div class="visual-link-collection">
  <a href="/destination-1" class="visual-link-item">
    <div class="visual-link-icon">
      <svg aria-hidden="true"><!-- icon content --></svg>
    </div>
    <h3 class="visual-link-label">Link Title One</h3>
    <p class="visual-link-description">Brief description of this destination</p>
  </a>
  
  <a href="/destination-2" class="visual-link-item">
    <div class="visual-link-icon">
      <svg aria-hidden="true"><!-- icon content --></svg>
    </div>
    <h3 class="visual-link-label">Link Title Two</h3>
    <p class="visual-link-description">Brief description of this destination</p>
  </a>
  
  <a href="/destination-3" class="visual-link-item">
    <div class="visual-link-icon">
      <svg aria-hidden="true"><!-- icon content --></svg>
    </div>
    <h3 class="visual-link-label">Link Title Three</h3>
    <p class="visual-link-description">Brief description of this destination</p>
  </a>
</div>
```

**With Images Instead of Icons:**
```html
<div class="visual-link-collection">
  <a href="/destination" class="visual-link-item">
    <img src="image.jpg" alt="Descriptive alt text" class="visual-link-image">
    <h3 class="visual-link-label">Link Title</h3>
  </a>
</div>
```

### Context

The Visual Link Collection component is part of the MDWDS component library and provides a flexible pattern for organizing multiple related links with visual support. It can be used within page templates and composes with heading, typography, and icon components to create cohesive navigation experiences.

---

# Templates

## Action Page

*Templates*

The Action Page is a template designed for pages that guide users toward completing specific tasks or taking action. It provides a structured layout to present call-to-action elements, instructions, and supporting information in a clear hierarchy. Use this template when you need to direct users to perform a specific action like submitting a form, requesting a service, or completing a transaction.

### Key Information

The Action Page template typically includes:

- **Header/Hero section**: Prominent title and description of the action
- **Call-to-Action button(s)**: Primary action button prominently displayed
- **Supporting content areas**: Sections for context, requirements, or prerequisites
- **Related links**: Navigation to related pages or alternative actions
- **Status indicators**: Optional badges or indicators for task status

Key layout patterns:
- Single-column or two-column layouts depending on content volume
- Button placement above or alongside content
- Clear visual hierarchy with headings and spacing
- Responsive design that works on mobile and desktop

The template leverages Maryland's standard button styles, typography, and spacing conventions from the design system.

### Implementation

```html
<!-- Action Page Template Structure -->
<div class="page-action">
  <!-- Header Section -->
  <section class="page-header">
    <div class="container">
      <h1 class="page-title">Action Page Title</h1>
      <p class="page-subtitle">Brief description of the action or service</p>
    </div>
  </section>

  <!-- Main Content Section -->
  <main class="page-content">
    <div class="container">
      <!-- Call-to-Action Section -->
      <section class="action-section">
        <h2>Ready to get started?</h2>
        <p>Introductory text explaining what the user will do.</p>
        <a href="#" class="btn btn-primary btn-lg">Primary Action Button</a>
        <a href="#" class="btn btn-secondary btn-lg">Secondary Action</a>
      </section>

      <!-- Supporting Content -->
      <section class="supporting-content">
        <h2>What you'll need</h2>
        <ul>
          <li>Requirement or document</li>
          <li>Requirement or document</li>
        </ul>
      </section>

      <!-- Related Information -->
      <section class="related-section">
        <h2>Related resources</h2>
        <ul class="link-list">
          <li><a href="#">Related page link</a></li>
          <li><a href="#">Related page link</a></li>
        </ul>
      </section>
    </div>
  </main>
</div>
```

### Context

The Action Page template is a composition of core Maryland design system components including typography, buttons, containers, and spacing utilities. It serves as a high-level page template that organizes these foundational elements and components into a cohesive, task-focused layout pattern.

---

## Agency Homepage

*Templates*

The Agency Homepage is a full-page template designed for Maryland state agency websites. It provides a standardized layout and structure that agencies can use to create consistent, branded web presences aligned with MDWDS guidelines. This template solves the problem of building agency websites from scratch by offering pre-configured sections, components, and layouts that follow state design standards.

### Key Information

The Agency Homepage template is a complete page composition that typically includes:

- **Header/Navigation**: Standard MDWDS header with agency branding and main navigation
- **Hero Section**: Large featured content area at the top of the page
- **Main Content Area**: Primary section for key agency information and services
- **Sidebar/Secondary Navigation**: Optional navigation for related content or services
- **Footer**: Standard MDWDS footer with required state links and information

**Key Characteristics:**
- Responsive design that works across desktop, tablet, and mobile devices
- Uses semantic HTML5 structure
- Integrates core MDWDS components (buttons, cards, navigation, etc.)
- Follows accessibility standards (WCAG 2.1 AA)
- Implements state color palette and typography standards
- Supports multiple content sections and flexible layouts

**Important Considerations:**
- Agency branding should follow the MDWDS brand guidelines
- Content should be organized hierarchically with clear navigation
- All interactive elements must include proper ARIA labels and roles
- The template serves as a starting point that should be customized for specific agency needs

### Implementation

```html
<!-- Agency Homepage Template -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agency Name - Maryland State Government</title>
    <link rel="stylesheet" href="mdwds-styles.css">
</head>
<body>
    <!-- Header with Navigation -->
    <header class="mdwds-header" role="banner">
        <div class="header-container">
            <div class="header-logo">
                <a href="/" class="logo-link">
                    <span class="agency-name">Agency Name</span>
                </a>
            </div>
            <nav class="header-nav" role="navigation" aria-label="Main Navigation">
                <ul class="nav-list">
                    <li><a href="#section1">Section 1</a></li>
                    <li><a href="#section2">Section 2</a></li>
                    <li><a href="#section3">Section 3</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero-section" aria-label="Featured Content">
        <div class="hero-container">
            <h1 class="hero-title">Welcome to [Agency Name]</h1>
            <p class="hero-subtitle">Your gateway to [agency mission/services]</p>
            <a href="#" class="btn btn-primary">Get Started</a>
        </div>
    </section>

    <!-- Main Content -->
    <main class="main-content" role="main">
        <div class="content-container">
            <!-- Primary Content Area -->
            <section class="primary-content">
                <h2>Key Services</h2>
                <div class="cards-grid">
                    <article class="card">
                        <h3>Service 1</h3>
                        <p>Description of service</p>
                        <a href="#" class="btn btn-secondary">Learn More</a>
                    </article>
                    <article class="card">
                        <h3>Service 2</h3>
                        <p>Description of service</p>
                        <a href="#" class="btn btn-secondary">Learn More</a>
                    </article>
                </div>
            </section>

            <!-- Sidebar (Optional) -->
            <aside class="sidebar" role="complementary" aria-label="Sidebar Navigation">
                <nav class="sidebar-nav">
                    <h3>Quick Links</h3>
                    <ul>
                        <li><a href="#">Link 1</a></li>
                        <li><a href="#">Link 2</a></li>
                        <li><a href="#">Link 3</a></li>
                    </ul>
                </nav>
            </aside>
        </div>
    </main>

    <!-- Footer -->
    <footer class="mdwds-footer" role="contentinfo">
        <div class="footer-container">
            <div class="footer-content">
                <p>&copy; 2024 State of Maryland</p>
                <ul class="footer-links">
                    <li><a href="#">Accessibility</a></li>
                    <li><a href="#">Privacy</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </div>
        </div>
    </footer>
</body>
</html>
```

### Context

The Agency Homepage template is a complete page composition that brings together multiple MDWDS components (header, navigation, cards, buttons, footer) into a cohesive, full-page layout. It serves as a reference implementation for how agencies should structure their websites while adhering to Maryland state design standards and best practices.

---

## Basic Page

*Templates*

The Basic Page template is a foundational layout template that provides a standardized structure for creating Maryland state web pages. It establishes the core page architecture, including header, navigation, and content areas that align with MDWDS standards. Use this template when creating new Maryland government web pages that require a consistent, accessible page structure.

### Key Information

### Overview
The Basic Page template serves as the foundational page structure for Maryland state web pages. It includes:

- Standard page header and branding
- Navigation and wayfinding elements
- Main content area
- Sidebar/complementary content area (optional)
- Footer with standard Maryland government links

### Key Components
- **Header**: Contains Maryland state branding and main navigation
- **Main Navigation**: Primary site navigation structure
- **Skip to Content**: Accessibility feature allowing users to bypass navigation (linked via "Skip to sidebar" toolbar)
- **Content Area**: Main content section for page body
- **Sidebar**: Optional secondary navigation or related content
- **Footer**: Standard Maryland government footer

### Required Structure
- Proper semantic HTML (header, main, aside, footer elements)
- Skip links for accessibility
- Responsive layout that adapts to mobile and desktop viewports
- Standard Maryland state branding and color scheme
- ARIA landmarks for screen reader navigation

### Variants
The template can accommodate different sidebar configurations:
- With sidebar (two-column layout)
- Without sidebar (single-column full-width)
- Variable content widths based on page needs

### Implementation

```html
<!-- Basic Page Template Structure -->
<div class="page-wrapper">
  <!-- Skip to Navigation Links -->
  <a href="#main-content" class="skip-link">Skip to main content</a>
  <a href="#sidebar" class="skip-link">Skip to sidebar</a>

  <!-- Header -->
  <header class="page-header" role="banner">
    <div class="header-container">
      <!-- Maryland State Branding -->
      <div class="state-branding">
        <span class="state-seal"></span>
        <span class="state-name">State of Maryland</span>
      </div>
      <!-- Site Title/Logo -->
      <div class="site-title">
        <h1>Your Agency or Site Name</h1>
      </div>
    </div>
  </header>

  <!-- Navigation -->
  <nav class="primary-navigation" role="navigation" aria-label="Main">
    <!-- Navigation items -->
  </nav>

  <!-- Main Content Area -->
  <div class="page-container">
    <main id="main-content" class="main-content" role="main">
      <!-- Page content goes here -->
      <h1>Page Title</h1>
      <p>Page content...</p>
    </main>

    <!-- Sidebar (Optional) -->
    <aside id="sidebar" class="sidebar" role="complementary" aria-label="Sidebar">
      <!-- Related content, secondary navigation, etc. -->
    </aside>
  </div>

  <!-- Footer -->
  <footer class="page-footer" role="contentinfo">
    <!-- Maryland state footer content -->
  </footer>
</div>
```

### Alternative: Full-Width Variant (No Sidebar)
```html
<div class="page-wrapper no-sidebar">
  <!-- Same header and nav structure -->
  
  <div class="page-container full-width">
    <main id="main-content" class="main-content" role="main">
      <!-- Full-width page content -->
    </main>
  </div>

  <!-- Footer -->
</div>
```

### Context

The Basic Page template is the foundational layout pattern within MDWDS Templates and composes standard elements (header, navigation, footer) that are reused across Maryland government web properties. It provides the structural scaffold into which other MDWDS components (Accordion, Cards, Forms, etc.) are placed to create complete, accessible web pages.

---

## Landing Page

*Templates*

The Landing Page template is a full-page layout designed as the primary entry point for Maryland state websites. It combines hero sections, featured content areas, and call-to-action elements to welcome users and guide them to key information or services.

### Key Information

## Structure
The Landing Page template serves as a complete page layout combining multiple MDWDS components into a cohesive entry experience.

## Key Components Used
- Hero section or banner for primary messaging
- Navigation integration from MDWDS navbar component
- Featured content cards or sections
- Call-to-action buttons using MDWDS button component
- Content sections for key information areas
- Footer integration from MDWDS footer component

## Layout Considerations
- Responsive design that adapts to mobile, tablet, and desktop viewports
- Uses Maryland design tokens for spacing, colors, and typography
- Integrates with MDWDS grid system for consistent layout alignment
- Accessibility-first approach with proper semantic HTML and ARIA attributes

## Variants
- May include different hero configurations (image, gradient, solid color backgrounds)
- Optional featured content grid layouts
- Various CTA button placements and configurations

## Important Facts
- This is a complete template, not a single component
- Intended as a starting point for new Maryland state web properties
- Composes together multiple individual MDWDS components
- Should maintain Maryland branding standards and visual hierarchy

### Implementation

```html
<!-- Landing Page Template Structure -->
<div class="mdwds-landing-page">
  <!-- Navigation -->
  <nav class="mdwds-navbar" role="navigation" aria-label="Main navigation">
    <!-- Navigation component implementation -->
  </nav>

  <!-- Hero Section -->
  <section class="mdwds-hero" aria-label="Hero section">
    <div class="mdwds-hero__content">
      <h1 class="mdwds-hero__title">Welcome to [Service/Department]</h1>
      <p class="mdwds-hero__subtitle">Supporting Maryland residents and businesses</p>
      <button class="mdwds-button mdwds-button--primary mdwds-button--large">
        Get Started
      </button>
    </div>
  </section>

  <!-- Main Content -->
  <main class="mdwds-main-content" id="main-content">
    <!-- Featured Services Section -->
    <section class="mdwds-featured-section" aria-label="Featured services">
      <div class="mdwds-container">
        <h2 class="mdwds-heading-2">Featured Services</h2>
        <div class="mdwds-grid mdwds-grid--3-cols">
          <div class="mdwds-card">
            <h3 class="mdwds-card__title">Service 1</h3>
            <p class="mdwds-card__description">Description of service</p>
            <a href="#" class="mdwds-button mdwds-button--secondary">Learn More</a>
          </div>
          <!-- Additional cards -->
        </div>
      </div>
    </section>

    <!-- Information Section -->
    <section class="mdwds-info-section" aria-label="Key information">
      <div class="mdwds-container">
        <h2 class="mdwds-heading-2">Important Information</h2>
        <!-- Content here -->
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer class="mdwds-footer" role="contentinfo">
    <!-- Footer component implementation -->
  </footer>
</div>
```

## Responsive Variants

```html
<!-- Mobile-optimized variant -->
<section class="mdwds-featured-section">
  <div class="mdwds-container">
    <h2 class="mdwds-heading-2">Featured Services</h2>
    <!-- Grid adjusts to 1 column on mobile via responsive utilities -->
    <div class="mdwds-grid mdwds-grid--1-col-mobile mdwds-grid--2-cols-tablet mdwds-grid--3-cols-desktop">
      <!-- Cards automatically adjust -->
    </div>
  </div>
</section>
```

### Context

The Landing Page template is a complete page composition that brings together multiple MDWDS components (navbar, buttons, cards, grid, footer) into a cohesive entry experience for Maryland state websites. It serves as the primary template for establishing consistent branding, navigation, and user guidance across the MDWDS ecosystem.

---

## Listing Page

*Templates*

The Listing Page is a template that displays collections of related items or content in an organized, scannable format. It provides a standardized layout for presenting lists of resources, documents, news items, or other content types that users need to browse and filter. This template is used when you need to present multiple similar items with consistent styling and interactive elements like filtering or search.

### Key Information

## Variants and Structure

The Listing Page template typically includes:

- **Header Section**: Page title and optional description
- **Filter/Search Bar**: For users to narrow down results
- **List Container**: Organized display of individual items
- **Item Cards/Rows**: Consistent presentation of each list item with relevant metadata
- **Pagination**: Navigation controls for browsing multiple pages of results

## Key Components

- List items should be presented in a consistent, repeating format
- Each item typically includes: title, brief description, date/metadata, and action link
- Items should be scannable with proper spacing and typography hierarchy
- Optional filters, sorting options, and search functionality
- Pagination or infinite scroll for managing large lists

## CSS Classes and Structure

The template uses standard MDWDS components combined with layout utilities. Items are typically wrapped in grid or flex containers for responsive display.

## Required Attributes

- Proper heading hierarchy (h1 for page title, h2/h3 for item titles)
- Semantic HTML list elements where appropriate
- ARIA labels for filter controls and interactive elements
- Link destinations for each list item

## Important Facts

- This is a composition of multiple MDWDS components (cards, buttons, filters, pagination)
- Responsive design adapts from single column (mobile) to multiple columns (desktop)
- Should follow MDWDS typography and spacing standards
- Can be customized for different content types while maintaining structure

### Implementation

```html
<!-- Listing Page Template -->
<main class="container">
  <!-- Page Header -->
  <div class="listing-header">
    <h1>Page Title</h1>
    <p class="lead">Optional page description or subtitle</p>
  </div>

  <!-- Filter/Search Section -->
  <div class="listing-controls">
    <div class="search-bar">
      <input type="search" placeholder="Search items..." aria-label="Search listing">
      <button type="submit">Search</button>
    </div>
    <div class="filters">
      <select aria-label="Filter by category">
        <option value="">All Categories</option>
        <option value="category-1">Category 1</option>
        <option value="category-2">Category 2</option>
      </select>
    </div>
  </div>

  <!-- List Container -->
  <div class="listing-items" role="region" aria-label="Search results">
    <!-- Individual List Item -->
    <article class="listing-item">
      <h2><a href="/item-detail">Item Title</a></h2>
      <p class="item-meta">
        <span class="date">Published: January 1, 2024</span>
        <span class="category">Category Tag</span>
      </p>
      <p class="item-description">Brief description of the item goes here.</p>
      <a href="/item-detail" class="btn btn-primary">View Details</a>
    </article>

    <!-- Additional List Items Follow Same Pattern -->
    <article class="listing-item">
      <h2><a href="/item-detail-2">Another Item</a></h2>
      <p class="item-meta">
        <span class="date">Published: December 15, 2023</span>
        <span class="category">Category Tag</span>
      </p>
      <p class="item-description">Another item description.</p>
      <a href="/item-detail-2" class="btn btn-primary">View Details</a>
    </article>
  </div>

  <!-- Pagination -->
  <nav aria-label="Pagination" class="listing-pagination">
    <a href="#" class="btn btn-outline" aria-label="Previous page" rel="prev">Previous</a>
    <span>Page 1 of 5</span>
    <a href="#" class="btn btn-outline" aria-label="Next page" rel="next">Next</a>
  </nav>
</main>
```

### Context

The Listing Page template is a composition of foundational MDWDS components (typography, spacing, cards, buttons) combined into a complete page layout. It provides a reusable structure for displaying collections of content while maintaining consistency with Maryland state web standards and accessibility requirements.

---

## Location Page

*Templates*

The Location Page is a template for displaying Maryland state office or facility locations with contact information and directions. It provides a standardized way to present location details, hours of operation, and contact methods to site visitors. Use this template when you need to feature a specific Maryland state office, facility, or service location.

### Key Information

This is a full-page template that combines multiple components to create a location-focused landing page. The template typically includes:

- **Page Header**: Maryland state branding and navigation
- **Hero/Title Section**: Location name and primary identifier
- **Content Sections**: Key information areas for hours, address, phone, email, and directions
- **Contact Information Block**: Structured display of office details (hours, address, phone numbers, email)
- **Map Integration**: Embedded map or directions link
- **Services/Info Cards**: Additional details specific to the location
- **Call-to-Action Elements**: Links to online services or related locations

The page follows Maryland's standard page layout and component patterns, maintaining consistency with other state templates. It leverages the grid system, typography, spacing utilities, and component library established in MDWDS.

### Implementation

```html
<!-- Location Page Template Structure -->
<div class="page-wrapper">
  <!-- Header/Navigation -->
  <header class="site-header">
    <!-- Standard Maryland header components -->
  </header>

  <!-- Hero/Page Title Section -->
  <section class="page-hero">
    <div class="container">
      <h1 class="page-title">Location Name</h1>
      <p class="page-subtitle">Organization or Department</p>
    </div>
  </section>

  <!-- Main Content -->
  <main class="page-content">
    <div class="container">
      <div class="row">
        <!-- Primary Content Column -->
        <div class="col-md-8">
          <section class="location-details">
            <h2>About This Location</h2>
            <p>Description of the location and services provided.</p>
          </section>

          <section class="services-section">
            <h2>Services Available</h2>
            <!-- Service cards or list -->
          </section>
        </div>

        <!-- Sidebar - Contact & Hours -->
        <aside class="col-md-4">
          <div class="location-info-card">
            <h3>Hours of Operation</h3>
            <ul class="hours-list">
              <li>Monday - Friday: 8:00 AM - 5:00 PM</li>
              <li>Saturday - Sunday: Closed</li>
            </ul>

            <h3>Address</h3>
            <address>
              Street Address<br>
              City, State ZIP Code
            </address>

            <h3>Contact Information</h3>
            <p>
              <strong>Phone:</strong> 
              <a href="tel:+14105551234">(410) 555-1234</a>
            </p>
            <p>
              <strong>Email:</strong> 
              <a href="mailto:info@maryland.gov">info@maryland.gov</a>
            </p>

            <h3>Directions</h3>
            <a href="#map" class="btn btn-primary">Get Directions</a>
          </div>
        </aside>
      </div>

      <!-- Map Section -->
      <section id="map" class="location-map-section">
        <h2>Location Map</h2>
        <div class="map-container">
          <!-- Embedded map or iframe -->
        </div>
      </section>

      <!-- Additional Resources -->
      <section class="related-locations">
        <h2>Other Locations</h2>
        <!-- Links to related location pages -->
      </section>
    </div>
  </main>

  <!-- Footer -->
  <footer class="site-footer">
    <!-- Standard Maryland footer -->
  </footer>
</div>
```

### Context

The Location Page template is part of MDWDS Templates and provides a pre-built structure for Maryland state locations and facilities. It combines foundation elements (typography, spacing, grid), core components (cards, buttons, navigation), and utilities to create a complete, accessible page experience that aligns with Maryland's digital standards.

---

## Maryland Homepage

*Templates*

The Maryland Homepage is a template that demonstrates the proper structure and composition of a full-page website for Maryland state organizations. It serves as a reference implementation showing how to assemble various MDWDS components (header, navigation, hero, content sections, and footer) into a cohesive, accessible web page that meets state web standards and branding guidelines.

### Key Information

This template integrates core MDWDS components including:
- **Header**: Contains the Maryland state branding and logo
- **Navigation**: Primary navigation bar with links to main sections
- **Hero Section**: Prominent banner area for featured content or messaging
- **Content Sections**: Main page content area with flexible layout options
- **Footer**: Footer with state-level links and information
- **Accessibility**: Implements ARIA labels and semantic HTML structure
- **Responsive Design**: Mobile-first responsive layout that adapts to different screen sizes
- **Skip Links**: Skip to main content navigation for keyboard users

The template demonstrates proper semantic HTML structure, correct class name usage, and the composition pattern of how MDWDS components work together at the page level. It serves as the starting point for creating new Maryland state web pages.

### Implementation

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Maryland Homepage Template</title>
  <link rel="stylesheet" href="mdwds-styles.css">
</head>
<body>
  <!-- Skip Link -->
  <a href="#main-content" class="skip-link">Skip to main content</a>
  
  <!-- Toolbar/Header -->
  <header class="md-header" role="banner">
    <div class="md-header-top">
      <div class="container">
        <a href="/" class="md-logo">
          <img src="maryland-logo.svg" alt="State of Maryland">
        </a>
        <nav class="md-header-nav" role="navigation" aria-label="Primary navigation">
          <!-- Navigation items -->
        </nav>
      </div>
    </div>
  </header>

  <!-- Skip to Sidebar Link -->
  <a href="#sidebar" class="skip-link">Skip to sidebar</a>

  <!-- Main Content -->
  <main id="main-content" role="main">
    <!-- Hero Section -->
    <section class="md-hero">
      <div class="container">
        <!-- Hero content -->
      </div>
    </section>

    <!-- Page Content -->
    <section class="md-page-content">
      <div class="container">
        <!-- Main content goes here -->
      </div>
    </section>
  </main>

  <!-- Sidebar (if applicable) -->
  <aside id="sidebar" role="complementary" aria-label="Secondary navigation">
    <!-- Sidebar content -->
  </aside>

  <!-- Footer -->
  <footer class="md-footer" role="contentinfo">
    <div class="container">
      <!-- Footer content -->
    </div>
  </footer>
</body>
</html>
```

### Context

The Maryland Homepage template is the top-level reference implementation in MDWDS that demonstrates how to properly structure a complete state web page by composing header, navigation, hero, content, and footer components according to system standards. It establishes the foundational pattern that all Maryland state web pages should follow to maintain consistency, accessibility, and brand compliance.

---

## News Page

*Templates*

The News Page is a template that provides a structured layout for displaying news articles and content related to Maryland state government. It serves as a reusable page template that helps maintain consistency across news-related content on state websites. Use this template when creating dedicated pages for news, announcements, or press releases within the Maryland Web Design System.

### Key Information

The News Page template follows the MDWDS design patterns and layout structure for presenting news-related information. It includes standard header and navigation components integrated with content areas for articles, dates, and related metadata. This template should maintain responsive design principles and comply with accessibility standards required for Maryland state web properties. The page structure includes standard Maryland branding elements, navigation patterns, and content organization suited for news and announcement publishing.

### Implementation

```html
<!-- News Page Template Structure -->
<div class="news-page">
  <!-- Header and Navigation (standard MDWDS header) -->
  <header class="mdwds-header" role="banner">
    <!-- Maryland branding and navigation -->
  </header>

  <!-- Main Content Area -->
  <main class="mdwds-main-content" role="main">
    <div class="news-container">
      <!-- News Page Title/Hero Section -->
      <section class="news-hero">
        <h1>News</h1>
      </section>

      <!-- News Articles List -->
      <section class="news-articles" aria-label="News Articles">
        <article class="news-item">
          <h2><a href="#">Article Title</a></h2>
          <time datetime="YYYY-MM-DD">Date Published</time>
          <p>Article summary or excerpt</p>
        </article>
      </section>
    </div>
  </main>

  <!-- Footer (standard MDWDS footer) -->
  <footer class="mdwds-footer" role="contentinfo">
    <!-- Standard Maryland footer content -->
  </footer>
</div>
```

### Context

The News Page template is part of the MDWDS Templates collection and combines standard header, navigation, and footer components with a specialized news content layout. It follows the established MDWDS component patterns to ensure visual and functional consistency across Maryland state government web properties.

---

## Search Page

*Templates*

The Search Page is a template for implementing a full-page search interface for Maryland state websites. It provides a standardized layout and component structure for users to enter search queries and interact with search results, ensuring consistency across state web properties.

### Key Information

This template serves as a pre-built page layout designed for search-focused functionality. Key features include:

- **Purpose**: Full-page search interface for state websites
- **Template Type**: Reusable page layout combining multiple components
- **Structure**: Integrates header, search input, filters, and results display areas
- **Composition**: Uses foundational components (search box, buttons, typography, spacing utilities) combined into a cohesive template
- **Responsive**: Adapts to different screen sizes while maintaining usability
- **Accessibility**: Includes proper semantic HTML and ARIA labels for search functionality

Common use cases:
- Site-wide search functionality
- Public records search
- Service finder interfaces
- Document and resource discovery pages

### Implementation

```html
<!-- Search Page Template Structure -->
<main role="main" class="page-wrapper">
  <!-- Header Section -->
  <header class="search-page-header">
    <h1>Search</h1>
    <p class="subtitle">Find information, services, and resources</p>
  </header>

  <!-- Search Input Section -->
  <section class="search-input-section">
    <form role="search" method="get" action="/search">
      <div class="form-group">
        <label for="search-input" class="form-label">Search Query</label>
        <div class="input-wrapper">
          <input 
            type="search" 
            id="search-input" 
            name="q" 
            class="form-control search-input"
            placeholder="Enter your search terms"
            required
          />
          <button 
            type="submit" 
            class="btn btn-primary"
            aria-label="Submit search"
          >
            Search
          </button>
        </div>
      </div>

      <!-- Optional Filters -->
      <div class="search-filters">
        <fieldset>
          <legend class="filter-legend">Refine Your Search</legend>
          <div class="filter-options">
            <label class="checkbox">
              <input type="checkbox" name="filter-type" value="pages" />
              <span>Web Pages</span>
            </label>
            <label class="checkbox">
              <input type="checkbox" name="filter-type" value="documents" />
              <span>Documents</span>
            </label>
          </div>
        </fieldset>
      </div>
    </form>
  </section>

  <!-- Results Section -->
  <section class="search-results" aria-live="polite" aria-label="Search results">
    <div class="results-info">
      <p>Showing <strong id="result-count">0</strong> results</p>
    </div>

    <div class="results-list">
      <!-- Search result items populated dynamically -->
      <article class="search-result-item">
        <h2 class="result-title">
          <a href="#" class="result-link">Result Title</a>
        </h2>
        <p class="result-url">https://example.maryland.gov/page</p>
        <p class="result-snippet">Brief description or excerpt of the search result...</p>
        <div class="result-metadata">
          <span class="result-date">Published: January 15, 2024</span>
        </div>
      </article>
    </div>

    <!-- Pagination (if applicable) -->
    <nav class="pagination" aria-label="Search results pagination">
      <ul class="pagination-list">
        <li><a href="#" class="pagination-link" aria-current="page">1</a></li>
        <li><a href="#" class="pagination-link">2</a></li>
        <li><a href="#" class="pagination-link">3</a></li>
      </ul>
    </nav>
  </section>
</main>
```

### Context

The Search Page template combines foundational components (form inputs, buttons, typography, spacing) with MDWDS patterns to create a complete, accessible search interface. It demonstrates how to compose multiple system components into a functional page template that serves a specific user need within Maryland state websites.

---

# Utilities

## Layout Grid

*Utilities*

The Layout Grid is a responsive utility system for creating flexible, consistent page layouts across Maryland state websites. It provides a foundation for organizing content into rows and columns that adapt to different screen sizes. Use it to ensure visual consistency and responsive behavior across all page templates and components.

### Key Information

## Overview
- Responsive grid system based on a 12-column layout
- Supports multiple breakpoints for mobile, tablet, and desktop views
- Uses flexbox for alignment and distribution

## Class Names
- `.grid` - Main grid container wrapper
- `.grid-row` - Row container (direct child of grid)
- `.grid-col` - Column element (direct child of grid-row)
- `.grid-col-{n}` - Width modifier (e.g., `.grid-col-6` for 50% width)
- `.grid-col-auto` - Auto-width column
- `.grid-gap` - Add gap/spacing between grid items
- `.grid-gap-{size}` - Gap size modifiers (small, medium, large)

## Responsive Breakpoints
- Mobile-first approach
- Prefix modifiers with breakpoint: `tablet:`, `desktop:`, `widescreen:`
- Examples: `.desktop:grid-col-4`, `.tablet:grid-col-6`

## Key Attributes
- Display flex by default
- Supports alignment utilities: `align-items`, `justify-content`
- Works with standard spacing and sizing utilities

## Important Facts
- Mobile-first responsive design
- Ensures consistent 16px base unit spacing
- Compatible with all MDWDS components
- Improves accessibility through semantic structure

### Implementation

## Basic Grid Structure

```html
<div class="grid">
  <div class="grid-row">
    <div class="grid-col grid-col-12 tablet:grid-col-6 desktop:grid-col-4">
      <!-- Content here -->
    </div>
    <div class="grid-col grid-col-12 tablet:grid-col-6 desktop:grid-col-4">
      <!-- Content here -->
    </div>
    <div class="grid-col grid-col-12 tablet:grid-col-6 desktop:grid-col-4">
      <!-- Content here -->
    </div>
  </div>
</div>
```

## Full-Width Column

```html
<div class="grid">
  <div class="grid-row">
    <div class="grid-col grid-col-12">
      <!-- Full width content -->
    </div>
  </div>
</div>
```

## Grid with Gaps

```html
<div class="grid grid-gap">
  <div class="grid-row">
    <div class="grid-col grid-col-12 desktop:grid-col-6">
      <!-- Content -->
    </div>
    <div class="grid-col grid-col-12 desktop:grid-col-6">
      <!-- Content -->
    </div>
  </div>
</div>
```

## Auto-Width Columns

```html
<div class="grid">
  <div class="grid-row">
    <div class="grid-col grid-col-auto">
      <!-- Content auto-sizes -->
    </div>
    <div class="grid-col grid-col-auto">
      <!-- Content auto-sizes -->
    </div>
  </div>
</div>
```

### Context

The Layout Grid is a foundational utility component that works with all MDWDS templates and page layouts to provide consistent responsive behavior across Maryland state web pages. It pairs with spacing utilities and alignment helpers to create well-structured, accessible page layouts.

---

# Other

## Adopt Conventional Comments for Code Reviews

*Other*

This is an Architecture Decision Record (ADR) documenting the adoption of Conventional Comments as a standard for code reviews within the Maryland Web Design System project. It establishes best practices for providing structured, consistent feedback during the peer review process to improve code quality and team communication.

### Key Information

This ADR establishes the use of Conventional Comments as the standard format for code review feedback in MDWDS. Key points include:

- **Purpose**: Standardizes code review comments to improve clarity, reduce ambiguity, and streamline the review process
- **Conventional Comments Format**: Uses a structured prefix system for different types of comments:
  - `praise:` - Positive feedback on well-executed code
  - `nitpick:` - Minor stylistic or formatting suggestions
  - `suggestion:` - Non-blocking recommendations for improvement
  - `issue:` - Blocking concerns that should be addressed before merge
  - `question:` - Requests for clarification
  - `thought:` - Exploratory or informational comments
  - `chore:` - Maintenance-related comments

- **Benefits**: Improves communication clarity, distinguishes blocking from non-blocking feedback, helps reviewers and authors understand the priority and nature of each comment, and creates a more constructive review culture

- **Implementation**: All team members should use the Conventional Comments format when providing feedback on pull requests and code reviews

### Implementation

While this is a policy/process document rather than a UI component, the implementation involves:

**Code Review Comment Format:**

```
<TYPE>: [optional blocking marker] <summary>

[optional body]

[optional metadata]
```

**Examples:**

```
praise: Great refactoring of the button component! The code is much more maintainable.
```

```
suggestion: Consider using the `useCallback` hook here to memoize the event handler and improve performance.
```

```
issue: This breaks the existing API contract. The component no longer accepts the `disabled` prop, which will cause issues downstream.
```

```
question: Why are we using flexbox here instead of grid? Is there a specific reason for this approach?
```

```
nitpick: The variable name `temp` could be more descriptive. Consider `formattedDate` or similar.
```

**Guidelines:**
- Include the comment type prefix to clarify intent
- Use optional blocking marker `[blocking]` to indicate critical issues
- Keep comments constructive and focused
- Provide context and suggestions for improvement when possible

### Context

This ADR is part of the MDWDS developer documentation and governance, establishing development practices and standards that all team members follow when collaborating on the design system. It supports quality assurance and consistency across all components and contributions to the system.

---

## Adopt Conventional Commits for Versioning and Clarity

*Other*

This is an Architecture Decision Record (ADR) documenting the adoption of Conventional Commits as the standard commit message format for the Maryland Web Design System. It establishes clear versioning and communication practices across the design system codebase. This applies to all developers contributing to MDWDS to ensure consistency, automated changelog generation, and semantic versioning.

### Key Information

## Conventional Commits Standard

Conventional Commits is a specification for adding human and machine-readable meaning to commit messages. The format follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Commit Types
- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (formatting, missing semicolons, etc.)
- **refactor**: Code change that neither fixes a bug nor adds a feature
- **perf**: Code change that improves performance
- **test**: Adding or updating tests
- **chore**: Changes to build process, dependencies, or tooling
- **ci**: Changes to CI/CD configuration

### Breaking Changes
- Append `!` after the type/scope to indicate a breaking change: `feat!:` or `feat(scope)!:`
- Include `BREAKING CHANGE:` in the footer to describe the breaking change

### Scope (Optional)
- Identifies the section of the codebase affected (e.g., `button`, `form`, `accessibility`)
- Helps categorize and filter commits

### Description Requirements
- Use imperative mood ("add" not "added" or "adds")
- Do not capitalize first letter
- No period (.) at the end
- Keep it concise (50 characters or less preferred)

### Body (Optional)
- Explain what and why, not how
- Wrap at 72 characters
- Separated from description by blank line

### Footer (Optional)
- Reference issues: `Closes #123`, `Fixes #456`, `Relates to #789`
- Include `BREAKING CHANGE:` for significant API changes

## Benefits
- Automated semantic versioning (major.minor.patch)
- Automated changelog generation
- Clear commit history
- Better repository navigation and filtering
- Integration with CI/CD pipelines

### Implementation

## Example Conventional Commits

### Feature Commit
```
feat(button): add loading state to primary button

Add new loading prop to button component that displays 
a spinner and disables interaction while async action 
is in progress.

Closes #234
```

### Bug Fix
```
fix(accessibility): improve keyboard navigation in modal

Previously tabbing through modal did not properly trap focus
in accessible ways. Fixed by implementing proper focus trap
and returning focus to trigger on close.

Fixes #567
```

### Breaking Change
```
feat(form)!: restructure form validation API

BREAKING CHANGE: The onChange handler signature has changed from
onChange(value) to onChange({value, errors}). Update all form
implementations to destructure the new object format.

Closes #890
```

### Documentation
```
docs: add accessibility guidelines to README

Update main README with comprehensive accessibility guidelines
including WCAG 2.1 AA compliance requirements.
```

### Chore/Dependency Update
```
chore(deps): upgrade react to v18.0.0
```

### Style/Format
```
style(button): remove trailing whitespace and reformat CSS
```

### Performance Improvement
```
perf(grid): optimize rendering of large lists

Use React.memo on grid row component to prevent unnecessary
re-renders when parent grid updates.
```

### Test Update
```
test(button): add tests for loading state

Add unit tests covering loading state transitions, disabled
state verification, and spinner visibility.
```

### Context

This ADR establishes development practices and code quality standards for the Maryland Web Design System team. It ensures all contributors follow a consistent approach to versioning and commit messaging, which improves project maintainability, automated tooling integration, and developer communication across the MDWDS project.

---

## Changelog

*Other*

The Changelog documents the version history and updates to the Maryland Web Design System (MDWDS), including new features, bug fixes, improvements, and breaking changes. It serves as a reference for developers and designers to understand what has changed between releases and how to migrate their implementations when needed.

### Key Information

The Changelog is a historical record maintained for the MDWDS project. Key aspects include:

- **Purpose**: Tracks all updates, features, and fixes released in different versions
- **Content Types**: Features, bug fixes, improvements, deprecations, and breaking changes
- **Version References**: Links specific changes to version numbers for dependency management
- **Update Frequency**: Updated with each release cycle
- **Accessibility**: Provides important information for developers deciding when to upgrade their projects
- **Breaking Changes**: Clearly documents any changes that may require code modifications in consuming applications

Developers should regularly consult the Changelog when:
- Updating MDWDS to a new version
- Planning component implementations
- Understanding deprecated features
- Troubleshooting issues that may be version-related

### Implementation

The Changelog is a documentation reference page rather than a reusable component. It typically uses standard markdown or documentation formatting:

```html
<!-- Changelog documentation structure -->
<main class="docs-content">
  <h1>Changelog</h1>
  <article>
    <h2>Version X.X.X</h2>
    <p><strong>Release Date:</strong> YYYY-MM-DD</p>
    
    <h3>Features</h3>
    <ul>
      <li>New feature description</li>
    </ul>
    
    <h3>Bug Fixes</h3>
    <ul>
      <li>Bug fix description</li>
    </ul>
    
    <h3>Breaking Changes</h3>
    <ul>
      <li>Breaking change with migration guidance</li>
    </ul>
  </article>
</main>
```

For implementation details, consult specific version entries in the Changelog for exact changes to affected components.

### Context

The Changelog is a foundational reference document within the MDWDS that complements the component library and design guidelines. It documents the evolution of all system components and helps teams ensure their implementations remain compatible with current versions while understanding deprecations and improvements across the entire system.

---
