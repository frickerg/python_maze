import subprocess
import sys


def install_pip(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])


install_pip("numpy")
install_pip("termcolor")

import numpy as np

from functions import utils
from functions import console
from functions import merge
from time import sleep

from classes.Navigator import Navigator

filename = "./resources/maze-many.txt"
setup = list()

with open(filename) as fp:
    for cnt, line in enumerate(fp):
        setup.insert(cnt, [])
        chars = list(line.strip())
        for i in range(len(chars)):
            mappedChar = utils.map_character(chars[i])
            setup[cnt].append(mappedChar)


def remove_loose_ends(actual_path):
    clean_list = list()
    for element in actual_path:
        if element in clean_list:
            for indice in [i for i, x in enumerate(clean_list) if x == element]:
                del clean_list[indice : len(clean_list)]
        clean_list.append(element)
    return clean_list


def looper(hand):
    if hand == "left":
        last_moving_direction = "N"
    elif hand == "right":
        last_moving_direction = "S"

    maze = np.array(setup)
    result_a = utils.get_position_tuple_of(maze, 2)
    result_b = utils.get_position_tuple_of(maze, 3)
    navigator = Navigator(result_a, result_b, hand)

    while navigator.has_arrived != True:
        result_a = utils.get_position_tuple_of(maze, 2)
        coordinates_list = utils.create_coordinates_list(maze, result_a)
        next_step = navigator.get_most_suitable_moving_direction(maze, coordinates_list, moving_direction=last_moving_direction)

        navigator.move_to(maze, result_a, next_step["coordinates"])
        last_moving_direction = next_step["direction"]

    return navigator.actual_path


def printing_looper(merged_path):
    maze = np.array(setup)
    result_a = utils.get_position_tuple_of(maze, 2)
    result_b = utils.get_position_tuple_of(maze, 3)
    navigator = Navigator(result_a, result_b)
    direction_list = list()

    for next_step in merged_path:
        sleep(1 / 30)
        console.clear()
        print(next_step)
        result_a = utils.get_position_tuple_of(maze, 2)
        navigator.move_to(maze, result_a, next_step)
        direction_list.append(next_step)
        console.prettyprint(maze, navigator.visited_coordinates)


actual_left = looper("left")
len_left = len(actual_left)
clean_left = remove_loose_ends(actual_left)

actual_right = looper("right")
len_right = len(actual_right)
clean_right = remove_loose_ends(actual_right)

merged_path = merge.merge_to_shortest_path(clean_left, clean_right)
printing_looper(merged_path)
console.success(len(merged_path), len_left, len_right)
