# This file is used to test/experiment with new functionality and potential bug fixes before implementing them in the main file
from selenium import webdriver
import time

# Opens MonkeyType in a Chromemium/Chrome window
browser = webdriver.Chrome(executable_path='chromedriver')
browser.get('https://monkeytype.com/')


def find_words():
    words = browser.find_elements_by_class_name('word')

    word_list = []

    for word in words:
        word_list.append(word.get_attribute('textContent'))

    return word_list


time.sleep(10)

find_words()
