from itertools import permutations
from sympy import isprime

def get_all_pans():
    pans = []
    for i in range(1, 10):
        check = ''
        for j in range(1, i + 1):
            check += str(j)
        perms = list(permutations(check))
        for k in range(len(perms)):
            perms[k] = int(''.join(perms[k]))
        pans += perms
    return pans

pans = get_all_pans()

for p in pans[::-1]:
    if isprime(p):
        print(p)
        break