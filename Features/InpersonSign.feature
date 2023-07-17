Feature: In person sign functionality

  Scenario Outline: User is able to create document by adding inperson recipient and submit the document.

    Given User login to application using "<Email>" and "<Password>"
    When User should be on dashboard page
    And Upload a file from local machine
    And Click on next button
    And Next move to select page and add one recipient and then select notary
    And Click on next button
    And I drop controls for both the recipients

    Examples:
      | Email                   | Password      |companyID|userId|
      | mitisphere1@gmail.com | Signulu@1234 |67         |158   |