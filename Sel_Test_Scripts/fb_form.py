import time

from selenium import webdriver
#Launch Firefox browser
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

print("Firefox.........")
driver=webdriver.Firefox(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\geckodriver.exe")
print(type(driver))
driver.get("https://www.facebook.com/")
url=driver.current_url
print(type(url))
print(url)
#Title
title=driver.title
print(type(title))
print(title)
new_acc=driver.find_element_by_id("u_0_2")
new_acc.click()
time.sleep(5)
fname=driver.find_element_by_name("firstname")
fname.send_keys("johan")
lname=driver.find_element_by_name("lastname")
lname.send_keys("paul")
mobile=driver.find_element_by_name("reg_email__")
mobile.send_keys("123456789")
pword=driver.find_element_by_id("password_step_input")
pword.send_keys("asdfg")
day=driver.find_element_by_id("day")
sel=Select(day)
sel.select_by_value("9")
# day.send_keys("9")
month=driver.find_element_by_id("month")
sel_month=Select(month)
sel_month.select_by_visible_text("Sep")
# month.send_keys("Jan")
year=driver.find_element_by_id("year")
sel_year=Select(year)
sel_year.select_by_visible_text("2010")
# year.send_keys("2010")
radio=driver.find_element_by_xpath("//label[text()='Male']")
radio.click()

