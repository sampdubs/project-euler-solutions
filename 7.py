import sympy

prime_count = 1
counter = 1
while True:
    counter += 2
    if sympy.isprime(counter):
        prime_count += 1
    if prime_count == 10001:
        break

print(counter)
    