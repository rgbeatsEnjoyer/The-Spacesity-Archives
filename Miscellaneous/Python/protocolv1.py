"""

PROTOCOL v1.0.0

By Spacesity

"""

# Intro and credits

print("PROTOCOL v1.0.0 Created by Spacesity")
print("Welcome to PROTOCOL agent! Your task is to infiltrate and blow up the Russian base.  For each level you have some choices. Make sure to chose wisely as each option leads to a different outcome. Stay alive and good luck")

health = 100 # Variables
level = "Part1"

rooms = {} # Decisions

rooms["Part1"] = {"A":{"Next":"Part1","Msg":"You were shot in the head by a soldier","Health": -100},
                  "B":{"Next":"Part2","Msg":"You are inside the Russian base","Health": 0},
                  "C":{"Next":"Part2","Msg":"You are inside the Russian base","Health": 0},
                  "Text":"You are outside the building, A) Burst through the door B) Climb through the vents C) Break through the window"}

rooms["Part2"] = {"A":{"Next":"Part3a","Msg":"You shot the guard in the head","Health": 0},
                  "B":{"Next":"Part1","Msg":"You were shot in the head by a soldier","Health": -100},
                  "C":{"Next":"Part3b","Msg":"You get taken to an interrogation room","Health": 0},
                  "Text":"A guard spots you, A) Shoot him B) Run into a corner C) You pretend to be a Russian soldier"}

rooms["Part3a"] = {"A":{"Next":"Part1","Msg":"You were shot in the head by a soldier","Health": -100},
                   "B":{"Next":"Part1","Msg":"You were shot in the head by a soldier","Health": -100},
                   "C":{"Next":"FINISH","Msg":"You were shot in the leg by a soldier but survived. You plant a bomb in the bathroom and escape through the vents.","Health": 0},
                   "Text":"The shot fired sounds the alarm, troops come rushing towards you, A) Make a final stand B) Run C) Lock yourself in the bathroom"}

rooms["Part3b"] = {"A":{"Next":"Part1","Msg":"You were brutally tortured and died","Health": -100},
                   "B":{"Next":"Part1","Msg":"You were brutally tortured and died","Health": -100},
                   "C":{"Next":"FINISH","Msg":"They let you go to the bathroom. You plant a bomb in the bathroom and escape through the vents.","Health": 0},
                   "Text":"The commander walks in, he asks you some questions, A) You dont speak B) You try and resist C) You ask to go to the bathroom"}

while level != "FINISH" and health > 0: # Main code
    print(rooms[level]["Text"])
    Decision=input('Decision:')
    move = Decision.strip().upper()
    health = health + rooms[level][move]["Health"]
    print(rooms[level][move]["Msg"])
    print("Your health is:",health)

    level = rooms[level][move]["Next"]

if health <= 0: # Game Over
    print("Mission Failed")
    print("Run the program again to retry!")


if level == "FINISH": # Game Victory
    print("Mission Accomplished")
    print("Your total health is:",health,"Well done!")




    
    
    



        



