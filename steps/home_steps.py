from behave import *


@given(u'I am user on DemoBlaze home page')
def step_impl(context):
    context.home_page.open()


@then(u'I have visibility on category "{category_name}"')
def step_impl(context, category_name):
    context.home_page.check_categories_visibility(category_name)


@then(u'The URL of the page is "{url}"')
def step_impl(context, url):
    context.home_page.is_url_correct(url), "The login page url is incorrect."
