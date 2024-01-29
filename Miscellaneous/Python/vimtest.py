import time

decrement = 5

while True:
	print(time.time())
	while decrement > 0:
		command = input("Enter command:")
		decrement -= 1 
	decrement = 5
