import turtle
import random
import time

# Variables
screen = turtle.Screen()

# Player Variables
player = turtle.Turtle()
player.color(0,0,0)
player.speed(10)

# Functions
def up():
    player.setheading(90)
    player.forward(100)

def down():
    player.setheading(270)
    player.forward(100)

def left():
    player.setheading(180)
    player.forward(100)

def right():
    player.setheading(0)
    player.forward(100)

def clickleft():
    player.penup()

def clickright():
    player.pendown()

turtle.listen()

# Events

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

# Main Loop


turtle.mainloop() # Must be at bottom of program






