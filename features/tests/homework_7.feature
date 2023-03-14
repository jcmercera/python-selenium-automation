# Created by JeiM at 3/12/23
Feature: Amazon page
  # Enter feature description here

 Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amazon page
 When Click Amazon Orders link
 Then Verify Sign In page is opened


Scenario: 'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon page
 When Click on cart icon
 Then Verify "Your Shopping Cart is empty." text present


 Scenario: User is able to add object to cart
  Given Open Amazon page
  When Input text table
  And Click on search button
  And Click on the first product
  And Click on Add to cart button
  Then Product is added to the cart