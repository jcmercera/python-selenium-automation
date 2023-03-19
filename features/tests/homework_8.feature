# Created by JeiM at 3/18/23
Feature: Main page
  #### PRACTICE WITH ACTIONS AND SELECT.

 Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present


   ######Homework 8########

    Scenario: User can select and search in a department
       Given Open Amazon page
       When Select department by alias software
       When Input text faust
       When Click on search button
       Then Verify software department is selected

   Scenario: User can select colors
       Given Open Amazon product B074T9VX58 page
       When Hover over New Arrivals
       Then Verify user can see the deals
