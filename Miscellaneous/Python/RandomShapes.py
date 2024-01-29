import random
import turtle

# Turtle Values
turtle.speed(10)

# Variables
int = random.randint(3,20)

for i in range(int):
    turtle.forward(1000/int)
    turtle.right(360/int)
