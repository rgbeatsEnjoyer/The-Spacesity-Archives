import json
import sys

with open('list.txt') as list_file:
	lst = json.load(list_file)

class Tasks():
	def create_task():
		global command
		if command == "C":
			create = input("New task:")
			lst.append(create)

	def view_task():
		number = 0
		if command == "V":
			for index in range(0,len(lst)):
				print(f"Task {number + 1}: {lst[index]}")
				number += 1
        
	def remove_task():
		if command == "R":
			if len(lst) != 0:
				remove = int(input("Task number (to remove):"))
				remove = remove - 1
				lst.pop(remove)
				print(f"Task: {remove + 1} was removed")

	def edit_task():
		if command == "E":
			if len(lst) != 0:
				task_number = int(input("Task number (to edit):"))
				task_number = task_number - 1
				task_edit = (input("Edit:"))
				lst[task_number] = task_edit

def exit_function():
	if command == "Q":
		with open('list.txt','w') as list_file:
			json.dump(lst, list_file)
			sys.exit()

print("Spacesity's Task-list program")

while True:
	command = input("Create (C), Remove (R), Edit (E) or View (V) list? If neither, Quit (Q):").capitalize()
	Tasks.create_task()
	Tasks.view_task()
	Tasks.remove_task()
	Tasks.edit_task()
	exit_function()
