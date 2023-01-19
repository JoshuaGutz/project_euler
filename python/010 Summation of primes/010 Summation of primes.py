
# https://projecteuler.net/problem=10
# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

####################################################################################
############### NOTE THIS VERSION GETS THE RIGHT ANSWER 142913828922 ###############
####################################################################################

# The problem with the code is that it is checking the bit value of the prime numbers in the array, but it should be checking the bit value of the composites. In other words, if the bit value is 1, it means the number is composite and should be excluded from the sum, whereas if the bit value is 0, it means the number is prime and should be included in the sum.

# Here is the corrected version of the code:

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

# This is the correct version of the code, It uses a bit array to store the composite numbers, which greatly reduces the memory usage of the algorithm and makes it more efficient. The iteration starts from 2 till the square root of limit and for each prime number, it marks all the multiples of that number as composite numbers. Finally, it returns the sum of all prime numbers that are not marked as composite numbers.
