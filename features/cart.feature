Feature: Testing cart page functionality on DemoBlaze website
  Background:
    Given I am user on Demoblaze home page
@cart
Scenario: Test Cart function by placing order without items or inputs
    When  I click on Cart on navigation menu
    When  I click on Place Order on cart page
    When  I click Purchase on place order popup
    Then  I should see a pop-up alert message "Please fill out Name and Creditcard." and choose ok