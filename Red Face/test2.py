"""import random 

a = random.randint(0,10)

b = random.randint(0,10)

c = random.randint(0,10)

x = True
y = True
z = True

while x == True:
    if a == b:
        x = True
        a = random.randint(0,10)
        b = random.randint(0,10)
    else:
        x = False

while y == True:   
    if a == c: 
        y = True
        a = random.randint(0,10)
        c = random.randint(0,10)
    else:
        y = False

while z == True:
    if b == c: 
        z = True
        a = random.randint(0,10)
        b = random.randint(0,10)
    else:
        z = False

print(a)
print(b)
print(c)"""

import random

def exclusive_random(excl1, excl2):
    p = True 
    gcse = random.randint(0,9)
    while p == True:
        if gcse == excl1 or gcse == excl2:
            p = True 
            gcse = random.randint(0,9)
        else:
            p = False
            return gcse

a = c = e = -1 

for set_num in range(1, 10):
    a = exclusive_random(c, e)
    c = exclusive_random(a, e)
    e = exclusive_random(a, c)
    print("set: ", set_num, ":", a, c, e)

