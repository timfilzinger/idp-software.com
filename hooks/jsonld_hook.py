"""
Custom MkDocs hook for generating JSON-LD structured data.

This hook generates appropriate JSON-LD schema based on page URL patterns:
- /vendors/*/index.md → Organization + Product schema
- /vendors/*/2025-*.md → NewsArticle schema
- /capabilities/* → TechArticle schema
- /about/*, /events/* → WebPage schema
"""

import json
import re
import subprocess
from datetime import datetime, date, timezone
from pathlib import Path
from subprocess import check_output
from bs4 import BeautifulSoup


def get_git_dates(file_path: str) -> tuple[str, str]:
    """
    Get git creation and modification dates for a file.

    Args:
        file_path: Absolute path to the file

    Returns:
        Tuple of (creation_date, last_modified_date) in ISO format
    """
    file_path = str(Path(file_path).resolve())
    # Use full ISO 8601 datetime format with timezone (preferred by Google)
    # Git uses format: "YYYY-MM-DD HH:MM:SS +HHMM"
    import time
    tz_offset = time.strftime("%z")  # Get current timezone offset like +0200
    today = datetime.now()
    default_creation = (today.replace(year=today.year - 1)).strftime(f"%Y-%m-%d %H:%M:%S {tz_offset}")
    default_modified = today.strftime(f"%Y-%m-%d %H:%M:%S {tz_offset}")

    try:
        # Check if git is available and we're in a git repo
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            capture_output=True,
            check=True
        )

        # Get first commit date (creation)
        creation_output = check_output(
            ["git", "log", "--reverse", "--pretty=format:%ai", file_path],
            stderr=subprocess.DEVNULL
        ).decode().strip()

        creation_date = creation_output.split("\n")[0] if creation_output else default_creation

        # Get last commit date (modification)
        modified_output = check_output(
            ["git", "log", "-1", "--pretty=format:%ai", file_path],
            stderr=subprocess.DEVNULL
        ).decode().strip()

        last_modified_date = modified_output if modified_output else default_modified

        # Keep full datetime with timezone (ISO 8601 format preferred by Google)
        # Git format is: "YYYY-MM-DD HH:MM:SS +TIMEZONE"
        # This is already valid ISO 8601
        if not creation_date or len(creation_date) < 10:
            creation_date = default_creation

        if not last_modified_date or len(last_modified_date) < 10:
            last_modified_date = default_modified

        return creation_date, last_modified_date

    except (subprocess.CalledProcessError, FileNotFoundError, IndexError):
        # Git not available or not a git repo
        return default_creation, default_modified


def on_post_page(output: str, page, config) -> str:
    """
    Generate and inject JSON-LD structured data into the page.

    Args:
        output: The HTML content of the rendered page
        page: The MkDocs page object
        config: The MkDocs configuration object

    Returns:
        Modified HTML with JSON-LD script tag in the head
    """
    if not config.get("site_url"):
        return output

    # Ensure URL ends with trailing slash for consistency
    page_url = config["site_url"].rstrip("/") + "/" + page.url.lstrip("/")
    if not page_url.endswith("/"):
        page_url += "/"

    # Detect page type based on URL pattern
    json_ld = generate_json_ld(page, page_url, config)

    if not json_ld:
        return output

    # Parse HTML and inject JSON-LD
    soup = BeautifulSoup(output, "html.parser")

    # Create JSON-LD script tag
    script_tag = soup.new_tag("script", type="application/ld+json")
    script_tag.string = json.dumps(json_ld, indent=2, ensure_ascii=False)

    # Inject into head
    if soup.head:
        soup.head.append(script_tag)

    return str(soup)


