def get_data(filename='data.txt'):
    with open(filename, 'rt') as file:
        buffer = "|".join(file.read().splitlines()).split('||')

        data = {int(row.split('|')[0][-5:-1]): row.split('|')[1:] for row in buffer}

        return data


data = get_data()
from pprint import pprint

pprint(data)