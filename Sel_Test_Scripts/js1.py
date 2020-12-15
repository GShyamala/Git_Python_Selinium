from selenium import webdriver

driver=webdriver.Chrome(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\chromedriver.exe")
print(type(driver))
driver.get("https://www.facebook.com/")
url=driver.current_url
print(type(url))
print(url)
#Title
title=driver.title
print(type(title))
print(title)
driver.maximize_window()
u_name=driver.find_element_by_id("email")
driver.execute_script("arguments[0].setAttribute('value','johan')",u_name)
txt_uname=driver.execute_script("return arguments[0].getAttribute('value')",u_name)
print(txt_uname)
# u_name.send_keys("johan")
p_word=driver.find_element_by_id("pass")
driver.execute_script("arguments[0].setAttribute('value','12345')",p_word)
txt_pword=driver.execute_script("return arguments[0].getAttribute('value')",p_word)
print(txt_pword)
# p_word.send_keys("123456")
btn_login=driver.find_element_by_name("login")
driver.execute_script("arguments[0].click()",btn_login)
# btn_login.click()
#driver.quit()