import math
def primes_below(n):
    a = [False, False] + [True for _ in range(n - 1)]
    for i in range(2, math.floor(math.sqrt(n) + 1)):
        if a[i]:
            k = 0
            j = (i + k) * i
            while j <= n:
                a[j] = False
                k += 1
                j = (i + k) * i
    outlist = []
    for i in range(n + 1):
        if a[i]:
            outlist.append(i)
    return outlist

print(sum(primes_below(2000000)))