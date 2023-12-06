from behave import *


@when(u'I click an item')
def step_impl(context):
    context.cart_page.click_item()


@then(u'I will be redirected to the product details')
def step_impl(context):
    assert context.cart_page.element_displayed(), "Product details is not displayed"


@when(u'I click Add to Cart')
def step_impl(context):
    context.cart_page.add_item_to_cart()


@then(u'Dialog box should open to enter details to place order')
def step_impl(context):
    context.cart_page.set_name_input("Lucian")
    context.cart_page.set_country_input("Ro")
    context.cart_page.set_city_input("Bn")
    context.cart_page.set_credit_input("Master")
    context.cart_page.set_month_input("Iulie")
    context.cart_page.set_year_input("2026")


@then(u'I should see successful message saying "{message}"')
def step_impl(context, message):
    context.cart_page.verify_purchase_message(message)


@when(u'I click on Cart on navigation menu')
def step_impl(context):
    context.cart_page.click_on_cart_nav_menu()

@then(u'I have "{number}" items in the cart list')
def step_impl(context, number):
    context.cart_page.verify_cart_nr_of_items(number)

@when(u'I click on Place Order on cart page')
def step_impl(context):
    context.cart_page.click_on_place_order()


@when(u'I click Purchase on place order popup')
def step_impl(context):
    context.cart_page.click_on_purchase()
