import random
import sys
import tkinter
import PySimpleGUI as sg
from turtle import Screen, Turtle
import CommonStrings
import functions

class Level1:
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
    level = 1
    def __init__(self):
        pass

    def start(self, player):
        # Prepare running board
        self.screen.setup(width=self.window_width, height=self.window_height)
        self.screen.title("Rat Race")
        self.screen.register_shape("rat", self.rat_shape)
        self.screen.tracer(0)

        # load turtles
        functions.draw_end_line(self.rat_length, self.screen)
        for turtle in range(5):
            turtle_to_be_added = Turtle("rat")
            turtle_to_be_added.color('gray')
            self.list_of_turtles.append(turtle_to_be_added)
        player_turtle = Turtle("rat")
        player_turtle.color(player.color.lower())
        self.list_of_turtles.append(player_turtle)
        random.shuffle(self.list_of_turtles)

        # Set turtles on positions
        y_position_start = (self.window_height / 2) - self.margin
        distance = self.window_height / len(self.list_of_turtles)
        for turtle in self.list_of_turtles:
            turtle.penup()
            turtle.goto(x=self.x_position_start, y=y_position_start)
            y_position_start = y_position_start - distance

        # Start the race
        winning_rat = ''
        self.screen.tracer(1)
        deadline_lap = 0
        while winning_rat == '':
            deadline_x_position =((self.window_width / 2) * (-1) - self.margin + deadline_lap)
            for turtle in self.list_of_turtles:
                turtle.forward(random.randint(0, 5))
                if turtle.pencolor() == 'red':
                    turtle.forward(100)
                if int(turtle.position()[0]) + self.rat_length >= self.end_line - 30:
                    winning_rat = turtle.pencolor()
                    break
                if int(turtle.position()[0]) < deadline_x_position:
                    turtle.hideturtle()
                    self.list_of_turtles.remove(turtle)
                if len(self.list_of_turtles) == 0:
                    winning_rat = 'None'
                    break
            self.screen.tracer(0)
            functions.draw_dead_line(deadline_x_position, self.window_height)
            self.screen.tracer(1)
            deadline_lap += self.level
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