def generate_json_ld(page, page_url: str, config) -> dict:
    """
    Generate appropriate JSON-LD schema based on page URL pattern.

    Args:
        page: The MkDocs page object
        page_url: The full URL of the page
        config: The MkDocs configuration object

    Returns:
        Dictionary containing JSON-LD structured data
    """
    page_path = page.url

    # Default author/publisher organization
    default_org = {
        "@type": "Organization",
        "name": "IDP Software",
        "url": config.get("site_url", "https://idp-software.com")
    }

    # Get dates from git history (first commit = published, last commit = modified)
    date_published, date_modified = get_git_dates(page.file.abs_src_path)

    # Vendor index pages: Organization + Product schema
    if re.match(r"vendors/[^/]+/index\.html$", page_path):
        return generate_organization_schema(page, page_url, config)

    # Vendor news pages: NewsArticle schema
    # Match both: vendors/vendor-name/2025-08-03.html AND vendors/vendor-name/2025-08-03/
    elif re.match(r"vendors/[^/]+/\d{4}-\d{2}-\d{2}(/index\.html|\.html|/)$", page_path):
        return generate_news_article_schema(page, page_url, config, default_org, date_published, date_modified)

    # Capability pages: TechArticle schema
    elif page_path.startswith("capabilities/"):
        return generate_tech_article_schema(page, page_url, config, default_org, date_published, date_modified)

    # About/Events pages: WebPage schema
    elif page_path.startswith("about/") or page_path.startswith("events/"):
        return generate_webpage_schema(page, page_url, config, default_org)

    # Default: Article schema for other content pages
    elif page_path != "" and page_path != "index.html":
        return generate_article_schema(page, page_url, config, default_org, date_published, date_modified)

    return None


def generate_organization_schema(page, page_url: str, config) -> dict:
    """Generate Organization schema for vendor profile pages."""
    from bs4 import BeautifulSoup

    schema = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": page.title,
        "url": page_url,
    }

    # Add description if available
    if "description" in page.meta:
        schema["description"] = page.meta["description"]

    # Add logo/image if available
    if "image" in page.meta:
        schema["logo"] = page.meta["image"]
        schema["image"] = page.meta["image"]

    # Try to extract company website, email, phone from the page content
    # Parse the markdown content to find company information
    if hasattr(page, 'content'):
        soup = BeautifulSoup(page.content, 'html.parser')

        # Look for company information section
        company_section = soup.find('h2', string=re.compile(r'Company Information', re.IGNORECASE))
        if company_section:
            section_content = []
            for sibling in company_section.find_next_siblings():
                if sibling.name == 'h2':
                    break
                section_content.append(sibling.get_text())

            content_text = '\n'.join(section_content)

            # Extract website URL
            web_match = re.search(r'(?:Web|Website):\s*<?([https://]+[^\s>]+)>?', content_text, re.IGNORECASE)
            if web_match and 'url' in schema:
                vendor_url = web_match.group(1).strip()
                schema["sameAs"] = [vendor_url]  # Link to actual company website

            # Extract email
            email_match = re.search(r'Email:\s*([^\s\n]+@[^\s\n]+)', content_text, re.IGNORECASE)
            if email_match:
                schema["email"] = email_match.group(1).strip()

            # Extract phone
            phone_match = re.search(r'Tel(?:ephone)?:\s*([+\d\s\-()]+)', content_text, re.IGNORECASE)
            if phone_match:
                schema["telephone"] = phone_match.group(1).strip()

            # Extract address (simple extraction of lines before Web/Email/Tel)
            address_lines = []
            for line in content_text.split('\n'):
                line = line.strip()
                if line and not any(x in line.lower() for x in ['web:', 'email:', 'tel:', 'website:']):
                    # Looks like an address line
                    if any(char.isdigit() for char in line) or any(x in line for x in ['Ave', 'Street', 'St', 'Road', 'Rd']):
                        address_lines.append(line)

            if address_lines:
                schema["address"] = {
                    "@type": "PostalAddress",
                    "streetAddress": address_lines[0] if len(address_lines) > 0 else "",
                    "addressLocality": address_lines[1].split(',')[0] if len(address_lines) > 1 else "",
                    "addressCountry": "US" if "United States" in content_text else address_lines[-1] if address_lines else ""
                }

    return schema


