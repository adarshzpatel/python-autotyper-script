# This file is used to test/experiment with new functionality and potential bug fixes before implementing them in the main file
import sys
import time
import random
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


# Opens MonkeyType in a Chromemium/Chrome window
browser = webdriver.Chrome(executable_path='chromedriver')
browser.get('https://monkeytype.com/')


def find_words():
    words = browser.find_elements_by_class_name('word')

    for word in words:
        actions = ActionChains(browser)
        actions.send_keys(word.get_attribute('textContent') + ' ')
        actions.perform()


time.sleep(10)
find_words()
