# Trigonometry and Pythag
import math, sys
number = float

# Functions
class sohcahtoa:
    def sin_function(number):
        a = math.sin(number)
        print(a)
        return a
    
    def cos_function(number):
        b = math.cos(number)
        print(b)
        return b
    
    def tan_function(number):
        c = math.tan(number)
        print(c)
        return c

class pythag:
    def hyp_function(number1, number2):
        hyp = math.sqrt((number1 ** 2) + (number2 ** 2))
        print(hyp)
        return hyp
    
    def opp_or_adj_function(number):
        opp_or_adj = math.sqrt((number1 ** 2) - (number2 ** 2))
        print(opp_or_adj)
        return(opp_or_adj)

class miscellaneous:
    def input_constructor(input_variable, check, text, preformed_function):
        global number
        if input_variable == str(check): # E.g inp1, "TAN"
            number = float(input(str(text))) # E.g "Enter value:"
            preformed_function(number)

# Calculator
while True:
    select = str(input("Trigonometry (T) or Pythag (P). If not Quit (Q):").upper().strip())
    
    if select == "T":
        inp1 = str(input("What calculation would you like to preform (Sin, Cos or Tan)?:").upper().strip())
        miscellaneous.input_constructor(inp1, "SIN", "Enter value:", sohcahtoa.sin_function)
        miscellaneous.input_constructor(inp1, "COS", "Enter value:", sohcahtoa.cos_function)
        miscellaneous.input_constructor(inp1, "TAN", "Enter value:", sohcahtoa.tan_function)
        if inp1 != "SIN" or inp1 != "COS" or inp1 != "TAN":
            pass
    
    elif select == "P":
        inp2 = str(input("What calculation would you like to work out? Hypoteneus (H) or Adjacent/Opposite (AO):").upper().strip())
        if inp2 == "H":
            number1 = float(input("Enter Adjacent:"))
            number2 = float(input("Enter Opposite:"))
            pythag.hyp_function(number1, number2)
        elif inp2 == "AO":
            number1 = float(input("Enter Hypoteneus:"))
            number2 = float(input("Enter Adjacent or Opposite:"))
            pythag.opp_or_adj_function(number1, number2)
        else:
            pass
    
    elif select == "Q":
        sys.exit()
    
    else:
        pass 