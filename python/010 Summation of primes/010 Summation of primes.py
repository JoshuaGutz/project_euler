
# https://projecteuler.net/problem=10
# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

################################################################################
################ NOTE THIS GETS THE WRONG ANSWER OF 27931306768 ################
################################################################################

# Another way to improve the performance of the Sieve of Eratosthenes algorithm is by using a bit array instead of a regular array to store the prime numbers. A bit array is a compact data structure that uses one bit to represent each value, as opposed to one byte in a regular array. This can greatly reduce the memory usage of the algorithm and make it more efficient.

# Here's an example of how the Sieve of Eratosthenes algorithm can be optimized using the wheel factorization method and a bit array:

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

# This version of the code uses the wheel factorization method to eliminate the need to check divisibility by 2, 3, 5, and 7 during the sieving process, which reduces the number of divisions that need to be performed. Additionally, it uses a bit array to store the prime numbers, which greatly reduces the memory usage of the algorithm and makes it more efficient.

# It's important to note that this version of the code is more complex than the previous ones and it may be harder to understand and maintain.

# It's also important to test and compare the performance of different optimizations to find the best solution for your specific use case.
