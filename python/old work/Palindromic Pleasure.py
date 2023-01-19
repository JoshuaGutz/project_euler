# Palindromic Pleasure
# A palindromic number is any (real) number that is able to have its 
# digits reversed, and it stay the same number. For example, 11 is a 
# palindrome because if you reverse its digits, it is still 11. 92729 
# is another example, if you reverse the digits, it is still 92729. 
# Here is the problem:

# What is the only (double-digit, or above) Prime number that is 
# palindromic in both base-2 (binary), and base-10 (decimal) instances?

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

i = 10
while True:
    if isPrime(i):
        if isPalendromic(i):
            if isPalendromic(binary_int(i)):
                a = i
                print i
                print binary_int(i)
                break
    i += 1
