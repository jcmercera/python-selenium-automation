from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class MainPage(Page):
    HAM_MENU = (By.ID, 'nav-hamburger-menu')
    FOOTER_LINKS = (By.CSS_SELECTOR, "table.navFooterMoreOnAmazon td.navFooterDescItem")
    HEADER_LINKS = (By.CSS_SELECTOR, "#nav-xshop a.nav-a[data-csa-c-type='link']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-button')
    ORDERS_LINK = (By.CSS_SELECTOR, "a[href='/gp/css/order-history?ref_=nav_orders_first']")
    CART_ICON = (By.CSS_SELECTOR, "#nav-cart-count-container")

    def open_main(self):
        self.open_url('www.amazon.com')

    def click_cart_icon(self, *locator):
        self.driver.main.click(*self.CART_ICON)
