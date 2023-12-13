from behave import *


@given(u'I am user on DemoBlaze home page')
def step_impl(context):
    context.home_page.open()


@then(u'I have visibility on category "{category_name}"')
def step_impl(context, category_name):
    context.home_page.check_categories_visibility(category_name)

@then(u'Get In Touch section is correctly displayed')
def step_impl(context):
    context.home_page.verify_get_in_touch_text_is_correct()

@then(u'About Us section is correctly displayed')
def step_impl(context):
    context.home_page.verify_about_us_text_is_correct()

@when(u'I click on "Phones" category link')
def step_impl(context):
    context.home_page.click_phones_category()
@when(u'I click on "Laptops" category link')
def step_impl(context):
    context.home_page.click_laptops_category()

@when(u'I click on "Monitors" category link')
def step_impl(context):
    context.home_page.click_monitors_category()

@then(u'Items of listed category is displayed')
def step_impl(context):
    context.home_page.check_items_display()
@then(u'The URL of the page is "{url}"')
def step_impl(context, url):
    context.home_page.is_url_correct(url)
