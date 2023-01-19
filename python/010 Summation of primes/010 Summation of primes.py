
# https://projecteuler.net/problem=10
# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

###################################################################################
############### NOTE THIS VERSION GETS THE WRONG ANSWER 27931306768 ###############
###################################################################################

# The problem with the code is that it's only counting prime numbers in the range of 0 to limit, but the requirement was to find the sum of all the primes below two million.

# Here is the corrected version of the code:

import array

def sum_of_primes_below_two_million():
    limit = 2000000
    primes = array.array('B', [1] * (limit // 8 + 1))
    primes[0] = primes[1] = 0

    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i // 8] & (1 << (i % 8)):
            for j in range(i * i, limit, i):
                primes[j // 8] &= ~(1 << (j % 8))

    return sum(i for i in range(2, limit) if primes[i // 8] & (1 << (i % 8)))

print(sum_of_primes_below_two_million())

# In this corrected version, The range of the iteration starts from 2 instead of 0 and it ends at limit. Also, the sum that is returned is the sum of the prime numbers between 2 and limit instead of the sum of all numbers between 0 and limit.
