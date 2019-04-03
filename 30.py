def is_sum_of_pows(num, pow):
    total = 0
    s_num = str(num)
    for d in s_num:
        total += int(d) ** pow
    return total == num

fith_nums = []
for n in range(10, 1000000):
    if is_sum_of_pows(n, 5):
        fith_nums.append(n)

print(sum(fith_nums))