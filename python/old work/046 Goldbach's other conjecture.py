# 46 Goldbach's other conjecture

def instructions():
    # It was proposed by Christian Goldbach that every odd composite 
    # number can be written as the sum of a prime and twice a square.

    # 9 = 7 + 2 x 1^2
    # 15 = 7 + 2 x 2^2
    # 21 = 3 + 2 x 3^2
    # 25 = 7 + 2 x 3^2
    # 27 = 19 + 2 x 2^2
    # 33 = 31 + 2 x 1^2

    # It turns out that the conjecture was false.

    # What is the smallest odd composite that cannot be written as the 
    # sum of a prime and twice a square?
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

def isqrt(x):
    # http://code.activestate.com/recipes/577821-integer-square-root-function/
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def is_perfect_square(x): # returns True or False
    temp = isqrt(x)
    if temp * temp == x:
        return True
    else:
        return False
pass

Goldbachs_other_conjecture = True
test = 1


while Goldbachs_other_conjecture:
    test += 2
    if is_prime(test):
        print test, "is prime"
        continue
    number = 1
    twice_square = 2 * number * number
    while True:
        if twice_square < test:
            if is_prime(test - twice_square):
                print test, "=", test - twice_square, "+ 2 x", number, "^2"
                break
            number += 1
            twice_square = 2 * number * number
        else:
            Goldbachs_other_conjecture = False
            break
pass

print test