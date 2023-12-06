from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(BasePage):
    LOGIN_LINK = (By.ID, "login2")
    INPUT_USERNAME = (By.ID, "loginusername")
    INPUT_PASSWORD = (By.ID, "loginpassword")
    BUTTON_LOGIN = (By.XPATH, '//button[contains(text(),"Log in")]')
    MODAL_FORM = (By.CSS_SELECTOR, 'h5[id=logInModalLabel]')
    BUTTON_CLOSE = (By.XPATH, '//div[@id="logInModal"]//button[contains(text(),"Close")]')
    LOGOUT_LINK = (By.LINK_TEXT, "Log out")

    def click_on_login_menu(self):
        self.driver.implicitly_wait(1)
        self.click(self.LOGIN_LINK)

    def set_username(self, username_text):
        # self.driver.find_element(*self.INPUT_EMAIL).send_keys(email_text)
        self.type(self.INPUT_USERNAME, username_text)

    def set_password(self, pass_text):
        self.type(self.INPUT_PASSWORD, pass_text)

    def click_login_button(self):
        self.click(self.BUTTON_LOGIN)

    def click_close_button(self):
        self.click(self.BUTTON_CLOSE)

    def click_logout_button(self):
        sleep(3)
        self.click(self.LOGOUT_LINK)
        assert self.find(self.LOGIN_LINK).is_displayed()

    def is_modal_form_displayed(self):
        assert self.find(self.MODAL_FORM).is_displayed()

    # def alert_login(self, message):
    #     self.test_validate_confirmation_message_alert(message)
    def check_login_link(self, user):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, f'//a[contains(text(),"{user}")]')))
        assert self.driver.find_element(By.XPATH,
                                        f'//a[contains(text(), "{user}")]').is_displayed(), "I am not in my account page"
