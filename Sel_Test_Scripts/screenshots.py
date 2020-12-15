import time

from selenium import webdriver

screen=webdriver.Chrome(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\chromedriver.exe")
screen.get("https://www.facebook.com/")
screen.save_screenshot(r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Sel_Test_Scripts\GreensTech.png")
fb=screen.find_element_by_id("email")
display=fb.is_displayed()
print("Displyed or not",display)
sub_btn=screen.find_element_by_id("u_0_2")
enab=sub_btn.is_enabled()
print("Enabled or not....",enab)
sub_btn.click()
time.sleep(5)
radio_btn=screen.find_element_by_xpath("(//input[@name='sex'])[1]")
sele=radio_btn.is_selected()
print("Selected or not....",sele)
radio_btn.click()
sele1=radio_btn.is_enabled()
print("Radio button clicked.........", sele1)

