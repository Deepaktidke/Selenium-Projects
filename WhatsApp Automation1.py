from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.maximize_window()


driver.get("https://web.whatsapp.com/")
time.sleep(15)

driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys("akki bro")

time.sleep(20)

driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[3]/div/div/div[2]').click()

for i in range(1000):
 driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("phone hacked")
 driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)







