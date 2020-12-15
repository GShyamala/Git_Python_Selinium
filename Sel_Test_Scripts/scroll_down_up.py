import time

from selenium import webdriver

scroll=webdriver.Chrome(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\chromedriver.exe")
scroll.get("http://toolsqa.com/")
print(scroll.title)
print(scroll.current_url)
Rec_Articles=scroll.find_element_by_xpath("//span[text()='Recent Articles']")
scroll.execute_script("arguments[0].scrollIntoView(true)",Rec_Articles)
time.sleep(5)
share=scroll.find_element_by_xpath("//div[text()='Share this page']")
scroll.execute_script("arguments[0].scrollIntoView(true)",share)
time.sleep(5)
go_up=scroll.find_element_by_xpath("//span[text()='Latest Tutorials']")
scroll.execute_script("arguments[0].scrollIntoView(false)",go_up)