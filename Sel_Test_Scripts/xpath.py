from selenium import webdriver
#Launch Firefox browser
print("Firefox.........")
driver=webdriver.Firefox(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\geckodriver.exe")
print(type(driver))
driver.get("https://www.facebook.com/")
url=driver.current_url
print(type(url))
print(url)
#Title
title=driver.title
print(type(title))
print(title)
uname_txt=driver.find_element_by_xpath("//input[@id='email']")
uname_txt.send_keys("johan")
pword_txt=driver.find_element_by_xpath("//input[@id='pass']")
pword_txt.send_keys(1214143)
word_txt=driver.find_element_by_xpath("//a[text()='Create a Page']")
print(type(word_txt))
word=word_txt.text
print(word)
wel_text=driver.find_element_by_xpath("//h2[contains(text(),'Facebook')]")
welcome=wel_text.text
print(welcome)
new_acc=driver.find_element_by_xpath("//a[contains(@id,'u_0_2')]")
new_account=new_acc.text
print(new_account)
uname_id=uname_txt.get_attribute("id")
print(uname_id)
uname_value=uname_txt.get_attribute("value")
print(uname_value)