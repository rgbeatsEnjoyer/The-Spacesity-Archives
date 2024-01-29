# Circle Calculator
import json

# Pi 
pi = int

try:
    with open('CircleCalculatorPi.txt')as number:
        pi = json.load(number)
except:
    print("Pi was not created or found!")

area = int
circumference = int
diameter = int

# Functions
def diameter_function():
    global diameter
    diameter = radius * 2

def area_function():
    global area
    area = pi * (radius**2)

def circumference_function():
    global circumference
    circumference = pi * radius * 2

# Calculator
while True:
    radius = float(input("What is the radius?:"))
    diameter_function()
    area_function()
    circumference_function()
    print("Circle diameter = ", diameter, "Units")
    print("Circle area =", area, "Units^2")
    print("Circle circumference =", circumference, "Units")

    