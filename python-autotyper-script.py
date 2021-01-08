# Install pyautogui by typing " pip install pyautogui " in the command line.
import pyautogui
import time
import random
from datetime import datetime
random.seed(datetime.now())

# time delay after which script runs after starting the program
time.sleep(5)

text = ""  # Enter the text to type inside the double quotes


def get_random_pause(lower_bound, upper_bound):
    # Sets the pause between each character to a random float between two bounds of 0.0N seconds
    # This makes the typing consistency more believable.
    pyautogui.PAUSE = float(random.randint(lower_bound, upper_bound) / 100)


def get_given_pause(pause_time):
    # Sets the pause between each character to a given number of 0.0N seconds
    pyautogui.PAUSE = float(pause_time / 100)


def type_text(text_to_type):

    char_list = [i for i in text_to_type]

    for char in char_list:
        # Use either get_random_pause() or get_given_pause() to set the time paused between typing each character.
        # Using higher values for these functions decreases the typing speed and using lower values increases the typing speed.
        # get_random_pause()
        # get_given_pause()
        pyautogui.typewrite(char)
