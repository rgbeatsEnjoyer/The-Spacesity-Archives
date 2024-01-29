"""
Loops Testing
"""

for i in 'Spacesity':
    print(i)

initial = int(input("What is your starting number?"))
target = int(input("Which number is your target?:"))
crement = int(input("What is your increase(positive)/decrease(negative) number?:"))
    
for i in range(initial,target,crement):
    if target > initial:
        print(i + 1)
    else:
        print(i - 1)
