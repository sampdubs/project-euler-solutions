from math import sqrt

def is_pent(n):
    N = (1 + sqrt(24 * n + 1)) / 6
    return N % 1 == 0

j = 0

while True:
    j += 1
    J = int(j * (3 * j - 1) / 2)
    for k in range(j - 1, 0, -1):
        K = int(k * (3 * k - 1) / 2)
        if is_pent(J + K):
            diff = abs(J - K)
            if is_pent(diff):
                print(diff)
                exit()