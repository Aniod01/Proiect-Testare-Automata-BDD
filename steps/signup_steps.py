from behave import *


@when(u'I click on Sign up page on top menu')
def step_impl(context):
    context.sign_up_page.click_on_sign_up_menu()


@when(u'I enter "{username_text}" as Username on "Sign up" pop-up from')
def step_impl(context, username_text):
    context.sign_up_page.set_username_sign_up(username_text)


@when(u'I enter "{pass_text}" as Password on "Sign up" pop-up from')
def step_impl(context, pass_text):
    context.sign_up_page.set_password_sign_up(pass_text)


@when(u'I click on Sign up button in the "Sign up" pop-up from')
def step_impl(context):
    context.sign_up_page.click_sign_up_button()


@when(u'I click on Close button in the "Sign up" pop-up from')
def step_impl(context):
    context.sign_up_page.click_close_sign_up_button()
