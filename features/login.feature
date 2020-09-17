Feature: Login feature

  Background:
    Given I am on the website

  Scenario Outline: Test login feature with valid parameters
    When I enter username "<username>" and password "<password>"
    And I click login button
    Then User must login successfully to the page
    Examples:
      | username | password |
      | admin    | admin123 |

  Scenario Outline: Test login feature with invalid parameters

    When I enter username "<username>" and password "<password>"
    And I click login button
    Then invalid message should be displayed
    Examples:
      | username | password |
      | admin1   | admin    |
      | abc      | abc123   |