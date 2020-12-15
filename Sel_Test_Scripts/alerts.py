import time
from selenium import webdriver

alert_test=webdriver.Firefox(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\geckodriver.exe")
print(type(alert_test))
alert_test.get("http://demo.automationtesting.in/Alerts.html")
url=alert_test.current_url
print(url)
title=alert_test.title
print(title)
simple_alert=alert_test.find_element_by_xpath("//button[@class='btn btn-danger']")
simple_alert.click()
time.sleep(3)
s_a=alert_test.switch_to.alert
print(s_a.text)
s_a.accept()
conform_alert=alert_test.find_element_by_xpath("(//a[@class='analystic'])[2]")
conform_alert.click()
conform_alert1=alert_test.find_element_by_xpath("//button[@class='btn btn-primary']")
conform_alert1.click()
time.sleep(3)
c_a=alert_test.switch_to.alert
print(c_a.text)
c_a.dismiss()
promt_alert=alert_test.find_element_by_xpath("(//a[@class='analystic'])[3]")
promt_alert.click()
promt_alert1=alert_test.find_element_by_xpath("//button[@class='btn btn-info']")
promt_alert1.click()
time.sleep(3)
p_a=alert_test.switch_to.alert
p_a.send_keys("Automation testing")
p_a.accept()
