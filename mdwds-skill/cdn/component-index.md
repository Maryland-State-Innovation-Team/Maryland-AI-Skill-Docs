# Component Index

Lookup table for every MDWDS component. Use this to decide which file to read next.

**Three source families:**
- **MDWDS-original** (`maryland-*`) — components designed by the Maryland team
- **USWDS-themed** (`maryland-*` wrapping USWDS markup, or pure `usa-*`) — USWDS components restyled for Maryland
- **Web components** (`<maryland-statewide-banner>`, `<maryland-statewide-footer>`) — Lit-based custom elements

**Important duplication note:** MDWDS has two parallel "Card" components and two "Header"/Nav patterns because some components were re-implemented as MDWDS-specific while keeping the USWDS-styled versions available. The "Which to use" notes below tell you which.

---

## Layout & navigation

| Component | Source | What it is | When to use | Reference |
|---|---|---|---|---|
| `usa-banner` | USWDS | The "Official website of the State of Maryland" strip at the top of every page. | **Always.** Required on every state page. | [usa-banner.md](components/usa-banner.md) |
| `<maryland-statewide-banner>` | MDWDS web component | Web-component equivalent of `usa-banner`, lighter to embed in non-MDWDS sites. | Embedding the banner in a non-MDWDS site. For full MDWDS pages, prefer `usa-banner`. | [maryland-statewide-banner.md](components/maryland-statewide-banner.md) |
| `maryland-header` | MDWDS | Maryland-branded site header with utility nav + logo + primary nav. | Every full Maryland.gov page. | [maryland-header.md](components/maryland-header.md) |
| `maryland-nav` | MDWDS | Primary navigation bar inside the header. | Used automatically by `maryland-header`. Standalone only for custom layouts. | [maryland-nav.md](components/maryland-nav.md) |
| `maryland-utility-nav` | MDWDS | Small top-strip links above the header (sign-in, language, etc.). | Used automatically by `maryland-header`. | [maryland-utility-nav.md](components/maryland-utility-nav.md) |
| `maryland-footer` | MDWDS | Per-agency footer (address, phone, email, social). | Below `<main>`, above `<maryland-statewide-footer>`, on agency sites. | [maryland-footer.md](components/maryland-footer.md) |
| `<maryland-statewide-footer>` | MDWDS web component | The state-wide service-directory footer. Zero config. | At the very bottom of every Maryland.gov page. | [maryland-statewide-footer.md](components/maryland-statewide-footer.md) |
| `maryland-breadcrumb` | MDWDS | Maryland-styled breadcrumb trail. | Inside the hero, or above page content. **Use this, not `usa-breadcrumb`, on Maryland.gov pages.** | [maryland-breadcrumb.md](components/maryland-breadcrumb.md) |
| `usa-breadcrumb` | USWDS | The plain USWDS breadcrumb. | Only inside USWDS-styled subpages where MDWDS theming is undesirable. | [usa-breadcrumb.md](components/usa-breadcrumb.md) |
| `maryland-sidenav` | MDWDS | Sidebar navigation for documentation-style pages. | Sidebar on multi-page sections. | [maryland-sidenav.md](components/maryland-sidenav.md) |
| `usa-sidenav` | USWDS | The plain USWDS sidenav. | Prefer `maryland-sidenav` on Maryland pages. | [usa-sidenav.md](components/usa-sidenav.md) |
| `usa-in-page-navigation` | USWDS | On-this-page anchor links column. | Long article-style pages with multiple sections. | [usa-in-page-navigation.md](components/usa-in-page-navigation.md) |
| `usa-pagination` | USWDS | Pagination control (prev / page numbers / next). | Listing pages, search results. | [usa-pagination.md](components/usa-pagination.md) |
| `maryland-table-of-contents` | MDWDS | TOC component for long pages. | Top of long-form pages. | [maryland-table-of-contents.md](components/maryland-table-of-contents.md) |
| `usa-identifier` | USWDS | Agency identifier strip (parent agency, mission, etc.). | At the very bottom of federal-style pages. Rarely used in MDWDS — `maryland-statewide-footer` covers similar needs. | [usa-identifier.md](components/usa-identifier.md) |

## Hero & promo

