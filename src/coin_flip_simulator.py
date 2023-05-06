from coin_flip import coin_flip

def coin_flip_simulator(flips):
    heads_count = 0
    tails_count = 0

    for _ in range(flips):
        result = coin_flip()
        if result == 'Heads':
            heads_count += 1
        else:
            tails_count += 1

    return heads_count, tails_count
