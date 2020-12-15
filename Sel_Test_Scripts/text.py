from selenium import webdriver
#Launch Firefox browser
print("Firefox.........")
gt=webdriver.Firefox(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\geckodriver.exe")
print(type(gt))
gt.get("http://www.greenstechnologys.com")
url=gt.current_url
print(type(url))
print(url)
#Title
title=gt.title
print(type(title))
print(title)
para=gt.find_element_by_xpath("//font[contains(text(),'We at Greens Technology have been in IT industry for nearly')]")
para1=gt.find_element_by_xpath("//font[contains(text(),'emerging technologies like')]")
para_text=para.text
para_text1=para1.text
print(para_text+" "+para_text1)
# print(para_text1)