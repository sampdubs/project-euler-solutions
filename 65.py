from fractions import Fraction as F

def genESeq(n):
    yield 2
    for i in range(n - 1):
        if i % 3 == 1:
            yield 2 * ((i + 2) // 3)
        else:
            yield 1

def makeFracString(n):
    oldString = ""
    string = "next"
    for num in genESeq(n):
        oldString = string
        string = string.replace("next", f"{num} + F(1, next)")
    return oldString.replace("next", str(num))
    
# Instead of writing code to actually simplify the long fraction down, 
# this solution opts to use the already existing frations module.
# I make a string of the continued fraction approximation, then call eval
# and let the module do the computation, while the code simply pulls out the numerator
# and adds together the digits to get the solution

n = 100
print(sum(int(x) for x in str(eval(makeFracString(n)).as_integer_ratio()[0])))