from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from behave import given, when, then



CART_COUNT = (By.ID, 'nav-cart-count')


@when('Open the cart page')
def open_the_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
    context.driver.wait.until(EC.element_to_be_clickable((CART_COUNT)))


@then('Verify if cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_count = context.driver.find_element(*CART_COUNT).text
    assert expected_count == actual_count, f'Expected {expected_count}, but got actual {actual_count}'


