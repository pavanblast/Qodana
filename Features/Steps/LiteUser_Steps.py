from behave import given, when


@when('Navigate to add document page')
def add_document_page_navigation(context):
    context.liteuserpages.document_add_page()


@when('Upload all allowed valid files from the local machine and then click on next and again return to add step')
def add_document_page_navigation(context):
    context.liteuserpages.upload_files()


@when('Upload a file')
def file_upload(context):
    context.lite_user_file_upload_from_local_machine()


@when('Click on next button')
def file_upload(context):
    context.liteuserpages.next_button_click()
