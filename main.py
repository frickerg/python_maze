import numpy as np
np.set_printoptions(threshold=np.inf)

filename = './resources/maze-one.txt'
setup = list()

with open(filename) as fp:  
   for cnt, line in enumerate(fp):
       print("Line {}: {}".format(cnt, line.strip()))
       chars = list(line.strip())
       setup.insert(cnt, [])
       for i in range(len(chars)):
           setup[cnt].append(chars[i])

maze = np.array(setup)

print(maze)
npwhere = np.where(maze == 'A')
result = list(zip(npwhere[0], npwhere[1]))[0]
print('Tuple of arrays returned : ', result)
print('Found A in array[{}][{}]'.format(result[0],result[1]))
print(maze[result[0]][result[1]])

# numpy examples
a = np.array([1, 2, 3])   # Create a rank 1 array
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"
