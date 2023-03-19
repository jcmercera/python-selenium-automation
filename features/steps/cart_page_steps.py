from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from behave import given, when, then
from app.application import Application


@when('Open the cart page')
def open_the_cart_page(context):
    context.app.cart_page.open_the_cart_page()


@then('Verify if cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    context.app.cart_page.verify_cart_count(expected_count)


@then('Product is added to the cart')
def product_is_added_to_cart(context):
    context.app.cart_page.verify_cart_count('1')


@then('Verify "Your Shopping Cart is empty." text present')
def verify_empty_cart(context):
    context.app.cart_page.verify_empty_cart()
