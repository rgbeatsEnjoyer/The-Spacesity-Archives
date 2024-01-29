# Python Lambda test
def calculate(n):
    return lambda a, b : (a**n) + (b**n)

square_add = calculate(2)
print(square_add(6,9))