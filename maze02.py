import readchar
import random
import os
#Posiciones
POS_X = 0 #inicializa en cero
POS_Y = 1 # inicializa en 1
MAP_WIDTH = 20 #Ancho del mapa
MAP_HEIGTH = 15 # alto del mapa
NUM_OF_MAP_OBJECTS = 11 #Tamaño de la cola

####Este es el mapa
obstacle_definition = """\
###########################
                       ####
####################   ####
####################   ####
###########
###################  ######
###############         ###
#######            ########
##############
#####################   ###
#####     ########        #
########                ###
#######   #########
#####    ##########    ####
###########################\
"""

my_position = [6, 3] #inicializacion del mapa
tail_length = 0 #incializa en cero la cola
tail = []   #cole en vacio
map_objects = [] #conteo del objetivos del mapa

end_game = False #inicializa el juego en falso
died = False #Conre el numero de muertes

# Create obstacle map
#contea los caracteres y al final de line hace un corte
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
print(obstacle_definition)

# Main Loop
while not end_game:
    #os.system("cls")
    # Generate random objects on the map
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGTH)]

        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)

    # Draw map
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGTH):
        print("|", end="")
        
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"
                    tail_in_cell = tail_piece
            
            
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1

                if tail_in_cell:
                    end_game = True
                    died = True
            
            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"


            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")       

    # Ask user where he wants to move 
    #direction = input("¿Donde te quieres mover? [WASD]: ")
    direction = readchar.readchar().decode()

    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGTH
    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGTH
    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        end_game = True

    os.system("cls") 

if died:
    print("Has muerto!")