
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_PAGE_URL = "https://www.demoblaze.com/cart.html"
    CART_LINK = (By.LINK_TEXT, "Cart")

    ADD_CART_SAMSUNG_LINK = (By.LINK_TEXT, "Samsung galaxy s6")
    ADD_CART_SAMSUNG_BUTTON = (By.LINK_TEXT, "Add to cart")
    PRODUCT_DETAILS_H2 = (By.CLASS_NAME, 'name')
    SUCCES_MESSAGE_H2 = (By.XPATH, '//div[@class="sweet-alert  showSweetAlert visible"]/h2')

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
        self.driver.implicitly_wait(1)
        self.click(self.PURCHASE_BUTTON)

    def click_item(self):
        self.driver.implicitly_wait(1)
        self.click(self.ADD_CART_SAMSUNG_LINK)

    def element_displayed(self):
        return self.find(self.PRODUCT_DETAILS_H2).is_displayed(), "Product details is not displayed"

    def add_item_to_cart(self):
        sleep(2)
        self.click(self.ADD_CART_SAMSUNG_BUTTON)

    def verify_cart_item(self):
        count = len(self.find(self.CART_LIST))
        assert count == 2

    def set_name_input(self, name_input):
        self.type(self.NAME_INPUT, name_input)

    def set_country_input(self, country_input):
        self.type(self.COUNTRY_INPUT, country_input)

    def set_city_input(self, city_input):
        self.type(self.CITY_INPUT, city_input)

    def set_credit_input(self, credit_input):
        self.type(self.CREDIT_CARD_INPUT, credit_input)

    def set_month_input(self, month_input):
        self.type(self.MONTH_INPUT, month_input)

    def set_year_input(self, year_input):
        self.type(self.YEAR_INPUT, year_input)

    def verify_purchase_message(self, message):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SUCCES_MESSAGE_H2))
        actual = self.find(self.SUCCES_MESSAGE_H2).text
        assert message in actual, "No expected messsage"



