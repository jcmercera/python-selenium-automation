from amazon_search_script import driver
from pages.base_page import Page
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(Page):
    CART_COUNT = (By.ID, 'nav-cart-count')
    PRODUCT_TEXT = (By.CSS_SELECTOR, 'span.a-color-state a-text-bold')
    CART_EMPTY_TEXT = (By.XPATH, "//h2[text()='Your Amazon Cart is empty']")

    def empty_cart(self, *locator):
        return self.find_element(*self.CART_EMPTY_TEXT).text

    def product_results_shown(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, \
            f'Checking by locator {locator}. Expected {expected_text}, but got {actual_text}'

