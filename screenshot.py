#!/usr/bin/env python3

import os
import re
import time
import argparse
from pathlib import Path

from slugify import slugify
from playwright.sync_api import sync_playwright


def find_vendor_index_files(root_dir):
    """Find all index.md files in docs/vendors/*/index.md pattern."""
    vendors_dir = Path(root_dir) / 'docs' / 'vendors'
    if not vendors_dir.exists():
        return []

    vendor_files = []
    for vendor_dir in vendors_dir.iterdir():
        if vendor_dir.is_dir():
            index_file = vendor_dir / 'index.md'
            if index_file.exists():
                vendor_files.append(index_file)

    return vendor_files


def extract_first_url(file_path):
    """Extract the first URL from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # URL regex pattern
    url_pattern = r'\[.*?\]\((https?://[^\s\)]+)\)'
    url_matches = re.findall(url_pattern, content)

    if url_matches:
        return url_matches[0]
    return None


def extract_h1_title(file_path):
    """Extract the H1 title from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # H1 regex pattern
    h1_pattern = r'^# (.+)$'
    h1_matches = re.findall(h1_pattern, content, re.MULTILINE)

    if h1_matches:
        return h1_matches[0]
    return "screenshot"


def has_screenshot(file_path):
    """Check if the vendor page already has a screenshot.

    Returns:
        tuple: (has_assets_folder, has_image_file, has_markdown_link, image_path)
    """
    parent_dir = file_path.parent
    assets_dir = parent_dir / 'assets'

    # Check 1: Does assets folder exist?
    has_assets_folder = assets_dir.exists() and assets_dir.is_dir()

    # Check 2: Does an image file exist?
    has_image_file = False
    image_path = None
    if has_assets_folder:
        # Look for any PNG images in the assets folder
        image_files = list(assets_dir.glob('*.png'))
        if image_files:
            has_image_file = True
            image_path = image_files[0]  # Take the first one

    # Check 3: Does the markdown have an image link?
    has_markdown_link = False
    if has_image_file:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Check if there's an image link pointing to assets folder
        image_pattern = r'!\[.*?\]\(\.?/?assets/.*?\)'
        if re.search(image_pattern, content):
            has_markdown_link = True

    return has_assets_folder, has_image_file, has_markdown_link, image_path


def ensure_assets_folder(file_path):
    """Ensure assets folder exists in the same directory as the file."""
    parent_dir = file_path.parent
    assets_dir = parent_dir / 'assets'
    assets_dir.mkdir(exist_ok=True)
    return assets_dir


def get_user_agent(agent_type='modern'):
    """Return a user agent string based on the specified type.

    Args:
        agent_type: Type of user agent to return (googlebot, modern, mobile, desktop, firefox)

    Returns:
        A user agent string
    """
    user_agents = {
        'googlebot': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'modern': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'mobile': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1',
        'desktop': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'firefox': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    }

    return user_agents.get(agent_type.lower(), user_agents['modern'])


