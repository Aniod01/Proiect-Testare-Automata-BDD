from time import sleep

from selenium import webdriver


class Browser:
    driver = webdriver.Chrome()
    driver.maximize_window()

    def close(self):
        sleep(1)
        self.driver.quit()