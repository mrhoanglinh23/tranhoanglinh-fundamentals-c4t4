from turtle import *

n = 10

speed(-1)
shape("turtle")
color("green")

for i in range(n):
    forward(100)
    left(360/n)

mainloop()