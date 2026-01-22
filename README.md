# Python Playwright Automation Framework 🎭

[![Playwright Tests 🎭](https://github.com/diegoechauri/playwright-automation-framework/actions/workflows/playwright.yml/badge.svg)](https://github.com/diegoechauri/playwright-automation-framework/actions/workflows/playwright.yml)

## Overview
This repository contains a scalable test automation framework built with **Python** and **Playwright**.
It is designed to demonstrate modern QA practices applied to end-to-end testing.

## Tech Stack 🛠️
* **Language:** Python 3.10+
* **Core Library:** Playwright
* **Test Runner:** Pytest
* **Design Pattern:** Page Object Model (POM)
* **Reporting:** Pytest-HTML / Allure
* **CI/CD:** GitHub Actions (In Progress)

## Project Roadmap 🗺️
- [x] Environment Setup & Dependency Management
- [x] Base Page & Page Object Implementation
- [x] End-to-End Test Scenarios (Login, Search, Cart)
- [x] CI/CD Pipeline Configuration

## How to Run
### 1. Clone the repository
```bash
git clone git@github.com:diegoechauri/playwright-automation-framework.git
cd playwright-automation-framework
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers
```bash
playwright install
playwright install-deps
```

### 5. Run tests
```bash
pytest
```
