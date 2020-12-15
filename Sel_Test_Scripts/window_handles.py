import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\chromedriver.exe")
print(type(driver))
driver.get("https://www.amazon.in/")
url=driver.current_url
print(url)
title=driver.title
print(title)
driver.maximize_window()
txt_search=driver.find_element_by_name("field-keywords")
txt_search.send_keys("iphone")
search=driver.find_element_by_xpath("(//input[@type='submit'])[1]")
search.click()
iphone=driver.find_element_by_xpath("(//div[@class='a-section aok-relative s-image-fixed-height'])[1]")
iphone.click()
par_id=driver.current_window_handle
print(par_id)
all_id=driver.window_handles
print(all_id)
driver.switch_to.window(all_id[1])
time.sleep(5)
add_cart=driver.find_element_by_id("add-to-cart-button")
add_cart.click()
time.sleep(5)
new_url=driver.current_url
print(new_url)
new_title=driver.title
print(new_title)
driver.switch_to.window(all_id[0])
time.sleep(5)
driver.switch_to.window(all_id[1])
time.sleep(5)
driver.close()

driver.quit()