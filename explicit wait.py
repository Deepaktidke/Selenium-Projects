from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.expedia.co.in/")

driver.find_element_by_xpath('//*[@id="uitk-tabs-button-container"]/li[2]/a').click()

driver.find_element_by_xpath('//*[@id="uitk-tabs-button-container"]/div/li[2]').click()

driver.find_element_by_class_name("uitk-faux-input").send_keys("Mumbai")

driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/header/section/div/input').send_keys("NYC")
