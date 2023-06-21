import time

from behave import given, when


@given('User login to application using "{Email}" and "{Password}"')
def login_with_valid_details(context, Email, Password):
    context.loginpage.landing_page_login_button_click()
    context.loginpage.email_and_psw_inputs(Email, Password)
    context.loginpage.captcha_enter()
    context.loginpage.login_click()
    context.loginpage.home_page_text()


@when('Logout from the application')
def log_out(context):
    context.loginpage.log_out()


@given('Verifying elements on login page')
def elements_verification_on_login_page(context):
    time.sleep(3)
    context.loginpage.login_page_signulu_logo_validation()
    context.loginpage.login_page_headers_validations()
    context.loginpage.login_page_paragraphs_validations()


@when(u'Verifying elements of Terms and condition popup')
def step_impl(context):
    pass


@when(u'Verifying elements of Privacy policy popup')
def step_impl(context):
    pass


@when(u'Login without providing email and password fields')
def step_impl(context):
    pass


@when(u'Login without providing Email field')
def step_impl(context):
    pass


@when(u'Login without providing password field')
def step_impl(context):
    pass


@when(u'Login without validating the captcha')
def step_impl(context):
    pass


@when(u'Login with invalid email id')
def step_impl(context):
    pass


@when(u'Login with invalid Password <Email>')
def step_impl(context):
    pass


@when(u'Verifying elements on Forgot password')
def step_impl(context):
    pass
