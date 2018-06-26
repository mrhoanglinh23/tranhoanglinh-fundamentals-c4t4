from random import randint

number = randint(1, 100)
print(number)
playing = True
count = 0

while playing:
    guess = int(input("Guess number (1-100): "))
    if guess < number:
        print("Too small :d")
    elif guess > number:
        print("A little too large :( ")
    else:
        print("Bingo")
        break

    count += 1
    if count == 7:
        print("You lose")
        playing = False