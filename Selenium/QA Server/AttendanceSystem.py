import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from colorama import Fore, Back, Style
from CommonScripts.login import *
from selenium.common.exceptions import NoSuchElementException

PATH = "D:\Coding\Python\Selenium\chromedriver.exe"

login()
os.system('cls')
print(Fore.GREEN+'Test Started!')
print(Fore.RESET)

driver.get("http://172.16.10.4:8082/jw/web/userview/HRMAttendanceMOdule/hrmUserview/_/automatedAttendanceCrud")
print(Fore.YELLOW+driver.title)
print(Fore.RESET)
sleep(2)

# ----------------------------------------------------------SearchBar----------------------------------------------------------
try:
    searchbar = driver.find_element(By.ID, 'st')
    print(Fore.GREEN+'Searchbar Present')
    print(Fore.RESET)
except NoSuchElementException:
    print(Fore.RED+'Searchbar Missing')
    print(Fore.RESET)

try:
    searchbar = driver.find_element(By.XPATH, '//*[@title="Reset"]')
    print(Fore.GREEN+'Searchbar Reset Button Present')
    print(Fore.RESET)
except NoSuchElementException:
    print(Fore.RED+'Searchbar Reset Button Missing')
    print(Fore.RESET)

# ----------------------------------------------------------SearchBar----------------------------------------------------------

# ----------------------------------------------------------C.R.U.D----------------------------------------------------------
print(Fore.BLUE+'C.R.U.D Icons Test started')


# ----------------------------------------------------------Reset State----------------------------------------------------------

try:
    searchbar = driver.find_element(By.ID, 'reloadGridState')
    print(Fore.GREEN+'Reset State Button Present')
    print(Fore.RESET)

except NoSuchElementException:
    print(Fore.RED+'Reset State Button Missing')
    print(Fore.RESET)
# ----------------------------------------------------------Reset State----------------------------------------------------------
# ----------------------------------------------------------CSV----------------------------------------------------------
try:
    searchbar = driver.find_element(By.XPATH, '//*[@title="CSV"]')
    print(Fore.GREEN+'CSV Button Present')
    print(Fore.RESET)
except NoSuchElementException:
    print(Fore.RED+'CSV Button Missing')
    print(Fore.RESET)
# ----------------------------------------------------------CSV----------------------------------------------------------
# ----------------------------------------------------------Save State----------------------------------------------------------
try:
    searchbar = driver.find_element(By.XPATH, '//*[@title="Save State"]')
    print(Fore.GREEN+'Save State Button Present')
    print(Fore.RESET)
except NoSuchElementException:
    print(Fore.RED+'Save State Button Missing')
    print(Fore.RESET)
# ----------------------------------------------------------Save State----------------------------------------------------------

# ----------------------------------------------------------Load State----------------------------------------------------------
try:
    searchbar = driver.find_element(By.XPATH, '//*[@title="Load State"]')
    print(Fore.GREEN+'Load State Button Present')
    print(Fore.RESET)
except NoSuchElementException:
    print(Fore.RED+'Load State Button Missing')
    print(Fore.RESET)
# ----------------------------------------------------------Load State----------------------------------------------------------
# ----------------------------------------------------------Add----------------------------------------------------------
try:
    searchbar = driver.find_element(By.XPATH, '//*[@title="Add"]')
    print(Fore.GREEN+'Add Button Present')
    print(Fore.RESET)
except NoSuchElementException:
    print(Fore.RED+'Add Button Missing')
    print(Fore.RESET)
# ----------------------------------------------------------Add----------------------------------------------------------

# ----------------------------------------------------------Dormant----------------------------------------------------------
try:
    searchbar = driver.find_element(By.XPATH, '//*[@title="Dormant"]')
    print(Fore.GREEN+'Dormant Button Present')
    print(Fore.RESET)
except NoSuchElementException:
    print(Fore.RED+'Dormant Button Missing')
    print(Fore.RESET)
# ----------------------------------------------------------Dormant----------------------------------------------------------
try:
    searchbar = driver.find_element(By.XPATH, '//*[@title="Dormant"]')
    print(Fore.GREEN+'Dormant Button Present')
    print(Fore.RESET)
except NoSuchElementException:
    print(Fore.RED+'Dormant Button Missing')
    print(Fore.RESET)
# ----------------------------------------------------------Delete----------------------------------------------------------
try:
    searchbar = driver.find_element(By.XPATH, '//*[@title="Delete"]')
    print(Fore.GREEN+'Delete Button Present')
    print(Fore.RESET)
except NoSuchElementException:
    print(Fore.RED+'Delete Button Missing')
    print(Fore.RESET)
# ----------------------------------------------------------Delete----------------------------------------------------------

print(Fore.CYAN+'Test Completed')
print(Fore.RESET)
sleep(2)
