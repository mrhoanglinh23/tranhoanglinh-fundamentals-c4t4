from turtle import *

speed()
shape("turtle")


for i in range (3,7):
    for _ in range (i):
        color("red")
        forward (100)
        color("blue")
        left (360/i)
    
       

mainloop()