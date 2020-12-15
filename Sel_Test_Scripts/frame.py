from selenium import webdriver

driver=webdriver.Chrome(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\chromedriver.exe")
print(type(driver))
driver.get("http://demo.guru99.com/test/guru99home/")
url=driver.current_url
print(type(url))
print(url)
title=driver.title
print(type(title))
print(title)
driver.maximize_window()
# driver.switch_to.frame("a077aa5e")
# fr_ex=driver.find_element_by_xpath("//img[@src='Jmeter720.png']")
# fr_ex.click()
frme_path=driver.find_element_by_xpath("//iframe[@name='a077aa5e']")
driver.switch_to.frame(frme_path)
fr_ex=driver.find_element_by_xpath("//img[@src='Jmeter720.png']")
fr_ex.click()
list_frames=driver.find_elements_by_tag_name("iframe")
print(len(list_frames))
driver.switch_to.default_content()