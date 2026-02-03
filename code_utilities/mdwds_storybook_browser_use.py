import asyncio
import os
import sys
from datetime import datetime
from typing import List, Optional
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from browser_use import Agent, Controller, ChatGoogle, Tools

# Reconfigure stdout to always use utf-8
sys.stdout.reconfigure(encoding='utf-8')

os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Load environment variables (Expects GOOGLE_API_KEY)
load_dotenv()

# --- Configuration ---
STORYBOOK_URL = "https://designsystem.maryland.gov/"
OUTPUT_FILE = "mdwds_skill_document.md"
BROWSING_MODEL = "gemini-3-flash-preview"

# ------------------------------------------------------------------
# Data Models
# ------------------------------------------------------------------

class ComponentDocumentation(BaseModel):
    """Documentation for a single MDWDS component."""
    name: str = Field(..., description="Name of the component")
    category: str = Field(..., description="Category: Foundation, Components, Templates, or Utilities")
    description: str = Field(default="", description="Description of what the component does")
    html_code: str = Field(default="", description="HTML code example for the component")
    css_classes: List[str] = Field(default_factory=list, description="CSS classes used by the component")
    variants: List[str] = Field(default_factory=list, description="Different variants or states of the component")
    usage_notes: str = Field(default="", description="Notes on how to use the component")
    accessibility_notes: str = Field(default="", description="Accessibility considerations")

class MDWDSDocumentation(BaseModel):
    """Complete MDWDS documentation structure."""
    version: str = Field(default="", description="Current MDWDS version")
    cdn_css_url: str = Field(default="", description="CDN URL for CSS")
    cdn_js_url: str = Field(default="", description="CDN URL for JavaScript")
    getting_started: str = Field(default="", description="Getting started instructions")
    foundation_docs: List[ComponentDocumentation] = Field(default_factory=list)
    component_docs: List[ComponentDocumentation] = Field(default_factory=list)
    template_docs: List[ComponentDocumentation] = Field(default_factory=list)
    utility_docs: List[ComponentDocumentation] = Field(default_factory=list)


# ------------------------------------------------------------------
# Markdown Generator
# ------------------------------------------------------------------

