import redis
import json
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
r = redis.Redis(host='127.0.0.1', port=6379, password="6379", db=0)

@app.get("/players")
def get_players():
	player_ids = r.smembers("players")
	players = {}
	for x in player_ids:
		players[x] = json.loads(r.get(x))
	return {"player_ids" : player_ids, "players" : players}

@app.get("/world/{screen_width_blocks}/{screen_height_blocks}/{x}/{y}")
def get_world(screen_width_blocks : int, screen_height_blocks : int, x: int, y: int):
	world = {}
	coords_list = []
	for i in range(screen_width_blocks):
		world[i] = {}
		for j in range(screen_height_blocks):
			coords_list.append(f"{i + x}:{j + y}")
	positions = {}
	output = r.hmget("world", coords_list)	
	return {"output":output, "positions":positions}

@app.put("/players/{player_code}/{x}/{y}/{player_color}/{username}")
def put_players(player_code : str, x : int, y : int, player_color : int, username : str):
	player_ids = r.smembers("players")
	if str(player_code) not in player_ids:
		r.sadd("players", player_code)
	r.set(int(player_code), json.dumps({"username" : str(username), "cords" : (x,y), "color" : player_color}))
	
@app.put("/exit/{player_code}")
def remove_players(player_code : str):
	r.srem("players", 1, player_code)

@app.put("/place/{x}/{y}/{color}")
def place_block(x : int, y : int, color : int):
	r.hset("world", f"{x}:{y}", color)
