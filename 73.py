from fractions import Fraction
from tqdm import trange, tqdm
from math import gcd

def cp(n):
    return [i for i in range(n) if gcd(n, i) < 2]

fracs = set()
for d in trange(2, 12001):
    for n in cp(d):
        fracs.add(Fraction(n, d))

good_fracs = []
for frac in tqdm(fracs):
    if frac > Fraction(1, 3) and frac < Fraction(1, 2):
        good_fracs.append(frac)

print(len(good_fracs))