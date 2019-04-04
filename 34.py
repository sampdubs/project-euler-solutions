facts = {0: 1, 1: 1, 2: 2}

def factorial(n):
    if n in facts:
        return facts[n]
    answer = n * factorial(n - 1)
    facts[n] = answer
    return answer

def curious(n):
    sum_of_facts = 0
    for i in str(n):
        sum_of_facts += factorial(int(i))
    return sum_of_facts == n

curiouses = []
for n in range(10, 3 * factorial(9)):
    if curious(n):
        curiouses.append(n)

print(sum(curiouses))