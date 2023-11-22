from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_PAGE_URL = "https://www.demoblaze.com/cart.html"
    CART_LINK = (By.LINK_TEXT, "Cart")

    ADD_CART_SAMSUNG_LINK = (By.LINK_TEXT, "Samsung galaxy s6")
    ADD_CART_SAMSUNG_BUTTON = (By.LINK_TEXT, "Add to cart")
    PRODUCT_DETAILS_H2 = (By.CLASS_NAME, 'name')

    CART_LIST = (By.ID, "tbodyid")
    PURCHASE_BUTTON = (By.XPATH, "//button[contains(text(),'Purchase')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Place Order')]")
    PURCHASE_SUCCESSFUL_MESSAGE = "Thank you for your purchase!"
    NAME_INPUT = (By.ID, "name")
    COUNTRY_INPUT = (By.ID, "country")
    CITY_INPUT = (By.ID, "city")
    CREDIT_CARD_INPUT = (By.ID, "card")
    MONTH_INPUT = (By.ID, "month")
    YEAR_INPUT = (By.ID, "year")

    def click_on_cart_nav_menu(self):
        self.click(self.CART_LINK)

    def click_on_place_order(self):
        self.driver.implicitly_wait(1)
        self.click(self.PLACE_ORDER_BUTTON)

    def click_on_purchase(self):
        self.click(self.PURCHASE_BUTTON)

    def click_item(self):
        self.driver.implicitly_wait(1)
        self.click(self.ADD_CART_SAMSUNG_LINK)

    def element_displayed(self):
        assert self.find(self.PRODUCT_DETAILS_H2).is_displayed(), "Product details is not displayed"
    def add_item_to_cart(self):
        sleep(1)
        self.click(self.ADD_CART_SAMSUNG_BUTTON)



