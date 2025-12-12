# OrangeHRM Test Automation Project

Automated testing suite for OrangeHRM Admin Module using Selenium WebDriver, Python, and Pytest.

## Project Overview

- **Application Under Test:** OrangeHRM Demo (https://opensource-demo.orangehrmlive.com)
- **Module Tested:** Admin - User Management - System Users
- **Framework:** Pytest + Selenium WebDriver
- **Language:** Python 3.8+
- **Design Pattern:** Helper Functions with Centralized Locators
- **Author:** Simone Dominique Makinano
- **Date:** December 2025

## Features

- 16 test functions covering 19+ test scenarios
- Automatic screenshot capture on test failure
- HTML test reports with pytest-html
- Reusable helper utilities for Selenium operations
- Custom pytest markers for test organization
- Comprehensive logging
- Webdriver-manager for automatic ChromeDriver management
- Parametrized tests for data-driven testing


## Project Structure
TESTQUAFINALS/
├── tests/
│ └── test_admin.py # All test cases (16 functions)
├── utils/
│ ├── init.py # Package initializer
│ └── helpers.py # Reusable Selenium helper functions
├── screenshots/ # Auto-generated on test failure
├── reports/ # HTML test reports
├── conftest.py # Pytest fixtures and hooks
├── pytest.ini # Pytest configuration
├── TEST_PLAN.md # Detailed test plan documentation
├── PYTEST_FEATURES.md # Pytest implementation details
├── README.md # This file
└── requirements.txt # Python dependencies


## Installation

### Prerequisites
- Python 3.8 or higher
- Google Chrome browser
- pip (Python package manager)

### Setup Steps

1. **Clone or download the project**
   - TESTQUAFINALS
   
2. **Create virtual environment (WINDOWS)**
   - python -m venv venv 
   - venv\Scripts\activate
   - 
3. **Install dependencies**
   - pip install selenium 
   - pip install pytest 
   - pip install pytest-html 
   - pip install webdriver-manager


## Running Tests

### Run All Tests
pytest tests/test_admin.py -v

### Run with HTML Report
pytest --html=reports/report.html --self-contained-html

### Run Specific Test Categories
Smoke tests only
pytest -m smoke -v

Admin module tests only
pytest -m admin -v

Regression tests only
pytest -m regression -v

Login tests only
pytest -m login -v


### Run Specific Test
pytest tests/test_admin.py::test_positive_login -v

### Run Tests by Name Pattern
Run all tests with "search" in name
pytest -k "search" -v

Run all parametrized tests
pytest -k "multiple or different" -v


## Test Cases

| Test ID | Test Name | Priority | Type | Status |
|---------|-----------|----------|------|--------|
| TC-LOGIN-001 | Positive Login | High | Smoke |  Running |
| TC-LOGIN-002 | Negative Login | High | Smoke |  Running |
| TC-LOGIN-003 | Parametrized Login (3 scenarios) | High | Smoke |  Running |
| TC-ADMIN-001 | Search by Username | High | Regression |  Running |
| TC-ADMIN-002 | Search by User Role | High | Regression |  Running |
| TC-ADMIN-003 | Search by Status | Medium | Regression |  Running |
| TC-ADMIN-004 | Search by Employee Name | Medium | Regression | ️ Skipped* |
| TC-ADMIN-005 | Combined Filter Search | High | Regression | Running |
| TC-ADMIN-006 | Reset Search Filters | High | Regression |  Running |
| TC-ADMIN-007 | Search Different Roles (2 scenarios) | Medium | Regression |  Running |
| TC-ADMIN-008 | Search Different Statuses (2 scenarios) | Medium | Regression |  Running |
| TC-NAV-001 | Upgrade Button | Low | Regression |  Running |
| TC-NAV-002 | Profile About Dialog | Low | Regression |  Running |
| TC-NAV-003 | Profile Support Link | Low | Regression |  Running |
| TC-NAV-004 | Sidebar Search Valid | Low | Regression |  Running |
| TC-NAV-005 | Sidebar Search No Results | Low | Regression |  Running |

**Total Test Functions:** 16  
**Total Test Scenarios:** 19 (with parametrization)  
**Automated & Running:** 15  
**Skipped:** 1 (due to demo environment limitations)

*TC-ADMIN-004 skipped because demo environment employee data changes unpredictably.


##  Test Reports

After running tests:
- **HTML Report:** `reports/report.html` - Open in browser for detailed results
- **Screenshots:** `screenshots/` - Automatic screenshots of failed tests with timestamps
- **Console Output:** Real-time test execution logs

##  Configuration

### Test Data
Located in `tests/test_admin.py`:

- URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
- USERNAME = 'Admin' 
- PASSWORD = 'admin123'


### Wait Times
Configured in `conftest.py`:
- IMPLICIT_WAIT = 5 # seconds 
- EXPLICIT_WAIT = 10 # seconds


### Pytest Markers
- `@pytest.mark.smoke` - Critical path tests
- `@pytest.mark.regression` - Full regression suite
- `@pytest.mark.admin` - Admin module tests
- `@pytest.mark.login` - Login tests
- `@pytest.mark.navigation` - Navigation tests



## Troubleshooting

### ChromeDriver Issues
The project uses webdriver-manager for automatic ChromeDriver download. If issues occur:
- pip install --upgrade webdriver-manager


### Element Not Found
- Ensure browser is maximized (handled automatically)
- Check if OrangeHRM demo site is accessible
- Review screenshots in `screenshots/` folder for visual debugging

### Tests Fail Randomly
- Check internet connection stability
- Increase wait times in `conftest.py` if needed
- Run individual tests to isolate issues

## Documentation

- **TEST_PLAN.md** - Comprehensive test planning documentation
- **PYTEST_FEATURES.md** - Pytest framework features and usage
- **Code Comments** - Inline documentation throughout test files

##  Dependencies
- selenium==4.15.2 
- pytest==7.4.3 
- pytest-html==4.1.1 
- webdriver-manager==4.0.1



## Contact

**Author:** MAKINANO, SIMONE DOMINIQUE
**Email:** itsimonemakinano@gmail.com  
**Project Date:** December 2025

## Project Purpose

This is an educational project demonstrating test automation best practices for:
- Selenium WebDriver usage
- Pytest framework implementation
- Test planning and documentation
- Professional code organization

---

**Made with ❤️ for Software Testing & Quality Assurance**






