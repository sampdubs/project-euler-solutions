def is_duo_pal(n):
    binary = "{0:b}".format(n)
    n = str(n)
    return n == n[::-1] and binary == binary[::-1]

pals = []
for n in range(1000000):
    if is_duo_pal(n):
        pals.append(n)
print(sum(pals))