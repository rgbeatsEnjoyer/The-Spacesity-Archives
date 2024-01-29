# University applications
import json

# Data stores
grades = {"A*": 8, "A": 7, "B": 6, "C": 5, "D": 4, "E": 3, "F": 2, "U": 1}
minimum_pass = 18

# Functions

# Iterations
print("To enter university, you need an avg grade of B")
print("Enter applicant name then 3 A-level grades")

applicant = input("Applicant:")
grade1 = input("Applicant's Grade 1:")
grade2 = input("Applicant's Grade 2:")
grade3 = input("Applicants Grade 3:")

total_grade = grade1 + grade2 + grade3
average_grade = total_grade/3
    
# Output
