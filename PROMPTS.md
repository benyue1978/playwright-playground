# PROMPTS.md

## Summary of Key Steps and Prompts

This document summarizes the main steps and user/AI prompts used so far in the Playwright UI testing project for <https://joinhorizons.com/>.

---

### 1. Generate UI Testing Task List

**Prompt:**

```text
I want to write some Playwright UI tests for the site @https://joinhorizons.com/. Please generate TASKS.md for me.
```

**Action:**

- The AI generated a detailed UI testing task list, grouped by homepage,
  authentication, recruitment flow, resources/tools, responsiveness,
  accessibility, footer, and error handling.

---

### 2. Add Development Environment Initialization Task

**Prompt:**

```text
add task 0, init the dev environment
```

**Action:**

- Added Task 0 at the top of TASKS.md, including steps for virtual environment,
  uv, Ruff, Playwright, and dependency installation.

---

### 3. Environment Setup and Dependency Management

**Prompt:**

```text
setup environment and update readme.md, manage dependency using pyproject.toml
```

**Action:**

- Created pyproject.toml for unified dependency management.
- Updated README.md with detailed instructions for environment setup,
  dependency installation, Playwright browser installation, Ruff checks,
  and running pytest.

---

### 4. Execute and Verify Environment Initialization

**Prompt:**

```text
Initialize the environment, verify it is ready, and update TASKS.md
```

**Action:**

- Automated creation of virtual environment, dependency installation,
  Playwright browser installation, Ruff check, and pytest run.
- Updated TASKS.md, marking Task 0 as complete and adding verification notes.

---

## Notes

- All steps follow Python project best practices: dependency management with
  pyproject.toml + uv, code style with Ruff, and testing with pytest.
- Prompts are provided in English for future reuse and team collaboration.

---

> This document serves as a reference for future project members to quickly understand and reuse the main prompts and workflow.
