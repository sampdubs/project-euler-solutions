from sympy import primerange
from sympy.ntheory.factor_ import totient
from tqdm import tqdm

def len_of_chain(n):
    if n == 1:
        return 1
    return 1 + len_of_chain(totient(n))

if __name__ == "__main__":
    total = 0
    for prime in tqdm(list(primerange(0, 40_000_000))): # generation of the primes takes a while (~1-2 minutes). Looping over the primes also takes a while (~20 minutes)
        if len_of_chain(prime) == 25:
            total += prime
    print(total) # 1677366278943