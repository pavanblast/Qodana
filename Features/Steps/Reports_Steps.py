from behave import when,then


@when('I validate counts on Reports dashboard cards for "{companyid}"')
def validate_counts_of_reports(context, companyid):
    context.reportspage.fetch_records(companyid)


@then('I validate page headers are displayed')
def validate_headers(context):
    context.reportspage.validate_headers()


@then('I validate Donut chart')
def validate_donut_chart(context):
    context.reportspage.validate_donut_chart()


@then('I validate Bar chart')
def validate_bar_chart(context):
    context.reportspage.validate_bar_chart()


@then('I validate transaction reports display')
def validate_transaction_reports(context):
    context.reportspage.transactions_reports()
