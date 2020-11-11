from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

d=webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
d.maximize_window()

d.get("C:\chromedriver_win32\chromedriver.exe")

d.find_element_by_id("textbox").send_keys("abc")

d.find_element_by_id("createTxt").click()

