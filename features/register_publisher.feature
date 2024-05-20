Feature: Register publisher
  In order to keep track of the publishers that publish products
  As a user
  I want to register a publisher with all their data


  Background: There is a registered user
    Given Exists a user "user" with password "password"

    Scenario: Register a publisher with all data
    Given I login as user "user" with password "password"
    When I register a publisher data
        | name  |
        | Publisher test   |
    Then There are 1 publisher


    Scenario: Register a publisher with no data
    Given I login as user "user" with password "password"
    When I register a publisher data
        | name  |
    Then There are 0 publisher



    Scenario: Try to register steam user but not logged in
    Given I'm not logged in
    When I register a publisher data
        | name  |
        | Publisher test   |
    Then I'm redirected to the login form
    Then There are 0 publisher