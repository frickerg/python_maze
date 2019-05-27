import numpy as np

def getPositionTupleOf(array, symbol):
    whereNp = np.where(array == symbol)
    return list(zip(whereNp[0], whereNp[1]))[0]