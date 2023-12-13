from time import sleep

from selenium.webdriver.common.by import By

from browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(Browser):

    # Functie care cauta si returneaza un Web Element dupa un locator dat
    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_text(self, locator, text):
        return self.driver.find_element(*locator, text)

    # Functie care cauta si returneaza o lista cu Web Elements dupa un locator dat (sub forma de tuplu)
    # Daca nu gaseste nimic, va returna o lista goala
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def is_element_absent(self, locator):
        elements = self.driver.find_elements(*locator)
        return len(elements) == 0

    # Functie care face click pe un Web Element
    def click(self, locator):
        # self.driver.find_element(*locator).click()
        self.find(locator).click()

    # Functie care scrie pe un Web Element si primeste 2 parametri
    def type(self, locator, text):
        self.find(locator).send_keys(text)

    # Functie care returneaza textul de pe un Web Element
    def get_text(self, locator):
        return self.find(locator).text

    def is_url_correct(self, url):
        assert self.driver.current_url == url, "The home page url is incorrect."

    def alert_ok(self):
        self.driver.switch_to.alert.accept()

    def alert_dismiss(self):
        self.driver.switch_to.alert.dismiss()

    def alert_get(self):
        return self.driver.switch_to.alert.text  # Functia care preia textul din popup alert

    def validate_confirmation_message_alert(self, message):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # assert self.alert_get() == message, "Unexpected alert message"
        assert message in self.alert_get(), "Unexpected alert message"
        self.alert_ok()
