#! /usr/bin/env python

import sys
from itertools import product, combinations

grid_size = int(sys.argv[1])

def mirror_0(x):
    return x[0], grid_size + 1 - x[1]

def mirror_45(x):
    return grid_size + 1 - x[1], grid_size + 1 - x[0]

def mirror_90(x):
    return grid_size + 1 - x[0], x[1]

def mirror_135(x):
    return x[1], x[0]

def rotate_90(x):
    return x[1], grid_size + 1 - x[0]

def sort_arrangement(arrangement):
    return tuple(sorted(arrangement, key=lambda x: (x[0], x[1])))

def transform(arrangement, fn):
    return sort_arrangement(map(fn, arrangement))

coords = product(range(1, grid_size + 1), repeat=2)
arrangements = combinations(coords, grid_size)

solutions = set()
i = 1
for arrangement in arrangements:
    print('Test arrangement', i)
    i += 1
    distances = set()
    for first, second in combinations(arrangement, 2):
        distances.add((first[0] - second[0])**2 + (first[1] - second[1])**2)
    if len(distances) == grid_size * (grid_size - 1) / 2:
        if transform(arrangement, mirror_0) in solutions:
            continue
        if transform(arrangement, mirror_45) in solutions:
            continue
        if transform(arrangement, mirror_90) in solutions:
            continue
        if transform(arrangement, mirror_135) in solutions:
            continue
        rot90 = transform(arrangement, rotate_90)
        if rot90 in solutions:
            continue
        rot180 = transform(rot90, rotate_90)
        if rot180 in solutions:
            continue
        rot270 = transform(rot180, rotate_90)
        if rot270 in solutions:
            continue
        solutions.add(arrangement)

for solution in solutions:
    print(solution)

