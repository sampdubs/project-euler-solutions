from sympy import isprime, primerange
from itertools import permutations

def numDigits(n):
    digits = 0
    if n < 0: digits = 1
    while n:
        n //= 10
        digits += 1
    return digits

def addZeros(n, zeros):
    for _ in range(zeros):
        n *= 10
    return n

def concat(p1, p2):
    # A fairly fast way to concatenate two numbers.
    # Needed to speed things up such as
        # Using log10 to find number of digits is slow
        # Built in exponents of 10 to add zeros is slow
    return addZeros(p1, numDigits(p2)) + p2

def checkSet(primes):
    # Look at every combination in both orders to ensure every concatenation is prime
    return all(isprime(concat(*perm)) for perm in permutations(primes, 2))

def findSet(n, top, prev=[]):
    # Recursive backtracking method of finding sequence.
    # Because any subsequence also follows the rules, we can use recursive backtracking
    if prev: pr = primerange(prev[-1] + 2, top)
    else: pr = primerange(3, top)
    for p in pr:
        trynext = [*prev, p]
        if checkSet(trynext):
            if len(trynext) == n:
                return trynext
            if (success := findSet(n, top, trynext)):
                return success
    return False

# takes around 1 minute. Somewhat arbitrary 10,000 upper bound found through experimentation
print(sum(findSet(5, 10000)))