from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.maximize_window()


driver.get("http://testautomationpractice.blogspot.com/")


driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
time.sleep(5)


#close alert window using OK button
####driver.switch_to_alert().accept()


#closes alert using cancel buutton
driver.switch_to_alert().dismiss()
