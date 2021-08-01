def powFast(base, power):
    result = 1
    for _ in range(power):
        result *= base
    return result

# arbitrarily choose 100 as the upper bound
total = 0
for power in range(1, 100):
    lower = powFast(10, power - 1)
    upper = lower * 10
    lower -= 1

    for base in range(1, 10):
        if lower < powFast(base, power) < upper:
            total += 1

print(total)