Feature: Register developer
  In order to keep track of the developers that make products
  As a user
  I want to register a developer with all their data

  Background: There is a registered user
    Given Exists a user "user" with password "password"

    Scenario: Register a developer with all data
    Given I login as user "user" with password "password"
    When I register a developer data
        | name  |
        | Developer test   |
    Then There are 1 developer



    Scenario: Register a developer with no data
    Given I login as user "user" with password "password"
    When I register a developer data
        | name  |
    Then There are 0 developer



    Scenario: Try to register steam user but not logged in
    Given I'm not logged in
    When I register a developer data
        | name  |
        | Developer test   |
    Then I'm redirected to the login form
    And There are 0 developer