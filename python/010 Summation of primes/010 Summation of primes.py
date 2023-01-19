
# https://projecteuler.net/problem=10
# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def sum_of_primes_below_two_million():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [2]
    for i in range(3, 2000000):
        if is_prime(i):
            primes.append(i)
    return sum(primes)

print(sum_of_primes_below_two_million())

# This code uses a nested function to check whether a given number is prime or not, and then iterates through numbers from 3 to 2 million, adding all prime numbers found to a list, and finally returns the sum of all prime numbers in the list.

# However, this code would be very slow because it check prime number one by one, so you can use Sieve of Eratosthenes for a more efficient solution.
