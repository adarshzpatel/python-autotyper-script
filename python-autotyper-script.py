import pyautogui
import time
import random
from datetime import datetime
from selenium import webdriver


# Uses the current time as a seed for randomised typing speed
# This method is outdated as of Python 3.9, so I have to find a different solution for seeding.
random.seed(datetime.now())

# Opens MonkeyType in a Chromemium/Chrome window
browser = webdriver.Chrome(executable_path='chromedriver')
browser.get('https://monkeytype.com/')

# Enter the text to type inside the double quotes, this is used in the custom text mode on MonkeyType
text = ""


def type_random_text():
    # Doesn't support timed mode yet (15, 30, 60, 120 seconds)
    # time delay after which script runs after starting the program.
    # This delay allows the user to switch to a typing test mode with a given number of words: 10, 25, 50, 100 words.
    time.sleep(10)
    words = browser.find_elements_by_class_name('word')

    for word in words:
        for char in word.get_attribute('textContent'):
            pyautogui.typewrite(char)
        # Adds a space after every word typed
        pyautogui.typewrite(' ')


def type_given_text(text_to_type):
    # time delay after which script runs after starting the program
    # This is used to allow the user some time to switch to the typing test running in the browser
    time.sleep(10)
    char_list = [i for i in text_to_type]

    for char in char_list:
        # Uncomment line below and insert parameters for randomised typing speed.
        # get_random_pause()
        pyautogui.typewrite(char)


def get_random_pause(lower_bound, upper_bound):
    if lower_bound > upper_bound:
        print('Lower bound cannot be greater than upper bound')
        return
    # Sets the pause between each character to a random float between two bounds of N/100 seconds
    # This makes the typing consistency more believable.
    pyautogui.PAUSE = float(random.randint(lower_bound, upper_bound) / 100)


def get_given_pause(pause_time):
    if pause_time < 0:
        print('Pause time cannot be less than 0')
        return
    # Sets the pause between each character to a given number of N/100 seconds
    pyautogui.PAUSE = float(pause_time / 100)


get_given_pause(3)
type_random_text()
