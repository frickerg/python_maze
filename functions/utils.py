import numpy as np
from termcolor import colored

from classes.Compass import Compass

character_mapping = list([(0, "*"), (1, " "), (2, "A"), (3, "B")])
direction_mapping = {
    "N": {"next": "E", "opposite": "S"},
    "E": {"next": "S", "opposite": "W"},
    "S": {"next": "W", "opposite": "N"},
    "W": {"next": "N", "opposite": "E"},
}

# Toggles character to number and number to character
def map_character(argument, has_visited=False, override=False):
    for number, string in character_mapping:
        if number == argument:
            if override == True:
                return colored(string, "red", "on_yellow", attrs=["bold"])
            elif has_visited == True:
                return "A"
            return string
        elif string == argument:
            return number


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


def get_next_direction(direction):
    if direction != "None":
        return direction_mapping[direction]["next"]
    return direction
