from pages.base_page import Page
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(Page):
    CART_COUNT = (By.ID, 'nav-cart-count')
    PRODUCT_TEXT = (By.CSS_SELECTOR, 'span.a-color-state a-text-bold')
    CART_EMPTY_TEXT = (By.XPATH, "//h2")

    # def empty_cart(self, *locator):
    #     return self.find_element(*self.CART_EMPTY_TEXT).text

    def product_results_shown(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, \
            f'Checking by locator {locator}. Expected {expected_text}, but got {actual_text}'

    def open_the_cart_page(self):
        self.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
        self.wait.until(EC.element_to_be_clickable(*self.CART_COUNT))

    def verify_cart_count(self, expected_count):
        actual_count = self.find_element(*self.CART_COUNT).text
        assert expected_count == actual_count, \
            f'Expected {expected_count}, but got actual {actual_count}'

    def click_on_cart_count(self, *locator):
        self.click(*self.CART_COUNT)

    def verify_empty_cart(self, *locator):
        assert self.find_element(*self.CART_EMPTY_TEXT).text, "Empty Cart is not Verified"
