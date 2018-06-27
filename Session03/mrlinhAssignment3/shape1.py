from turtle import *


for i in range(2, 8):
    for j in range(i):
        forward(100)
        left(360/i)
    if i == 2:
        color("red")
    elif i == 3:
        color("blue")
    elif i == 4:
        color("purple")
    elif i == 5:
        color("yellow")
    elif i == 6:
        color("grey")
    
mainloop()