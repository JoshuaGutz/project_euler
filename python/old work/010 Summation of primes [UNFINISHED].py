# 10 Summation of primes

def instructions():
    # The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    # Find the sum of all the primes below two million.
    pass
pass

def is_prime(number):
    count = number / 2
    while count > 1:
        if number / count * count == number:
            return False
            break
        else:
            count -= 1
    return True
pass

i = 3
total = 2 # 2 from the prime number 2
while i < 2000000:
    if is_prime(i):
        total += i
        print i, "is prime", total
    i += 2
pass

print total