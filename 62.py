from collections import defaultdict

def cubes():
    n = 1
    while (n := n + 1):
        yield n * n * n

found = defaultdict(list)
# found dict will have the sorted string of digits corresponding to a list of cubes with those digits

for cube in cubes():
    digits = "".join(sorted(str(cube)))
    found[digits].append(cube)
    if len(found[digits]) == 5:
        print(found[digits][0])
        break