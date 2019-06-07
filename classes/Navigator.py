from functions import utils

# Class that handles the navigation within the maze numpy array
class Navigator:
    has_arrived = False
    visited_coordinates = set()
    actual_path = list()
    destination = (0, 0)
    starting_point = (0, 0)
    hand_side = None

    def __init__(self, starting_point, destination, hand_side="left"):
        self.visited_coordinates.clear()
        self.actual_path.clear()
        self.add_coordinates(starting_point)
        self.starting_point = starting_point
        self.destination = destination
        self.hand_side = hand_side

    def add_coordinates(self, coordinates):
        # actual_path is a list and contains ALL coordinates in traversing order
        self.actual_path.append(coordinates)
        # visited_coordinates is a set and contains every coordinate only once!
        # if the algorithm is looking for a coordinate, visited_coordinates is much faster because it's much shorter that the actual_path
        self.visited_coordinates.add(coordinates)

    # moves to a new position
    def move_to(self, maze, previous, coordinates):
        # swap maze[previous] with maze[coordinates]
        maze[previous], maze[coordinates] = maze[coordinates], maze[previous]
        self.add_coordinates(coordinates)
        if coordinates == self.destination:
            # if the destination has been reached, replace "B" with " " and set the flag to True
            maze[previous] = 1
            self.has_arrived = True

    # returns a single entry from a list, if it can be found
    def contains(self, available, item):
        found_items = list(entry for entry in available if entry["direction"] == item)
        if len(found_items) > 0:
            return found_items[0]
        return False

    # this is the actual algorithm and it's very sexy
    def get_most_suitable_moving_direction(self, array, compass, moving_direction="None"):
        # creates a list of available coordinates from the compass instance
        # the available list contains all entries which have the value 1 (" ") or 3 ("B")
        available = list(
            [
                {"direction": attr, "coordinates": value, "value": array[value]}
                for attr, value in compass.fields.items()
                if array[value] == 1 or array[value] == 3
            ]
        )

        # get the next direction from moving direction, which is always considered high priority if directions must be switched
        next_direction = utils.get_next_direction(moving_direction, self.hand_side)
        # check if there is an outwards corner on hand side
        for element in available:
            if element["direction"] == next_direction:
                return element
        # check if there is a wall on hand side
        for element in available:
            if element["direction"] == moving_direction:
                return element
        # check if there is an inwards corner on hand side
        for element in available:
            if element["direction"] == utils.get_opposite_direction(next_direction):
                return element
        # if no direction can be found, turn around
        for element in available:
            if element["direction"] == utils.get_opposite_direction(moving_direction):
                return element
