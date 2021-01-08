# This file is used to test/experiment with new functionality and potential bug fixes before implementing them in the main file
from selenium import webdriver

# Opens MonkeyType in a Chromemium/Chrome window
browser = webdriver.Chrome(executable_path='chromedriver')
browser.get('https://monkeytype.com/')


def find_words():
    # This function is used to find a fix for Selenium not being able to retrieve all words in the HTML source
    words = browser.find_elements_by_class_name('word')

    word_list = []

    for word in words:
        if len(word.text) < 1:
            break
        else:
            word_list.append(word.text)

    print(word_list)
