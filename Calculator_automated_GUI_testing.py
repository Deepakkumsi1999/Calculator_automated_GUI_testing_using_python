# This Python program uses the pyautogui library to automate interactions with the Calculator application.
# This script essentially automates the process of entering numbers and functions
# in the Calculator application,showcasing the capabilities of the pyautogui library for GUI automation.

# Note: This script is works on screen Size(width=1920, height=1080) HP Windows 11 OS.


# importing the necessary modules, "pyautogui" for automating mouse and keyboard actions
import pyautogui

# importing the necessary modules, "time" for adding delays.
import time

# returns a size object with width and height of the screen
print(pyautogui.size())

# move to search window
pyautogui.moveTo(700, 1060, duration=1)
# pyautogui.press("Ctrl + Esc")

# simulates a click at the present mouse position start menu
pyautogui.click(button="left")
time.sleep(1)
# types the string passed inside the  function
pyautogui.typewrite("Calculator")

# The program uses duration=1 in pyautogui.moveTo to specify the time taken for the mouse cursor
# to move to the specified position.This adds a one-second delay for each movement,
# making the automation more controlled.
time.sleep(1)

# simulates pressing the enter key
pyautogui.press("enter")
# time.sleep(1)

# simulates pressing the hotkey Windows key + Up arrow to maximize the window
pyautogui.press("Windows key + Up arrow")

# moves to number "1" position in calculator in 1 sec
pyautogui.moveTo(x=206, y=862, duration=1)
pyautogui.click()
# moves to number "2" position in calculator in 1 sec
pyautogui.moveTo(x=580, y=861, duration=1)
pyautogui.click()
# moves to number "3" position in calculator in 1 sec
pyautogui.moveTo(x=1007, y=861, duration=1)
pyautogui.click()
# moves to number "4" position in calculator in 1 sec
pyautogui.moveTo(x=206, y=749, duration=1)
pyautogui.click()
# moves to number "5" position in calculator in 1 sec
pyautogui.moveTo(x=580, y=749, duration=1)
pyautogui.click()
# moves to number "6" position in calculator in 1 sec
pyautogui.moveTo(x=1007, y=749, duration=1)
pyautogui.click()
# moves to number "6" position in calculator in 1 sec
pyautogui.moveTo(x=206, y=635, duration=1)
pyautogui.click()
# moves to number "7" position in calculator in 1 sec
pyautogui.moveTo(x=580, y=635, duration=1)
pyautogui.click()
# moves to number "8" position in calculator in 1 sec
pyautogui.moveTo(x=1007, y=635, duration=1)
pyautogui.click()
# moves to number "9" position in calculator in 1 sec
pyautogui.moveTo(x=602, y=975, duration=1)
pyautogui.click()
# moves to number "0" position in calculator in 1 sec
pyautogui.moveTo(x=201, y=971, duration=1)
pyautogui.click()
# moves to function "+/-" position in calculator in 1 sec
pyautogui.moveTo(x=990, y=979, duration=1)
pyautogui.click()
# moves to function "=" position in calculator in 1 sec
pyautogui.moveTo(x=1393, y=976, duration=1)
pyautogui.click()
# moves to function "+" position in calculator in 1 sec
pyautogui.moveTo(x=1402, y=854, duration=1)
pyautogui.click()
# moves to function "-" position in calculator in 1 sec
pyautogui.moveTo(x=1402, y=732, duration=1)
pyautogui.click()
# moves to function "*" position in calculator in 1 sec
pyautogui.moveTo(x=1402, y=638, duration=1)
pyautogui.click()
# moves to function "*" position in calculator in 1 sec
pyautogui.moveTo(x=1402, y=523, duration=1)
pyautogui.click()
# moves to function "clear screen" position in calculator in 1 sec
pyautogui.moveTo(x=1402, y=411, duration=1)
pyautogui.click()
# moves to function "clear screen" position in calculator in 1 sec
pyautogui.moveTo(x=1014, y=525, duration=1)
pyautogui.click()
# moves to function "clear screen" position in calculator in 1 sec
pyautogui.moveTo(x=1005, y=412, duration=1)
pyautogui.click()
# moves to function "sqr(0)" position in calculator in 1 sec
pyautogui.moveTo(x=596, y=520, duration=1)
pyautogui.click()
# moves to function "clear screen" position in calculator in 1 sec
pyautogui.moveTo(x=601, y=412, duration=1)
pyautogui.click()
# moves to function "%" position in calculator in 1 sec
pyautogui.moveTo(x=206, y=412, duration=1)
pyautogui.click()
# moves to function "1/x" position in calculator in 1 sec
pyautogui.moveTo(x=202, y=526, duration=1)
pyautogui.click()
# moves to function "clear screen" position in calculator in 1 sec
pyautogui.moveTo(x=601, y=412, duration=1)
pyautogui.click()

# script to check functionality of the calculator
# click number "5"
pyautogui.press("5", 1)
time.sleep(1)
# function "+"
pyautogui.press("+", 1)
time.sleep(1)
# adding number "7"
pyautogui.press("7", 1)
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
# moves to function "clear screen" position in calculator in 1 sec
pyautogui.moveTo(x=601, y=412, duration=1)

# moves to position Closing the Calculator window
pyautogui.moveTo(x=1900, y=10, duration=1)
pyautogui.click()
