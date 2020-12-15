import time

from selenium import webdriver

hdfc=webdriver.Chrome(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\chromedriver.exe")
hdfc.get("https://netbanking.hdfcbank.com/netbanking/?_ga=2.176378149.1819882415.1533883212-608727520.1532670997")
print(hdfc.current_url)
print(hdfc.title)
time.sleep(5)
cnt=hdfc.find_elements_by_xpath("(//img[@alt='continue'])")
cnt.click()
time.sleep(3)
simple_alert=hdfc.switch_to.alert
print(simple_alert.text)
simple_alert.accept()
