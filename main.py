import random
import tkinter
from tkinter import messagebox
from turtle import Screen, Turtle
import functions

#Main menu
from GUI import StartGui


StartGui.run_gui()

screen = Screen()
root = tkinter.Tk()
root.withdraw()


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
list_of_turtles = []
rat_shape = ((0, 0), (0, 10), (-10, 20), (-10, 30), (-5, 35), (-10, 35), (-5, 40), (1, 47), (1, 0))
window_width = (root.winfo_screenwidth()) * 0.6
window_height = (root.winfo_screenheight()) * 0.3
margin = 20
rat_length = max(max(rat_shape))
x_position_end = (window_width / 2)
end_line = x_position_end - margin
x_position_start = x_position_end * (-1)

# Prepare running board
screen.setup(width=window_width, height=window_height)
screen.title("Rat Race")
screen.register_shape("rat", rat_shape)
screen.tracer(0)
functions.draw_start_line(x_position_start, rat_length, window_height)
functions.draw_end_line(rat_length, screen)
for color in colors:
    turtle_to_be_added = Turtle("rat")
    turtle_to_be_added.color(color)
    list_of_turtles.append(turtle_to_be_added)

# Set turtle on position
y_position_start = (window_height / 2) - margin
distance = window_height / len(colors)
for turtle in list_of_turtles:
    turtle.penup()
    turtle.goto(x=x_position_start, y=y_position_start)
    y_position_start = y_position_start - distance

# Start the race
winning_rat = ''
screen.tracer(1)
while winning_rat == '':
    for turtle in list_of_turtles:
        turtle.forward(random.randint(0, 5))
        if int(turtle.position()[0]) + rat_length >= end_line - 30:
            winning_rat = turtle.pencolor()
            break
messagebox.showinfo("The end", f"winner is {winning_rat}")
screen.exitonclick()
