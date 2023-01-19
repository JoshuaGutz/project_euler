# 14 Longest Collatz 

# The following iterative sequence is defined for the set of positive 
# integers:

# n >> n/2 (n is even)
# n >> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following 
# sequence:

# 13 >> 40 >> 20 >> 10 >> 5 >> 16 >> 8 >> 4 >> 2 >> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) 
# contains 10 terms. Although it has not been proved yet 
# (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one 
# million.

def collatz_chain_length(number):
    new = number
    count = 1
    while new != 1:
        if new % 2 == 0:
            new = new / 2
        else:
            new = 3 * new + 1
        count += 1
    return count

i = 1
max_chain_length = 1
while i < 10 ** 6:
    i_collatz_length = collatz_chain_length(i)
    if i_collatz_length > max_chain_length:
        max_chain_length = i_collatz_length
        print i, "has length", i_collatz_length
    i += 1

# 837799 has length 525