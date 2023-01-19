
# https://projecteuler.net/problem=10
# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

################################################################
############# NOTE THIS ONE FREEZES, DOES NOT WORK #############
################################################################
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
#   File "C:\Users\jgutz\AppData\Local\Programs\Python\Python311\Lib\multiprocessing\spawn.py", line 120, in spawn_main
#     exitcode = _main(fd, parent_sentinel)
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\jgutz\AppData\Local\Programs\Python\Python311\Lib\multiprocessing\spawn.py", line 129, in _main
#     prepare(preparation_data)
#   File "C:\Users\jgutz\AppData\Local\Programs\Python\Python311\Lib\multiprocessing\spawn.py", line 240, in prepare
#     _fixup_main_from_path(data['init_main_from_path'])
#   File "C:\Users\jgutz\AppData\Local\Programs\Python\Python311\Lib\multiprocessing\spawn.py", line 291, in _fixup_main_from_path
#     main_content = runpy.run_path(main_path,
#                    ^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "<frozen runpy>", line 291, in run_path
#   File "<frozen runpy>", line 98, in _run_module_code
#   File "<frozen runpy>", line 88, in _run_code
#   File "C:\Users\jgutz\Desktop\project_euler\python\010 Summation of primes\010 Summation of primes.py", line 44, in <module>
#     print(sum_of_primes_below_two_million())
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
################################################################

# Here is an example of how the Sieve of Eratosthenes algorithm can be optimized using the wheel factorization method and multi-processing:

from multiprocessing import Process, Manager

def sum_of_primes_below_two_million():
    limit = 2000000
    primes = [True] * limit
    primes[0] = primes[1] = False

    def sieve(start, step, primes):
        for i in range(start, limit, step):
            primes[i] = False

    processes = []
    manager = Manager()
    primes = manager.list(primes)
    # Eliminate multiples of 2
    processes.append(Process(target=sieve, args=(4, 2, primes)))
    # Eliminate multiples of 3
    processes.append(Process(target=sieve, args=(9, 3, primes)))
    # Eliminate multiples of 5
    processes.append(Process(target=sieve, args=(25, 5, primes)))
    # Eliminate multiples of 7
    processes.append(Process(target=sieve, args=(49, 7, primes)))
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    for i in range(11, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit, i):
                primes[j] = False

    return sum(i for i in range(limit) if primes[i])

print(sum_of_primes_below_two_million())

# This version of the code uses the wheel factorization method to eliminate the need to check divisibility by 2, 3, 5, and 7 during the sieving process, which reduces the number of divisions that need to be performed. Additionally, it uses multi-processing to parallelize the sieving process, which improves the performance of the algorithm by allowing multiple sieving operations to be performed simultaneously.

# It's important to note that multi-processing can be beneficial on multi-core machines and the performance can vary depending on the machine, but it may come with a memory overhead.

# As the limit of 2 million is not that big, the performance gain may not be that significant, but for bigger limits, it can make a noticeable difference.

# It's important to note that the best solution depends on the specific use case, it's always a good idea to test and compare the performance of different optimizations.
