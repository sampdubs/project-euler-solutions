from fractions import Fraction
from math import gcd
from tqdm import trange
from sympy import primefactors
from sympy import totient

def brute_force_count(x):
    all_fracs = set()
    for d in range(2, x + 1):
        for n in range(1, d):
            all_fracs.add(Fraction(n, d))
    return len(all_fracs)

def cum_gcd_count(x):
    primefacts = { n: set(primefactors(n)) for n in trange(1, x + 1) }
    total = 0
    for i in trange(2, x + 1):
        for j in range(1, i):
            # total += gcd(i, j) == 1
            total += len(primefacts[i].intersection(primefacts[j])) == 0
    return total

def cum_phi_count(x):
    total = 0
    for i in trange(2, x + 1):
        total += totient(i)
    return total

assert brute_force_count(8) == 21
assert cum_gcd_count(8) == 21
assert cum_phi_count(8) == 21
# print(brute_force_count(1_000_000))
# for i in range(1, 100):
#     print(str(i).zfill(2), str(brute_force_count(i)).zfill(3), brute_force_count(i) - brute_force_count(i - 1))

# print(cum_gcd_count(1_000_000))
print(cum_phi_count(1_000_000))
# 303963552391

# How I solved this problem:
# First, I wrote a naive method to find the answers for small numbers using brute force and builtin fractions
# Then, I tried to find a pattern in how the number of fractions was changing for each increase
# I realized it was increasing by the number of coprimes less than the number was added
# So I wrote cum_gcd_count, which adds the number of coprimes of each number to a total
# Then I realized, the number of comprimes of n less than n is just Euler's totient function
# So I wrote cum_phi_count, which simply sums up the values of the totient function up the n
# It's likely not the most efficient, but it runs under a minute on my computer!