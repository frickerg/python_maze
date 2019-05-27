import numpy as np
mapping = list([(0, '*'), (1, ' '), ('A', 2), ('B', 3)])

# Toggles character to number and number to character
def mapCharacter(argument):
    for number, string in mapping:
        if number == argument:
            return string
        elif string == argument:
            return number

def getPositionTupleOf(array, symbol):
    whereNp = np.where(array == symbol)
    return list(zip(whereNp[0], whereNp[1]))[0]

def createCompassList(array, position):
    north = ('N', ((position[0] - 1), position[1]))
    east = ('E', (position[0], (position[1] + 1)))
    south = ('S', ((position[0] + 1), position[1]))
    west = ('W', (position[0], (position[1] - 1)))
    return list([north, east, south, west])

# Work in Progress!
def getMostSuitableMovingDirection(array, compass, movingDirection='none'):
    mappedEntries = list([direction, coordinates, array[coordinates]]
        for direction, coordinates in compass)
    
    print('mapped entries', mappedEntries)

    available = list([[direction, coordinates, value]
        for direction, coordinates, value
        in mappedEntries if value  == 1])
    
    if len(available) == 1:
        return available[0]
    elif 1 == 1:
        print('WIP')
        #TODO: check if one of two directions is the direction we came from
        pass
    else:
        pass