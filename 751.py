from math import floor
from decimal import Decimal

def b(n):
    prev = n
    while True:
        yield prev
        prev = floor(prev) * (prev % 1 + 1)

def a(n):
    B = b(n)
    while True:
        yield floor(next(B))

def tau(n, precision):
    A = a(n)
    leading = str(next(A))
    decimal = ""
    while len(decimal) < precision + 1:
        decimal += str(next(A))
    return round(Decimal(leading + "." + decimal), precision)

# Binary search!
lower = 2
upper = 3
guess = Decimal((lower + upper) / 2)
while guess != (result := tau(guess, 24)):
    if result < guess:
        upper = guess
    else:
        lower = guess
    guess = Decimal((lower + upper) / 2)
print(result)