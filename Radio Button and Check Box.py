from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


#how to provide value to the text box
driver.find_element_by_id("RESULT_TextField-1").send_keys("Deepak")

driver.find_element_by_id("RESULT_TextField-2").send_keys("Tidke")

driver.find_element_by_id("RESULT_TextField-3").send_keys("9503562999")

# to scroll the webpage
driver.execute_script("window.scrollTo(0,200)")


#Radio button selected or not by using method "is_selected()"
# .click
status=driver.find_element_by_id("RESULT_RadioButton-7_1").is_selected()  #true/false
print(status)
time.sleep(5)


driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[1]/td/label').click()
time.sleep(5)
statu=driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[1]/td/label').is_selected()
print(statu)

