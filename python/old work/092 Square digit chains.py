# 92 Square digit chains

# A number chain is created by continuously adding the square of the 
# digits in a number to form a new number until it has been seen before.
# For example,
# 44 >> 32 >> 13 >> 10 >> 1 >> 1
# 85 >> 89 >> 145 >> 42 >> 20 >> 4 >> 16 >> 37 >> 58 >> 89
# Therefore any chain that arrives at 1 or 89 will become stuck in an 
# endless loop. What is most amazing is that EVERY starting number will 
# eventually arrive at 1 or 89.
# How many starting numbers below ten million will arrive at 89?

def next_number(n): # returns number after n
    next_number = 0
    for i in list(str(n)):
        next_number += int(i) ** 2
    return next_number

def number_chain_ending(n): # returns either 1 or 89
    while n != 1 and n != 89:
        n = next_number(n)
    return n

###count those that end in 1 and subtract from (10,000,000 - 1)
# i = 1
# count = 0
# end_in_1 = set([1])
# while i < 10000000:
    # if i in end_in_1:
        # count += 1
    # elif number_chain_ending(i) == 1:
        # print i
        # end_in_1.add(i)
        # count += 1
    # i += 1

# print (10000000 - 1) - count
### printed 8581146 (took awhile to run)


### count down from 10000000 - 1, storing numbers seen in chains in sets
# i = 10000000 - 1
# count = 0
# end_in_1 = set([1])
# end_in_89 = set([89])
# while i > 0:
    # if i in end_in_89:
        # count += 1
    # elif i in end_in_1:
        # pass
    # elif number_chain_ending(i) == 89:
        # end_in_89.add(i)
        # i_next = next_number(i)
        # while not (i_next in end_in_89):
            # end_in_89.add(i_next)
            # i_next = next_number(i_next)
        # count += 1
    # elif number_chain_ending(i) == 1:
        # end_in_1.add(i)
        # i_next = next_number(i)
        # while not (i_next in end_in_1):
            # end_in_1.add(i_next)
            # i_next = next_number(i_next)
        # print i, count
    # i -= 1
# print count
### printed 8581146 (took awhile to run)

# i = 1
# count = 0
# end_in_1 = set([1])
# end_in_89 = set([89])
# while i < 10000000:
    # if i in end_in_89:
        # count += 1
    # elif i in end_in_1:
        # pass
    # elif number_chain_ending(i) == 89:
        # end_in_89.add(i)
        # count += 1
    # elif number_chain_ending(i) == 1:
        # print i
        # end_in_1.add(i)
    # i += 1
# print count

# i = 1
# count = 0
# end_in_89 = set([89])
# while i < 10000000:
    # if i in end_in_89:
        # count += 1
    # elif number_chain_ending(i) == 89:
        # print i
        # end_in_89.add(i)
        # count += 1
    # i += 1

# print count

# print number_chain_ending(1),
# print number_chain_ending(44),
# print number_chain_ending(32),
# print number_chain_ending(13),
# print number_chain_ending(10)
# print number_chain_ending(89),
# print number_chain_ending(85),
# print number_chain_ending(145),
# print number_chain_ending(42),
# print number_chain_ending(20),
# print number_chain_ending(4),
# print number_chain_ending(16),
# print number_chain_ending(37),
# print number_chain_ending(58)