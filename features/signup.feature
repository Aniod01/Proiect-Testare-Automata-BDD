Feature: Testing the Sign up functionality on DemoBlaze website
 Background:
    Given I am user on Demoblaze home page
    When  I click on Sign up page on top menu

 @sign_up_1
  Scenario: Test Sign up without inputs
    When  I click on Sign up button in the "Sign up" pop-up from
    Then  I should see a pop-up alert message "Please fill out Username and Password." and choose ok

 @sign_up_2
  Scenario: Test Sign up with registered user
    When I enter "aniod01" as Username on "Sign up" pop-up from
    When I enter "1234" as Password on "Sign up" pop-up from
    When I click on Sign up button in the "Sign up" pop-up from
    Then I should see a pop-up alert message "This user already exist." and choose ok

 @sign_up_3
  Scenario: Test Sign up with unregistered user and accept
    When  I enter "aniod15" as Username on "Sign up" pop-up from
    When  I enter "testtest" as Password on "Sign up" pop-up from
    When  I click on Sign up button in the "Sign up" pop-up from
    Then  I should see a pop-up alert message "Sign up successful." and choose ok


  @signup_close
  Scenario: Test Sign up function by clicking close
    When  I click on Close button in the "Sign up" pop-up from
    Then I am returned to DemoBlaze homepage "url"
