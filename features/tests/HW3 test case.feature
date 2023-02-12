# Created by JeiM at 2/11/23
# BDD of HW2
Feature: Test scenarios sign in page

   Scenario: User sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click on Orders icon
    Then Verify if Sign In header is visible
     Then Verify if email input field is present

#Create a test case using BDD that opens amazon.com,
# clicks on the cart icon
# and verifies that Your Amazon Cart is empty.
  Scenario: User sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click on the cart icon
    Then Verify if cart is empty

############# Creative #############

  ##Scenario: User is able to add object to cart
    #Given Open Google page
    #When Input dress into search field
    #And Click on search icon
    #And Click on a dress
    #Then Product results for pants are shown