"""
Circuit Fence: Game v1.0

Programmer: Spacesity
Graphics Designer: Ninja Noodles
Music/SFX Producer: Sync
"""

import sys, random, json, time
import pygame
from pygame.locals import *
from pygame import mixer
from CircuitFencePlayer import Player

# Initialize
pygame.init()
clock = pygame.time.Clock()
pygame.key.set_repeat(5)

# Creates screen
screen_width, screen_height = 600,750
screen = pygame.display.set_mode((screen_width, screen_height)) # Screen dimensions

# Graphics
playButton = pygame.image.load("buttonplaceholder.png").convert_alpha()
resumeButton = pygame.image.load("buttonplaceholder.png").convert_alpha()
restartButton = pygame.image.load("buttonplaceholder.png").convert_alpha()
pauseButton = pygame.image.load("smallbuttonplaceholder.png").convert_alpha()
menuButton = pygame.image.load("smallbuttonplaceholder.png").convert_alpha()
creditButton = pygame.image.load("buttonplaceholder.png").convert_alpha()
playerIdle = pygame.image.load("playeridle.png").convert_alpha()
playerFire = pygame.image.load("playerfire.png").convert_alpha()
levelButton1 = pygame.image.load("levelButton_Hacked.png").convert_alpha()
levelButton2 = pygame.image.load("buttonplaceholder.png").convert_alpha()
levelButton3 = pygame.image.load("buttonplaceholder.png").convert_alpha()
levelButtonL = pygame.image.load("levelButton_Locked.png").convert_alpha()

# User Interface
class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        action = False
        mouse_position = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
    
        screen.blit(self.image,(self.rect.x, self.rect.y))

        return action

# Graphical Interface
play_button = Button(150,150,playButton)
credit_button = Button(150,350,creditButton)
menu_button = Button(150,150,menuButton)
resume_button = Button(150,150,resumeButton)
pause_button = Button(10,10,pauseButton)
level_button1 = Button(150,100,levelButton1)
level_button2 = Button(150,300,levelButtonL)
level_button3 = Button(150,500,levelButtonL)

# Window title and icon
pygame.display.set_caption("Circuit Fence")
pygame.display.set_icon(playerFire)

# Player
P1 = Player(275,600,playerIdle,playerFire)
fireRate = 0 # Frames (60 = 1 second interval)

# Variables
programRun = True
mainMenu = True
level_1 = False
pauseMenu = False
deathMenu = False
creditsMenu = False
levelSelector = False
count = 0

# Functions
def screenControl():
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

def rate_control():
    global fireRate
    if fireRate > 0:
        fireRate -= 1

# Game loop
while programRun:
    screen.fill((255,255,255))

    # Main Menu
    if mainMenu:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYUP:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass

        # Interface Actions
        if play_button.draw():
            mainMenu = False
            time.sleep(0.1)
            levelSelector = True
            count = 0
        if credit_button.draw():
            mainMenu = False
            time.sleep(0.1)
            creditsMenu = True

        # Accumulate frames
        count += 1

        # GUI screening
        play_button = Button(150,150,playButton)
        credit_button = Button(150,350,creditButton)
        
    # Credits Menu
    elif creditsMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Interface Actions
        if menu_button.draw():
            creditsMenu = False
            time.sleep(0.1)
            mainMenu = True

        # Accumulate frames
        count += 1

        # GUI screening
        menu_button = Button(10,10,menuButton)
        
    # Game Start
    elif level_1:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if fireRate <= 0:
                        P1.shoot()
                        pygame.draw.line(screen, (0,0,0),
                             (P1.bulletStartX, P1.bulletStartY),
                             (P1.bulletEndX,P1.bulletEndY),P1.bulletWidth)
                        screen.blit(playerFire, (P1.playerX, P1.playerY))
                        fireRate += 5 # Frames (60 = 1 second interval)
                P1.movement(event)
            elif event.type == pygame.KEYUP:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        # Interface Actions
        if pause_button.draw():
            level_1 = False
            time.sleep(0.1)
            pauseMenu = True
        
        # Accumulate frames
        count += 1

        # Weapons
        rate_control()

        # GUI screening
        screen.blit(playerIdle, (P1.playerX, P1.playerY))
        pause_button = Button(10,10,pauseButton)
        
    # Pause Menu
    elif pauseMenu:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
                
        # Interface Actions
        if resume_button.draw():
            pauseMenu = False
            time.sleep(0.1)
            level_1 = True
        if menu_button.draw():
            pauseMenu = False
            time.sleep(0.1)
            mainMenu = True

        # Accumulate frames
        count += 1

        # GUI screening
        resume_button = Button(150,150,resumeButton)
        menu_button = Button(10,10,menuButton)

    elif levelSelector:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        # Interface Actions
        if level_button1.draw():
            levelSelector = False
            time.sleep(0.1)
            level_1 = True

        if level_button2.draw():
            pass

        if level_button3.draw():
            pass

    screenControl()
