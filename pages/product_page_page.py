from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from behave import given, when, then
from pages.base_page import Page


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    PRODUCT_NAME = (By.ID, 'productTitle')
    PRODUCT_PRICE = (By.ID, 'corePrice_feature_div')
    COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
    CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")
    THUMBNAIL_IMG = (By.CSS_SELECTOR, '#altImages input.a-button-input')

    def add_to_cart(self, *locator):
        self.driver.click(*self.ADD_TO_CART_BTN)
