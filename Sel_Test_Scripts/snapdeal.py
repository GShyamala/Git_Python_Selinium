import time

from selenium import webdriver
#Launch Firefox browser
from selenium.webdriver import ActionChains

print("Firefox.........")
sc=webdriver.Firefox(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\geckodriver.exe")
print(type(sc))
sc.get("https://www.snapdeal.com/")
url=sc.current_url
print(url)
#Title
title=sc.title
print(title)
mobile=sc.find_element_by_xpath("//span[text()='Mobile & Tablets']")
ac=ActionChains(sc)
ac.move_to_element(mobile).perform()
time.sleep(5)
smartphone=sc.find_element_by_xpath("//span[text()='Smartphones']")
smartphone.click()
time.sleep(10)
product_list=sc.find_elements_by_xpath("//p[@class='product-title ']")
print(type(product_list))
print("Products are :")
for i in range(0,3):
    print(product_list[i].text)
# print(phone1)
# print(phone2)
