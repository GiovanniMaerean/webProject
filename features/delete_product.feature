Feature: Delete product
  In order to keep cleaned the products registered
  As a user
  I want to delete a product that is no longer necessary

  Background: There is registered a user and a product
    Given Exists a user "user" with password "password"
    And Exists product registered by user
      | name         | appId | type   | age |  recommendations | releaseDate | categories          | genres     | price | discount | languages | description                   |
      | Hollow Knight| 367520| game   |  0  |  28799          | 2017-02-24  | Action, Adventure   | Adventure  | $14.99| 25       | English   | Descend into the Hallownest |


    Scenario: Delete a product
    Given I login as user "user" with password "password"
    When I delete Hollow Knight product
    Then There are 0 products


    Scenario: Try to delete product but not logged in
    Given I'm not logged in
    When I delete Hollow Knight product
    Then I'm redirected to the login form
    And There are 1 products