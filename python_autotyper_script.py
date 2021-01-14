import sys
import time
import random
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from datetime import datetime, timedelta

# Generates a random seed for randomizing typing speed and consistency
seedValue = random.randrange(sys.maxsize)
random.seed(seedValue)

# Opens MonkeyType in a Chromemium/Chrome window
browser = webdriver.Chrome(executable_path='chromedriver')
browser.get('https://monkeytype.com/')


def type_text(words):
    for word in words:
        # Using selenium send_keys() to type the word if it contains single or double quotation marks.
        if "'" in word.get_attribute('textContent') or '"' in word.get_attribute('textContent'):

            # Because 'word' isn't an input element, an ActionChain is used to be able to send keys
            actions = ActionChains(browser)
            actions.send_keys(word.get_attribute('textContent') + ' ')
            actions.perform()

        # If the word doesn't contain quotation marks, the word is typed character by character.
        # This is done to be able to make use of the pause_time functions.
        else:
            for char in word.get_attribute('textContent'):
                pyautogui.typewrite(char)

            # Adds a space after every word typed
            pyautogui.typewrite(' ')


def given_word_count():
    # time delay after which script runs after starting the program.
    # This delay allows the user to switch to a typing test mode with a given number of words: 10, 25, 50, 100 words.
    time.sleep(3)
    words = browser.find_elements_by_class_name('word')

    type_text(words)


def given_duration(test_time):
    # Performs a typing test with a given duration
    # Call this function with either 15, 30, 60 or 120 seconds as value for the test_time parameter
    # time.sleep() allows the user some time to select the desired test mode on monkeytype.com
    time.sleep(5)

    # Performs the function while the current time is less than the current time + the duration of the test
    end_time = datetime.now() + timedelta(seconds=test_time)
    while datetime.now() < end_time:
        # Stores the active word to type in a list in order to be used as a parameter for type_text()
        words = []

        # Finds the current word to be typed in the typing test and sends the keypresses to monkeytype.com
        words.append(browser.find_element_by_css_selector('div.word.active'))
        type_text(words)


def get_given_pause(pause_time):
    if pause_time < 0:
        print('Pause time cannot be less than 0')
        return
    # Sets the pause between each character to a given number of N/100 seconds
    pyautogui.PAUSE = float(pause_time / 100)


# This is an example of how to call the typing functions
# Call `given_word_count()` to perform a words, custom or quote test
get_given_pause(5)
given_duration(120)
