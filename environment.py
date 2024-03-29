from browser import Browser
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.sign_up_page import SignUpPage


def before_all(context):
    context.browser = Browser()
    context.base_page = BasePage()
    context.home_page = HomePage()
    context.login_page = LoginPage()
    context.sign_up_page = SignUpPage()
    context.cart_page = CartPage()

def after_all(context):
    context.browser.close()
