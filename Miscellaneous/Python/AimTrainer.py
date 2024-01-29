"""
Spacesity's AimTrainer v1.0.0
"""
import pygame
from pygame.locals import * 
from pygame import mixer
import sys, random, json, time

# Initialize 
pygame.init()
clock = pygame.time.Clock() # Frames per second
pygame.key.set_repeat()

# Creates Screen
screen = pygame.display.set_mode((1000, 1000)) # Screen resolution

# Target
target = pygame.image.load("target.png").convert_alpha()

# Co-ordinates
targetX = 450
targetY = 450

# Variables
count = 0
score = 0
programRun = True
randomX = random.randint(1,950)
randomY = random.randint(1,950)
(x,y) = pygame.mouse.get_pos()

# Window title and icon
pygame.display.set_caption("Spacesity's AimTrainer")
pygame.display.set_icon(target) 

# Functions

# Program Loop
while programRun:
    mousePosition = pygame.mouse.get_pos()
    screen.fill((255,255,255)) # White screen
    for event in pygame.event.get(): # Game exit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if event.type == MOUSEBUTTONDOWN:
        print(mousePosition)
        time.sleep(0.1)
        if target.collidepoint(event.pos):
            score += 1
            print(score)

    count = count + 1 # Adds a second

    screen.blit(target, (targetX, targetY)) # Displays target

    # Update display
    pygame.display.flip()
    clock.tick(60) # Frames per second
    pygame.display.update()

