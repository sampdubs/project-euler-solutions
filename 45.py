from math import sqrt

def is_pent(n):
    N = (1 + sqrt(24 * n + 1)) / 6
    return N % 1 == 0

def is_tri(n):
    N = (sqrt(8 * n + 1) - 1) / 2
    return N % 1 == 0

h = 144

while True:
    H = h * (2 * h - 1)
    if is_tri(H) and is_pent(H):
        print(H)
        break
    h += 1