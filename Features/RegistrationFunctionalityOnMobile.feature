Feature: Website
  Scenario: Verifying elements on Landing page.
    Given I navigate to registration page
    When  I enter email id and then click on create free account button
    And  I verify the thank you page
