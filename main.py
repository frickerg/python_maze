import numpy as np

from functions import utils
from functions import console
from time import sleep

from classes.Compass import Compass
from classes.Navigator import Navigator

filename = "./resources/maze-one.txt"
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

# TODO: ask if the user wants to move with left/right hand
last_moving_direction = "N"

number_of_steps = 0
while navigator.has_arrived != True:
    sleep(0.1)
    console.clear()

    result_a = utils.get_position_tuple_of(maze, 2)
    coordinates_list = utils.create_coordinates_list(maze, result_a)
    next_step = navigator.get_most_suitable_moving_direction(maze, coordinates_list, moving_direction=last_moving_direction)

    navigator.move_to(maze, next_step["coordinates"])
    last_moving_direction = next_step["direction"]

    console.prettyprint(maze, navigator.visited_coordinates)

    number_of_steps += 1
    if next_step["coordinates"] == navigator.starting_point:
        console.bad_algorithm()

# Algorithm successful!
console.success(number_of_steps)
