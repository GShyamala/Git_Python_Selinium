from selenium import webdriver
#Launch Chrome browser
from selenium.webdriver import ActionChains

print("Chrome.........")
driver=webdriver.Chrome(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\chromedriver.exe")
print(type(driver))
driver.get("http://www.greenstechnologys.com/")
url=driver.current_url
print(type(url))
print(url)
#Title
title=driver.title
print(type(title))
print(title)
#Close the browser
# u_name=driver.find_element_by_id("email")
# print(type(u_name))
# u_name.send_keys("johan")
# p_word=driver.find_element_by_id("pass")
# print(type(p_word))
# p_word.send_keys("123456")
# btn_login=driver.find_element_by_name("login")
# btn_login.click()
#driver.quit()
#Launch Firefox
courses_menu=driver.find_element_by_xpath("//a[text()='COURSES']")
cm=ActionChains(driver)
cm.move_to_element(courses_menu).perform()
bd=driver.find_element_by_xpath("//span[text()='Oracle Training']")
cm.move_to_element(bd).perform()
sql=driver.find_element_by_xpath("//span[text()='SQL Certification']")
sql.click()
