#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:19:05 2026

@author: paratusalcantara
"""

"""
This Python script runs in Spyder via Anaconda as a Chrome-Mac-based YouTube Sleep Timer.

Requirements & Usage:
1. Open your YouTube video in Chrome on macOS and keep it as the active tab.
2. Pause the video, switch to Spyder, and press F5 to execute.
3. The script will automatically switch to Chrome, "Play" (resume), and enter "Full screen" mode.
4. A min:sec countdown will overlay at the top-right of your screen (outside full-screen) 
   to remind you the script is active.
5. Once the timer expires, the overlay disappears, the YouTube video pauses, and "Exit full screen".
6. The script will bring you back to Spyder and end, allowing you to press F5 to run it again.
"""

import pyautogui
import time
import os
import subprocess
import sys
# import tkinter as tk


minute = 25
second = 0
CD = minute * 60 + second


os.system('osascript -e \'tell application "Google Chrome" to activate\'')
time.sleep(0.1)
pyautogui.press('space')
time.sleep(0.1)
pyautogui.hotkey('F') # 'f' will go to chrome. 'F' before 'space' will go to chrome.

""""""
# sleepGUI(CD)
# import subprocess
# import time
# import sys
# CD = 300

timer_code = f'''
import tkinter as tk

CD = {CD}

root = tk.Tk()
root.title("Time")

root.geometry(
    f"150x60+{{root.winfo_screenwidth()-140}}+0"
)

root.attributes("-topmost", True)

label = tk.Label(
    root,
    font=("Arial", 16)
)

label.pack(
    padx=20,
    pady=20
)


def update_timer(t):
    if t > 0:
        minute = t // 60
        second = t % 60

        label.config(
            text=f"Sleep in {{minute}}:{{second:02d}}"
        )

        root.after(
            1000,
            update_timer,
            t - 1
        )


update_timer(CD)

root.mainloop()
'''

process = subprocess.Popen(
    [sys.executable, "-c", timer_code]
)

# Main sleeper
time.sleep(CD)

# Kill the separate timer process
process.terminate()
process.wait()
""""""
# time.sleep(CD) # The sleepGUI has a time.sleep(CD) inside, we should make one and only one active.

# pyautogui.hotkey('command', 'tab')
os.system('osascript -e \'tell application "Google Chrome" to activate\'')
# print("\a")
pyautogui.press('space')
time.sleep(0.1)
pyautogui.hotkey('F')
os.system('osascript -e \'tell application "Python" to activate\'')
