from itertools import permutations

perms = list(permutations(range(10)))

print(''.join(map(str, perms[999999])))