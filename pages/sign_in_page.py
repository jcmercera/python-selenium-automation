from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class SignInPage(Page):
    EMAIL_INPUT_FIELD = (By.ID, 'ap_email')

    def sign_in_page_open(self):
        self.wait.until(EC.url_contains('www.amazon.com/ap/signin?'))

    def verify_email_input(self, *locator):
        assert self.driver.find_element(*self.EMAIL_INPUT_FIELD), 'Email field not shown'
