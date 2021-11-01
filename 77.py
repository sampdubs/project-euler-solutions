from functools import cache
from sympy import primerange

@cache
def count_decreasing_prime_sums(n, max=None):
    if n == 1:
        return 0
    if n == 2:
        return 1

    max = max or n
    total = 0
    for first_addend in primerange(2, min(max + 1, n)):
        total += count_decreasing_prime_sums(n - first_addend, first_addend)
    if n <= max > 1:
        return total + 1
        # adds one to account for the option of not breaking up further into sums
    return total

n = 2
while count_decreasing_prime_sums(n) <= 5001:
    n += 1
print(n)