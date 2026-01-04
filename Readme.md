#  SauceDemo Test Automation Framework

##  Project Overview
This project is a **robust Selenium 4 automation framework** developed to validate critical user workflows of the **SauceDemo** e-commerce application.

The framework is implemented using **Python with PyTest**, follows the **Page Object Model (POM)** design pattern, and is developed in **IntelliJ IDEA**.

The automation focuses on **Login** and **Add to Cart** functionalities, covering both **positive and negative test scenarios** to ensure application reliability and correctness.

---

##  Objectives
- Automate core functional flows of the SauceDemo application
- Ensure reliable validation using assertions and explicit waits
- Build a scalable, maintainable, and reusable automation framework
- Follow industry-standard test automation best practices

---

##  Test Scenarios Covered

###  Login Module
- Login with **4 valid user credentials**
- Login with **4 invalid user credentials**
- Verify successful login redirection
- Verify appropriate error messages for invalid login attempts

###  Add to Cart Module
- Add a single product to the cart
- Add multiple products to the cart

- Verify selected products appear on the cart page

---

##  Test Case Summary

| Module    | Test Coverage                              |
|----------|--------------------------------------------|
| Login     | Valid login, Invalid login, Error handling |
| Inventory | Product selection                          |
| Cart      | Add items g                                |

---

##  Automation Approach
- **Page Object Model (POM)** used to separate locators and test logic
- **Explicit waits** used for better synchronization
- **Assertions** implemented to validate expected results
- **PyTest** used for test execution and reporting
- Modular and reusable test structure for easy maintenance

---

##  Framework & Tools Used

| Category          | Technology            |
|------------------|----------------------|
| Programming Language | Python               |
| Automation Tool   | Selenium 4           |
| Test Framework    | PyTest               |
| Design Pattern    | Page Object Model    |
| IDE               | IntelliJ IDEA        |
| Browser           | Google Chrome        |
| Driver            | ChromeDriver         |
| Version Control   | Git & GitHub         |
| OS Support        | Windows / macOS     |

---

##  Setup Instructions

###  Prerequisites
- Python **3.10 or above**
- IntelliJ IDEA
- Google Chrome Browser
- ChromeDriver (compatible with installed Chrome version)
- Git installed on the system

---

###  Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/parasgiri660/SaucedemoAutomation.git

```
---

###  Run the command to start specific test 
```bash
cd SaucedemoAutomation/tests
pytest <test_file_name>
```
