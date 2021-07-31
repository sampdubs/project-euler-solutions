from itertools import permutations

TRI = [x for n in range(200) if 999 < (x := n * (n + 1) // 2) < 10000]
SQR = [x for n in range(200) if 999 < (x := n * n) < 10000]
PNT = [x for n in range(200) if 999 < (x := n * (3 * n - 1) // 2) < 10000]
HEX = [x for n in range(200) if 999 < (x := n * (2 * n - 1)) < 10000]
HPT = [x for n in range(200) if 999 < (x := n * (5 * n - 3) // 2) < 10000]
OCT = [x for n in range(200) if 999 < (x := n * (3 * n - 2)) < 10000]

POLY = [TRI, SQR, PNT, HEX, HPT, OCT]

## change name
def findSet(nums, polysToAdd):
    if len(polysToAdd) == 0:
        if nums[0] // 100 == nums[-1] % 100:
            return nums
        return False
    possibles = [n for n in polysToAdd[0] if n // 100 == nums[-1] % 100]
    for possible in possibles:
        if (answer := findSet(nums + [possible], polysToAdd[1:])):
            return answer
    return False

for order in permutations(POLY):
    for start in order[0]:
        nums = [start]
        if (answer := findSet(nums, order[1:])):
            print(sum(answer))
            exit()