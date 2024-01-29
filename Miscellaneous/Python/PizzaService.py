# Pizza Service Project (For computer science year 11)
import os, json, sys, time, random

# Data store
pizza_list = []
shopping_list = []
money = float

# Data check
if os.path.exists("ThePizzaFile.txt"):
    for i in range(0,70):
        print("Initializing Pizza file...", "(", i,"% )")
        time.sleep(0.069)
    print("PIZZA FILE INITIALIZED")
    time.sleep(1)
else:
  print("Error: Pizzas not found lmao")

# Classes and Functions
class pizza_worker():
    global statement
    def view_pizzas(): # V
        if statement == "V":
            viewing_pizzas = open("ThePizzaFile.txt", "r")
            for pizzas in viewing_pizzas:
                print(pizzas)

def view_pizzas():
    viewing_pizzas = open("ThePizzaFile.txt", "r")
    print("Pizza Menu:")
    for pizzas in viewing_pizzas:
        print(pizzas)
    viewing_pizzas.close()

# Main Loop
print("Welcome to Spacesity's Pizza Service Simulator!")
time.sleep(2)
print("Earn money as a worker and buy pizzas using your hard earnt money as a customer to gain rewards!")
time.sleep(3)

view_pizzas()

# Make loop structure first then focus on functions/class etc...
