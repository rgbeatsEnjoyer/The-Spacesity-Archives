import sys
import json
import time
import pygame
from pygame.locals import *
from pygame import mixer

# miscellaneous
pygame.init()
clock = pygame.time.Clock()
count = 0
screen_width,screen_height = 350,600
lastTime = time.time()
monitor_size = [pygame.display.Info().current_w,pygame.display.Info().current_h]
screen = pygame.display.set_mode((screen_width, screen_height))
fullscreen = False
font = pygame.font.Font(None, 25)

# data
states = {"mainMenu" : True, "optionsMenu" : False, "levelSelector" : False,
    "current_level" : False, "music_enabled" : True,
    "sound_enabled" : True, "pauseMenu" : False, "previous_state" : ""}
levels = [[]]
current_level = 0
blocks = []
cords = []
clicked = []
spawned = []
target_x = 125
increment = -1
player_x, player_y = 125, 475
attempts = [0]
successes = [0]
blocks_destroyed = 0
misspress = False
attempt_added = False
fps = 60
last_time = time.time()
try:
    with open('data//MusicGameLevel1.txt')as level_data:
        levels[current_level] = json.load(level_data)
except:
    print("No levels found!")

for i in range(len(levels[current_level])):
    spawned.append(0)

# graphics
player = pygame.image.load("images//MusicGameBlock.png").convert()
title_image = pygame.image.load("images//MusicGameTitle.png").convert()
logo_image = pygame.image.load("images//MusicGameLogo.png").convert()
play_button = pygame.image.load("images//MusicGamePlayButton.png").convert()
options_button = pygame.image.load("images//MusicGameOptionsButton.png").convert()
return_button = pygame.image.load("images//MusicGameReturnButton.png").convert()
musicsettings_image = pygame.image.load("images//MusicGameMusicSettings.png").convert()
soundsettings_image = pygame.image.load("images//MusicGameSoundSettings.png").convert()
onstate_button = pygame.image.load("images//MusicGameOnState.png").convert()
offstate_button = pygame.image.load("images//MusicGameOffState.png").convert()
level_button = pygame.image.load("images//MusicGameLevelButtonPlaceholder.png").convert()
settings_button = pygame.image.load("images//MusicGameSettingsButton.png").convert()
background = pygame.image.load("images//MusicGameBackground.png").convert()
resume_button = pygame.image.load("images//MusicGameResumeButton.png").convert()
home_button = pygame.image.load("images//MusicGameHomeButton.png").convert()
block_images = []

for i in range(len(levels[0])):
    if levels[current_level][i][4] == 1:
        block_images.append(pygame.image.load("images//MusicGameBlockRed.png").convert())
    elif levels[current_level][i][4] == 2:
        block_images.append(pygame.image.load("images//MusicGameBlockGreen.png").convert())
    elif levels[current_level][i][4] == 3:
        block_images.append(pygame.image.load("images//MusicGameBlockBlue.png").convert())
    else:
        print("Invalid level design: Presumably RGB block assignment out of range")

# display
pygame.display.set_caption("Music Game v1.0")
pygame.display.set_icon(logo_image)

# functions
def screen_control():
    pygame.display.flip()
    pygame.display.update()
    clock.tick(fps)

def game_exit():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def fullscreen_function():
    global fullscreen, screen
    if event.key == K_f:
        fullscreen = not fullscreen
        if fullscreen:
            screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
        else:
            screen = pygame.display.set_mode((screen_width, screen_height))

# classes
class user_interface():
    def switch_to_previous_state(states, current_state, prev_state):
        if states["previous_state"] == prev_state:
            states[current_state] = False
            time.sleep(0.1)
            states[prev_state] = True

    def state_click_detection(startvertex_x, startvertex_y, width, height, states, state1, state2, pos, tag):
        if pos[0] >= startvertex_x and pos[0] <= startvertex_x + width:
            if pos[1] >= startvertex_y and pos[1] <= startvertex_y + height:
                if tag == 0 and states["pauseMenu"]:
                    user_interface.switch_to_previous_state(states, "pauseMenu", "current_level")
                else:
                    states["previous_state"] = state1
                    states[state1] = not states[state1]
                    time.sleep(0.1)
                    states[state2] = not states[state1]

    def click_detection_settings(startvertex_x, startvertex_y, width, height, states, single_state, pos):
        if pos[0] >= startvertex_x and pos[0] <= startvertex_x + width:
            if pos[1] >= startvertex_y and pos[1] <= startvertex_y + height:
                states[single_state] = not states[single_state]
                
    def state_enabler(states, single_state, display_x, display_y, image1, image2):
        if states[single_state] == True:
            screen.blit(image1, (display_x, display_y))
        else:
            screen.blit(image2, (display_x, display_y))

