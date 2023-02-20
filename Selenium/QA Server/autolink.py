import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from colorama import Fore, Back, Style
from CommonScripts.login import *
from selenium.common.exceptions import NoSuchElementException

PATH = "D:\Coding\Python\Selenium\chromedriver.exe"

driver.maximize_window()
login()
os.system('cls')
print(Fore.GREEN+'------------------------------------------------------------Test Started!------------------------------------------------------------')
print(Fore.RESET)

links = ["http://172.16.10.4:8082/jw/web/userview/litigationMgmt/litigationMgmtUv/_/court"]
total_number_of_links = len(links)
linkNumber = 0


while linkNumber != total_number_of_links:
    driver.get(links[linkNumber])
    print(Fore.YELLOW+driver.title)
    print(Fore.RESET)
    sleep(5)

    # print(driver.find_elements(
    #     By.XPATH, "//*[@title='Configuration']//child::li"))
    print(driver.find_elements(
        By.XPATH, "//*[@id='category-container']/li[1]/a//child::li"))

    # for link in linktest:
    #     print("link")

    # ----------------------------------------------------------SearchBar----------------------------------------------------------
    MandatorySearchBar = 0
    try:
        searchbar = driver.find_element(By.ID, 'st')
        print(Fore.GREEN+'Searchbar Present')
        print(Fore.RESET)
        MandatorySearchBar += 1
    except NoSuchElementException:
        print(Fore.RED+'Searchbar Missing')
        print(Fore.RESET)

    try:
        searchbar = driver.find_element(By.XPATH, '//*[@title="Reset"]')
        print(Fore.GREEN+'Searchbar Reset Button Present')
        print(Fore.RESET)
        MandatorySearchBar += 1
    except NoSuchElementException:
        print(Fore.RED+'Searchbar Reset Button Missing')
        print(Fore.RESET)

    # ----------------------------------------------------------SearchBar----------------------------------------------------------
    # ----------------------------------------------------------GRID TESTING----------------------------------------------------------

    print(Fore.CYAN+'Final Result:')
    print(Fore.RESET)

    if MandatorySearchBar == 2:
        print(Fore.GREEN+'Searchbar Test Passed')
        print(Fore.RESET)
    else:
        print(Fore.RED+'Searchbar Test Failed')
        print(Fore.RESET)

    linkNumber += 1
print(Fore.CYAN+'Test Completed')
print(Fore.RESET)
sleep(2)
