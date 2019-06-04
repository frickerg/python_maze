import numpy as np

from functions import utils
from functions import console
from time import sleep

from classes.Compass import Compass
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

maze = np.array(setup)
result_a = utils.get_position_tuple_of(maze, 2)
result_b = utils.get_position_tuple_of(maze, 3)
navigator = Navigator(result_a, result_b)

# TODO: ask if the user wants to move with left/right hand (?)
last_moving_direction = "N"

# TODO: find alternative routes that are shorter!
while navigator.has_arrived != True:
    result_a = utils.get_position_tuple_of(maze, 2)
    coordinates_list = utils.create_coordinates_list(maze, result_a)
    next_step = navigator.get_most_suitable_moving_direction(maze, coordinates_list, moving_direction=last_moving_direction)

    print("Looking for the closest path...")
    navigator.move_to(maze, result_a, next_step["coordinates"])
    last_moving_direction = next_step["direction"]
    console.clear()

final_path = navigator.actual_path
remove_loose_ends = list()
for element in final_path:
    if element in remove_loose_ends:
        for indice in [i for i, x in enumerate(remove_loose_ends) if x == element]:
            del remove_loose_ends[indice : len(remove_loose_ends)]
    remove_loose_ends.append(element)

# TODO: Remove duplicate of code at the start!
maze = np.array(setup)
result_a = utils.get_position_tuple_of(maze, 2)
result_b = utils.get_position_tuple_of(maze, 3)
navigator = Navigator(result_a, result_b)

for next_step in remove_loose_ends:
    sleep(1 / 30)
    console.clear()
    result_a = utils.get_position_tuple_of(maze, 2)
    navigator.move_to(maze, result_a, next_step)
    console.prettyprint(maze, navigator.visited_coordinates)

console.success(len(navigator.actual_path))
