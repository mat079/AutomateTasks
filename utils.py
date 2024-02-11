import os
import time
import undetected_chromedriver as uc

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import wait


########################
### WEB DRIVER STUFF ###
########################

#Init the webDriver
def initWebDriver(waitTime=1):
  wd = uc.Chrome(use_subprocess=True,headless=False)
  wd.maximize_window()
  # set implicit wait time
  wd.implicitly_wait(waitTime) # seconds
  return wd



######################
### MANAGE COOKIES ###
######################

def parseCookies(cookiesPath):
  cookiesDict = {}
  if cookiesPath != None:
    with open(cookiesPath) as f:
        for line in f:
          line = line.rstrip()
          cookie = line.split(',')
          cookiesDict[cookie[0]] = cookie[1]
  return cookiesDict

def useCookies(wb, cookiesPath):
  cookiesDict = parseCookies(cookiesPath)
  wb.delete_all_cookies()
  if (cookiesDict != None):
    for key, value in cookiesDict.items():
      wb.add_cookie({'name': key, 'value': value})

#Connect to a website
def connectWithCookies(webdriver,website,cookiesPath):
  #open website with coookie
  webdriver.get(website)
  #wait current cookies load to delete them
  time.sleep(15)
 # Adds the cookie into current browser context
  useCookies(webdriver, cookiesPath)
  # Opens a new tab and switches to new tab
  time.sleep(5)
  #to bypass cloudflare
  webdriver.switch_to.new_window('tab')
  webdriver.get(website)
  #webdriver.refresh()
  
#clickOnButton
def clickOnButton(webdriver, buttonClassName):
  button =  WebDriverWait(webdriver, timeout=10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, buttonClassName))
  )
  button.click()






"""
  content = webdriver.find_element(By.NAME, 'cognitoUsername')
  content.send_keys(credential[0])
  content = webdriver.find_element(By.NAME, 'password')
  content.send_keys(credential[1])
  links = webdriver.find_elements(By.TAG_NAME,"button")
  cookie = WebDriverWait(webdriver, 10).until(
    EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyButtonDecline"))
  )
  cookie.click()
  for l in links:
    if(l.text == "Connectez-vous"):
      l.click()
  el = WebDriverWait(webdriver, timeout=30).until(lambda d: d.find_element(By.ID,"app"))
"""
