from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(15)

driver.switch_to_frame(0)
time.sleep(10)

driver.find_element_by_xpath('//*[@id="RESULT_FileUpload-10"]').send_keys()