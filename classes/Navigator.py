from functions import utils


class Navigator:
    has_arrived = False
    visited_coordinates = []
    destination = (0, 0)
    starting_point = (0, 0)

    def __init__(self, starting_point, destination):
        self.add_coordinates(starting_point)
        self.starting_point = starting_point
        self.destination = destination

    def add_coordinates(self, coordinates):
        self.visited_coordinates.append(coordinates)

    def move_to(self, maze, coordinates):
        print(coordinates)
        last_move = self.visited_coordinates[len(self.visited_coordinates) - 1]
        maze[last_move], maze[coordinates] = maze[coordinates], maze[last_move]
        self.add_coordinates(coordinates)
        if coordinates == self.destination:
            self.has_arrived = True

    def contains(self, available, item):
        found_items = list(entry for entry in available if entry["direction"] == item)
        if len(found_items) > 0:
            return found_items[0]
        return False

    # Work in Progress!
    def get_most_suitable_moving_direction(self, array, compass, moving_direction="None"):
        available = list(
            [
                {"direction": attr, "coordinates": value, "value": array[value]}
                for attr, value in compass.fields.items()
                if array[value] == 1 or array[value] == 3
            ]
        )

        if len(available) == 1:
            return available[0]

        next_direction = utils.get_next_direction(moving_direction)
        move_prioritized = self.contains(available, next_direction)
        if move_prioritized and move_prioritized["coordinates"] not in self.visited_coordinates:
            return move_prioritized

        move_ambushed = list([entry for entry in available if entry["coordinates"] in self.visited_coordinates])

        available_copy = list.copy(available)
        for avoider in move_ambushed:
            available_copy.remove(avoider)

        keep_moving = self.contains(available, moving_direction)

        if len(available) == 1:
            return available[0]
        elif len(available_copy) == 0 and move_prioritized:
            return move_prioritized
        elif len(available_copy) == 0 and keep_moving:
            return keep_moving

        if keep_moving and keep_moving["coordinates"] not in self.visited_coordinates:
            return keep_moving

        # TODO: Inefficient callback, must be removed through optimizing!
        if len(available_copy) == 1:
            return available_copy[0]

        # TODO: Inefficient callback, must be removed through optimizing!
        for i in range(len(available)):
            if moving_direction == "E" and available[i]["direction"] == "S":
                return available[i]
            elif moving_direction == "S" and available[i]["direction"] == "W":
                return available[i]
            elif moving_direction == "W" and available[i]["direction"] == "N":
                return available[i]
            elif moving_direction == "N" and available[i]["direction"] == "E":
                return available[i]
            elif moving_direction == "E" and available[i]["direction"] == "N":
                return available[i]
            elif moving_direction == "W" and available[i]["direction"] == "S":
                return available[i]
            elif moving_direction == "S" and available[i]["direction"] == "E":
                return available[i]
            elif moving_direction == "N" and available[i]["direction"] == "W":
                return available[i]
