"""
---

Avatar of Light v1.3.0

Created by Spacesity

Music by my friend Sync (Check out his Music at https://soundcloud.com/user-902044539)

Software is open source. Feel free to modify this game for your own purpose.

---

Developer notes:

- New music by my friend Sync (Beginning of Something New)
- Allow support for both Arrow Keys and WASD

---

Controls:

Press 'SPACE' to interact (Start/Pause/Restart). 
Use arrow keys or 'A' and 'D' to move left and right.

---
"""

import pygame
from pygame.locals import *
from pygame import mixer
import sys
import random

pygame.init()
mixer.init()

clock = pygame.time.Clock() # Frames per second

pygame.key.set_repeat()

# Screen setup
screen = pygame.display.set_mode((500, 500)) # Screen size

# Image loading
startButton = pygame.image.load("playbuttonv4.png").convert_alpha()
pauseButton = pygame.image.load("pausebuttonv3.png").convert_alpha()
retryButton = pygame.image.load("retrybuttonv4.png").convert_alpha()
face = pygame.image.load("thelightv1.png").convert_alpha() # Red face
enemyFace = pygame.image.load('thebadv1.png').convert_alpha() # Enemy face
star = pygame.image.load('starobjectv2.png').convert_alpha()
logo = pygame.image.load("thelightlogo.png").convert_alpha()# Star object

# Text loading
redFaceFont = pygame.font.Font(None, 25) # RedFace font
hint = redFaceFont.render("Press space to start!", True, (255,255,255))
credit = redFaceFont.render("Created by Spacesity", True, (255,255,255)) 
retryHint = redFaceFont.render("You died. Retry? Press space!", True, (255,255,255))

# Sound loading
mixer.music.load('BeginningOfSomethingNew.mp3')
mixer.music.play(-1)

# Character size
blockSize = 50

# Main game variables
enemySpeed = blockSize/7 # Enemy Speed
count = 0 # Frame counter  
score = 0 # Players game score
starDust = 0 # Stardust count
highScore = 0 # High score (for game session)
gameStart = False # Start
gamePause = False # Pause
c = 0
e = 0
w = 0

# Main game functions
def exclusive_random(excl1, excl2, excl3): # Anti-SameLaneEnemies
    p = True 
    gcse = int(random.random()*10)*blockSize
    while p == True:
        if gcse == excl1 or gcse == excl2 or gcse == excl3:
            p = True 
            gcse = random.randint(0,9)*blockSize
        else:
            p = False
            return gcse

# Co-ordinates
a = exclusive_random(c,e,w)# Position enemy 1
b = -75

c = exclusive_random(a,e,w) # Position enemy 2
d = -500

e = exclusive_random(a,c,w) # Position enemy 3
f = -1000

w = exclusive_random(e,c,a) # Position star
z = -2000

x = 250 # Position of character
targetx = x
y = 500 - blockSize * 2 # Position of character 

# Draws the screen
screen.blit(hint, (169, 325))
screen.blit(credit, (169, 400))
screen.blit(startButton, (75,125)) # Start button co-ordinates
colour = (255, 255, 255)# Rect colour
pygame.display.set_caption('Avatar of Light')
pygame.display.set_icon(logo)

while True: # Start screen
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                gameStart = True
                
    if gameStart:
        break

    # Update display
    pygame.display.flip()
    clock.tick(60) # Fps
    
