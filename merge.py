import itertools
from itertools import groupby

a = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13), (4, 13), (5, 13), (5, 14), (5, 15), (5, 16), (5, 17), (6, 17), (7, 17), (7, 18), (7, 19), (6, 19), (5, 19), (5, 20), (5, 21), (4, 21), (3, 21), (3, 22), (3, 23), (3, 24), (3, 25), (3, 26), (3, 27), (3, 28), (3, 29), (3, 30), (2, 30), (1, 30), (1, 31), (1, 32), (1, 33), (1, 34), (1, 35), (1, 36), (1, 37), (1, 38), (1, 39), (1, 40), (1, 41), (1, 42), (1, 43), (2, 43), (3, 43), (3, 44), (3, 45), (2, 45), (1, 45), (1, 46), (1, 47), (2, 47), (3, 47), (3, 48), (3, 49), (3, 50), (3, 51), (2, 51), (1, 51), (1, 52), (1, 53), (2, 53), (3, 53), (3, 54), (3, 55), (2, 55), (1, 55), (1, 56), (1, 57), (2, 57), (3, 57), (3, 58), (3, 59), (3, 60), (3, 61), (4, 61), (5, 61), (5, 62), (5, 63), (6, 63), (7, 63), (8, 63), (9, 63), (10, 63), (11, 63), (12, 63), (13, 63), (13, 62), (13, 61), (14, 61), (15, 61), (15, 62), (15, 63)]
b = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 9), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13), (4, 13), (5, 13), (5, 14), (5, 15), (5, 16), (5, 17), (6, 17), (7, 17), (7, 18), (7, 19), (6, 19), (5, 19), (5, 20), (5, 21), (4, 21), (3, 21), (3, 22), (3, 23), (3, 24), (3, 25), (3, 26), (3, 27), (3, 28), (3, 29), (3, 30), (3, 31), (3, 32), (3, 33), (4, 33), (5, 33), (6, 33), (7, 33), (7, 34), (7, 35), (7, 36), (7, 37), (8, 37), (9, 37), (9, 36), (9, 35), (9, 34), (9, 33), (10, 33), (11, 33), (11, 32), (11, 31), (11, 30), (11, 29), (11, 28), (11, 27), (10, 27), (9, 27), (8, 27), (7, 27), (7, 26), (7, 25), (8, 25), (9, 25), (10, 25), (11, 25), (12, 25), (13, 25), (14, 25), (15, 25), (15, 26), (15, 27), (15, 28), (15, 29), (14, 29), (13, 29), (13, 30), (13, 31), (13, 32), (13, 33), (14, 33), (15, 33), (15, 34), (15, 35), (15, 36), (15, 37), (15, 38), (15, 39), (15, 40), (15, 41), (15, 42), (15, 43), (14, 43), (13, 43), (12, 43), (11, 43), (10, 43), (9, 43), (9, 44), (9, 45), (9, 46), (9, 47), (10, 47), (11, 47), (11, 48), (11, 49), (10, 49), (9, 49), (9, 50), (9, 51), (8, 51), (7, 51), (7, 50), (7, 49), (7, 48), (7, 47), (7, 46), (7, 45), (6, 45), (5, 45), (5, 44), (5, 43), (5, 42), (5, 41), (4, 41), (3, 41), (2, 41), (1, 41), (1, 42), (1, 43), (2, 43), (3, 43), (3, 44), (3, 45), (2, 45), (1, 45), (1, 46), (1, 47), (2, 47), (3, 47), (3, 48), (3, 49), (3, 50), (3, 51), (2, 51), (1, 51), (1, 52), (1, 53), (2, 53), (3, 53), (3, 54), (3, 55), (2, 55), (1, 55), (1, 56), (1, 57), (2, 57), (3, 57), (3, 58), (3, 59), (4, 59), (5, 59), (5, 58), (5, 57), (6, 57), (7, 57), (8, 57), (9, 57), (9, 58), (9, 59), (8, 59), (7, 59), (7, 60), (7, 61), (7, 62), (7, 63), (8, 63), (9, 63), (10, 63), (11, 63), (12, 63), (13, 63), (13, 62), (13, 61), (14, 61), (15, 61), (15, 62), (15, 63)]

intersect_from_a = [list(g) for k, g in groupby(a, lambda x: x not in b)]
intersect_from_b = [list(g) for k, g in groupby(b, lambda x: x not in a)]

merged_path = list()
for i in range(len(intersect_from_a)):
    if intersect_from_a[i] == intersect_from_b[i]:
        for step in intersect_from_a[i]:
            merged_path.append(step)
    else:
        if len(intersect_from_a[i]) < len(intersect_from_b[i]):
            for step in intersect_from_a[i]:
                merged_path.append(step)
        else:
            for step in intersect_from_b[i]:
                merged_path.append(step)

print(merged_path)

'''
def lookup(iterable, length):
    tees = itertools.tee(iterable, length)
    for i, t in enumerate(tees):
        for _ in xrange(i):
            next(t, None)
    return itertools.izip(*tees)

def has_sequence(array, sequence):
    # Convert to tuple for easy testing later
    sequence = tuple(sequence)
    return any(group == sequence for group in lookup(array, len(sequence)))

def intersection(lst1, lst2): 
    lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2] 
    return lst3 

intersect = intersection(a, b)
print(intersect)
'''

'''
intersect = list(set(a).intersection(b))
print(intersect)
merged_path = list()

for foo, bar in itertools.zip_longest(a,b):
    if foo in intersect:
        merged_path.append(foo)

print(merged_path)

for entry in intersect:
    a.remove(entry)
    b.remove(entry)

print('a', a)
print('b', b)

'''

'''
merged_path = list()

index = 0
max_len = len(a)
if len(b) > len(a):
    max_len = len(b)

while index < max_len:
    foo = a[index]
    bar = b[index]
    if foo in b and a.index(foo) == b.index(foo):
        merged_path.append(foo)
        a.remove(foo)
        b.remove(bar)
        max_len = len(a)
        if len(b) > len(a):
            max_len = len(b)
    else:
        steps_a = 0
        steps_b = 0
        if foo in b:
            steps_a = a.index(foo)
            steps_b = b.index(foo)
        print(steps_a, steps_b)
        index += 1

print(merged_path)
'''