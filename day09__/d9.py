def get_data():
    with open('data.txt', 'rt') as file:
        buffer = file.read().splitlines()
        buffer = list(map(int, buffer))
        return buffer



data = get_data()

def find_pair(S, target):

    for a in S:
        for b in S:
            if a+b == target:
                return True

    return False

def first(data):
    for i in range(len(data)):

        slc = data[i: i+26]
        if not find_pair(slc[:-1], slc[-1]):
            print(slc[-1])
            break



def cumulative_sum(S, target):

    for i, a in enumerate(S):
        acc = 0
        for j, b in enumerate(S[i:],0):
            acc += b
            if acc == target:
                #print(i, j, acc)
                print(f"found target {acc} {i}-{i+j}")
                return i, j


def second(data):
    first, last = cumulative_sum(data, 26796446)

    A, B = min(data[first: first+last+1]), max(data[first: first+last+1])
    print(" + ".join(map(str,data[first: first+last+1])), "=", sum(data[first: first+last+1]))
    print(A, "+", B, "=", A+B)
    assert 26796446 == sum(data[first: first+last+1])
    assert 3184168 == A+B


second(data)