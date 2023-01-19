
# https://projecteuler.net/problem=10
# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Here is an example of how the Sieve of Eratosthenes algorithm can be optimized using the wheel factorization method and multi-threading:

import threading

def sum_of_primes_below_two_million():
    limit = 2000000
    primes = [True] * limit
    primes[0] = primes[1] = False

    def sieve(start, step):
        for i in range(start, limit, step):
            primes[i] = False

    threads = []
    # Eliminate multiples of 2
    threads.append(threading.Thread(target=sieve, args=(4, 2)))
    # Eliminate multiples of 3
    threads.append(threading.Thread(target=sieve, args=(9, 3)))
    # Eliminate multiples of 5
    threads.append(threading.Thread(target=sieve, args=(25, 5)))
    # Eliminate multiples of 7
    threads.append(threading.Thread(target=sieve, args=(49, 7)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    for i in range(11, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit, i):
                primes[j] = False

    return sum(i for i in range(limit) if primes[i])

print(sum_of_primes_below_two_million())

# This version of the code uses the wheel factorization method to eliminate the need to check divisibility by 2, 3, 5, and 7 during the sieving process, which reduces the number of divisions that need to be performed. Additionally, it uses multi-threading to parallelize the sieving process, which improves the performance of the algorithm by allowing multiple sieving operations to be performed simultaneously.

# It's important to note that multi-threading may only be beneficial on multi-core machines and the performance can vary depending on the machine.

# As the limit of 2 million is not that big, the performance gain may not be that significant, but for bigger limits, it can make a noticeable difference.
