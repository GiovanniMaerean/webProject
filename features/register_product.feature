Feature: Register product
  In order to keep track of the products someone has
  As a user
  I want to register a product with all their details and price

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register a product with all data
    Given I login as user "user" with password "password"
    When I register a product data
    | name         | appId | type   | age |  recommendations | releaseDate | categories          | genres     | price | discount | languages | description                   |
    | Hollow Knight| 367520| game   |  0  |  28799          | 2017-02-24  | Action, Adventure   | Adventure  | $14.99| 25       | English   | Descend into the Hallownest |
    Then There are 1 products

  Scenario: Register a product with only name, appId and type
    Given I login as user "user" with password "password"
    When I register a product data
    | name         | appId | type   |
    | Hollow Knight| 367520| game   |
    Then There are 1 products

  Scenario: Register a product with only name and appId
    Given I login as user "user" with password "password"
    When I register a product data
    | name         | appId |
    | Hollow Knight| 367520|
    Then There are 0 products

  Scenario: Register a product with only name
    Given I login as user "user" with password "password"
    When I register a product data
    | name         |
    | Hollow Knight|
    Then There are 0 products

    Scenario: Register a product with no data
    Given I login as user "user" with password "password"
    When I register a product data
    | name         |
    Then There are 0 products

  Scenario: Try to register product but not logged in
    Given I'm not logged in
    When I register a product data
    | name         | appId | type   | age |  recommendations | releaseDate | categories          | genres     | price | discount | languages | description                   |
    | Hollow Knight| 367520| game   |  0  |  28799          | 2017-02-24  | Action, Adventure   | Adventure  | $14.99| 25       | English   | Descend into the Hallownest |
    Then I'm redirected to the login form
    And There are 0 products