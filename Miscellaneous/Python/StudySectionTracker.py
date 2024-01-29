# Study Section Tracker
import sys, time, csv

command_options = ["Update Section (U)", "View Current Section (V)", "Command List (C)", "Exit (E)"]

# Functions
class commands():
    def section_complete(inputter):
        if inputter > 0 and inputter < 6:
            with open("SectionTrackerFile.txt", "w") as section_file:
                section_file.write(str(inputter + 1))
                print("You are now on Section: ",  inputter + 1)
                section_file.close()
        elif inputter == 6:
            with open("SectionTrackerFile.txt", "w") as section_file:
                section_file.write(str(1))
                print("You are now on Section: ", 1)
                section_file.close()
        else:
            print("Invalid input for sections. There are only 6 sections (excluding homework sections)")

    def exit():
        print("Well done, keep doing the hard work! Stick to your system and you will be grateful for the hardwork you put in now.")
        time.sleep(5)
        print("Closing...")
        time.sleep(1)
        sys.exit()
    
    def command_list():
        for i in range(0, len(command_options)):
            print(command_options[i])
            time.sleep(0.25)
    
    def view_section():
        with open("SectionTrackerFile.txt", "r") as section_file:
            print("Current Section: ", section_file.read())
            section_file.close()

# Iterations
print("Spacesity's Study Section Tracker")
while True:
    command = str(input("What would you like to preform? Enter 'C' for command list or 'E' to exit the program: ").strip().upper())
    if command == "U":
        command_input = int(input("Enter the section you have just finished! Section: "))
        commands.section_complete(command_input)
    elif command == "V":
        commands.view_section()
    elif command == "C":
        commands.command_list()
    elif command == "E":
        commands.exit()
    else:
        print("Invalid command")