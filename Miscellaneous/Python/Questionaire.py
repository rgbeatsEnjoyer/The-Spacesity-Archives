"""
Questionaire 
Created by Spacesity
"""
import time

# Data store
question_dict = {"Q1" : input("How many prime ministers did the UK have in 2022"),
                "Q2": input("How many bytes are in a megabyte?")}

answer_dict = {"Q1_A" : "3", "Q2_A" : "1024"} # REMEMBER KEY AND VALUE FOR NEXT TIME

# Variables
score = 0
current_question = 0

# Classes
class questionaire():
    def __init__(self,answered):
        self.question = question_dict[0]
        self.answered = False

    def question_giver(self):
        global current_question
        if current_question >= 0:
            print(question_dict(current_question))
    
    # def next_question(self):
        

        

questionaire.question_giver()
        
        







"""
Development:

Aim: Create a quiz which brings up questions and marks answer

1) Create a store of questions

2) Question

"""