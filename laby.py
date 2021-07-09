import random
import os
#Make a naturally-generated labyrinth with an exit
#Player can move in all directions
#When player exits the labyrinth the game stops
os.system('clear')

def labypener(mapp,unopened_laby_map):
    laby_map = open(unopened_laby_map)
    redlines = laby_map.readlines() #list with strs. Every str is a line
    labyrinth = [line.split(sep = ',') for line in mapp] #line is (example) '_*_,_*_,_*_,_*_,_*_,_*_,_*_,_*_,_*_,_*_,',
    return labyrinth #labyrinth is list with 10 elements(lists), each containing 10 blocks ('_*_'/'___'(str))
def labycutter(uncut_laby):
    for line in uncut_laby:
        del(line[-1])
    return uncut_laby

def labyprinter(mapp):
    for line in mapp:
        print(''.join(line))

'''
for i in opened:
    print(i)
    input
'''
def location_extractor(mapFileText,loc):
    coordinates = mapFileText[loc]
    replaced_n_coordinates = coordinates.replace('\n','')
    refracted_coordinates = replaced_n_coordinates.split(sep = ',')
    converted_coordinates = []
    for f in refracted_coordinates:
        converted_coordinates.append(int(f))
    return converted_coordinates

laby_map = open('/Users/alex/Library/Mobile Documents/com~apple~CloudDocs/Pygaming/Pybirinth/labyrinth_maps/labyrinth_walls_1.map')
mapFileText = laby_map.readlines()
counter = 0
mapStartsFrom = None
mapEndsOn = None
start = None
end = None
for line in mapFileText:
    if line == 'map_start\n':
        mapStartsFrom = counter + 1
    if line == 'map_end\n':
        mapEndsOn = counter - 1
    if line == 'start\n':
        start = counter + 1
    if line == 'end\n':
        end = counter + 1
    counter = counter + 1
labyrinth = mapFileText[mapStartsFrom:mapEndsOn]
fixed_labyrinth = labypener(labyrinth,'/Users/alex/Library/Mobile Documents/com~apple~CloudDocs/Pygaming/Pybirinth/labyrinth_maps/labyrinth_walls_1.map')
cutted_labyrinth = labycutter(fixed_labyrinth)

