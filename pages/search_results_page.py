from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from behave import given, when, then
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class SearchResults(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "span.a-price")
    BESTSELLER_LINKS = (By.CSS_SELECTOR, "#zg_header ul li")
    SUBNAV = (By.CSS_SELECTOR, "#nav-subnav[data-category={CATEGORY}]")

    def get_subnav_locator(self, category):
        return [self.SUBNAV[0], self.SUBNAV[1].replace('{CATEGORY}', category)]

    def verify_search_results(self, expected_text):
        actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
        assert expected_text == actual_result, f'Expected {expected_text}, but got {actual_result}'

    def click_on_first_product(self, *locator):
        self.find_element(*self.PRODUCT_PRICE).click()

    def banner_link_amount(self, expected_amount, *locator):
        expected_amount = int(expected_amount)
        bestseller_links = self.driver.find_element(*self.BESTSELLER_LINKS)
        assert len(bestseller_links) == expected_amount, \
            f'Expected {expected_amount} links but got {len(bestseller_links)}'

    def verify_product_dept_selected(self, category):
        locator = self.get_subnav_locator(category)
        print(locator)
        print(type(locator))
        self.wait_for_element_appear(*locator)
