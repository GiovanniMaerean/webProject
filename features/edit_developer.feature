Feature: Edit Developer
  In order to keep updated my previous registers about developers
  As a user
  I want to edit a developer register I created

  Background: There is registered a user and a developer
    Given Exists a user "user" with password "password"
    And Exists developer registered by user with id 5b7c1d19-8f48-4d30-9322-24c73182f83e
      | name  |
      | Developer test   |


    Scenario: Edit developer name
    Given I login as user "user" with password "password"
    When I edit Developer test developer
      | name  |
      | Modified developer   |
    Then The name of 5b7c1d19-8f48-4d30-9322-24c73182f83e developer is Modified developer
    And There are 1 developer


    Scenario: Try to edit steam user but not logged in
    Given I'm not logged in
    When I edit Developer test developer
      | name  |
      | Modified developer   |
    Then I'm redirected to the login form
    Then The name of 5b7c1d19-8f48-4d30-9322-24c73182f83e developer is Developer test