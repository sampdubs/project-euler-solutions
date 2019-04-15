from fractions import Fraction

root2 = Fraction(1, 2)
count = 0

for _ in range(1000):
    root2 = 1 / (2 + root2)
    if len(str(root2.numerator + root2.denominator)) > len(str(root2.denominator)):
        count += 1

print(count)