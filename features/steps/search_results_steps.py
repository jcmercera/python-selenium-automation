from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


PRODUCT_PRICE = (By. CSS_SELECTOR, "span.a-price")


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()
