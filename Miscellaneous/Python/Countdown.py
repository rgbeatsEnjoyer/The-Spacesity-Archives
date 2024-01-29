"""
Countdown Project
"""

# Modules
import PySimpleGUI as sg
import os.path
import time

# Variables
count = 0

# Structure and Layout
layout = [[sg.Text('Countdown v1.0')]]

window = sg.Window('Countdown Project')

# Program Loop
while True:
    events, values = window.read()
    # Program Exit
    if event == sg.WIN_CLOSED:
        break

window.close()
