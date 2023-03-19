import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from behave import given, when, then


@given('Open Amazon product {product_id} page')
def open_product_page(context, product_id):
    context.app.product_page_page.open_product_page(product_id)


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.app.product_page_page.add_to_cart()


@when('Hover over New Arrivals')
def hover_over_new_arrivals(context):
    context.app.product_page_page.hover_over_new_arrivals()


@then('Verify user can click through colors')
def verify_user_can_select_product_colors(context):
    context.app.product_page_page.verify_user_can_select_product_colors()


@then('Verify user can see the deals')
def verify_new_arrivals_deals_shown(context):
    context.app.product_page_page.verify_new_arrivals_deals_shown()