#!/usr/bin/env python3

import os
import unittest
from pathlib import Path
from unittest import mock
from tempfile import TemporaryDirectory

# Import the functions from screenshot.py
from screenshot import (
    find_index_files,
    extract_first_url,
    extract_h1_title,
    ensure_assets_folder,
    add_image_link_to_file,
    process_index_file
)


class TestScreenshotFunctions(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.temp_dir = TemporaryDirectory()
        self.test_dir = Path(self.temp_dir.name)

    def tearDown(self):
        # Clean up the temporary directory
        self.temp_dir.cleanup()

    def test_get_user_agent(self):
        # Import the function
        from screenshot import get_user_agent

        # Test default agent
        default_agent = get_user_agent()
        self.assertIn('Chrome', default_agent)
        self.assertIn('Mozilla', default_agent)

        # Test googlebot agent
        googlebot_agent = get_user_agent('googlebot')
        self.assertIn('Googlebot', googlebot_agent)

        # Test mobile agent
        mobile_agent = get_user_agent('mobile')
        self.assertIn('iPhone', mobile_agent)

        # Test firefox agent
        firefox_agent = get_user_agent('firefox')
        self.assertIn('Firefox', firefox_agent)

        # Test with unknown agent type (should return modern)
        unknown_agent = get_user_agent('unknown')
        self.assertEqual(unknown_agent, get_user_agent('modern'))

    def test_find_index_files(self):
        # Create test directory structure
        (self.test_dir / 'folder1').mkdir()
        (self.test_dir / 'folder1' / 'index.md').write_text('# Test Index 1')
        (self.test_dir / 'folder2').mkdir()
        (self.test_dir / 'folder2' / 'index.md').write_text('# Test Index 2')
        (self.test_dir / 'folder3').mkdir()
        (self.test_dir / 'folder3' / 'other.md').write_text('# Not an index')

        # Test finding index files
        index_files = find_index_files(self.test_dir)

        # Verify we found the correct number of files
        self.assertEqual(len(index_files), 2)

        # Verify the files are the ones we expect
        paths = [file.name for file in index_files]
        self.assertIn('index.md', paths)

    def test_extract_first_url(self):
        # Create test index file with a URL
        test_file = self.test_dir / 'index.md'
        test_file.write_text(
            '# Test Title\n\n'
            'This is a test file with a [link](https://example.com) and '
            'another [link](https://example.org).'
        )

        # Test extracting the first URL
        url = extract_first_url(test_file)

        # Verify the URL is correct
        self.assertEqual(url, 'https://example.com')

        # Test with no URLs
        no_url_file = self.test_dir / 'no_url.md'
        no_url_file.write_text('# Test Title\n\nThis is a test file with no URLs.')

        # Verify None is returned when no URL is found
        self.assertIsNone(extract_first_url(no_url_file))

    def test_extract_h1_title(self):
        # Create test index file with an H1 title
        test_file = self.test_dir / 'index.md'
        test_file.write_text('# This is a Test Title\n\nContent goes here.')

        # Test extracting the H1 title
        title = extract_h1_title(test_file)

        # Verify the title is correct
        self.assertEqual(title, 'This is a Test Title')

        # Test with no H1 title
        no_title_file = self.test_dir / 'no_title.md'
        no_title_file.write_text('Content without a title.')

        # Verify default title is returned when no H1 is found
        self.assertEqual(extract_h1_title(no_title_file), 'screenshot')

    def test_ensure_assets_folder(self):
        # Create test index file
        test_dir = self.test_dir / 'test_folder'
        test_dir.mkdir()
        test_file = test_dir / 'index.md'
        test_file.write_text('# Test')

        # Test ensuring assets folder exists
        assets_dir = ensure_assets_folder(test_file)

        # Verify assets folder was created
        self.assertTrue(assets_dir.exists())
        self.assertEqual(assets_dir.name, 'assets')
        self.assertEqual(assets_dir.parent, test_file.parent)

        # Test with existing assets folder
        assets_dir = ensure_assets_folder(test_file)

        # Verify function works with existing folder
        self.assertTrue(assets_dir.exists())

    def test_add_image_link_to_file(self):
        # Create test index file
        test_file = self.test_dir / 'index.md'
        original_content = '# Test Title\n\nThis is the content.'
        test_file.write_text(original_content)

        # Create test image path
        image_path = self.test_dir / 'assets' / 'test-title.png'

        # Test adding image link to file
        add_image_link_to_file(test_file, image_path, 'Test Title')

        # Read updated file content
        updated_content = test_file.read_text()

        # Verify image link was added at the top
        self.assertTrue(updated_content.startswith('![Test Title](assets/test-title.png)'))
        self.assertIn(original_content, updated_content)


class TestScreenshotIntegration(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.temp_dir = TemporaryDirectory()
        self.test_dir = Path(self.temp_dir.name)

        # Create a test index file
        self.test_file = self.test_dir / 'index.md'
        self.test_file.write_text(
            '# Test Page\n\n'
            'This is a test page with a [link](https://example.com).'
        )

    def tearDown(self):
        # Clean up the temporary directory
        self.temp_dir.cleanup()

    @mock.patch('screenshot.take_screenshot')
    def test_process_index_file(self, mock_take_screenshot):
        # Configure the mock to return True
        mock_take_screenshot.return_value = True

        # Test processing an index file
        result = process_index_file(self.test_file)

        # Verify the result is True (success)
        self.assertTrue(result)

        # Verify take_screenshot was called
        mock_take_screenshot.assert_called_once()

        # Verify the first argument to take_screenshot is the expected URL
        args, _ = mock_take_screenshot.call_args
        self.assertEqual(args[0], 'https://example.com')

        # Verify assets folder was created
        assets_dir = self.test_file.parent / 'assets'
        self.assertTrue(assets_dir.exists())

        # Verify the image link was added to the file
        updated_content = self.test_file.read_text()
        self.assertIn('![Test Page]', updated_content)

    @mock.patch('screenshot.take_screenshot')
    def test_process_index_file_no_url(self, mock_take_screenshot):
        # Create a test file with no URL
        no_url_file = self.test_dir / 'no_url.md'
        no_url_file.write_text('# Test Page\n\nThis is a test page with no URL.')

        # Test processing a file with no URL
        result = process_index_file(no_url_file)

        # Verify the result is False (failure)
        self.assertFalse(result)

        # Verify take_screenshot was not called
        mock_take_screenshot.assert_not_called()


# Mock class for Playwright Context
class MockPage:
    def __init__(self):
        self.goto_called = False
        self.screenshot_called = False
        self.extra_headers = {}
        self.event_handlers = {}
        self.url = None
        self.selectors = {}
        self.load_states = []

    def goto(self, url, wait_until=None, timeout=None):
        self.goto_called = True
        self.goto_url = url
        self.wait_until = wait_until
        self.timeout = timeout
        # Return a mock response
        return {"status": 200}

    def wait_for_timeout(self, timeout):
        self.timeout = timeout

    def wait_for_load_state(self, state, timeout=None):
        self.load_states.append(state)

    def wait_for_selector(self, selector, timeout=None):
        self.selectors[selector] = True

    def query_selector(self, selector):
        if selector in self.selectors:
            return MockElement(self)
        return None

    def screenshot(self, path, full_page=False, timeout=None):
        self.screenshot_called = True
        self.screenshot_path = path
        self.full_page = full_page
        self.screenshot_timeout = timeout

        # Create an empty file to simulate the screenshot
        Path(path).touch()
        # Make the file at least 1KB to pass size check
        with open(path, 'wb') as f:
            f.write(b'0' * 1024)
        return True

    def set_extra_http_headers(self, headers):
        self.extra_headers = headers

    def on(self, event, callback):
        if event not in self.event_handlers:
            self.event_handlers[event] = []
        self.event_handlers[event].append(callback)


class MockElement:
    def __init__(self, page):
        self.page = page
        self.clicked = False

    def click(self):
        self.clicked = True


class MockContext:
    def __init__(self):
        self.page = MockPage()
        self.timeout = 30000

    def new_page(self):
        return self.page

    def set_default_timeout(self, timeout):
        self.timeout = timeout


class MockBrowser:
    def __init__(self):
        self.context = MockContext()
        self.closed = False

    def new_context(self, viewport, device_scale_factor):
        self.viewport = viewport
        self.device_scale_factor = device_scale_factor
        return self.context

    def close(self):
        self.closed = True


class MockPlaywright:
    def __init__(self):
        self.chromium = MockChromium()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class MockChromium:
    def __init__(self):
        self.browser = MockBrowser()

    def launch(self, headless=True):
        self.headless = headless
        return self.browser


class TestTakeScreenshot(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.temp_dir = TemporaryDirectory()
        self.test_dir = Path(self.temp_dir.name)

        # Create a test output path
        self.output_path = self.test_dir / 'test_screenshot.png'

    def tearDown(self):
        # Clean up the temporary directory
        self.temp_dir.cleanup()

    @mock.patch('screenshot.sync_playwright', return_value=MockPlaywright())
    def test_take_screenshot(self, mock_sync_playwright):
        # Import take_screenshot here to use the patched sync_playwright
        from screenshot import take_screenshot

        # Test taking a screenshot
        result = take_screenshot('https://example.com', self.output_path, interactive=False, user_agent_type='modern')

        # Verify the result is True (success)
        self.assertTrue(result)

        # Verify the output file was created
        self.assertTrue(self.output_path.exists())

        # Get the mock objects
        mock_playwright = mock_sync_playwright.return_value
        mock_browser = mock_playwright.chromium.browser
        mock_page = mock_browser.context.page

        # Verify browser was launched headless (since interactive=False)
        self.assertTrue(mock_playwright.chromium.headless)

        # Verify correct viewport settings
        self.assertEqual(mock_browser.viewport, {'width': 1280, 'height': 720})
        self.assertEqual(mock_browser.device_scale_factor, 2)

        # Verify page navigation
        self.assertTrue(mock_page.goto_called)
        self.assertEqual(mock_page.goto_url, 'https://example.com')

        # Verify screenshot was taken
        self.assertTrue(mock_page.screenshot_called)
        self.assertEqual(str(mock_page.screenshot_path), str(self.output_path))
        self.assertFalse(mock_page.full_page)

        # Verify browser was closed
        self.assertTrue(mock_browser.closed)

    @mock.patch('screenshot.sync_playwright', return_value=MockPlaywright())
    @mock.patch('builtins.input', return_value='')
    def test_take_screenshot_interactive(self, mock_input, mock_sync_playwright):
        # Import take_screenshot here to use the patched sync_playwright
        from screenshot import take_screenshot

        # Test taking a screenshot in interactive mode
        result = take_screenshot('https://example.com', self.output_path, interactive=True, user_agent_type='firefox')

        # Verify the result is True (success)
        self.assertTrue(result)

        # Get the mock objects
        mock_playwright = mock_sync_playwright.return_value
        mock_browser = mock_playwright.chromium.browser

        # Verify browser was launched non-headless (since interactive=True)
        self.assertFalse(mock_playwright.chromium.headless)

        # Verify user was prompted for input
        mock_input.assert_called_once()

        # Verify firefox user agent was used
        self.assertIn('firefox', mock_browser.context.page.extra_headers.get('User-Agent', '').lower())

    @mock.patch('screenshot.sync_playwright')
    @mock.patch('os.path.exists', return_value=False)
    def test_take_screenshot_retry_on_failure(self, mock_exists, mock_sync_playwright):
        # Configure the mocks
        mock_playwright = MockPlaywright()
        mock_sync_playwright.return_value = mock_playwright

        # Import take_screenshot here to use the patched sync_playwright
        from screenshot import take_screenshot

        # Test taking a screenshot with retry
        result = take_screenshot('https://example.com', self.output_path, retry_count=2)

        # Verify the result is False (failure after retries)
        self.assertFalse(result)

        # Verify sync_playwright was called multiple times (for retries)
        self.assertEqual(mock_sync_playwright.call_count, 2)

    @mock.patch('screenshot.sync_playwright')
    def test_take_screenshot_with_redirect(self, mock_sync_playwright):
        # Configure the mock
        mock_playwright = MockPlaywright()
        mock_playwright.chromium.browser.context.page.url = 'https://example.org'  # Simulated redirect
        mock_sync_playwright.return_value = mock_playwright

        # Import take_screenshot here to use the patched sync_playwright
        from screenshot import take_screenshot

        # Test taking a screenshot with a redirect
        result = take_screenshot('https://example.com', self.output_path)

        # Verify the result is True (success)
        self.assertTrue(result)

        # Verify the page was loaded with the original URL
        mock_page = mock_playwright.chromium.browser.context.page
        self.assertEqual(mock_page.goto_url, 'https://example.com')


if __name__ == '__main__':
    unittest.main()
