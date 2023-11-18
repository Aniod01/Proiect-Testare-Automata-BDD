from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage(BasePage):
    HOME_PAGE_URL = "https://www.demoblaze.com/index.html"

    MODAL_FORM = (By.ID, 'logInModalLabel')
    TEXT = (By.XPATH, f'//a[contains(text(),"")]')
    # categories

    PHONES = (By.XPATH, '//a[contains(text(),"Phones")]')
    LAPTOPS = (By.XPATH, '//a[contains(text(),"Laptops")]')
    MONITORS = (By.XPATH, '//a[contains(text(),"Monitors")]')
    categories = (By.XPATH, f'//a[contains(text(), ]')

    def open(self):
        self.driver.get(self.HOME_PAGE_URL)

    def is_modal_form_displayed(self):
        #self.driver.implicitly_wait(1)
        assert self.find(self.MODAL_FORM).is_displayed()

    def check_categories_visibility(self, category_name):
        element = self.driver.find_element(By.XPATH, f'//a[contains(text(),"{category_name}")]')
        assert element, f'Element {category_name} is not visible or does not exists!'



