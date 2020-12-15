import time

from selenium import webdriver

sbi=webdriver.Chrome(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\chromedriver.exe")
# canara.get("https://netbanking.canarabank.in/entry/ENULogin.jsp")
# print(canara.current_url)
# print(canara.title)
# time.sleep(5)
# cnt=canara.find_element_by_xpath("//input[@type='submit']")
# cnt.click()
# time.sleep(3)
# s_a=canara.switch_to.alert
# print(s_a.text)
# s_a.accept()

sbi.get("https://retail.onlinesbi.com/retail/login.htm")
print(sbi.current_url)
print(sbi.title)
login=sbi.find_element_by_xpath("(//a[text()='CONTINUE TO LOGIN'])[1]")
login.click()
time.sleep(5)
login1=sbi.find_element_by_id("Button2")
login1.click()
time.sleep(3)
alert=sbi.switch_to.alert
print(alert.text)
alert.accept()