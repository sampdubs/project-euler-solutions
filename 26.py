from decimal import getcontext, Decimal

def find_repeating(s, max_len):
    for i in range(len(s)):
        for l in range(1, max_len + 1):
            r_test = s[i:i + l]
            if r_test * 3 in s:
                return r_test
    return -1

def getRepeatingLen(d):
    frac = str(Decimal(1) / Decimal(d))
    if len(frac) < 1000:
        return 0
    return len(find_repeating(frac, d - 1))

winner = 0
winning_val = 0
getcontext().prec = 5000
for d in range(2, 1000):
    l = getRepeatingLen(d)
    if l > winning_val:
        winner = d
        winning_val = l

print(winner)