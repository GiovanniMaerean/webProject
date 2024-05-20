Feature: Register steam user
  In order to keep track of the steam users that exist
  As a user
  I want to register a steam user with all their info

  Background: There is a registered user
    Given Exists a user "user" with password "password"

    Scenario: Register a steam user with all data
    Given I login as user "user" with password "password"
    When I register a steam user data
        | steamID  | realName     | personaName  | country |
        | 123456   | John Doe     | johndoe123   | USA     |
    Then There are 1 steam user


    Scenario: Register a steam user with only steamID, realName and personaName
    Given I login as user "user" with password "password"
    When I register a steam user data
        | steamID  | realName     | personaName  |
        | 123456   | John Doe     | johndoe123   |
    Then There are 0 steam user


    Scenario: Register a steam user with only steamID and realName
    Given I login as user "user" with password "password"
    When I register a steam user data
        | steamID  | realName     |
        | 123456   | John Doe     |
    Then There are 0 steam user



    Scenario: Register a steam user with only steamID
    Given I login as user "user" with password "password"
    When I register a steam user data
        | steamID  |
        | 123456   |
    Then There are 0 steam user


    Scenario: Register a steam user with no data
    Given I login as user "user" with password "password"
    When I register a steam user data
        | steamID  |
    Then There are 0 steam user


    Scenario: Try to register steam user but not logged in
    Given I'm not logged in
    When I register a steam user data
        | steamID  | realName     | personaName  | country |
        | 123456   | John Doe     | johndoe123   | USA     |
    Then I'm redirected to the login form
    And There are 0 products
