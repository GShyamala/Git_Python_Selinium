import time

import keyboard
from selenium import webdriver
from selenium.webdriver import ActionChains

fkart=webdriver.Firefox(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\geckodriver.exe")
fkart.get("https://www.flipkart.com/")
url=fkart.current_url
print(url)
fk_title=fkart.title
print(fk_title)
login=fkart.find_element_by_xpath("//a[@class='_3Ep39l']")
ac=ActionChains(fkart)
ac.click(login)
time.sleep(5)
email=fkart.find_element_by_xpath("//input[@class='_2zrpKA _1dBPDZ']")
email.send_keys("abcd@gmail.com")
keyboard.press('control')
keyboard.press('a')
keyboard.release('control')
keyboard.release('a')
keyboard.press('control')
keyboard.press('c')
keyboard.release('control')
keyboard.release('c')
pword=fkart.find_element_by_xpath("//input[@class='_2zrpKA _3v41xv _1dBPDZ']")
pword.click()
time.sleep(3)
keyboard.press('control')
keyboard.press('v')
keyboard.release('control')
keyboard.release('v')

