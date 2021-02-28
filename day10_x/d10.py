def get_data(filename='data.txt'):
    with open(filename, 'rt') as file:

        buffer = file.read().splitlines()
        buffer = list(map(int, buffer))
        return sorted(buffer)


data = get_data('test2')

print(data)
print(len(data))


counts = 1


# this seems like breadth-first search

for i, n in enumerate(data):

    candidates = set(data[i+1: i+4])
    legals = {n+1, n+2, n+3}

    choices = candidates.intersection(legals)



    print(n, candidates, choices)

    counts *= len(choices) if len(choices) else 1

print(counts)











def first(data):
    ones = []
    threes = []

    for idx in range(1,len(data)):

        if data[idx] - data[idx-1] == 1:
            ones.append(1)
        elif data[idx] - data[idx-1] == 3:
            threes.append(1)


    print(sum(ones), sum(threes), (len(ones)+1)*(1+len(threes)))