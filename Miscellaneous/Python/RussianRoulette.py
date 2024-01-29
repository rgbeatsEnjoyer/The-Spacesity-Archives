"""
Spacesity's Russian Roulette v1.0.3

Created by Spacesity
"""

import time 
import random

# Randomiser
Bullet = random.randint(1,6)

# Variables
Death = False
Score = 0
Guesses = [1,2,3,4,5,6]
GuessesTaken = []
HighScore = 0

# Statements
print("Welcome to Russian Roulette! Pick a bullet chamber (1-6) and hope it isn't a bullet!")
time.sleep(4)
print("Score points by surviving. If you die you lose and points reset!")
time.sleep(4)

# Game loop
while Death == False:
    if len(GuessesTaken) == 5:
        print("You survived Russian Roulette. Well done!")
        time.sleep(2)
        Again = input('Again? (If so type "Y"):')
        YesStripUpper = Again.strip().upper()
        if Score > HighScore:
            HighScore = Score
            print("NEW HIGH SCORE:",HighScore)
        if Again == 'Y':
            Death = False
            Guesses = [1,2,3,4,5,6]
            GuessesTaken = []
            Score = 0
            Bullet = random.randint(1,6)
            print("Welcome to Russian Roulette! Pick a bullet chamber (1-6) and hope it isn't a bullet!")
            time.sleep(4)
            print("Score points by surviving. If you die you lose and points reset!")
            time.sleep(4)
            print("Current High Score:",HighScore)
            time.sleep(2)
        else:
            print("Thank you for playing!")
    else:
        Guess = int(input("Bullet Chamber:"))
        
    if Guess in GuessesTaken:
        print("You have already played that option. Pick another chamber")
        time.sleep(2)

    elif Guess not in Guesses:
        print("Bro wtf, are you going to play the game properly or what?")
        time.sleep(2)

    elif Guess != Bullet:
        Score = Score + 10
        Guesses.pop(Guesses.index(Guess))
        GuessesTaken.append(Guess)
        print("You pull the trigger...")
        time.sleep(2)
        print("You survived!")
        time.sleep(2)
        print("Score:",Score)
            
    elif Guess == Bullet or Countdown == 0:
        Score == 0
        print("You pull the trigger...")
        time.sleep(2)
        print("BANG! You're dead!")
        time.sleep(2)
        print("Your score was:",Score)
        time.sleep(2)
        if Score > HighScore:
            HighScore = Score
            print("NEW HIGH SCORE:",HighScore)
            time.sleep(2)
        Death = True
        Again = input('Again? (If so type "Y"):')
        YesStripUpper = Again.strip().upper()
        if Again != 'Y':
            print("Thank you for playing!")
        else:
            time.sleep(2)
            Death = False
            Guesses = [1,2,3,4,5,6]
            GuessesTaken = []
            Score = 0
            Bullet = random.randint(1,6)
            print("Welcome to Russian Roulette! Pick a bullet chamber (1-6) and hope it isn't a bullet!")
            time.sleep(4)
            print("Score points by surviving. If you die you lose and points reset!")
            time.sleep(4)
            print("Current High Score:",HighScore)
            time.sleep(2)
            
        
        
    
    


