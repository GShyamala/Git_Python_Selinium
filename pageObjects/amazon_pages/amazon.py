from pageObjects.amazon_pages.login import loginPage
from pageObjects.amazon_pages.newAccount import new_Account
from pageObjects.amazon_pages.registration import registration
from pageObjects import Input_details
from selenium import webdriver
from base_pkg.all_methods import baseClass
b=baseClass()
driver=b.feach_browser()
print(type(driver))
url="https://www.amazon.in"
b.feach_url(url)
c_url=b.current_url()
print("url is ",c_url)
url_title=b.url_title()
print("Title is",url_title)
l=loginPage(driver)
b.we_click(l.get_click_login())
b.sleep_mtd(5)
n=new_Account(driver)
b.we_click(n.get_click_create())
b.sleep_mtd(5)
r=registration(driver)
name_txt=r.get_name_txt()
b.insert_value(name_txt,Input_details.name)
mobile=r.get_mobile()
b.insert_value(mobile,Input_details.mobile)
email=r.get_email_txt()
b.insert_value(email,Input_details.email)
pword=r.get_pword()
b.insert_value(pword,Input_details.pword)
clk_cont=r.get_btn_continue()
b.we_click(clk_cont)
