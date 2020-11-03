from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#how to find how many input boxes are present in web page

INPUTBOEX=driver.find_elements_by_class_name("text_field")


#print to show the result of how many input boxex are present
print(len(INPUTBOEX))

status=driver.find_element_by_id("RESULT_TextField-1").is_displayed()
print("Displayed or not :",status)  #true/false

Status=driver.find_element_by_id("RESULT_TextField-1").is_enabled()
print("Enabled or not",status)   #enable or not


#how to provide value to the text box
driver.find_element_by_id("RESULT_TextField-1").send_keys("Deepak")

driver.find_element_by_id("RESULT_TextField-2").send_keys("Tidke")

driver.find_element_by_id("RESULT_TextField-3").send_keys("9503562999")

driver.quit()
