import numpy as np
from termcolor import colored

from classes.Compass import Compass

mapping = list([(0, "*"), (1, " "), (2, "A"), (3, "B")])

# Toggles character to number and number to character
def map_character(argument, has_visited=False, override=False):
    for number, string in mapping:
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


# Work in Progress!
def get_most_suitable_moving_direction(array, compass, movingDirection="none"):
    available = list(
        [
            {"direction": attr, "coordinates": value, "value": array[value]}
            for attr, value in compass.fields.items()
            if array[value] == 1
        ]
    )

    if len(available) == 1:
        return available[0]
    elif 1 == 1:
        print("WIP")
        # TODO: check if one of two directions is the direction we came from
        pass
    else:
        pass