class player_mechanics():
    def movement_mechanic():
        global player_x
        global target_x
        if player_x == target_x:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                target_x = player_x - 100
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                target_x = player_x + 100
            
    def smooth_movement_mechanic():
        global player_x
        global target_x
        if player_x != target_x and target_x < player_x:
            player_x -= 10 * delta
            if player_x < target_x:
                player_x = target_x
        if player_x != target_x and target_x > player_x:
            player_x += 10 * delta
            if player_x > target_x:
                player_x = target_x

    def side_barrier():
        global player_x
        global target_x
        if target_x < 25:
            player_x = 25
            target_x = player_x
        elif target_x > 225:
            player_x = 225
            target_x = player_x

class level_constructor():
    def cords_assignment(x_cord, y_cord):
        global increment
        cords.append([x_cord, y_cord])
        spawned[increment] = 1
        increment += 1
        clicked.append(0)
        
    def block_spawning():
        global increment, current_level
        if len(levels[current_level]) > increment:
            if count >= levels[current_level][increment][1]*fps:
                if spawned[increment] == 0:
                    blocks.append(increment)
                    if levels[current_level][increment][2] == 1:
                        level_constructor.cords_assignment(25,-100)
                    elif levels[current_level][increment][2] == 2:
                        level_constructor.cords_assignment(125,-100)
                    elif levels[current_level][increment][2] == 3:
                        level_constructor.cords_assignment(225,-100)
            elif increment == -1:
                if spawned[increment] == 0:
                    increment += 1
    
    def block_falling():
        for i in range(len(cords)):
            if len(cords) > 0:
                if clicked[i] == 0:
                    cords[i][1] = (levels[current_level][i][3] * delta) + cords[i][1]
            else:
                print("All blocks have been destroyed!")
    
    def defeat_check():
        for i in range(0, len(cords)):
            if len(cords) > 0:
                if cords[i][1] + 100 > 600:
                    game_restart(1)
    
    def victory_check():
        global successes
        if blocks_destroyed == len(levels[current_level]):
            print("Level Complete!")
            successes[0] += 1
            print("Successes:", successes[0])
            time.sleep(2)
            game_restart(0)
            states["levelSelector"] = True

def game_restart(attempt_check):
    global count, increment, target_x, player_x, player_y, blocks_destroyed, attempt_added
    states["current_level"] = False
    count = 0
    player_x, player_y = 125, 475
    target_x = 125
    increment = -1
    blocks_destroyed = 0
    for i in range(0, len(cords)):
        cords[i][1] = 0
    for i in range(len(clicked)):
        clicked[i] = 0
    for i in range(len(spawned)):
        spawned[i] = 0
    for i in reversed(range(len(cords))):
        del cords[i]
    states["levelSelector"] = True
    if attempt_added == False:
        if attempt_check == 1:
            attempts[0] += 1
        attempt_added = True
    if attempt_check == 1:
        print("Attempts:", attempts[0])

def block_player_collision():
    def collision_math(check_number):
        global blocks_destroyed, misspress
        previous = blocks_destroyed
        for i in range(0, len(cords)):
            if cords[i][0] + 99 >= player_x and cords[i][0] <= player_x + 99:
                if cords[i][1] + 99 >= player_y and cords[i][1] <= player_y + 99:
                    if clicked[i] == 0:
                        if levels[current_level][i][4] == check_number:
                            clicked[i] = 1
                            blocks_destroyed += 1
                        
        if blocks_destroyed == previous:
            misspress = True

    if event.key == pygame.K_1 or event.key == pygame.K_j:
        collision_math(1)
    elif event.key == pygame.K_2 or event.key == pygame.K_k:
        collision_math(2)
    elif event.key == pygame.K_3 or event.key == pygame.K_l:
        collision_math(3)

