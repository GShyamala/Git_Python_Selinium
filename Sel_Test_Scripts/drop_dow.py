import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

dd=webdriver.Chrome(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\chromedriver.exe")
dd.get(r"https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
print(dd.current_url)
print(dd.title)
# cont=dd.find_element_by_name("country")
# sel=Select(cont)
# sel.select_by_value("INDIA")
# time.sleep(5)
# sel.select_by_index(4)
# time.sleep(5)
# sel.select_by_visible_text("AUSTRALIA")
# #get all options
# cont_opt=sel.options
# print(type(cont_opt))
# print(len(cont_opt))
# #To print even countries
# for each_opt in range (0,len(cont_opt)):
#     if  ((each_opt%2) == 0) :
#         print(cont_opt[each_opt].text)
# #To print ODD listed countries
# for each_opt in range(0,len(cont_opt)):
#     if ((each_opt%2)!=0):
#         cot_option=cont_opt[each_opt].get_attribute("value")
#         print(cot_option)

list_demo=dd.find_element_by_id("multi-select")
sel=Select(list_demo)
mul=sel.is_multiple
print("Multiple selection",mul)
sel.select_by_visible_text("California")
sel.select_by_value("New Jersey")
sel.select_by_index(4)
print("Selected opptions are")
sel_opt=sel.all_selected_options
for each_opt in sel_opt:
    print(each_opt.text)
print("first selected options")
print((sel.first_selected_option).text)
print("Deselect the options")
sel.deselect_by_visible_text("Ohio")
time.sleep(7)
sel.deselect_all()
