from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

x=webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
x.maximize_window()

x.get("https://testautomationpractice.blogspot.com/")


x.find_element_by_id("RESULT_FileUpload-10").send_keys("C:/Users/deepak.tidke/Pictures/Screenshots/Screenshot(79).png")