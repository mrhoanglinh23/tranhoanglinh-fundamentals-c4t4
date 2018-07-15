from turtle import *

speed(0)
color('blue')
def draw_star(x, y, length):
    for i in range(100):
        import random
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        length = random.randint(3, 10)
        draw_star(x, y, length)

mainloop()
