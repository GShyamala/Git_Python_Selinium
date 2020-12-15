from selenium import webdriver

driver=webdriver.Chrome(executable_path=r"C:\Users\sony\PycharmProjects\SeleniumTestProj\Drivers\chromedriver.exe")
print(type(driver))
driver.get("https://www.w3schools.com/tags/ref_byfunc.asp")
url=driver.current_url
print(url)
title=driver.title
print(title)
driver.maximize_window()
list_tables=driver.find_elements_by_tag_name("table")
print("No of tables are",len(list_tables))
table=list_tables[3]
print("Whole table content is\n",table.text)
table=driver.find_element_by_xpath("(//table[@class='w3-table-all notranslate'])[1]")
trows=table.find_elements_by_tag_name("tr")
print("_________Printing the last 2 rows________________")
for i in range(0,len(trows)):
    each_row=trows[i]
    if (i>len(trows)-3):
        print(each_row.text)
print("_________All Odd rows are:___________________")
for i in range(0,len(trows)):
    each_row=trows[i]
    if (i%2 == 0):
        print(each_row.text)
print("________All Even rows are:________________________")
for i in range(0,len(trows)):
    each_row=trows[i]
    if (i%2 != 0):
        print(each_row.text)
print("________Printing only headings_____________________")
t_head=table.find_elements_by_tag_name("th")
for each_head in t_head:
    print(each_head.text)
print("_________Alternate rows are:_______________________")
for i in range(0,len(trows)):
    each_row=trows[i]
    if (i%2 == 0):
        print(each_row.text)
t_data=table.find_elements_by_tag_name("td")
print("__________Print only 1st 3 data____________________")
for i in range(0,len(t_data)):
    if i<3:
        print(t_data[i].text)

print("__________Get particular data")
for i in range(0,len(trows)):
    t_datas=trows[i].find_elements_by_tag_name("td")
    for j in range(0,len(t_datas)):
        if t_datas[j].text == "Defines a comment":
            print(t_datas[j].text)
            print("Required data present at row No",i,"Cell No",j)