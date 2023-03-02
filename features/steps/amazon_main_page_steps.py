from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from behave import given, when, then


AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
BESTSELLER_LINKS = (By.CSS_SELECTOR, "#zg_header ul li")
FOOTER_LINKS = (By.CSS_SELECTOR, "table.navFooterMoreOnAmazon td.navFooterDescItem")
HEADER_LINKS = (By.CSS_SELECTOR, "#nav-xshop a.nav-a[data-csa-c-type='link']")
SIGN_IN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-button')

@given('Open Amazon bestsellers page')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')




@when('Input text {search_word}')
def input_search_word(context, search_word):
    context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(search_word)

@when('Click on search button')
def click_search(context):
    context.driver.find_element(*SEARCH_BUTTON).click()



@then('Verify that the bestseller banner has {expected_amount} links')
def verify_bestseller_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    bestseller_links = context.driver.find_elements(*BESTSELLER_LINKS)
    assert len(bestseller_links) == expected_amount, f'Expected {expected_amount} links but got {len(bestseller_links)}'




