import re

class Day4():

    def __init__(self, filename="data.txt"):
        with open(filename, 'rt') as file:
            buffer = "|".join(file.read().splitlines())
            self.passports = [k.replace('|', ' ') for k in buffer.split('||')]



    def first(self, buffer):

        splits = [STR for STR in buffer.split()]

        fuk = dict()
        for word in splits:
            a, b = word.split(':')
            fuk[a] = b


        if len(fuk) == 7 and 'cid' not in fuk:
            return True

        if 'hgt' not in fuk:
            return False

        if len(fuk) < 7:
            return False

        if len(fuk) == 8:
            return True

    def second(self, buffer):

        splits = [STR for STR in buffer.split()]

        fuk = dict()
        for word in splits:
            a, b = word.split(':')
            fuk[a] = b


        required_fields = {'byr': r'(19[2-8][0-9]|199[0-9]|200[0-2])',
                           'iyr': r'(201[0-9]|2020)',
                           'eyr': r'(202[0-9]|2030)',
                           'hgt': r'((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in)',

                           'hcl': r'#[0-9a-f]{6}',
                           'ecl': r'amb|blu|brn|gry|grn|hzl|oth',


                           'pid': r'\d{9}',
                           }


        for key, pattern in required_fields.items():

            D = fuk.get(key, '----------')

            print(key, D)
            M = re.findall(f"^{pattern}$", D)

            print(M)
            #if len(M)>1:
            #    print(M)

            if len(M) > 1 or not M:
                print( "->", key, pattern, f'"{D}"', fuk, )
                return False

        return True



if __name__ == '__main__':

    d4 = Day4()


    def second():
        t = 0
        for passport in d4.passports:

            if d4.first(passport) and d4.second(passport) :
                t += 1

                print("-"*80)
        return t



    def first():
        t = 0
        for passport in d4.passports:
            if d4.first(passport):
                t += 1


        return t


    print(second())
