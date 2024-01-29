"""
---
Light test v1.0.0

Created by Spacesity
---
"""

import pygame, sys, random

pygame.init()

clock = pygame.time.Clock() # Frames per second

# Screen setup
screen = pygame.display.set_mode((1000, 1000)) # Screen size
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Image loading
lightOff = pygame.image.load("LEDlightExampleNo1.png").convert_alpha()
lightOn1 = pygame.image.load("LEDlightExampleNo2.png").convert_alpha()
lightOn2 = pygame.image.load("LEDlightExampleNo3.png").convert_alpha()
lightOn3 = pygame.image.load("LEDlightExampleNo4.png").convert_alpha()
letterO = pygame.image.load("opensignO.png").convert_alpha()
letterP = pygame.image.load("opensignP.png").convert_alpha()
letterE = pygame.image.load("opensignE.png").convert_alpha()
letterN = pygame.image.load("opensignN.png").convert_alpha()

# Text loading

# Main game variables
programStart = False # Execute program
count = 0
lightbulbs = []
for bulbs in range(0,9):
    lightbulbs.append((200,100*bulbs + 50))

lightbulbs.append((400,500))
# Light states
lights = [3,2,1,0,0,0,0,0,0,0,0]

# Function ( Light Alternation )

pygame.display.set_caption('LED Light Idea')

# TEST
def count_function(count): # Light alternation
    if count %10 == 0:
        lights.insert(0, lights[9])
        del lights[10]
        
# Main program loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # Start program
                programStart = not programStart
                
        if event.type == pygame.QUIT: # Exit program
            pygame.quit()
            sys.exit()
        

    screen.fill((255,255,255)) # Screen fill
    
    

    if programStart:
        count = count + 1
        count_function(count)
    for light_location in range(0,10):
        if lights[light_location] == 1:
            screen.blit(lightOn1, lightbulbs[light_location])
        elif lights[light_location] == 2:
            screen.blit(lightOn2, lightbulbs[light_location])
        elif lights[light_location] == 3:
            screen.blit(lightOn3, lightbulbs[light_location])
        else:
             screen.blit(lightOff, lightbulbs[light_location])
        

   
    
       

    # Update display
    pygame.display.flip()
    clock.tick(60) # Fps
