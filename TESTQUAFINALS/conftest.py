"""
Pytest configuration file
Contains shared fixtures and hooks for WebDriver setup
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os

# Test configuration constants
BASE_URL = "https://opensource-demo.orangehrmlive.com"
IMPLICIT_WAIT = 5
EXPLICIT_WAIT = 10


@pytest.fixture(scope="function")
def driver():
    """
    WebDriver fixture with proper setup and teardown
    Uses webdriver-manager for automatic ChromeDriver management

    Scope: function (creates new browser instance for each test)
    """
    # Setup - Initialize ChromeDriver with webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Configure browser
    driver.maximize_window()
    driver.implicitly_wait(IMPLICIT_WAIT)

    yield driver

    # Teardown - Quit browser
    driver.quit()


@pytest.fixture(scope="function")
def wait(driver):
    """
    Explicit wait fixture for reusable waits across tests
    Returns a WebDriverWait object with 10 second timeout
    """
    from selenium.webdriver.support.ui import WebDriverWait
    return WebDriverWait(driver, EXPLICIT_WAIT)


# Pytest hook for screenshot capture on test failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Captures screenshots when tests fail
    Screenshots saved to 'screenshots/' directory with timestamp
    """
    outcome = yield
    report = outcome.get_result()

    # Only capture screenshot if test failed during execution
    if report.when == 'call' and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            # Create screenshots directory if it doesn't exist
            screenshot_dir = 'screenshots'
            os.makedirs(screenshot_dir, exist_ok=True)

            # Generate filename with timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshot_dir, screenshot_name)

            # Capture and save screenshot
            driver.save_screenshot(screenshot_path)
            print(f"\n📸 Screenshot saved: {screenshot_path}")


def pytest_configure(config):
    """
   Custom markers for test categorization
    Markers allow running specific test subsets (e.g., pytest -m smoke)
    """
    config.addinivalue_line("markers", "smoke: Critical smoke tests")
    config.addinivalue_line("markers", "regression: Comprehensive regression tests")
    config.addinivalue_line("markers", "admin: Admin module tests")
    config.addinivalue_line("markers", "login: Login functionality tests")
    config.addinivalue_line("markers", "navigation: Navigation tests")
