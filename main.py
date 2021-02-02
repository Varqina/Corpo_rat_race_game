from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
list_of_turtles = []

screen = Screen()
screen.setup(width=500, height=400)
for color in colors:
    turtle_to_be_added = Turtle(shape='turtle')
    turtle_to_be_added.color(color)
    list_of_turtles.append(turtle_to_be_added)




#Set turtle on positions
max_width = -230
height = 180
distance = 360 / len(colors)
for turtle in list_of_turtles:
    turtle.penup()
    turtle.goto(x=max_width, y=height)
    height = height - distance

while True:
    for turtle
screen.exitonclick()