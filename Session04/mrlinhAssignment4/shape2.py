from turtle import *

speed(-1)
color("blue")
for i in range(30):
    for j in range(4):
        forward(i * 4-1)
        right(90)
    left(20)

mainloop()

