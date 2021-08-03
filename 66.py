# This algorithm for solving Pell equations (equations of the form x2 – Dy2 = 1)
# relies on square root continued fractions and rational approximations thereof
# https://en.wikipedia.org/wiki/Pell%27s_equation#Fundamental_solution_via_continued_fractions

from fractions import Fraction as F
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

def genContFrac(n):
    approximation = floor(sqrt(n))
    yield approximation
    newBlock, newIntNum, newIntDenom = simpRootFrac(1, n, -approximation)
    while True:
        yield newBlock
        newBlock, newIntNum, newIntDenom = simpRootFrac(newIntDenom, n, newIntNum)

def genFracApprox(n):
    oldString = ""
    string = "next"
    for num in genContFrac(n):
        oldString = string
        string = string.replace("next", f"{num} + F(1, next)")
        yield eval(oldString.replace("next", str(num)))

def testSolution(x, D, y):
    return (x * x - D * y * y) == 1

if __name__ == "__main__":
    limit = 1000
    square = {x * x for x in range(ceil(sqrt(limit)))}
    nonsquare = [x for x in range(limit + 1) if x not in square]
    winningX = 0
    winningD = 0
    for num in nonsquare:
        for approx in genFracApprox(num):
            x, y = approx.as_integer_ratio()
            if testSolution(x, num, y):
                if x > winningX:
                    winningX = x
                    winningD = num
                break
    print(winningD)
