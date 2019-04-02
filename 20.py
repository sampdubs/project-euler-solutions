def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

fact_100 = str(factorial(100))
num_list = []
for n in fact_100:
    num_list.append(int(n))

print(sum(num_list))