def curious(n, d):
    common = ''
    if n[0] in d:
        common = n[0]
    elif n[1] in d:
        common = n[1]
    else:
        return False
    if common == '0' or n == d:
        return False
    n1 = n.replace(common, '', 1)
    d1 = d.replace(common, '', 1)
    if d1 == '0':
        return False
    if int(n) / int(d) == int(n1) / int(d1):
        return True
    return False

curiouses = []
for n in range(10, 100):
    for d in range(n + 1, 100):
        if curious(str(n), str(d)):
            curiouses.append((n, d))

product = 1
for c in curiouses:
    product *= c[0] / c[1]
print(round(product, 5))