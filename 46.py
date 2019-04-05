from sympy import isprime

def follows_conj(n):
    i = 0
    while True:
        i += 1
        sq = 2 * i * i
        if sq > n:
            return False
        diff = n - sq
        if isprime(diff):
            return True

i = 1
while True:
    i += 2
    if not isprime(i):
        if not follows_conj(i):
            print(i)
            break