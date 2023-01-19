# 1 Multiples of 3 and 5

def instructions():
    # If we list all the natural numbers below 10 that are multiples of 
    # 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    # Find the sum of all the multiples of 3 or 5 below 1000.
    pass
pass

test = 1
sum = 0
while test < 1000:
    if test % 3 == 0:
        sum += test
    elif test % 5 == 0:
        sum += test
    test += 1
print sum