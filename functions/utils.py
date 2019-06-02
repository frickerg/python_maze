import numpy as np
from classes.Compass import Compass

mapping = list([(0, "*"), (1, " "), ("A", 2), ("B", 3)])

# Toggles character to number and number to character
def map_character(argument):
    for number, string in mapping:
        if number == argument:
            return string
        elif string == argument:
            return number


def get_position_tuple_of(array, symbol):
    whereNp = np.where(array == symbol)
    return list(zip(whereNp[0], whereNp[1]))[0]


def create_coordinates_list(array, position):
    north = ("N", ((position[0] - 1), position[1]))
    east = ("E", (position[0], (position[1] + 1)))
    south = ("S", ((position[0] + 1), position[1]))
    west = ("W", (position[0], (position[1] - 1)))
    return list([north, east, south, west])


# Work in Progress!
def get_most_suitable_moving_direction(array, compass, movingDirection="none"):
    mappedEntries = list(
        [direction, coordinates, array[coordinates]]
        for direction, coordinates in compass
    )

    available = list(
        [
            {"direction": direction, "coordinates": coordinates, "value": value}
            for direction, coordinates, value in mappedEntries
            if value == 1
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
