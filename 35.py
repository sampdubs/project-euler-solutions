from sympy import isprime

def is_cprime(n):
    rots = set()
    n = str(n)
    for i in range(len(n)):
        rots.add(int(n))
        n = n[-1] + n[:-1]
    for i in rots:
        if not isprime(i):
            return False
    return True

c_primes = [2, 3, 5, 7]
for n in range(11, 1000000, 2):
    if is_cprime(n):
        c_primes.append(n)

print(len(c_primes))