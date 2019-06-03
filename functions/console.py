from os import system, name
from functions import utils

# define clear function
def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def prettyprint(array, visited_coordinates):
    for i in range(len(array)):
        formatted_line = ""
        for k in range(len(array[i])):
            override = False
            has_visited = False
            try:
                visited_coordinates.index((i, k))
                has_visited = True
                if visited_coordinates[len(visited_coordinates) - 1] == (i, k):
                    override = True

            except ValueError:
                pass
            formatted_line += utils.map_character(array[i][k], has_visited, override)
        print(*formatted_line, sep="")
