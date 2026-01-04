# Import By class to locate elements using different strategies (ID, XPATH, etc.)
from selenium.webdriver.common.by import By
# Import BasePage class to inherit common methods for element interaction
from pages.base_page import BasePage

# Page Object Model (POM) - LoginPage class
# POM is a design pattern that creates an object repository for web UI elements
# Benefits: Code reusability, maintainability, and readability
class LoginPage(BasePage):
    # Define locators as class attributes using XPATH strategy
    # These are the web elements we will interact with on the login page
    USERNAME_INPUT = (By.XPATH, "//input[@id='user-name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")


    # Constructor method to initialize the LoginPage with a webdriver instance
    def __init__(self, driver):
        # Call the parent class (BasePage) constructor to initialize driver and wait
        super().__init__(driver)

    # Method to click on the login link


    # Method to enter username in the username input field
    def enter_username(self, username):
        """Enter username/email"""
        # Use the enter_text method from BasePage to input the username
        self.enter_text(self.USERNAME_INPUT, username)

    # Method to enter password in the password input field
    def enter_password(self, password):
        """Enter password"""
        # Use the enter_text method from BasePage to input the password
        self.enter_text(self.PASSWORD_INPUT, password)

    # Method to click on the login button
    def click_login_button(self):
        """Click on the login button"""
        # Use the click_element method from BasePage to click the login button
        self.click_element(self.LOGIN_BUTTON)



    # Method to perform the complete login process with given credentials
    def login(self, username, password):
        """Perform login with given credentials"""

        self.enter_username(username)
        # Enter the password in the input field
        self.enter_password(password)
        # Click the login button to submit the credentials
        self.click_login_button()
