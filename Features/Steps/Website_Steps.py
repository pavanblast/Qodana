import time

from behave import given, when


@given('Verifying nav bar elements in Landing page')
def nav_bar_elements_test(context):
    context.websitepages.landing_page_nav_bar_elements_redirection()


@when('Verifying start trial buttons click even and redirection test on Landing page')
def start_trail_buttons_test(context):
    context.websitepages.landing_page_start_trail_buttons()


@when('Verifying know more buttons click even and redirection test on Landing page')
def know_more_trail_buttons_test(context):
    context.websitepages.landing_page_know_more_buttons()


@when('Verifying videos on Landing page')
def videos_verification(context):
    context.websitepages.videos_validation()


@when('Verifying images on Landing page')
def images_verification(context):
    context.websitepages.landing_page_images_validation()


@when('Verifying Carousels section on Landing page')
def carousels_section(context):
    context.websitepages.carousels_validation()


@when('Verifying social media icons on Landing page')
def social_media_icons_redirection_test(context):
    context.websitepages.social_media_icons()


@given('Verifying nav bar elements in About page')
def nav_bar_elements_test(context):
    context.websitepages.about_page_nav_bar_elements_redirection()


@when('Verifying start trial buttons click even and redirection test on About page')
def start_trail_buttons_test(context):
    context.websitepages.about_page_start_trail_buttons()


@when('Verifying know more buttons click even and redirection test on About page')
def know_more_trail_buttons_test(context):
    context.websitepages.about_page_know_more_buttons()


@when('Verifying images on About page')
def images_verification(context):
    context.websitepages.about_page_images_validation()


@when('Verifying social media icons on About page')
def social_media_icons_redirection_test(context):
    context.websitepages.about_page_social_media_icons()
