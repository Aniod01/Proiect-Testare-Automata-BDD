Feature: Testing the home page functionality on DemoBlaze website

  Background:
    Given I am user on DemoBlaze home page

  @category
  Scenario Outline:Test that categories are shown
    Then I have visibility on category "<category_01>"
    Then I have visibility on category "<category_02>"
    Then I have visibility on category "<category_03>"
    Examples:
      | category_01 | category_02 | category_03 |
      | Phones      | Laptops     | Monitors    |

  Scenario: Check that the URL is correct
    Then The URL of the page is "https://www.demoblaze.com"
