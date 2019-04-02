from functools import reduce

def d(n):
    return sum(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))) - n

num_to_facts = {}

for i in range(1, 10000):
    num_to_facts[i] = d(i)

amicable_nums = []

for num in num_to_facts:
    facts = num_to_facts[num]
    if facts in num_to_facts and facts != num:
        if num_to_facts[facts] == num:
            amicable_nums.append(num)

print(sum(amicable_nums))