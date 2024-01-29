"""
Class Testing

Player enter details and output player color using pygame

When player has customized his character, game then starts up
"""
import pygame, sys
from pygame.locals import *

# Variables
player_ready = False
R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
s_x = 100
s_y = 100
s_w = 50
s_h = 50

# Classes
class Player:
    def __init__(self,username,level,color):
        self.username = "Undefined"
        self.level = "Undefined"
        self.color = "Undefined"

    def username_assignment():
        assignment = str(input("What do you wanna be called? Only use letters:"))
        if assignment: # If something has been input
            username = assignment
            print("Welcome",username)
        else:
            print("Username not valid")

        return assignment

    def level_assignment():
        assignment = int(input("What is your level? Enter a number:"))
        if assignment:
            level = assignment
            print("Your level is",level)
        else:
            print("Level not valid")

        return assignment
    
    def choose_color():
        global color
        assignment = str(input("What color do you wanna be? Red (R), Green (G) or Blue (B):"))
        if assignment == R or G or B:
            color = assignment
            print("You will be",color)
        
        return assignment

    def player_display():
        global player_ready
        if color != "Undefined":
            player_ready = True
            
# Assignment
game_state = Game()
p1 = Player
Player.username_assignment()
Player.level_assignment()
Player.choose_color()

# Initialize
pygame.init()
clock = pygame.time.Clock()

# Display
screen_width,screen_height = 500,500
screen = pygame.display.set_mode((screen_width,screen_height))

# Window
pygame.display.set_caption("Classes Test")

# Functions
def screen_control():
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

class Game:
    def __init__(self):
        self.state = 'game_waiting'

    def game_waiting(self): # Waits for player to customize
        if player_ready == False:
            screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            screen_control()
            
    def main_loop(self): 
        if player_ready:
            screen.fill((30,30,30))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.draw.rect(screen,(255,255,255),pygame.Rect(s_x,s_y,s_w,s_h))
            screen_control()

    def state_handler(self):
        if self.state == 'game_waiting':
            self.game_waiting()
        elif self.state == 'game_main':
            self.main_loop()
        




# Game Loop
while True:
    Game.state_handler()
    
    
