#print("Hi there, here you favorite things so far")
#menu = ["death note", "netflix", "teaching"]
#print(*menu, sep=", ")

#list = input("Name one thing you want to add? ")
#menu.append("coding")

#print(*menu, sep=", ")
#Test 2

pos = int(input("postion you want to update: "))
update_favs = input("Your replacing fav: ")


favs = ["death note", "netflix", "teaching"]
print(favs)
favs[pos - 1] = update_favs

for index, fav in enumerate(favs):
     print(index + 1, fav, sep=". ")
print("* " * 20)

