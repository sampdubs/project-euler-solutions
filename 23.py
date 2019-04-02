from functools import reduce

def sum_of_factors(n):
    return sum(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))) - n

def get_abundants(n):
    return [i for i in range(12, n) if sum_of_factors(i) > i]

all_as = get_abundants(28123)
all_sums = set()
for i in range(len(all_as)):
        for j in range(i, len(all_as)):
            all_sums.add(all_as[i] + all_as[j])
all_sums = list(all_sums)

not_sum_of_as = []
for n in range(1, 28123):
    if n not in all_sums:
        not_sum_of_as.append(n)


print(sum(not_sum_of_as))