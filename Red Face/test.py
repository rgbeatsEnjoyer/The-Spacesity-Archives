x = 0 # variables
a = 1
while x < 21: # x acending to any number (in this case 20) 
    x = x + 1
    for ace in range(1,x):
        print("a", end = "")
    print()


while x > 0: # x decending from 20 
    x = x - 1 
    """
    print(x) 
    """ # 3 quotes (""") is used to write longer comments
    for ace in range(1,x):
        print("a", end = "")
    print()

fruit = ["Banana", "Apple", "Grapefruit", "Passionfruit", "Watermelon"] # list (basically tables from Lua)
print(fruit)

print(fruit[0])
if fruit[0] == "Banana": 
    print("BANANAS!")

fruit.append("Mango")
print(fruit)

fruit.insert(3, "Pear") # puts "Pear" into position 3, everything above moves along 
print(fruit)

tiger = {"species": "cat", "habitat": "jungle", "colour": "orange"} # dict (dictionary)
print(tiger)
tiger["habitat"] = "forest"
print(tiger)

def calculation(a,x,y): # functioning calculator v1.2
    
    if a == "*":
        print(x,y)
        return int(x)*int(y)
    elif a == "/":
        print(x,y)
        return int(x)/int(y)
    elif a == "+":
        print(x,y)
        return int(x)+int(y)
    elif a == "-":
        print(x,y)
        return int(x)-int(y)
    
op1=input('enter a operator =')   
num1=input('enter a value =')
num2=input('enter a value =')
print(calculation(op1,num1,num2))

def sequence(num): # pattern maker test 
    print("aaa")
    print("aaa")
    print("aaa")
    print("bbbbbb")
    print("bbbbbb")
    print("bbbbbb")
    for number in range(1,num + 1):
        print("aaa")
        print("aaa")
        print("aaa")
        print("bbbbbb")
        print("bbbbbb")
        print("bbbbbb") 
        
    
sequence(0)




