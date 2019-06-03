class Navigator:
    has_arrived = False
    visited_coordinates = []
    destination = (0, 0)

    def __init__(self, starting_point, destination):
        self.add_coordinates(starting_point)
        self.destination = destination

    def add_coordinates(self, coordinates):
        self.visited_coordinates.append(coordinates)

    def move_to(self, maze, coordinates):
        last_move = self.visited_coordinates[len(self.visited_coordinates) - 1]
        maze[last_move], maze[coordinates] = maze[coordinates], maze[last_move]
        self.add_coordinates(coordinates)
        if coordinates == self.destination:
            self.has_arrived = True
