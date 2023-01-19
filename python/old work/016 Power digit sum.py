# 16 Power digit sum

def instructions():
    # 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    # What is the sum of the digits of the number 2^1000?
    pass
pass

number = 2**1000
number_as_string = str(number)
total = 0

for i in range(len(number_as_string)):
    total += int(number_as_string[i])
    
print total

# Returns 1366