def get_data(filename='data.txt'):
    with open(filename, 'rt') as file:
        return [line*10000 for line in file.read().splitlines()]

JUMPS = [(1,1), (3,1), (5,1), (7,1), (1,2)]
mult = 1

data = get_data()

for X_JUMP, Y_JUMP in JUMPS:

    sx, sy = 0, 0
    collisions = 0
    for row in data[::Y_JUMP]:
        if row[sx] == '#':
            collisions += 1
        sx += X_JUMP

    mult *= collisions
    print(collisions, mult)
    print("-"*80)

print(mult)