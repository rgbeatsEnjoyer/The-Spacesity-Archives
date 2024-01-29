from manager import AccountsManager
from messanger import Messanger

# program states
states = {"sign_up" : False, "login" : False,
          "contacts_list" : False, "preferences" : False,
          "messanger" : False}

# functions
def choose_state():
    s_or_l = str(input("Sign up or login (S/L):"))
    if s_or_l.lower() == 's':
        states["login"] = False
        states["sign_up"] = True
    elif s_or_l.lower() == 'l':
        states["sign_up"] = False
        states["login"] = True

# main loop
while True:
    choose_state()
    if states["sign_up"]:
        AccountsManager.sign_up()
    elif states["login"]:
        AccountsManager.login()
    else:
        pass