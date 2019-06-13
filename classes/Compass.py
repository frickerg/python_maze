class Compass:
    north = east = south = west = ()

    #Defining the 4 cardinal points within the init method
    def __init__(self):
        self.fields = {"N": self.north, "E": self.east, "S": self.south, "W": self.west}

    #Setting the the direction according to the coordinates
    def set(self, direction, coordinates):
        self.fields[direction] = coordinates

    #Getting the Key methode
    def get(self, key):
        return self.fields[key]
