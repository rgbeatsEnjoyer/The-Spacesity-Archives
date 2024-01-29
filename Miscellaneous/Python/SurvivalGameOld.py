"""
Survival game v1.0.0

Programmer: Spacesity
Graphics Designer: Ninja Noodles
Music/SFX Producer: Sync
"""

import pygame
from pygame.locals import * 
from pygame import mixer
"""from SurvivalPlayer import Player"""
import sys, random, json, time 
pygame.init() 
clock = pygame.time.Clock() # Frames per second
pygame.key.set_repeat(5) # Repeat key actions every 5ms

# Creates screen
screen = pygame.display.set_mode((600, 750)) # Screen dimensions

# Player
playerX = 275
playerY = 600
playerSize = 75

# Bullet
spray = random.randint(47,55)
bulletXtarget = playerX + spray
fireRate = 0 # Frames (60 = 1 second interval)

# Graphics
playerIdle = pygame.image.load("playeridle.png").convert_alpha()
playerFire = pygame.image.load("playerfire.png").convert_alpha()
bullet = pygame.image.load("raycast.png").convert_alpha()
playButton = pygame.image.load("buttonplaceholder.png").convert_alpha()
resumeButton = pygame.image.load("buttonplaceholder.png").convert_alpha()
restartButton = pygame.image.load("buttonplaceholder.png").convert_alpha()
menuButton = pygame.image.load("buttonplaceholder.png").convert_alpha()
creditButton = pygame.image.load("buttonplaceholder.png").convert_alpha()

# Variables
fire = False
programRun = True
mainMenu = True
gameStart = False
pauseMenu = False
deathMenu = False
creditsMenu = False
count = 0

# Window title and icon
pygame.display.set_caption("Survival Game")
pygame.display.set_icon(playerFire) 

# Functions
def screenControl():
    pygame.display.flip()
    clock.tick(60) 
    pygame.display.update()

def movement():
    global playerX
    global playerY
    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
        playerX -= 1
    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        playerX += 1 

def shooting():
    global spray
    global fire
    if fire == True:
        bulletXtarget = playerX + spray
        screen.blit(bullet,(bulletXtarget,0))
        spray = random.randint(47,55)
        time.sleep(0)

def pause():
    global pauseMenu
    global gameStart
    if gameStart == True:
        gameStart = False
        pauseMenu = True
    else:
        pauseMenu = False
        gameStart = True

def rate():
    global fireRate
    if fireRate > 0:
        fireRate -= 1

# Game loop
while programRun == True:
    screen.fill((255,255,255))
    # Main Menu/Credits
    if mainMenu == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.exit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_c:
                    mainMenu = False
                    creditsMenu = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mainMenu = False
                gameStart = True

        count = count + 1 # Accumulate frames

        # GUI screening

        screenControl()

    # Credits Menu
    elif creditsMenu == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_c:
                    creditsMenu = False
                    mainMenu = True

        count = count + 1 # Accumulate frames

        # GUI screening
        screen.blit(creditButton, (150,150))

        screenControl()

    # Game Start/Pause
    elif gameStart == True:
        screen.fill((255,255,255)) # White screen
        for event in pygame.event.get(): # All events
            if event.type == pygame.QUIT: # Game exit
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if fireRate == 0:
                        fire = True
                        shooting()
                        screen.blit(playerFire, (playerX, playerY))
                        fireRate += 5
                movement()
            if event.type == pygame.KEYUP:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                pause()   

        
        count = count + 1 # Accumulate frames
        rate()

        # GUI screening
        screen.blit(playerIdle, (playerX, playerY)) # Displays player

        screenControl()

    # Pause Menu
    elif pauseMenu == True:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pause()
                
        count = count + 1 # Accumulate frames

        # GUI screening

        screenControl()          

"""
Development Notes:
- Implement object oriented programming
"""
