#!/usr/bin/env python3

import os
import re
import time
import argparse
from pathlib import Path
from urllib.parse import urlparse

import requests
from slugify import slugify
from playwright.sync_api import sync_playwright


def find_index_files(root_dir):
    """Find all index.md files in the given directory and its subdirectories."""
    return list(Path(root_dir).rglob('index.md'))


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
    """Add image link to the top of the markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create relative path from file to image
    rel_image_path = os.path.relpath(image_path, file_path.parent)

    # Create markdown image link
    image_link = f"![{alt_text}]({rel_image_path})\n\n"

    # Add image link to the top of the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(image_link + content)

    print(f"Added image link to {file_path}")
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

    # Extract URL
    url = extract_first_url(file_path)
    if not url:
        print(f"No URL found in {file_path}")
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

    # Add image link to file if not interactive
    if not interactive:
        add_image_link_to_file(file_path, output_path, h1_title)

    return True


def main():
    parser = argparse.ArgumentParser(description='Process index.md files to add screenshots')
    parser.add_argument('--root', '-r', default='.', help='Root directory to search for index.md files')
    parser.add_argument('--file', '-f', help='Process a specific index.md file instead of searching')
    parser.add_argument('--interactive', '-i', action='store_true', help='Open browser for manual interaction (e.g., for CAPTCHA or cookie consent)')
    parser.add_argument('--user-agent', '-u', choices=['googlebot', 'modern', 'mobile', 'desktop', 'firefox'], default='modern', 
                      help='User agent type to use for browser')
    args = parser.parse_args()

    if args.interactive:
        print("\nRunning in INTERACTIVE mode. Browser windows will open for manual interaction.")
        print("You will need to manually accept cookie banners or solve CAPTCHA challenges.")
        print("The script will wait for your input before taking each screenshot.\n")

    if args.file:
        # Process specific file
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"File {file_path} does not exist")
            return
        process_index_file(file_path, interactive=args.interactive, user_agent_type=args.user_agent)
    else:
        # Find and process all index.md files
        index_files = find_index_files(args.root)
        print(f"Found {len(index_files)} index.md files")

        for file_path in index_files:
            process_index_file(file_path, interactive=args.interactive, user_agent_type=args.user_agent)


if __name__ == "__main__":
    main()
