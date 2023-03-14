from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from time import sleep





# @given('Open Amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')


@when('Click on Orders icon')
def click_orders(context):
    context.driver.find_element(By.XPATH, "//span[@class='nav-line-2' and text()= '& Orders']").click()


@then('Verify if Sign In header is visible')
def verify_sign_in(context):
    expected_result1 = 'Sign in'
    actual_result1 = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small' and contains(text(), 'Sign in')]").text
    assert expected_result1 == actual_result1, f'Expected {expected_result1} but got actual {actual_result1}'


@then('Verify if email input field is present')
def verify_email_input(context):
    assert context.driver.find_element(By.ID, 'ap_email'), 'Email field not shown'



@when('Click on the cart icon')
def click_on_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()


@then('Verify if cart is empty')
def empty_cart(context):
    assert context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Your Amazon Cart is empty')]"), "Empty Cart is not Verified"

############# Creative #############


#@when('Input text {search_word}')
#def input_search_word(context, search_word):
    #context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)


#@when('Click on search button')
#def click_search(context):
    #context.driver.find_element(By.ID, 'nav-search-submit-button').click()


#@when('Click on a dress')
#def click_dress(context):
    #context.driver.find_element(By. )
