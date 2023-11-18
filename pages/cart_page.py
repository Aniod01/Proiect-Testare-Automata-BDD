from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_PAGE_URL = "https://www.demoblaze.com/cart.html"
    CART_LINK = (By.LINK_TEXT, "Cart")
    # Elements mapping
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


