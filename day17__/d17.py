import itertools

def get_data(filename='data.txt'):
    with open(filename, 'rt') as file:
        buffer = file.read().replace('#', '1').replace('.', '0').splitlines()

        mines = set()
        for y, row in enumerate(buffer):
            for x, col in enumerate(row):
                if col == '1':
                    mines.add((x,y,0,0))

        return mines




actives = get_data('data.txt')


def get_neighbors(d):
    neighbors = list(itertools.product((0, -1, +1), repeat=len(d)))

    neighbors = {tuple(x + C for i, (x, C) in enumerate(zip(neighbor, d)))
                 for neighbor in neighbors}

    return neighbors - {d}


# we can always just count the actives and their immediate neighbors. we never have to care about inactives.

for kierros in range(7):
    print(kierros, len(actives))

    to_be_removed = set()
    to_be_added = set()

    for d in actives:
        N = get_neighbors(d)

        I = actives.intersection(N)

        if len(I) == 2 or len(I) == 3:
            pass
        else:
            to_be_removed.add(d)

        for n in N:
            nN = get_neighbors(n)
            nI = actives.intersection(nN)

            if len(nI) == 3:
                to_be_added.add(n)

    actives = actives - to_be_removed
    actives = actives.union(to_be_added)




