import sympy

def factorize(n):
    factors = []
    if sympy.isprime(n):
        return [n]
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            factors.append(int(i))
            factors.append(int(n / i))
            break
    for num in factors:
        factors += factorize(num)
        factors = list(set(factors))
    return sorted(factors)

def GPF(n):
    options = factorize(n)
    for num in options[::-1]:
        if sympy.isprime(num):
            return num

print(GPF(600851475143))