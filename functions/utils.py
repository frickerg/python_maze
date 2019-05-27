import numpy as np

def getPositionTupleOf(array, symbol):
    whereNp = np.where(array == symbol)
    return list(zip(whereNp[0], whereNp[1]))[0]


def switch_probe(argument):
    if argument == '*':
        return 0
    elif argument == ' ':
        return 1
    elif argument == 'A':
        return 2
    elif argument == 'B':
        return 3


#myList = ['A',' ','B','*']

#for ele in myList:
   # print (switch_probe(ele))
    