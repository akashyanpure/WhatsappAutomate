# !/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


browser = webdriver.Chrome('A:/WhatsappAutomate/chromedriver')
browser.get('http://localhost/FinIQ_CADB_V2.1/')
wait = WebDriverWait(browser, 600)
time.sleep(3)
User = browser.find_element_by_id('btnContinue')
User.click()
time.sleep(35)
PriceAll = browser.find_element_by_id('btnBack1')
PriceAll.click()
