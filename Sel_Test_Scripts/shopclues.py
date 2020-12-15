import time

from selenium import webdriver
#Launch Firefox browser
from selenium.webdriver import ActionChains

print("Firefox.........")
sc=webdriver.Firefox(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\geckodriver.exe")
print(type(sc))
sc.get("https://www.shopclues.com/wholesale.html")
url=sc.current_url
print(url)
#Title
title=sc.title
print(title)
ac=ActionChains(sc)
menu=sc.find_element_by_xpath("//a[text()='Mobiles & More']")
ac.move_to_element(menu).perform()
time.sleep(5)
mobile=sc.find_element_by_xpath("//strong[text()='Smartphones & Tablets']")
mobile.click()
time.sleep(10)
check_box=sc.find_element_by_xpath("//input[@value='1001.00-2500.00']")
ac.move_to_element(check_box)
check_box.click()
