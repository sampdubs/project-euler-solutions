from math import ceil, floor, sqrt

def simpRootFrac(num, root, intd):
    # takes in a numerator, and the two parts of the irrational root
    # simplify by mutliplying by the conjugate
    # returns whole number, plus 3 parts of remaining fraction.
    
    newIntNum = -intd
    newDenom = root - intd * intd
    newDenom //= num

    approximation = floor((newIntNum + sqrt(root)) / newDenom)
    newIntNum -= approximation * newDenom

    return (approximation, newIntNum, newDenom)

def hasOddPeriod(n):
    approximation = floor(sqrt(n))
    newBlock, newIntNum, newIntDenom = simpRootFrac(1, n, -approximation)
    seen = {(newBlock, newIntNum, newIntDenom),}
    period = 0
    while True:
        period += 1
        seen.add((newBlock, newIntNum, newIntDenom))
        newBlock, newIntNum, newIntDenom = simpRootFrac(newIntDenom, n, newIntNum)
        if (newBlock, newIntNum, newIntDenom) in seen:
            break
    return period % 2 == 1

if __name__ == "__main__":
    highest = 10_000
    squares = {n * n for n in range(ceil(sqrt(highest)) + 1)}
    # squares are all the things to avoid because they don't give continued fractions
    total = 0
    for n in range(2, highest + 1):
        if n not in squares:
            total += hasOddPeriod(n)
    print(total)