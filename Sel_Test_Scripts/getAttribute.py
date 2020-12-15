from selenium import webdriver
#Launch Firefox browser
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
u_name=driver.find_element_by_id("email")
print(type(u_name))
u_name.send_keys("johan")
p_word=driver.find_element_by_id("pass")
print(type(p_word))
p_word.send_keys("123456")
uname_value=u_name.get_attribute("value")
pWord_value=p_word.get_attribute("value")
print(uname_value)
print(pWord_value)