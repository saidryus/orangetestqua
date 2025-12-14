# OrangeHRM Test Automation Project

Automated testing suite for OrangeHRM Admin Module using Selenium
WebDriver, Python, and Pytest.

## Project Overview

-   **Application Under Test:** OrangeHRM Demo
    (https://opensource-demo.orangehrmlive.com)
-   **Module Tested:** Admin - User Management - System Users
-   **Framework:** Pytest + Selenium WebDriver
-   **Language:** Python 3.13.9
-   **Design Pattern:** Helper Functions with Centralized Locators
-   **Author:** Simone Dominique Makinano
-   **Date:** December 2025

## Features

-   39 test functions covering 45+ test scenarios
-   Automatic screenshot capture on test failure
-   HTML test reports with pytest-html
-   Reusable helper utilities for Selenium operations
-   Custom pytest markers for test organization (5 markers)
-   Comprehensive logging with custom logger
-   Webdriver-manager for automatic ChromeDriver management
-   Parametrized tests for data-driven testing (4 parametrized tests)
-   Admin module navigation tests (tab and dropdown navigation)
-   User management operations (delete validation)
-   Edge case testing (long usernames, special characters)

## Project Structure
``` text
TESTQUAFINALS/ 
├── tests/ 
│ ├── init.py 
│ ├── test_admin.py # All test cases (39 functions, 45 scenarios) 
│ └── conftest.py \# Pytest fixtures and hooks 
├── utils/ 
│ ├── init.py 
│ └── helpers.py # SeleniumHelpers class with reusable methods 
├── screenshots/ \# Auto-generated
screenshots/ on test failure 
├── reports/ # HTML test reports 
├── pytest.ini # Pytest configuration and markers 
├── TEST_PLAN.md # Detailed test plan documentation 
├── PYTEST_FEATURES.md # Pytest
implementation details 
├── README.md \# This file 
└── requirements.txt # Python dependencies 
```
## Installation

### Prerequisites

-   Python 3.8 or higher (tested with Python 3.13.9)
-   Google Chrome browser (v143+)
-   pip (Python package manager)

### Setup Steps

1.  **Clone or download the project** 
   - cd TESTQUAFINALS
2.  **Create virtual environment (WINDOWS)** 
   - python -m venv .venv 
   - .venv`\Scripts`{=tex}`\activate`{=tex}
3.  **Install dependencies** 
   - pip install -r requirements.txt

## Running Tests

### Run All Tests

pytest tests/test_admin.py -v 

### Run with HTML Report

pytest tests/test_admin.py --html=reports/report.html
--self-contained-html 

### Run Specific Test Categories

### Smoke tests only (5 tests) 
- pytest -m smoke -v

### Admin module tests only (13 tests) 
- pytest -m admin -v

### Regression tests only (8 tests) 
- pytest -m regression -v

### Login tests only (5 tests) 
- pytest -m login -v

### Navigation tests only (12 tests) 
- pytest -m navigation -v 

### Run Specific Test
- pytest tests/test_admin

### Single test function 
- pytest tests/test_admin.py::test_positive_login -v

### Delete user error test 
- pytest tests/test_admin.py::test_delete_admin_user_shows_error -v

### Navigation tests 
- pytest tests/test_admin.py::test_admin_top_tabs_navigation -v 

### Run all parametrized tests 
- pytest -k "multiple or different or tabs" -v

### Run all navigation tests 
- pytest -k "navigation" -v

### Run delete test 
- pytest -k "delete" -v 

## Advanced Execution Options

### Stop on first failure 
- pytest tests/test_admin.py -x

### Run with print output visible 
- pytest tests/test_admin.py -v -s

### Rerun last failed tests 
- pytest --lf 


## Test Cases

### Login Tests (5 tests)
| Test ID | Test Name | Priority | Type | Status |
|---------|-----------|----------|------|--------|
| TC-LOGIN-001 | Positive Login | High | Smoke | Running |
| TC-LOGIN-002 | Negative Login | High | Smoke | Running |
| TC-LOGIN-003 | Parametrized Login (3 scenarios) | High | Smoke | Running |
| TC-LOGIN-004 | Empty Username Login | High | Smoke | Running |
| TC-LOGIN-005 | Empty Password Login | High | Smoke | Running |

### Admin Search Tests (13 tests)
| Test ID | Test Name | Priority | Type | Status |
|---------|-----------|----------|------|--------|
| TC-ADMIN-001 | Search by Username | High | Functional | Running |
| TC-ADMIN-002 | Search by User Role | High | Functional | Running |
| TC-ADMIN-003 | Search by Status | Medium | Functional | Running |
| TC-ADMIN-004 | Search by Employee Name | Medium | Functional | Skipped* |
| TC-ADMIN-005 | Combined Filter Search | High | Regression | Running |
| TC-ADMIN-006 | Reset Search Filters | High | Regression | Running |
| TC-ADMIN-007 | Search Different Roles (2 scenarios) | Medium | Regression | Running |
| TC-ADMIN-008 | Search Different Statuses (2 scenarios) | Medium | Regression | Running |
| TC-ADMIN-011 | Search with Empty Filters | Medium | Functional | Running |
| TC-ADMIN-012 | Search with Mixed Filters | Medium | Functional | Running |
| TC-ADMIN-013 | Reset with No Filters | Medium | Functional | Running |
| TC-ADMIN-014 | Search with Long Username | Medium | Edge Case | Running |
| TC-ADMIN-015 | Search with Special Characters | Medium | Edge Case | Running |
| TC-ADMIN-016 | Add User | Medium | Functional | Skipped* |
| TC-ADMIN-017 | Edit User | Medium | Functional | Skipped* |
| TC-ADMIN-018 | Delete Admin User Error | High | Functional | Running |

### Navigation Tests (12 tests)
| Test ID | Test Name | Priority | Type | Status |
|---------|-----------|----------|------|--------|
| TC-NAV-001 | Upgrade Button | Low | Functional | Running |
| TC-NAV-002 | Profile About Dialog | Low | Functional | Running |
| TC-NAV-003 | Profile Support Link | Low | Functional | Running |
| TC-NAV-004 | Sidebar Search Valid | Low | Functional | Running |
| TC-NAV-005 | Sidebar Search No Results | Low | Functional | Running |
| TC-NAV-006 | Sidebar Search Invalid | Low | Functional | Running |
| TC-NAV-007 | Navigate to Dashboard | Low | Functional | Running |
| TC-NAV-008 | Admin Top Tabs (2 scenarios) | Medium | Functional | Running |
| TC-NAV-009 | Job Dropdown Navigation | Medium | Functional | Running |
| TC-NAV-010 | Organization Dropdown | Medium | Functional | Running |
| TC-NAV-011 | Qualifications Dropdown | Medium | Functional | Running |
| TC-NAV-012 | Configuration Dropdown | Medium | Functional | Running |

**Total Test Functions:** 39  
**Total Test Scenarios:** 45 (with parametrization)  
**Automated & Running:** 36  
**Skipped:** 3 (documented demo environment limitations)  
**Pass Rate:** 92%

*Skipped tests due to OrangeHRM demo environment limitations (employee autocomplete instability).

## Test Reports

After running tests:
- **HTML Report:** `reports/report.html` - Open in browser for detailed results with execution times, pass/fail status, and metadata
- **Screenshots:** `screenshots/` - Automatic screenshots of failed tests with timestamps (format: `testname_YYYYMMDD_HHMMSS.png`)
- **Console Output:** Real-time test execution logs with custom logging from SeleniumHelpers

## Configuration

### Test Data
Located in `tests/test_admin.py`:


URL =
"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = 'Admin' PASSWORD = 'admin123' 

### Wait Times
Configured in `conftest.py` and `utils/helpers.py`:
- IMPLICIT_WAIT = 5 # seconds (browser-level)
- EXPLICIT_WAIT = 10 # seconds (helper methods default)


### Pytest Markers
Defined in `pytest.ini`:
- `@pytest.mark.smoke` - Critical path tests (5 tests)
- `@pytest.mark.regression` - Full regression suite (8 tests)
- `@pytest.mark.admin` - Admin module tests (13 tests)
- `@pytest.mark.login` - Login tests (5 tests)
- `@pytest.mark.navigation` - Navigation tests (12 tests)

## Helper Utilities

### SeleniumHelpers Class
Located in `utils/helpers.py`, provides:

### Safe clicking with JavaScript fallback
SeleniumHelpers.safe_click(driver, locator, timeout=10)

### Safe text input with clear option 
SeleniumHelpers.safe_send_keys(driver, locator, text, timeout=10, clear_first=True)

### Wait for element visibility
SeleniumHelpers.wait_for_element_visible(driver, locator, timeout=10)

### Wait for element to be clickable
SeleniumHelpers.wait_for_element_clickable(driver, locator, timeout=10)

### Get element text with wait 
SeleniumHelpers.get_element_text(driver,locator, timeout=10)

### Handle custom dropdowns 
SeleniumHelpers.select_dropdown_option(driver,dropdown_locator, option_text, timeout=10)

### Wait for table updates 
SeleniumHelpers.wait_for_table_to_update(driver, timeout=10) 


All methods include:
- Built-in explicit waits
- Logging for debugging
- Error handling with fallback mechanisms
- Descriptive error messages

## Troubleshooting

### ChromeDriver Issues
The project uses webdriver-manager for automatic ChromeDriver download. If issues occur:

pip install --upgrade webdriver-manager 

### Element Not Found
-   Ensure browser is maximized (handled automatically in `conftest.py`)
-   Check if OrangeHRM demo site is accessible:
    https://opensource-demo.orangehrmlive.com
-   Review screenshots in `screenshots/` folder for visual debugging
-   Check console logs for detailed error messages from SeleniumHelpers

### Tests Fail Randomly

-   Check internet connection stability
-   Increase wait times in helper methods if needed (default is 10
    seconds)
-   Run individual tests to isolate issues:
    `pytest tests/test_admin.py::test_name -v`
-   Review HTML report for failure patterns
-   Check if demo site has changed structure (locators may need updates)

### Test Execution is Slow

-   Typical execution time: 5-7 minutes for full suite (39 tests)
-   Consider running specific test categories using markers
-   Use `pytest -x` to stop on first failure during debugging

## Documentation

-   **TEST_PLAN.md** - Comprehensive test planning documentation with
    all 39 test cases
-   **PYTEST_FEATURES.md** - Pytest framework features, fixtures,
    parametrization, and best practices
-   **Code Comments** - Inline documentation throughout test files with
    TC IDs and priorities
-   **Docstrings** - All test functions include descriptive docstrings

## Dependencies

- selenium==4.x pytest==9.0.2 
- pytest-html==4.1.1 
- pytest-metadata==3.1.1 
- webdriver-manager==4.x See 
See `requirements.txt` for exact versions.

## Key Features

### Pytest Framework Implementation
- **Fixtures:** WebDriver setup/teardown with function scope
- **Parametrization:** 4 tests with 9 total scenarios
- **Markers:** 5 custom markers for flexible test execution
- **Hooks:** Screenshot capture on failure using `pytest_runtest_makereport`
- **Skip Strategy:** 3 tests skipped with documented reasons

### Test Coverage
- **Login:** Valid, invalid, parametrized, empty field scenarios
- **Search:** Username, role, status, combined filters, reset functionality
- **Navigation:** Sidebar, profile, tabs, dropdown menus
- **Edge Cases:** Long inputs, special characters, empty filters
- **User Management:** Delete validation with error verification

### Code Quality
- Centralized locator classes (LoginLocators, AdminLocators, NavigationLocators)
- Reusable helper utilities with error handling
- Consistent naming conventions
- Comprehensive assertions with descriptive messages
- Professional logging throughout

## Contact

**Author:** MAKINANO, SIMONE DOMINIQUE  
**Email:** itsimonemakinano@gmail.com  
**Project Date:** December 2025

## Project Purpose

This is an educational project demonstrating test automation best practices for:
- Selenium WebDriver usage with Python
- Pytest framework implementation (fixtures, parametrization, markers, hooks)
- Test planning and comprehensive documentation
- Professional code organization and maintainability
- Helper utilities and design patterns
- Error handling and debugging strategies

## License

This project is for educational purposes.

---

**Last Updated:** December 14, 2025
