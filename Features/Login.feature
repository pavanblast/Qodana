Feature: Login
  Scenario Outline: User is able to login and see dashboard pageples.
    Given User login to application using "<Email>" and "<Password>"
    When Logout from the application
    Examples:
      | Email                   | Password      |
      | mitisphere1@gmail.com | Signulu@1234 |

#  Scenario: Login page negative scenarios
#    Given Verifying elements on login page
#    When Verifying elements of Terms and condition popup
#    And Verifying elements of Privacy policy popup
#    And Login without providing email and password fields
#    And Login without providing Email field
#    And Login without providing password field
#    And Login without validating the captcha
#    And Login with invalid email id
#    And Login with invalid Password <Email>
#    And Verifying elements on Forgot password
#    And Sending reset password link with email
#    Then Login with valid email <email> and password <password> and then Logout
#    Then Close the browser