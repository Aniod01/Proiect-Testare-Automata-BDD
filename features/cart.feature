Feature: Testing cart page functionality on DemoBlaze website
  Background:
    Given I am user on Demoblaze home page

@place_order
Scenario: Test place order successfully with inputs but "0" item.
    When I click on Cart on navigation menu
    Then I have "0" items in the cart list
    When I click on Place Order on cart page
    Then Dialog box should open to enter details to place order
    When I click Purchase on place order popup
    Then I should see successful message saying "Thank you for your purchase!"

@cart_no_inputs
Scenario: Test Cart function by placing order without items or inputs
    When  I click on Cart on navigation menu
    Then  I have "0" items in the cart list
    When  I click on Place Order on cart page
    When  I click Purchase on place order popup
    Then  I should see a pop-up alert message "Please fill out Name and Creditcard." and choose ok

@add_to_cart
Scenario: Test add an item to cart
	When I click an item
	Then I will be redirected to the product details
	When I click Add to Cart
	Then I should see a pop-up alert message "Product added" and choose ok
    When I click on Cart on navigation menu
    Then I have "1" items in the cart list