def generate_markdown(docs: MDWDSDocumentation) -> str:
    """Generate a comprehensive markdown skill document from the scraped documentation."""
    
    md = []
    
    # Header
    md.append("# Maryland Web Design System (MDWDS) - LLM Skill Document")
    md.append("")
    md.append(f"*Generated on {datetime.now().strftime('%Y-%m-%d')}*")
    md.append("")
    md.append("## Overview")
    md.append("")
    md.append("The Maryland Web Design System (MDWDS) is a design system for building Maryland state government websites. This document provides comprehensive guidance on using MDWDS components via CDN.")
    md.append("")
    
    # Getting Started
    md.append("## Getting Started")
    md.append("")
    md.append("### CDN Setup")
    md.append("")
    md.append("**IMPORTANT:** The version number in CDN URLs should NOT include the `v` prefix, even though version tags may show it.")
    md.append("")
    md.append("Include the following in your HTML `<head>`:")
    md.append("")
    md.append("```html")
    md.append(f'<link rel="stylesheet" href="{docs.cdn_css_url}">')
    md.append(f'<script src="{docs.cdn_js_url}" defer></script>')
    md.append("```")
    md.append("")
    
    if docs.getting_started:
        md.append("### Additional Setup Notes")
        md.append("")
        md.append(docs.getting_started)
        md.append("")
    
    # Foundation
    if docs.foundation_docs:
        md.append("## Foundation")
        md.append("")
        md.append("Foundation elements define the core visual language of MDWDS including colors, typography, spacing, and grid systems.")
        md.append("")
        
        for item in docs.foundation_docs:
            md.append(f"### {item.name}")
            md.append("")
            if item.description:
                md.append(item.description)
                md.append("")
            if item.html_code:
                md.append("```html")
                md.append(item.html_code)
                md.append("```")
                md.append("")
            if item.css_classes:
                md.append("**CSS Classes:**")
                for cls in item.css_classes:
                    md.append(f"- `{cls}`")
                md.append("")
            if item.variants:
                md.append("**Variants:**")
                for variant in item.variants:
                    md.append(f"- {variant}")
                md.append("")
            if item.usage_notes:
                md.append("**Usage Notes:**")
                md.append(item.usage_notes)
                md.append("")
            if item.accessibility_notes:
                md.append("**Accessibility:**")
                md.append(item.accessibility_notes)
                md.append("")
    
    # Components
    if docs.component_docs:
        md.append("## MDWDS Components")
        md.append("")
        md.append("Components are reusable UI elements that can be combined to build pages.")
        md.append("")
        
        for item in docs.component_docs:
            md.append(f"### {item.name}")
            md.append("")
            if item.description:
                md.append(item.description)
                md.append("")
            if item.html_code:
                md.append("```html")
                md.append(item.html_code)
                md.append("```")
                md.append("")
            if item.css_classes:
                md.append("**CSS Classes:**")
                for cls in item.css_classes:
                    md.append(f"- `{cls}`")
                md.append("")
            if item.variants:
                md.append("**Variants:**")
                for variant in item.variants:
                    md.append(f"- {variant}")
                md.append("")
            if item.usage_notes:
                md.append("**Usage Notes:**")
                md.append(item.usage_notes)
                md.append("")
            if item.accessibility_notes:
                md.append("**Accessibility:**")
                md.append(item.accessibility_notes)
                md.append("")
    
    # Templates
    if docs.template_docs:
        md.append("## Templates")
        md.append("")
        md.append("Templates are pre-built page layouts combining multiple components.")
        md.append("")
        
        for item in docs.template_docs:
            md.append(f"### {item.name}")
            md.append("")
            if item.description:
                md.append(item.description)
                md.append("")
            if item.html_code:
                md.append("```html")
                md.append(item.html_code)
                md.append("```")
                md.append("")
            if item.usage_notes:
                md.append("**Usage Notes:**")
                md.append(item.usage_notes)
                md.append("")
    
    # Utilities
    if docs.utility_docs:
        md.append("## Utilities")
        md.append("")
        md.append("Utility classes for common styling needs.")
        md.append("")
        
        for item in docs.utility_docs:
            md.append(f"### {item.name}")
            md.append("")
            if item.description:
                md.append(item.description)
                md.append("")
            if item.html_code:
                md.append("```html")
                md.append(item.html_code)
                md.append("```")
                md.append("")
            if item.css_classes:
                md.append("**CSS Classes:**")
                for cls in item.css_classes:
                    md.append(f"- `{cls}`")
                md.append("")
            if item.usage_notes:
                md.append("**Usage Notes:**")
                md.append(item.usage_notes)
                md.append("")
    
    # Best Practices
    md.append("## Best Practices")
    md.append("")
    md.append("1. **Always use the CDN** - Use the official Maryland CDN for CSS and JS files")
    md.append("2. **Version pinning** - Pin to a specific version to avoid breaking changes")
    md.append("3. **Semantic HTML** - Use appropriate HTML5 semantic elements")
    md.append("4. **Accessibility** - Follow WCAG 2.1 AA guidelines")
    md.append("5. **Mobile-first** - MDWDS is designed mobile-first; test on all screen sizes")
    md.append("6. **Component composition** - Combine components as documented; avoid custom overrides")
    md.append("")
    
    return "\n".join(md)


# ------------------------------------------------------------------
# Browser-Use Agent for Scraping
# ------------------------------------------------------------------

