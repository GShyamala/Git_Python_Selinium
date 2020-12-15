from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

key=webdriver.Firefox(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\geckodriver.exe")
key.get("http://www.greenstechnologys.com/")
name=key.title
print(name)
contact=key.find_element_by_xpath("//a[text()='CONTACT US']")
contact.click()
ac=ActionChains(key)
key.maximize_window()
name=key.find_element_by_id("InputName")
ac.key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()
ac.key_down(Keys.SHIFT,name).send_keys("abcdefg").key_up(Keys.SHIFT,name).perform()
email=key.find_element_by_id("InputEmail1")
ac.key_down(Keys.SHIFT,email).send_keys("dfhdfd@gmail.com").key_up(Keys.SHIFT,email).perform()
mobile=key.find_element_by_id("InputSubject")
mobile.send_keys(12345678)
courses=key.find_element_by_name("courses")
courses.send_keys("Python")
branch=key.find_element_by_name("branch")
branch.send_keys("adyar")
time=key.find_element_by_name("time")
time.send_keys("immediately")
msg=key.find_element_by_name("comments")
msg.send_keys("join python")
submit=key.find_element_by_id("submit")
submit.click()