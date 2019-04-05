from sympy import isprime

primes = {}
for i in range(1000, 10000):
    primes[i] = isprime(i)

def is_unusual(a, b, c):
    if not(primes[a] and primes[b] and primes[c]):
        return False
    if "".join(sorted(str(a))) == "".join(sorted(str(b))) and "".join(sorted(str(a))) == "".join(sorted(str(c))):
        return True
    return False

unusuals = []

for i in range(1000, 9996):
    for d in range(2, (9999 - i) // 2 + 1, 2):
        if is_unusual(i, i + d, i + d + d):
            unusuals.append(f"{i}{i + d}{i + d + d}")

print(unusuals[1])