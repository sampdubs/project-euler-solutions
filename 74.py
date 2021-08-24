from functools import cache
from tqdm import trange

@cache
def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1

@cache
def iterate(n):
    return sum(factorial(int(d)) for d in str(n))

def len_of_chain(n):
    chain = [n]
    while True:
        link = iterate(chain[-1])
        if link in chain:
            return len(chain)
        chain.append(link)

assert len_of_chain(69) == 5

count = 0
for n in trange(1, 1_000_000):
    count += len_of_chain(n) == 60
print(count)