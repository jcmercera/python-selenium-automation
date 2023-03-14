from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click on Orders icon')
def click_orders(context):
    context.app.header.open_orders_icon()


@then('Verify if Sign In header is visible')
def verify_sign_in(context):
    context.app.header.verify_sign_in()


@then('Verify if email input field is present')
def verify_email_input(context):
    context.app.sign_in_page.verify_email_input()


@when('Click on the cart icon')
def click_on_cart(context):
    context.app.cart_page.click_on_cart_count()


@then('Verify if cart is empty')
def empty_cart(context):
    context.app.cart_page.empty_cart()


