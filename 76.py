from functools import cache

@cache
def count_decreasing_sums(n, max=None):
    if n == 1:
        return 1

    max = max or n
    total = 0
    for first_addend in range(1, min(max + 1, n)):
        total += count_decreasing_sums(n - first_addend, first_addend)
    if n <= max > 1:
        return total + 1
        # adds one to account for the option of not breaking up further into sums
    return total

print(count_decreasing_sums(100) - 1)
# subtract one because 100 is being counted as a valid sum