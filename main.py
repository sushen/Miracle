#   Copyright (c) 2021.
#   Version : 0.0.1
#   Script Author : Sushen Biswas
#
#   Sushen Biswas Github Link : https://github.com/sushen
#
#   !/usr/bin/env python
#   coding: utf-8


from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random


chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--incognito")

driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")


# actions = ActionChains(driver)


driver.get("https://primexbt.com")
# actions.send_keys(Keys.BACK_SPACE)
# driver.implicitly_wait(5)
#
#
# actions.send_keys(Keys.TAB * 2)
# actions.send_keys(Keys.ENTER)


# driver.quit()