# "The Game Loop"
while True: 
    screen.fill((0,0,0)) # Constantly black background
    
    
    if gameStart:
        # Events input
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If player presses exit button
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP: # Detects key
                
                if event.key == pygame.K_a or event.key == pygame.K_LEFT: # Moving left
                    targetx -= 50
                    x = x - 5                   

                if event.key == pygame.K_d or event.key == pygame.K_RIGHT: # Moving right
                    targetx += 50
                    x = x + 5 

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE: # Pause game
                    gameStart = False
                    gamePause = True
                    
        if x > targetx:
            x -= 5
        if x < targetx:
            x += 5
            
        if x > (549 - blockSize): # Teleports player from RightHandSide to left
            x = 0
            targetx = x

        if x < -49: # Teleports player from LeftHandSide to left
            x = 450
            targetx = x

        
        count = count + 1 # Increase frame counter
        
        if count >= 1200:
            # Every (number) frames
            b = b + round(blockSize/10)

            d = d + round(blockSize/14)

            f = f + round(blockSize/18)

            z = z + round(blockSize/25)
        else:
            # Every (number) frames
            b = b + round(blockSize/12)

            d = d + round(blockSize/16)

            f = f + round(blockSize/20)

            z = z + round(blockSize/25) 

        
        if b >= 500:
            a = exclusive_random(c,e,w)
            b = 0
            score = score + 1 + starDust
            
        if d >= 500:
            c = exclusive_random(a,e,w)
            d = 0
            score = score + 1 + starDust
            
        if f >= 500:
            e = exclusive_random(a,c,w)
            f = 0
            score = score + 1 + starDust

        if z >= 6000:
            w = exclusive_random(e,c,a)
            z = -1000

        
        # Draws the enemies
        screen.blit(star, (w, z)) # Star
        for enemyPosition in [(a,b),(c,d),(e,f)]:
            screen.blit(enemyFace, (enemyPosition[0], enemyPosition[1])) # Enemy square

        img = redFaceFont.render("Score: " + str( score), True, (255,255,255))
        screen.blit(img, (10, 475))

        starScore = redFaceFont.render("Stardust: " + str( starDust), True, (255,255,255))
        screen.blit(starScore, (10, 455))

        screen.blit(face, (x, y))

        # Enemy Collision (So much code omg)
        def EnemyCollision (playerX,playerY,enemyX,enemyY):
            if (playerX < enemyX + blockSize and playerY >= enemyY and playerY < enemyY + blockSize and playerX >= enemyX) or \
            (playerX + blockSize < enemyX + blockSize and playerY >= enemyY and playerY < enemyY + blockSize and playerX + blockSize > enemyX) or \
            (playerX < enemyX + blockSize and playerY + blockSize >= enemyY and playerY + blockSize < enemyY + blockSize and playerX >= enemyX) or \
            (playerX + blockSize < enemyX + blockSize and playerY + blockSize >= enemyY and playerY + blockSize < enemyY + blockSize and playerX + blockSize > enemyX):  
                return True
            else:
                return False

        for enemyPosition in [(a,b),(c,d),(e,f)]:
            if EnemyCollision(x,y,enemyPosition[0],enemyPosition[1]):
                gameStart = False

        if EnemyCollision(x,y,w,z):
            starDust = starDust + 1
            w = 525
            z = 525
            

    # If game pauses
    elif gamePause:
        pygame.key.set_repeat() 
        screen.blit(pauseButton, (75,125)) # Display pause
        pauseHint = redFaceFont.render("Press space to resume!", True, (255,255,255))
        currentScore = redFaceFont.render("Score: " + str( score), True, (255,255,255))
        screen.blit(pauseHint, (160, 325))
        screen.blit(currentScore, (215, 360))# Resume
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    gameStart = True
                    gamePause = False
                    

    else:
        pygame.key.set_repeat() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    gameStart = True
                    
                    count = 0 
                    score = 0
                    starDust = 0
                    targetx = x = 250 # Position of character 
                    y = 500 - blockSize * 2

                    a = exclusive_random(c,e,w) # Enemy positions
                    b = 0

                    c = exclusive_random(a,e,w)
                    d = 0 

                    e = exclusive_random(a,c,w)
                    f = 0

                    w = exclusive_random(a,c,e) # Star position
                    z = -2000
                    
        screen.blit(retryButton, (75,125))
        screen.blit(retryHint, (125, 325))
        retryScore = redFaceFont.render("Your score was: " + str( score), True, (255,255,255))
        if highScore < score:
            highScore = score
        textHighScore = redFaceFont.render("High Score: " + str( highScore), True, (255,255,255))
        screen.blit(textHighScore, (195, 385))
        screen.blit(retryScore, (175, 355))
        
    # Update display
    pygame.display.flip()
    clock.tick(120) # Fps

"""
Further Update Plan:

1/ Add an intro (credits, update logs, etc)

"""
