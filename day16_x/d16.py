import re

def get_data(filename='data.txt'):
    with open(filename, 'rt') as file:
        buffer = "|".join(file.read().splitlines())
        return buffer.split('||')

rules, _, tickets = get_data()

rule_pattern = r'(\d+)-(\d+) or (\d+)-(\d+)$'

rule_legals = []

for rule in rules.split('|'):
    a,b, c,d = re.findall(rule_pattern, rule)[0]

    first = {x for x in range(int(a), int(b)+1)}
    second = {x for x in range(int(c), int(d)+1)}

    legal = first.union(second)
    rule_legals.append(legal)


problems = 0
broken_tickets = []
for i, ticket in enumerate(tickets.split('|')[1:]):

    #print(ticket)
    ticket_entries = {int(v) for v in ticket.split(',')}

    for entry in ticket_entries:
        #print(f"Trying entry {entry}")
        for ruleset in rule_legals:
            #print(ruleset)
            if entry in ruleset:
                break
        else:
            problems += entry
            broken_tickets.append(i)

print(problems)
print(broken_tickets)