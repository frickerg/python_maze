import numpy as np
import itertools

from functions import utils
from functions import console
from time import sleep

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


def remove_loose_ends(actual_path):
    clean_list = list()
    for element in actual_path:
        if element in clean_list:
            for indice in [i for i, x in enumerate(clean_list) if x == element]:
                del clean_list[indice : len(clean_list)]
        clean_list.append(element)
    return clean_list


def looper(hand):
    if hand == "left":
        last_moving_direction = "N"
    elif hand == "right":
        last_moving_direction = "S"

    maze = np.array(setup)
    result_a = utils.get_position_tuple_of(maze, 2)
    result_b = utils.get_position_tuple_of(maze, 3)
    navigator = Navigator(result_a, result_b, hand)

    while navigator.has_arrived != True:
        result_a = utils.get_position_tuple_of(maze, 2)
        coordinates_list = utils.create_coordinates_list(maze, result_a)
        next_step = navigator.get_most_suitable_moving_direction(maze, coordinates_list, moving_direction=last_moving_direction)

        navigator.move_to(maze, result_a, next_step["coordinates"])
        last_moving_direction = next_step["direction"]

    return navigator.actual_path


def printing_looper(array):
    maze = np.array(setup)
    result_a = utils.get_position_tuple_of(maze, 2)
    result_b = utils.get_position_tuple_of(maze, 3)
    navigator = Navigator(result_a, result_b)
    direction_list = list()

    for next_step in array:
        sleep(1 / 30)
        console.clear()
        print(next_step)
        result_a = utils.get_position_tuple_of(maze, 2)
        navigator.move_to(maze, result_a, next_step)
        direction_list.append(next_step)
        console.prettyprint(maze, navigator.visited_coordinates)

    # TODO: Make direction_list contain the actual directions
    print(direction_list)
    console.success(len(navigator.actual_path))


actual_left = looper("left")
clean_left = remove_loose_ends(actual_left)
printing_looper(clean_left)

actual_right = looper("right")
clean_right = remove_loose_ends(actual_right)
printing_looper(clean_right)
merged_path = list()

print(None in clean_left)
for left, right in itertools.zip_longest(clean_left, clean_right):
    if left == right:
        merged_path.append(left)
    else:
        try:
            iter_start_left = clean_left.index(left)
            iter_start_right = clean_right.index(right)
            iter_end_left = 0
            iter_end_right = 0
            steps_left = 0
            steps_right = 0
        except ValueError:
            pass
        try:
            if left in clean_right:
                iter_end_left = clean_right.index(left)
                print("left", iter_start_left, iter_end_left, "->", iter_start_right, iter_end_right)
                print("steps", steps_left)
                steps_left += 1
            else:
                pass
        except ValueError:
            pass
        try:
            if right in clean_left:
                iter_end_right = clean_left.index(right)
                print("right", iter_start_right, iter_end_right, "->", iter_start_left, iter_end_left)
                print("steps", steps_right)
                steps_right += 1
            else:
                pass
        except ValueError:
            pass
"""
for i in range(len(clean_right)):
    if clean_left[i] == clean_right[i]:
        merged_path.append(clean_left)
    else:
        steps_left = 0
        steps_right = 0
        found_left = False
        found_right = False

        while found_left == False:
            try:
                print(clean_left.index(clean_right[i + steps_right]))
                print('right',clean_right[i + steps_right])
                found_left = True
            except ValueError:
                pass
            steps_left += 1
            steps_right += 1
        while found_right == False:
            try:
                clean_right.index(clean_left[i + steps_left])
                print('left',clean_left[i + steps_left])
                found_right = True
            except ValueError:
                pass
            steps_left += 1
            steps_right += 1
        print(steps_left, steps_right)
print(merged_path)
"""
