from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignUpPage(BasePage):
    SIGN_UP_LINK = (By.ID, "signin2")
    INPUT_USERNAME_SIGN_UP = (By.ID, "sign-username")
    INPUT_PASSWORD_SIGN_UP = (By.ID, "sign-password")
    BUTTON_SIGN_UP = (By.XPATH, '//button[contains(text(),"Sign up")]')
    BUTTON_CLOSE_SIGN_UP = (By.XPATH, '//div[@id="signInModal"]//button[contains(text(),"Close.")]')

    def click_on_sign_up_menu(self):
        self.driver.implicitly_wait(1)
        self.click(self.SIGN_UP_LINK)

    def set_username_sign_up(self, username_text):
        self.type(self.INPUT_USERNAME_SIGN_UP, username_text)

    def set_password_sign_up(self, pass_text):
        self.type(self.INPUT_PASSWORD_SIGN_UP, pass_text)

    def click_sign_up_button(self):
        self.click(self.BUTTON_SIGN_UP)

    def click_close_sign_up_button(self):
        self.driver.implicitly_wait(1)
        self.click(self.BUTTON_CLOSE_SIGN_UP)

    def alert_sign_up(self):
        self.test_validate_confirmation_message_alert()
