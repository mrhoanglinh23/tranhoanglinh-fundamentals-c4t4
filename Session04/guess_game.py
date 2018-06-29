print("Guess your number game")
print("Now think of a number (0-100), then press Enter")
input()

print("""
All you have to do is answer to my guess
'c' if my guess is correct
's' if my guess is smaller than your number
'l' if my guess is larger than your number

""")

low = 0
high = 100
count +=1
playing = True

while playing:
    mid = (low +high)//2
    ans = input("Is {0} your number ". format(mid)).upper()

    if ans == "C":
        print("I knew it")
        playing = False
    elif ans == "S":
        low = mid
    elif ans == "L":
        high = mid
    else:
        playing = False

        