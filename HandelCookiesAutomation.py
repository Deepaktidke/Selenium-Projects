from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.amazon.in/")

#Capture all the cookies
cookies=driver.get_cookies()

#it will print number of all the cookies >>len=length(how many)<<
print(len(cookies))

print(cookies)

####How to add new cookie to the browser
cookie={'name':'MyCookie','value':'1234567890'}
driver.add_cookie(cookie)

cookies=driver.get_cookies()

#it will print number of all the cookies >>len=length(how many)<<
print(len(cookies))

print(cookies)

#Delete the cookie

driver.delete_cookie('MyCookie')

cookies=driver.get_cookies()

#it will print number of all the cookies >>len=length(how many)<<
print(len(cookies))

print(cookies)

####Delete all the cookies

driver.delete_all_cookies()

cookies=driver.get_cookies()

#it will print number of all the cookies >>len=length(how many)<<
print(len(cookies))

print(cookies)

driver.quit()

