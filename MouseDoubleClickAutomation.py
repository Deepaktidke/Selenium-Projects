from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

element=driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')

actions=ActionChains(driver)

actions.double_click(element).perform() #Double click on element
time.sleep(5)


driver.quit()