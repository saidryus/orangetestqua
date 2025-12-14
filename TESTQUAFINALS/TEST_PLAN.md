# Test Plan - OrangeHRM Admin Module Automation

## 1. Project Overview
**Project Name:** OrangeHRM Admin System Users Search Functionality Test Automation  
**Application Under Test:** OrangeHRM Demo (https://opensource-demo.orangehrmlive.com)  
**Module:** Admin - System Users  
**Created By:** MAKINANO, SIMONE DOMINIQUE  
**Date:** December 11, 2025  
**Last Updated:** December 14, 2025

---

## 2. Scope

### In Scope
- Login functionality (positive, negative, and edge case scenarios)
- **Admin > User Management > Users tab**
  - System Users search functionality
    - Search by Username
    - Search by User Role
    - Search by Employee Name
    - Search by Status
    - Combined filter search
    - Reset filters functionality
  - User management operations
    - Delete User (error verification)
- Admin module navigation
  - Top-level tabs (Nationalities, Corporate Branding)
  - Dropdown menu navigation (Job, Organization, Qualifications, Configuration)
- General navigation verification
  - Admin menu access
  - Navbar interactions (Upgrade button, Profile dropdown)
  - Sidebar search functionality
  - Dashboard navigation

### Out of Scope - Admin Module (Future Testing)
- Detailed functionality within:
  - Job tab (Job Titles, Pay Grades, Employment Status, Job Categories, Work Shifts)
  - Organization tab (General Information, Locations, Structure)
  - Qualifications tab (Skills, Education, Licenses, Languages, Memberships)
  - Nationalities configuration (detailed management)
  - Corporate Branding (detailed customization)
  - Configuration settings (detailed setup)
- Add User functionality (demo environment limitation)
- Edit User functionality (demo environment limitation)
- **Rationale:** Focused testing approach - thoroughly testing User Management 
  and navigation demonstrates comprehensive automation skills better than shallow 
  coverage of all functionality

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
5. Verify delete operations show appropriate error messages for protected users
6. Validate navigation between Admin module tabs and submenus
7. Ensure sidebar and profile navigation functions correctly
8. Establish automated regression suite for Admin module features

---

## 4. Test Environment

### Hardware
- OS: Windows 11
- RAM: Minimum 16GB
- Processor: R7 5700X or equivalent

### Software
- **Browser:** Google Chrome (v143+)
- **WebDriver:** ChromeDriver (winx64 v143+)
- **Python:** 3.13.9
- **Framework:** Pytest 9.0.2
- **Automation Tool:** Selenium WebDriver 4.x
- **IDE:** PyCharm
- **Plugins:** pytest-html 4.1.1, pytest-metadata 3.1.1

### Test Data
- **Valid Username:** Admin
- **Valid Password:** admin123
- **Test URL:** https://opensource-demo.orangehrmlive.com
- **Test Employee:** manda user (autocomplete test - skipped due to data instability)

---

## 5. Test Strategy

### Automation Approach
- **Framework:** Pytest with Selenium WebDriver
- **Design Pattern:** Centralized locators with reusable helper utilities
- **Wait Strategy:** Explicit waits using WebDriverWait with fallback mechanisms
- **Assertions:** Pytest assert statements with descriptive error messages
- **Reporting:** pytest-html for detailed test reports
- **Screenshot Capture:** Automatic screenshot on test failure

### Test Types
- **Smoke Tests:** Critical path tests (login variations)
- **Regression Tests:** Comprehensive search functionality and navigation tests
- **Negative Tests:** Invalid login, empty searches, protected user deletion
- **Edge Cases:** Long usernames, special characters, empty filters

### Execution Strategy
- Tests run sequentially in fresh browser sessions per test
- Each test is independent with setup/teardown via pytest fixtures
- Browser maximized to ensure element visibility
- Markers used for selective test execution (smoke, admin, navigation, regression, login)

---

## 6. Test Cases

### Login Test Cases

#### TC-LOGIN-001: Positive Login
**Priority:** High (Smoke Test)  
**Description:** Verify user can login with valid credentials  
**Preconditions:** Application is accessible  
**Test Data:** username=Admin, password=admin123  
**Expected Result:** User successfully logged in and redirected to Dashboard

---

#### TC-LOGIN-002: Negative Login
**Priority:** High (Smoke Test)  
**Description:** Verify appropriate error message for invalid credentials  
**Preconditions:** Application is accessible  
**Test Data:** username=wrongUsername, password=admin123  
**Expected Result:** Error message "Invalid credentials" displayed

---

#### TC-LOGIN-003: Parametrized Login Tests
**Priority:** High (Smoke Test)  
**Description:** Test multiple login credential combinations  
**Scenarios:**
1. Valid credentials (Admin/admin123) - Should succeed
2. Invalid username (wronguser/admin123) - Should fail
3. Invalid password (Admin/wrongpass) - Should fail

---

#### TC-LOGIN-004: Empty Username Login
**Priority:** High (Smoke Test)  
**Description:** Verify error when username field is empty  
**Test Data:** username="", password=admin123  
**Expected Result:** "Required" error message displayed

---

#### TC-LOGIN-005: Empty Password Login
**Priority:** High (Smoke Test)  
**Description:** Verify error when password field is empty  
**Test Data:** username=Admin, password=""  
**Expected Result:** "Required" error message displayed

---

### Admin Search Test Cases

#### TC-ADMIN-001: Search by Username
**Priority:** High  
**Description:** Verify System Users search by Username field  
**Test Data:** username=Admin  
**Expected Result:** Table displays user(s) with username "Admin"

---

#### TC-ADMIN-002: Search by User Role
**Priority:** High  
**Description:** Verify System Users search by User Role dropdown  
**Test Data:** role=Admin  
**Expected Result:** Table displays only users with Admin role

---

#### TC-ADMIN-003: Search by Status
**Priority:** Medium  
**Description:** Verify System Users search by Status dropdown  
**Test Data:** status=Enabled  
**Expected Result:** Table displays only users with Enabled status

---

#### TC-ADMIN-004: Search by Employee Name
**Priority:** Medium  
**Status:** SKIPPED  
**Description:** Verify System Users search by Employee Name autocomplete  
**Reason:** Demo environment employee data is inconsistent and unpredictable

---

#### TC-ADMIN-005: Search with All Filters Combined
**Priority:** High (Regression)  
**Description:** Verify System Users search with all filters applied together  
**Test Data:** username=Admin, role=Admin, status=Enabled  
**Expected Result:** Table displays only records matching ALL filter criteria

---

#### TC-ADMIN-006: Reset Search Filters
**Priority:** High (Regression)  
**Description:** Verify Reset button clears all filters and restores default table  
**Expected Result:** All filters cleared, table shows all records, input fields empty

---

#### TC-ADMIN-007: Parametrized Role Search
**Priority:** Medium (Regression)  
**Description:** Search by different user roles  
**Scenarios:**
1. Admin role search
2. ESS role search

---

#### TC-ADMIN-008: Parametrized Status Search
**Priority:** Medium (Regression)  
**Description:** Search by different status values  
**Scenarios:**
1. Enabled status search
2. Disabled status search

---

#### TC-ADMIN-011: Search with Empty Filters
**Priority:** Medium  
**Description:** Verify search with no filters returns all users  
**Expected Result:** All users displayed in table

---

#### TC-ADMIN-012: Search with Mixed Filters
**Priority:** Medium  
**Description:** Search with valid username but contradicting role/status  
**Test Data:** username=Admin, role=ESS, status=Disabled  
**Expected Result:** Search executes, results match filter logic

---

#### TC-ADMIN-013: Reset with No Filters
**Priority:** Medium  
**Description:** Verify reset button works when no filters are applied  
**Expected Result:** Table remains unchanged, no errors

---

#### TC-ADMIN-014: Search with Long Username
**Priority:** Medium (Edge Case)  
**Description:** Test search with very long username input  
**Test Data:** username="A" * 50  
**Expected Result:** Search executes without errors

---

#### TC-ADMIN-015: Search with Special Characters
**Priority:** Medium (Edge Case)  
**Description:** Test search with special characters in username  
**Test Data:** username="admin@test.com"  
**Expected Result:** Search executes without errors

---

#### TC-ADMIN-016: Add User with Valid Data
**Priority:** Medium  
**Status:** SKIPPED  
**Description:** Verify adding a new system user  
**Reason:** Demo environment employee autocomplete unreliable

---

#### TC-ADMIN-017: Edit Existing User
**Priority:** Medium  
**Status:** SKIPPED  
**Description:** Verify editing an existing system user  
**Reason:** Demo environment users reset between sessions

---

#### TC-ADMIN-018: Delete Admin User Shows Error
**Priority:** High  
**Description:** Verify deleting Admin user shows "Cannot be deleted" error  
**Expected Result:** Error toast message "Cannot be deleted" appears

---

### Navigation Test Cases

#### TC-NAV-001: Upgrade Button Opens New Tab
**Priority:** Low  
**Description:** Verify Upgrade button opens upgrade page in new tab  
**Expected Result:** New tab opens with upgrade page URL

---

#### TC-NAV-002: Profile About Dialog
**Priority:** Low  
**Description:** Verify About dialog displays company information  
**Expected Result:** About dialog appears with company name label

---

#### TC-NAV-003: Profile Support Link
**Priority:** Low  
**Description:** Verify Support link navigates correctly  
**Expected Result:** URL changes to /help/support

---

#### TC-NAV-004: Sidebar Search Valid Term
**Priority:** Low  
**Description:** Verify sidebar search filters menu with valid term  
**Test Data:** search_term="claim"  
**Expected Result:** Only "Claim" menu item visible

---

#### TC-NAV-005: Sidebar Search No Results
**Priority:** Low  
**Description:** Verify sidebar search shows no results for invalid term  
**Test Data:** search_term="negative item search"  
**Expected Result:** No menu items displayed

---

#### TC-NAV-006: Sidebar Search Invalid Term
**Priority:** Low  
**Description:** Verify sidebar search with nonsense input  
**Test Data:** search_term="xyz999"  
**Expected Result:** No menu items displayed

---

#### TC-NAV-007: Navigate to Dashboard
**Priority:** Low  
**Description:** Verify dashboard link navigation  
**Expected Result:** Dashboard page loads with "Dashboard" header

---

#### TC-NAV-008: Admin Top Tabs Navigation (Parametrized)
**Priority:** Medium  
**Description:** Verify top-level Admin tabs navigate correctly  
**Scenarios:**
1. Nationalities tab - navigates to /admin/nationality
2. Corporate Branding tab - navigates to /admin/addTheme

---

#### TC-NAV-009: Job Dropdown Navigation
**Priority:** Medium  
**Description:** Verify Job dropdown menu navigation  
**Expected Result:** Job Titles page loads (/admin/viewJobTitleList)

---

#### TC-NAV-010: Organization Dropdown Navigation
**Priority:** Medium  
**Description:** Verify Organization dropdown menu navigation  
**Expected Result:** General Information page loads (/admin/viewOrganizationGeneralInformation)

---

#### TC-NAV-011: Qualifications Dropdown Navigation
**Priority:** Medium  
**Description:** Verify Qualifications dropdown menu navigation  
**Expected Result:** Skills page loads (/admin/viewSkills)

---

#### TC-NAV-012: Configuration Dropdown Navigation
**Priority:** Medium  
**Description:** Verify Configuration dropdown menu navigation  
**Expected Result:** Email Configuration page loads (/admin/listMailConfiguration)

---

## 7. Test Case Summary

| Test ID | Test Case Name | Priority | Type | Status |
|---------|---------------|----------|------|--------|
| **LOGIN TESTS** |
| TC-LOGIN-001 | Positive Login | High | Smoke | Implemented |
| TC-LOGIN-002 | Negative Login | High | Smoke | Implemented |
| TC-LOGIN-003 | Parametrized Login | High | Smoke | Implemented (3 scenarios) |
| TC-LOGIN-004 | Empty Username Login | High | Smoke | Implemented |
| TC-LOGIN-005 | Empty Password Login | High | Smoke | Implemented |
| **ADMIN SEARCH TESTS** |
| TC-ADMIN-001 | Search by Username | High | Functional | Implemented |
| TC-ADMIN-002 | Search by User Role | High | Functional | Implemented |
| TC-ADMIN-003 | Search by Status | Medium | Functional | Implemented |
| TC-ADMIN-004 | Search by Employee Name | Medium | Functional | Skipped* |
| TC-ADMIN-005 | Combined Filter Search | High | Regression | Implemented |
| TC-ADMIN-006 | Reset Filters | High | Regression | Implemented |
| TC-ADMIN-007 | Search Different Roles | Medium | Regression | Implemented (2 scenarios) |
| TC-ADMIN-008 | Search Different Statuses | Medium | Regression | Implemented (2 scenarios) |
| TC-ADMIN-011 | Search with Empty Filters | Medium | Functional | Implemented |
| TC-ADMIN-012 | Search with Mixed Filters | Medium | Functional | Implemented |
| TC-ADMIN-013 | Reset with No Filters | Medium | Functional | Implemented |
| TC-ADMIN-014 | Search with Long Username | Medium | Edge Case | Implemented |
| TC-ADMIN-015 | Search with Special Characters | Medium | Edge Case | Implemented |
| TC-ADMIN-016 | Add User | Medium | Functional | Skipped* |
| TC-ADMIN-017 | Edit User | Medium | Functional | Skipped* |
| TC-ADMIN-018 | Delete Admin User Error | High | Functional | Implemented |
| **NAVIGATION TESTS** |
| TC-NAV-001 | Upgrade Button | Low | Functional | Implemented |
| TC-NAV-002 | Profile About Dialog | Low | Functional | Implemented |
| TC-NAV-003 | Profile Support Link | Low | Functional | Implemented |
| TC-NAV-004 | Sidebar Search Valid | Low | Functional | Implemented |
| TC-NAV-005 | Sidebar Search No Results | Low | Functional | Implemented |
| TC-NAV-006 | Sidebar Search Invalid | Low | Functional | Implemented |
| TC-NAV-007 | Navigate to Dashboard | Low | Functional | Implemented |
| TC-NAV-008 | Admin Top Tabs | Medium | Functional | Implemented (2 scenarios) |
| TC-NAV-009 | Job Dropdown Navigation | Medium | Functional | Implemented |
| TC-NAV-010 | Organization Dropdown | Medium | Functional | Implemented |
| TC-NAV-011 | Qualifications Dropdown | Medium | Functional | Implemented |
| TC-NAV-012 | Configuration Dropdown | Medium | Functional | Implemented |

**Total Test Functions:** 39  
**Implemented & Running:** 36  
**Skipped:** 3*  
**Total Scenarios (with parametrization):** 45

*Skipped tests due to demo environment data inconsistency. Tests are valid but require stable test data.

---

## 8. Test Deliverables
- Test Plan document (this document)
- Automated test scripts (Python + Selenium + Pytest)
  - `test_admin.py` - 39 test functions covering 45 scenarios
  - `helpers.py` - Reusable Selenium utilities (SeleniumHelpers class)
  - `conftest.py` - Pytest fixtures and configuration
- Test execution reports (HTML format via pytest-html)
- Screenshots of failures (automatically captured in screenshots/)
- README with setup and execution instructions
- PYTEST_FEATURES.md - Pytest implementation documentation
- Centralized locator classes for maintainability

---

## 9. Entry and Exit Criteria

### Entry Criteria
- Test environment is set up and configured
- Python 3.13.9, Selenium, and Pytest installed
- ChromeDriver v143 installed and configured
- OrangeHRM demo site is accessible
- Test data identified and available
- Helper utilities implemented

### Exit Criteria
- All test cases executed
- 90%+ test pass rate (36/39 = 92% pass rate, 3 intentionally skipped)
- All critical/high priority tests passing
- Test report generated with pytest-html
- Defects documented in test plan

---

## 10. Test Assumptions
- OrangeHRM demo site is stable and available 24/7
- Demo site data (users, employees) may be inconsistent (mitigation: skip unstable tests)
- Chrome browser v143+ is available on test machine
- Internet connection is stable
- Test user credentials (Admin/admin123) remain valid
- Browser must be maximized for proper element interaction
- Some elements have dynamic attributes requiring flexible XPath locators

---

## 11. Constraints and Limitations
- Testing limited to Chrome browser only
- Demo site limitations:
  - Cannot reliably add/delete users (protected users, unstable employee data)
  - Employee autocomplete data changes unpredictably
  - Some users cannot be deleted (protected accounts)
- Limited test data available on demo site
- Cannot test data persistence (demo site resets)
- Network speed may affect test execution time
- No access to backend/database for verification
- Some elements have dynamic attributes requiring flexible locators
- Dropdown menus require explicit wait and interaction patterns

---

## 12. Known Issues & Mitigations

### Demo Environment Limitations
1. **Employee Autocomplete Instability**
   - Issue: Employee names change between sessions
   - Mitigation: TC-ADMIN-004 skipped with documentation
   
2. **Protected User Deletion**
   - Issue: Admin user cannot be deleted
   - Mitigation: Test verifies error message instead (TC-ADMIN-018)
   
3. **Add/Edit User Unreliability**
   - Issue: Employee autocomplete fails during user creation
   - Mitigation: TC-ADMIN-016 and TC-ADMIN-017 skipped

---

## 13. Schedule
- **Test Plan Creation:** Day 1 (12-11-25)
- **Initial Test Script Development:** Day 2-3 (12-12-25 to 12-13-25)
- **Test Expansion & Refinement:** Day 4 (12-14-25)
  - Added delete user test
  - Added navigation tests (6 new tests)
  - Added edge case tests (5 new tests)
  - Added empty field login tests (2 new tests)
- **Test Execution & Debugging:** Day 4-5
- **Reporting & Documentation:** Day 5

---

## 14. Approval
**Prepared By:** MAKINANO, SIMONE DOMINIQUE  
**Reviewed By:** [Instructor Name]  
**Approved By:** [Instructor Name]  
**Date:** December 14, 2025

---

## 15. Test Execution Summary (Parametrization Details)

The following tests use pytest parametrization to execute multiple scenarios efficiently:

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

### TC-NAV-008: Parametrized Admin Tab Navigation
**Scenarios executed:** 2
1. Nationalities tab
2. Corporate Branding tab

**Total Test Functions:** 39  
**Total Test Scenarios Executed:** 45 (due to parametrization)

This demonstrates efficient test design using pytest's parametrize feature, allowing multiple test scenarios to be executed from a single test function definition while maintaining code quality and readability.

---

## 16. Test Coverage Metrics

### By Priority
- **High Priority:** 13 tests (33%)
- **Medium Priority:** 19 tests (49%)
- **Low Priority:** 7 tests (18%)

### By Type
- **Smoke Tests:** 5 tests (13%)
- **Functional Tests:** 24 tests (62%)
- **Regression Tests:** 8 tests (21%)
- **Edge Cases:** 2 tests (5%)

### By Module
- **Login:** 5 tests
- **Admin Search:** 13 tests
- **Navigation:** 12 tests
- **User Management:** 9 tests

**Overall Pass Rate:** 92% (36/39 passing, 3 intentionally skipped)

---

## 17. Pytest Markers Used

Tests are organized using pytest markers for selective execution:

- @pytest.mark.smoke # Critical path tests (5 tests)
- @pytest.mark.login # Login-related tests (5 tests)
- @pytest.mark.admin # Admin module tests (13 tests)
- @pytest.mark.navigation # Navigation tests (12 tests)
- @pytest.mark.regression # Regression suite tests (8 tests)


**Example Execution:**
- **Run only smoke tests**
  - pytest -m smoke

- **Run all admin tests**
  - pytest -m admin

- **Run navigation tests only**
  - pytest -m navigation


This demonstrates efficient test design using pytest's parametrize feature and markers, allowing for flexible test execution and comprehensive coverage.
