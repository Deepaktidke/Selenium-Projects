from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.maximize_window()


driver.get("https://www.google.com/?gws_rd=ssl")

links=driver.find_elements_by_tag_name("a")

print(len(links))

for link in links:
    link.text
    print(link.text)


#partial link text
driver.find_element_by_link_text("Business").click()

time.sleep(5)

driver.back()

driver.find_element_by_partial_link_text("Gmail").click()

time.sleep(5)

driver.back()

#partial link text
driver.find_element_by_partial_link_text("ठी").click()





