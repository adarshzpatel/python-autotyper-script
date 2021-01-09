import sys
import time
import random
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

# Generates a random seed for randomizing typing speed and consistency
seedValue = random.randrange(sys.maxsize)
random.seed(seedValue)

# Opens MonkeyType in a Chromemium/Chrome window
browser = webdriver.Chrome(executable_path='chromedriver')
browser.get('https://monkeytype.com/')


def type_text():
    # Doesn't support timed mode yet (15, 30, 60, 120 seconds)
    # time delay after which script runs after starting the program.
    # This delay allows the user to switch to a typing test mode with a given number of words: 10, 25, 50, 100 words.
    time.sleep(10)
    words = browser.find_elements_by_class_name('word')

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
type_text()
