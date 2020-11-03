from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)

driver.find_element_by_id("txtUsername").send_keys("Admin")

driver.find_element_by_id("txtPassword").send_keys("admin123")

driver.find_element_by_id("btnLogin").click()

time.sleep(5)

#driver.switch_to_alert().accept()

#driver.switch_to_alert().dismiss()

admon=driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')

user=driver.find_element_by_id("menu_admin_UserManagement")

usermng=driver.find_element_by_id("menu_admin_viewSystemUsers")

actions=ActionChains(driver)

actions.move_to_element(admon).move_to_element(user).move_to_element(usermng).click().perform()



