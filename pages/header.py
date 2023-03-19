import self
from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from setuptools.command.alias import alias
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SELECT_DEPT = (By.ID, 'searchDropdownBox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    ORDERS_LINK = (By.CSS_SELECTOR, "a[href='/gp/css/order-history?ref_=nav_orders_first']")
    HEADER_LINKS = (By.CSS_SELECTOR, "#nav-xshop a.nav-a[data-csa-c-type='link']")
    LANG_OPTIONS = (By.ID, 'icp-nav-flyout')
    # SPANISH_LANG = (By.CSS_SELECTOR, "a.[href='#switch-lang=es_US']")
    SPANISH_LANG = (By.CSS_SELECTOR, "a.nav-link.nav-item[href='#switch-lang=es_US']")
    SIGN_IN_BUTTON = (By.ID, 'nav-link-accountList-nav-line-1')
    SIGN_IN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small' and contains(text(), 'Sign in')]")
    # SIGN_IN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-button')
    CART_ICON = (By.CSS_SELECTOR, "#nav-cart-count-container")
    HAM_MENU = (By.ID, "nav-hamburger-menu")

    def click_cart_icon(self, *locator):
        self.click(*self.CART_ICON)

    def input_search_text(self, search_word):
        self.input_text(search_word, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_BUTTON)

    def open_orders_icon(self, *locator):
        self.click(*self.ORDERS_LINK)

    def verify_sign_in(self, *locator):
        expected_result1 = 'Sign in'
        actual_result1 = self.find_element(*self.SIGN_IN_TEXT).text
        assert expected_result1 == actual_result1, f'Expected {expected_result1} but got actual {actual_result1}'

    def hover_language_options(self):
        lang_options = self.find_element(*self.LANG_OPTIONS)
        # spanish_lang = self.find_element(*self.SPANISH_LANG)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()

    def verify_spanish_option_present(self, *locator):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_department(self, alias):
        department_dd = self.find_element(*self.SELECT_DEPT)
        select = Select(department_dd)
        select.select_by_value(f'search-alias={alias}')
