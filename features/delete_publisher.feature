Feature: Delete publisher
  In order to keep cleaned the publishers registered
  As a user
  I want to delete a publisher that is no longer necessary

  Background: There is registered a user and a publisher
    Given Exists a user "user" with password "password"
    And Exists a publisher registered by user
      | name  |
      | Publisher test   |


    Scenario: Delete a publisher
    Given I login as user "user" with password "password"
    When I delete Publisher test publisher
    Then There are 0 publisher


    Scenario: Try to delete publisher but not logged in
    Given I'm not logged in
    When I delete Publisher test publisher
    Then I'm redirected to the login form
    And There are 1 publisher