import pygame
import json
import sys
import random
import requests

# pygame
pygame.init()
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN])
clock = pygame.time.Clock()
block_size = 50
screen_width_blocks, screen_height_blocks = 19, 13 # must be odd numbers
screen_width, screen_height = block_size * screen_width_blocks, block_size * screen_height_blocks
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.Font(None, 15)
pygame.key.set_repeat(100)

# variables
fps = 60

# graphics
player_icon = {}
player_block = {}
player_icon[0] = pygame.image.load("blueplayer.png").convert_alpha()
player_icon[1] = pygame.image.load("redplayer.png").convert_alpha()
player_block[0]= pygame.image.load("blueblock.png").convert_alpha()
player_block[1] = pygame.image.load("redblock.png").convert_alpha()

# arrays
players = {}
world = {}

# generation
def block_generation():
	world_x, world_y = screen_width_blocks // 2, screen_height_blocks // 2
	request = requests.get(f"http://localhost:8000/world/{screen_width_blocks}/{screen_height_blocks}/{player1.x - world_x}/{player1.y - world_y}")
	output = request.json()["output"]
	for i in range(screen_width_blocks):
		for j in range(screen_height_blocks):
			color = output.pop(0)
			if color is not None and int(color) in [0, 1]:
				screen.blit(player_block[int(color)], (i*block_size, j*block_size))	

# client
username = str(input("Please enter a username:").upper())
player_code = random.randint(1,1000000000000000000000000000000000000)
while True:
	player_color = str(input("Blue (0) or Red (1)?:"))
	if player_color == "0" or player_color == "1":
		player_color = int(player_color)
		break
request = requests.put(f"http://localhost:8000/players/{player_code}/{0}/{0}/{player_color}/{username}")
request = requests.get("http://localhost:8000/players")
players = request.json()["players"]

# classes
class General:
	def screen_control():
		pygame.display.flip()
		pygame.display.update()
		clock.tick(fps)
	
	def game_exit():
		if event.type == pygame.QUIT:
			request = requests.put(f"http://localhost:8000/exit/{player_code}")
			pygame.quit()
			sys.exit()

class Player:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.velocity = 1
		self.color = player_color

	def movement(self):
		if event.key == pygame.K_w:
			self.y -= self.velocity
		elif event.key == pygame.K_s:
			self.y += self.velocity
		elif event.key == pygame.K_a:
			self.x -= self.velocity
		elif event.key == pygame.K_d:
			self.x += self.velocity
		self.place_block()
		request = requests.put(f"http://localhost:8000/players/{player_code}/{self.x}/{self.y}/{player_color}/{username}")	
		
	def display_player(self):
		global image
		request = requests.get("http://localhost:8000/players")
		players = request.json()["players"]
		player_ids = request.json()["player_ids"]
		for x in player_ids:
			pos_x = screen_width / 2 - 25
			pos_y = screen_height / 2 - 25
			screen.blit(player_icon[players[x]["color"]], ((players[x]["cords"][0] - self.x) * block_size + pos_x, (players[x]["cords"][1] - self.y) * block_size + pos_y))
			text = font.render(players[x]["username"], True, (0,0,0))
			text_box = text.get_rect()
			text_box.center = ((players[x]["cords"][0] - self.x) * block_size + 25 + pos_x, (players[x]["cords"][1] - self.y) * block_size - 10  + pos_y)
			screen.blit(text, text_box)
	
	def miscellaneous(self):
		text = font.render("(" + str(self.x) + "," + str(self.y) + ")", True, (0,0,0))
		screen.blit(text, (5,5))
		text = font.render(str(round(clock.get_fps())), True, (0,0,0))
		screen.blit(text, (5,15))	
	
	def place_block(self):
		request = requests.put(f"http://localhost:8000/place/{self.x}/{self.y}/{self.color}")

player1 = Player(0,0) 	

# iteration
while True:
	screen.fill([255,255,255])	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:	
			player1.movement()
			player1.place_block()
		General.game_exit()
	block_generation()
	player1.display_player()
	player1.miscellaneous()
	General.screen_control()

# quit
General.game_exit()
