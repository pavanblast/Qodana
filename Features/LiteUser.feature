Feature: Lite User
#  Scenario Outline: Valid files Upload verification
#    Given User login to application using "<Email>" and "<Password>"
#    When Navigate to add document page
#    And Upload all allowed valid files from the local machine and then click on next and again return to add step
#    Examples:
#      | Email                   | Password      |
#      | johnsmithinfo39@gmail.com | Signulu@1234 |


  Scenario Outline: Submit document by adding one recipient with all controls in parallel
    Given User login to application using "<Email>" and "<Password>"
    When Navigate to add document page
    And Upload a file
    And Click on next button
    And Add one recipient through add new recipient
    And Click on next
    And Drop all controls for initiator and recipient
    Examples:
      | Email                   | Password      |
      | johnsmithinfo39@gmail.com | Signulu@1234 |