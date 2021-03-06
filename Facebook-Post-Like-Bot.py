import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pathlib
import pyperclip as pc

# Time Counting
StartTime = time.time()
print("This Script Start " + time.ctime())

# Setting the chrome_options
global chrome_options
chrome_options = Options()
scriptDirectory = pathlib.Path().absolute()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument('--profile-directory=Profile 8')
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("user-data-dir=chrome-data")
chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")

# Setting the driver
global driver
driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
driver.get("https://facebook.com")


def login():
    try:
        # I use environment veriable  base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
        username = os.environ.get('facebook_zrliqi_email')
        password = os.environ.get('facebook_zrliqi_pass')

        driver.find_element_by_id("email").send_keys(username)
        driver.find_element_by_id("pass").send_keys(password)
        driver.find_element_by_name("login").click()
        print(input("Press any Key: "))
        print("Login work Successfully ")

    except:
        pass


groupPostList = [
    "https://www.facebook.com/groups/118355661537061/permalink/4158266657545921/",
    "https://www.facebook.com/groups/402353916617590/permalink/1644448839074752/",
    "https://www.facebook.com/groups/mathfordatascience/permalink/1461052630895489/",
    "https://www.facebook.com/groups/135196957162117/permalink/791655444849595/",
    "https://www.facebook.com/groups/youngcodersLP/permalink/1498237833901959/",
    "https://www.facebook.com/groups/366190054572553/permalink/508867153638175/",
    "https://www.facebook.com/groups/632595694006151/permalink/858058588126526",
    "https://www.facebook.com/groups/youngcodersLP/permalink/1498237833901959/",
    "https://www.facebook.com/groups/machine.learning.bangladesh/permalink/1150708802101898/",
    "https://www.facebook.com/groups/pythonsnake/permalink/5829285400422492/",
    "https://www.facebook.com/groups/programmingbasicsconcepts/permalink/1168579300275791/",
    "https://www.facebook.com/groups/pythonsnake/permalink/5829991850351847/",
    "https://www.facebook.com/groups/10ms.programming/permalink/2178588115617675",
    "https://www.facebook.com/groups/2092683587684490/permalink/3073151069637732/",
    "https://www.facebook.com/groups/729769827368286/permalink/1462033394141922/"
]


def navigateCommentWhenNavigateCommentNotFound():
    driver.implicitly_wait(20)
    time.sleep(2)
    # Navigate Comment Aria
    navigateCommentWhenNavigateCommentNotFoundBtnXpath = "//div[@aria-label='Actions for this post']"
    navigateCommentWhenNavigateCommentNotFoundBtnXpathAria = driver.find_elements_by_xpath(
        navigateCommentWhenNavigateCommentNotFoundBtnXpath)
    if driver.find_elements_by_xpath(navigateCommentWhenNavigateCommentNotFoundBtnXpath):
        navigateCommentWhenNavigateCommentNotFoundBtnXpathAria[0].click()
        navigateCommentWhenNavigateCommentNotFoundBtnXpathAria[0].click()
        print(navigateCommentWhenNavigateCommentNotFoundBtnXpathAria[0])

        navigateCommentWhenNavigateCommentNotFoundActions = ActionChains(driver)
        total_tab = 3
        for i in range(total_tab):
            navigateCommentWhenNavigateCommentNotFoundActions.send_keys(Keys.TAB)
            print(
                str(i + 1) + " tabs Working for navigateCommentWhenNavigateCommentNotFoundActions Like btn navigation")
        navigateCommentWhenNavigateCommentNotFoundActions.send_keys(Keys.ENTER)
        navigateCommentWhenNavigateCommentNotFoundActions.perform()
    else:
        print("Path Not Found ")
        print(input("You Path is not found it will create wrong Navigation fixed it: "))


def switchBrowserTab():
    window_before = driver.window_handles[0]
    print("Group Window :" + window_before)

    window_after = driver.window_handles[1]
    print("Single Group Link Window :" + window_after)

    driver.switch_to.window(window_after)
    pc.copy(driver.current_url)
    groupUrl = pc.paste()
    print(driver.title)
    print(groupUrl)


    # Write Url in a file
    # groupUrlForList = str(i) + ". " + groupUrl + "\n"
    groupUrlForList = groupUrl + "\n"

    line_index = 3
    lines = None
    with open('fb_profile_list_file.txt', 'r') as file_handler:
        lines = file_handler.readlines()

    lines.insert(line_index, groupUrlForList)

    with open('fb_profile_list_file.txt', 'w') as file_handler:
        file_handler.writelines(lines)

    time.sleep(5)
    driver.close()
    driver.switch_to.window(window_before)

def save_profile_link():
    save_profile_link_actions = ActionChains(driver)
    save_profile_link_actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL)
    save_profile_link_actions.perform()


def go_profile_name():
    go_profile_name_actions = ActionChains(driver)
    go_profile_name_actions.key_down(Keys.SHIFT).send_keys(Keys.TAB * 3).key_up(Keys.SHIFT)
    go_profile_name_actions.perform()


def navigateLike():
    driver.implicitly_wait(20)
    time.sleep(2)
    # Navigate Profile Massage Aria
    likeBtnXpath = "//span [normalize-space()='Like']"
    # print(likeBtnXpath)
    likeBtnXpathAria = driver.find_elements_by_xpath(likeBtnXpath)
    print(likeBtnXpathAria)

    likeBtnList = []
    try:
        for likeBtn in likeBtnXpathAria:
            likeBtnList.append(likeBtn)
            print(str(len(likeBtnList)) + " Like Btn")
            likeBtnXpathAria[(len(likeBtnList)) * 2].click()
            print(likeBtnXpathAria[(len(likeBtnList)) * 2])
            time.sleep(3)
            go_profile_name()
            save_profile_link()
            # print(input("Press any Key: "))
            switchBrowserTab()
            # print(input("Press any Key: "))

    except:
        pass

    print("Like Function Working")


driver.implicitly_wait(20)
time.sleep(5)

for groupPost in groupPostList:
    driver.get(groupPost)
    print(driver.title)
    print(groupPost + " link")
    time.sleep(2)

    navigateLike()

    time.sleep(2)
    # print(input("Press any Key: "))

# Time Counting
EndTime = time.time()
print("\nThis Script End " + time.ctime())
totalRunningTime = EndTime - StartTime
print("This Script is running for " + str(int(totalRunningTime)) + " Second. or\n")
print("This Script is running for " + str(int(totalRunningTime / 60)) + " Minutes.")
