# map

map = {
    "size_x": 5,
    "size_y": 5
}
# player

player = {"x": 2, "y": 4 }

# boxes

boxes = [
    {"x": 1, "y": 1 },
    {"x": 2, "y": 2 },
    {"x": 3, "y": 3 }
]
# destination

destination = [
    {"x": 2, "y": 1 },
    {"x": 3, "y": 2 },
    {"x": 4, "y": 3 }
]

playing = True

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

            if player_is_here == True:
                print("P ", end="")    
            elif box_is_here == True:
                print("B ", end="")
            elif destination_is_here == True:
                print("D ", end="")
            else:
                print("- ", end="")

        print()
    #end of print map

    #check win
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

    if move == 'w':
        dy = -1
    elif move == 's':
        dy = 1
    elif move == 'a':
        dx = -1
    elif move == 'd':
        dx = 1
    else:
        print("No")
        
    
    if 0 <= player['x'] + dx < map['size_x'] and 0 <= player['y'] + dy < map['size_y'] :
            player['x'] += dx
            player['y'] += dy
    
    for box in boxes:
        if box['x'] == player['x'] and box['y'] == player['y']:
            box['x'] += dx
            box['y'] += dy

            