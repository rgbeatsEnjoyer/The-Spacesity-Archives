"""
Avatar of Light v1.4.1

Created by Spacesity

Sounds and Music created by Sync

Controls:
Press 'SPACE' to interact (Start/Pause/Restart). 
Use arrow keys or 'A' and 'D' to move left and right.
"""

import pygame
from pygame.locals import *
from pygame import mixer
import sys, random, json, time

pygame.init()
mixer.init()


clock = pygame.time.Clock() # Frames per second
pygame.key.set_repeat()
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

# Screen setup
screen = pygame.display.set_mode((500, 500)) # Screen size

# Image loading
startButton = pygame.image.load("playbuttonv4.png").convert_alpha()
pauseButton = pygame.image.load("pausebuttonv3.png").convert_alpha()
retryButton = pygame.image.load("retrybuttonv4.png").convert_alpha()
face = pygame.image.load("thelightv1.png").convert_alpha()
enemyFace = pygame.image.load('thebadv1.png').convert_alpha() 
mult = pygame.image.load('multiplierv1.png').convert_alpha()
logo = pygame.image.load("thelightlogo.png").convert_alpha()

# Text loading
UsualFont = pygame.font.Font(None, 25) # RedFace font
hint = UsualFont.render("Press space to start!", True, (255,255,255))
credit1 = UsualFont.render("Created by Spacesity", True, (255,255,255))
credit2 = UsualFont.render("Music created by Sync", True, (255,255,255))
retryHint = UsualFont.render("You died. Retry? Press space!", True, (255,255,255))

# Sound loading
multiplierSound = pygame.mixer.Sound("powerUp.wav")
deathSound = pygame.mixer.Sound("explosion3.wav")
StartSound = pygame.mixer.Sound("StartSound.wav")
mixer.music.load('aolMenu.wav')
mixer.music.set_volume(0.7)
mixer.music.play(-1)

# Character size
blockSize = 50

# Main game variables
enemySpeed = 5 # Enemy Speed
count = 0 # Frame counter  
score = 0 # Players game score
multiplier = 1 # Multiplier
highScore = [0] # High score
volume = 0.7

try:
    with open('aol_highscore.txt')as score_file:
        highScore = json.load(score_file)
except:
    print('High Score file not created yet')
gameStart = False # Start
gamePause = False # Pause
c = 0
e = 0
w = 0

# Functions
def exclusive_random(excl1, excl2, excl3): # Anti-SameLaneEnemies
    p = True 
    EnemyRan = int(random.random()*10)*blockSize
    while p == True:
        if EnemyRan == excl1 or EnemyRan == excl2 or EnemyRan == excl3:
            p = True 
            EnemyRan = random.randint(0,9)*blockSize
        else:
            p = False
            return EnemyRan

def music_random(): # Randomizes Music Tracks
    SongRandomizer = random.randint(1,3)
    if SongRandomizer == 1:
        mixer.music.load('Summer_song_FINAL.wav')
        mixer.music.set_volume(volume)
        mixer.music.play(-1)
    if SongRandomizer == 2:
        mixer.music.load('BeginningOfSomethingNew.wav')
        mixer.music.set_volume(volume)
        mixer.music.play(-1)
    if SongRandomizer == 3:
        mixer.music.load('guitar_song.wav')
        mixer.music.set_volume(volume)
        mixer.music.play(-1)

def EnemyCollision (playerX,playerY,enemyX,enemyY): # Collision
            if (playerX < enemyX + blockSize and playerY >= enemyY and playerY < enemyY + blockSize and playerX >= enemyX) or \
            (playerX + blockSize < enemyX + blockSize and playerY >= enemyY and playerY < enemyY + blockSize and playerX + blockSize > enemyX) or \
            (playerX < enemyX + blockSize and playerY + blockSize >= enemyY and playerY + blockSize < enemyY + blockSize and playerX >= enemyX) or \
            (playerX + blockSize < enemyX + blockSize and playerY + blockSize >= enemyY and playerY + blockSize < enemyY + blockSize and playerX + blockSize > enemyX):  
                return True
            else:
                return False

# Co-ordinates
a = exclusive_random(c,e,w)# Position enemy 1
b = -150

c = exclusive_random(a,e,w) # Position enemy 2
d = -300

e = exclusive_random(a,c,w) # Position enemy 3
f = -450

w = exclusive_random(e,c,a) # Position star
z = -2000

x = 250 # Position of character
targetx = x
y = 500 - blockSize * 2 # Position of character 

# Draws the screen
screen.blit(hint, (169, 325))
screen.blit(credit1, (169, 400))
screen.blit(credit2, (165, 425))
screen.blit(startButton, (75,125)) # Start button co-ordinates
pygame.display.set_caption('Avatar of Light')
pygame.display.set_icon(logo)

while 1: # Start screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If player presses exit button
            with open('aol_highscore.txt','w')as score_file:
                    json.dump(highScore,score_file)
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_u: # Volume up
                volume += 0.1
                mixer.music.set_volume(volume)
                

            if event.key == pygame.K_i: # Volume down
                volume -= 0.1
                mixer.music.set_volume(volume)
                

            if event.key == pygame.K_SPACE:
                mixer.music.pause()
                StartSound.play()
                music_random()
                gameStart = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if startButton.get_rect().collidepoint(75, 125):
                mixer.music.pause()
                StartSound.play()
                music_random()
                gameStart = True

    if gameStart:
        break

    # Update display
    pygame.display.flip()
    clock.tick(120) # Fps
    pygame.display.update()
    
