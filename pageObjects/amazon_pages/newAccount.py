from selenium.webdriver.common.by import By

from pageObjects import locators


class new_Account():
    def __init__(self, driver):
        self.driver=driver

        self.create_btn = driver.find_element(By.ID,locators.create_Acc_btn_id)

    def get_click_create(self):
        return self.create_btn