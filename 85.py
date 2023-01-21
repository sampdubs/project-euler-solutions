def slow(W, H):
    total = 0
    for w in range(1, W+1):
        for h in range(1, H+1):
            total += (W-w+1)*(H-h+1)
    return total

# I derived this formula manually, but before I could even write the code for it, GitHub Copilot wrote it for me.
def fast(W, H):
    return W*H*(W+1)*(H+1)/4

# Fast (W, H) = 2,000,000 when
# W = ((H*(H*H*H+2*H*H+8000001*H+8000000)) ** 0.5 - H*(H+1))/(H*(H+1))
# Used a CAS for this, probably a more elegant way to find these approximate pairs

def closestWs(H):
    w = int(((H*(H*H*H+2*H*H+8000001*H+8000000)) ** 0.5 - H*(H+1))/(H*(H+1)))
    return w, w+1

# When H = 1, W between 1999 and 2000 (closestWs(1) = (1999, 2000))
# Meaning the max value of H or W we need to test is 2000

winningArea = 0
winningDist = 2000000

for H in range(1, 2000):
    for W in closestWs(H):
        if abs(fast(W, H) - 2000000) < winningDist:
            winningArea = W*H
            winningDist = abs(fast(W, H) - 2000000)
            print("Winner:", W, H)

print(winningArea)