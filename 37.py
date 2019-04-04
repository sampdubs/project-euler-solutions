from sympy import isprime, nextprime

def is_right_t(n):
    while n > 9:
        n = (n - (n % 10)) // 10
        if not isprime(n):
            return False
    return True

def is_left_t(n):
    n = str(n)
    while len(n) > 1:
        n = n[1:]
        if not isprime(int(n)):
            return False
    return True

n = 10
duo_truncs = []

while len(duo_truncs) < 11:
    n = nextprime(n)
    if is_right_t(n) and is_left_t(n):
        duo_truncs.append(n)

print(sum(duo_truncs))