import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from CommonScripts.login import *

PATH = "D:\Coding\Python\Selenium\chromedriver.exe"

login()
os.system('cls')
print('Test Started!')
sleep(2)


driver.get("http://172.16.10.4:8082/jw/web/userview/HRMAttendanceMOdule/hrmUserview/_/8A4476F801BF4E4998A50FB480FB292D")
print('HRM Attendance Management Opened')
sleep(2)
print('Test Finished')
