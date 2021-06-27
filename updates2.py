# !/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# *----- Fetching Updates --------#

f = open('A:/WhatsappAutomate/updates.txt', 'r')
updates = f.read()
updates = updates.split("\n\n")

# *--------------------------------

# ? ---------Navigating to Whatsapp group --------------#

browser = webdriver.Chrome('A:/WhatsappAutomate/chromedriver')
browser.get('https://web.whatsapp.com/')
time.sleep(20)
wait = WebDriverWait(browser, 600)
target = updates[1].split(':')[1]
print(target)
x_arg = '//span[contains(@title,' + target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()


# ? ---------Looping through each update after specific time time --------#
for i in range(len(updates)):
    time.sleep(180)
    specific_chat = []
    main_chat_div = browser.find_element_by_class_name('_2nmDZ')
    print(updates[i+2])
    # ------------Finding a specific message to reply ----------#
    while True:
        # your first entry in update should be your last update to which you replying
        specific_chat = main_chat_div.find_elements_by_xpath(
            "//*[contains(text(),'" + updates[i] + "')]")
        time.sleep(3)
        if specific_chat == []:
            main_chat_div.send_keys(Keys.CONTROL + Keys.HOME)
            continue
        break
    # print(specific_chat[0].text)

    print(specific_chat[0])
    time.sleep(5)
    parent_div = specific_chat[0].find_element_by_xpath(
        ".//ancestor::div[starts-with(@class,'_3zb-j')]")
    # Mouse over action for reply popup
    time.sleep(3)
    actions = ActionChains(browser)
    actions.move_to_element(parent_div).perform()
    dropdown = parent_div.find_element_by_xpath("//*[@class='_38oIx']")
    # print(dropdown)
    dropdown.click()
    time.sleep(3)
    replyBtn = browser.find_element_by_xpath("//*[@title='Reply']")
    replyBtn.click()

    # Inserting an update into input field and send
    input_box = browser.find_element_by_class_name('_1Plpp')
    input_box.send_keys(updates[i + 3] + Keys.ENTER)
