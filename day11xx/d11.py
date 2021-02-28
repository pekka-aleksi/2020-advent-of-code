import itertools


def get_data(filename):
    with open(filename, 'rt') as file:
        buffer = file.read().splitlines()
        return buffer


data = get_data('data.txt')


def get_neighbors(d, datadimension=(99, 93)):

    neighbors = list(itertools.product((0, -1, +1), repeat=2))

    neighbors = {tuple(min(max(x + C, 0), datadimension[dim])
                       for dim, (x, C) in enumerate(zip(neighbor, d))) for neighbor in neighbors} - {d}
    return neighbors


occupied = set()
empty = set()

for y, row in enumerate(data):
    for x, col in enumerate(row):
        if col == 'L':
            empty.add((x, y))

while True:
    will_be_occupied = set()
    will_be_empty = set()

    for coordinate in empty:
        neighbors = get_neighbors(coordinate)
        if not neighbors.intersection(occupied):
            will_be_occupied.add(coordinate)

    for coordinate in occupied:
        neighbors = get_neighbors(coordinate)
        if len(neighbors.intersection(occupied)) >= 4:
            will_be_empty.add(coordinate)

    occupied = occupied - will_be_empty
    occupied = occupied.union(will_be_occupied)

    empty = empty - will_be_occupied
    empty = empty.union(will_be_empty)

    if not will_be_empty and not will_be_occupied:
        print(len(occupied), len(empty))
        break