| Component | Source | What it is | When to use | Reference |
|---|---|---|---|---|
| `maryland-hero` | MDWDS | Page hero. Four variants: `landing-main`, `landing-agency`, `landing-regular`, `basic`. | Top of every page below the header. | [maryland-hero.md](components/maryland-hero.md) |
| `maryland-promo` | MDWDS | Large promotional card / banner with image + CTA. | Cross-page promotions, featured content. | [maryland-promo.md](components/maryland-promo.md) |
| `maryland-video-promo` | MDWDS | Promo block with embedded video. | Featured video content. | [maryland-video-promo.md](components/maryland-video-promo.md) |

## Content display

| Component | Source | What it is | When to use | Reference |
|---|---|---|---|---|
| `maryland-card` | MDWDS | **Use this for most card needs on Maryland pages.** Five variants: simple, media, full, flag, linked. Designed for the Maryland visual style. | Service cards, news items, related links. | [maryland-card.md](components/maryland-card.md) |
| `usa-card` | USWDS | The plain USWDS card. Different markup, different visual. | Inside USWDS-style internal tools. **Don't** use on Maryland-branded pages — use `maryland-card`. | [usa-card.md](components/usa-card.md) |
| `usa-collection` | USWDS | Vertical list of items (articles, events) with optional images, dates, tags, and metadata. Variants: default, condensed, headings-only. | News listings, search results, event lists. | [usa-collection.md](components/usa-collection.md) |
| `maryland-callout` | MDWDS | Visually distinct callout box for highlighting key info. | Important info inside body content. | [maryland-callout.md](components/maryland-callout.md) |
| `maryland-highlight` | MDWDS | Highlighted text or block with accent styling. | Drawing attention to a key fact or quote. | [maryland-highlight.md](components/maryland-highlight.md) |
| `maryland-summary-box` | MDWDS | Maryland-styled summary box for quick recaps. | Tops of long pages. | [maryland-summary-box.md](components/maryland-summary-box.md) |
| `usa-summary-box` | USWDS | The USWDS summary box. | Prefer `maryland-summary-box` on Maryland pages. | [usa-summary-box.md](components/usa-summary-box.md) |
| `maryland-alert` | MDWDS | Maryland-styled alert (info/warning/error/success/emergency). | Page-level or global alerts. **Use this, not `usa-alert`, on Maryland pages.** | [maryland-alert.md](components/maryland-alert.md) |
| `usa-alert` | USWDS | The USWDS alert. | Internal tools where Maryland theming is undesirable. | [usa-alert.md](components/usa-alert.md) |
| `usa-site-alert` | USWDS | Full-width site-wide alert strip (different from `usa-alert`). | Statewide notices (typically the "global alert" slot between banner and header). | [usa-site-alert.md](components/usa-site-alert.md) |
| `maryland-action-items` | MDWDS | Vertical list of "do this next" actions with icons. | Service-completion checklists. | [maryland-action-items.md](components/maryland-action-items.md) |
| `maryland-step-list` | MDWDS | Visual numbered step-by-step process. | "How to apply" type pages. | [maryland-step-list.md](components/maryland-step-list.md) |
| `usa-process-list` | USWDS | Vertical numbered process list (different visual from step-list). | Step-by-step process instructions in USWDS-style flow. | [usa-process-list.md](components/usa-process-list.md) |
| `maryland-statistic-list` | MDWDS | Large-number statistics display. | Impact-data sections, dashboards. | [maryland-statistic-list.md](components/maryland-statistic-list.md) |
| `maryland-icon-list` | MDWDS | Icon-prefixed bullet list. | Feature lists with visual prefix. | [maryland-icon-list.md](components/maryland-icon-list.md) |
| `usa-icon-list` | USWDS | Icon list (USWDS markup). | Prefer `maryland-icon-list` on Maryland pages. | [usa-icon-list.md](components/usa-icon-list.md) |
| `maryland-link-collection` | MDWDS | Grouped list of related links with optional descriptions. | "More resources" sections. | [maryland-link-collection.md](components/maryland-link-collection.md) |
| `maryland-visual-link-collection` | MDWDS | Link collection with visual styling (cards-lite). | Service-directory pages. | [maryland-visual-link-collection.md](components/maryland-visual-link-collection.md) |
| `maryland-automatic-list` | MDWDS | Auto-generated list from page sections (e.g., for `<h2>`s). | Dynamic page-section TOC. | [maryland-automatic-list.md](components/maryland-automatic-list.md) |
| `maryland-social-media` | MDWDS | Row of social-media icon links. | Inside footer or "Connect with us" sections. | [maryland-social-media.md](components/maryland-social-media.md) |

## Interactive

