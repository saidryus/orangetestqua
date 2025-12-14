## Project overview
This is an automated UI testing project built with pytest + Selenium against the OrangeHRM demo website (https://opensource-demo.orangehrmlive.com/...).​
Tests are organized by feature area (Login, Admin, Navigation) and use reusable helper methods to make Selenium more stable.

## Folder & file map 
- tests/test_admin.py: Main test suite file containing:
  - Test cases (functions starting with test_...) for Login, Admin module searches, navigation checks, etc.
  - Locator classes: LoginLocators, AdminLocators, NavigationLocators (central place for XPaths/CSS selectors).
  - Test data constants (URL, username/password).
------------------------  
- utils/helpers.py: Reusable Selenium utilities used by tests:
  - safe_click() = waits for element to be clickable; if it fails, tries JavaScript click.
  - safe_send_keys() = waits and types into inputs (optionally clears first). 
  - wait_for_element_visible() / wait_for_element_clickable() = explicit waits wrappers. 
  - wait_for_table_to_update() = OrangeHRM-specific “table has rows” wait. 
  - select_dropdown_option() and select_autocomplete_option() for OrangeHRM’s custom dropdown/autocomplete controls.
------------------------ 
- conftest.py: Pytest configuration file that provides shared fixtures and hooks:
  - driver fixture: starts Chrome using webdriver-manager, sets window and waits, yields driver to each test, then quits after test. 
  - Screenshot-on-failure hook: saves screenshots into screenshots/ when a test fails. 
  - wait fixture: returns a reusable WebDriverWait object.
------------------------ 
- pytest.ini: Project-wide pytest configuration:

  - Registers markers like smoke, regression, admin, login, navigation. 
  - Sets test discovery patterns and CLI defaults (e.g., verbose output and HTML report generation). 
  - reports/report.html: Generated HTML report after a pytest run (from pytest-html). 
  - screenshots/: Auto-saved screenshots when tests fail (helpful for debugging locators/timing).