from selenium import webdriver
#Launch Firefox browser
from selenium.webdriver import ActionChains

print("Firefox.........")
driver=webdriver.Firefox(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\geckodriver.exe")
print(type(driver))
driver.get("http://www.greenstechnologys.com")
url=driver.current_url
print(type(url))
print(url)
#Title
title=driver.title
print(type(title))
print(title)
contact=driver.find_element_by_xpath("//a[text()='CONTACT US']")
contact.click()
name=driver.find_element_by_id("InputName")
name.send_keys("abcd")
email=driver.find_element_by_id("InputEmail1")
email.send_keys("dfhdfd@gmail.com")
mobile=driver.find_element_by_id("InputSubject")
mobile.send_keys(12345678)
courses=driver.find_element_by_name("courses")
courses.send_keys("Python")
branch=driver.find_element_by_name("branch")
branch.send_keys("adyar")
time=driver.find_element_by_name("time")
time.send_keys("immediately")
msg=driver.find_element_by_name("comments")
msg.send_keys("join python")
submit=driver.find_element_by_id("submit")
submit.click()