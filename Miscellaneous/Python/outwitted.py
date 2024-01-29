"""
Outwitted v1.0.0

Created by Spacesity
"""

import pygame, sys, random

pygame.init()

clock = pygame.time.Clock() # FPS

# Screen setup
screen = pygame.display.set_mode((555, 555)) # Screen size

# Image loading
squareImage = pygame.image.load("puzzlesquare.png").convert_alpha()
redguyImage = pygame.image.load("redguy.png").convert_alpha()
blueguyImage = pygame.image.load("blueguy.png").convert_alpha()
outofbounds = pygame.image.load("outofbounds.png").convert_alpha()
food = pygame.image.load("food.png").convert_alpha()

# Main game variables
gameStart = False # Start/Stop game
redguyLocation = (0,0)
blueguyLocation = (9,9)
SQUARE = 0
REDGUY = 1
BLUEGUY = 2
GREYSQUARE = 3
FOOD = 4 
squaregrid = [[0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,3,3,0,0,0,0],
              [0,0,0,0,3,3,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0],
              [4,0,0,0,0,0,0,0,0,0]]
count = 0
foodcount = 0

# 

# Main program loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # Start program
                gameStart = not gameStart

        if event.type == pygame.QUIT: # Exit program
            pygame.quit()
            sys.exit()

        screen.fill((0,0,139)) # Screen fill

        if event.type == pygame.KEYDOWN:

        # RED GUY MOVEMENT
                    
            if event.key == pygame.K_LEFT: # Moving left
                redguyLocation = (redguyLocation[0] - 1,redguyLocation[1])                   

            if event.key == pygame.K_RIGHT: # Moving right
                redguyLocation = (redguyLocation[0] + 1,redguyLocation[1])

            if event.key == pygame.K_UP: # Moving up
                redguyLocation = (redguyLocation[0],redguyLocation[1] - 1)

            if event.key == pygame.K_DOWN: # Moving down
                redguyLocation = (redguyLocation[0],redguyLocation[1] + 1)

         # BLUE GUY MOVEMENT
                    
            if event.key == pygame.K_a: # Moving left
                blueguyLocation = (blueguyLocation[0] - 1,blueguyLocation[1])                  

            if event.key == pygame.K_d: # Moving right
                blueguyLocation = (blueguyLocation[0] + 1,blueguyLocation[1])

            if event.key == pygame.K_w: # Moving up
                blueguyLocation = (blueguyLocation[0],blueguyLocation[1] - 1)

            if event.key == pygame.K_s: # Moving down
                blueguyLocation = (blueguyLocation[0],blueguyLocation[1] + 1)

    if gameStart:
        for row_number, row_contents in enumerate(squaregrid):
            for column_number, cell_content in enumerate(row_contents):
                screen.blit(squareImage, (row_number*55+5, column_number*55+5))
                if GREYSQUARE == cell_content:  
                    screen.blit(outofbounds, (row_number*55+5, column_number*55+5)) # Draws out of bounds areas
                if FOOD == cell_content:
                    screen.blit(food, (row_number*55+5, column_number*55+5)) 
        if squaregrid[9][0] == FOOD:
            if redguyLocation  == (9,0) or blueguyLocation == (9,0):
                squaregrid[9][0] = SQUARE
                foodcount = count
                print(count)
                print(foodcount)
        if squaregrid[9][0] == SQUARE:
            if count == foodcount + 600:
                squaregrid[9][0] = FOOD
                foodcount = count
                print(count)
                print(foodcount) 
       
       
       
        screen.blit(redguyImage, (redguyLocation[0]*55+5, redguyLocation[1]*55+5)) # Draws characters 
        screen.blit(blueguyImage,(blueguyLocation[0]*55+5, blueguyLocation[1]*55+5))

    count = count + 1
                
                
                



    # Update display
    pygame.display.flip()
    clock.tick(60) # Fps


"""

1) Key handling code (movement) = COMPLETE
2) Board barriers/player barriers = INCOMPLETE
3) Shrinking board = INCOMPLETE
4) Random spawning food = INCOMPLETE
5) Player trail and movements etc. = INCOMPLETE
6) Endgame + GUI = INCOMPLETE
        
"""






"""
Store players in the square grid as value 1 or 2 (red and blue)

Game rules:
- 10x10 board (each square has a small gap in between, numbers for co-ordinates)
- 2 players (red and blue), aim: to trap opponents with your trail. 
- Players trail expires after a certain amount of moves (e.g 10)
- avoid own trail?
- Middle blocked of by 2x2 square (no player can access the area) 
- Cannot take peoples trails 
"""


"""
In the top right and bottom left corners, food spawns in every 600 frames.

If play obtains food then, player trail length + 1.

playertrail = []

Food will add a new value to the player trail.
"""
