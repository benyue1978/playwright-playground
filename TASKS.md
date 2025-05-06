# TASKS.md

## 0. Development Environment Initialization

- [x] Set up a Python virtual environment
- [x] Install dependencies using [uv](https://github.com/astral-sh/uv)
- [x] Install and configure Ruff for code style checking
- [x] Install Playwright and its required browsers
- [x] Ensure all dependencies are listed in requirements file or pyproject.toml
- [x] Run `ruff check .` to verify code style (all checks passed)
- [x] Run `pytest` to verify test discovery (no tests found, environment ready)

> Environment initialization completed successfully. All dependencies installed,
> Playwright browsers ready, code style check passed, and pytest runs without
> errors.

## Playwright UI Testing Task List for joinhorizons.com

### 1. Home Page

- [ ] Verify the home page loads successfully and the logo is visible
- [ ] Check that the main navigation bar (Platform, Pricing, Coverage,
      Partnership, About, Resources) is visible and clickable
- [ ] Test the "Book a demo" button navigates to the correct page
- [ ] Validate the display of key modules (Employer of Record, Contractor of
      Record, International Recruitment, Global Payroll, Add-ons, About company,
      Resources)

### 2. Authentication

- [ ] Verify the "Login" button navigates to the login page
- [ ] Check login form input validation (required fields, email format)
- [ ] Test login with valid and invalid credentials, and check for correct
      messages

### 3. Recruitment & Hiring Flow

- [ ] Check all items in the "Hire Globally" dropdown navigate correctly
- [ ] Verify "Onboard employees" and "Onboard contractors" entry points are
      accessible
- [ ] Test the "Recruit talent" entry point

### 4. Resources & Tools

- [ ] Verify the "Global Payroll Calculator" tool page is accessible
- [ ] Check navigation and content display for "Explore our hiring guides"

### 5. Responsiveness & Accessibility

- [ ] Test layout on major resolutions (desktop, mobile)
- [ ] Verify accessibility of main buttons and form elements (keyboard
      navigation, aria-labels)

### 6. Footer & Global Elements

- [ ] Check all footer links for correct navigation
- [ ] Verify the "Book a demo" button is available on all major pages

### 7. Error Handling

- [ ] Test 404 page navigation and messaging
- [ ] Check error messages for form submission failures

---

## Notes

- All tests should include typing annotations and English docstrings
- Place all test files in the `./tests` directory
- Follow Playwright and Python best practices for test independence and
  maintainability
- Prefer one test file per page/module for clarity and scalability
- Cover main flows, edge cases, and error scenarios

---

> This checklist is based on the current structure and content of <https://joinhorizons.com/>. Please adjust or extend according to actual UI and business requirements.
