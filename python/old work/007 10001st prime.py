# 7 10001st prime

def instructions():
    # By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we 
    # can see that the 6th prime is 13.

    # What is the 10 001st prime number?
    pass
pass

def is_prime(number):
    count = number / 2
    while count > 1:
        if number % count == 0:
            return False
            break
        else:
            count -= 1
    return True
pass

i = 2
test_prime = 3
while i <= 10001:
    if is_prime(test_prime):
        print i, test_prime
        i += 1
    test_prime += 2
pass

print "The 10001st prime is ", i, test_prime

###runs in about 2 minutes or so. Slows down close to 10001

# returns 104745