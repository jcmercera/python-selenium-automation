from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class TermsAndConditions(Page):
    PRIVACY_NOTICE = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")

    def click_privacy_notice_link(self, *locator):
        self.find_element(*self.PRIVACY_NOTICE).click()

    def store_t_c_page(self):
        self.store_original_window()

    def switch_to_new_t_c_window(self):
        self.switch_to_new_window()

    def verify_privacy_notice_page_open(self):
        self.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html'))
        assert '/gp/help/customer/display.html' in self.driver.current_url, f'URL: {self.driver.current_url} does not contain the query'
