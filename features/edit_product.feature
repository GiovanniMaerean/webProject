Feature: Edit Product
  In order to keep updated my previous registers about products
  As a user
  I want to edit a product register I created

  Background: There is registered a user and a product
    Given Exists a user "user" with password "password"
    And Exists product registered by user
      | name         | appId | type   | age |  recommendations | releaseDate | categories          | genres     | price | discount | languages | description                   |
      | Hollow Knight| 367520| game   |  0  |  28799          | 2017-02-24  | Action, Adventure   | Adventure  | $14.99| 25       | English   | Descend into the Hallownest |


    Scenario: Edit product price
    Given I login as user "user" with password "password"
    When I edit Hollow Knight product
      | price           |
      | $11.49           |
    Then The price of Hollow Knight is $11.49
    And There are 1 products


    Scenario: Try to edit product but not logged in
    Given I'm not logged in
    When I edit Hollow Knight product
      | price           |
      | $11.49           |
    Then I'm redirected to the login form
    Then The price of Hollow Knight is $14.99