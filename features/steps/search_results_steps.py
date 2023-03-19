from selenium.webdriver.common.by import By
from behave import given, when, then
from app.application import Application


@when('Click on the first product')
def click_first_product(context):
    context.app.search_results_page.click_on_first_product()


@then('Verify that text {expected_result} is shown')
def verify_search_result(context, expected_result):
    context.app.search_results_page.verify_search_results(expected_result)


@then('Verify {category} department is selected')
def verify_product_dept_selected(context, category):
    context.app.search_results_page.verify_product_dept_selected(category)
