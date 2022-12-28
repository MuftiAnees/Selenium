import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from CommonScripts.login import *
from selenium.common.exceptions import NoSuchElementException


PATH = "D:\Coding\Python\Selenium\chromedriver.exe"

login()
os.system('cls')
print('Test Started!')
sleep(2)


driver.get("http://172.16.10.4:8082/jw/web/userview/HRMAttendanceMOdule/hrmUserview/_/8A4476F801BF4E4998A50FB480FB292D")
print('HRM Attendance Management Opened')
print(driver.title)
sleep(2)

try:
    searchbar = driver.find_element(By.ID, 'st')
except NoSuchElementException:
    print('Searchbar Missing')


search = driver.find_element(
    By.XPATH, '//*[@id="category-container"]/li').click()
sleep(2)
search = driver.find_element(
    By.XPATH, '//*[@id="D59C07C9D89C425C82EC4A06963CB6CA"]/a').click()

print(driver.title)
try:
    searchbar = driver.find_element(By.ID, 'st')
except NoSuchElementException:
    print('Searchbar Missing')

print('Test Completed')
sleep(2)
