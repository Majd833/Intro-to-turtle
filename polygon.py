import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().screensize(300, 400)
polygon=turtle.Turtle()
sidenum=6
angle=360/sidenum
sideleng=70
for i in range(sidenum):
    turtle.forward(sideleng)
    turtle.right(angle)
turtle.done()
