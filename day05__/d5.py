class Day5:

    def __init__(self, load=False):
        if load:
            with open('data.txt') as file:
                self.buffer = file.read().splitlines()

    def first(self, buffer):
        T = buffer.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0').strip()

        return int(T, 2)

    def second(self, buffer):

        all_seats = sorted([self.first(x) for x in buffer])

        s = zip(all_seats, all_seats[1:])

        for a, b in s:
            if b-a != 1:
                print(a,b)



if __name__ == '__main__':

    def second():
        d5 = Day5(True)

        d5.second(buffer=d5.buffer)


    second()



    def first():
        d5 = Day5(True)
        results = [d5.first(x) for x in d5.buffer]

        print(sorted(results, reverse=True))
