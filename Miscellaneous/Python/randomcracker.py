import time
import random

password = [random.randint(0,9) for i in range(4)]
search = [0,0,0,0]
lst = []

for i in range(100):
    start_time = time.time()
    while search != password:
        search = [random.randint(0,9) for i in range(4)]
        print(search)
        if search == password:
            break
    end_time = time.time()
    time_taken = end_time - start_time
    print(time_taken)
    lst.append(time_taken)
    password = [random.randint(0,9) for i in range(4)]
    search = [0,0,0,0]

average = sum(lst) / 100
print(f"average time taken to crack codes:{average}")
    