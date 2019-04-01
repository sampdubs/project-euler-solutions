fib_nums = [1, 2]
even_sum = 0

while True:
    if fib_nums[-1] % 2 == 0:
        even_sum += fib_nums[-1]
    fib_nums.append(fib_nums[-1] + fib_nums[-2])
    if fib_nums[-1] > 4000000:
        break

print(fib_nums)
print(even_sum)