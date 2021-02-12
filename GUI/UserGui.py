import sys

import PySimpleGUI as sg

import CommonStrings
from RatClassUser import RatClassUser


def create_player():
    background = '#F0F0F0'
    free_points = 10
    diligence_value = 0
    intellect_value = 0
    helpful_value = 0
    ambitious_value = 0
    sneaky_value = 0
    idler_value = 0
    color = ''
    sg.theme('Default1')
    abilities_column_left_title = [[sg.Text('Diligence', font=("MS PGothic", 12), justification='left')],
                                   [sg.Text('Helpful', font=("MS PGothic", 12), justification='center')],
                                   [sg.Text('Ambitious', font=("MS PGothic", 12), justification='center')]]
    abilities_column_left_value = [[get_button(r'images\remove.png', background, 'remove_diligence'),
                                    sg.Input(diligence_value, key='diligence_value', size=(2, 1)),
                                    get_button(r'images\add.png', background, 'add_diligence')],
                                   [get_button(r'images\remove.png', background, 'remove_helpful'),
                                    sg.Input(helpful_value, key='helpful_value', size=(2, 1)),
                                    get_button(r'images\add.png', background, 'add_helpful')],
                                   [get_button(r'images\remove.png', background, 'remove_ambitious'),
                                    sg.Input(ambitious_value, key='ambitious_value', size=(2, 1)),
                                    get_button(r'images\add.png', background, 'add_ambitious')]]

    abilities_column_right_title = [[sg.Text('Intellect', font=("MS PGothic", 12), justification='right')],
                                    [sg.Text('Sneaky', font=("MS PGothic", 12), justification='right')],
                                    [sg.Text('Idler', font=("MS PGothic", 12), justification='right')]]
    abilities_column_right_value = [[get_button(r'images\remove.png', background, 'remove_intellect'),
                                     sg.Input(intellect_value, key='intellect_value', size=(2, 1)),
                                     get_button(r'images\add.png', background, 'add_intellect')],
                                    [get_button(r'images\remove.png', background, 'remove_sneaky'),
                                     sg.Input(sneaky_value, key='sneaky_value', size=(2, 1)),
                                     get_button(r'images\add.png', background, 'add_sneaky')],
                                    [get_button(r'images\remove.png', background, 'remove_idler'),
                                     sg.Input(idler_value, key='idler_value', size=(2, 1)),
                                     get_button(r'images\add.png', background, 'add_idler')]]

    layout = [[sg.Text('Player name', font=("MS PGothic", 12), key='name_text'), sg.Input(key='player_name')],
              [sg.Text('Player color', font=("MS PGothic", 12), key='color_text'),
               sg.Combo(CommonStrings.color_list, key='color')],
              [sg.Text('Player abilities', font=("MS PGothic", 12))],
              [sg.Text(f'You have', font=("MS PGothic", 10)),
               sg.Text(free_points, text_color='green', font=("MS PGothic", 10), key='point_value'),
               sg.Text('points remaining', font=("MS PGothic", 10))],
              [sg.Column(abilities_column_left_title, element_justification='left'),
               sg.Column(abilities_column_left_value, element_justification='left'),
               sg.Column(abilities_column_right_title, element_justification='left'),
               sg.Column(abilities_column_right_value, element_justification='right')],
              [sg.Button('Start', size=(30, 1), font=("MS PGothic", 20))]]
    window = sg.Window(CommonStrings.game_name, layout, element_justification='left', icon=r'images\rat_icon.ico')
    while True:
        key, values = window.read()
        if key == 'Start':
            if validate_form(values):
                color = values['color']
                break
            else:
                if values['player_name'] == '':
                    window.FindElement('name_text').Update(text_color='red')
                if values['color'] == '':
                    window.FindElement('color_text').Update(text_color='red')

        if key == 'add_diligence':
            if free_points > 0:
                diligence_value += 1
                free_points -= 1
                window.FindElement('diligence_value').Update(diligence_value)
        if key == 'remove_diligence':
            if diligence_value > 0:
                diligence_value -= 1
                free_points += 1
            window.FindElement('diligence_value').Update(diligence_value)

        if key == 'add_helpful':
            if free_points > 0:
                helpful_value += 1
                free_points -= 1
                window.FindElement('helpful_value').Update(helpful_value)
        if key == 'remove_helpful':
            if helpful_value > 0:
                helpful_value -= 1
                free_points += 1
            window.FindElement('helpful_value').Update(helpful_value)

        if key == 'add_ambitious':
            if free_points > 0:
                ambitious_value += 1
                free_points -= 1
                window.FindElement('ambitious_value').Update(ambitious_value)
        if key == 'remove_ambitious':
            if ambitious_value > 0:
                ambitious_value -= 1
                free_points += 1
            window.FindElement('ambitious_value').Update(ambitious_value)

        if key == 'add_intellect':
            if free_points > 0:
                intellect_value += 1
                free_points -= 1
                window.FindElement('intellect_value').Update(intellect_value)
        if key == 'remove_intellect':
            if intellect_value > 0:
                intellect_value -= 1
                free_points += 1
            window.FindElement('intellect_value').Update(intellect_value)

        if key == 'add_sneaky':
            if free_points > 0:
                sneaky_value += 1
                free_points -= 1
                window.FindElement('sneaky_value').Update(sneaky_value)
        if key == 'remove_sneaky':
            if sneaky_value > 0:
                sneaky_value -= 1
                free_points += 1
            window.FindElement('sneaky_value').Update(sneaky_value)

        if key == 'add_idler':
            if free_points > 0:
                idler_value += 1
                free_points -= 1
                window.FindElement('idler_value').Update(idler_value)
        if key == 'remove_idler':
            if idler_value > 0:
                idler_value -= 1
                free_points += 1
            window.FindElement('idler_value').Update(idler_value)

        if key == sg.WIN_CLOSED or key == 'Exit':
            sys.exit()
        if free_points <= 3:
            window.FindElement('point_value').Update(text_color='red')
        window.FindElement('point_value').Update(free_points)
    window.close()
    player = RatClassUser(ambitious=ambitious_value, idler=idler_value, intellect=intellect_value,
                          sneaky=sneaky_value, diligence=diligence_value, helpful=helpful_value, color=color)
    return player


def get_button(icon, background, key):
    return sg.Button(image_filename=icon, image_size=(20, 20), key=key, button_color=(background, background))


def validate_form(values):
    if values['player_name'] != '' and values['color'] != '':
        return True
    return False
