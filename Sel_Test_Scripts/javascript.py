import time

from selenium import webdriver

ex_script=webdriver.Firefox(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\geckodriver.exe")
ex_script.get("https://www.flipkart.com/")
print(ex_script.title)
print(ex_script.current_url)
ex_script.maximize_window()
time.sleep(10)
uname=ex_script.find_element_by_xpath("//input[@class='_2IX_2- VJZDxU']")
ex_script.execute_script("arguments[0].setAttribute('value','johan')",uname)
txt_uname=ex_script.execute_script("return arguments[0].getAttribute('value')",uname)
print(txt_uname)
pword=ex_script.find_element_by_xpath("//input[@type='password']")
# pword.send_keys("12345")
ex_script.execute_script("arguments[0].setAttribute('value','12345')",pword)
txt_pword=ex_script.execute_script("return arguments[0].getAttribute('value')",pword)
print(txt_pword)
btn_login=ex_script.find_element_by_xpath("//button[@class='L0Z3Pu']")
ex_script.execute_script("arguments[0].click()",btn_login)
# print(btn_login.is_selected())
# print(btn_login.is_displayed())

