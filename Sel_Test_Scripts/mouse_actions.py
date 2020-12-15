from selenium import webdriver
#Launch Firefox browser
from selenium.webdriver import ActionChains

print("Firefox.........")
driver=webdriver.Firefox(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\geckodriver.exe")
print(type(driver))
driver.get("http://www.greenstechnologys.com/")
url=driver.current_url
print(type(url))
print(url)
#Title
title=driver.title
print(type(title))
print(title)
courses_menu=driver.find_element_by_xpath("//a[text()='COURSES']")
cm=ActionChains(driver)

bd=driver.find_element_by_xpath("//span[text()='Oracle Training']")
cm.move_to_element(courses_menu).move_to_element(bd).perform()
# cm.move_to_element(bd).perform()
sql=driver.find_element_by_xpath("//span[text()='SQL Certification']")
sql.click()

