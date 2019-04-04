def is_pandigital(n):
    return ''.join(sorted(n)) == '123456789'

def makes_c_pan(n):
    concatenated = ""
    counter = 1
    while len(concatenated) < 9:
        concatenated += str(n * counter)
        counter += 1
    if len(concatenated) < 9:
        return False
    if is_pandigital(concatenated):
        return concatenated

winner = -1
for n in range(1000000):
    mcp = makes_c_pan(n)
    if mcp:
        if int(mcp) > winner:
            winner = int(mcp)
print(winner)