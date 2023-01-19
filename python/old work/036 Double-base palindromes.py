# 36 Double-base palindromes
# The decimal number, 585 = 10010010012 (binary), is palindromic in 
# both bases.

# Find the sum of all numbers, less than one million, which are 
# palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not 
# include leading zeros.)

import math
def isPrime(n):
	for m in range(2,int(math.sqrt(n))+1):
	    if n % m == 0:
	        return False
        else:
	        return True

def isPalendromic(n):
    n_reverse = list(str(n))
    n_original = list(str(n))
    n_reverse.reverse()
    if n_original == n_reverse:
        return True
    else:
        return False

def binary_int(n):
    return int(bin(n)[2:])

i = 0
sum = 0
while True:
    if i < 1000000:
        if isPalendromic(i) and isPalendromic(binary_int(i)):
            sum += i
        i += 1
    else:
        break

print sum