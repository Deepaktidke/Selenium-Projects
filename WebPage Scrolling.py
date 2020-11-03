from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.youtube.com/watch?v=aqXkKgkyk2I&list=PLUDwpEzHYYLvx6SuogA7Zhb_hZl3sln66&index=16")

time.sleep(10)

#To scroll till particular pixel hight
driver.execute_script("window.scrollBy(0,1000)""")

time.sleep(10)

#To find particular element in page
#a = driver.find_element_by_xpath('//*[@id="video-title"]')
#driver.execute_script("arguments[0],scrollIntoView();", a)




#To sccroll till the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

driver.quit()