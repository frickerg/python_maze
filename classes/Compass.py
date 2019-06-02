# ################
# Compass Class:
# Bei dieser Klasse geht es darum, einen Wert für die verschiedenen Richtungen zu setzen, und dazu sagen können, auf welcher Position sich dieser Wert befindet.
# Die klasse muss nicht umbedingt Compass heissen ;-)
# 
# Beispiel: compass.setNorth(1, (x, y)) // hier sagen wir, dass sich auf dem Tupel der position (x, y) der Wert vom Typ '1' befindet
# ################
class Compass:
    north = east = south = west = ()

    def __init__(self):
        self.fields = {
            'N': self.north, 
            'E': self.east, 
            'S': self.south, 
            'W': self.west
        }

    def set(self, direction, coordinates, value):
        self.fields[direction] = coordinates
   
    def get(self, key):
        return self.fields[key]