from collections import defaultdict, Counter
import numpy as np

def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)

num_trips_by_sums = defaultdict(int)
n = 1_500_000
for trip in gen_prim_pyth_trips(n):
    this_sum = trip.sum()
    m = 1
    multiple = this_sum * m
    while multiple <= n:
        num_trips_by_sums[multiple] += 1
        m += 1
        multiple = this_sum * m

print(Counter(num_trips_by_sums.values())[1])
