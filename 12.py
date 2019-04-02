from functools import reduce
t_nums = [0]

def factors_of(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

while True:
    new = t_nums[-1] + len(t_nums)
    t_nums.append(new)
    num_factors = len(factors_of(new))
    if num_factors > 500:
        break

print(t_nums[-1])