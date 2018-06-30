menu=["T-Shirt", "Sweater"]
while True:
    n=input("Welcome to our shop, what do you want (C, R, U, D)?").lower()
    if n=="r":
        print("Our items: ", *menu, sep=", ")
    elif n=="c":
        item=input("Enter new item:")
        menu.append(item) 
        print(*menu, sep = ", ")
    elif n=="u":
        update = int(input("Update Postion"))
        new = input("New Item:")
        menu[update-1] = new
        print("Our Item:", *menu, sep=",")
    elif n=="d":
        delete = input("Delete postion:")
        del menu[2];
        print("Our items:", *menu, sep=", ")
        break
    
        