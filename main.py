import numpy as np

from functions import utils
from functions import console
from time import sleep

from classes.Compass import Compass

# numpy examples
a = np.array([1, 2, 3])  # Create a rank 1 array
print(a.shape)  # Prints "(3, )"
print(a[0], a[1], a[2])  # Prints "1 2 3"
a[0] = 5  # Change an element of the array
print(a)  # Prints "[5, 2, 3]"

b = np.array([[1, 2, 3], [4, 5, 6]])  # Create a rank 2 array
print(b.shape)  # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])  # Prints "1 2 4"

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

console.prettyprint(maze)
resultA = utils.get_position_tuple_of(maze, 2)
resultB = utils.get_position_tuple_of(maze, 3)
print("Tuple of arrays returned A:", resultA)
print("Tuple of arrays returned B:", resultB)
print("Found A in [{}][{}]".format(resultA[0], resultA[1]))
print("Found B in [{}][{}]".format(resultB[0], resultB[1]))
print(maze[resultA[0]][resultA[1]], maze[resultB[0]][resultB[1]])

coordinatesList = utils.create_coordinates_list(maze, resultA)

nextStep = utils.get_most_suitable_moving_direction(maze, coordinatesList)
print("Next step:", nextStep)  # Work in Progress!
print("Move to:", coordinatesList.get(nextStep["direction"]))
