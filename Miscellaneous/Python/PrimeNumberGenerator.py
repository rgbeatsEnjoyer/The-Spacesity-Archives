# Prime Number Generator
import json

# Data stores
prime_numbers = []

# Load
try:
    with open('PrimeNumbers.txt')as prime_file:
        prime_numbers = json.load(prime_file)
except:
    print("Error, no txt file to save prime numbers")

# Variables
num = prime_numbers[-1] # Continue where left off

# Iterations
while True:
    prime = True
    for i in range(2,num): # Not prime
        if num % i == 0:
            prime = False
            break
    if prime: # Prime number
        prime_numbers.append(num)
        with open('PrimeNumbers.txt','w')as prime_file:
            json.dump(prime_numbers, prime_file)
        print(num)
    num += 2 # Increment counter
