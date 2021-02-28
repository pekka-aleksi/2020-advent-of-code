
import re
from pprint import pprint


def get_data(filename='data.txt'):
    with open(filename, 'rt') as file:
        buffer = file.read().splitlines()
        return buffer



pattern = r'\(.*\)'

def split(data):
    rowstacks = dict()

    for i, row in enumerate(data):
        print(row)

        R = f'row{i}'
        rowstacks[R] = {0: {0: []}}
        stack_index, nest_depth = 0, 0

        for ch in row.replace(' ', ''):

            if ch == '(':
                stack_index +=1
                nest_depth += 1
                rowstacks[R][stack_index] = {nest_depth: []}

            elif ch == ')':
                stack_index += 1
                nest_depth -= 1
                rowstacks[R][stack_index] = {nest_depth: []}

            else:
                rowstacks[R][stack_index][nest_depth].append(ch)

    return rowstacks




data = get_data('test.txt')
splits = split(data)

from copy import deepcopy


for idx, (n, rowdata) in enumerate(splits.items()):

    full_clause = [depth for entry, depth in rowdata.items()]
    max_depth = max([list(entry.keys())[0] for entry in full_clause])

    print(data[idx])
    print(full_clause)
    for depth in range(max_depth, -1, -1):  # this has to be iterated for AS LONG as there are possible doings

        print("--------- LAYER ", depth)

        clause_changes = {}
        print("full clause", full_clause)

        for col, column in enumerate(full_clause):

            to_eval = column.get(depth, [])
            print(to_eval)
            operands = list(zip(to_eval, to_eval[1:], to_eval[2:]))

            result = int(operands[0][0]) if len(operands) else 0

            for A, op,  B in operands[::2]:
                #print(result,'\t', A, op, B)

                if result == 0:
                    result = A

                if op == '+':
                    result += int(B)
                elif op == '*':
                    result *= int(B)

            #print("RESULT", result)
            #print(f"--- {col}")

            if result != 0:
                clause_changes[col] = result

        for column, result in clause_changes.items():
            full_clause[column] = {depth-1: str(result)}

        print("full clause", full_clause)

    print(*["-"*80]*3, sep='\n')