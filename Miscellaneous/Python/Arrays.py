# Data Structures
import math, json

# Variables + Array
array = []
y = 0
n = 0

# Iterations
print("Enter numbers, finish adding by typing in -1")
while True: # Number input 
    input_num = int(input("What number would you like to add to array?:"))
    if input_num != -1:
        array.append(input_num)
    else:
        break
x = len(array)
y = sum(array)
    
# Output
print("Amount of numbers:",x)
print("Total value of numbers:",y)
print("Average of all numbers:",y/x)
