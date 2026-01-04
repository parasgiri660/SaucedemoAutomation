import pytest
import time

from pages.login_page import LoginPage
from data.cart_data import TEST_USERS
from utils.test_runner import create_driver
from utils.assertions import assert_true, assert_false
from pages.addtocart_page import AddToCart

class TestAddtoCart():
    def setup_method(self):
        self.driver = create_driver()
        self.login_page = LoginPage(self.driver)
        self.add_to_cart = AddToCart(self.driver)
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        """Teardown method to quit driver"""
        self.driver.quit()

    @pytest.mark.parametrize("user_data", TEST_USERS)
    def test_valid_addtocart(self, user_data):
        #perform add to cart steps
        self.login_page.enter_username(user_data["username"])

        self.login_page.enter_password(user_data["password"])

        self.login_page.click_login_button()

        self.add_to_cart.click_product()
        self.add_to_cart.click_addtocart()
        self.add_to_cart.click_cartlink()
        time.sleep(3)
        product_present = self.add_to_cart.is_element_present(self.add_to_cart.CARTPRODUCT)
        assert_true(product_present, "add to cart failed")



