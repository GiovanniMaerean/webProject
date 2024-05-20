Feature: Delete steam user
  In order to keep cleaned the steam users registered
  As a user
  I want to delete a steam user that is no longer necessary

  Background: There is registered a user and a steam user
    Given Exists a user "user" with password "password"
    And Exists steam user registered by user
      | steamID  | realName     | personaName  | country |
      | 123456   | John Doe     | johndoe123   | USA     |


    Scenario: Delete a steam user
    Given I login as user "user" with password "password"
    When I delete 123456 steam user
    Then There are 0 steam user


    Scenario: Try to delete steam user but not logged in
    Given I'm not logged in
    When I delete 123456 steam user
    Then I'm redirected to the login form
    And There are 1 steam user