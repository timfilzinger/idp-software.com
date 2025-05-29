# Testing the Screenshot Script

This guide explains how to run and extend the tests for the screenshot.py script.

## Running the Tests

To run the tests, use the unittest module from the command line:

```bash
python -m unittest test_screenshot.py
```

Or with pytest for a more detailed output:

```bash
pip install pytest
python -m pytest test_screenshot.py -v
```

## Test Coverage

To check test coverage, use pytest-cov:

```bash
pip install pytest-cov
python -m pytest test_screenshot.py --cov=screenshot
```

## Test Structure

The tests are organized into several test classes:

1. `TestScreenshotFunctions` - Tests for individual utility functions
2. `TestScreenshotIntegration` - Tests for the integration of multiple functions
3. `TestTakeScreenshot` - Tests for the screenshot taking functionality with mocked Playwright

## Adding New Tests

When adding new functionality to the screenshot script, be sure to add corresponding tests. Follow these steps:

1. For new utility functions, add unit tests to `TestScreenshotFunctions`
2. For changes to the core workflow, add tests to `TestScreenshotIntegration`
3. For changes to the screenshot capturing, add tests to `TestTakeScreenshot`

## Mocking External Dependencies

The tests use unittest.mock to avoid making actual web requests or browser interactions. The key mocks include:

- `sync_playwright` - Mocked to return a controlled Playwright instance
- `take_screenshot` - Mocked in integration tests to avoid actual screenshot capture

When adding tests for new external dependencies, create appropriate mock objects.

## Test Data

Test data is created in temporary directories that are automatically cleaned up after tests complete. This approach prevents test pollution and ensures tests can be run in any environment.

## Continuous Integration

The tests are automatically run in GitHub Actions when changes are made to the screenshot script or tests. See the `.github/workflows/test_screenshot.yml` file for details.
