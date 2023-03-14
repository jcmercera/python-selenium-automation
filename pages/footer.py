from selenium.webdriver.common.by import By
from pages.base_page import Page


class Footer(Page):
    FOOTER_LINKS = (By.CSS_SELECTOR, "table.navFooterMoreOnAmazon td.navFooterDescItem")
