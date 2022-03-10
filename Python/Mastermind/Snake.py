import readchar
import os
import random

#Info
'''
# cursors
UP = "\x1b\x5b\x41"
DOWN = "\x1b\x5b\x42"
LEFT = "\x1b\x5b\x44"
RIGHT = "\x1b\x5b\x43"

# common
LF = "\x0d"
CR = "\x0a"
ENTER = "\x0d"
BACKSPACE = "\x08"
SUPR = ""
SPACE = "\x20"
ESC = "\x1b"


# Symbols Unicode I like
⊞ \u229E
♠   ☼   ♥   ♦   ȸ   ȹ	
₠	₡	₢	₣	₤	₥	₦	₧	₨	₩	₪	₫	€	₭	₮	₯
₰	₱	₲	₳	₴	₵	₶	₷	₸	₹	₺	₻	₼	₽	₾	₿
◙ 
█
▲   ►   ▼   ◄
'''

# Constants 

TITLE_GAME = """                                          
\t███████╗███╗   ██╗ █████╗ ██╗  ██╗███████╗
\t██╔════╝████╗  ██║██╔══██╗██║ ██╔╝██╔════╝
\t███████╗██╔██╗ ██║███████║█████╔╝ █████╗  
\t╚════██║██║╚██╗██║██╔══██║██╔═██╗ ██╔══╝  
\t███████║██║ ╚████║██║  ██║██║  ██╗███████╗
\t╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
""" 
FINAL_MESSAGE_GAME_OVER = """                                                                          
\t ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
\t██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
\t██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
\t██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
\t╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
\t ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝                                                                          
"""

FINAL_MESSAGE_ESC = """
\t██████╗ ██╗   ██╗███████╗
\t██╔══██╗╚██╗ ██╔╝██╔════╝
\t██████╔╝ ╚████╔╝ █████╗  
\t██╔══██╗  ╚██╔╝  ██╔══╝  
\t██████╔╝   ██║   ███████╗
\t╚═════╝    ╚═╝   ╚══════╝                       
"""

POSX = 0
POSY = 1


title_pic = [ list(row) for row in TITLE_GAME.split("\n") ]


# Defining Map Size according to Title
MAP_WIDTH = int(len(title_pic[0])/3) # dividing by 3 for fixinig with the title width
MAP_HEIGTH = 20

## CONSTANT PLAYER
POSX_PLAYER_INITIAL = random.randint(0, MAP_WIDTH-1)
POSY_PLAYER_INITIAL = random.randint(0, MAP_HEIGTH-1)
INITIAL_POSITION_PLAYER = [POSX_PLAYER_INITIAL,POSY_PLAYER_INITIAL]

## CONSTANT OBJECTS
NUMBER_OF_OBJECTS = 10

## CONSTANTS OBSTACLES
NUMBER_OF_OBSTACLES = NUMBER_OF_OBJECTS * 3

# Initialazing variables


## Player variables
player_position = INITIAL_POSITION_PLAYER
player_image = "▲" # A man 
posx_player = POSX_PLAYER_INITIAL
posy_player = POSY_PLAYER_INITIAL

## tail of player variables
tail = []
tail_image = "◙"

## Objects in map variables
map_objects = []
food_image = "☼"

## Obstacles variables
map_obstacle = []
obstacle_image ="x"

'''
#Understanding map drawing
for x in range(MAP_WIDTH):
    for y in range(MAP_LENGTH):
        print(" ({},{}) ".format(x,y),end="")

    print("\n")   
'''

#Initialazing Game
game_on = True
score = 0

while game_on:

    # Printing initial game
    print(TITLE_GAME)
    print("\tScore: {}".format(score))
    print("\tPosition on Map: {}\n".format(player_position))
    print("\tPress Esc to exit...")
    # print("Tail position vector {}".format(tail))

    # Generating obstacles in map

    while len(map_obstacle) < NUMBER_OF_OBSTACLES:
        new_position = [random.randint(0,MAP_WIDTH-1),random.randint(0,MAP_HEIGTH-1)]
        if new_position not in map_obstacle \
            and new_position not in map_objects \
                and new_position not in tail \
                    and new_position != player_position:

            map_obstacle.append(new_position)

    # Generating objects in map

    while len(map_objects) < NUMBER_OF_OBJECTS:
        new_position = [random.randint(0,MAP_WIDTH-1),random.randint(0,MAP_HEIGTH-1)]
        if new_position not in map_objects \
            and new_position not in map_obstacle \
                 and new_position not in tail \
                    and new_position != player_position:

            map_objects.append(new_position)

    # print("Objects position vector {}".format(map_objects))    
    
    # Drawing a character for each pixel

    # Border por map

    print("\t╔",end="")
    print("═"*(MAP_WIDTH)*3,end="")
    print("╗")


    for y in range(MAP_HEIGTH):
        
        # Border of Box
        print("\t║", end="")

        for x in range(MAP_WIDTH):

            #Reinitialazing pixel to draw before drawing map
            pixeltodraw = " "

            # Drawing obstacle in map
            for obstacle in map_obstacle:
                if obstacle[POSX] == x and obstacle[POSY] == y:
                    pixeltodraw = obstacle_image
                # Deleting obstacle eaten by player
                if player_position == obstacle:
                    
                    game_on = False
                    message = FINAL_MESSAGE_GAME_OVER
                    

            # Drawing food in map
            for food in map_objects:
                if food[POSX] == x and food[POSY] == y:
                    pixeltodraw = food_image
                # Deleting food eaten by player
                if player_position == food:
                    
                    map_objects.remove(player_position)
                    score += 1
                

            # Drawing Player position
            if player_position[POSX] == x and player_position[POSY] == y:
                pixeltodraw = player_image

            # Drawing tail position
            for piece in tail:
                if piece[POSX] == x and piece[POSY] == y:
                    pixeltodraw = tail_image
                
            print(" {} ".format(pixeltodraw),end="")
            #print(" (x={} {} y={}) ".format(x,pixeltodraw,y),end="")

        # This print is for making a new line
        print("║")

    # Drawing bottom margin
    print("\t╚",end="")
    print("═"*(MAP_WIDTH)*3,end="")
    print("╝")

    # Updating tail position when score is greater than 0
    if score > 0:
        tail.insert(0,player_position.copy())
        tail = tail[:score]
    else:
        tail = []

    # Input movement of player

    movement_key = readchar.readkey()

    if movement_key == "\x1b\x5b\x41": #UP
        player_position[POSY] = (player_position[POSY]-1) % MAP_HEIGTH
        player_image = "▲"
    elif movement_key == "\x1b\x5b\x42": #DOWN
        player_position[POSY] = (player_position[POSY]+1) % MAP_HEIGTH
        player_image = "▼"
    elif movement_key == "\x1b\x5b\x44": #LEFT
        player_position[POSX] = (player_position[POSX]-1) % MAP_WIDTH
        player_image = "◄"
    elif movement_key == "\x1b\x5b\x43": #RIGHT
        player_position[POSX] = (player_position[POSX]+1) % MAP_WIDTH
        player_image = "►"
    elif movement_key == "\x1b":
        game_on = False
        message = FINAL_MESSAGE_ESC

    # Verifing if player touch obstacle or tail
    if player_position in tail:
        game_on = False
        message = FINAL_MESSAGE_GAME_OVER
    
    os.system("cls")


os.system("cls")
print("\n\tFinal Score: {}".format(score))
print(message)





