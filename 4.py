def is_pal(n):
    return str(n) == str(n)[::-1]

winner = -1
for i in range(1, 1000):
    for j in range(1, i + 1):
        if is_pal(i * j):
            if i * j > winner:
                winner = i * j

print(winner)