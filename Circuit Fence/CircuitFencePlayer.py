"""
Circuit Fence: Player Module
"""

import pygame
from pygame.locals import *
import random, time

class Player:

    def __init__(self,playerX,playerY,playerIdle,playerFire):
        # Player itself
        self.playerX = playerX
        self.playerY = playerY
        self.playerIdle = playerIdle
        self.playerFire = playerFire
        # Bullet
        self.bulletEndX = 0
        self.bulletStartX = self.playerX + 68
        self.bulletStartY = 600
        self.bulletEndY = 0
        self.bulletWidth = 2
        
    def movement(self,evt):
        if evt.key == pygame.K_a or evt.key == pygame.K_LEFT:
            self.playerX -= 1
        if evt.key == pygame.K_d or evt.key == pygame.K_RIGHT:
            self.playerX += 1

    def shoot(self):
        self.bulletStartX = self.playerX + 68
        spray = random.randint(-30,30)
        self.bulletEndX = self.bulletStartX + spray
        time.sleep(0)
