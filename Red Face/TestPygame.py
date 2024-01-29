import pygame, sys

import random

pygame.init()

clock = pygame.time.Clock() # Frames per second 

screen = pygame.display.set_mode((500, 500)) # Screen size
colour = (255, 255, 255)# Rect colour
screen.fill((0, 0, 0)) # Black background

pygame.display.set_caption('Red Face')
programIcon = pygame.image.load('redfacev2.png')
pygame.display.set_icon(programIcon)

a = random.randint(0,19)*25 # Position enemy 1
b = 0

c = random.randint(0,19)*25 # Position enemy 2
d = 0 

e = random.randint(0,19)*25 # Position enemy 3
f = 0

x = 250 # position of character 
y = 425

face = pygame.image.load("redfacev2.png") # Red face
enemyFace = pygame.image.load('badfacev2.png') # Enemy face

count = 0 # Frame counter  
score = 0 # Players game score

redFaceFont = pygame.font.Font(None, 25) # RedFace font
startButton = pygame.image.load("playbuttonv2.png")
hint = redFaceFont.render("Press space to start!", True, (255,255,255))
screen.blit(hint, (169, 325))
credit = redFaceFont.render("Created by Spacesity", True, (255,255,255))
screen.blit(credit, (169, 400))

retryButton = pygame.image.load("retrybuttonv1.png")
retryHint = redFaceFont.render("You died. Retry? Press space!", True, (255,255,255))

screen.blit(startButton, (75,125)) # Start button co-ordinates

gameStart = False
gamePause = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gameStart = True
                
    if gameStart:
        break

    # Update display
    pygame.display.flip()
    clock.tick(60) # Fps
    

while True: # Main code
    screen.fill((0,0,0)) # Constantly black background

    if gameStart:
        # Events input

        for event in pygame.event.get():
            #screen.blit(face, (x, y))
            if event.type == pygame.QUIT: # If player presses exit button
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: # Detects key
                
                if event.key == pygame.K_LEFT: # Moving left
                    x = x - 25
                    
                if event.key == pygame.K_RIGHT: # Moving right
                    x = x + 25

                if event.key == pygame.K_SPACE: # Pause game
                    gameStart = False
                    gamePause = True
                    
        if x > 475: # Teleports player from RightHandSide to left
            x = 0

        if x < 0: # Teleports player from LefttHandSide to left
            x = 475
                    
        count = count + 1 # Increase frame counter
        
        if count >= 1200:
            if count % 1 == 0: # Every (number) frames
                b = b + 25

            if count % 2 == 0: 
                d = d + 25

            if count % 3 == 0:
                f = f + 25
        else:
            if count % 2 == 0: # Every (number) frames
                b = b + 25

            if count % 3 == 0: 
                d = d + 25

            if count % 4 == 0:
                f = f + 25

        if b == 500:
            a = random.randint(0,19)*25
            b = 0
            score = score + 1
            
        if d == 500:
            c = random.randint(0,19)*25
            d = 0
            score = score + 1
            
        if f == 500:
            e = random.randint(0,19)*25
            f = 0
            score = score + 1
            
        # Draws the enemies
        screen.blit(enemyFace, (a, b)) # Enemy square
        screen.blit(enemyFace, (c, d)) # Enemy square
        screen.blit(enemyFace, (e, f)) # Enemy square

        img = redFaceFont.render("Score: " + str( score), True, (255,255,255))
        screen.blit(img, (400, 475))
     
        screen.blit(face, (x, y)) # Player 
        if x < a + 25 and y >= b and y < b + 25 and x >= a: # Enemy collision
                    gameStart = False

        screen.blit(face, (x, y)) # Player 
        if x < c + 25 and y >= d and y < d + 25 and x >= c: # Enemy collision
                    gameStart = False

        screen.blit(face, (x, y)) # Player 
        if x < e + 25 and y >= f and y < f + 25 and x >= e: # Enemy collision
                    gameStart = False

    elif gamePause:
        pauseButton = pygame.image.load("pausebuttonv1.png")
        screen.blit(pauseButton, (75,125)) # Display pause
        
        pauseHint = redFaceFont.render("Press space to resume!", True, (255,255,255))
        screen.blit(pauseHint, (160, 325)) # Resume
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameStart = True
                    gamePause = False

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameStart = True
                    
                    count = 0 
                    score = 0
                    x = 250 # Position of character 
                    y = 425

                    a = random.randint(0,19)*25 # Enemy positions
                    b = 0

                    c = random.randint(0,19)*25
                    d = 0 

                    e = random.randint(0,19)*25
                    f = 0
                    
        screen.blit(retryButton, (75,125))
        screen.blit(retryHint, (125, 325))
        retryScore = redFaceFont.render("Your score was: " + str( score), True, (255,255,255))
        screen.blit(retryScore, (175, 355))


    # Update display
    pygame.display.flip()
    clock.tick(60) # Fps


# Ideas and plans for future updates

"""
Highscore:

Saves score on start screen and retry screen. Saves permanently on a file.
"""




    


