from pages.base_page import Page
from selenium.webdriver.common.by import By


class TermsAndConditions(Page):
    PRIVACY_NOTICE = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")


