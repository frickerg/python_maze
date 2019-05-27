import numpy as np
np.set_printoptions(threshold=np.inf)

filename = './resources/maze-one.txt'
maze = np.array([])

with open(filename) as fp:  
   for cnt, line in enumerate(fp):
       print("Line {}: {}".format(cnt, line.strip()))
       chars = np.array(list(line.strip()))
       maze = np.append(maze, chars)

print(maze)

a = np.array([1, 2, 3])   # Create a rank 1 array
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"
