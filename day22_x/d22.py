from collections import deque

def get_data(filename='data.txt'):
    with open(filename, 'rt') as file:
        buffer = "|".join(file.read().splitlines())
        players = buffer.split('||')

        data_a, data_b = (*players,)

        A = deque(map(int, data_a.split('|')[1:]))
        B = deque(map(int, data_b.split('|')[1:]))

        return A,B

A, B = get_data('data.txt')

def first(A, B):

    while len(A) and len(B):
        if A[0] > B[0]:
            a_right = B.popleft()
            A.rotate(-1)
            A.append(a_right)
        else:
            b_right = A.popleft()
            B.rotate(-1)
            B.append(b_right)

    X, Y = sum([k * x for k, x in enumerate(reversed(B), 1)]), sum([k * x for k, x in enumerate(reversed(A), 1)])

    return max(X, Y)

val= first(A,B)
print(val)