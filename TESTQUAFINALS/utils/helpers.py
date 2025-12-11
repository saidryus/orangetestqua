"""
Selenium helper utilities for improved test stability and reusability
Contains wrapper functions for common Selenium operations
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SeleniumHelpers:
    """Collection of reusable Selenium helper methods for robust test automation"""

    @staticmethod
    def safe_click(driver, locator, timeout=10):
        """
        Safely click an element with proper wait and fallback

        Args:
            driver: WebDriver instance
            locator: Tuple (By.XPATH, "path")
            timeout: Max wait time in seconds

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            wait = WebDriverWait(driver, timeout)
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info(f"✓ Clicked element: {locator[1][:50]}")
            return True
        except TimeoutException:
            logger.warning(f"⚠ Element not clickable, trying JavaScript: {locator[1][:50]}")
            try:
                element = driver.find_element(*locator)
                driver.execute_script("arguments[0].click();", element)
                logger.info(f"✓ JavaScript click successful")
                return True
            except Exception as e:
                logger.error(f"✗ Click failed: {e}")
                return False
        except Exception as e:
            logger.error(f"✗ Click error: {e}")
            return False

    @staticmethod
    def safe_send_keys(driver, locator, text, timeout=10, clear_first=True):
        """
        Safely send keys to element with proper wait

        Args:
            driver: WebDriver instance
            locator: Tuple (By.XPATH, "path")
            text: Text to enter
            timeout: Max wait time
            clear_first: Clear field before typing
        """
        try:
            wait = WebDriverWait(driver, timeout)
            element = wait.until(EC.element_to_be_clickable(locator))
            if clear_first:
                element.clear()
            element.send_keys(text)
            logger.info(f"✓ Sent keys to element: {text}")
        except Exception as e:
            logger.error(f"✗ Send keys failed: {e}")
            raise

    @staticmethod
    def wait_for_element_visible(driver, locator, timeout=10):
        """Wait for element to be visible and return it"""
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.visibility_of_element_located(locator))
        logger.info(f"✓ Element visible: {locator[1][:50]}")
        return element

    @staticmethod
    def wait_for_element_clickable(driver, locator, timeout=10):
        """Wait for element to be clickable and return it"""
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        logger.info(f"✓ Element clickable: {locator[1][:50]}")
        return element

    @staticmethod
    def get_element_text(driver, locator, timeout=10):
        """Get text from element with wait"""
        element = SeleniumHelpers.wait_for_element_visible(driver, locator, timeout)
        return element.text

    @staticmethod
    def wait_for_table_to_update(driver, timeout=10):
        """
        Wait for table body to be present and contain rows
        Specific to OrangeHRM tables
        """
        from selenium.webdriver.common.by import By
        wait = WebDriverWait(driver, timeout)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-table-body")))
        # Wait for at least one row to appear
        wait.until(
            lambda d: len(d.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")) > 0
        )
        logger.info(f"✓ Table updated with results")

    @staticmethod
    def select_dropdown_option(driver, dropdown_locator, option_text, timeout=10):
        """
        Handle custom dropdowns (non-select elements)
        1. Click dropdown
        2. Wait for listbox
        3. Click option
        """
        from selenium.webdriver.common.by import By

        # Click dropdown to open
        SeleniumHelpers.safe_click(driver, dropdown_locator, timeout)

        # Wait for listbox to appear
        listbox = (By.XPATH, "//div[@role='listbox']")
        SeleniumHelpers.wait_for_element_visible(driver, listbox, timeout)

        # Click the option
        option = (By.XPATH, f"//div[@role='listbox']//span[text()='{option_text}']")
        SeleniumHelpers.safe_click(driver, option, timeout)

        logger.info(f"✓ Selected dropdown option: {option_text}")

    @staticmethod
    def select_autocomplete_option(driver, input_locator, search_text, option_text, timeout=10):
        """
        Handle autocomplete fields
        1. Type search text
        2. Wait for suggestions
        3. Click matching option
        """
        from selenium.webdriver.common.by import By

        # Type in autocomplete field
        SeleniumHelpers.safe_send_keys(driver, input_locator, search_text, timeout)

        # Wait for autocomplete listbox
        listbox = (By.XPATH, "//div[@role='listbox']")
        SeleniumHelpers.wait_for_element_visible(driver, listbox, timeout)

        # Small delay for autocomplete to populate
        time.sleep(1)

        # Click matching option
        option = (By.XPATH, f"//div[@role='listbox']//span[contains(text(),'{option_text}')]")
        SeleniumHelpers.safe_click(driver, option, timeout)

        logger.info(f"✓ Selected autocomplete: {option_text}")
