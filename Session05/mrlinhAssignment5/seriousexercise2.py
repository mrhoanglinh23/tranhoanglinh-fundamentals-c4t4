price = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for key in price:
    print(key)
    print ("price:{} ".format(price[key]))
    print ("stock:{} ".format(stock[key]))

total = 0
for total in price: 
    total = 4 * 6
    print("Total:", total)
    