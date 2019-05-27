from os import system, name 
from functions import utils

# define clear function 
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def prettyprint(array):
    for line in array:
        mappedLine = ''.join(utils.mapNumberToKey(char) for char in line)
        print(mappedLine, sep="")