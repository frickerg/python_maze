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

while navigator.has_arrived == False:
    sleep(0.5)
    console.clear()

    coordinatesList = utils.create_coordinates_list(maze, result_a)
    nextStep = utils.get_most_suitable_moving_direction(maze, coordinatesList)

    navigator.move_to(maze, nextStep["coordinates"])
    console.prettyprint(maze, navigator.visited_coordinates)
