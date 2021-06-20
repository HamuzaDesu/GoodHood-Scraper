from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import sys
import os
import json

config = 0
with open('goodHoodScraper\config.json', 'r') as f:
    config = json.load(f)
    print(config)

PATH = "C:\Program Files (x86)\chromedriver.exe"

def getSize():
    # put all the sizen in ehre or write code to dynamically get all teh sizes from the website
    availableSizes = ['7', '7.5', '8', '8.5', '9', '9.5', '10', '10.5', '11']

    while True:
        try:
            userSize = input("Choose a size between 7 and 11: ")
            if userSize in availableSizes:
                break
            else: raise ValueError
        except ValueError:
            print("try again")
            continue

    size = f'UK{userSize}'

    return size

def scrapeSite(profile, link, size):
    driver = webdriver.Chrome(PATH)

    usernameOne = profile['username']
    passwordOne = profile['password']
    cvc = profile['CVC']

    driver.implicitly_wait(10)
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    base_url = 'https://launches.goodhoodstore.com/'
    checkoutlink = 'https://launches.goodhoodstore.com/checkout'

    link = link
    driver.get(base_url + link)
    # GETTING THE URL

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/article/div/div/section/div[1]/form/div/select').click()
    driver.find_element_by_xpath(f"//select[@name='id']/option[text()='UK{size}']").click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/article/div/div/section/div[1]/form/input').click()

    driver.find_element_by_xpath("//select[@name='cart_del_region_id']/option[text()='United Kingdom']").click()
    driver.execute_script("window.scrollTo(0, 500)") 
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/article/div/div/div/div[4]/div/div/p/span/a').click()
    driver.find_element_by_id('fsignin_e').send_keys(usernameOne)
    driver.find_element_by_id('fsignin_p').send_keys(passwordOne)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/article/div/div/div/div[7]/div[1]/form/p[3]/button').click()
    checkbox = driver.find_element_by_xpath('/html/body/div/div[2]/div/article/div/div/div[3]/div/div/div[1]/label').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/article/div/div/div[3]/div/div/div[3]/form/div/button[2]').click()

    threeDig = driver.find_element_by_id('cvv-input').send_keys(cvc)

def allentries(link, size):
    scrapeSite(config['profileOne'], link, size)
    scrapeSite(config['profileTwo'], link, size)

#------------------------------------------------
# MAIN
#------------------------------------------------

print(f'Running {sys.argv[0]}')
print()


def argumentError():
    print()
    print('----------------------------')
    print(f'Please give options:')
    print()
    print(f"'python {os.path.basename(__file__)} --all' for all profiles")
    print(f"'python {os.path.basename(__file__)} --one' for profile one")
    print(f"'python {os.path.basename(__file__)} --two' for profile two")
    print('----------------------------')
    print()
    print('Command should look like this:')
    print(f'python {os.path.basename(__file__)} [--all|--one|--two] [link] [size]')
    print()

# variable should be 0 for all profiles, 1 for profile one and 2 for profile 2
profileToUse = -1

if len(sys.argv) <= 1:
    argumentError()
elif sys.argv[1] == '--all':
    profileToUse = 0
elif sys.argv[1] == '--one':
    profileToUse = 1
elif sys.argv[1] == '--two':
    profileToUse = 2
else:
    print(f'{sys.argv[1]} is not a valid option')
    print()
    argumentError()

if 2 < len(sys.argv):
    link = sys.argv[2]
else: argumentError()

if 3 < len(sys.argv):
    size = sys.argv[3]
else: argumentError()


if profileToUse == 0:
    allentries(link, size)
elif profileToUse == 1:
    scrapeSite(config['profileOne'], link, size)
elif profileToUse == 2:
    scrapeSite(config['profileTwo'], link, size)