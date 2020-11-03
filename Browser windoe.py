from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("http://demo.automationtesting.in/Windows.html")
time.sleep(3)
#driver.current_window_handle
#driver. window_handle

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
time.sleep(3)

print(driver.current_window_handle)

handles=driver.window_handles

for handle in handles:
    (driver.switch_to_window(handle))
    print(driver.title)
    driver.close()


time.sleep(3)

driver.close()

