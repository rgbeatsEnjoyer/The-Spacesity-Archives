"""
---

Avatar of Light v1.0.0

Created by Spacesity

Software is open source. Feel free to modify this game for your own pleasure.

Made with Python™

---

Developer notes:

- Added Stardust
- GUI fixes and improvements

---
"""

import pygame, sys, random

pygame.init()

clock = pygame.time.Clock() # Frames per second

pygame.key.set_repeat()

# Screen setup
screen = pygame.display.set_mode((500, 500)) # Screen size

# Image loading
startButton = pygame.image.load("playbuttonv3.png").convert_alpha()
pauseButton = pygame.image.load("pausebuttonv2.png").convert_alpha()
retryButton = pygame.image.load("retrybuttonv3.png").convert_alpha()
face = pygame.image.load("thelightv1.png").convert_alpha() # Red face
enemyFace = pygame.image.load('thebadv1.png').convert_alpha() # Enemy face
star = pygame.image.load('starobjectv2.png').convert_alpha()
logo = pygame.image.load("thelightlogo.png").convert_alpha()# Star object

# Text loading
redFaceFont = pygame.font.Font(None, 25) # RedFace font
hint = redFaceFont.render("Press space to start!", True, (255,255,255))
credit = redFaceFont.render("Created by Spacesity", True, (255,255,255))
retryHint = redFaceFont.render("You died. Retry? Press space!", True, (255,255,255))

# Character size
blockSize = 50

# Main game variables
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
b = 0

c = exclusive_random(a,e,w) # Position enemy 2
d = 0 

e = exclusive_random(a,c,w) # Position enemy 3
f = 0

w = exclusive_random(e,c,a) # Position star
z = -2000

x = 250 # Position of character 
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
        pygame.key.set_repeat(16)

        for event in pygame.event.get():
            #screen.blit(face, (x, y))
            if event.type == pygame.QUIT: # If player presses exit button
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: # Detects key
                
                if event.key == pygame.K_LEFT: # Moving left
                    x = x - round(blockSize/8)                   

                if event.key == pygame.K_RIGHT: # Moving right
                    x = x + round(blockSize//8) 

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE: # Pause game
                    gameStart = False
                    gamePause = True
                    
                    
                    
        if x > (549 - blockSize): # Teleports player from RightHandSide to left
            x = 0

        if x < -49: # Teleports player from LefttHandSide to left
            x = 500 - blockSize
                    
        count = count + 1
        
        # Increase frame counter
        
        if count >= 1200:
            # Every (number) frames
            b = b + round(blockSize/6)

            d = d + round(blockSize/7)

            f = f + round(blockSize/8)

            z = z + round(blockSize/10)
        else:
            # Every (number) frames
            b = b + round(blockSize/6)

            
            d = d + round(blockSize/7)

            
            f = f + round(blockSize/8)

        
            z = z + round(blockSize/10) 

        
        if b >= 500:
            a = exclusive_random(c,e,w)
            b = 0
            score = score + 1
            
        if d >= 500:
            c = exclusive_random(a,e,w)
            d = 0
            score = score + 1
            
        if f >= 500:
            e = exclusive_random(a,c,w)
            f = 0
            score = score + 1

        if z >= 6000:
            w = exclusive_random(e,c,a)
            z = -2000

        
        # Draws the enemies
        screen.blit(star, (w, z)) # Star
        screen.blit(enemyFace, (a, b)) # Enemy square
        screen.blit(enemyFace, (c, d)) # Enemy square
        screen.blit(enemyFace, (e, f)) # Enemy square
       
        img = redFaceFont.render("Score: " + str( score), True, (255,255,255))
        screen.blit(img, (400, 475))

        starScore = redFaceFont.render("Stardust: " + str( starDust), True, (255,255,255))
        screen.blit(starScore, (400, 455))
     
        screen.blit(face, (x, y)) # Player (Play col. code order: Top left, Top right, Bottom left, Bottom right) 
        if (x < a + blockSize and y >= b and y < b + blockSize and x >= a) or \
            (x + blockSize < a + blockSize and y >= b and y < b + blockSize and x + blockSize > a) or \
            (x < a + blockSize and y + blockSize >= b and y + blockSize < b + blockSize and x >= a) or \
            (x + blockSize < a + blockSize and y + blockSize >= b and y + blockSize < b + blockSize and x + blockSize > a):  
                    gameStart = False
                    

        # screen.blit(face, (x, y)) # Player (Play col. code order: Top left, Top right, Bottom left, Bottom right)
        if (x < c + blockSize and y >= d and y < d + blockSize and x >= c) or \
            (x + blockSize < c + blockSize and y >= d and y < d + blockSize and x + blockSize > c) or \
            (x < c + blockSize and y + blockSize >= d and y + blockSize < d + blockSize and x >= c) or \
            (x + blockSize < c + blockSize and y + blockSize >= d and y + blockSize < d + blockSize and x + blockSize > c):
                    gameStart = False
                    

        # screen.blit(face, (x, y)) # Player (Play col. code order: Top left, Top right, Bottom left, Bottom right)
        if (x < e + blockSize and y >= f and y < f + blockSize and x >= e) or \
            (x + blockSize < e + blockSize and y >= f and y < f + blockSize and x + blockSize > e) or \
            (x < e + blockSize and y + blockSize >= f and y + blockSize < f + blockSize and x >= e) or \
            (x + blockSize < e + blockSize and y + blockSize >= f and y + blockSize < f + blockSize and x + blockSize > e):
                    gameStart = False

        # screen.blit(face, (x, y)) # Player (Play col. code order: Top left, Top right, Bottom left, Bottom right)
        if (x < w + blockSize and y >= z and y < z + blockSize and x >= w) or \
            (x + blockSize < w + blockSize and y >= z and y < z + blockSize and x + blockSize > w) or \
            (x < w + blockSize and y + blockSize >= z and y + blockSize < z + blockSize and x >= w) or \
            (x + blockSize < w + blockSize and y + blockSize >= z and y + blockSize < z + blockSize and x + blockSize > w):
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
                    x = 250 # Position of character 
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
    clock.tick(60) # Fps
