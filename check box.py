from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")

driver.get("https://html.form.guide/checkbox/html-form-with-checkbox/")

driver.find_element_by_xpath('/html/body/div/div[2]/article/p[2]/input').click()