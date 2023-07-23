import turtle
     
polygon=turtle.Screen()
polygon.bgcolor("white")
polygon=turtle.Turtle()
#polygon.speed(0)
a=6
b=200
angle=360.0/a
polygon.fillcolor("red")
polygon.begin_fill()
for i in range(a):
     polygon.forward(b)
     polygon.right(angle)
     polygon.hideturtle()
polygon.end_fill()  
    #polygon.left(angle)
turtle.done()






