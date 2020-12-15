import time

import keyboard as keyboard
from selenium import webdriver
#Launch Firefox browser
print("Firefox.........")
rb=webdriver.Firefox(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\geckodriver.exe")
rb.get("https://www.redbus.in/")
url=rb.current_url
print(url)
title=rb.title
print(title)
def key_board():
    keyboard.press("enter")
    keyboard.release("enter")
rb_from=rb.find_element_by_xpath("//input[contains(@id,'src')]")
rb_from.send_keys("Madurai")
time.sleep(3)
key_board()
rb_to=rb.find_element_by_xpath("//input[contains(@id,'dest')]")
rb_to.send_keys("Chennai")
time.sleep(3)
key_board()
date=rb.find_element_by_id("onward_cal")
date.click()
time.sleep(5)
next=rb.find_element_by_xpath("//td[@class='next']")
next.click()
time.sleep(5)
book_date=rb.find_element_by_xpath("//td[text()='23']")
book_date.click()
search=rb.find_element_by_xpath("//button[text()='Search Buses']")
search.click()


