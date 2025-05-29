# Screenshot Script for Markdown Files

This script finds index.md files, extracts the first URL, takes a screenshot, and adds it to the top of the file.

## Features

- Searches for all index.md files in a directory structure
- Extracts the first URL from each markdown file
- Creates an 'assets' folder if it doesn't exist
- Takes SEO-optimized screenshots sized for Google (1200x630)
- Slugifies the H1 heading from the markdown file for the screenshot filename
- Adds the screenshot at the top of the markdown file
- Handles URL redirects automatically
- Automatically dismisses common cookie consent dialogs
- Includes retry logic for failed screenshot attempts
- Waits for page content to fully load including lazy-loaded images

## Requirements

```
python-slugify==8.0.4
playwright==1.42.0
requests==2.31.0
```

## Installation

1. Install the required packages:

```bash
pip install -r requirements-screenshot.txt
```

2. Install Playwright browsers:

```bash
playwright install
```

## Usage

### Process all index.md files in the current directory and subdirectories

```bash
python screenshot.py
```

### Process all index.md files in a specific directory

```bash
python screenshot.py --root docs
```

### Process a specific index.md file

```bash
python screenshot.py --file docs/vendors/tiny-IDP/index.md
```

### Interactive Mode (for handling CAPTCHAs and cookie banners manually)

Use the `--interactive` or `-i` flag to open browser windows for manual interaction:

```bash
python screenshot.py --file docs/vendors/tiny-IDP/index.md --interactive
```

In interactive mode, the script will:
1. Open a visible browser window
2. Navigate to the target URL
3. Wait for you to manually handle any cookie banners or CAPTCHA challenges
4. Take the screenshot when you press Enter in the terminal

### User Agent Selection

You can choose from different user agent profiles using the `--user-agent` or `-u` option:

```bash
python screenshot.py --file docs/vendors/tiny-IDP/index.md --user-agent desktop
```

Available user agent options:
- `googlebot`: Google search bot (may trigger different site behavior)
- `modern`: Latest Chrome browser (default)
- `mobile`: iPhone Safari browser
- `desktop`: MacOS Chrome browser
- `firefox`: Windows Firefox browser

Example with both interactive mode and custom user agent:

```bash
python screenshot.py --file docs/vendors/tiny-IDP/index.md --interactive --user-agent firefox
```

## How It Works

1. The script searches for index.md files
2. For each file, it extracts the first URL and the H1 heading
3. It creates an assets folder if one doesn't exist in the same directory
4. It takes a screenshot of the URL using Playwright
5. It saves the screenshot as a PNG with a slugified version of the H1 heading
6. It adds a markdown image link at the top of the index.md file
