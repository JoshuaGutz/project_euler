# 35 Circular primes

# The number, 197, is called a circular prime because all rotations of 
# the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 
# 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

def circulate(number): # returns the number circulated one digit
    number_string = str(number)
    first_digit = int(number_string[0])
    power = len(number_string)
    new_number = number * 10 - first_digit * 10 ** power + first_digit
    return new_number

def is_prime(number): # returns true for prime numbers
    count = 2
    while count <= number / 2:
        if number % count == 0:
            return False
            break
        else:
            count += 1
    return True

def is_circular(number): # returns True or False
    check_number = number
    i = 1
    while i <= len(str(number)):
        if is_prime(check_number):
            check_number = circulate(check_number)
            i += 1
        else:
            return False
            break
    return True


not_in_circular_primes = ("0", "2", "4", "5", "6", "8")
count = 4 # account for single digit 2, 3, 5, 7
number = 8
while number < 1000000:
    could_be_circular = True
    for digit in str(number):
        if digit in not_in_circular_primes:
            could_be_circular = False
            # print number, "contains", digit, "ie not circular prime"
    if could_be_circular:
        if is_circular(number):
            count += 1
            print number, "is", count, "circular prime"
    number += 1
print
print count, "circular primes below 1,000,000"

### Prints 55 circular primes below 1,000,000
### Takes about 90 seconds or so to run
### 6 digit circula primes consist of:
### 193939 is 44 circular prime
### 199933 is 45 circular prime
### 319993 is 46 circular prime
### 331999 is 47 circular prime
### 391939 is 48 circular prime
### 393919 is 49 circular prime
### 919393 is 50 circular prime
### 933199 is 51 circular prime
### 939193 is 52 circular prime
### 939391 is 53 circular prime
### 993319 is 54 circular prime
### 999331 is 55 circular prime
### 55 circular primes below 1,000,000