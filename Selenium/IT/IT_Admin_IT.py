import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from colorama import Fore, Back, Style
from selenium.common.exceptions import NoSuchElementException


PATH = "D:\Coding\Python\Selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("http://172.16.10.4:8082/jw/web/login")
sleep(2)
search = driver.find_element(By.ID, "j_username")
search.send_keys("15001")
search = driver.find_element(By.ID, "j_password")
search.send_keys("Care@123")
search = driver.find_element(By.NAME, "submit").click()
# print("Login Successful!")
# sleep(2)

driver.get(
    "http://172.16.10.4:8082/jw/web/userview/pac_IT/pac_IT_UV/_/C8F5DC67202C40858B66764F9A71C78B")
sleep(4000)