# Click detection
import pygame, sys
from pygame.locals import *
pygame.init()

# Variables
clock = pygame.time.Clock()
count = 0

# Screen
screen_width,screen_height = 500,500
screen = pygame.display.set_mode((screen_width, screen_height))

# Functions
def screen_control(): # Update display
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

def click_detection(startvertex_x,startvertex_y,distance_x,distance_y):
    if pos[0] >= startvertex_x and pos[0] <= startvertex_x + distance_x:
        if pos[1] >= startvertex_y and pos[1] <= startvertex_y + distance_y:
            print("Detection Valid:", pos)

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            click_detection(0,0,250,250)
    
    count += 1 
    screen_control()
