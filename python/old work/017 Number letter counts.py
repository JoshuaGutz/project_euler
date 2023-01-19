# 17 Number letter counts

def instructions():
    # If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    # If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
    # NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
    pass
pass

dictionary = {0:"",
                    1:"one",
                    2:"two",
                    3:"three",
                    4:"four",
                    5:"five",
                    6:"six",
                    7:"seven",
                    8:"eight",
                    9:"nine",
                    10:"ten",
                    11:"eleven",
                    12:"twelve",
                    13:"thirteen",
                    14:"fourteen",
                    15:"fifteen",
                    16:"sixteen",
                    17:"seventeen",
                    18:"eighteen",
                    19:"nineteen",
                    20:"twenty",
                    30:"thirty",
                    40:"forty",
                    50:"fifty",
                    60:"sixty",
                    70:"seventy",
                    80:"eighty",
                    90:"ninety",
                    100:"hundred",
                    1000:"thousand"}
pass

total = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            # number = i * 100 + j * 10 + k
            if j == 1:
                total += len(dictionary[i]) + len(dictionary[k + 10])
            else:
                total += len(dictionary[i]) + len(dictionary[j * 10]) + len(dictionary[k])
            if i > 0:
                total += len(dictionary[100])
                if j > 0 or k > 0:
                    total += len("and")

total += len(dictionary[1]) + len(dictionary[1000])
print total

# Returns 21124