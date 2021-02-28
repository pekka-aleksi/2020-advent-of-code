def get_data():
    with open('data.txt', 'rt') as file:
        buffer = [(a[0], int(a[1:])) for a in file.read().splitlines()]
        return buffer


data = get_data()


def second(data):

    # +0   E: ( x, y)
    # +90  S: (-y, x)
    # +180 W: (-x, y)
    # +270 N: ( y,-x)


    wx, wy = 10, -1
    wangle = 0

    mapdict = {0: lambda a:   (a[0], a[1]),
               90: lambda a:  (-a[1], a[0]),
               180: lambda a: (-a[0], -a[1]),
               270: lambda a: (a[1], -a[0])}


    directiondict = {'E': (1, 0), 'S': (0, 1), 'W': (-1, 0), 'N': (0,-1)}

    sx, sy = 0, 0

    for instruction, number in data:
        #

        if instruction == 'R':
            print(instruction, number)
            print(f"before rotation at {wangle}     ({wx}, {wy})")
            wangle = (wangle + number) % 360
            wx, wy = mapdict[wangle]((wx,wy))
            print(f"rotating RIGHT+{number} to {wangle}   ({wx}, {wy})")

        elif instruction == 'L':
            print(instruction, number)
            print(f"before rotation {wangle}       ({wx}, {wy})")
            wangle = (wangle - number) % 360
            wx, wy = mapdict[wangle]((wx,wy))
            print(f"rotating LEFT-{number} to {wangle} ({wx}, {wy})")

        elif instruction in directiondict:
            nx, ny = directiondict[instruction]
            wx += number*nx
            wy += number*ny

        elif instruction == 'F':
            sx += number*wx
            sy += number*wy
            #print(f"going forward {number} to {sx} {sy}")

    print(sx, sy, abs(sx) + abs(sy))


second(data)




def first(data):

    angle = 0

    angledict = {0: 'E', 90: 'S', 180: 'W', 270: 'N'}
    directiondict = {'E': (1, 0), 'S': (0, 1), 'W': (-1, 0), 'N': (0,-1)}

    x, y = 0, 0

    for instruction, number in data:
        print(instruction, number)
        if instruction == 'R':
            angle = (angle + number) % 360

        elif instruction == 'L':
            angle = (angle - number) % 360

        elif instruction in angledict.values():
            nx, ny = directiondict[instruction]
            x += number*nx
            y += number*ny

        elif instruction == 'F':

            instruction = angledict[angle]
            nx, ny = directiondict[instruction]

            x += number*nx
            y += number*ny
            print(f"going forward {number} to {x} {y}")

    print(x, y, abs(x) + abs(y))




#first(data)
