from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from behave import given, when, then




@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()

@given('Open Amazon product {product_id} page')
def open_product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')

@then('Verify user can click through colors')
def verify_user_can_select_product_colors(context):
    context.driver.find_element(*COLOR_OPTIONS).click()

    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print('All colors:', all_color_options)
    expected_colors = ('Black', 'Bluestone', 'Brite Lime', 'Brite Orange', 'Carbon Heather', 'Carhartt Brown', 'Desert', 'Fire Red Heather', 'Heather Gray', 'Jade Heather', 'Lakeshore', 'Malachite', 'Marine Blue Heather', 'Moonstone Nep', 'Navy', 'North Woods Heather', 'Oiled Walnut Heather', 'Pale Apricot Nep', 'Port', 'Sundance Heather', 'Terracotta', 'White')

    actual_colors = []
    for color in all_color_options:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print('Current color:', current_color)
        actual_colors += [current_color]

    assert expected_colors == actual_colors, f'Expected {expected_colors}, but got {actual_colors}'