| Component | Source | What it is | When to use | Reference |
|---|---|---|---|---|
| `maryland-accordion` | MDWDS | Maryland-styled accordion. | FAQs, collapsible sections. **Use this, not `usa-accordion`, on Maryland pages.** | [maryland-accordion.md](components/maryland-accordion.md) |
| `usa-accordion` | USWDS | The USWDS accordion. | Where Maryland theming is undesirable. | [usa-accordion.md](components/usa-accordion.md) |
| `usa-modal` | USWDS | Dialog/modal. | Confirmations, forms-in-overlay. | [usa-modal.md](components/usa-modal.md) |
| `usa-tooltip` | USWDS | Hover/focus tooltip. | Inline help text on form fields. | [usa-tooltip.md](components/usa-tooltip.md) |

## Forms

| Component | Source | What it is | When to use | Reference |
|---|---|---|---|---|
| `usa-form` | USWDS | Form wrapper with built-in spacing. | Wraps all form fields. | [usa-form.md](components/usa-form.md) |
| `usa-input` | USWDS | Text input. | Single-line text fields. | [usa-input.md](components/usa-input.md) |
| `usa-textarea` | USWDS | Multi-line text input. | Long-form input. | [usa-textarea.md](components/usa-textarea.md) |
| `usa-select` | USWDS | Native `<select>` dropdown. | Simple option list. | [usa-select.md](components/usa-select.md) |
| `usa-combo-box` | USWDS | Searchable dropdown with autocomplete. | Long option lists. | [usa-combo-box.md](components/usa-combo-box.md) |
| `usa-radio` | USWDS | Radio buttons. | Mutually exclusive choice. | [usa-radio.md](components/usa-radio.md) |
| `usa-checkbox` | USWDS | Checkboxes. | Multi-select. | [usa-checkbox.md](components/usa-checkbox.md) |
| `usa-file-input` | USWDS | File upload control. | File uploads. | [usa-file-input.md](components/usa-file-input.md) |
| `usa-date-picker` | USWDS | Date input with calendar popup. | Single date selection. | [usa-date-picker.md](components/usa-date-picker.md) |
| `usa-date-range-picker` | USWDS | Two date pickers for ranges. | From-to date selection. | [usa-date-range-picker.md](components/usa-date-range-picker.md) |
| `usa-time-picker` | USWDS | Time-of-day input. | Appointment scheduling. | [usa-time-picker.md](components/usa-time-picker.md) |
| `usa-memorable-date` | USWDS | Three-field MM/DD/YYYY input. | Date inputs without a picker (memorable dates like birthdays). | [usa-memorable-date.md](components/usa-memorable-date.md) |
| `usa-input-mask` | USWDS | Masked input with format guides. | Phone, SSN, ZIP. | [usa-input-mask.md](components/usa-input-mask.md) |
| `usa-input-prefix-suffix` | USWDS | Input with leading/trailing icon or text. | Currency, percentages, search-icon inputs. | [usa-input-prefix-suffix.md](components/usa-input-prefix-suffix.md) |
| `usa-character-count` | USWDS | Character-count helper for inputs. | Inputs with max length. | [usa-character-count.md](components/usa-character-count.md) |
| `usa-range-slider` | USWDS | Numeric range slider. | Settings, filters. | [usa-range-slider.md](components/usa-range-slider.md) |
| `usa-validation` | USWDS | Form validation messages. | Inline form errors. | [usa-validation.md](components/usa-validation.md) |
| `usa-step-indicator` | USWDS | Multi-step form progress. | Multi-page forms. | [usa-step-indicator.md](components/usa-step-indicator.md) |
| `maryland-search-form` | MDWDS | The Maryland search form (used at top of pages). | Site search entry point. | [maryland-search-form.md](components/maryland-search-form.md) |
| `usa-search` | USWDS | The USWDS search form. | Prefer `maryland-search-form` on Maryland pages. | [usa-search.md](components/usa-search.md) |

## Buttons & links

| Component | Source | What it is | When to use | Reference |
|---|---|---|---|---|
| `usa-button` | USWDS | Standard button. Eight variants (default, secondary, accent-cool, accent-warm, base, white, black, outline). | All buttons. | [usa-button.md](components/usa-button.md) |
| `usa-button-group` | USWDS | Group of related buttons. | Adjacent button rows. | [usa-button-group.md](components/usa-button-group.md) |
| `maryland-button-group` | MDWDS | Maryland-styled button group. | Where Maryland-specific button grouping is needed. | [maryland-button-group.md](components/maryland-button-group.md) |
| `maryland-link` | MDWDS | Maryland-styled link element with variants (skipnav, labelled). | Used internally by other components; rarely standalone. | [maryland-link.md](components/maryland-link.md) |
| `usa-link` | USWDS | The USWDS link helper. | Inline external links with icon. | [usa-link.md](components/usa-link.md) |
| `usa-tag` | USWDS | Pill-shaped tag/label. | Categories, status. | [usa-tag.md](components/usa-tag.md) |

