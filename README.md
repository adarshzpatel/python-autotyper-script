# Python-autotyper-script
Python Script to simulate keyboard key presses using pyautogui.  
This script is designed for use on the website monkeytype.com

Requirements:

* Python  
* Pyautogui module  
* Selenium  
* Chromium

# Installing pyautogui
1. Open your cmd/terminal
2. Type `pip install pyautogui` and it will install the module for you.

# Installing selenium
1. Open your cmd/terminal
2. Type `pip install selenium` and it will install the module for you.

# Installing Chromium

* On Arch based distributions use `sudo pacman -S chromium`  
* On Ubuntu based distrubutions use `sudo apt-get install chromium-browser`  
* On other operating systems, go to: https://www.chromium.org/getting-involved/download-chromium

# How to use  
Right now this script only supports the following typing modes on MonkeyType:

*Custom* - To let the script type a custom text, enter the text you want to type into the MonkeyType interface. Then also enter it into the `text` variable in the script. Finally call the `type_given_text()` method with the `text` variable inside the parentheses. After starting the script, switch to the browser in which the typing test is opened. 
  
*Words* - To let the script perform a typing test in the _words_ mode, simply call the `type_random_text()` and start the script. A new Chrome/Chromium window will now open. In the window you can start a typing test with either 10, 25, 50 or 100 words.  
  
*Quote* - Typing quotes are partially supported right now. The script is not yet able to type some characters such as quotations marks. Aside from these symbols the script will perform well.  
  

There are a few options the user can use to modify the execution of the script:  

* Random typing speed. To randomize typing speed, the user can call the `get_random_pause()` method to randomize the pausing time between each character. This allows for a varying speed and consistency. 
* Given typing speed. To increase or decrease the time between each typed character, the `get_given_pause()` method can be called. The time between each character is the same when using this method. 
* Sleep time before execution. When one of the typing methods is called, the program wil pause execution. This is done in order to allow the user to open the desired typing mode on MonkeyType.


