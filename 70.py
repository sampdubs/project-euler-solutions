from functools import cache
from math import ceil, sqrt
from sympy import totient, sieve
from tqdm import trange
from tqdm.std import tqdm


def is_perm(a, b):
    return sorted(str(a)) == sorted(str(b))

# This is Jonas's TRASH solution (actually probably just a little slower and way simpler)
# print(argmin([n/phin for n in trange(1, 10_000_000) if is_perm(n, (phin := totient(n)))]) + 1)

top = 10 ** 7
PRIMES = list(sieve.primerange(0, ceil(sqrt(top))))


@cache
def factorsOf(n):
    factors = []
    halfN = ceil(sqrt(n))
    if n in PRIMES:
        return [n]
    for p in PRIMES:
        if p > halfN:
            break
        div, mod = divmod(n, p)
        if mod == 0:
            factors.append(p)
            prevDiv = div
            div, mod = divmod(div, p)
            while mod == 0:
                prevDiv = div
                div, mod = divmod(div, p)
            factors += factorsOf(prevDiv)
    return set(factors)


def nOnPhiN(n):
    # p = factorint(n).keys()
    p = factorsOf(n)
    total = 1
    for fact in p:
        total *= (fact - 1) / fact
    return 1 / total


possible = sorted([(nOnPhiN(n), n) for n in trange(2, top)], key=lambda a: (a[0], top - a[1]))
for pair in tqdm(possible):
    ratio, n = pair
    if is_perm(n, totient(n)):
        print(n)
        break
