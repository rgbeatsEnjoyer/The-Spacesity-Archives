# Game State changer

class game_states:
    def __init__(self):
        gamestate = 'main_menu'

    def mainmenu(self):
        print("Main Menu")

    def ingame(self):
        print("In Game")

    def statehandler(self):
        if gamestate == 'main_menu':
            gamestate = 'In Game'

while True:
    game_states.statehandler