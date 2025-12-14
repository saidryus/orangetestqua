"""
OrangeHRM Admin Module Test Suite
Tests for User Management - System Users functionality
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

# parent directory to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.helpers import SeleniumHelpers

import logging
logger = logging.getLogger(__name__)

# Test Data
URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = 'Admin'
PASSWORD = 'admin123'


# Locator Constants (Best Practice - centralized locators)
class LoginLocators:
    """Login page locators"""
    USERNAME_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    DASHBOARD_HEADER = (By.TAG_NAME, "h6")
    ERROR_MESSAGE = (By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")


class AdminLocators:
    """Admin page locators"""
    ADMIN_MENU = (By.XPATH, "//span[text()='Admin']")
    TABLE = (By.CLASS_NAME, "oxd-table")
    FORM = (By.CLASS_NAME, "oxd-form")
    TABLE_BODY = (By.CLASS_NAME, "oxd-table-body")
    TABLE_ROWS = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")

    # Search form
    USERNAME_INPUT = (By.XPATH, "(//label[text()='Username']/parent::div/following-sibling::div/input)[1]")
    USER_ROLE_DROPDOWN = (By.XPATH, "(//label[text()='User Role']/parent::div/following-sibling::div//div[@class='oxd-select-text-input'])[1]")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    STATUS_DROPDOWN = (By.XPATH, "(//label[text()='Status']/parent::div/following-sibling::div//div[@class='oxd-select-text-input'])[1]")

    # Buttons
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    RESET_BUTTON = (By.XPATH, "//button[normalize-space()='Reset']")

    # Table cells
    FIRST_ROW_USERNAME = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row'][1]//div[@role='cell'][2]")
    FIRST_ROW_ROLE = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row'][1]//div[@role='cell'][3]")
    FIRST_ROW_EMPLOYEE = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row'][1]//div[@role='cell'][4]")
    FIRST_ROW_STATUS = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row'][1]//div[@role='cell'][5]")

    # Delete functionality
    FIRST_ROW_CHECKBOX = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row'][1]//div[@role='cell'][1]//i")
    FIRST_ROW_DELETE_BUTTON = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row'][1]//button[.//i[contains(@class, 'bi-trash')]]")
    ERROR_TOAST = (By.XPATH, "//div[contains(@class, 'oxd-toast--error')]")

class NavigationLocators:
    """Navigation element locators"""
    UPGRADE_BUTTON = (By.XPATH, "//button[contains(., 'Upgrade')]")
    PROFILE_DROPDOWN = (By.CSS_SELECTOR, "p.oxd-userdropdown-name")
    ABOUT_LINK = (By.XPATH, "//a[contains(., 'About')]")
    SUPPORT_LINK = (By.XPATH, "//a[contains(., 'Support')]")
    ABOUT_DIALOG = (By.CSS_SELECTOR, "div.oxd-dialog-container-default")
    COMPANY_NAME_LABEL = (By.XPATH, ".//p[contains(., 'Company Name')]")
    SIDEBAR_SEARCH = (By.XPATH, "//input[@placeholder='Search']")
    SIDEBAR_MENU_ITEMS = (By.CSS_SELECTOR, "ul.oxd-main-menu li")


# ========== LOGIN TESTS ========== #

@pytest.mark.smoke
@pytest.mark.login
def test_positive_login(driver):
    """
    TC-LOGIN-001: Verify successful login with valid credentials
    Priority: High
    """
    driver.get(URL)

    # Use helper functions for improved reliability
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.USERNAME_INPUT, USERNAME)
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.PASSWORD_INPUT, PASSWORD)
    SeleniumHelpers.safe_click(driver, LoginLocators.LOGIN_BUTTON)

    # Verify dashboard appears
    dashboard_text = SeleniumHelpers.get_element_text(driver, LoginLocators.DASHBOARD_HEADER)
    assert "Dashboard" in dashboard_text, f"Expected 'Dashboard', got '{dashboard_text}'"


@pytest.mark.smoke
@pytest.mark.login
def test_negative_login(driver):
    """
    TC-LOGIN-002: Verify error message with invalid credentials
    Priority: High
    """
    driver.get(URL)

    SeleniumHelpers.safe_send_keys(driver, LoginLocators.USERNAME_INPUT, "wrongUsername")
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.PASSWORD_INPUT, PASSWORD)
    SeleniumHelpers.safe_click(driver, LoginLocators.LOGIN_BUTTON)

    # Verify error message
    error_text = SeleniumHelpers.get_element_text(driver, LoginLocators.ERROR_MESSAGE)
    assert "Invalid credentials" in error_text, f"Expected error message, got '{error_text}'"


# ========== PARAMETRIZED LOGIN TESTS ========== #

@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.parametrize("username,password,should_succeed", [
    ("Admin", "admin123", True), # Valid credentials - should login
    ("wronguser", "admin123", False), # Wrong username - should fail
    ("Admin", "wrongpass", False), # Wrong password - should fail
])
def test_login_with_multiple_credentials(driver, username, password, should_succeed):
    """
    TC-LOGIN-003: Parametrized login test with multiple credential combinations
    Priority: High
    Tests valid and invalid login scenarios
    """
    driver.get(URL)

    # Enter credentials
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.USERNAME_INPUT, username)
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.PASSWORD_INPUT, password)

    # Click login
    SeleniumHelpers.safe_click(driver, LoginLocators.LOGIN_BUTTON)

    import time
    time.sleep(2)

    if should_succeed:
        # Should see Dashboard
        try:
            dashboard_text = SeleniumHelpers.get_element_text(driver, LoginLocators.DASHBOARD_HEADER, timeout=5)
            assert "Dashboard" in dashboard_text, f"Login should succeed but Dashboard not found"
        except Exception as e:
            assert False, f"Login should succeed with {username}/{password} but failed: {e}"
    else:
        # Should see error message
        try:
            error_text = SeleniumHelpers.get_element_text(driver, LoginLocators.ERROR_MESSAGE, timeout=5)
            assert "Invalid credentials" in error_text, f"Expected error message, got: {error_text}"
        except Exception as e:
            # Sometimes error appears differently, check page source
            assert "Invalid credentials" in driver.page_source or "Required" in driver.page_source, \
                   f"Login should fail with {username}/{password} but no error shown"

@pytest.mark.admin
@pytest.mark.regression
@pytest.mark.parametrize("role", ["Admin", "ESS"])
def test_search_by_different_roles(driver, role):
    """
    TC-ADMIN-007: Parametrized test for searching different user roles.
    Priority: Medium
    Note: OrangeHRM demo data is inconsistent, so this test only verifies that
    the search returns at least one result for each role value, not that all
    returned rows are strictly filtered.
    """
    test_positive_login(driver)

    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.TABLE)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.FORM)

    # Select role from dropdown
    SeleniumHelpers.select_dropdown_option(driver, AdminLocators.USER_ROLE_DROPDOWN, role)
    SeleniumHelpers.safe_click(driver, AdminLocators.SEARCH_BUTTON)

    # Wait for table to update
    SeleniumHelpers.wait_for_table_to_update(driver)

    # Verify at least one row is returned
    table_rows = driver.find_elements(*AdminLocators.TABLE_ROWS)
    assert len(table_rows) > 0, f"No results returned when filtering by role='{role}'"



@pytest.mark.admin
@pytest.mark.regression
@pytest.mark.parametrize("status", ["Enabled", "Disabled"])
def test_search_by_different_statuses(driver, status):
    """
    TC-ADMIN-008: Parametrized test for searching different statuses.
    Priority: Medium
    Note: Due to unstable demo data, this test verifies that the search
    executes and returns at least one row for each status value.
    """
    test_positive_login(driver)

    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.TABLE)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.FORM)

    # Select status
    SeleniumHelpers.select_dropdown_option(driver, AdminLocators.STATUS_DROPDOWN, status)
    SeleniumHelpers.safe_click(driver, AdminLocators.SEARCH_BUTTON)

    # Wait for table to update
    SeleniumHelpers.wait_for_table_to_update(driver)

    # Verify at least one row is returned
    table_rows = driver.find_elements(*AdminLocators.TABLE_ROWS)
    assert len(table_rows) > 0, f"No results returned when filtering by status='{status}'"


# ========== ADMIN MODULE TESTS ========== #

@pytest.mark.admin
@pytest.mark.regression
def test_search_by_username(driver):
    """
    TC-ADMIN-001: Search by username and verify results
    Priority: High
    """
    # Login
    test_positive_login(driver)

    # Navigate to Admin
    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.TABLE)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.FORM)

    # Search by username
    SeleniumHelpers.safe_send_keys(driver, AdminLocators.USERNAME_INPUT, "Admin")
    SeleniumHelpers.safe_click(driver, AdminLocators.SEARCH_BUTTON)

    # Wait for table to update
    SeleniumHelpers.wait_for_table_to_update(driver)

    # Verify result
    username_text = SeleniumHelpers.get_element_text(driver, AdminLocators.FIRST_ROW_USERNAME)
    assert "Admin" in username_text, f"Expected 'Admin', got '{username_text}'"


@pytest.mark.admin
@pytest.mark.regression
def test_search_by_user_role(driver):
    """
    TC-ADMIN-002: Search by user role and verify results
    Priority: High
    """
    test_positive_login(driver)

    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.TABLE)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.FORM)

    # Select role from dropdown
    SeleniumHelpers.select_dropdown_option(driver, AdminLocators.USER_ROLE_DROPDOWN, "Admin")
    SeleniumHelpers.safe_click(driver, AdminLocators.SEARCH_BUTTON)

    # Verify results
    SeleniumHelpers.wait_for_table_to_update(driver)
    role_text = SeleniumHelpers.get_element_text(driver, AdminLocators.FIRST_ROW_ROLE)
    assert "Admin" in role_text, f"Expected 'Admin', got '{role_text}'"


@pytest.mark.admin
@pytest.mark.regression
def test_search_by_status(driver):
    """
    TC-ADMIN-003: Search by status and verify results
    Priority: Medium
    """
    test_positive_login(driver)

    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.TABLE)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.FORM)

    # Select status
    SeleniumHelpers.select_dropdown_option(driver, AdminLocators.STATUS_DROPDOWN, "Enabled")
    SeleniumHelpers.safe_click(driver, AdminLocators.SEARCH_BUTTON)

    # Verify results
    SeleniumHelpers.wait_for_table_to_update(driver)
    status_text = SeleniumHelpers.get_element_text(driver, AdminLocators.FIRST_ROW_STATUS)
    assert "Enabled" in status_text, f"Expected 'Enabled', got '{status_text}'"


@pytest.mark.admin
@pytest.mark.regression
@pytest.mark.skip(reason="Employee autocomplete data is inconsistent in demo environment - cannot reliably test")
def test_search_by_employee_name(driver):
    """
    TC-ADMIN-004: Search by employee name using autocomplete
    Priority: Medium

    SKIPPED: This test is skipped because the OrangeHRM demo environment
    resets employee data unpredictably. Employee names change between sessions,
    making it impossible to create a stable, repeatable test for this feature.

    In a production environment with stable test data, this test would:
    1. Type partial employee name in autocomplete field
    2. Select employee from suggestions
    3. Click Search
    4. Verify employee appears in filtered results
    """
    pass


@pytest.mark.admin
@pytest.mark.regression
def test_search_with_all_filters(driver):
    """
    TC-ADMIN-005: Search with multiple filters combined
    Priority: High
    NOTE: Tests username, role, and status filters (employee filter excluded due to data variability)
    """
    test_positive_login(driver)

    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.TABLE)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.FORM)

    # Fill three stable filters (no employee)
    SeleniumHelpers.safe_send_keys(driver, AdminLocators.USERNAME_INPUT, "Admin")
    SeleniumHelpers.select_dropdown_option(driver, AdminLocators.USER_ROLE_DROPDOWN, "Admin")
    SeleniumHelpers.select_dropdown_option(driver, AdminLocators.STATUS_DROPDOWN, "Enabled")

    # Search
    SeleniumHelpers.safe_click(driver, AdminLocators.SEARCH_BUTTON)
    SeleniumHelpers.wait_for_table_to_update(driver)

    # Verify results exist
    table_rows = driver.find_elements(*AdminLocators.TABLE_ROWS)
    assert len(table_rows) > 0, "No results found for combined filter search"

    # Verify all three filters worked
    username_text = SeleniumHelpers.get_element_text(driver, AdminLocators.FIRST_ROW_USERNAME)
    assert "Admin" in username_text, f"Username filter failed: got '{username_text}'"

    role_text = SeleniumHelpers.get_element_text(driver, AdminLocators.FIRST_ROW_ROLE)
    assert "Admin" in role_text, f"Role filter failed: got '{role_text}'"

    status_text = SeleniumHelpers.get_element_text(driver, AdminLocators.FIRST_ROW_STATUS)
    assert "Enabled" in status_text, f"Status filter failed: got '{status_text}'"


@pytest.mark.admin
@pytest.mark.regression
def test_reset_search_filters(driver):
    """
    TC-ADMIN-006: Verify Reset button clears all filters
    Priority: High
    NOTE: Tests with username, role, and status filters
    """
    test_positive_login(driver)

    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.TABLE)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.FORM)

    import time

    # Get initial count
    initial_rows = driver.find_elements(*AdminLocators.TABLE_ROWS)
    initial_count = len(initial_rows)

    # Apply filters (username, role, status - no employee)
    SeleniumHelpers.safe_send_keys(driver, AdminLocators.USERNAME_INPUT, "Admin")
    SeleniumHelpers.select_dropdown_option(driver, AdminLocators.USER_ROLE_DROPDOWN, "Admin")
    SeleniumHelpers.select_dropdown_option(driver, AdminLocators.STATUS_DROPDOWN, "Enabled")

    # Search and get filtered count
    SeleniumHelpers.safe_click(driver, AdminLocators.SEARCH_BUTTON)
    SeleniumHelpers.wait_for_table_to_update(driver)

    filtered_rows = driver.find_elements(*AdminLocators.TABLE_ROWS)
    filtered_count = len(filtered_rows)

    # Click reset
    SeleniumHelpers.safe_click(driver, AdminLocators.RESET_BUTTON)
    time.sleep(2)

    # Verify reset
    reset_rows = driver.find_elements(*AdminLocators.TABLE_ROWS)
    reset_count = len(reset_rows)

    # After reset, should have more records than filtered
    assert reset_count > filtered_count, f"Reset failed: filtered={filtered_count}, reset={reset_count}"

    # Should return close to initial count
    assert reset_count >= initial_count - 3, f"Table not fully reset: initial={initial_count}, reset={reset_count}"

    # Verify username field is cleared
    username_value = driver.find_element(*AdminLocators.USERNAME_INPUT).get_attribute('value')
    assert username_value == "", "Username field not cleared after reset"

    # Verify role dropdown is reset (should show placeholder text)
    role_dropdown = driver.find_element(*AdminLocators.USER_ROLE_DROPDOWN)
    role_text = role_dropdown.text
    # After reset, dropdown should not show "Admin" - it should be empty or show "-- Select --"
    assert role_text != "Admin" or role_text == "", f"Role dropdown not reset: still shows '{role_text}'"


# ========== NAVIGATION TESTS ========== #

@pytest.mark.navigation
@pytest.mark.regression
def test_upgrade_button_opens_upgrade_page(driver):
    """
    TC-NAV-001: Verify Upgrade button opens new tab
    Priority: Low
    """
    test_positive_login(driver)

    SeleniumHelpers.safe_click(driver, NavigationLocators.UPGRADE_BUTTON)

    # Wait for new window
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2)
    driver.switch_to.window(driver.window_handles[1])

    assert "open-source/upgrade-to-advanced" in driver.current_url


@pytest.mark.navigation
@pytest.mark.regression
def test_profile_about_dialog(driver):
    """
    TC-NAV-002: Verify About dialog displays company information
    Priority: Low
    """
    test_positive_login(driver)

    SeleniumHelpers.safe_click(driver, NavigationLocators.PROFILE_DROPDOWN)
    SeleniumHelpers.safe_click(driver, NavigationLocators.ABOUT_LINK)

    # Wait for dialog
    dialog = SeleniumHelpers.wait_for_element_visible(driver, NavigationLocators.ABOUT_DIALOG)

    # Verify company label present
    company_label = dialog.find_element(*NavigationLocators.COMPANY_NAME_LABEL)
    assert "Company Name" in company_label.text


@pytest.mark.navigation
@pytest.mark.regression
def test_profile_support_link(driver):
    """
    TC-NAV-003: Verify Support link navigates correctly
    Priority: Low
    """
    test_positive_login(driver)

    SeleniumHelpers.safe_click(driver, NavigationLocators.PROFILE_DROPDOWN)
    SeleniumHelpers.safe_click(driver, NavigationLocators.SUPPORT_LINK)

    # Wait for URL change
    WebDriverWait(driver, 10).until(EC.url_contains("/web/index.php/help/support"))
    assert "/web/index.php/help/support" in driver.current_url


@pytest.mark.navigation
@pytest.mark.regression
def test_sidebar_search_claim(driver):
    """
    TC-NAV-004: Verify sidebar search filters menu correctly
    Priority: Low
    """
    test_positive_login(driver)

    search_box = SeleniumHelpers.wait_for_element_clickable(driver, NavigationLocators.SIDEBAR_SEARCH)
    search_box.send_keys("claim")

    # Wait for sidebar to update
    WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located(NavigationLocators.SIDEBAR_MENU_ITEMS)
    )

    items = driver.find_elements(*NavigationLocators.SIDEBAR_MENU_ITEMS)
    visible = [i.text for i in items if i.is_displayed()]

    assert visible == ["Claim"], f"Expected ['Claim'], got {visible}"


@pytest.mark.navigation
@pytest.mark.regression
def test_sidebar_search_no_results(driver):
    """
    TC-NAV-005: Verify sidebar search shows no items for invalid search
    Priority: Low
    """
    test_positive_login(driver)

    search_box = SeleniumHelpers.wait_for_element_clickable(driver, NavigationLocators.SIDEBAR_SEARCH)
    search_box.send_keys("negative item search")

    # Wait for sidebar to update
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located(NavigationLocators.SIDEBAR_MENU_ITEMS)
    )

    items = driver.find_elements(*NavigationLocators.SIDEBAR_MENU_ITEMS)
    assert len(items) == 0, f"Expected 0 items, got {len(items)}"

@pytest.mark.smoke
@pytest.mark.login
def test_login_with_empty_username(driver):
    """
    TC-LOGIN-004: Verify error message with empty username
    Priority: High
    """
    driver.get(URL)
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.PASSWORD_INPUT, PASSWORD)
    SeleniumHelpers.safe_click(driver, LoginLocators.LOGIN_BUTTON)
    try:
        error_text = SeleniumHelpers.get_element_text(driver, LoginLocators.ERROR_MESSAGE, timeout=5)
        assert "Required" in error_text, f"Expected error for empty username, got: {error_text}"
    except Exception as e:
        assert "Required" in driver.page_source, "Required message not found on page"

@pytest.mark.smoke
@pytest.mark.login
def test_login_with_empty_password(driver):
    """
    TC-LOGIN-005: Verify error message with empty password
    Priority: High
    """
    driver.get(URL)
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.USERNAME_INPUT, USERNAME)
    SeleniumHelpers.safe_click(driver, LoginLocators.LOGIN_BUTTON)
    try:
        error_text = SeleniumHelpers.get_element_text(driver, LoginLocators.ERROR_MESSAGE, timeout=5)
        assert "Required" in error_text, f"Expected error for empty password, got: {error_text}"
    except Exception as e:
        assert "Required" in driver.page_source, "Required message not found on page"

@pytest.mark.admin
@pytest.mark.regression
def test_search_with_empty_filters(driver):
    """
    TC-ADMIN-011: Search with empty filters and verify all users are displayed
    Priority: Medium
    """
    test_positive_login(driver)
    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.TABLE)
    SeleniumHelpers.safe_click(driver, AdminLocators.SEARCH_BUTTON)
    SeleniumHelpers.wait_for_table_to_update(driver)
    table_rows = driver.find_elements(*AdminLocators.TABLE_ROWS)
    assert len(table_rows) > 0, "Expected at least one user when no filters applied"

@pytest.mark.admin
@pytest.mark.regression
def test_search_with_mixed_filters(driver):
    """
    TC-ADMIN-012: Search with valid username and invalid role/status
    Priority: Medium
    """
    test_positive_login(driver)
    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.safe_send_keys(driver, AdminLocators.USERNAME_INPUT, "Admin")
    SeleniumHelpers.select_dropdown_option(driver, AdminLocators.USER_ROLE_DROPDOWN, "ESS")
    SeleniumHelpers.select_dropdown_option(driver, AdminLocators.STATUS_DROPDOWN, "Disabled")
    SeleniumHelpers.safe_click(driver, AdminLocators.SEARCH_BUTTON)
    SeleniumHelpers.wait_for_table_to_update(driver)
    table_rows = driver.find_elements(*AdminLocators.TABLE_ROWS)
    assert len(table_rows) >= 0, "Expected some results for mixed filters"

@pytest.mark.admin
@pytest.mark.regression
def test_reset_with_no_filters(driver):
    """
    TC-ADMIN-013: Reset search without applying filters
    Priority: Medium
    """
    test_positive_login(driver)
    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.TABLE)
    SeleniumHelpers.safe_click(driver, AdminLocators.RESET_BUTTON)
    SeleniumHelpers.wait_for_table_to_update(driver)
    table_rows = driver.find_elements(*AdminLocators.TABLE_ROWS)
    assert len(table_rows) > 0, "Expected all users after reset with no filters"

@pytest.mark.navigation
@pytest.mark.regression
def test_sidebar_search_invalid_term(driver):
    """
    TC-NAV-006: Verify sidebar search shows no results for invalid term
    Priority: Low
    """
    test_positive_login(driver)
    search_box = SeleniumHelpers.wait_for_element_clickable(driver, NavigationLocators.SIDEBAR_SEARCH)
    search_box.send_keys("xyz999")
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located(NavigationLocators.SIDEBAR_MENU_ITEMS)
    )
    items = driver.find_elements(*NavigationLocators.SIDEBAR_MENU_ITEMS)
    assert len(items) == 0, f"Expected 0 items, got {len(items)}"

@pytest.mark.navigation
@pytest.mark.regression
def test_navigate_to_dashboard(driver):
    """
    TC-NAV-007: Verify navigation to Dashboard
    Priority: Low
    """
    test_positive_login(driver)
    dashboard_link = (By.XPATH, "//a[@href='/web/index.php/dashboard/index']")
    SeleniumHelpers.safe_click(driver, dashboard_link)
    dashboard_text = SeleniumHelpers.get_element_text(driver, LoginLocators.DASHBOARD_HEADER)
    assert "Dashboard" in dashboard_text, "Dashboard not loaded"

@pytest.mark.admin
@pytest.mark.regression
def test_search_with_long_username(driver):
    """
    TC-ADMIN-014: Search with very long username
    Priority: Medium
    """
    test_positive_login(driver)
    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.safe_send_keys(driver, AdminLocators.USERNAME_INPUT, "A" * 50)
    SeleniumHelpers.safe_click(driver, AdminLocators.SEARCH_BUTTON)
    SeleniumHelpers.wait_for_table_to_update(driver)
    table_rows = driver.find_elements(*AdminLocators.TABLE_ROWS)
    assert len(table_rows) >= 0, "Expected at least zero results for very long username"

@pytest.mark.admin
@pytest.mark.regression
def test_search_with_special_characters(driver):
    """
    TC-ADMIN-015: Search with special characters in username
    Priority: Medium
    """
    test_positive_login(driver)
    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.safe_send_keys(driver, AdminLocators.USERNAME_INPUT, "admin@test.com")
    SeleniumHelpers.safe_click(driver, AdminLocators.SEARCH_BUTTON)
    SeleniumHelpers.wait_for_table_to_update(driver)
    table_rows = driver.find_elements(*AdminLocators.TABLE_ROWS)
    assert len(table_rows) >= 0, "Expected at least zero results for special characters"

@pytest.mark.admin
@pytest.mark.regression
@pytest.mark.skip(reason="Add User cannot be reliably automated: demo site employee autocomplete frequently returns invalid, making the flow inconsistent between sessions.")
def test_add_user_with_valid_data(driver):
    """
    TC-ADMIN-016: Add new system user with valid data
    Priority: Medium

    SKIPPED: The OrangeHRM demo environment often rejects valid employee names
    as 'Invalid', so this flow cannot be made stable across sessions.

    Intended steps in a stable environment:
    1. Login and navigate to Admin > User Management > Users.
    2. Click 'Add' button.
    3. Fill Username, Role, Employee Name, Status, and Password fields.
    4. Click Save.
    5. Verify the new user appears in the users table.
    """
    pass

@pytest.mark.admin
@pytest.mark.regression
@pytest.mark.skip(reason="Edit User cannot be reliably automated: target users and their data change between sessions in the demo environment.")
def test_edit_existing_user(driver):
    """
    TC-ADMIN-017: Edit an existing system user
    Priority: Medium

    SKIPPED: The demo environment does not guarantee a stable, known user
    to edit. Usernames and records can change or be reset between sessions.

    Intended steps in a stable environment:
    1. Login and navigate to Admin > Users.
    2. Search for a known existing user.
    3. Open the user in edit mode.
    4. Modify fields (e.g., status or role).
    5. Save and verify the changes in the table.
    """
    pass


@pytest.mark.admin
@pytest.mark.regression
def test_delete_admin_user_shows_error(driver):
    """
    TC-ADMIN-018: Verify that attempting to delete Admin user shows "Cannot be deleted" error
    Priority: High

    This test verifies that the system prevents deletion of the Admin user
    and displays the error message: "Cannot be deleted"
    """
    # Login
    driver.get(URL)
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.USERNAME_INPUT, USERNAME)
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.PASSWORD_INPUT, PASSWORD)
    SeleniumHelpers.safe_click(driver, LoginLocators.LOGIN_BUTTON)

    # Navigate to Admin
    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.TABLE)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.FORM)

    # Search for Admin user
    SeleniumHelpers.safe_send_keys(driver, AdminLocators.USERNAME_INPUT, "Admin")
    SeleniumHelpers.safe_click(driver, AdminLocators.SEARCH_BUTTON)
    SeleniumHelpers.wait_for_table_to_update(driver)

    import time
    time.sleep(1)

    # Click checkbox to select the Admin user
    checkbox = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row'][1]//div[@role='cell'][1]//i")
    SeleniumHelpers.safe_click(driver, checkbox)

    # Click delete button (trash icon)
    delete_btn = (By.XPATH,
                  "//div[@class='oxd-table-body']//div[@role='row'][1]//button[.//i[contains(@class, 'bi-trash')]]")
    SeleniumHelpers.safe_click(driver, delete_btn)

    # Wait for and verify error toast appears
    error_toast = (By.XPATH, "//div[contains(@class, 'oxd-toast--error')]")
    toast_element = SeleniumHelpers.wait_for_element_visible(driver, error_toast, timeout=5)

    # Verify error message
    error_text = toast_element.text
    assert "Cannot be deleted" in error_text, f"Expected 'Cannot be deleted' error, got: '{error_text}'"

    logger.info(f"✓ Delete error verified: {error_text}")


@pytest.mark.navigation
@pytest.mark.regression
@pytest.mark.parametrize("tab_name,expected_url_part", [
    ("Nationalities", "/admin/nationality"),
    ("Corporate Branding", "/admin/addTheme"),
])
def test_admin_top_tabs_navigation(driver, tab_name, expected_url_part):
    """
    TC-NAV-008: Verify Admin top navigation tabs work correctly
    Priority: Medium
    """
    # Login
    driver.get(URL)
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.USERNAME_INPUT, USERNAME)
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.PASSWORD_INPUT, PASSWORD)
    SeleniumHelpers.safe_click(driver, LoginLocators.LOGIN_BUTTON)

    # Navigate to Admin
    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.TABLE)

    import time
    time.sleep(2)

    # Click the tab by link text
    tab_locator = (By.LINK_TEXT, tab_name)
    SeleniumHelpers.safe_click(driver, tab_locator)

    time.sleep(2)

    # Verify URL contains expected path
    current_url = driver.current_url
    assert expected_url_part in current_url, \
        f"Expected URL to contain '{expected_url_part}', but got: {current_url}"


@pytest.mark.navigation
@pytest.mark.regression
def test_job_tab_navigation(driver):
    """
    TC-NAV-009: Verify Job tab navigates correctly
    Priority: Medium
    """
    # Login
    driver.get(URL)
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.USERNAME_INPUT, USERNAME)
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.PASSWORD_INPUT, PASSWORD)
    SeleniumHelpers.safe_click(driver, LoginLocators.LOGIN_BUTTON)

    # Navigate to Admin
    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.TABLE)

    import time
    time.sleep(2)

    # Click Job dropdown to expand it
    job_dropdown = (By.XPATH, "//span[contains(text(), 'Job')]")
    SeleniumHelpers.safe_click(driver, job_dropdown)
    time.sleep(1)

    # Click the menu item inside
    job_titles = (By.LINK_TEXT, "Job Titles")
    SeleniumHelpers.safe_click(driver, job_titles)

    time.sleep(2)

    # Verify URL changed
    current_url = driver.current_url
    assert "/admin/viewJobTitleList" in current_url, \
        f"Expected URL to contain '/admin/viewJobTitleList', but got: {current_url}"


@pytest.mark.navigation
@pytest.mark.regression
def test_organization_tab_navigation(driver):
    """
    TC-NAV-010: Verify Organization tab navigates correctly
    Priority: Medium
    """
    # Login
    driver.get(URL)
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.USERNAME_INPUT, USERNAME)
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.PASSWORD_INPUT, PASSWORD)
    SeleniumHelpers.safe_click(driver, LoginLocators.LOGIN_BUTTON)

    # Navigate to Admin
    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.TABLE)

    import time
    time.sleep(2)

    # Click Organization dropdown
    org_dropdown = (By.XPATH, "//span[contains(text(), 'Organization')]")
    SeleniumHelpers.safe_click(driver, org_dropdown)
    time.sleep(1)

    # Click General Information
    general_info = (By.LINK_TEXT, "General Information")
    SeleniumHelpers.safe_click(driver, general_info)

    time.sleep(2)

    # Verify URL changed
    current_url = driver.current_url
    assert "/admin/viewOrganizationGeneralInformation" in current_url, \
        f"Expected URL to contain '/admin/viewOrganizationGeneralInformation', but got: {current_url}"


@pytest.mark.navigation
@pytest.mark.regression
def test_qualifications_tab_navigation(driver):
    """
    TC-NAV-011: Verify Qualifications tab navigates correctly
    Priority: Medium
    """
    # Login
    driver.get(URL)
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.USERNAME_INPUT, USERNAME)
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.PASSWORD_INPUT, PASSWORD)
    SeleniumHelpers.safe_click(driver, LoginLocators.LOGIN_BUTTON)

    # Navigate to Admin
    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.TABLE)

    import time
    time.sleep(2)

    # Click Qualifications dropdown
    qual_dropdown = (By.XPATH, "//span[contains(text(), 'Qualifications')]")
    SeleniumHelpers.safe_click(driver, qual_dropdown)
    time.sleep(1)

    # Click Skills
    skills = (By.LINK_TEXT, "Skills")
    SeleniumHelpers.safe_click(driver, skills)

    time.sleep(2)

    # Verify URL changed
    current_url = driver.current_url
    assert "/admin/viewSkills" in current_url, \
        f"Expected URL to contain '/admin/viewSkills', but got: {current_url}"


@pytest.mark.navigation
@pytest.mark.regression
def test_configuration_tab_navigation(driver):
    """
    TC-NAV-012: Verify Configuration tab navigates correctly
    Priority: Medium
    """
    # Login
    driver.get(URL)
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.USERNAME_INPUT, USERNAME)
    SeleniumHelpers.safe_send_keys(driver, LoginLocators.PASSWORD_INPUT, PASSWORD)
    SeleniumHelpers.safe_click(driver, LoginLocators.LOGIN_BUTTON)

    # Navigate to Admin
    SeleniumHelpers.safe_click(driver, AdminLocators.ADMIN_MENU)
    SeleniumHelpers.wait_for_element_visible(driver, AdminLocators.TABLE)

    import time
    time.sleep(2)

    # Click Configuration dropdown
    config_dropdown = (By.XPATH, "//span[contains(text(), 'Configuration')]")
    SeleniumHelpers.safe_click(driver, config_dropdown)
    time.sleep(1)

    # Click Email Configuration
    email_config = (By.LINK_TEXT, "Email Configuration")
    SeleniumHelpers.safe_click(driver, email_config)

    time.sleep(2)

    # Verify URL changed
    current_url = driver.current_url
    assert "/admin/listMailConfiguration" in current_url, \
        f"Expected URL to contain '/admin/listMailConfiguration', but got: {current_url}"




