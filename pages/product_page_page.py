from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from behave import given, when, then
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    PRODUCT_NAME = (By.ID, 'productTitle')
    PRODUCT_PRICE = (By.ID, 'corePrice_feature_div')
    COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
    CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")
    THUMBNAIL_IMG = (By.CSS_SELECTOR, '#altImages input.a-button-input')
    NEW_ARRIVALS = (By.XPATH, "//*[contains(@href, 'New-Arrivals') and @class='nav-a nav-hasArrow']")
    NEW_ARRIVALS_DEALS = (By.ID, 'nav-flyout-aj:https://m.media-amazon.com/images/G/01/Softlines/Store/MegaMenu/megamenucreator_removeps_en_US.json:subnav-sl-megamenu-8:0')

    def add_to_cart(self, *locator):
        self.click(*self.ADD_TO_CART_BTN)

    def open_product_page(self, product_id):
        self.driver.get(f'https://www.amazon.com/dp/{product_id}')

    def verify_user_can_select_product_colors(self, *locator):
        self.find_element(*self.COLOR_OPTIONS).click()
        all_color_options = self.driver.find_elements(*self.COLOR_OPTIONS)
        print('All colors:', all_color_options)
        expected_colors = (
            'Black', 'Bluestone', 'Brite Lime', 'Brite Orange', 'Carbon Heather', 'Carhartt Brown', 'Desert',
            'Fire Red Heather', 'Heather Gray', 'Jade Heather', 'Lakeshore', 'Malachite', 'Marine Blue Heather',
            'Moonstone Nep', 'Navy', 'North Woods Heather', 'Oiled Walnut Heather', 'Pale Apricot Nep', 'Port',
            'Sundance Heather', 'Terracotta', 'White')

        actual_colors = []
        for color in all_color_options:
            color.click()
            current_color = self.driver.find_element(*self.CURRENT_COLOR).text
            print('Current color:', current_color)
            actual_colors += [current_color]
            assert expected_colors == actual_colors, f'Expected {expected_colors}, but got {actual_colors}'

    def hover_over_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_new_arrivals_deals_shown(self):
        self.wait_for_element_appear(*self.NEW_ARRIVALS_DEALS)