import random
from tkinter import messagebox
from turtle import Screen, Turtle

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
list_of_turtles = []
rat_shape = ((0, 0), (0, 10), (-10, 20), (-10, 30), (-5, 35), (-10, 35), (-5, 40), (1, 47), (1, 0))
window_width = 1500
window_height = 400

screen = Screen()
screen.setup(width=window_width, height=window_height)
screen.register_shape("rat", rat_shape)





for color in colors:
    turtle_to_be_added = Turtle("rat")
    turtle_to_be_added.color(color)
    list_of_turtles.append(turtle_to_be_added)




#Set turtle on positions
margin = 20
x_position_start = (window_width/2) * (-1)
y_position_start = (window_height/2) - margin
distance = window_height / len(colors)
for turtle in list_of_turtles:
    turtle.penup()
    turtle.goto(x=x_position_start, y=y_position_start)
    y_position_start = y_position_start - distance
user_bet = screen.textinput(title="Make your bet", prompt="provide turtle color")
winning_color = ''
while winning_color == '':
    for turtle in list_of_turtles:
        turtle.forward(random.randint(0, 10))
        if int(turtle.position()[0]) >= 230:
            winning_color = turtle.pencolor()
            break
messagebox.showinfo("The end", f"winner is {winning_color}")
screen.exitonclick()