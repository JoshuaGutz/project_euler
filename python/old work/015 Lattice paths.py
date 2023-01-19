# 15 Lattice paths

# Starting in the top left corner of a 2x2 grid, and only being able to 
# move to the right and down, there are exactly 6 routes to the bottom 
# right corner.

# How many such routes are there through a 20x20 grid?

# through trial and error i got 20 for the 3x3 (15 at the stair step)
# nxn grid has x paths
# 1x1 grid has 2 paths   0*2 through center + 2 outside
# 2x2 grid has 6 paths   2*2 through center + 2 outside
# 3x3 grid has 20 paths  9*2 through center + 2 outside
# 20x20 grid has x paths y*2 through center + 2 outside

#  if 1   1       is row 1 of pascals triangle  has 2 elements
#    1 *2* 1      is row 2 (1x1)                has 3 elements
#   1  3 3  1     is row 3                      has 4 elements
#  1 4 *6* 4 1    is row 4 (2x2)                has 5 elements
# 1 5 10 10 5 1   is row 5                      has 6 elements
#1 6 15*20*15 6 1 is row 6 (3x3)                has 7 elements

# looking for middle term of row 40 (20x20)     has 41 elements
# middle term will be 21st nonzero term

#0 1 1
#0 1 2  1
#0 1 3  3  1
#0 1 4  6  4  1
#0 1 5 10 10  5 1
#0 1 6 15 20 15 6 1
#   i-1 i               row n-1
#       i               row n

def pascal2_row_n(n):
    if n == 1:
        return [1, 1]
    else:
        answer = [1]
        prev_row = pascal2_row_n(n - 1)
        i = 1
        while i < n:
            answer += [prev_row[i - 1] + prev_row[i]]
            i += 1
        answer += [1]
        return answer

print max(pascal2_row_n(40))

########################################################################
###############################EXTRA BITS###############################
########################################################################
def i_term_n_row(i, n):
    if i == 0:
        return 0
    else:
        if n == 1:
            return 1
        elif n > 1:
            if i == n + 1:
                return 1
            else:
                return i_term_n_row(i - 1, n - 1) + i_term_n_row(i, n - 1)

def pascal_row_n(n):
    print "row", n, "=",
    for i in range(n+1):
        print i_term_n_row(i, n),
    print i_term_n_row(n + 1, n)
    
# print max(pascal2_row_n(1))
# print max(pascal2_row_n(2))
# print max(pascal2_row_n(3))
# print max(pascal2_row_n(4))
# print max(pascal2_row_n(5))
# print max(pascal2_row_n(6))
# print max(pascal2_row_n(7))
# print max(pascal2_row_n(8))
# print max(pascal2_row_n(10))
# print max(pascal2_row_n(15))
# print max(pascal2_row_n(20))
# print max(pascal2_row_n(25))
# print max(pascal2_row_n(30))
# print i_term_n_row(0, 6),
# print i_term_n_row(1, 6),
# print i_term_n_row(2, 6),
# print i_term_n_row(3, 6),
# print i_term_n_row(4, 6),
# print i_term_n_row(5, 6),
# print i_term_n_row(6, 6),
# print i_term_n_row(7, 6)
# pascal_row_n(1)
# pascal_row_n(2)
# pascal_row_n(3)
# pascal_row_n(4)
# pascal_row_n(5)
# pascal_row_n(6)
# pascal_row_n(7)
# pascal_row_n(8)
# pascal_row_n(40)
# print i_term_n_row(10, 20),
# print i_term_n_row(11, 20),
# print i_term_n_row(12, 20)
# print i_term_n_row(15, 30),
# print i_term_n_row(16, 30),
# print i_term_n_row(17, 30)
# print i_term_n_row(20, 40),
# print i_term_n_row(21, 40),
# print i_term_n_row(22, 40)
