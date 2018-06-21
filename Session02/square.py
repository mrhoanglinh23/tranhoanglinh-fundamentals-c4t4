from turtle import *
speed(-1)
shape("turtle")
color("green")
for i in range(3):
    for _ in range(4):
        forward(10 + i * 20)
        left(90)
    right(60)
    forward(19)

mainloop()