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
  
_Make sure to download a Chrome/Chromium version that is compatible with the Chromedriver, you can also replace the Chromedriver with a different version_
# How to use  
Right now this script only supports the following typing modes on MonkeyType:

* *Custom* - To let the script perform a typing test in the _custom_ mode, call the `type_text()` function at the bottom of the file and start the script. A new Chrome/Chromium window will now open. A new Chrome/Chromium window will now open. Use the starting delay to change the custom text and start the test.  
  
* *Words* - To let the script perform a typing test in the _words_ mode, call the `type_text()` function at the bottom of the file and start the script. A new Chrome/Chromium window will now open. A new Chrome/Chromium window will now open. Use the starting delay to switch to the Words mode of your desired length.  
  
* *Quote* - To let the script perform a typing test in the _quote_ mode, call the `type_text()` function at the bottom of the file method and start the script. A new Chrome/Chromium window will now open. Use the starting delay to switch to the Quote mode of your desired length.  
  
*Timed tests, 15, 30, 60 and 120 seconds, are not supported*

There are a few options the user can use to modify the execution of the script:  

* Random typing speed. To randomize typing speed, the user can call the `get_random_pause()` function can be called at the bottom of the file, before calling `type_text()`. This randomizes typing speed and allows for a varying consistency. 
* Given typing speed. To increase or decrease the time between each typed character, the `get_given_pause()` function can be called at the bottom of the file, before calling `type_text()`. The time between each character is the same when using this function. 
* Sleep time before execution. When the `type_text()` function is called, the program wil pause execution. This is done in order to allow the user to open the desired typing mode on MonkeyType.

# Demonstrations


* Custom typing test: https://www.youtube.com/watch?v=FW1lzQ1OVnk