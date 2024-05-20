Feature: Edit Steam user
  In order to keep updated my previous registers about steam users
  As a user
  I want to edit a steam user register I created

  Background: There is registered a user and a steam user
    Given Exists a user "user" with password "password"
    And Exists steam user registered by user
      | steamID  | realName     | personaName  | country |
      | 123456   | John Doe     | johndoe123   | USA     |


    Scenario: Edit Steam user personaName
    Given I login as user "user" with password "password"
    When I edit 123456 steam user
      | realName     | personaName  |
      | John Douglas     | johndouglas123   |
    Then The name of 123456 steam user is John Douglas
    And There are 1 steam user


    Scenario: Try to edit steam user but not logged in
    Given I'm not logged in
    When I edit 123456 steam user
      | realName     | personaName  |
      | John Douglas     | johndouglas123   |
    Then I'm redirected to the login form
    Then The name of 123456 steam user is John Doe