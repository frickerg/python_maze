from os import system, name
from functions import utils
from termcolor import colored
from time import sleep

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


def bad_algorithm():
    sleep(2)
    print(colored("Your algorithm seems to be a dumb little donkey.", color="red"))
    print(colored("To master the mysteries of kung-fu, you must become the python.", color="red"))
    print(colored("Now get some coffee and do it better! 💥☕", color="yellow"))
    exit()


def success(number_of_steps):
    sleep(2)
    print(colored("The light of past discovery draws me forward. Its shining light guides me to the glory of exploration.", color="green"))
    print(colored("Batteries all charged up, snakebites not included!", color="green"))
    print("finished the algorithm in {} steps".format(number_of_steps))
    print(colored("Made by Guillaume Fricker and Amir Khalife, 2019", color="yellow"))
    exit()
