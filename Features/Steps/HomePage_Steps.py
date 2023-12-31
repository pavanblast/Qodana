from behave import given, when


@when('User should be on dashboard page')
def i_should_be_on_dashboard_page(context):
    context.homepage.home_page_title()


@when('Multi language test on home page')
def i_verify_multi_language(context):
    context.homepage.multi_lang_test_for_arabic_on_home_page()
    context.homepage.multi_lang_test_for_hindi_on_home_page()
    context.homepage.multi_lang_test_for_french_on_home_page()
    context.homepage.multi_lang_test_for_spanish_on_home_page()
    context.homepage.multi_lang_test_for_english_on_home_page()


@when('Verify the days left and documents count')
def i_validate_days_left_and_used_documents_count(context):
    context.homepage.validate_days_left_and_used_documents_count()


@when('I verify document start options are displayed')
def i_verify_document_start_options_are_displayed(context):
    context.homepage.home_page_cards_visibility_check()


@when('I validate dashboard cards are displayed')
def i_validate_dashboard_cards_are_displayed(context):
    context.homepage.dash_board_cards_visibility_check()


@when('I validate counts on dashboard cards with "{userId}", "{companyID}" and "{Email}"')
def i_validate_counts_on_dashboard_cards(context, userId, companyID, Email):
    context.homepage.dash_board_cards_count_validation(userId, companyID, Email)


@when('I validate recent records and more button options')
def i_validate_recent_records_and_more_button_options(context):
    pass
