
def get_data():
    with open('data.txt', 'rt') as file:
        buffer = file.read().splitlines()
        buffer = list(map(int, buffer))
        return buffer



def first_and_second():
    data = get_data()
    for first in data:
        for second in data:
            if first + second == 2020:
                print(first*second)

            for third in data:
                if first + second + third == 2020:
                    print(first*second*third)
