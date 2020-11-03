from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to_frame("packageListFrame")

driver.find_element_by_partial_link_text("html5").click()
time.sleep(3)

driver.back()
#driver.switch_to.default_content()

driver.switch_to_frame("packageFrame")
driver.find_element_by_partial_link_text("ChangeUrl").click()
time.sleep(3)

driver.back()

driver.switch_to_frame("classFrame")
driver.find_element_by_xpath('/html/body/div[1]/ul/li[5]').click()






