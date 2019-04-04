from itertools import permutations

check = '0123456789'
otn_pans = list(permutations(check))
for k in range(len(otn_pans)):
    otn_pans[k] = ''.join(otn_pans[k])

def is_special(n):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        sub = n[i:i + 3]
        if not (int(sub) % primes[i - 1] == 0):
            return False
    return True

specials = []
for pan in otn_pans:
    if is_special(pan):
        specials.append(int(pan))

print(sum(specials))