import turtle
#star = turtle.Turtle()
 
#star.right(75)
#star.forward(100)
 
#for i in range(4):
    #star.right(144)
    #star.forward(100)
     
#turtle.done()
polygon=turtle.Screen()
polygon.bgcolor("white")
polygon=turtle.Turtle()
#polygon.speed(0)
num_sides=6
side_length=200
angle=360.0/num_sides
polygon.fillcolor("red")
polygon.begin_fill()
for i in range(num_sides):
     polygon.forward(side_length)
     polygon.right(angle)
     polygon.hideturtle()
polygon.end_fill()  
    #polygon.left(angle)
turtle.done()






