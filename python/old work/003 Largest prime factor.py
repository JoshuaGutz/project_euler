# 3 Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

number = 600851475143


def is_prime(number):
    count = number / 2
    while count > 1:
        if number % count == 0:
            return False
            break
        else:
            count -= 1
    return True
    
def largest_factor(number):
    guess = number / 2
    while guess > 1:
        if number % guess == 0:
            print guess, "*", number / guess, "=", number
            return guess
            break
        else:
            guess -= 1

#largest_factor(number)

def largest_factor_method_2(number):
    i = 2
    while i < number / 2:
        if number / i * i == number:
            print number / i, "*", i, "=", number
            return number / i
            break
        else:
            i += 1
            while not is_prime(i):
                i += 1
            
# largest_factor_method_2(number)
# print largest_factor_method_2(number)
largest_factor_method_2(
largest_factor_method_2(
largest_factor_method_2(
largest_factor_method_2(number))))

print is_prime(71)
print is_prime(839)
print is_prime(6857)
print is_prime(1471)
print "71 * 839 * 6857 * 1471", "=", 71 * 839 * 6857 * 1471


def largest_factor_method_3(number):
    guess = number / 2
    while guess > 1:
        if is_prime(guess):
            if number / guess * guess == number:
                print guess, "*", number / guess, "=", number
                return guess
                break
        else:
            guess -= 1

# largest_factor_method_3(144)










