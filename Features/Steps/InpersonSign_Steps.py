from behave import given, when


@when('Upload a file from local machine')
def file_upload_normal_user(context):
    context.inpersonsign.normal_user_file_upload_from_local_machine()


@when('Next move to select page and add one recipient and then select inperson')
def add_recipient_and_select_notary(context):
    context.inpersonsign.select_page_adding_recipient_selecting_notary()
    
@when('I drop controls for both the recipients')
def add_recipient_and_select_notary(context):
    context.inpersonsign.drop_controls_for_both_recipients()
