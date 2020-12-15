from selenium import webdriver
#Launch Firefox browser
from selenium.webdriver import ActionChains

print("Firefox.........")
driver=webdriver.Firefox(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\geckodriver.exe")
print(type(driver))
driver.get("http://demo.guru99.com/test/drag_drop.html")
url=driver.current_url
print(type(url))
print(url)
#Title
title=driver.title
print(type(title))
print(title)
bank_box=driver.find_element_by_id("credit2")
dd=ActionChains(driver)
dest_box=driver.find_element_by_xpath("//ol[@id='bank']")
dd.drag_and_drop(bank_box,dest_box).perform()
src_amount=driver.find_element_by_id("fourth")
dest_box2=driver.find_element_by_xpath("//ol[@id='amt7']")
dd.drag_and_drop(src_amount,dest_box2).perform()
src_box=driver.find_element_by_id("credit1")
dest_box3=driver.find_element_by_id("loan")
dd.click_and_hold(src_box).release(dest_box3).perform()
# dd.release(dest_box3).perform()
src_amt=driver.find_element_by_id("fourth")
des_box4=driver.find_element_by_id("amt8")
dd.click_and_hold(src_amt).release(des_box4).perform()
# dd.release(des_box4).perform()
#
