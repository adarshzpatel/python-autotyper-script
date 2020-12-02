import pyautogui #Install pyautogui by typing " pip install pyautogui " in the command line. 
import time

#time delay after which script runs after starting the program
time.sleep(4);

text = "Place your text here" #inside double quotes

pyautogui.PAUSE = 0.01  #Pause between each key press in miliseconds, increase to get slow wpm, decrease to get high wpm

charList = [ i for i in text ]

for char in charList:
    pyautogui.typewrite(char)
                        