def misspress_detector():
    global misspress
    if misspress == True:
        misspress = False
        print("You didn't press on a block!")
        game_restart(1)

# iterations
while True:
    delta = time.time() - last_time
    delta *= fps
    last_time = time.time()
    screen.fill((0,0,0))
    if states["previous_state"] == "pauseMenu":
        game_restart(0)
    if states["mainMenu"]:
       	fps = 30
        for event in pygame.event.get():
            game_exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Interface actions
                pos = pygame.mouse.get_pos()

                user_interface.state_click_detection(15, 180, 170, 70, states, "mainMenu", "levelSelector", pos, 0)
                user_interface.state_click_detection(15, 265, 170, 70, states, "mainMenu", "optionsMenu", pos, 1)
            
            if event.type == pygame.KEYDOWN:
                fullscreen_function()
            
        screen.blit(play_button, (15, 180)) # screen.blit = Display graphics
        screen.blit(options_button, (15, 265))
        screen.blit(title_image, (15, 15))
        
    elif states["levelSelector"]:
        fps = 30
        for event in pygame.event.get():
            game_exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                user_interface.state_click_detection(5, 5, 30, 30, states, "levelSelector", "mainMenu", pos, 0)
                user_interface.state_click_detection(25, 50, 300, 150, states, "levelSelector", "current_level", pos, 1)
                user_interface.state_click_detection(25, 215, 300, 150, states, "levelSelector", "current_level", pos, 1)
                user_interface.state_click_detection(25, 380, 300, 150, states, "levelSelector", "current_level", pos, 1)
            
            if event.type == pygame.KEYDOWN:
                fullscreen_function()
        
        screen.blit(return_button, (5, 5))
        screen.blit(level_button, (25, 50))
        screen.blit(level_button, (25, 215))
        screen.blit(level_button, (25, 380))

    elif states["optionsMenu"]:
        fps = 30
        for event in pygame.event.get():
            game_exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                user_interface.state_click_detection(5, 5, 30, 30, states, "optionsMenu", "mainMenu", pos, 0)
                user_interface.click_detection_settings(185, 60, 150, 50, states, "music_enabled", pos)
                user_interface.click_detection_settings(185, 125, 150, 50, states, "sound_enabled", pos)
            
            if event.type == pygame.KEYDOWN:
                fullscreen_function()

        user_interface.state_enabler(states, "music_enabled", 185, 60, onstate_button, offstate_button)
        user_interface.state_enabler(states, "sound_enabled", 185, 125, onstate_button, offstate_button)
        screen.blit(return_button, (5, 5))
        screen.blit(musicsettings_image, (15,60))
        screen.blit(soundsettings_image, (15,125))
    
    elif states["current_level"]: # Standard level
        fps = 60
        deltaTime = time.time() - lastTime
        deltaTime *= 60
        lastTime = time.time()
        for event in pygame.event.get():
            game_exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Interface actions
                pos = pygame.mouse.get_pos()

                user_interface.state_click_detection(160, 5, 30, 20, states, "current_level", "pauseMenu", pos, 0)
            
            if event.type == pygame.KEYDOWN:
                player_mechanics.movement_mechanic()
                block_player_collision()
                fullscreen_function()
                
        level_constructor.block_spawning()
        level_constructor.block_falling()
        
        screen.blit(background, (0, 0))
        for i in range(len(cords)):
            if clicked[i] == 0:
                screen.blit(block_images[i], (cords[i][0], cords[i][1]))
            else:
                pass
        screen.blit(player, (player_x, player_y))
        screen.blit(settings_button, (160,5))

        player_mechanics.side_barrier()
        player_mechanics.smooth_movement_mechanic()
        count += delta
        level_constructor.defeat_check()
        level_constructor.victory_check()
        misspress_detector()
        attempt_added = False

    elif states["pauseMenu"]:
        fps = 30
        for event in pygame.event.get():
            game_exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                user_interface.state_click_detection(90, 100, 170, 70, states, "pauseMenu", "previous_state", pos, 0)
                user_interface.state_click_detection(90, 195, 170, 70, states, "pauseMenu", "mainMenu", pos, 1)
            
            if event.type == pygame.KEYDOWN:
                fullscreen_function()
            
        screen.blit(resume_button, (90, 100))
        screen.blit(home_button, (90, 195))
    
    screen_control()
