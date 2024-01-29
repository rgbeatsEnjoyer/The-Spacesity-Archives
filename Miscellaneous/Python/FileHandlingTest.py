# File Handling test
import os

f = open("FileTest.txt", "at")
f.write(" is doing python!")
f.close()

f = open("FileTest.txt", "rt")
print(f.read())
f.close()
