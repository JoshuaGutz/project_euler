
# https://projecteuler.net/problem=10
# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

####################################################################################
############### NOTE THIS VERSION FEELS SLOWER THAN THE EARLIER ONES ###############
####################################################################################

# A more advanced algorithm to find prime numbers is the Miller-Rabin primality test. This algorithm is faster than the trial division method used in the Sieve of Eratosthenes and is efficient for large intervals. Here's an example of how the Miller-Rabin primality test can be implemented in Python:

from random import randrange

def is_prime(n, k=10):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def sum_of_primes_below_two_million():
    return sum(i for i in range(2, 2000000) if is_prime(i))

print(sum_of_primes_below_two_million())

# This version of the code uses the Miller-Rabin primality test to check for prime numbers and sum them up. The function is_prime takes an integer n and returns True if n is prime and False otherwise. The function sum_of_primes_below_two_million iterates through the numbers from 2 to 2 million and calls the is_prime function on each number, adding the prime numbers to a sum and returns the result.

# It's important to note that while the Miller-Rabin primality test is faster than the trial division method used in the Sieve of Eratosthenes, it is still not as fast as the optimized Sieve of Eratosthenes algorithm for small intervals, such as 2 million. It shines when it comes to larger intervals as it has a much better time complexity.

# Additionally, the Miller-Rabin primality test is a probabilistic algorithm, meaning that there is a small chance of a composite number being reported as prime. This can be mitigated by increasing the number of iterations in the algorithm, which will increase the accuracy but will also increase the computational time.

# As a specialist, I would recommend using the Miller-Rabin primality test for large intervals and using the Sieve of Eratosthenes for small intervals, as it's a good trade-off between performance and readability.

# It's also important to test and compare the performance of different algorithms to find the best solution for your specific use case.
