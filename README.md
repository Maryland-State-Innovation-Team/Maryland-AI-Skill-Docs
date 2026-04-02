# Maryland AI Skill Docs

Skill documents for the Maryland State Innovation Team. Each file is a Markdown document written for LLMs — attach it to a conversation to give the model the knowledge and patterns needed to complete a specific task correctly on the first try.

## Skill Documents

### `mdwds_skill_document.md` — Maryland Web Design System (MDWDS)

Enables LLMs to build Maryland state government web pages using the [Maryland Web Design System](https://designsystem.maryland.gov/) via CDN. Covers all 107 documented components including the full page shell structure, `maryland-*` web components, `usa-*` USWDS-inherited classes, layout grid, templates, and accessibility requirements.

Generated automatically by the scraper in `code_utilities/mdwds_storybook_scraper.py`, which crawls the live MDWDS Storybook, extracts real rendered HTML from component iframes, and synthesizes the document using Claude on AWS Bedrock.

**Example prompt:**
```
Use the attached skill document to build a Maryland state agency homepage with a hero section, three feature cards, and a news listing.
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

## `code_utilities/`

Scripts that generate or maintain the skill documents above.

- **`mdwds_storybook_scraper.py`** — Three-phase Playwright + Bedrock pipeline for regenerating `mdwds_skill_document.md`. Discovers all Storybook component pages, scrapes real rendered HTML from component iframes, runs per-page extraction with Claude Haiku, then synthesizes a holistic intro with Claude Sonnet. Results are cached so phases can be re-run independently.

- **`mdwds_storybook_browser_use.py`** — Earlier browser-use/Gemini approach, superseded by `mdwds_storybook_scraper.py`.

### Regenerating the MDWDS skill document

```bash
# First-time setup
python -m venv .venv && source .venv/bin/activate
pip install "anthropic[bedrock]" playwright pydantic python-dotenv
playwright install chromium

# Run (AWS credentials with Bedrock access required)
python code_utilities/mdwds_storybook_scraper.py
```

Cache files are written to `code_utilities/`:
- Delete `mdwds_scraped_pages.json` to re-crawl the Storybook
- Delete `mdwds_extracted_pages.json` to re-run per-page extraction
- Delete neither to re-run synthesis only

---

## License

See [LICENSE](LICENSE) for details.
