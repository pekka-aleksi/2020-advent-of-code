import re
import collections

def get_data():
    with open('data.txt', 'rt') as file:
        buffer = file.read().splitlines()
        groups = [re.match(r'(\d+)-(\d+) (.): (.+)', row).groups() for row in buffer]
        letter_counts = [(letter, int(m), int(M)) for m, M, letter, _ in groups]
        passwords = [x[-1] for x in groups]
        return letter_counts, passwords

if __name__ == '__main__':

    lc, pw = get_data()


    def second():
        totals = 0
        for i, ((letter, a, b), password) in enumerate(zip(lc, pw)):
            try:
                if password[a-1] == password[b-1]:
                    continue
            except IndexError:
                continue

            if password[a-1] == letter or password[b-1] == letter:
                print(i, password, a, b, letter)
                totals += 1

        print(totals)




    def first():
        sorted_pw = ["".join(sorted(p)) for p in pw]

        assert len(lc) == 1000
        assert len(lc) == len(sorted_pw)

        total = 0
        for i, ((char, m, M), word) in enumerate(zip(lc, sorted_pw)):
            counter = collections.Counter(word)
            if int(m) <= counter[char] <= int(M):
                print(i, m, M, char, word)
                total += 1

        print(total)
