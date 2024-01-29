"""
Snowball Minigames (CONCEPT)

Programmed by Spacesity

Graphics created by AlphaV53
"""

import pygame
import random
import time

# Variables
Username = ''
UsernameChosen = False
GamePasscode = '123456'
Access = False

# Username Select
while UsernameChosen == False:
    NameSelector = input("Enter a username:")
    Comfirm = input("You wish to be called this? (Y/N):")
    if Comfirm == 'Y' or Comfirm == 'y':
        Username = NameSelector
        print("Welcome,",NameSelector)
        UsernameChosen = True
        break
    else:
        pass

# Game Passcode
while Access == False:
    InputCode = input("Please enter a Game Code:")
    
    if InputCode == GamePasscode:
        print("VALID CODE. PLEASE WAIT...")
        Access = True
        break
    else:
        print("INVALID GAME CODE")
        
        
