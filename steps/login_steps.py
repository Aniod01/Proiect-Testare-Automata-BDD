from behave import *


@when(u'I click on Login page on top menu')
def step_impl(context):
    context.login_page.click_on_login_menu()


@when(u'I click on Log in button in the "Log in" pop-up from')
def step_impl(context):
    context.login_page.click_login_button()


@then(u'I should see a pop-up alert message "{message}" and choose ok')
def step_impl(context, message):
    # context.home_page.alert_login(message)
    context.base_page.validate_confirmation_message_alert(message)


@when(u'I enter "{username_text}" as Username on "Log in" pop-up from')
def step_impl(context, username_text):
    context.login_page.set_username(username_text)


@when(u'I enter "{pass_text}" as Password on "Log in" pop-up from')
def step_impl(context, pass_text):
    context.login_page.set_password(pass_text)


@then(u'I should able to see Welcome "{user}" in login page')
def step_impl(context, user):
    context.login_page.check_login_link(user)


@when(u'I click on  Log out button')
def step_impl(context):
    context.login_page.click_logout_button()


@when(u'I click on Close button in the "Log in" pop-up from')
def step_impl(context):
    context.login_page.click_close_button()


@then(u'I am returned to DemoBlaze homepage "{url}"')
def step_impl(context, url):
    context.login_page.is_url_correct(url), "The home page url is incorrect."
