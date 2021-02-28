def get_data(filename='data.txt'):
    with open(filename, 'rt') as file:
        buffer = file.read().splitlines()
        target = buffer[0]
        busses = "".join(buffer[1:]).split(',')
        return target, busses

target, busses = get_data()

def first(target, busses):
    numbers = sorted([int(n) for n in busses if n != 'x'])

    for route_length in numbers:
        routes_number, minutes_until_next_route = divmod(int(target), route_length)
        to_wait = route_length - minutes_until_next_route
        print(route_length, to_wait)


def second(busses):
    numbers = [(i, int(n)) for i, n in enumerate(busses) if n != 'x']

    MAX = 5_000_000_000
    legal_multiples = {k for k in range(MAX)}

    ZIP = zip(numbers, numbers[1:])

    for (idx_a, a), (idx_b, b) in ZIP:

        first_multiples = {a*i-idx_a for i in range(1_000_000_000)}
        second_multiples = {b*i-idx_b for i in range(1_000_000_000)}

        these_multiples = first_multiples.intersection(second_multiples)
        legal_multiples = legal_multiples.intersection(these_multiples)

    print(sorted(legal_multiples)[0])


def test():
    for i in range(2, 7):
        target, busses = get_data(f'test{i}.txt')
        print(target)

        second(busses)
        print("-" * 80)

test()
#second(busses)
