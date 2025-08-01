# Pango Pay & Go — UI Automation Testing Project

## Overview

This project implements a UI automation framework using **Python**, **PyTest**, and **Selenium WebDriver**  
to validate the core functionalities of a **Parking Management Web App**.

The project covers:
- Authentication
- Vehicle parking operations
- Field validations (including HTML5 native browser validation)
- Duplicate vehicle handling between users
- History log verification

---

## Test Scenarios

### `test_duplicate_vehicle.py`
- **Verify one vehicle can’t be parked by two users simultaneously**
  - Login as user A → Start parking → Logout  
  - Login as user B → Attempt same plate → Validate error message

### `test_fields_validation.py`
- Covers edge cases for license plate input:
  - Empty input
  - Less/More than 8 digits
  - All identical digits
  - Sequential digits
  - Letters (non-numeric)

### `test_parking_appears_in_history.py`
- Start + Stop parking
- Validate that entry appears in the **History table**

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run all tests

```bash
pytest tests/
```

---

## Technologies

- Python 3.11+
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- Logging with Timestamps
- Browser: Chrome (incognito, headless optional)

---

## Documentation

- [STP - Pay&Go Parking Lot Manager](docs/STP-%20Pay&Go%20Parking%20Lot%20Manager.pdf)
- [Bug Reports](docs/bug_reports.md)

## Project Structure

```
PangoPayGo/
├── base/
│ └── base_page.py
│
├── docs/
│ ├── bug1_screenvideo.gif
│ ├── bug2_screenshot.png
│ ├── bug3_screenshot.png
│ ├── bug_reports.md
│ └── STP- Pay&Go Parking Lot Manager.pdf
│
├── pages/
│ ├── history_page.py
│ ├── login_page.py
│ └── parking_page.py
│
├── tests/
│ ├── test_duplicate_vehicle.py
│ ├── test_fields_validation.py
│ └── test_parking_appears_in_history.py
│
├── utils/
│ ├── logger_config.py
│ └── utils.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---
