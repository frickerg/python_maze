import numpy as np

def getPositionTupleOf(array, symbol):
    whereNp = np.where(array == symbol)
    return list(zip(whereNp[0], whereNp[1]))[0]

def getNeigbourOf(array, position):
    print(position[0] + 1)
    print ('N =>', array[(position[0]-1)][position[1]])
    print ('E =>', array[position[0]][(position[1] + 1)])
    print ('S =>', array[(position[0]+1)][position[1]])
    print ('W =>', array[position[0]][(position[1] - 1)])