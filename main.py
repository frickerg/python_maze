import subprocess
import sys

# Install PIP module automatically
def install_pip(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])


install_pip("numpy")
# Coloring of print()
install_pip("termcolor")

import numpy as np

from functions import utils
from functions import console
from functions import merge
from time import sleep

from classes.Navigator import Navigator

import os

# Build absolute path from project directory
# FIXED BUG: Run main.py from everywhere
path_name = os.path.dirname(os.path.abspath(__file__))
resources_path = os.path.join(path_name, "resources")
filename = os.path.join(resources_path, "maze-many.txt")

# List which contains the maze file txt content
setup = list()

# Read (open) File
with open(filename) as fp:
    # for every line in file
    # param cnt: line count (index)
    # param line: line content
    for cnt, line in enumerate(fp):
        # insert new sublist --> [] at index cnt
        # example: [[linechar1, linechar2, ..., linecharN]] --> [[linechar1, linechar2, ..., linecharN], []]
        setup.insert(cnt, [])
        # makes list of characters in line
        # example: 1234 --> [1,2,3,4]
        chars = list(line.strip())
        for i in range(len(chars)):
            # 1 --> " "
            mappedChar = utils.map_character(chars[i])
            # append to the current line list
            # example: [1,2,3] --> [1,2,3,4]
            setup[cnt].append(mappedChar)

# method which cuts all paths that lead back to the same route
# param actual_path: set from Navigator, contains all steps performed as coordinates
def remove_loose_ends(actual_path):
    clean_list = list()
    for element in actual_path:
        if element in clean_list:
            # creates a for loop that deletes the entire sequence that leads back to the same route
            for indice in [i for i, x in enumerate(clean_list) if x == element]:
                # del from indice to len of clean_list
                del clean_list[indice : len(clean_list)]
        clean_list.append(element)
    return clean_list


# function which provides the traversing algorithm in a loop
# param hand: left | right --> which hand to follow
def looper(hand):
    if hand == "left":
        last_moving_direction = "N"
    elif hand == "right":
        last_moving_direction = "S"

    # create numpy array from setup list
    # decided to build the setup list first, because it requires less performance!
    # (see bibliography "NumPy Multidimensional Array")
    maze = np.array(setup)
    result_a = utils.get_position_tuple_of(maze, 2)
    result_b = utils.get_position_tuple_of(maze, 3)
    navigator = Navigator(result_a, result_b, hand)

    while navigator.has_arrived != True:
        # get position coordinates of A
        result_a = utils.get_position_tuple_of(maze, 2)
        # get all neighbouring coordinates of A
        coordinates_list = utils.create_coordinates_list(maze, result_a)
        # decide on which step to perfom
        next_step = navigator.get_most_suitable_moving_direction(maze, coordinates_list, moving_direction=last_moving_direction)

        # perform the next step
        navigator.move_to(maze, result_a, next_step["coordinates"])
        # set last_moving_direction for algorithm logic
        last_moving_direction = next_step["direction"]

    return navigator.actual_path


# Functions the same way as looper, but additionally requires a predefined path
# The printing_looper function prints the algorithm steps on the console
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
        # print the maze pretty
        console.prettyprint(maze, navigator.visited_coordinates)


# left hand algorithm
actual_left = looper("left")
len_left = len(actual_left)
clean_left = remove_loose_ends(actual_left)

# right hand algorithm
actual_right = looper("right")
len_right = len(actual_right)
clean_right = remove_loose_ends(actual_right)

# find shortest route from left and rigth hand algorithm, then print the path
merged_path = merge.merge_to_shortest_path(clean_left, clean_right)
printing_looper(merged_path)
console.success(len(merged_path), len_left, len_right)