## Data

| Component | Source | What it is | When to use | Reference |
|---|---|---|---|---|
| `maryland-table` | MDWDS | Maryland-styled data table. | Most data tables on Maryland pages. | [maryland-table.md](components/maryland-table.md) |
| `usa-table` | USWDS | USWDS table. | Internal tools, less brand-styled contexts. | [usa-table.md](components/usa-table.md) |
| `usa-list` | USWDS | Bulleted/numbered list helper classes. | Custom-styled lists where `usa-prose` defaults aren't enough. | [usa-list.md](components/usa-list.md) |
| `usa-data-visualizations` | USWDS | Chart helpers (axis styles, etc.). | Charts and graphs. | [usa-data-visualizations.md](components/usa-data-visualizations.md) |

## Utility

| Component | Source | What it is | When to use | Reference |
|---|---|---|---|---|
| `usa-icon` | USWDS | Inline SVG icon helper. | Standalone icons in body content. | [usa-icon.md](components/usa-icon.md) |
| `usa-typography` | USWDS | Typography utility classes (`text-bold`, `font-heading-*`, etc.). | Typography fine-tuning. | [usa-typography.md](components/usa-typography.md) |
| `usa-grid` | USWDS | The 12-column grid system. | All layout. See `cdn/composition.md`. | [usa-grid.md](components/usa-grid.md) |
| `usa-language-selector` | USWDS | Language switcher dropdown. | Multi-language sites. | [usa-language-selector.md](components/usa-language-selector.md) |
| `maryland-placeholder` | MDWDS | Placeholder block for in-progress design. | Wireframes, prototypes. **Not** for production. | [maryland-placeholder.md](components/maryland-placeholder.md) |
| `maryland-listing-page` | MDWDS | Listing page wrapper (filters + collection + pagination). | Use the `cdn/recipes/listing-page.md` recipe instead — it composes this with the page shell. | [maryland-listing-page.md](components/maryland-listing-page.md) |

## Disambiguation summary — pick one

| Use case | The right choice | Why |
|---|---|---|
| Standard service card on a Maryland page | `maryland-card` | Designed for Maryland visual style; supports the variants the design system expects |
| Vertical list of news/articles | `usa-collection` | The collection component handles the metadata, dates, tags, and images well. There is no `maryland-collection`. |
| Site-wide top banner | `usa-banner` (with `aria-label="Official website of the State of Maryland"`) | The state-required statewide banner. The `<maryland-statewide-banner>` web component is for embedding in non-MDWDS sites. |
| Site footer | `maryland-footer` for agency info + `<maryland-statewide-footer>` for state services | Both go on the page; agency above statewide. |
| Top-of-page alert | `maryland-alert` | Maryland-themed colors |
| Statewide notice strip between banner and header | `usa-site-alert` (or `maryland-alert` rendered full-width) | Either works; `usa-site-alert` is the canonical "site-wide" alert pattern |
| FAQ-style collapsible | `maryland-accordion` | Maryland visual styling |
| Sidebar nav for a documentation section | `maryland-sidenav` | Maryland visual styling |
| Breadcrumbs at top of inner page | `maryland-breadcrumb` (often nested inside hero) | Maryland visual styling |
| Buttons | `usa-button` | No `maryland-button` — USWDS handles this; CDN colors are themed |
| Site search bar (in header) | `maryland-search-form` | Maryland-specific form structure |
| Tabular data | `maryland-table` | Maryland visual styling |

## What's NOT a component

- **Skip link** (`a.usa-skipnav`) — it's a single class on an `<a>`, not a component file. See `cdn/page-shell.md`.
- **Grid layout** (`grid-container`, `grid-row`, `grid-col-*`) — utilities, not components. See `cdn/composition.md`.
- **Prose styling** (`usa-prose`) — a wrapper class, not a component. See `cdn/composition.md`.
- **Spacing utilities** (`margin-y-*`, `block-spacing`, etc.) — see `cdn/composition.md`.
- **Color utilities** (`text-primary`, `bg-base-lightest`) — see `cdn/foundation.md`.
