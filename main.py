import numpy as np

from functions import utils
from functions import console
from time import sleep

from classes.Compass import Compass

sleep(0.5)
console.clear()

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
visited_coordinates = [result_a]

console.prettyprint(maze, visited_coordinates)

result_b = utils.get_position_tuple_of(maze, 3)
print("Tuple of A returned:", result_a)
print("Tuple of B returned:", result_b)
print(maze[result_a[0]][result_a[1]], maze[result_b[0]][result_b[1]])

coordinatesList = utils.create_coordinates_list(maze, result_a)

nextStep = utils.get_most_suitable_moving_direction(maze, coordinatesList)
print("Next step:", nextStep)  # Work in Progress!
print("Move to:", nextStep["coordinates"])
