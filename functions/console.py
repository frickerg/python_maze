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
            has_visited = (i, k) in visited_coordinates
            formatted_line += utils.print_character(array[i][k], has_visited)
        print(*formatted_line, sep="")


def bad_algorithm():
    print(colored("ERROR: Algorithm points back to starting position!", color="red"))
    exit()


def success(number_of_steps):
    sleep(2)
    print(colored("\nMade by Guillaume Fricker and Amir Khalife, 2019", "yellow"))
    print(colored("The light of past discovery draws me forward. Its shining light guides me to the glory of exploration.", color="green"))
    print(colored("Finished the maze in {} steps\n".format(number_of_steps), "red", "on_yellow", attrs=["bold"]))
    exit()
