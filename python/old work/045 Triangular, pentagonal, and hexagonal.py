# 45 Triangular, pentagonal, and hexagonal
def instructions():
    # Triangle, pentagonal, and hexagonal numbers are generated by the 
    # following formulae:

    # Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
    # Pentagonal	Pn=n(3n-1)/2	1, 5, 12, 22, 35, ...
    # Hexagonal	 	Hn=n(2n-1)	 	1, 6, 15, 28, 45, ...
    # It can be verified that T285 = P165 = H143 = 40755.

    # Find the next triangle number that is also pentagonal and 
    # hexagonal.
    pass
pass

t_index = 285
max_triangular = 40755

p_index = 165
max_pentagonal = 40755

h_index = 143
max_hexagonal = 40755

def is_pentagonal(n):
    global p_index, max_pentagonal
    while n > max_pentagonal:
        p_index += 1
        max_pentagonal = p_index * (3 * p_index - 1) / 2
    if n == max_pentagonal:
        return True
    else:
        return False
pass

def is_hexagonal(n):
    global h_index, max_hexagonal
    while n > max_hexagonal:
        h_index += 1
        max_hexagonal = h_index * (2 * h_index - 1)
    if n == max_hexagonal:
        return True
    else:
        return False
pass

while True:
    t_index += 1
    triangular = t_index * (t_index + 1) / 2
    if is_pentagonal(triangular) and is_hexagonal(triangular):
        print "triangular index =", t_index
        print "pentagonal index =", p_index
        print "hexagonal index =", h_index
        print "triangular =", triangular
        break
pass