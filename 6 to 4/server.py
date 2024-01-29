import socket
import json
import pygame
import time
import sys

# networking
HOST = "127.0.0.1"
PORT = 6969

# pygame
pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 1280,720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 20)
pygame.display.set_caption("6 to 4")

# variables
fps = 10
last_time = time.time() # frame independence
player_color = 1
tile_width, tile_height = 60,60
board_x, board_y = 80,100

# arrays
board = [0,0,0,0,0,0,0,0, ### 0 = unoccupied
         0,0,0,0,0,0,0,0, ### 1 = player 1
         0,0,0,0,0,0,0,0, ### 2 = player 2
         0,0,0,0,0,0,0,0, ### 3 = player 3
         0,0,0,0,0,0,0,0, ### 4 = Player 4
         0,0,0,0,0,0,0,0, ### 
         0,0,0,0,0,0,0,0, ### 
         0,0,0,0,0,0,0,0] ###

tile_cords = []
counters = [6,6,6,6] # players 1 - 4 (6 counters each)

# functions
def board_generator():
    global tile_cords, tile_width, tile_height
    alternate = False
    increment = 0
    x, y = board_x, board_y
    for i in range(0,8): 
        for j in range(0,8):
            try:
                if board[increment] == 0:
                    if alternate == False:
                        pygame.draw.rect(screen, (255,255,255), pygame.Rect(x, y, tile_width, tile_height))
                    elif alternate == True:
                        pygame.draw.rect(screen, (217,217,217), pygame.Rect(x, y, tile_width, tile_height))
                elif board[increment] == 1:
                    pygame.draw.rect(screen, (255,0,0), pygame.Rect(x, y, tile_width, tile_height))
                elif board[increment] == 2:
                    pygame.draw.rect(screen, (0,184,243), pygame.Rect(x, y, tile_width, tile_height))
                elif board[increment] == 3:
                    pygame.draw.rect(screen, (0,188,77), pygame.Rect(x, y, tile_width, tile_height))
                elif board[increment] == 4:
                    pygame.draw.rect(screen, (252,249,0), pygame.Rect(x, y, tile_width, tile_height))
                else:
                    pass
            except IndexError:
                print("incorrect board generator values :/")
            except Exception as exception:
                print("something went wrong:", exception)
            finally:
                tile_cords.append([x,y])
                increment += 1
                x += tile_width
                alternate = not alternate
        alternate = not alternate
        x = board_x
        y += tile_height

# classes
class General():
    def game_exit():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    def screen_control():
        pygame.display.flip()
        pygame.display.update()
        clock.tick(fps)

class Click_detection():
    def place_color(): 
        global player_color, board_x, board_y
        width, height = tile_width, tile_height
        if pos[0] >= board_x and pos[0] <= board_x + tile_width * 8.4:
            if pos[1] >= board_x and pos[1] <= board_x + tile_width * 8.4:
                for i in range(len(board)):
                    if pos[0] >= tile_cords[i][0] and pos[0] <= tile_cords[i][0] + width:
                        if pos[1] >= tile_cords[i][1] and pos[1] <= tile_cords[i][1] + height:
                            if board[i] == 0:
                                if counters[player_color - 1] != 0:
                                    board[i] = player_color
                                    counters[player_color - 1] -= 1
                                    if player_color != 4:
                                        player_color += 1
                                    elif player_color == 4:
                                        player_color = 1
                            elif board[i] == player_color:
                                if counters[player_color - 1] == 0:
                                    board[i] = 0
                                    counters[player_color - 1] += 1
                                

# iterations
while True:
    delta_time = time.time() - last_time
    current_time = time.time()
    delta_time = current_time - last_time
    last_time = current_time 
    screen.fill((75,75,75))

    for event in pygame.event.get():
        General.game_exit() 
        if event.type == pygame.KEYDOWN: 
            pass
        if event.type == pygame.MOUSEBUTTONDOWN: 
            pos = pygame.mouse.get_pos() 
            Click_detection.place_color() 

    # graphics
    pygame.draw.rect(screen, (100,100,100), pygame.Rect(board_x -10, board_y - 10, tile_width * 8 + 20, tile_height * 8 + 20))
    
    board_generator()
    General.screen_control()