import time

import keyboard as keyboard
from selenium import webdriver
#Launch Firefox browser
from selenium.webdriver import ActionChains
print("Firefox.........")
sc=webdriver.Firefox(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\geckodriver.exe")
print(type(sc))
sc.get("https://www.flipkart.com/")
url=sc.current_url
print(url)
#Title
title=sc.title
print(title)
uname=sc.find_element_by_xpath("//input[@class='_2zrpKA _1dBPDZ']")
uname.send_keys("abcdefgh")
pword=sc.find_element_by_xpath("//input[@class='_2zrpKA _3v41xv _1dBPDZ']")
ac=ActionChains(sc)
ac.double_click(uname).perform()
ac.context_click(uname).perform()
time.sleep(5)
def enter():
    keyboard.press("enter")
    keyboard.release("enter")
def key_board():
    time.sleep(2)
    keyboard.press("down arrow")
    keyboard.release("down arrow")
for i in range(0,5):
    key_board()
enter()
print("moving to pword")
ac.context_click(pword).perform()
time.sleep(5)
for i in range(0,5):
    key_board()
enter()




