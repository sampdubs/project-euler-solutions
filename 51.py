from sympy import isprime, sieve

goal = 8

def how_many_primes(n):
    total = 0
    smallest = -1
    if n[0] == '*':
        start = 1
    else:
        start = 0
    for i in range(start, 10):
        p = int(n.replace('*', str(i)))
        if (isprime(p)):
            total += 1
            if smallest == -1:
                smallest = i
    return (total, str(smallest))


primes = list(sieve.primerange(0, 50000))

for i in range(len(primes)):
    n = str(primes[i])
    for r in set(n):
        rn = n.replace(r, '*')
        total, smallest = how_many_primes(rn)
        if total == goal:
            print(rn.replace('*', smallest))
            exit()
        total, smallest = how_many_primes('*' + rn)
        if total == goal:
            print(('*' + rn).replace('*', smallest))
            exit()