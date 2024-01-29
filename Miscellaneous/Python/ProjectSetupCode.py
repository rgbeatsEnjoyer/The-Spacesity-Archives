"""
Pygame Project Set-up

Used for setting up a new project using Pygame
"""

import pygame
from pygame.locals import * 
from pygame import mixer # Music and Sound
import sys, random, json, time # Additional modules

# Initialize 
pygame.init()
clock = pygame.time.Clock() # Frames per second
pygame.key.set_repeat()
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP]) # Prioritize events

# Creates Screen
screen = pygame.display.set_mode((500, 500)) # Screen resolution

# Player(s)
player = pygame.image.load("...").convert_alpha()

# Co-ordinates
playerX = 300
playerY = 300

# Variables
count = 0

# Window title and icon
pygame.display.set_caption("...")
pygame.display.set_icon(player) 

# Functions

# Program Loop
programRun = True
gameStart = False

while programRun:
    screen.fill((255,255,255)) # White screen
    for event in pygame.event.get():
        # Game exit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    count = count + 1 # Adds a second

    screen.blit(player, (playerX, playerY)) # Displays player

    # Update display
    pygame.display.flip()
    clock.tick(60) # Frames per second
    pygame.display.update()
