from behave import given, when, then
from app.application import Application
from selenium import webdriver


@then('Verify Sign In page is opened')
def sign_in_page_is_open(context):
    context.app.sign_in_page.sign_in_page_open()

