from random import choice
words = ["champion", "dungeon", "vodka"]

word = choice(words)
chars = list(word)

while len(chars) > 0:
    rand_char = choice(chars)
    print(rand_char, end=" ")
    chars.remove(rand_char)

print()

while True:
    ans = input("Your answer: ")
    if ans == word:
        print("Hurra")
        break
    else:
        print("Wrong aaaaaaaaaaaahhhh")
        
