def get_data():
    with open('data.txt', 'rt') as file:
        buffer = file.read().splitlines()
        buffer = [(b[:3], int(b[4:])) for b in buffer]

        return buffer


data = get_data()


def first():

    accumulator = 0
    idx = 0

    visited = list()

    while idx not in visited:
        visited.append(idx)
        command, number = data[idx]

        if command == 'nop':
            idx += 1
        if command == 'jmp':
            idx += number
        if command == 'acc':
            idx += 1
            accumulator += number

    print(accumulator)
    print(idx, visited)


