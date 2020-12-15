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
# create_acc=driver.
# btn_login=driver.find_element_by_xpath("//button[@name='login']")
# btn_login.click()
# txt_box=driver.find_elements_by_xpath("//input[@class='inputtext _55r1 _6luy']")
# print(type(txt_box))
# print(len(txt_box))
# print(btn_login[0])
# print(btn_login[1])

# btn_login=driver.find_element_by_name("login")
# btn_login.click()
#Close the browser
# driver.quit()
