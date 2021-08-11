three_sevenths = 3 / 7
closest = 0
closestFrac = (0, 2)

for d in range(1, 1_000_001):
    if d % 7 == 0: continue
    n = d * 3 // 7
    x = n / d
    if (three_sevenths) - x < (three_sevenths) - closest:
        # ensure this fraction isn't equivalent to the current winner
        # ensures the aswer is fully reduced
        if d % closestFrac[1] != 0 and n % closestFrac[1] != 0:
            closest = x
            closestFrac = (n, d)

print(closestFrac[0])