# 94 Almost equilateral triangles

# import math
# import gmpy # http://www.gmpy.org/home
def instructions():
    # It is easily proved that no equilateral triangle exists with 
    # integral length sides and integral area. However, the almost 
    # equilateral triangle 5-5-6 has an area of 12 square units.

    # We shall define an almost equilateral triangle to be a triangle 
    # for which two sides are equal and the third differs by no more 
    # than one unit.

    # Find the sum of the perimeters of all almost equilateral triangles
    # with integral side lengths and area and whose perimeters do not 
    # exceed one billion (1,000,000,000).
    pass

def isqrt(x):
    # http://code.activestate.com/recipes/577821-integer-square-root-function/
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def is_perfect_square(x): # returns True or False
    temp = isqrt(x)
    if temp * temp == x:
        return True
    else:
        return False

def perimeter(triangle): # triangle is a list of 3 side lengths
    return sum(triangle)

def perimeter_up(side): # side is the known length of two sides
    return (3 * side + 1)

def perimeter_down(side): # side is the known length of two sides
    return (3 * side - 1)

def area_is_integer(triangle): # returns True or False
    # if c = (a - 1)
    # A^2 = (1 / 16) * (a - 1)^2 * (a + 1) * (3 * a - 1)
    # A = (1 / 4) * (a - 1) * sqrt[ (a + 1) * (3 * a - 1)]

    
    # if c = (a + 1)
    # A^2 = (1 / 16) * (a + 1)^2 * (a - 1) * (3 * a + 1)
    # A = (1 / 4) * (a + 1) * sqrt[ (a - 1) * (3 * a + 1)]
    
    if False: # legacy code
        # A^2 = (P * (P - 2a) * (P - 2b) * (P - 2c)) / 16
        # P = perimeter(triangle)
        # a, b, c = triangle[0], triangle[1], triangle[2]
        # area_squared_times_16 = (P * (P - 2 * a) * (P - 2 * b) * (P - 2 * c))
        # if not area_squared_times_16 / 16 * 16 == area_squared_times_16:
            # # print "area_squared_times_16 =", area_squared_times_16
            # # print "area =", (area_squared_times_16 / 16.) ** 0.5
            # return False
        # area_squared = area_squared_times_16 / 16
        # area = math.sqrt(area_squared)
        # if area_squared - area ** 2 == 0:
            # return True
        # return False
        pass
    if False: # legacy code
        # n = 1
        # while n ** 2 < area_squared:
            # n += 1
        # if n ** 2 == area_squared:
            # # print "n^2 = area squared =", area_squared
            # return True
        # print "n^2 =", n ** 2, " > area squared =", area_squared
        # return False
        pass

def area_up_is_integer(side): # returns True or False c = (a + 1)
    # if c = (a + 1)
    # A^2 = (1 / 16) * (a + 1)^2 * (a - 1) * (3 * a + 1)
    # A = (1 / 4) * (a + 1) * sqrt[ (a - 1) * (3 * a + 1)]
    a = side
    radicand = (a - 1) * (3 * a + 1)
    if not is_perfect_square(radicand):
        return False
    area_times_4 = (a + 1) * isqrt(radicand)
    if not area_times_4 / 4 * 4 == area_times_4:
        return False
    return True

def area_down_is_integer(side): # returns True or Falsec = (a - 1)
    # if c = (a - 1)
    # A^2 = (1 / 16) * (a - 1)^2 * (a + 1) * (3 * a - 1)
    # A = (1 / 4) * (a - 1) * sqrt[ (a + 1) * (3 * a - 1)]
    a = side
    radicand = (a + 1) * (3 * a - 1)
    if not is_perfect_square(radicand):
        return False
    area_times_4 = (a - 1) * isqrt(radicand)
    if not area_times_4 / 4 * 4 == area_times_4:
        return False
    return True

def test_prints():
    print area_is_integer([5,5,5])
    print area_is_integer([5,5,6])
    print area_is_integer([1,1,0])
    print area_is_integer([1,1,2])
# test_prints()

side = 2
total = 0
area_up_integers = []
area_down_integers = []

while side <= 333333333:
    print side, total
    if area_up_is_integer(side):
        area_up_integers.append(side)
        total += perimeter_up(side)
        print side, "area_up_is_integer  ", "total =", total
    
    if area_down_is_integer(side):
        area_down_integers.append(side)
        total += perimeter_down(side)
        print side, "area_down_is_integer", "total =", total
    side += 1
pass

print "area_up_integers=", area_up_integers
print "area_down_integers=", area_down_integers
print "sum of the perimeters =", total

def correct_output():
    # Timed it. Ran for just less than 27.5 hours.
    # 333333330 518408346
    # 333333331 518408346
    # 333333332 518408346
    # 333333333 518408346
    # area_up_integers= [5, 65, 901, 12545, 174725, 2433601, 33895685]
    # area_down_integers= [17, 241, 3361, 46817, 652081, 9082321, 126500417]
    # sum of the perimeters = 518408346
    pass
pass
