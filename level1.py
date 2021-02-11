import random
import sys
import tkinter
from time import sleep

import PySimpleGUI as sg
from turtle import Screen, Turtle

import CommonStrings
import functions

screen = Screen()
root = tkinter.Tk()
root.withdraw()
rat_shape = ((0, 0), (0, 10), (-10, 20), (-10, 30), (-5, 35), (-10, 35), (-5, 40), (1, 47), (1, 0))
window_width = (root.winfo_screenwidth()) * 0.6
window_height = (root.winfo_screenheight()) * 0.3
margin = 20
rat_length = max(max(rat_shape))
list_of_turtles = []
x_position_end = (window_width / 2)
end_line = x_position_end - margin
x_position_start = x_position_end * (-1)
test = ""
test.lower()


def run(player):
    # Prepare running board
    screen.setup(width=window_width, height=window_height)
    screen.title("Rat Race")
    screen.register_shape("rat", rat_shape)
    screen.tracer(0)

    # load turtles
    functions.draw_end_line(rat_length, screen)
    for turtle in range(5):
        turtle_to_be_added = Turtle("rat")
        turtle_to_be_added.color('gray')
        list_of_turtles.append(turtle_to_be_added)
    player_turtle = Turtle("rat")
    player_turtle.color(player.color.lower())
    list_of_turtles.append(player_turtle)
    random.shuffle(list_of_turtles)

    # Set turtles on positions
    y_position_start = (window_height / 2) - margin
    distance = window_height / len(list_of_turtles)
    for turtle in list_of_turtles:
        turtle.penup()
        turtle.goto(x=x_position_start, y=y_position_start)
        y_position_start = y_position_start - distance

    # Start the race
    winning_rat = ''
    screen.tracer(1)
    deadline_lap = 0
    while winning_rat == '':
        for turtle in list_of_turtles:
            turtle.forward(random.randint(0, 5))
            if turtle.pencolor() == 'red':
                turtle.forward(100)
            if int(turtle.position()[0]) + rat_length >= end_line - 30:
                winning_rat = turtle.pencolor()
                break
        screen.tracer(0)
        functions.draw_dead_line(((window_width / 2) * (-1) - 20 + deadline_lap), window_height)
        screen.tracer(1)
        deadline_lap += 1
    if winning_rat == player.color.lower():
        image = r'images/promotion.png'
    else:
        image = r'images/loser.png'

    sg.theme('Default1')
    window = sg.Window(CommonStrings.game_name, [[sg.Image(image)]], icon=r'images\rat_icon.ico')
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or 'Exit':
            break
    window.close()
    if 'loser' in image:
        sys.exit()
