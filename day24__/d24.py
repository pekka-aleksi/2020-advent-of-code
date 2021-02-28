import collections

def get_data(filename='data.txt'):
    with open(filename, 'rt') as file:
        buffer = file.read().splitlines()

        rows = []
        for j, row in enumerate(buffer):
            row = row.replace('ne', '0').replace('nw', '1').replace('se', '2').replace('sw', '3')
            parsed_row = [coordinate_mapping[d] for d in row]
            rows.append(parsed_row)

        return rows


coordinate_mapping = {'e': (1, 0), 'w': (-1, 0), '0': (+1, -1), '1': (0, -1), '2': (0, +1), '3': (-1, +1)}

def first(data):

    tiles = []

    for d in data:
        counter = collections.Counter(d)
        vals = sorted(counter.items(), key=lambda a: a[0])
        tiles.append(vals)

    all_coords = list()

    for coord in tiles:

        multiplied_coords = [(mult*direction[0], mult*direction[1]) for direction, mult in coord]
        summed_coords = map(sum,zip(*multiplied_coords))

        all_coords.append(tuple(summed_coords))

    v = collections.Counter(all_coords)
    black_tiles = {item for item, value in v.items() if value % 2}

    print("Not divisible by two", len(black_tiles))

    return black_tiles


def get_neighbors(tile):

    neighbors = set()

    for value in coordinate_mapping.values():
        new_neighbor = tile[0]+value[0], tile[1]+value[1]
        neighbors.add(new_neighbor)

    return neighbors


data = get_data('data.txt')


ALL_black_tiles = first(data)


for k in range(0, 101):

    if k % 10 == 0:
        print(k, len(ALL_black_tiles))
        print()
        print("-" * 80)

    new_black_tiles = set()
    new_white_tiles = set()

    for black_tile in ALL_black_tiles:

        black_tile_neighbors = get_neighbors(black_tile)
        black_adjacents = black_tile_neighbors.intersection(ALL_black_tiles)
        white_adjacents = black_tile_neighbors - black_adjacents

        assert len(black_adjacents.union(white_adjacents)) == 6

        if len(black_adjacents) == 0 or len(black_adjacents) > 2:
            new_white_tiles.add(black_tile)

        for white_tile in white_adjacents:
            white_tile_neighbors = get_neighbors(white_tile)
            white_correct_adjacents = ALL_black_tiles.intersection(white_tile_neighbors)

            if len(white_correct_adjacents) == 2:
                new_black_tiles.add(white_tile)

    ALL_black_tiles = ALL_black_tiles - new_white_tiles
    ALL_black_tiles = ALL_black_tiles.union(new_black_tiles)
