from behave import given, when


@given('I navigate to registration page')
def register_page_navigation(context):
    context.registrationpageonmobile.mobile_registration_page_navigation()


@when('I enter email id and then click on create free account button')
def enter_email_and_click_on_create_free_account_btn(context):
    context.registrationpageonmobile.enter_email_and_ciclk_on_btn()


@when('I verify the thank you page')
def thank_you_page(context):
    context.registrationpageonmobile.thank_you_page_verification()
