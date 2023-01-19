# 25 1000-digit Fibonacci number

# Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# F1 = 1, F2 = 1, F3 = 2, F4 = 3, F5 = 5, F6 = 8, F7 = 13, F8 = 21, 
# F9 = 34, F10 = 55, F11 = 89, F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# What is the first term in the Fibonacci sequence to contain 1000 
# digits?

n = 3
fn_minus_2 = 1
fn_minus_1 = 1
digits = 1000

while True:
    fn = fn_minus_1 + fn_minus_2
    if len(str(fn)) == digits:
        break
    else:
        fn_minus_2 = fn_minus_1
        fn_minus_1 = fn
        n += 1

print "n =", n
print "digits =", digits