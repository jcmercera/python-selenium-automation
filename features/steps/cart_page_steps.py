from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from behave import given, when, then
from app.application import Application

CART_COUNT = (By.ID, 'nav-cart-count')
PRODUCT_TEXT = (By.CSS_SELECTOR, 'span.a-color-state a-text-bold')


@when('Open the cart page')
def open_the_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
    context.driver.wait.until(EC.element_to_be_clickable((CART_COUNT)))


@then('Verify if cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_count = context.driver.find_element(*CART_COUNT).text
    assert expected_count == actual_count, \
        f'Expected {expected_count}, but got actual {actual_count}'


@then('Product results for dress are shown')
def product_results_shown(context):
    context.app.cart_page.product_results_shown()

@then('Verify "Your Shopping Cart is empty." text present')
def cart_empty(context):
    context.app.cart_page.empty_cart()

# @then('Verify that text {expected_text} is shown')
# def verify_product_text_shown(context, expected_text):
#     actual_text = context.driver.find_element(*PRODUCT_TEXT).text
#     assert expected_text == actual_text, \
#         f'Expected {expected_text}, but got {actual_text}'
