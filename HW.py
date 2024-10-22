import turtle
turtle.Screen().bgcolor("Aqua")
turtle.Screen().screensize(300,300)
square=turtle.Turtle()
sidesum=4
sidelen=80
angle=360/sidesum
for i in range (sidesum):
    turtle.forward(sidelen)
    turtle.right(angle)