def generate_news_article_schema(page, page_url: str, config, author_org: dict, date_published: str, date_modified: str) -> dict:
    """Generate NewsArticle schema for vendor news pages."""
    # Extract vendor name from URL path (vendors/vendorname/date.html)
    vendor_slug = page.url.split("/")[1] if "/" in page.url else ""
    vendor_name = vendor_slug.replace("-", " ").title() if vendor_slug else ""

    # Create more descriptive headline for news articles
    headline = page.title
    if vendor_name and vendor_name.lower() not in page.title.lower():
        headline = f"{vendor_name} News: {page.title}"
    elif "summary" in page.meta:
        headline = f"{vendor_name}: {page.meta['summary']}"

    # Construct vendor organization URL
    site_url = config.get("site_url", "https://idp-software.com").rstrip("/")
    vendor_page_url = f"{site_url}/vendors/{vendor_slug}/" if vendor_slug else None

    schema = {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": headline,
        "url": page_url,
        "datePublished": date_published,
        "dateModified": date_modified,
        "author": [author_org],
        "publisher": author_org,
    }

    # Add "about" property to link this news article to the vendor organization
    if vendor_page_url and vendor_name:
        schema["about"] = {
            "@type": "Organization",
            "name": vendor_name,
            "url": vendor_page_url
        }

    # Add description if available
    if "description" in page.meta:
        schema["description"] = page.meta["description"]
        schema["abstract"] = page.meta["description"]
    elif "summary" in page.meta:
        schema["description"] = page.meta["summary"]
        schema["abstract"] = page.meta["summary"]

    # Add image if available
    if "image" in page.meta:
        schema["image"] = [page.meta["image"]]

    # Add article section/category if available
    if "categories" in page.meta:
        categories = page.meta["categories"]
        if isinstance(categories, list) and categories:
            schema["articleSection"] = categories[0]

    # Add keywords if available
    if "tags" in page.meta:
        tags = page.meta["tags"]
        if isinstance(tags, list):
            schema["keywords"] = ", ".join(tags)

    return schema


def generate_tech_article_schema(page, page_url: str, config, author_org: dict, date_published: str, date_modified: str) -> dict:
    """Generate TechArticle schema for capability/technical pages."""
    schema = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": page.title,
        "url": page_url,
        "datePublished": date_published,
        "dateModified": date_modified,
        "author": [author_org],
        "publisher": author_org,
    }

    # Add description if available
    if "description" in page.meta:
        schema["description"] = page.meta["description"]
        schema["abstract"] = page.meta["description"]

    # Add image if available
    if "image" in page.meta:
        schema["image"] = [page.meta["image"]]

    # Add keywords if available
    if "tags" in page.meta:
        tags = page.meta["tags"]
        if isinstance(tags, list):
            schema["keywords"] = ", ".join(tags)

    return schema


def generate_webpage_schema(page, page_url: str, config, author_org: dict) -> dict:
    """Generate WebPage schema for general pages like About and Events."""
    schema = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": page.title,
        "url": page_url,
        "publisher": author_org,
    }

    # Add description if available
    if "description" in page.meta:
        schema["description"] = page.meta["description"]

    # Add image if available
    if "image" in page.meta:
        schema["image"] = page.meta["image"]

    return schema


def generate_article_schema(page, page_url: str, config, author_org: dict, date_published: str, date_modified: str) -> dict:
    """Generate generic Article schema for other content pages."""
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": page.title,
        "url": page_url,
        "datePublished": date_published,
        "dateModified": date_modified,
        "author": [author_org],
        "publisher": author_org,
    }

    # Add description if available
    if "description" in page.meta:
        schema["description"] = page.meta["description"]
        schema["abstract"] = page.meta["description"]

    # Add image if available
    if "image" in page.meta:
        schema["image"] = [page.meta["image"]]

    return schema
