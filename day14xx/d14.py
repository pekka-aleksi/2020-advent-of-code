import re

def get_data(filename='data.txt'):
    with open(filename, 'rt') as file:
        buffer = file.read().split('mask = ')[1:]

        return buffer


data = get_data('test.txt')

masked_entries = dict()

for mask in data:

    entries = mask.splitlines()
    mybin = entries[0]#tuple((idx, value) for idx, value in enumerate(entries[0]) if value in {'0', '1'})

    masked_entries[mybin] = list()

    for entry in entries[1:]:
        match = re.match(r'mem\[(\d+)\] = (\d+)', entry)
        addr, num = match.group(1), match.group(2)
        masked_entries[mybin].append((int(addr), int(num)))

memory_value = 0

# does it matter if my native dtypes are not the correct size
# can we play with memory_value simulating a 36-bit value?
# it might not be enough though

M = 12
for mask, items in masked_entries.items():

    print("maski", mask[M:])

    for address, value in items:
        print(f"address {address} and value {value}")

        # kuinka uusi arvo lisätään +memory_value?
        ## onko turvallista vain lisätä ja sitten poistaa bitit, vai pitäisikö lisäyskin tehdä bittilisäyksenä?
        new_value = f"{bin(value)[2:]:0>{36}}"
        memory_bin = f"{bin(memory_value)[2:]:0>{36}}"

        memory_bin = "".join([f"{int(a)|int(b)}" for a,b in zip(memory_bin, new_value)])


        print("binary value", memory_bin)
        mask_binary = list(zip(mask[M:], memory_bin[M:]))
        print("mask binary", mask_binary)
        memory_value = [mask if mask in {'0', '1'} else x for mask, x in mask_binary]
        print(memory_value)
        memory_value = int("".join(memory_value[M:]), 2 )
        print("memory value", memory_value)




        print(mask_binary)
        #print(mask_binary)

        print(memory_value)




# print(memory_value)
