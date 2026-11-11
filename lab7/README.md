# Lab 7: Fuzzing for Input Validation Bugs

## Student Details
* **Name:** Ajay T Naik[cite: 26]
* **SRN:** PES1UG24CS552[cite: 26]
* **Section:** 5J[cite: 26]
* **Repository Link:** [https://github.com/AjayTNaik/L6_L7_03_coffee_shop_order](https://github.com/AjayTNaik/L6_L7_03_coffee_shop_order)

---

## Overview
This laboratory assignment explores dynamic **fuzz testing** using the **Hypothesis** library in Python to uncover edge-case bugs, unhandled exceptions, and input validation vulnerabilities in a coffee shop ordering application[cite: 1]. 

## Files Included
1. **`processor.py`**: The hardened and defended application script containing robust type checks and input sanitization.
2. **`test_processor.py`**: The property-based fuzz testing suite built using Hypothesis and executed via Pytest.
3. **`Screenshot.pdf`**: Comprehensive visual documentation of step-by-step terminal outputs, test failures, and final passing test results.

---

## Instructions to Run

### 1. Install Dependencies
Make sure you have `pytest` and `hypothesis` installed[cite: 3]:
```bash
pip install hypothesis pytest
