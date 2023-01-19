import array

def sum_of_primes_below_two_million():
    limit = 2000000
    primes = array.array('B', [1] * (limit // 8 + 1))
    primes[0] = primes[1] = 1

    for i in range(2, int(limit ** 0.5) + 1):
        if not primes[i // 8] & (1 << (i % 8)):
            for j in range(i * i, limit, i):
                primes[j // 8] |= (1 << (j % 8))

    return sum(i for i in range(2, limit) if not primes[i // 8] & (1 << (i % 8)))

print(sum_of_primes_below_two_million())
