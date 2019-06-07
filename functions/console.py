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


# print the maze pretty
def prettyprint(array, visited_coordinates):
    for i in range(len(array)):
        # create empty string which will be appended as one line
        formatted_line = ""
        for k in range(len(array[i])):
            # check if the coordinates have been visited yet
            has_visited = (i, k) in visited_coordinates
            # append character to current line
            formatted_line += utils.print_character(array[i][k], has_visited)
        # print the formatted_line with empty seperator of chars
        print(*formatted_line, sep="")


def bad_algorithm():
    print(colored("ERROR: Algorithm points back to starting position!", color="red"))
    exit()


def success(merged_path_len, left_hand_len, right_hand_len):
    print()
    sleep(1)
    print(colored("left hand algorithm:  {} steps".format(left_hand_len), "red", attrs=["bold"]))
    print(colored("right hand algorithm: {} steps".format(right_hand_len), "red", attrs=["bold"]))
    print(colored("merged algorithm:     {} steps".format(merged_path_len), "red", attrs=["bold"]))
    print()
    print(colored("Finished the maze in: {} steps".format(merged_path_len), "red", "on_yellow", attrs=["bold"]))
    sleep(2)
    print()
    print(colored("Made by Guillaume Fricker and Amir Khalife, 2019", "yellow"))
    print(colored("The light of past discovery draws me forward.", color="green"))
    print(colored("Its shining light guides me to the glory of exploration.", color="green"))
    print()
    exit()
