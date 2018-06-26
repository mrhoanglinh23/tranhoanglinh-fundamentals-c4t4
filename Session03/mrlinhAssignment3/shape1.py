from turtle import *


for i in range(3, 8):
    for j in range(i):
        forward(100)
        left(360/i)

    
mainloop()