import re
import collections
import networkx as nx

def get_data(filename='data.txt'):
    with open(filename, 'rt') as file:
        buffer = file.read().splitlines()
        pattern = re.compile(r'(\w+ \w+)')
        data = collections.defaultdict(dict)

        for b in buffer:
            root = re.findall(pattern, b)[0]
            targets = b.split("bags contain ")[-1]

            splits = targets.split(', ')
            targets = [tuple(*re.findall(r'(\d) (\w+ \w+)', targ)) for targ in splits]
            targets = [t for t in targets if t]

            for weight, target in targets:
                data[root][target] = int(weight)

        return data

data = get_data('data.txt')

edges = [(fro, to, weight) for fro, targets in data.items() for to, weight in targets.items()]

g = nx.MultiDiGraph()
g.add_nodes_from(data.keys())
g.add_weighted_edges_from(edges)

set_to_follow = {*g.predecessors('shiny gold')}

finals = set()

while True:
    next_set_to_follow = set()
    for node in set_to_follow:
        predecessors = {k for k in g.predecessors(node)}
        finals.add(node)
        next_set_to_follow = next_set_to_follow.union(predecessors)
    if not next_set_to_follow:
        break
    set_to_follow = next_set_to_follow

print(len(finals))