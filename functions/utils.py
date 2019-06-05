import numpy as np
from termcolor import colored

from classes.Compass import Compass

character_mapping = list([(0, "*"), (1, " "), (2, "A"), (3, "B")])

direction_mapping = {
    "N": {"next_left": "W", "next_right": "E", "opposite": "S"},
    "E": {"next_left": "N", "next_right": "S", "opposite": "W"},
    "S": {"next_left": "E", "next_right": "W", "opposite": "N"},
    "W": {"next_left": "S", "next_right": "N", "opposite": "E"},
}

# Toggles character to number and number to character
def map_character(argument):
    for number, string in character_mapping:
        if number == argument:
            return string
        elif string == argument:
            return number


def print_character(argument, has_visited=False):
    if argument == 0:
        return colored(map_character(argument), "white", "on_white")
    elif argument == 1 and has_visited:
        return colored(map_character(argument), "green", "on_green")
    elif argument == 2 or argument == 3:
        return colored(map_character(argument), "red", "on_yellow", attrs=["bold"])
    return map_character(argument)


def get_position_tuple_of(array, symbol):
    whereNp = np.where(array == symbol)
    return list(zip(whereNp[0], whereNp[1]))[0]


def create_coordinates_list(array, position):
    coord_north = ((position[0] - 1), position[1])
    coord_east = (position[0], (position[1] + 1))
    coord_south = ((position[0] + 1), position[1])
    coord_west = (position[0], (position[1] - 1))

    compass = Compass()
    compass.set("N", coord_north)
    compass.set("E", coord_east)
    compass.set("S", coord_south)
    compass.set("W", coord_west)
    return compass


def get_opposite_direction(direction):
    return direction_mapping[direction]["opposite"]


def get_next_direction(direction, hand):
    return direction_mapping[direction]["next_" + hand]
