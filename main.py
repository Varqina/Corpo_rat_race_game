import random
import tkinter
from tkinter import messagebox
from turtle import Screen, Turtle
import functions

#Main menu

from GUI import StartGui, UserGui

StartGui.run_gui()
player = UserGui.create_player()

import level1
level1.run(player)












