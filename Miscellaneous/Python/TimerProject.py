"""
Timer v1.0.0

Created by Spacesity
"""

import time
import pygame

# Variables
ProgramRun = True
TimerStart = False
TimerPause = False
TimerReset = False 
Seconds = 0

# Main program loop
while ProgramRun == True:

    if TimerStart == True:
        Seconds = Seconds + 1
        print(Seconds)
        time.sleep(1) 

    if TimerPause == True: # Timer paused
        TimerStart = False

    if TimerReset == True: # Timer restarted
        TimerStart = False
        Seconds = 0
        TimerReset = False
         
            
                                                             

  
        
