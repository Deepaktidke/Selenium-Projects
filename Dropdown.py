from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#to use select in dropdown
from selenium.webdriver.support.ui import Select
import time


driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")


driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#select one option
#capture options from dropdown
#count how many options ae pressent

driver.execute_script("window.scrollTo(0,600)")

drop=driver.find_element_by_id("RESULT_RadioButton-9")
drp=Select(drop)

#select by visible text
drp.select_by_visible_text('Morning')
time.sleep(5)


#select by index
drp.select_by_index(2)
time.sleep(5)


#select by value
drp.select_by_value("Radio-2")
time.sleep(5)


#count nummber of options
print(len(drp.options))


#print all the options and print them as output
all_options=drp.options

for option in all_options:
    print(option.text)








