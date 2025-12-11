# Test Plan - OrangeHRM Admin Module Automation

## 1. Project Overview
**Project Name:** OrangeHRM Admin System Users Search Functionality Test Automation  
**Application Under Test:** OrangeHRM Demo (https://opensource-demo.orangehrmlive.com)  
**Module:** Admin - System Users  
**Created By:** MAKINANO, SIMONE DOMINIQUE 
**Date:** December 11, 2025

---

## 2. Scope

### In Scope
- Login functionality (positive and negative scenarios)
- **Admin > User Management > Users tab ONLY**
  - System Users search functionality
    - Search by Username
    - Search by User Role
    - Search by Employee Name
    - Search by Status
    - Combined filter search
    - Reset filters functionality
- Basic navigation verification (Admin menu, navbar, sidebar)

### Out of Scope - Admin Module (Future Testing)
- Job tab (Job Titles, Pay Grades, Employment Status, Job Categories, Work Shifts)
- Organization tab (General Information, Locations, Structure)
- Qualifications tab (Skills, Education, Licenses, Languages, Memberships)
- Nationalities configuration
- Corporate Branding
- Configuration settings
- **Rationale:** Focused testing approach - thoroughly testing User Management 
  demonstrates comprehensive automation skills better than shallow coverage 
  of all tabs

### Out of Scope - Other Modules
- PIM (Personal Information Management)
- Leave Management
- Time tracking
- Recruitment
- Performance management
- All other OrangeHRM modules

---

## 3. Test Objectives
1. Verify that login functionality works correctly for valid and invalid credentials
2. Validate Admin module System Users search operates correctly with individual filters
3. Confirm that combined filters produce accurate results
4. Ensure Reset functionality clears all filters and restores default table view
5. Verify navigation elements function as expected
6. Establish automated regression suite for Admin module search features

---

## 4. Test Environment

### Hardware
- OS: Windows 10/11
- RAM: Minimum 16GB
- Processor: R7 5700X or equivalent

### Software
- **Browser:** Google Chrome (v120+)
- **WebDriver:** ChromeDriver (winx64)
- **Python:** 3.8+
- **Framework:** Pytest 7.4+
- **Automation Tool:** Selenium WebDriver 4.x
- **IDE:** PyCharm

### Test Data
- **Valid Username:** Admin
- **Valid Password:** admin123
- **Test URL:** https://opensource-demo.orangehrmlive.com
- **Test Employee:** manda akhil user

---

## 5. Test Strategy

### Automation Approach
- **Framework:** Pytest with Selenium WebDriver
- **Design Pattern:** Page Object Model (POM)
- **Wait Strategy:** Explicit waits using WebDriverWait
- **Assertions:** Pytest assert statements
- **Reporting:** pytest-html for test reports

### Test Types
- **Smoke Tests:** Critical path tests (login, basic navigation)
- **Regression Tests:** Comprehensive search functionality tests
- **Negative Tests:** Invalid login, empty searches

### Execution Strategy
- Tests will run sequentially in a fresh browser session
- Each test is independent with its own setup/teardown
- Browser maximized to ensure element visibility

---

## 6. Test Cases

### TC-001: Positive Login
**Priority:** High (Smoke Test)  
**Test ID:** TC-LOGIN-001  
**Description:** Verify user can login with valid credentials  
**Preconditions:** Application is accessible  

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to login page | Login page displayed |
| 2 | Enter username "Admin" | Username entered |
| 3 | Enter password "admin123" | Password entered |
| 4 | Click Login button | Dashboard page displayed with "Dashboard" header |

**Test Data:** username=Admin, password=admin123  
**Expected Result:** User successfully logged in and redirected to Dashboard

---

### TC-002: Negative Login
**Priority:** High (Smoke Test)  
**Test ID:** TC-LOGIN-002  
**Description:** Verify appropriate error message for invalid credentials  
**Preconditions:** Application is accessible  

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to login page | Login page displayed |
| 2 | Enter username "wrongUsername" | Username entered |
| 3 | Enter password "admin123" | Password entered |
| 4 | Click Login button | Error message "Invalid credentials" displayed |

**Test Data:** username=wrongUsername, password=admin123  
**Expected Result:** Error message displayed, user remains on login page

---

### TC-003: Search by Username
**Priority:** High  
**Test ID:** TC-ADMIN-001  
**Description:** Verify System Users search by Username field  
**Preconditions:** User is logged in and on Admin page  

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Admin > System Users | System Users page displayed |
| 2 | Enter "Admin" in Username field | Username entered |
| 3 | Click Search button | Table filtered to show matching records |
| 4 | Verify first row username column | "Admin" appears in username column |

**Test Data:** username=Admin  
**Expected Result:** Table displays user(s) with username "Admin"

---

### TC-004: Search by User Role
**Priority:** High  
**Test ID:** TC-ADMIN-002  
**Description:** Verify System Users search by User Role dropdown  
**Preconditions:** User is logged in and on Admin page  

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Admin > System Users | System Users page displayed |
| 2 | Click User Role dropdown | Dropdown options displayed |
| 3 | Select "Admin" from dropdown | "Admin" selected |
| 4 | Click Search button | Table filtered to show Admin role users |
| 5 | Verify first row role column | "Admin" appears in User Role column |

**Test Data:** role=Admin  
**Expected Result:** Table displays only users with Admin role

---

### TC-005: Search by Status
**Priority:** Medium  
**Test ID:** TC-ADMIN-003  
**Description:** Verify System Users search by Status dropdown  
**Preconditions:** User is logged in and on Admin page  

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Admin > System Users | System Users page displayed |
| 2 | Click Status dropdown | Dropdown options displayed |
| 3 | Select "Enabled" from dropdown | "Enabled" selected |
| 4 | Click Search button | Table filtered to show enabled users |
| 5 | Verify first row status column | "Enabled" appears in Status column |

**Test Data:** status=Enabled  
**Expected Result:** Table displays only users with Enabled status

---

### TC-006: Search by Employee Name
**Priority:** Medium  
**Test ID:** TC-ADMIN-004  
**Description:** Verify System Users search by Employee Name autocomplete  
**Preconditions:** User is logged in and on Admin page  

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Admin > System Users | System Users page displayed |
| 2 | Type "manda user" in Employee Name field | Autocomplete suggestions appear |
| 3 | Click "manda akhil user" from suggestions | Employee selected |
| 4 | Click Search button | Table filtered to show matching employee |
| 5 | Verify first row employee column | "manda" appears in Employee Name column |

**Test Data:** employee_name=manda akhil user  
**Expected Result:** Table displays user associated with selected employee

---

### TC-007: Search with All Filters Combined
**Priority:** High (Regression)  
**Test ID:** TC-ADMIN-005  
**Description:** Verify System Users search with all filters applied together  
**Preconditions:** User is logged in and on Admin page  

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Admin > System Users | System Users page displayed |
| 2 | Enter "Admin" in Username field | Username entered |
| 3 | Select "Admin" from User Role dropdown | Role selected |
| 4 | Select "manda akhil user" from Employee Name | Employee selected |
| 5 | Select "Enabled" from Status dropdown | Status selected |
| 6 | Click Search button | Table filtered with all criteria |
| 7 | Verify result matches all filters | All column values match filter criteria |

**Test Data:** username=Admin, role=Admin, employee=manda akhil user, status=Enabled  
**Expected Result:** Table displays only records matching ALL filter criteria

---

### TC-008: Reset Search Filters
**Priority:** High (Regression)  
**Test ID:** TC-ADMIN-006  
**Description:** Verify Reset button clears all filters and restores default table  
**Preconditions:** User is logged in and on Admin page with filters applied  

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Navigate to Admin > System Users | System Users page displayed |
| 2 | Capture initial table row count | Count recorded |
| 3 | Apply all filters and search | Filtered results displayed (fewer rows) |
| 4 | Click Reset button | Filters cleared |
| 5 | Verify table row count restored | Row count equals initial count |
| 6 | Verify all input fields cleared | All fields are empty |

**Test Data:** All filters from TC-007  
**Expected Result:** All filters cleared, table shows all records, input fields empty
### Test Case Summary

| Test ID | Test Case Name | Priority | Type | Status |
|---------|---------------|----------|------|--------|
| TC-LOGIN-001 | Positive Login | High | Smoke |  Implemented |
| TC-LOGIN-002 | Negative Login | High | Smoke |  Implemented |
| TC-LOGIN-003 | Parametrized Login | High | Smoke |  Implemented (3 scenarios) |
| TC-ADMIN-001 | Search by Username | High | Functional |  Implemented |
| TC-ADMIN-002 | Search by User Role | High | Functional |  Implemented |
| TC-ADMIN-003 | Search by Status | Medium | Functional |  Implemented |
| TC-ADMIN-004 | Search by Employee Name | Medium | Functional | ⏭️ Skipped* |
| TC-ADMIN-005 | Combined Filter Search | High | Regression |  Implemented |
| TC-ADMIN-006 | Reset Filters | High | Regression |  Implemented |
| TC-ADMIN-007 | Search Different Roles | Medium | Regression |  Implemented (2 scenarios) |
| TC-ADMIN-008 | Search Different Statuses | Medium | Regression |  Implemented (2 scenarios) |
| TC-NAV-001 | Upgrade Button | Low | Functional |  Implemented |
| TC-NAV-002 | Profile About Dialog | Low | Functional |  Implemented |
| TC-NAV-003 | Profile Support Link | Low | Functional |  Implemented |
| TC-NAV-004 | Sidebar Search Valid | Low | Functional |  Implemented |
| TC-NAV-005 | Sidebar Search No Results | Low | Functional |  Implemented |

**Total Test Cases:** 16  
**Implemented & Running:** 15  
**Skipped:** 1*  
**Total Scenarios (with parametrization):** 19

*TC-ADMIN-004 skipped due to demo environment data inconsistency. Test is valid but requires stable test data.

---

## 7. Test Deliverables
- Test Plan document (this document)
- Automated test scripts (Python + Selenium + Pytest)
  - `test_admin.py` - 16 test functions
  - `helpers.py` - Reusable Selenium utilities
  - `conftest.py` - Pytest fixtures and configuration
- Test execution reports (HTML format via pytest-html)
- Screenshots of failures (automatically captured)
- README with setup and execution instructions
- PYTEST_FEATURES.md - Pytest implementation documentation


---

## 8. Entry and Exit Criteria

### Entry Criteria
- Test environment is set up and configured
- Python, Selenium, and Pytest installed
- ChromeDriver installed and configured
- OrangeHRM demo site is accessible
- Test data identified and available

### Exit Criteria
- All test cases executed
- 90%+ test pass rate
- All critical/high priority tests passing
- Test report generated
- Defects documented (if any)

---

## 9. Test Assumptions
- OrangeHRM demo site is stable and available 24/7
- Demo site data (users, employees) remains consistent
- Chrome browser is available on test machine
- Internet connection is stable
- Test user credentials (Admin/admin123) remain valid
- Browser must be maximized for proper element interaction

---

## 10. Constraints and Limitations
- Testing limited to Chrome browser only
- Demo site limitations (cannot add/delete users)
- Limited test data available on demo site
- Cannot test data persistence (demo site resets)
- Network speed may affect test execution time
- No access to backend/database for verification
- Some elements have dynamic attributes requiring flexible locators

---

## 11. Schedule
- **Test Plan Creation:** Day 1 12-11-25
- **Test Script Development:** Day 2-3 
- **Test Execution & Debugging:** Day 4
- **Reporting & Documentation:** Day 5

---

## 12. Approval
**Prepared By:** MAKINANO, SIMONE DOMINIQUE  
**Reviewed By:** [Instructor Name]  
**Approved By:** [Instructor Name]  
**Date:**



---

## 13. Test Execution Summary (Parametrization Details)

The following tests use pytest parametrization to execute multiple scenarios:

### TC-LOGIN-003: Parametrized Login Tests
**Scenarios executed:** 3
1. Valid credentials (Admin/admin123) - Should succeed
2. Invalid username (wronguser/admin123) - Should fail
3. Invalid password (Admin/wrongpass) - Should fail

### TC-ADMIN-007: Parametrized Role Search
**Scenarios executed:** 2
1. Admin role search
2. ESS role search

### TC-ADMIN-008: Parametrized Status Search
**Scenarios executed:** 2
1. Enabled status search
2. Disabled status search

**Total Test Functions:** 16  
**Total Test Scenarios Executed:** 19 (due to parametrization)

This demonstrates efficient test design using pytest's parametrize feature, allowing multiple test scenarios to be executed from a single test function definition.

---
