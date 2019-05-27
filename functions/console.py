from os import system, name 
  
# define clear function 
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def prettyprint(array):
    for x in array:
        print(*x, sep="")