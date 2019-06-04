from functions import utils


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
        self.actual_path.append(coordinates)
        self.visited_coordinates.add(coordinates)

    def move_to(self, maze, previous, coordinates):
        print(coordinates)
        maze[previous], maze[coordinates] = maze[coordinates], maze[previous]
        self.add_coordinates(coordinates)
        if coordinates == self.destination:
            maze[previous] = 1
            self.has_arrived = True

    def contains(self, available, item):
        found_items = list(entry for entry in available if entry["direction"] == item)
        if len(found_items) > 0:
            return found_items[0]
        return False

    def get_most_suitable_moving_direction(self, array, compass, moving_direction="None"):
        available = list(
            [
                {"direction": attr, "coordinates": value, "value": array[value]}
                for attr, value in compass.fields.items()
                if array[value] == 1 or array[value] == 3
            ]
        )
            
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
        for element in available:
            if element["direction"] == utils.get_opposite_direction(moving_direction):
                return element
