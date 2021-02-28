real_card_pubkey, real_door_pubkey = 12_320_657, 9_659_666

card_loopsize, door_loopsize = 8, 11
card_pubkey, door_pubkey = 5_764_801, 17_807_724


def get_encryption_key(loopsize, N, SUBJECT=7):
    MOD = 20201227

    VALUE = 1

    for i in range(loopsize):
        VALUE = VALUE*SUBJECT
        VALUE = VALUE%MOD

        #if VALUE in N:
        #    print(i+1, VALUE)


    return VALUE


keys = {real_card_pubkey, real_door_pubkey}

#M = get_encryption_key(10_000_000, keys)

real_door_loopsize = 75188
real_card_loopsize = 6527904

print(get_encryption_key(loopsize=real_door_loopsize, N=None, SUBJECT=real_card_pubkey))
print(get_encryption_key(loopsize=real_card_loopsize, N=None, SUBJECT=real_door_pubkey))


