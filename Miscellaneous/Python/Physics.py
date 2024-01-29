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
player = pygame.image.load("BlackPlayer.png").convert_alpha()

# Co-ordinates
playerX = 225
playerY = 225
targetY = playerY

# Variables
count = 0
refresh = 10

# Window title and icon
pygame.display.set_caption("Jumper Test")
pygame.display.set_icon(player) 

# Functions
def game_exit(): # Exits program
    pygame.quit()
    sys.exit()

# Program Loop
programRun = True
gameStart = True
jump = False

while programRun:
    screen.fill((255,255,255)) # White screen
    for event in pygame.event.get():
        # Game exit
        if event.type == pygame.QUIT:
            game_exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True
                targetY = playerY - 100

    if playerY >= 500 or playerY <= 0: # Out of bounds
        game_exit()
            
    if playerY == targetY: 
       jump = False

    if playerY != targetY and jump == True:
        playerY -= 10
       
    if jump == False:
        playerY += 5

    count = count + 1 # Adds a second
    screen.blit(player, (playerX, playerY)) # Displays player

    # Update display
    pygame.display.flip()
    clock.tick(60) # Frames per second
    pygame.display.update()
