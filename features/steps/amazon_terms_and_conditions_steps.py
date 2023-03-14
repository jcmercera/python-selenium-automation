from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from behave import given, when, then
from app.application import Application


@given('Open Amazon T&C page')
def open_t_and_c_page(context):
    context.app.main_page.open_url('https://www.amazon.com/gp/help/customer/display.html/ref'
                                   '=ap_register_notification_condition_of_use?ie=UTF8'
                                   '&nodeId=508088')


@when('Store original window')
def store_original_window(context):
    context.app.terms_and_conditions_page.store_t_c_page()


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.app.terms_and_conditions_page.click_privacy_notice_link()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.terms_and_conditions_page.switch_to_new_t_c_window()


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page_open(context):
    context.app.terms_and_conditions_page.verify_privacy_notice_page_open()


@then('User can close new window')
def close_new_window(context):
    context.app.main_page.close_new_window()


@then('Switch back to original')
def switch_back_to_original_window(context):
    context.app.main_page.switch_back_to_original_window()