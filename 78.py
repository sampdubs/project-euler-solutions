from functools import cache

def sign():
    while True:
        yield 1
        yield 1
        yield -1
        yield -1

def gen_pent():
    n = 1
    while True:
        yield n * (3 * n - 1) // 2
        yield -n * (3 * -n - 1) // 2
        n += 1

@cache
def num_partitions(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return 1

    total = 0
    sign_gen = sign()
    for pent in gen_pent():
        if pent > n: break
        total += next(sign_gen) * num_partitions(n - pent)
    return total

n = 2
while num_partitions(n) % 1_000_000 != 0:
    n += 1
print(n)