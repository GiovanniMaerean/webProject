Feature: Edit Publisher
  In order to keep updated my previous registers about publishers
  As a user
  I want to edit a publisher register I created

  Background: There is registered a user and a publisher
    Given Exists a user "user" with password "password"
    And Exists publisher registered by user with id 5b7c1d19-8f48-4d30-9322-24c73182f83e
      | name  |
      | Publisher test   |


    Scenario: Edit publisher name
    Given I login as user "user" with password "password"
    When I edit Publisher test publisher
      | name  |
      | Modified Publisher   |
    Then The name of 5b7c1d19-8f48-4d30-9322-24c73182f83e publisher is Modified Publisher
    And There are 1 publisher


    Scenario: Try to edit steam user but not logged in
    Given I'm not logged in
    When I edit Publisher test publisher
      | name  |
      | Modified Publisher   |
    Then I'm redirected to the login form
    Then The name of 5b7c1d19-8f48-4d30-9322-24c73182f83e publisher is Publisher test