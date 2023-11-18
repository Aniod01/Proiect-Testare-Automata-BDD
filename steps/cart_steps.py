from behave import *


@when(u'I click on Cart on navigation menu')
def step_impl(context):
    context.cart_page.click_on_cart_nav_menu()


@when(u'I click on Place Order on cart page')
def step_impl(context):
    context.cart_page.click_on_place_order()


@when(u'I click Purchase on place order popup')
def step_impl(context):
    context.cart_page.click_on_purchase()