async def scrape_mdwds_documentation(llm) -> MDWDSDocumentation:
    """
    Uses Browser-Use Agent to comprehensively scrape the MDWDS Storybook.
    """
    print("Starting MDWDS Documentation Scraper...")
    
    # Container for collected documentation
    collected_docs = MDWDSDocumentation()
    
    # Initialize tools for streaming extraction
    tools = Tools()
    
    @tools.action("Save Getting Started Info")
    def save_getting_started(version: str, cdn_css_url: str, cdn_js_url: str, instructions: str):
        """
        Save the getting started information including CDN URLs.
        Args:
            version: Current MDWDS version number (without 'v' prefix)
            cdn_css_url: Full CDN URL for the CSS file
            cdn_js_url: Full CDN URL for the JavaScript file  
            instructions: Additional setup instructions
        """
        collected_docs.version = version
        collected_docs.cdn_css_url = cdn_css_url
        collected_docs.cdn_js_url = cdn_js_url
        collected_docs.getting_started = instructions
        print(f"  + Saved Getting Started (Version: {version})")
        return "Getting started info saved. Continue to Foundation section."

    @tools.action("Save Foundation Item")
    def save_foundation_item(
        name: str,
        description: str = "",
        html_code: str = "",
        css_classes: List[str] = [],
        variants: List[str] = [],
        usage_notes: str = "",
        accessibility_notes: str = ""
    ):
        """
        Save a Foundation documentation item (colors, typography, spacing, grid, etc).
        """
        item = ComponentDocumentation(
            name=name,
            category="Foundation",
            description=description,
            html_code=html_code,
            css_classes=css_classes,
            variants=variants,
            usage_notes=usage_notes,
            accessibility_notes=accessibility_notes
        )
        collected_docs.foundation_docs.append(item)
        print(f"  + Saved Foundation: {name}")
        return f"Foundation item '{name}' saved. Continue documenting."

    @tools.action("Save Component")
    def save_component(
        name: str,
        description: str = "",
        html_code: str = "",
        css_classes: List[str] = [],
        variants: List[str] = [],
        usage_notes: str = "",
        accessibility_notes: str = ""
    ):
        """
        Save an MDWDS Component documentation item.
        """
        item = ComponentDocumentation(
            name=name,
            category="Components",
            description=description,
            html_code=html_code,
            css_classes=css_classes,
            variants=variants,
            usage_notes=usage_notes,
            accessibility_notes=accessibility_notes
        )
        collected_docs.component_docs.append(item)
        print(f"  + Saved Component: {name}")
        return f"Component '{name}' saved. Continue documenting."

    @tools.action("Save Template")
    def save_template(
        name: str,
        description: str = "",
        html_code: str = "",
        css_classes: List[str] = [],
        variants: List[str] = [],
        usage_notes: str = "",
        accessibility_notes: str = ""
    ):
        """
        Save a Template documentation item.
        """
        item = ComponentDocumentation(
            name=name,
            category="Templates",
            description=description,
            html_code=html_code,
            css_classes=css_classes,
            variants=variants,
            usage_notes=usage_notes,
            accessibility_notes=accessibility_notes
        )
        collected_docs.template_docs.append(item)
        print(f"  + Saved Template: {name}")
        return f"Template '{name}' saved. Continue documenting."

    @tools.action("Save Utility")
    def save_utility(
        name: str,
        description: str = "",
        html_code: str = "",
        css_classes: List[str] = [],
        variants: List[str] = [],
        usage_notes: str = "",
        accessibility_notes: str = ""
    ):
        """
        Save a Utility class documentation item.
        """
        item = ComponentDocumentation(
            name=name,
            category="Utilities",
            description=description,
            html_code=html_code,
            css_classes=css_classes,
            variants=variants,
            usage_notes=usage_notes,
            accessibility_notes=accessibility_notes
        )
        collected_docs.utility_docs.append(item)
        print(f"  + Saved Utility: {name}")
        return f"Utility '{name}' saved. Continue documenting."

    task = f"""
    You are a documentation extraction agent for the Maryland Web Design System (MDWDS).
    
    Your goal is to create a comprehensive skill document for LLMs on how to build pages with MDWDS using the CDN.

    1. Go to {STORYBOOK_URL}

    2. **Read "Getting Started" page first:**
       - Click "Getting Started" in the sidebar
       - Find the current version number
       - IMPORTANT: The page may show version tags with a 'v' prefix, but CDN URLs must NOT include it
       - Correct CDN format: https://cdn.maryland.gov/mdwds/0.35.0/css/mdwds.min.css
       - Call `Save Getting Started Info` with the version (without 'v'), correct CDN URLs, and setup instructions

    3. **Document the FOUNDATION section:**
       - Click the arrow next to "FOUNDATION" to expand it
       - You will see: Block Spacing, Colors, Logo, Typography
       - For each item and sub-item:
         * Click to view it
         * If the page has a "Show code" button, click it to reveal HTML. Otherwise read the documentation on the page
         * Call `Save Foundation Item` with all details

    4. **Document the MDWDS COMPONENTS section:**
       - Click the arrow next to "MDWDS COMPONENTS" to expand it
       - Components include: Accordion, Action Items, Alert, Automatic List, Breadcrumb, Callout, Cards, Footer, Header, Hero, Highlight, LinkCollection, Links, Listing Page, Navigation, Promo, Search, Side Navigation, Statewide Banner, Statewide Footer, Summary Box, Table of Contents, Utility Nav, Video Promo, Visual Link Collection
       - Many components have sub-items (e.g., Action Items has: Docs, Featured Actions, Action Spotlight, Action Group, Action Hero, Action Page Contents)
       - For EACH component and its sub-items:
         * Click to view it
         * If the page has a "Show code" button, click it to reveal HTML. Otherwise read the documentation on the page
         * Call `Save Component` with all details including code

    5. **Document the TEMPLATES section:**
       - Click the arrow next to "TEMPLATES" to expand it
       - Under "Page" you will find: Maryland Homepage, Action Page, Agency Homepage, Basic Page, Landing Page, Listing Page, Location Page, News Page, Search Page
       - For each template:
         * Click to view it
         * If the page has a "Show code" button, click it to reveal HTML. Otherwise read the documentation on the page
         * Call `Save Template` with all details

    6. **Document the UTILITIES section:**
       - Click the arrow next to "UTILITIES" to expand it
       - Under "Layout Grid" you will find: Docs, Three Columns, Numeric Width, Auto Fill, Responsive Mix, Offset, Gutters
       - For each utility:
         * Click to view it
         * If the page has a "Show code" button, click it to reveal HTML. Otherwise read the documentation on the page
         * Call `Save Utility` with all details

    7. **For EVERY page you visit:**
       - Always look for and click "Show code" button when it exists to reveal HTML examples
       - Copy the complete HTML code shown
       - Note all CSS classes used
       - Read any usage notes or guidelines

    8. When you have documented ALL sections and sub-sections completely, finish the task.
    """

    agent = Agent(
        task=task,
        llm=llm,
        tools=tools,
        controller=Controller(),
        use_vision=True
    )

    try:
        await agent.run(max_steps=500)  # High step limit for comprehensive scraping
        print(f"\nScraping complete!")
        print(f"  - Foundation items: {len(collected_docs.foundation_docs)}")
        print(f"  - Components: {len(collected_docs.component_docs)}")
        print(f"  - Templates: {len(collected_docs.template_docs)}")
        print(f"  - Utilities: {len(collected_docs.utility_docs)}")
        
        return collected_docs
        
    except Exception as e:
        print(f"Error during scraping: {e}")
        # Return what we collected so far
        return collected_docs


# ------------------------------------------------------------------
# Main Execution
# ------------------------------------------------------------------

async def run():
    """Main execution function."""
    print("=" * 60)
    print("MDWDS Documentation Scraper")
    print("=" * 60)
    
    # Initialize LLM
    llm = ChatGoogle(model=BROWSING_MODEL)
    
    # Scrape the documentation
    docs = await scrape_mdwds_documentation(llm)
    
    # Generate markdown
    print("\nGenerating Markdown document...")
    markdown_content = generate_markdown(docs)
    
    # Save to file
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"\nSkill document saved to: {OUTPUT_FILE}")
    print(f"Document length: {len(markdown_content)} characters")
    
    # Also print a summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Version: {docs.version}")
    print(f"CSS CDN: {docs.cdn_css_url}")
    print(f"JS CDN: {docs.cdn_js_url}")
    print(f"Foundation items documented: {len(docs.foundation_docs)}")
    print(f"Components documented: {len(docs.component_docs)}")
    print(f"Templates documented: {len(docs.template_docs)}")
    print(f"Utilities documented: {len(docs.utility_docs)}")


if __name__ == "__main__":
    asyncio.run(run())