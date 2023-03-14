from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from behave import given, when, then
from pages.base_page import Page


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, '#twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, '#nav-search-submit-button')

    def input_search_text(self, search_word):
        self.input_text(search_word, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_BUTTON)
