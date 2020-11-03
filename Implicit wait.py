from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("https://my.naukri.com/account/createaccount?othersrcp=23531&wExp=N&utm_source=google&utm_medium=cpc&utm_campaign=Brand_Login_Register&gclid=EAIaIQobChMIwuOv0J_V7AIV0XwrCh29owJ4EAAYASAAEgKue_D_BwE")

driver.implicitly_wait(10)

driver.find_element_by_xpath("/html/body/header/div[1]/p/a").click()

driver.find_element_by_id("usernameField").send_keys("deeptidke2919@gmail.com")

driver.find_element_by_id("passwordField").send_keys("Protected1010@")

driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/div[3]/div/button[1]').click()