def take_screenshot(url, output_path, max_redirects=5, timeout=30000, retry_count=2, wait_time=2000, interactive=False, user_agent_type='modern'):
    """Take a screenshot of the given URL and save it to the output path.

    Args:
        url: The URL to take a screenshot of
        output_path: Path where the screenshot will be saved
        max_redirects: Maximum number of redirects to follow
        timeout: Page load timeout in milliseconds
        retry_count: Number of times to retry if screenshot fails
        wait_time: Time to wait after page load in milliseconds
        interactive: Whether to open a browser window for manual interaction
        user_agent_type: Type of user agent to use (googlebot, modern, mobile, desktop, firefox)

    Returns:
        True if screenshot was successful, False otherwise
    """
    print(f"Taking screenshot of {url}")

    # Track attempts
    attempts = 0
    final_url = None
    user_agent = get_user_agent(user_agent_type)

    while attempts < retry_count:
        try:
            with sync_playwright() as p:
                # Launch browser with specific viewport size for SEO optimization
                # If interactive mode is enabled, disable headless mode
                browser = p.chromium.launch(headless=not interactive)

                # SEO optimized size for Google: 1200x630 (optimal for social sharing)
                context = browser.new_context(
                    viewport={'width': 1280, 'height': 720},
                    device_scale_factor=2,  # For high-DPI screenshots
                    user_agent=user_agent,
                    java_script_enabled=True,  # Ensure JavaScript is enabled
                    has_touch=False,  # Desktop-like behavior
                    ignore_https_errors=True,  # Handle SSL issues
                )

                # Set max timeout to avoid hanging on slow sites
                context.set_default_timeout(timeout)

                # Create a new page
                page = context.new_page()

                # Enable console logging for debugging
                page.on("console", lambda msg: print(f"BROWSER CONSOLE: {msg.text}") if msg.type == "error" else None)

                # Track redirects
                redirect_count = 0
                current_url = url

                # Handle redirects manually if needed
                response = page.goto(current_url, wait_until='domcontentloaded', timeout=timeout)

                if not response:
                    print(f"Failed to get response from {url}")
                    browser.close()
                    attempts += 1
                    continue

                # Check if we got redirected
                final_url = page.url
                if final_url != url:
                    print(f"Redirected to: {final_url}")

                # Wait for network to be idle (no more than 2 connections for at least 500ms)
                try:
                    page.wait_for_load_state('networkidle', timeout=timeout)
                except Exception as e:
                    print(f"Network did not become idle, but continuing: {e}")

                # Wait for main content to load
                page.wait_for_timeout(wait_time)

                # Wait for any lazy-loaded images to appear
                try:
                    page.wait_for_selector('img[src]:not([src=""])', timeout=5000)
                except Exception:
                    # Continue even if no images are found
                    pass

                # In non-interactive mode, attempt to automatically handle cookie consents
                if not interactive:
                    try:
                        for selector in [
                            'button:has-text("Accept")', 'button:has-text("Accept All")',
                            'button:has-text("Accept")', 'button:has-text("Alle aktzeptieren")',
                            'button:has-text("I Accept")', 'button:has-text("Agree")',
                            'button:has-text("Close")', 'button:has-text("OK")',
                            '.cookie-consent button', '#cookie-notice button',
                            '.gdpr-consent button', '.consent-banner button'
                        ]:
                            consent_button = page.query_selector(selector)
                            if consent_button:
                                consent_button.click()
                                page.wait_for_timeout(500)
                                break
                    except Exception as e:
                        print(f"Error handling cookie consent: {e}")

                # If in interactive mode, prompt the user to interact with the page
                if interactive:
                    print("-" * 50)
                    print("INTERACTIVE MODE: Browser window opened for manual interaction")
                    print("Please complete any CAPTCHA challenges or accept cookie banners")
                    print("When ready to take the screenshot, press Enter in this terminal...")
                    print("-" * 50)
                    input("Press Enter to take the screenshot...")

                # Take screenshot
                try:
                    screenshot_path = str(output_path)
                    page.screenshot(path=screenshot_path, full_page=False, timeout=timeout)
                    print(f"Screenshot saved to {screenshot_path}")

                    # Check if the screenshot file exists and has content
                    if not os.path.exists(screenshot_path) or os.path.getsize(screenshot_path) < 1000:
                        print(f"Screenshot file is missing or too small: {screenshot_path}")
                        raise Exception("Invalid screenshot file")

                    browser.close()
                    return True
                except Exception as e:
                    print(f"Screenshot failed: {e}")
                    browser.close()
                    attempts += 1

        except Exception as e:
            print(f"Error taking screenshot (attempt {attempts+1}): {e}")
            attempts += 1
            time.sleep(2)  # Wait before retrying

    print(f"Failed to take screenshot after {retry_count} attempts")
    return False


