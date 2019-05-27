import numpy as np

def getPositionTupleOf(array, symbol):
    whereNp = np.where(array == symbol)
    return list(zip(whereNp[0], whereNp[1]))[0]

def getMostSuitableDirection(array, currentDirection, position):
    north = ('N', array[(position[0]-1)][position[1]])
    east = ('E', array[position[0]][(position[1] + 1)])
    south = ('S', array[(position[0]+1)][position[1]])
    west = ('W', array[position[0]][(position[1] - 1)])
    compass = list([north, east, south, west])
    print(compass)
    