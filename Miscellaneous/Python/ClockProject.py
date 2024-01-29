# Clock
import datetime, time
from datetime import datetime

# Variables
time_object = datetime.now()
current_time = time_object.strftime("%H:%M:%S")
current_date = time_object.strftime("%d-%m-%Y")

# Functions
def date_command():
    if command == "D" or command == "d":
        print("Date:", current_date)
        time.sleep(1)

def time_command():
    if command == "T" or command == "t":
        print("Time:", current_time)
        time.sleep(1)

# Loop
while True:
    print("What would you like to know?")
    time.sleep(1)
    command = input("Date (D) or Time (T)? If not, Exit (E):")
    date_command()
    time_command()
    
    if command == "E" or command == "e":
        print("Goodbye...")
        time.sleep(1)
        break