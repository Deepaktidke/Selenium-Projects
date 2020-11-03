from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")

driver.get("http://www.stealmylogin.com/demo.html")

ele=driver.find_element_by_name("username")

print(ele.is_displayed())

print(ele.is_enabled())

ele.send_keys("abc")

elem=driver.find_element_by_name("password")

print(elem.is_displayed())

print(elem.is_enabled())

elem.send_keys("xyz")

driver.find_element_by_name("login").click()