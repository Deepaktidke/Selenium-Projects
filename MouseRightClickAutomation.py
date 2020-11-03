from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.google.com/")

GoogleSearch=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')

actions=ActionChains(driver)

actions.context_click(GoogleSearch).perform()