# 9 Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, 
# for which, a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which 
# a + b + c = 1000.
# Find the product abc.

for a in range(1, 1000):
    for b in range(a, 1000):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print a, b, c
            print a * b * c

            
# OTHER ATTEMPTS

# a = 1000
# b = 0
# c = 1000 - a - b
# product = a * b * c

# while True:
    # if a ** 2 + b ** 2 == c ** 2:
        # break
    # else:
        # if a > 0:
            # a -= 1
            # c = 1000 - a - b
        # else:
            
    # if a ** 2 + b ** 2 == c ** 2:
        # product = a * b * c
        # break
    # else:
        
        # a -= 1
        # b += 1
        # c = 1000 - a - b
        # print a, b, c

