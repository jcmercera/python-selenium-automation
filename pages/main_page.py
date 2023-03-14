from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class MainPage(Page):

    def open_main_url(self):
        self.open_url('https://www.amazon.com/')






