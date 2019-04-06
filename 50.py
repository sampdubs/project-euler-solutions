from sympy import isprime, sieve

below = 1000000
primes = list(sieve.primerange(0, below))
sum_primes = [0]
primes_hash = {n: True for n in primes}
sums = set()
for i in range(len(primes)):
    sum_primes.append(sum_primes[i] + primes[i])

for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        sm = sum_primes[j] - sum_primes[i]
        if sm < below:
            sums.add((j - i, sm))

prime_sums = []
for n in sums:
    if n[1] in primes_hash:
        prime_sums.append(n)

print(max(prime_sums))