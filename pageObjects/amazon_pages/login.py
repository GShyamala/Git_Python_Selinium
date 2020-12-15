from selenium.webdriver.common.by import By

from pageObjects import locators


class loginPage():
    def __init__(self, driver):
        self.driver=driver

        self.login_btn = driver.find_element(By.ID,locators.login_btn_id)

    def get_click_login(self):
        return self.login_btn