def add_image_link_to_file(file_path, image_path, alt_text):
    """Add image link after the headline and first paragraph."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create relative path from file to image
    rel_image_path = os.path.relpath(image_path, file_path.parent)

    # Create markdown image link
    image_link = f"\n![{alt_text}]({rel_image_path})\n"

    # Find the position after the first paragraph
    # Pattern: H1 title, then first paragraph, then insert image
    lines = content.split('\n')

    # Find H1 line
    h1_index = -1
    for i, line in enumerate(lines):
        if line.startswith('# '):
            h1_index = i
            break

    if h1_index == -1:
        # No H1 found, add at the top
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(image_link + '\n' + content)
        print(f"Added image link at the top of {file_path}")
        return True

    # Find the end of the first paragraph after H1
    # First paragraph ends at the first empty line or next heading
    insert_index = h1_index + 1
    found_content = False

    for i in range(h1_index + 1, len(lines)):
        line = lines[i].strip()

        # Skip empty lines immediately after H1
        if not line and not found_content:
            continue

        # Found content
        if line and not found_content:
            found_content = True
            continue

        # If we found content and now hit empty line or another heading, insert here
        if found_content and (not line or line.startswith('#')):
            insert_index = i
            break
    else:
        # Reached end of file, insert at the end
        insert_index = len(lines)

    # Insert the image link
    lines.insert(insert_index, image_link)

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"Added image link after first paragraph in {file_path}")
    return True


def process_index_file(file_path, interactive=False, user_agent_type='modern'):
    """Process a single index.md file.

    Args:
        file_path: Path to the index.md file
        interactive: Whether to open a browser window for manual interaction
        user_agent_type: Type of user agent to use (googlebot, modern, mobile, desktop, firefox)

    Returns:
        True if processing was successful, False otherwise
    """
    print(f"\nProcessing {file_path}")

    # Check if screenshot already exists
    has_assets, has_image, has_link, existing_image_path = has_screenshot(file_path)

    if has_assets and has_image and has_link:
        print(f"[OK] Screenshot already exists and is linked in {file_path.parent.name}")
        return True

    if has_assets and has_image and not has_link:
        print(f"[WARN] Screenshot exists but not linked in markdown for {file_path.parent.name}")
        print(f"  Adding image link to {file_path}")
        h1_title = extract_h1_title(file_path)
        add_image_link_to_file(file_path, existing_image_path, h1_title)
        return True

    # Need to take a screenshot
    print(f"[INFO] No screenshot found for {file_path.parent.name}, will create one")

    # Extract URL
    url = extract_first_url(file_path)
    if not url:
        print(f"[ERROR] No URL found in {file_path}")
        return False

    # Extract H1 title
    h1_title = extract_h1_title(file_path)

    # Create slug from H1 title
    slug = slugify(h1_title)

    # Ensure assets folder exists
    assets_dir = ensure_assets_folder(file_path)

    # Create output path for screenshot
    output_path = assets_dir / f"{slug}.png"

    # Take screenshot
    success = take_screenshot(url, output_path, interactive=interactive, user_agent_type=user_agent_type)
    if not success:
        return False

    # Always add image link to file (even in interactive mode)
    add_image_link_to_file(file_path, output_path, h1_title)

    return True


def main():
    parser = argparse.ArgumentParser(
        description='Process vendor index.md files to add screenshots',
        epilog='By default, runs in INTERACTIVE mode for vendors without screenshots. Use --no-interactive to disable.'
    )
    parser.add_argument('--root', '-r', default='.', help='Root directory to search for docs/vendors/*/index.md files (default: current directory)')
    parser.add_argument('--file', '-f', help='Process a specific index.md file instead of searching all vendors')
    parser.add_argument('--no-interactive', action='store_true', help='Disable interactive mode (automatic screenshot without manual verification)')
    parser.add_argument('--user-agent', '-u', choices=['googlebot', 'modern', 'mobile', 'desktop', 'firefox'], default='modern',
                      help='User agent type to use for browser (default: modern)')
    args = parser.parse_args()

    # Interactive is ON by default, unless --no-interactive is specified
    interactive = not args.no_interactive

    if interactive:
        print("\n" + "="*70)
        print("INTERACTIVE MODE (default)")
        print("="*70)
        print("Browser windows will open for manual interaction.")
        print("You can accept cookie banners or solve CAPTCHA challenges.")
        print("Press Enter in the terminal to take each screenshot.")
        print("\nTip: Use --no-interactive flag to run without manual verification.")
        print("="*70 + "\n")
    else:
        print("\n" + "="*70)
        print("AUTOMATIC MODE")
        print("="*70)
        print("Screenshots will be taken automatically without manual verification.")
        print("Cookie consents will be handled automatically if possible.")
        print("="*70 + "\n")

    if args.file:
        # Process specific file
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"✗ File {file_path} does not exist")
            return
        process_index_file(file_path, interactive=interactive, user_agent_type=args.user_agent)
    else:
        # Find and process all vendor index.md files
        vendor_files = find_vendor_index_files(args.root)

        if not vendor_files:
            print(f"[ERROR] No vendor files found in {args.root}/docs/vendors/*/index.md")
            print(f"  Make sure you're running from the project root directory.")
            return

        print(f"Found {len(vendor_files)} vendor index.md files\n")

        # Count vendors needing screenshots
        needs_screenshot = []
        for file_path in vendor_files:
            has_assets, has_image, has_link, _ = has_screenshot(file_path)
            if not (has_assets and has_image and has_link):
                needs_screenshot.append(file_path)

        print(f"[OK] {len(vendor_files) - len(needs_screenshot)} vendors already have screenshots")
        print(f"[INFO] {len(needs_screenshot)} vendors need screenshots\n")

        if needs_screenshot:
            print("Vendors needing screenshots:")
            for file_path in needs_screenshot:
                print(f"  - {file_path.parent.name}")
            print()

        for file_path in vendor_files:
            process_index_file(file_path, interactive=interactive, user_agent_type=args.user_agent)


if __name__ == "__main__":
    main()
