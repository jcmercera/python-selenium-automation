# Created by JeiM at 2/19/23
Feature: Amazon items in cart
   Scenario: User can add a product to the cart
    Given Open Amazon page
    When Input text coffee
    When Click on search button
    And Click on the first product
    And Click on Add to cart button
    And Open the cart page
    Then Verify if cart has 1 item(s)

