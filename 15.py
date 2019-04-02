from collections import Counter
from math import factorial
from functools import reduce
import operator    

def unique_permutations(lst):
    c = Counter(lst)
    return factorial(len(lst)) // reduce(operator.mul, map(factorial, c.values()))

print(unique_permutations(["r"] * 20 + ["d"] * 20))