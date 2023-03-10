
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

def is_perfect_square(x):
    temp = isqrt(x)
    if temp * temp == x:
        return True
    else:
        return False
