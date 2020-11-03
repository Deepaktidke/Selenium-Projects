from selenium import webdriver
# To handle mouse action
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://en.wikipedia.org/wiki/Google")


driver.find_element_by_xpath('//*[@id="toc"]/ul/li[3]/ul/li[1]/a/span[2]')

driver.find_element_by_xpath('//*[@id="toc"]/ul/li[4]/a/span[2]')



