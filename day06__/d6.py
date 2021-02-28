def get_data():
    with open('data.txt', 'rt') as file:
        buffer = "|".join(file.read().splitlines())
        return buffer.split('||')

data = get_data()

def first(data):
    data = [k.replace('|', '') for k in data]
    totals = sum([len(set(group)) for group in data])
    print(totals)

def second(data):
    totals = 0

    for group in data:
        members = group.split('|')
        all_yes = set.intersection(set(member) for member in members)
        totals += len(all_yes)

    print(totals)


first(data)
#second(data)