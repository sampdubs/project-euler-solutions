def is_pal(n):
    strn = str(n)
    return strn == strn[::-1]

def is_lychrel(n):
    for _ in range(50):
        n += int(str(n)[::-1])
        if is_pal(n):
            return False
    return True

lychrels = []
for n in range(1, 10000):
    if is_lychrel(n):
        lychrels.append(n)

print(len(lychrels))