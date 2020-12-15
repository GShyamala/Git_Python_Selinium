import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class baseClass():
    def feach_browser(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\chromedriver.exe")
        return self.driver
    def feach_url(self,url):
        self.driver.get(url)
    def current_url(self):
        c_url=self.driver.current_url
        return c_url
    def url_title(self):
        url_title=self.driver.title
        return url_title
    def insert_value(self,w_element,value):
        w_element.send_keys(value)
    def we_click(self,w_element):
        w_element.click()
    def mouseOver(self,w_element):
        self.ac = ActionChains(self.driver)
        self.ac.move_to_element(w_element).perform()
    def click(self):
        self.ac.click().perform()
    def r_click(self,w_element):
        self.ac.context_click(w_element).perform()
    def double_click(self,w_element):
        self.ac.double_click(w_element).perform()
    def print_capital(self,key_name,input_txt):
        self.ac.key_down(Keys.SHIFT, key_name).send_keys(input_txt).key_up(Keys.SHIFT, key_name).perform()
    def drag_and_drop(self,src,dest):
        self.ac.drag_and_drop(src,dest).perform()
    def click_and_hold(self,src,dest):
        self.ac.click_and_hold(src).release(dest)
    def switch_to_alert(self):
        self.alerts=self.driver.switch_to.alert
    def switch_to_frame(self,frame_id):
        self.frames=self.driver.switch_to.frame(frame_id)
    def switch_to_window(self,win_id):
        self.windows=self.driver.switch_to.window(win_id)
    def switch_to_parent(self):
        self.driver.switch_to.default_content()
    def alert_accept(self):
        self.alerts.accept()
    def alert_dismiss(self):
        self.alerts.dismiss()
    def send_text_to_alert(self,alert_text):
        self.alerts.send_keys(alert_text)
    def get_text_frm_alert(self):
        alrt_txt=self.alerts.text
        return alrt_txt
    def current_window(self):
        par_id=self.driver.current_window_handle
        return par_id
    def all_open_windows(self):
        all_id=self.driver.window_handles
        return all_id
    def close_current_window(self):
        self.driver.close()
    def close_all_driver_win(self):
        self.driver.quit()
    def sleep_mtd(self,sec):
        time.sleep(sec)