start_location = location_extractor(mapFileText,start)
end_location = location_extractor(mapFileText,end)
player = '_Ω_'
while True:
    player_location = start_location.copy()
    game_on = False
    print('Welcome to LABY by Pygaming\n\nEnter 1 to choose map, enter 2 to choose skin, enter 3 to exit')
    choice = input('Time to make the choice! ')
    if choice == '2':
        print('1 for Omega(_Ω_), 2 for Little Boy(_I_), 3 for Fat Man(_O_)')
        skin_choice = input('Time to make the choice! ')
        if skin_choice == '1':
            player = '_Ω_'
            cutted_labyrinth[player_location[0]][player_location[1]] = player
        elif skin_choice == '2':
            player = '_I_'
        elif skin_choice == '3':
            player = '_O_'
    elif choice == '1':
        win = False
        map_choice = input('Choose a map!\n\n1 for Normalndy, 2 for Easyngburg ')
        if map_choice == 1:
            
            laby_map = open('/Users/alex/Library/Mobile Documents/com~apple~CloudDocs/Pygaming/Pybirinth/labyrinth_maps/labyrinth_walls.map')
            mapFileText = laby_map.readlines()
            counter = 0
            mapStartsFrom = None
            mapEndsOn = None
            start = None
            end = None
            for line in mapFileText:
                if line == 'map_start\n':
                    mapStartsFrom = counter + 1
                if line == 'map_end\n':
                    mapEndsOn = counter - 1
                if line == 'start\n':
                    start = counter + 1
                if line == 'end\n':
                    end = counter + 1
                counter = counter + 1
            labyrinth = mapFileText[mapStartsFrom:mapEndsOn]
            fixed_labyrinth = labypener(labyrinth,'/Users/alex/Library/Mobile Documents/com~apple~CloudDocs/Pygaming/Pybirinth/labyrinth_maps/labyrinth_walls.map')
            cutted_labyrinth = labycutter(fixed_labyrinth)

            start_location = location_extractor(mapFileText,start)
            end_location = location_extractor(mapFileText,end)

            cutted_labyrinth[player_location[0]][player_location[1]] = player
            print(f'{player} is player, П is exit, use w/a/s/d keys to move (Enter w to go up, etc).')
            game_on = True
            while game_on == True:
                labyprinter(cutted_labyrinth)
                put = input()
                os.system('clear')
                
                if put == 's':
                    print('BLINK!')
                    if cutted_labyrinth[player_location[0]+1][player_location[1]] == '___':
                        cutted_labyrinth[player_location[0]][player_location[1]] = '___' 
                        player_location[0] = player_location[0] + 1 
                        cutted_labyrinth[player_location[0]][player_location[1]] = player 
                    elif cutted_labyrinth[player_location[0]+1][player_location[1]] ==  '_П_':
                        print('YOU WON')
                        break
                elif put == 'w':
                    print('BLINK!')
                    if cutted_labyrinth[player_location[0]-1][player_location[1]] == '___':
                        cutted_labyrinth[player_location[0]][player_location[1]] = '___'
                        player_location[0] = player_location[0] - 1
                        cutted_labyrinth[player_location[0]][player_location[1]] = player
                    elif cutted_labyrinth[player_location[0]-1][player_location[1]] == '_П_':
                        print('YOU WON')
                        break
                elif put == 'a':
                    print('BLINK!')
                    if cutted_labyrinth[player_location[0]][player_location[1]-1] == '___':
                        cutted_labyrinth[player_location[0]][player_location[1]] = '___' 
                        player_location[1] = player_location[1] - 1 
                        cutted_labyrinth[player_location[0]][player_location[1]] = player
                    elif cutted_labyrinth[player_location[0]][player_location[1]-1] == '_П_':
                        print('YOU WIN')
                        break
                elif put == 'd':
                    print('BLINK!')
                    if cutted_labyrinth[player_location[0]][player_location[1]+1] == '___':
                        cutted_labyrinth[player_location[0]][player_location[1]] = '___'
                        player_location[1] = player_location[1] + 1
                        cutted_labyrinth[player_location[0]][player_location[1]] = player
                    elif cutted_labyrinth[player_location[0]][player_location[1]+1] == '_П_':
                        print('YOU WON')
                        break
        elif map_choice == '2':
                        
            laby_map = open('/Users/alex/Library/Mobile Documents/com~apple~CloudDocs/Pygaming/Pybirinth/labyrinth_maps/labyrinth_walls_1.map')
            mapFileText = laby_map.readlines()
            counter = 0
            mapStartsFrom = None
            mapEndsOn = None
            start = None
            end = None
            for line in mapFileText:
                if line == 'map_start\n':
                    mapStartsFrom = counter + 1
                if line == 'map_end\n':
                    mapEndsOn = counter - 1
                if line == 'start\n':
                    start = counter + 1
                if line == 'end\n':
                    end = counter + 1
                counter = counter + 1
            labyrinth = mapFileText[mapStartsFrom:mapEndsOn]
            fixed_labyrinth = labypener(labyrinth,'/Users/alex/Library/Mobile Documents/com~apple~CloudDocs/Pygaming/Pybirinth/labyrinth_maps/labyrinth_walls_1.map')
            cutted_labyrinth = labycutter(fixed_labyrinth)

            start_location = location_extractor(mapFileText,start)
            end_location = location_extractor(mapFileText,end)

            cutted_labyrinth[player_location[0]][player_location[1]] = player
            print(f'{player} is player, П is exit, use w/a/s/d keys to move (Enter w to go up, etc).')
            game_on = True
            while game_on == True:
                labyprinter(cutted_labyrinth)
                put = input()
                os.system('clear')
                
                if put == 's':
                    print('BLINK!')
                    if cutted_labyrinth[player_location[0]+1][player_location[1]] == '___':
                        cutted_labyrinth[player_location[0]][player_location[1]] = '___' 
                        player_location[0] = player_location[0] + 1 
                        cutted_labyrinth[player_location[0]][player_location[1]] = player 
                    elif cutted_labyrinth[player_location[0]+1][player_location[1]] ==  '_П_':
                        print('YOU WON')
                        break
                elif put == 'w':
                    print('BLINK!')
                    if cutted_labyrinth[player_location[0]-1][player_location[1]] == '___':
                        cutted_labyrinth[player_location[0]][player_location[1]] = '___'
                        player_location[0] = player_location[0] - 1
                        cutted_labyrinth[player_location[0]][player_location[1]] = player
                    elif cutted_labyrinth[player_location[0]-1][player_location[1]] == '_П_':
                        print('YOU WON')
                        break
                elif put == 'a':
                    print('BLINK!')
                    if cutted_labyrinth[player_location[0]][player_location[1]-1] == '___':
                        cutted_labyrinth[player_location[0]][player_location[1]] = '___' 
                        player_location[1] = player_location[1] - 1 
                        cutted_labyrinth[player_location[0]][player_location[1]] = player
                    elif cutted_labyrinth[player_location[0]][player_location[1]-1] == '_П_':
                        print('YOU WIN')
                        break
                elif put == 'd':
                    print('BLINK!')
                    if cutted_labyrinth[player_location[0]][player_location[1]+1] == '___':
                        cutted_labyrinth[player_location[0]][player_location[1]] = '___'
                        player_location[1] = player_location[1] + 1
                        cutted_labyrinth[player_location[0]][player_location[1]] = player
                    elif cutted_labyrinth[player_location[0]][player_location[1]+1] == '_П_':
                        print('YOU WON')
                        break



#print(f'player coordinates = {start_location}')
#print(f'exit coordinates = {end_location}')

#Homevrk = 'get all of this on git, comment and etc, remember the git commands'
#Homevrk = comment changes and push on git and delete useless code

#7.6.2021 Update changes and additions: Player can now change maps, deleted useless code.