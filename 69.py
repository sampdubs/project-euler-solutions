from numpy import argmax
from sympy import totient
from tqdm import trange

print(argmax([n/totient(n) for n in trange(1, 1_000_000)]) + 1)