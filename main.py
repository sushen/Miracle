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
import random
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
# chrome_options.add_argument("user-data-dir=chrome-data")
# chrome_options.add_argument('--profile-directory=Profile 3')
# actions = ActionChains(driver)


driver.get("https://primexbt.com")
# actions.send_keys(Keys.BACK_SPACE)
# driver.implicitly_wait(5)
#
#
# actions.send_keys(Keys.TAB * 2)
# actions.send_keys(Keys.ENTER)


# driver.quit()