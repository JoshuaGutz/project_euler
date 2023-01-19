# 4 Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit 
# numbers.

def isPalendromic(n):
    n_reverse = list(str(n))
    n_original = list(str(n))
    n_reverse.reverse()
    if n_original == n_reverse:
        return True
    else:
        return False

i = 999
answer = 0
while i >= 100:
    j = 999
    while j >= 100:
        if isPalendromic(i * j):
            if i * j > answer:
                print i,"*", j, "=", i * j
                answer = i * j
        j -= 1
    i -= 1
print answer