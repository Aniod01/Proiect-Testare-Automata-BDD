from selenium import webdriver


class Browser:
    driver = webdriver.Chrome()
    driver.maximize_window()

    def close(self):
        self.driver.quit()
