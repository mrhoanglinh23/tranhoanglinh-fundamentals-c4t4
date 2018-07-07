print("""
Hello!, Welcome to the Sokoban Demo, here is my game i was creating
I dont know can you beat 2 level yet
Press Enter?
""")
input()

print("""
Well, you are lucky then, 
i make to you 2 level, you have to beat 2 level and do not cheater
Are you ready? Press Enter
""")

input()

print("Ok then, let's go")
print("Level 1")
# map

map = {
    "size_x": 7,
    "size_y": 7
}
# player

player = {"x": 3, "y": 5 }

# boxes

boxes = [
    {"x": 1, "y": 3 },
    {"x": 2, "y": 3 }
]
# destination

destination = [
    {"x": 2, "y": 1 },
    {"x": 3, "y": 1 }

]

obstacle = [
    {"x": 1, "y": 2 },
    {"x": 2, "y": 2 }
]

playing = True

check = True
while playing:
    for y in range (map["size_y"]):
            for x in range(map["size_x"]):
                box_is_here = False
                for box in boxes:
                    if x == box['x'] and y == box['y']:
                        box_is_here = True
                
                player_is_here = False
                if x == player['x'] and y == player['y']:
                    player_is_here = True

                destination_is_here = False
                for dest in destination:
                    if x == dest['x'] and y == dest['y']:
                        destination_is_here = True
                
                obstacle_is_here = False
                for obs in obstacle:
                    if x == obs['x'] and y == obs['y']:
                        obstacle_is_here = True


                if player_is_here == True:
                    print("P ", end="")    
                elif box_is_here == True:
                    print("B ", end="")
                elif destination_is_here == True:
                    print("D ", end="")
                elif obstacle_is_here == True:
                    print("O ", end="")
                else:
                    print("- ", end="")

            print()

    win = True
    for box in boxes:
        if box not in destination:
            win = False

    if win == True:
        print("You Win")
        break
    #input
    move = input("Your move: ").lower()

    dx = 0
    dy = 0
    dz = 0

    if move == 'w':
        dy = -1
    elif move == 's':
        dy = 1
    elif move == 'a':
        dx = -1
    elif move == 'd':
        dx = 1

    
    else:
        print("End Game")
        playing = False
        
    # player
    if 0 <= player['x'] + dx < map['size_x'] and 0 <= player['y'] + dy < map['size_y'] :
            player['x'] += dx
            player['y'] += dy
    elif 0 > box['x'] - dx < map['size_x'] and 0 > box['y'] - dy < map['size_y'] :
            box['x'] += dx
            box['y'] += dy
    
    #boxes
    for box in boxes:
        if box['x'] == player['x'] and box['y'] == player['y']:
            box['x'] += dx
            box['y'] += dy


    for obs in obstacle:
        if obs['x'] == box['x'] and obs['y'] == box['y']:
            print("Oops, Obstacle")

