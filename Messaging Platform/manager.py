class AccountsManager:
    def __init__(self):
        pass

    def login():
        username_accepted = False
        password_accepted = False

        while True:
            if username_accepted == False:
                username = str(input("Enter your username:"))
                try:
                    file = open(f"user-data/{username}")
                    file.close()
                    username_accepted = True
                except:
                    print(f"Account {username} does not exist")
            elif username_accepted == True:
                password = str(input("Enter your password:"))
                try:
                    file = open(f"user-data/{username}")
                    check = str(file.readlines(2))
                    if check == password:
                        password_accepted = True
                    else:
                        return "Invalid password"
                    file.close()
                except:
                    return "Something went wrong"
            else:
                pass

    def sign_up():
        username_complete = False
        password_complete = False
        def input_function(info, user_or_pass):
            if len(info) < 3 or len(info) > 20:
                return "Please enter a username between 3-20 characters"
            elif len(info) > 3 and len(info) < 20:
                user_or_pass = True
            else:
                return "Error, please try again"

        while True:
            if username_complete == False:
                username = str(input("Please enter a username (lowercase):"))
                input_function(username, username_complete)
            elif username_complete:
                password = str(input("Please enter a password:"))
                input_function(password, password_complete)
            else:
                pass
                
            
