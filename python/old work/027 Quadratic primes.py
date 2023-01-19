# 27 Quadratic primes

def instructions():
    # Euler discovered the remarkable quadratic formula:
    
    # n^2 + n + 41
    
    # It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
    # However, when n=40, 40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.
    
    # The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79.
    # The product of the coefficients, -79 and 1601, is -126479.
    
    # Considering quadratics of the form:
    
    # n^2 + an + b, where |a|<1000 and |b|<=1000
    
    # Find the product of the coefficients, a and b, for the quadratic expression 
    # that produces the maximum number of primes for consecutive values of n, starting with n=0.
    pass
pass

def quadratic_expression(a, b, n):
    value = n*n + a*n + b
    return value
pass

def is_prime(number):
    if number <= 1:
        return False
    possible_multiple = 2
    possible_multiple_max = number / 2
    while (possible_multiple <= possible_multiple_max and is_prime(possible_multiple)):
        if number / possible_multiple * possible_multiple == number:
            return False
        else:
            possible_multiple += 1
    return True
pass

max_a = -1000
max_b = -1000
max_num_primes = 0
#for a in range(-61, -60):
#    for b in range(971, 972):
for a in range(-1000, 1001):
#   # consider n = 0 , expresion simplifies to "b"
    for b in range(2, 1001):
        if not(is_prime(b)):
            continue
        n = 1
        while True:
#    	# consider n = 1 , expresion simplifies to "1 + a + b"
            if (1 + a + b < 2):
                break
            print "a=", a , "," , "b=" , b , "," , "max_a=", max_a , "," , "max_b=" , max_b , "n=" , n , "," , "max_num_primes=" , max_num_primes , quadratic_expression(a, b, n)
            if not(is_prime(quadratic_expression(a, b, n))):
                break
            else:
                n += 1
                if n > max_num_primes:
                    max_num_primes = n
                    max_a = a
                    max_b = b

print max_a * max_b

# max_a= -61 , max_b= 971
# -59231