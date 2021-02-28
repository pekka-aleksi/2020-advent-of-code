import re

def get_data(filename='data.txt'):
    with open(filename, 'rt') as file:
        buffer = file.read().splitlines()

        pattern = r'(\w*)[,)]'
        allergens = [re.findall(pattern, row) for row in buffer]
        data = [{*row.rsplit(' (')[0].split()} for row in buffer]

        return data, allergens




data, allergens = get_data('test.txt')


# each single allergen is found by taking the intersection of each recipe where it's found
# then the next step is to take the Multiple - Single information where the solution isn't known

allergen_recipes = {A[0]:R for A, R in zip(allergens, data) if len(A) == 1}

print(allergen_recipes)

