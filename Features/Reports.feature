Feature: Reports
  Scenario Outline: Launch Reports page and validate the content
    Given User login to application using "<Email>" and "<Password>"
    When I validate counts on Reports dashboard cards for "<companyid>"
    Then I validate page headers are displayed
    And I validate Donut chart
    And I validate Bar chart
    And I validate transaction reports display

    Examples:
    |Email|Password|companyid|
    |mitisphere1@gmail.com|Signulu@1234|52|