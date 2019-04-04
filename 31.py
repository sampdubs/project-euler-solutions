total_ways = 8

def is_good(ones, twos, fives, tens, twenties, fifties, hundreds):
    return (ones + 2 * twos + 5 * fives + 10 * tens + 20 * twenties + 50 * fifties + 100 * hundreds) == 200

total = 8
for a in range(200):
    for b in range(100):
        for c in range(40):
            for d in range(20):
                for e in range(10):
                    for f in range(4):
                        for g in range(2):
                            if is_good(a, b, c, d, e, f, g):
                                total += 1
print(total)