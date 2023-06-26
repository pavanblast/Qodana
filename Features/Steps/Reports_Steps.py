from behave import given, when


@when('Validate count on reports page')
def reports_test(context):
    context.reportspage.fetch_records()