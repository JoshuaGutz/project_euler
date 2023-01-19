
# https://projecteuler.net/problem=10
# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def sum_of_primes_below_two_million():
    def sieve_of_eratosthenes(n):
        primes = [True] * (n + 1)
        primes[0] = False
        primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    primes = sieve_of_eratosthenes(2000000)
    return sum(i for i in range(len(primes)) if primes[i])

print(sum_of_primes_below_two_million())

# This code uses the Sieve of Eratosthenes algorithm to efficiently find all prime numbers below 2 million. The function sieve_of_eratosthenes returns a list of booleans representing whether each number from 0 to 2 million is prime or not. Then it iterates through this list and adds all prime numbers to a sum and returns the result. This solution is much more efficient than the previous one.
