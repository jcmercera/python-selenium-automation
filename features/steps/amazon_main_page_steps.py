from behave import given, when, then
from app.application import Application
from selenium import webdriver


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_url()


@given('Open Amazon bestsellers page')
def open_amazon_bestsellers(context):
    context.app.main_page.open_url('www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@when('Click on cart icon')
def click_on_cart_icon(context):
    context.app.header.click_cart_icon()


@when('Click Amazon Orders link')
def click_amazon_orders_link(context):
    context.app.header.open_orders_icon()


@when('Input text {search_word}')
def input_search_text(context, search_word):
    context.app.header.input_search_text(search_word)


@when('Click on search button')
def click_search(context):
    context.app.header.click_search()


@when('Hover over language options')
def hover_language_options(context):
    context.app.header.hover_language_options()


@when('Select department by alias {alias}')
def select_department(context, alias):
    context.app.header.select_department(alias)


@then('Verify that the bestseller banner has {expected_amount} links')
def verify_bestseller_link_count(context, expected_amount):
    context.app.search_results_page.banner_link_amount(expected_amount)


@then('Verify Spanish option present')
def verify_spanish_option_present(context):
    context.app.header.verify_spanish_option_present()
