Feature: Testing the home page functionality on DemoBlaze website

  Background:
    Given I am user on DemoBlaze home page

  @category
  Scenario Outline:Verify that categories are shown
    Then I have visibility on category "<category_01>"
    Then I have visibility on category "<category_02>"
    Then I have visibility on category "<category_03>"
    Examples:
      | category_01 | category_02 | category_03 |
      | Phones      | Laptops     | Monitors    |

  @category_click
  Scenario: Verify that items of phones category are shown
    When    I click on "Phones" category link
    Then    Items of listed category is displayed

  Scenario: Verify that items of laptops category are shown
    When    I click on "Laptops" category link
    Then    Items of listed category is displayed

  Scenario: Verify that items of monitors category are shown
    When    I click on "Monitors" category link
    Then    Items of listed category is displayed

  @bottom_page
  Scenario: Check Get In Touch on the footer
    Then    Get In Touch section is correctly displayed

  Scenario: Check about us description on the footer
    Then   About Us section is correctly displayed
  @url
  Scenario: Check that the URL is correct
    Then    The URL of the page is "https://www.demoblaze.com/index.html"


#    @nav_menu
#  Scenario: Test that all items is present in navigation menu
#    Then  Navigation menu contains all item