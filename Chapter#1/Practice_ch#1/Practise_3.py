# Practise 3:
# Install an external module and use it ot perform an operation of your insterest.


# External module:
# External module is a module that are built by someone else and  not installed in our program.
# Firstly, installed the external module in our program.




# pyttx3    is used for text to speech.

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello Maachhee! How are you? Toosi sari kurian barian hee batmeez ho")
engine.runAndWait()

# pywhatkit  is used for searching on google.

import pywhatkit
pywhatkit.search("pywhatkit")


# wikipedia  is used for searching on wikipedia

import wikipedia
wikipedia.summary("wikipedia")

# pyautogui  is used for taking screenshot

import pyautogui
pyautogui.screenshot()

# a  is used for taking audio input from user
# syntax of a is a.record()

import a
a.record()


# pyjokes  is used for generating jokes

import pyjokes
joke = pyjokes.get_joke()
print(joke)


