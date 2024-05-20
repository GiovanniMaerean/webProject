Feature: Delete developer
  In order to keep cleaned the developers registered
  As a user
  I want to delete a developer that is no longer necessary

  Background: There is registered a user and a developer
    Given Exists a user "user" with password "password"
    And Exists a developer registered by user
      | name  |
      | Developer test   |


    Scenario: Delete a developer
    Given I login as user "user" with password "password"
    When I delete Developer test developer
    Then There are 0 developer


    Scenario: Try to delete developer but not logged in
    Given I'm not logged in
    When I delete Developer test developer
    Then I'm redirected to the login form
    And There are 1 developer