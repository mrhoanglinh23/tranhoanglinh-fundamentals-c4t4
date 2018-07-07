
from turtle import *

speed()
shape("turtle")

# front roof

begin_fill ()
for i in range(3):
    color("red")
    forward(130)
    left(120)

end_fill()

color("black")

# side 
right(90)
forward(150)
left(90)
forward(130)
left(90)
forward(150)

# turtle pen
penup()
goto(15, -150)
pendown()

# front door
begin_fill()

color("blue")
forward(60)
right(90)
forward(30)
right(90)
forward(60)

end_fill()

penup()
goto(80, -20)
pendown()

begin_fill()

for j in range(4):
    color("yellow")
    forward(30)
    left(90)

end_fill()

mainloop()