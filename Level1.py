import random
import sys
import tkinter
import PySimpleGUI as sg
from turtle import Screen, Turtle
import CommonStrings
import functions
from Events.GlobalEvent import GlobalEvent
from RatClassAI import RatClassAI
from RatClassUser import RatClassUser


class Level1:
    def __init__(self):
        self.screen = Screen()
        self.root = tkinter.Tk()
        self.global_event = GlobalEvent()
        self.root.withdraw()
        self.rat_shape = ((0, 0), (0, 10), (-10, 20), (-10, 30), (-5, 35), (-10, 35), (-5, 40), (1, 47), (1, 0))
        self.window_width = (self.root.winfo_screenwidth()) * 0.6
        self.window_height = (self.root.winfo_screenheight()) * 0.3
        self.margin = 20
        self.rat_length = max(max(self.rat_shape))
        self.list_of_rats = []
        self.x_position_end = (self.window_width / 2)
        self.end_line = self.x_position_end - self.margin
        self.x_position_start = self.x_position_end * (-1)
        self.test = ""
        self.test.lower()
        self.level = 1

    def start(self, player):
        # Prepare running board
        self.screen.setup(width=self.window_width, height=self.window_height)
        self.screen.title("Rat Race")
        self.screen.register_shape("rat", self.rat_shape)
        self.screen.tracer(0)
        functions.draw_end_line(self.rat_length, self.screen)

        # load turtles
        for computer_players in range(5):
            computer_player_to_be_added = RatClassAI()
            computer_player_to_be_added.setup_random_parameters()
            computer_player_to_be_added.turtle.shape('rat')
            computer_player_to_be_added.turtle.color(computer_player_to_be_added.color)
            self.list_of_rats.append(computer_player_to_be_added)
        player.turtle.shape('rat')
        print('aaaaaaaaaaaaaa')
        print(player.color)
        print(player.turtle.color())

        self.list_of_rats.append(player)
        random.shuffle(self.list_of_rats)
        #for rat in self.list_of_rats:
        #    print(rat.turtle.pencolor())

        # Set turtles on positions
        y_position_start = (self.window_height / 2) - self.margin
        distance = self.window_height / len(self.list_of_rats)
        for rat in self.list_of_rats:
            rat.turtle.penup()
            rat.turtle.goto(x=self.x_position_start, y=y_position_start)
            y_position_start = y_position_start - distance


        # Start the race
        winning_rat = ''
        self.screen.tracer(1)
        deadline_lap = 0
        while winning_rat == '':
            lap_move_list = []
            deadline_x_position = ((self.window_width / 2) * (-1) - self.margin + deadline_lap)
            # lottery for event
            if random.randint(0, 10) == 7:
                self.global_event.get_event()
            for rat in self.list_of_rats:
                rat.turtle.forward(random.randint(0, 5))
                if rat.turtle.pencolor() == 'red':
                    rat.turtle.forward(100)
                if int(rat.turtle.position()[0]) + self.rat_length >= self.end_line - 30:
                    winning_rat = rat.turtle.pencolor()
                    break
                if int(rat.turtle.position()[0]) < deadline_x_position:
                    rat.turtle.hideturtle()
                    self.list_of_rats.remove(rat)
                if len(self.list_of_rats) == 0:
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



