import sys

class WriteMessage:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_message(self, message):
        try:
            with open(str(self.file_name), "w") as data_file:
                data_file.write(str(message))
        except:
            print("Something went wrong!")
        finally:
            print(f"Your message: \n{msg}")
            sys.exit()

while True:
    msg = str(input("Write a message:"))
    msg1 = WriteMessage(msg)
    question = str(input("Save message? (Y/N)"))
    if question.lower() == "y":
        msg1.write_message(msg1)
    else:
        print("Please re-enter a message")
    