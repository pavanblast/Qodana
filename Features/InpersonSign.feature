Feature: In person sign functionality

  Scenario Outline: User is able to create document by adding inperson recipient and submit the document.

    Given User login to application using "<Email>" and "<Password>"
    When Move to prepare page and drop the controls
#    When User should be on dashboard page
#    And Upload a file from local machine
#    And Click on next button
#    And Next move to select page and add one recipient and then select inperson
#    And Click on next button
#    When Move to prepare page and drop the controls
#    Then I validate recent records and more button options

    Examples:
      | Email                   | Password      |companyID|userId|
      | mitisphere2@gmail.com | Signulu@1234 |67         |158   |