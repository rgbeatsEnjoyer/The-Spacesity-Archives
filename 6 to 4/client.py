import socket
import json
import pygame
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
client_color = ""
client_turn = False

# arrays

