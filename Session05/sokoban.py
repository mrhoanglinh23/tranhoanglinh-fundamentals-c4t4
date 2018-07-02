# map

map = {
    "size-x": 5,
    "size-y": 5
}
# player

player = {"x": 3, "y": 4 }
# boxes

boxes = [
    {"x": 1, "y": 1 },
    {"x": 2, "y": 2 },
    {"x": 3, "y": 3 }
]
# destination

for y in range (map["size-y"]):
    for x in range(map["size-x"]):

        box_is_here = False
        player_is_here = False
        dest_is_here = False

        for box in boxes:
            if x == box['x'] and y == box['y']:
                box_is_here = True

        if x == player['x'] and y == player['y']:
            player_is_here = True

        for dest in dest_is_here:
            if x == dest['x'] and y == destroy['y']:
                dest_is_here = True

        if player_is_here == True:
            print("P ", end="")    
        elif box_is_here == True:
            print("B ", end="")
        else:
            print("- ", end="")

        
        u = input("Your move")
        


    print()


