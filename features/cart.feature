Feature: Testing cart page functionality on DemoBlaze website
  Background:
    Given I am user on Demoblaze home page

@add_to_cart
Scenario: Test add an item to cart
	When I click an item
	Then I will be redirected to the product details
	When I click Add to Cart
	Then I should see a pop-up alert message "Product added" and choose ok


@cart
Scenario: Test Cart function by placing order without items or inputs
    When  I click on Cart on navigation menu
    When  I click on Place Order on cart page
    When  I click Purchase on place order popup
    Then  I should see a pop-up alert message "Please fill out Name and Creditcard." and choose ok