Feature: Testing the Login/Logout functionality on DemoBlaze website
  Background:
    Given I am user on Demoblaze home page
    When  I click on Login page on top menu

  @login_without_inputs
  Scenario:Test Log in without inputs

    When  I click on Log in button in the "Log in" pop-up from
    Then  I should see a pop-up alert message "Please fill out Username and Password." and choose ok

  @login1
  Scenario: Test Log in using invalid username and valid password
    When I enter "doina" as Username on "Log in" pop-up from
    When I enter "1234" as Password on "Log in" pop-up from
    When I click on Log in button in the "Log in" pop-up from
    Then I should see a pop-up alert message "User does not exist." and choose ok
  @login2
  Scenario: Test Log in using valid username and invalid password
    When I enter "aniod01" as Username on "Log in" pop-up from
    When I enter "test" as Password on "Log in" pop-up from
    When I click on Log in button in the "Log in" pop-up from
    Then I should see a pop-up alert message "Wrong password." and choose ok

  @login_ok
  Scenario: Test Log in using valid credentials
    When I enter "aniod01" as Username on "Log in" pop-up from
    When I enter "1234" as Password on "Log in" pop-up from
    When I click on Log in button in the "Log in" pop-up from
    Then I should able to see Welcome "aniod01" in login page

  @logout
  Scenario: Test Log out
    When I enter "aniod01" as Username on "Log in" pop-up from
    When I enter "1234" as Password on "Log in" pop-up from
    When I click on Log in button in the "Log in" pop-up from
    When I click on  Log out button
    Then I am returned to DemoBlaze homepage "url"

  @login_close
  Scenario: Test Log in function by clicking close
    When  I click on Close button in the "Log in" pop-up from
    Then  I am returned to DemoBlaze homepage "url"



