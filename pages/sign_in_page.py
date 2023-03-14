from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class SignInPage(Page):
    def sign_in_page_open(self, query):
        self.driver.main.verify_url_query('www.amazon.com/ap/signin?')