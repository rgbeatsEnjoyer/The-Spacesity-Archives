import pygame
from pygame.locals import *
from pygame import mixer
import sys, random, json, time

# Initialize 
pygame.init()
clock = pygame.time.Clock() # Frames per second
pygame.key.set_repeat()
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

# Creates Screen
screen = pygame.display.set_mode((750, 750))

# Player and Projectiles
projectile = pygame.image.load("SimpleProjectile.png").convert_alpha()
player = pygame.image.load("SimpleCharacter.png").convert_alpha()

# Co-ordinates
projX = 350
projY = 350
mousePosition = pygame.mouse.get_pos()
target = [projX,projY]

# Variables
count = 0

# Title / Icon
pygame.display.set_caption("Test Project")
pygame.display.set_icon(player)

# Functions

# Program Loop
programRun = True
gameStart = False

while programRun:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()
            target = mousePosition
            print(target)

    if projX != target[0] and projY != target[1]:
        if target[0] > projX:
            projX += 1
        if target[0] < projX:
            projX -= 1
        if target[1] > projY:
            projY += 1
        if target[1] < projY:
            projY -= 1

    if projX != target[0] and projY == target[1] or projX == target[0] and projY != target[1]:
        if target[0] > projX:
            projX += 1
        if target[0] < projX:
            projX -= 1
        if target[1] > projY:
            projY += 1
        if target[1] < projY:
            projY -= 1

        screen.blit(projectile, (projX, projY))
        screen.blit(player, (325, 325))
        
        
        
    count = count + 1

    screen.blit(projectile, (projX, projY))
    screen.blit(player, (325, 325))
   

    # Update display
    pygame.display.flip()
    clock.tick(120) # Fps
    pygame.display.update()