# Game Loop
while 1:
    screen.fill((0,0,0)) # Black Background
    if gameStart:
        # Events input
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If player presses exit button
                with open('aol_highscore.txt','w')as score_file:
                    json.dump(highScore,score_file)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP: # Detects key
                
                if event.key == pygame.K_a or event.key == pygame.K_LEFT: # Moving left
                    targetx -= 50
                    x = x - 5                   

                if event.key == pygame.K_d or event.key == pygame.K_RIGHT: # Moving right
                    targetx += 50
                    x = x + 5

                if event.key == pygame.K_u: # Volume up
                    volume += 0.1
                    mixer.music.set_volume(volume)
                    

                if event.key == pygame.K_i: # Volume down
                    volume -= 0.1
                    mixer.music.set_volume(volume)
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    StartSound.play()# Pause game
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
        
        if count >= 2400:
            # Every (number) frames (HARD)
            b += round(blockSize/11)

            d += round(blockSize/11)

            f += round(blockSize/11)

            z += round(blockSize/20)
        elif count >= 1200:
            # Every (number) frames (MEDIUM)
            b += round(blockSize/12)

            d += round(blockSize/12)

            f += round(blockSize/12)

            z += round(blockSize/20)
        else:
            # Every (number) frames (EASY)
            b += round(blockSize/15)

            d += round(blockSize/15)

            f += round(blockSize/15)

            z += round(blockSize/20)
            
        # Path Randomizer
        if b >= 500:
            a = exclusive_random(c,e,w)
            b = 0
            score = score + multiplier
            
        if d >= 500:
            c = exclusive_random(a,e,w)
            d = 0
            score = score + multiplier
            
        if f >= 500:
            e = exclusive_random(a,c,w)
            f = 0
            score = score + multiplier

        if z >= 6000:
            w = exclusive_random(e,c,a)
            z = -2000

        # Draws the enemies
        screen.blit(mult, (w, z)) # Multiplier Image
        for enemyPosition in [(a,b),(c,d),(e,f)]:
            screen.blit(enemyFace, (enemyPosition[0], enemyPosition[1])) # Enemy square

        # Draws Text
        img = UsualFont.render("Score: " + str( score), True, (255,255,255))
        screen.blit(img, (10, 475))

        starScore = UsualFont.render("Multiplier: " + str( multiplier), True, (255,255,255))
        screen.blit(starScore, (10, 455))

        screen.blit(face, (x, y))

        for enemyPosition in [(a,b),(c,d),(e,f)]:
            if EnemyCollision(x,y,enemyPosition[0],enemyPosition[1]):
                deathSound.play()
                time.sleep(0.4)
                mixer.music.load('DeathSong.wav')
                mixer.music.set_volume(volume)
                mixer.music.play()
                gameStart = False

        if EnemyCollision(x,y,w,z):
            multiplierSound.play()
            multiplier = multiplier + 1
            w = 525
            z = 525

    # If game pauses
    elif gamePause:
        screen.blit(pauseButton, (75,125)) # Display pause
        pauseHint = UsualFont.render("Press space to resume!", True, (255,255,255))
        currentScore = UsualFont.render("Score: " + str( score), True, (255,255,255))
        screen.blit(pauseHint, (160, 325))
        screen.blit(currentScore, (215, 360))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                with open('aol_highscore.txt','w')as score_file:
                    json.dump(highScore,score_file)
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    StartSound.play()
                    gameStart = True
                    gamePause = False

    else:
        pygame.key.set_repeat() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                with open('aol_highscore.txt','w')as score_file:
                    json.dump(highScore,score_file)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_u: # volume up
                    volume += 0.1
                    mixer.music.set_volume(volume)
                    

                if event.key == pygame.K_i: # volume down
                    volume -= 0.1
                    mixer.music.set_volume(volume)
                    

                if event.key == pygame.K_SPACE:
                    StartSound.play()
                    music_random()
                    gameStart = True
                    count = 0 
                    score = 0
                    multiplier = 1
                    targetx = x = 250 # Position of character 
                    y = 500 - blockSize * 2

                    a = exclusive_random(c,e,w) # Enemy positions
                    b = -150

                    c = exclusive_random(a,e,w)
                    d = -300

                    e = exclusive_random(a,c,w)
                    f = -450

                    w = exclusive_random(a,c,e) # Star position
                    z = -2000
                    
        screen.blit(retryButton, (75,125))
        screen.blit(retryHint, (125, 325))
        retryScore = UsualFont.render("Your score was: " + str( score), True, (255,255,255))
        if highScore[0] < score:
            highScore[0] = score
        textHighScore = UsualFont.render("High Score: " + str( highScore[0]), True, (255,255,255))
        screen.blit(textHighScore, (195, 385))
        screen.blit(retryScore, (175, 355))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If player presses exit button
                with open('aol_highscore.txt','w')as score_file:
                    json.dump(highScore,score_file)
                pygame.quit()
                sys.exit()

    # Update display
    pygame.display.flip()
    clock.tick(120) # Fps
    pygame.display.update()
