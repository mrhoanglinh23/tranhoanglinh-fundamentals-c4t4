from random import randint


n = randint(1, 100)
print(n)
playing = True
count = 0


while playing:
    guess = int(input((n), "Is your number: "))
    if guess < n:
        print("Smaller than your number")
    elif guess > n:
        print("Large than your number")
    else:
        print("I knew it")
        break
