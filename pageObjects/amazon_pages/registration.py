from selenium.webdriver.common.by import By

from pageObjects import locators


class registration():
    def __init__(self,driver):
        self.driver=driver

        self.txt_name = driver.find_element(By.ID, locators.txt_name_id)
        self.txt_mobile = driver.find_element(By.ID, locators.txt_mobile_id)
        self.txt_email = driver.find_element(By.ID, locators.txt_email_id)
        self.txt_pword = driver.find_element(By.ID,locators.txt_pword_id)
        self.btn_continue = driver.find_element(By.ID, locators.btn_continue_id)

    def get_name_txt(self):
        return self.txt_name
    def get_mobile(self):
        return self.txt_mobile
    def get_email_txt(self):
        return self.txt_email
    def get_pword(self):
        return self.txt_pword
    def get_btn_continue(self):
        return self.btn_continue

