# JSON-LD Hook for IDP Software

This custom MkDocs hook automatically generates appropriate JSON-LD structured data for different page types across the site.

## Purpose

The hook generates SEO-optimized structured data that helps search engines understand your content better, potentially improving search visibility and rich snippet display.

## How It Works

The hook analyzes the URL pattern of each page and generates the appropriate schema.org type:

### Page Type Detection

| URL Pattern | Schema Type | Description |
|------------|-------------|-------------|
| `/vendors/*/index.html` | `Organization` | Vendor profile pages with company information |
| `/vendors/*/YYYY-MM-DD/` | `NewsArticle` | Vendor news aggregation pages (e.g., `/vendors/abbyy/2025-10-02/`) |
| `/capabilities/*` | `TechArticle` | Technical documentation and capability pages |
| `/about/*`, `/events/*` | `WebPage` | General information pages |
| Other pages | `Article` | Default for content pages |

**Note:** The NewsArticle pattern matches all URL formats: `2025-08-03.html`, `2025-08-03/`, and `2025-08-03/index.html`

### Author Attribution

All pages use **"IDP Software"** as the default Organization author, as specified in Google's best practices for structured data.

The actual contributors are still displayed in the page footer via the Ultralytics plugin's git author tracking.

## Schema Details

### NewsArticle Schema

For vendor news pages (`vendors/*/YYYY-MM-DD.html`):

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "Abbyy News: 2025-09-04 to 2025-10-02",
  "url": "https://idp-software.com/vendors/abbyy/2025-10-02/",
  "datePublished": "2025-10-02 14:23:15 +0000",
  "dateModified": "2025-10-15 09:42:31 +0000",
  "author": [{
    "@type": "Organization",
    "name": "IDP Software",
    "url": "https://idp-software.com"
  }],
  "publisher": {...},
  "about": {
    "@type": "Organization",
    "name": "Abbyy",
    "url": "https://idp-software.com/vendors/abbyy/"
  },
  "description": "Summary from page meta",
  "image": ["https://..."],
  "articleSection": "vendor-news",
  "keywords": "news, vendor, abbyy"
}
```

**Enhanced Features:**
- **`about` property**: Links the news article directly to the vendor Organization page
  - This tells search engines "this news is about Company XYZ"
  - Creates a clear semantic relationship between news and vendor
  - Helps with entity recognition and knowledge graph building
- **Headline Generation**: Includes vendor name for better SEO context
  - Format: `"{Vendor Name} News: {Title}"` or `"{Vendor Name}: {Summary}"`
  - Falls back to page title if vendor name is already in title

### Organization Schema

For vendor profile pages (`vendors/*/index.html`):

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "ABBYY",
  "url": "https://idp-software.com/vendors/abbyy/",
  "description": "Company description",
  "logo": "https://...",
  "image": "https://...",
  "sameAs": ["https://www.abbyy.com/"],
  "email": "office@abbyy.com",
  "telephone": "(408) 457-9777",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "600 Congress Ave., Suite 15015",
    "addressLocality": "Texas",
    "addressCountry": "United States"
  }
}
```

**Enhanced Features:**
- Automatically extracts company website, email, phone, and address from "Company Information" section
- Links to actual company website via `sameAs` property
- Includes full contact information for better local SEO

### TechArticle Schema

For capability/technical pages (`capabilities/*`):

```json
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "Data Extraction",
  "url": "https://idp-software.com/capabilities/extraction",
  "datePublished": "2025-10-22",
  "author": [{...}],
  "publisher": {...},
  "description": "...",
  "keywords": "..."
}
```

### WebPage Schema

For general pages (`about/*`, `events/*`):

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "About",
  "url": "https://idp-software.com/about",
  "publisher": {...},
  "description": "..."
}
```

## Metadata Usage

The hook reads metadata from your markdown frontmatter:

```yaml
---
title: "2025-09-04 to 2025-10-02"
date: 2025-10-02
summary: "Recent news and updates about abbyy"
tags: ["news", "vendor", "abbyy"]
categories: ["vendor-news"]
---
```

**Metadata mapping:**
- `title` → `headline` / `name`
- Git first commit date → `datePublished`
- Git last commit date → `dateModified`
- `description` or `summary` → `description` / `abstract`
- `image` → `image` (from Ultralytics plugin)
- `tags` → `keywords`
- `categories[0]` → `articleSection`

**Important:** The `datePublished` and `dateModified` fields are automatically retrieved from git history:
- `datePublished`: Full datetime with timezone of the **first git commit** for the file (when it was created)
- `dateModified`: Full datetime with timezone of the **last git commit** for the file (when it was last changed)
- Format: `"YYYY-MM-DD HH:MM:SS +TIMEZONE"` (e.g., `"2025-05-24 23:37:41 +0200"`)
- This ISO 8601 format is preferred by Google and other search engines for better datetime precision

## Configuration

The hook is registered in `mkdocs.yml`:

```yaml
hooks:
  - hooks/jsonld_hook.py

plugins:
  - ultralytics:
      add_json_ld: False  # Disabled - using custom hook instead
```

## Benefits

1. **Better SEO**: Search engines understand your content structure
2. **Rich Snippets**: Potential for enhanced search results display
3. **News Optimization**: NewsArticle schema helps with Google News indexing
4. **Accurate Attribution**: Organization-level authorship is transparent and compliant
5. **Automated**: No manual YAML metadata required per page
6. **Entity Linking**: The `about` property creates semantic connections between content and organizations
7. **Knowledge Graph**: Helps search engines build accurate knowledge graphs for each vendor
8. **Local SEO**: Full address and contact information improves local search visibility
9. **Vendor Disambiguation**: Clear relationships help differentiate between similar company names

## How It Helps Search Engines

### Entity Recognition
The `about` property in NewsArticle explicitly tells search engines:
- "This content is about Organization X"
- Links the article to the vendor's profile page
- Helps build entity relationships in knowledge graphs

### Organization Details
For vendor pages, the full Organization schema provides:
- **`sameAs`**: Links to the actual company website (crucial for entity merging)
- **Contact info**: Email, phone, address for better local search
- **Structured data**: Helps Google understand this is a real business entity

### Example Benefits:
- When someone searches "ABBYY news", your vendor news pages rank better
- Google can show rich snippets with company information
- Knowledge panels may include your vendor directory information
- Better disambiguation between vendors with similar names

## Validation

Test your JSON-LD with:
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org Validator](https://validator.schema.org/)
- Browser Dev Tools → View Page Source → Search for `application/ld+json`

## References

- [Schema.org Article](https://schema.org/Article)
- [Schema.org NewsArticle](https://schema.org/NewsArticle)
- [Schema.org Organization](https://schema.org/Organization)
- [Google Structured Data Guidelines](https://developers.google.com/search/docs/appearance/structured-data/article)
