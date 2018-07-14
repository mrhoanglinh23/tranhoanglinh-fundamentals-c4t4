from random import randint, choice
from eval import calc
import eval

x = randint(1, 10)
y = randint(1, 10)
op = choice(['+', '-', '*', '/'])

res = calc(x, y, op)

error = choice([-1, 0, 1])

display_res = res + error

print("* " * 10)
print(" {0} {1} {2} = {3}".format(x, op, y, display_res))
print("* " * 10)

ans = input("Y/N: ").lower()

if error == 0:
    if ans == 'y':
        print('Yay')
    elif ans == "n":
        print("Wrong")
else:
    if ans == 'y':
        print("Wrong")
    elif ans == "n":
        print("Yay")