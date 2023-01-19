
# https://projecteuler.net/problem=10
# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

###################################################################################
############### NOTE THIS VERSION GETS THE WRONG ANSWER 27931306768 ###############
###################################################################################

# going back to the code for the Sieve of Eratosthenes algorithm using a bit array instead of a regular array to store the prime numbers

# here is an example of how the Sieve of Eratosthenes algorithm can be implemented using a bit array instead of a regular array to store the prime numbers:

import array

def sum_of_primes_below_two_million():
    limit = 2000000
    primes = array.array('B', [1] * (limit // 8 + 1))
    primes[0] = primes[1] = 0

    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i // 8] & (1 << (i % 8)):
            for j in range(i * i, limit, i):
                primes[j // 8] &= ~(1 << (j % 8))

    return sum(i for i in range(limit) if primes[i // 8] & (1 << (i % 8)))

print(sum_of_primes_below_two_million())

# This version of the code uses a bit array to store the prime numbers, which greatly reduces the memory usage of the algorithm and makes it more efficient.

# It's important to note that the bit array version of the algorithm can be harder to understand and maintain than the regular array version, but it can be more memory-efficient for larger intervals.
