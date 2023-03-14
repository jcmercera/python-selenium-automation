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
    context.original_window = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.windows = context.driver.window_handles
    context.driver.switch_to.window(context.windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page_open(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html'))

    assert '/gp/help/customer/display.html' in context.driver.current_url, f'URL: {context.driver.current_url} does not contain the query'


@then('User can close new window')
def close_new_window(context):
    context.driver.close()


@then('Switch back to original')
def switch_back_to_original_window(context):
    context.driver.switch_to.window(context.original_window)
