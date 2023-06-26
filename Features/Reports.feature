Feature: Reports
  Scenario Outline: User is able to login and see dashboard pageples.
    Given User login to application using "<Email>" and "<Password>"
    When Validate count on reports page
    Examples:
      | Email                   | Password      |
      | mitisphere2@gmail.com | Signulu@1234 |