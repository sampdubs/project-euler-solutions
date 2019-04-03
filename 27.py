from sympy import isprime, primerange

def numPrimes(a, b):
    n = 0
    while isprime((n * n + a * n + b)):
        n += 1
    return n

winner = 0
winning_a = 0
winning_b = 0
p_under_1000 = list(primerange(2, 1000))
for a in range(-1000, 1000):
    for b in p_under_1000:
        if a + b > 1:
            val = numPrimes(a, b)
            if val > winner:
                winner = val
                winning_a = a
                winning_b = b

print(winning_a * winning_b)