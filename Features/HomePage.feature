Feature: Home Page

  Scenario Outline: User is able to login and see dashboard page

    Given User login to application using "<Email>" and "<Password>"
    When Multi language test on home page
    When User should be on dashboard page
#    And I verify document start options are displayed
#    And I validate dashboard cards are displayed
#    And I validate counts on dashboard cards with "<userId>", "<companyID>" and "<Email>"
#    Then I validate recent records and more button options

    Examples:
      | Email                   | Password      |companyID|userId|
      | mitisphere2@gmail.com | Signulu@1234 |67         |158   |