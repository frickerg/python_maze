class Compass:
    north = east = south = west = ()

    def __init__(self):
        self.fields = {"N": self.north, "E": self.east, "S": self.south, "W": self.west}

    def set(self, direction, coordinates):
        self.fields[direction] = coordinates

    def get(self, key):
        return self.fields[key]
