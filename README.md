# Maryland AI Skill Docs

Skill documents for the Maryland State Innovation Team. Each one gives an LLM the knowledge and patterns needed to complete a specific Maryland-government task correctly on the first try.

## Skills

### `mdwds-skill/` — Maryland Web Design System (MDWDS)

An installable [Anthropic Agent Skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) for building Maryland state government web pages with the [Maryland Web Design System](https://designsystem.maryland.gov/). Covers CDN setup, the full page shell, every documented `maryland-*` and `usa-*` component, and page-template recipes (agency homepage, landing, listing, basic, news, location, action, search).

Structure:

```
mdwds-skill/
├── SKILL.md                    # Index + auto-trigger frontmatter
└── cdn/
    ├── setup.md                # CDN tags, init script, FOUC
    ├── page-shell.md           # Required top-to-bottom shell
    ├── composition.md          # Headings, spacing, grid, prose
    ├── foundation.md           # Colors, typography, tokens
    ├── component-index.md      # Lookup table with maryland-/usa- disambiguation
    ├── components/*.md         # 78 component reference files
    └── recipes/*.md            # 9 full assembled page templates
```

Each component file documents what the component looks like (real pixel values, colors, breakpoint behavior), every variant's markup, what each class visually does, the prop schema, heading-level guidance, and common mistakes — so the LLM can picture the component before writing markup, instead of reaching for inline `<style>` blocks.

Pinned to MDWDS v0.47.4. CDN consumers should pin to the current stable version (see `mdwds-skill/cdn/setup.md`).

**Install locally:** copy or symlink `mdwds-skill/` into `.claude/skills/` (project-scoped) or `~/.claude/skills/` (user-scoped). Once installed, Claude auto-loads it when a prompt mentions building a Maryland.gov page, MDWDS, or any of the `maryland-*` components.

**Example prompt:**
```
Build me a Maryland state agency homepage with a hero section, three feature cards, and a news listing. The agency is the Department of Natural Resources.
```

---

### `imap_boundaries.md` — Maryland iMap Geospatial Boundary Data

Enables LLMs to fetch and use Maryland's official geospatial boundary data (GeoJSON) from the Maryland iMap ArcGIS FeatureServer. Covers counties, municipalities, legislative districts, ZIP codes, and other administrative boundaries.

**Example prompt:**
```
Use the attached context to create a map of Maryland legislative districts. When I click on a district I want to learn the legislator's name.
```

---

### `imap_geocoder.md` — Maryland iMap Geocoding Service

Enables LLMs to geocode Maryland addresses using the official Maryland iMap REST geocoding service. Covers address lookup, batch geocoding, response parsing, and map rendering.

**Example prompt:**
```
List 15 real addresses around the state of Maryland, then use the attached context to build an interactive map of their locations.
```

---

### `socrata_api.md` — Socrata Open Data APIs

Enables LLMs to query and visualize data from Socrata-powered open data portals (opendata.maryland.gov, data.cdc.gov, and others). Covers the SoQL query language, filtering, pagination, and building dashboards from API responses.

**Example prompt:**
```
Build me a dashboard using this context and this data URL: https://opendata.maryland.gov/resource/9qyj-bhez.json
```

---

## License

See [LICENSE](LICENSE) for details.
