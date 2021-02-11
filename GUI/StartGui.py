import PySimpleGUI as sg

import CommonStrings
from GUI import UserGui


def run_gui():
    sg.theme('Default1')
    layout = [[sg.Button('Start', size=(30, 2), font=("MS PGothic", 20))]]
    window = sg.Window(CommonStrings.game_name, layout, element_justification='center', icon=r'images\rat_icon.ico')
    while True:
        event, values = window.read()
        if event == 'Start':
            UserGui.run_gui()
            # start race
            break
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
    window.close()
