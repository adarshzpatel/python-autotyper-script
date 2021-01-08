# Install pyautogui by typing " pip install pyautogui " in the command line.
import pyautogui
import time
import random
from datetime import datetime
import requests
from selenium import webdriver

browser = webdriver.Chrome(executable_path='chromedriver')
browser.get('https://monkeytype.com/')

# Uses the current time as a seed for randomised typing speed
# This method is outdated as of Python 3.9
random.seed(datetime.now())

# time delay after which script runs after starting the program
# This is used to allow the user some time to switch to the typing test window
time.sleep(5)

text = ""  # Enter the text to type inside the double quotes, this is used in the custom text mode on MonkeyType


def type_randomised_text():
    # Finds all words on current typing test, by going through the source of the page
    words = browser.find_elements_by_class_name('word')

    for i in range(len(words)):
        # Calls the type_word() for every word in the typing test
        type_single_word(i)


def type_single_word(i):
    word = browser.find_element_by_xpath(
        '// *[@id="words"]/div[{}]'.format(i+1))
    for char in word.text:
        # Use either get_random_pause() or get_given_pause() to set the time paused between typing each character.
        # Using higher values for these functions decreases the typing speed and using lower values increases the typing speed.
        # get_random_pause()
        # get_given_pause()
        pyautogui.typewrite(char)
    pyautogui.typewrite(' ')


def get_random_pause(lower_bound, upper_bound):
    # Sets the pause between each character to a random float between two bounds of 0.0N seconds
    # This makes the typing consistency more believable.
    pyautogui.PAUSE = float(random.randint(lower_bound, upper_bound) / 100)


def get_given_pause(pause_time):
    # Sets the pause between each character to a given number of 0.0N seconds
    pyautogui.PAUSE = float(pause_time / 100)
