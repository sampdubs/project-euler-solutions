from math import factorial
def choose(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

total = 0
for n in range(23, 101):
    for r in range(2, n - 2):
        if choose(n, r) > 1000000:
            total += 1

print(total)