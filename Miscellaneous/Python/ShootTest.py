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

# Player + Projectile
player = pygame.image.load("BlackPlayer.png").convert_alpha()
bullet = pygame.image.load("SimpleProjectile.png")

# Co-ordinates
playerX = 225
playerY = 425
bulletX = -25
bulletY = -25
target = 0

# Variables
count = 0
shot = False

# Window title and icon
pygame.display.set_caption("Test")
pygame.display.set_icon(player) 

# Functions

# Program Loop
programRun = True
gameStart = False
bullets = []

while programRun:
    screen.fill((255,255,255)) # White screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and shot == False: # Refresh time 
                shot = True
                bulletY = playerY + 10
                bulletX = playerX + 10
                target = bulletY - 750
                bulletY -= 5

        if event.type == pygame.KEYDOWN: # Left
            if event.key == pygame.K_a:
                playerX -= 50

            if event.key == pygame.K_d: # Right
                playerX += 50

    if bulletY != target:
        bulletY -= 5

    if bulletY == target:
        shot = False
        
    count = count + 1 # Adds a second
    screen.blit(bullet, (bulletX, bulletY)) # Displays bullet
    screen.blit(player, (playerX, playerY)) # Displays player

    # Update display
    pygame.display.flip()
    clock.tick(60) # Frames per second
    pygame.display.update()
    
