from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    HOME_PAGE_URL = "https://www.demoblaze.com/index.html"
    MODAL_FORM = (By.ID, 'logInModalLabel')

    # categories
    PHONES = (By.XPATH, '//a[contains(text(),"Phones")]')
    LAPTOPS = (By.XPATH, '//a[contains(text(),"Laptops")]')
    MONITORS = (By.XPATH, '//a[contains(text(),"Monitors")]')
    ABOUT_US_BOTTOM = (By.XPATH, '//b[contains(text(),"About Us")]/parent::h4/following-sibling::p')
    ABOUT_US_BOTTOM_INFO = ("We believe performance needs to be validated at every stage of the software development "
                            "cycle and our open source compatible, massively scalable platform makes that a reality.")

    BOTTOM_GET_IN_TOUCH = (By.XPATH, '//b[contains(text(),"Get in Touch")]')
    # ------------------
    NAV_BAR = "navbarExample"
    PRODUCTS_NR = (By.ID, 'tbodyid')
    PRODUCT_CLASS = (By.CLASS_NAME, "hrefch")

    def open(self):
        self.driver.get(self.HOME_PAGE_URL)

    def is_modal_form_displayed(self):
        # self.driver.implicitly_wait(1)
        assert self.find(self.MODAL_FORM).is_displayed()

    def check_categories_visibility(self, category_name):
        element = self.driver.find_element(By.XPATH, f'//a[contains(text(),"{category_name}")]')
        assert element, f' Error, element {category_name} is not visible!'

    def get_in_touch(self):
        get_in_touch_element = self.find(self.BOTTOM_GET_IN_TOUCH).text
        assert "Get in Touch" in get_in_touch_element

    def about_us(self):
        description = self.find(self.ABOUT_US_BOTTOM).text
        assert description == self.ABOUT_US_BOTTOM_INFO, "Description does  not match"

    def click_phones_category(self):
        self.click(self.PHONES)

    def click_laptops_category(self):
        self.click(self.LAPTOPS)

    def click_monitors_category(self):
        self.click(self.MONITORS)

    def check_items_display(self):
        sleep(1)
        products_list = self.find_all(self.PRODUCT_CLASS)
        assert (len(products_list) >= 1)
        for product in products_list:
            assert product.is_displayed(), "Error, product not visible."
