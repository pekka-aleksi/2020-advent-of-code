import collections

inp = {}


def first(inp, TURN=2020):
    LAST_PRINTED_NUMBER = list(inp.keys())[-1]

    print(LAST_PRINTED_NUMBER)

    K = TURN+2

    for NUMBER_ON_TURN in range(len(inp), K):

        turns_spoken_on = inp.get(LAST_PRINTED_NUMBER, [])

        if not turns_spoken_on:
            turns_spoken_on = inp.get(LAST_PRINTED_NUMBER, [])

        if len(turns_spoken_on) == 1:

            if NUMBER_ON_TURN == TURN:
                print(LAST_PRINTED_NUMBER, "-> 0")

            if not inp.get(0):
                inp[0] = list()
            inp[0].append(NUMBER_ON_TURN)

            LAST_PRINTED_NUMBER = 0

        else:

            latest_turn_update = turns_spoken_on[-1] - turns_spoken_on[-2]

            LAST_PRINTED_NUMBER = latest_turn_update

            if NUMBER_ON_TURN == TURN - 1:
                print(NUMBER_ON_TURN, f"-> {latest_turn_update} *")

            if not inp.get(latest_turn_update):
                inp[latest_turn_update] = list()

            inp[latest_turn_update].append(NUMBER_ON_TURN)


data = {1: [0], 20: [1], 8: [2], 12: [3], 0: [4], 14: [5] } #

test1 = {0: [0], 3: [1], 6: [2]}

tests = [{1: [0], 3: [1], 2: [2]},
         {2: [0], 1: [1], 3: [2]},
         {1: [0], 2: [1], 3: [2]},
         {2: [0], 3: [1], 1: [2]},
         {3: [0], 2: [1], 1: [2]},
         {3: [0], 1: [1], 2: [2]}]


[first(data, 30_000_000) for test in tests]

