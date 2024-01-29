"""
Use binary search to solve the problem

Created by Spacesity
"""

import random

import sys

# Randomiser
RandomNumber = random.randint(1,999)
"""print(RandomNumber)"""

# Variables
numberOfGuesses = 1
Guess = 0

# Statements
print("I am thinking of a number, roughly between 1 and 999. Can you guess what it is?")

# Guessing loop
while Guess != RandomNumber:
    Guess = int(input('Guess:'))
    """GuessThingy = Guess.strip().upper()"""

    if Guess > RandomNumber:
        print("Number is too high!")
        numberOfGuesses = numberOfGuesses + 1
    if Guess < RandomNumber:
        print("Number is too low!")
        numberOfGuesses = numberOfGuesses + 1
    if Guess == RandomNumber:
        print("Well done, you guessed correctly!")
        print("Guesses taken:",numberOfGuesses) 
        Again = input('Again? (If so say "Yes"):')
        YesStripUpper = Again.strip().upper()
        if Again == 'Yes':
            Guess = 0
            numberOfGuesses = 0
            RandomNumber = random.randint(1,999)
            print("I am thinking of a number, roughly between 1 and 999. Can you guess what it is?")
            Guess != RandomNumber
        else:
            print("Thank you for playing!")
            sys.exit()
