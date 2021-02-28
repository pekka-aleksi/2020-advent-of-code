def first(S):

    indeksi = 0
    L = 3
    N = len(S) - L


    # the indexing for the cups starts at 1 but our indexing starts at 0, fix that

    for i in range(3):
        print(S)

        next_destination = (S[indeksi] - 1) % N

        picks = S[indeksi + 1: indeksi + L + 1]

        moving_index = 1

        while next_destination in picks:
            print(next_destination)
            next_destination = (S[indeksi - moving_index ]) % N
            moving_index += 1


        indeksi = (indeksi + 1) % N




test = [int(k) for k in "389125467"]



first(test)







X = "368195742"

