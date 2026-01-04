from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddToCart(BasePage):
    USERNAME_INPUT = (By.XPATH, "//input[@id='user-name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    PRODUCT= (By.XPATH,"//img[@alt='Sauce Labs Backpack']")
    ADDCART_BUTTON=(By.XPATH,"//button[@id='add-to-cart']")
    CARTLINK=(By.XPATH,"//a[@class='shopping_cart_link']")
    CARTPRODUCT= (By.XPATH,"//div[@class='inventory_item_name']")

    # Constructor method to initialize the LoginPage with a webdriver instance
    def __init__(self, driver):
        # Call the parent class (BasePage) constructor to initialize driver and wait
        super().__init__(driver)

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

    #method to click the product
    def click_product(self):
        self.click_element(self.PRODUCT)

     #method to click the add to cart button
    def click_addtocart(self):
        self.click_element(self.ADDCART_BUTTON)

        #method to click cart logo
    def click_cartlink(self):
        self.click_element(self.CARTLINK)

        # Method to perform the complete login process with given credentials
    def addcart(self, username, password):

        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.click_product()
        self.click_addtocart()
        self.click_cartlink()





